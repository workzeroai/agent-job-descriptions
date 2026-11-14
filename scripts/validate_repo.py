#!/usr/bin/env python3
"""
Repository integrity validator for agent-job-descriptions.
Checks:
  1. taxonomy.yaml loads and defines all expected roles & categories.
  2. Every role in taxonomy.yaml has:
       - roles/{category}/{role_id}.md
       - specs/{category}/{role_id}.agent.yaml
       - specs/{category}/{role_id}.agent.json
  3. YAML and JSON specs match each other and conform strictly to schemas/agent-spec.schema.json.
  4. All inter-agent references (compatible_agents, upstream_agents, downstream_agents)
     resolve to valid role_ids in taxonomy.yaml (or recognized external/human markers).
  5. Seniority levels, overlays, workflows, and raw-data/PENDING_ASIDE_CLI.md exist.
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent


def validate_against_schema(spec: Dict[str, Any], schema: Dict[str, Any], role_id: str) -> List[str]:
    errors: List[str] = []
    for req_key in schema.get("required", []):
        if req_key not in spec:
            errors.append(f"[{role_id}] Missing required top-level key: {req_key}")

    if spec.get("role_id") != role_id:
        errors.append(f"[{role_id}] role_id mismatch: {spec.get('role_id')}")

    if not re.match(r"^[a-z0-9-]+$", str(spec.get("role_id", ""))):
        errors.append(f"[{role_id}] Invalid role_id pattern")

    valid_cats = schema["properties"]["category"]["enum"]
    if spec.get("category") not in valid_cats:
        errors.append(f"[{role_id}] Invalid category: {spec.get('category')}")

    # Seniority modes
    sm = spec.get("seniority_modes", {})
    for tier in ["l1_worker", "l2_specialist", "l3_orchestrator", "l4_executive"]:
        if tier not in sm:
            errors.append(f"[{role_id}] Missing seniority_modes.{tier}")
        else:
            for k in ["archetype", "autonomy_level", "scope", "system_prompt"]:
                if not sm[tier].get(k):
                    errors.append(f"[{role_id}] Empty seniority_modes.{tier}.{k}")

    # Compute environment
    ce = spec.get("compute_environment", {})
    for k in ["runtime", "execution_model", "sandbox_level"]:
        if k not in ce:
            errors.append(f"[{role_id}] Missing compute_environment.{k}")
    if ce.get("execution_model") not in schema["properties"]["compute_environment"]["properties"]["execution_model"]["enum"]:
        errors.append(f"[{role_id}] Invalid execution_model: {ce.get('execution_model')}")
    if ce.get("sandbox_level") not in schema["properties"]["compute_environment"]["properties"]["sandbox_level"]["enum"]:
        errors.append(f"[{role_id}] Invalid sandbox_level: {ce.get('sandbox_level')}")

    # Cross validation sources
    cvs = spec.get("cross_validation_sources", {})
    for k in ["kr", "global", "consensus_core_tasks"]:
        if not isinstance(cvs.get(k), list) or len(cvs[k]) == 0:
            errors.append(f"[{role_id}] cross_validation_sources.{k} must be a non-empty list")

    # Tools & MCPs
    tm = spec.get("tools_and_mcps", {})
    for k in ["cli_tools", "mcp_servers", "saas_and_apis"]:
        if not isinstance(tm.get(k), list):
            errors.append(f"[{role_id}] tools_and_mcps.{k} must be a list")

    # IO contract
    ioc = spec.get("io_contract", {})
    for k in ["inputs", "outputs", "upstream_agents", "downstream_agents", "compatible_agents"]:
        if not isinstance(ioc.get(k), list):
            errors.append(f"[{role_id}] io_contract.{k} must be a list")

    # Workflows
    wf = spec.get("workflows", {})
    for k in ["routine_cron", "event_triggered"]:
        if not isinstance(wf.get(k), list) or len(wf[k]) == 0:
            errors.append(f"[{role_id}] workflows.{k} must be a non-empty list")

    # Guardrails
    gr = spec.get("guardrails", {})
    for k in ["autonomous", "human_approval_required", "prohibited"]:
        if not isinstance(gr.get(k), list) or len(gr[k]) == 0:
            errors.append(f"[{role_id}] guardrails.{k} must be a non-empty list")

    # KPIs
    kpis = spec.get("kpis", [])
    if not isinstance(kpis, list) or len(kpis) == 0:
        errors.append(f"[{role_id}] kpis must be a non-empty list")

    # Domain overlays
    do = spec.get("domain_overlays", {})
    for k in ["fintech", "ecommerce_d2c", "b2b_saas", "ai_native"]:
        if not do.get(k):
            errors.append(f"[{role_id}] Missing domain_overlays.{k}")

    return errors



def audit_markdown_files() -> List[str]:
    """Check all Markdown files for CommonMark delimiter bugs, broken nested-bracket links, raw HTML, and table/code errors."""
    md_errors: List[str] = []
    for md_path in sorted(BASE_DIR.rglob("*.md")):
        rel = md_path.relative_to(BASE_DIR)
        lines = md_path.read_text(encoding="utf-8").splitlines()
        in_code = False
        for i, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if re.search(r"</?(details|summary|strong|code|br)[^>]*>", line):
                md_errors.append(f"[MD_HTML] {rel}:{i}: raw HTML tag found")
            if re.search(r"\[[^\]]*\[[^\]]*\][^\]]*\]\([^\)]+\)", line):
                md_errors.append(f"[MD_LINK] {rel}:{i}: nested brackets inside link text")
            if line.count("`") % 2 != 0:
                md_errors.append(f"[MD_BACKTICK] {rel}:{i}: unbalanced backticks")
            if line.count("**") % 2 != 0:
                md_errors.append(f"[MD_BOLD_COUNT] {rel}:{i}: unbalanced **")
            if line.strip().startswith("|") and line.strip().endswith("|"):
                cols = line.count("|") - 1
                if i > 1 and lines[i - 2].strip().startswith("|"):
                    prev_cols = lines[i - 2].count("|") - 1
                    if cols != prev_cols:
                        md_errors.append(f"[MD_TABLE] {rel}:{i}: column count {cols} != {prev_cols}")
            for m in re.finditer(r"(\S?)\*\*(.+?)\*\*(\S?)", line):
                pre, inner, post = m.group(1), m.group(2), m.group(3)
                if pre and re.match(r"[^\w가-힣]", inner[0]):
                    md_errors.append(f"[MD_LEFT_BOLD] {rel}:{i}: {pre}**{inner}**")
                if post and re.match(r"[^\w가-힣]", inner[-1]):
                    md_errors.append(f"[MD_RIGHT_BOLD] {rel}:{i}: **{inner}**{post}")
            cleaned = re.sub(r"\*\*.*?\*\*", "", line)
            for m in re.finditer(r"(\S?)\*([^\*\s][^\*]*?)\*(\S?)", cleaned):
                pre, inner, post = m.group(1), m.group(2), m.group(3)
                if post and re.match(r"[^\w가-힣]", inner[-1]) and re.match(r"[\w가-힣]", post):
                    md_errors.append(f"[MD_RIGHT_ITALIC] {rel}:{i}: *{inner}*{post}")
        if in_code:
            md_errors.append(f"[MD_CODE_BLOCK] {rel}: unclosed code fence")
    return md_errors


def main() -> int:
    errors: List[str] = []

    taxonomy_path = BASE_DIR / "taxonomy.yaml"
    schema_path = BASE_DIR / "schemas" / "agent-spec.schema.json"
    if not taxonomy_path.exists():
        print("FATAL: taxonomy.yaml missing")
        return 1
    if not schema_path.exists():
        print("FATAL: schemas/agent-spec.schema.json missing")
        return 1

    taxonomy = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    all_role_ids: Set[str] = set()
    role_entries: List[tuple] = []
    for cat, info in taxonomy.get("categories", {}).items():
        for r in info.get("roles", []):
            rid = r["role_id"]
            all_role_ids.add(rid)
            role_entries.append((cat, rid))

    print(f"Found {len(role_entries)} roles in taxonomy.yaml")

    for cat, rid in role_entries:
        md_path = BASE_DIR / "roles" / cat / f"{rid}.md"
        yaml_path = BASE_DIR / "specs" / cat / f"{rid}.agent.yaml"
        json_path = BASE_DIR / "specs" / cat / f"{rid}.agent.json"

        for p in [md_path, yaml_path, json_path]:
            if not p.exists():
                errors.append(f"Missing file: {p.relative_to(BASE_DIR)}")

        if md_path.exists():
            md_text = md_path.read_text(encoding="utf-8")
            for section in ["## 1.", "## 2.", "## 3.", "## 4.", "## 5.", "## 6.", "## 7.", "## 8.", "## 9."]:
                if section not in md_text:
                    errors.append(f"[{rid}] Markdown missing section {section}")

        if yaml_path.exists() and json_path.exists():
            try:
                y_data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
                j_data = json.loads(json_path.read_text(encoding="utf-8"))
                if y_data != j_data:
                    errors.append(f"[{rid}] YAML and JSON spec contents do not match")
                errors.extend(validate_against_schema(j_data, schema, rid))

                ioc = j_data.get("io_contract", {})
                for ref_list_name in ["upstream_agents", "downstream_agents", "compatible_agents"]:
                    for ref in ioc.get(ref_list_name, []):
                        if ref not in all_role_ids:
                            errors.append(f"[{rid}] Invalid role reference in {ref_list_name}: {ref}")
            except Exception as exc:
                errors.append(f"[{rid}] Parse error: {exc}")

    # Check supporting directories and aside fallback queue
    required_files = [
        "README.md",
        "workflows/full-marketing-engine.yaml",
        "raw-data/PENDING_ASIDE_CLI.md",
        "raw-data/pending_aside_targets.json",
        "scripts/collect_jobs.py",
        "scripts/retry_with_aside.py",
    ]
    for rf in required_files:
        if not (BASE_DIR / rf).exists():
            errors.append(f"Missing required repo file: {rf}")

    errors.extend(audit_markdown_files())

    if errors:
        print(f"\nVALIDATION FAILED with {len(errors)} errors:")
        for e in errors:
            print("  -", e)
        return 1

    print(f"\nVALIDATION PASSED: {len(role_entries)}/{len(role_entries)} roles verified (Markdown + YAML + JSON + Inter-Agent Graph).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
