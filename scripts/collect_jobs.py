#!/usr/bin/env python3
"""
Real Job Posting Collector for Agent-Ready Job Descriptions.
Fetches live job postings from Global ATS APIs (Ashby, Greenhouse, Lever)
and Korean platforms (Wanted API v4, Saramin, Toss, Karrot, etc.).
Any blocked, login-walled, or failed targets are logged to
raw-data/pending_aside_targets.json and raw-data/PENDING_ASIDE_CLI.md
for retry with `aside` CLI later.
"""

import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw-data"
KR_DIR = RAW_DIR / "kr"
GLOBAL_DIR = RAW_DIR / "global"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/html;q=0.9, */*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}

TIMEOUT = 15

ROLE_KEYWORDS: Dict[str, List[str]] = {
    "cmo-chief-marketing-officer": [
        "chief marketing officer", "cmo", "vp of marketing", "vp marketing",
        "head of marketing", "마케팅 총괄", "마케팅 본부장", "마케팅 리드", "마케팅 임원"
    ],
    "cro-chief-revenue-officer": [
        "chief revenue officer", "cro", "chief business officer", "cbo",
        "vp of sales", "vp revenue", "head of revenue", "사업 총괄", "세일즈 총괄", "비즈니스 총괄"
    ],
    "cpo-cto-product-tech-executive": [
        "chief product officer", "cpo", "chief technology officer", "cto",
        "vp of engineering", "vp engineering", "vp of product", "head of product", "기술 총괄", "프로덕트 총괄"
    ],
    "market-trend-consumer-researcher": [
        "market research", "consumer insights", "user research", "ux researcher",
        "competitive intelligence", "시장조사", "트렌드 리서치", "소비자 리서치", "리서처", "인사이트"
    ],
    "brand-marketer-strategist": [
        "brand marketing", "brand marketer", "brand strategy", "brand strategist",
        "브랜드 마케터", "브랜드 마케팅", "브랜드 전략", "캠페인 전략"
    ],
    "influencer-seeding-affiliate-marketer": [
        "influencer", "creator marketing", "creator partnerships", "affiliate",
        "kol", "seeding", "인플루언서", "크리에이터 마케팅", "시딩", "어필리에이트", "공구"
    ],
    "social-viral-community-marketer": [
        "social media", "community manager", "community marketing", "viral",
        "short-form", "tiktok", "소셜 미디어", "바이럴", "숏폼", "커뮤니티 매니저", "sns 마케터"
    ],
    "content-copywriter-creative": [
        "content marketing", "content marketer", "copywriter", "creative strategist",
        "editorial", "콘텐츠 마케터", "콘텐츠 마케팅", "카피라이터", "크리에이티브 디렉터"
    ],
    "seo-aeo-geo-marketer": [
        "seo", "search engine optimization", "aeo", "geo", "organic growth",
        "검색엔진 최적화", "오가닉 그로스"
    ],
    "growth-performance-marketer": [
        "performance marketing", "growth marketing", "growth marketer", "paid acquisition",
        "paid media", "user acquisition", "퍼포먼스 마케터", "퍼포먼스 마케팅", "그로스 마케터", "그로스 마케팅"
    ],
    "crm-lifecycle-retention-marketer": [
        "crm", "lifecycle marketing", "retention", "email marketing",
        "crm 마케터", "crm 마케팅", "라이프사이클", "리텐션 마케터"
    ],
    "pr-communications-event-marketer": [
        "public relations", "communications", "comms", "pr manager", "event marketing",
        "언론홍보", "pr 담당", "홍보", "커뮤니케이션", "웨비나", "이벤트 마케터"
    ],
    "b2b-sales-sdr-ae": [
        "account executive", "sales development", "sdr", "bdr", "enterprise sales",
        "b2b sales", "b2b 영업", "세일즈", "어카운트 이그제큐티브", "사업개발"
    ],
    "biz-ops-strategy-cos": [
        "chief of staff", "business operations", "bizops", "strategy & operations",
        "strategic operations", "전략기획", "비즈니스 오퍼레이션", "경영기획", "사업전략"
    ],
    "product-manager": [
        "product manager", "product owner", "technical product manager",
        "프로덕트 매니저", "서비스 기획", "pm", "po"
    ],
    "data-analyst-bi": [
        "data analyst", "analytics engineer", "business intelligence", "marketing analyst",
        "product analyst", "데이터 분석가", "데이터 애널리스트", "bi 분석"
    ],
    "product-creative-designer": [
        "product designer", "ui/ux", "brand designer", "creative designer", "bx designer",
        "프로덕트 디자이너", "브랜드 디자이너", "콘텐츠 디자이너", "bx 디자이너"
    ],
    "software-ai-engineer": [
        "software engineer", "ai engineer", "agent engineer", "forward deployed engineer",
        "context engineer", "machine learning engineer", "full stack", "backend engineer",
        "소프트웨어 엔지니어", "ai 엔지니어", "백엔드 개발", "프론트엔드 개발", "풀스택"
    ],
}


def strip_html(raw: Optional[str]) -> str:
    if not raw:
        return ""
    soup = BeautifulSoup(raw, "html.parser")
    text = soup.get_text(separator="\n")
    lines = [re.sub(r"\s+", " ", ln).strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def classify_roles(title: str, department: str = "", body: str = "") -> List[str]:
    text = f"{title} {department}".lower()
    matched: List[str] = []
    for role_id, kws in ROLE_KEYWORDS.items():
        for kw in kws:
            if len(kw) <= 3:
                if re.search(rf"(?<![a-z0-9]){re.escape(kw)}(?![a-z0-9])", text):
                    matched.append(role_id)
                    break
            elif kw in text:
                matched.append(role_id)
                break
    return matched


def fetch_ashby(company: str, board: str, pending: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    url = f"https://api.ashbyhq.com/posting-api/job-board/{board}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if resp.status_code != 200:
            pending.append({
                "source": "ashby",
                "company": company,
                "url": f"https://jobs.ashbyhq.com/{board}",
                "api_url": url,
                "region": "global",
                "reason": f"HTTP {resp.status_code}",
                "aside_cmd": f"aside fetch https://jobs.ashbyhq.com/{board} --output raw-data/global/ashby_{board}.json",
            })
            return []
        data = resp.json()
        jobs = data.get("jobs", [])
        results: List[Dict[str, Any]] = []
        for j in jobs:
            title = j.get("title", "")
            dept = j.get("department", "") or j.get("team", "")
            desc = strip_html(j.get("descriptionHtml") or j.get("descriptionPlain", ""))
            roles = classify_roles(title, dept, desc)
            if roles:
                results.append({
                    "source": "ashby",
                    "company": company,
                    "region": "global",
                    "id": str(j.get("id", "")),
                    "title": title,
                    "department": dept,
                    "location": j.get("location", ""),
                    "url": j.get("jobUrl") or f"https://jobs.ashbyhq.com/{board}/{j.get('id', '')}",
                    "matched_roles": roles,
                    "description_excerpt": desc[:3500],
                })
        return results
    except Exception as exc:
        pending.append({
            "source": "ashby",
            "company": company,
            "url": f"https://jobs.ashbyhq.com/{board}",
            "api_url": url,
            "region": "global",
            "reason": str(exc),
            "aside_cmd": f"aside fetch https://jobs.ashbyhq.com/{board} --output raw-data/global/ashby_{board}.json",
        })
        return []


def fetch_greenhouse(company: str, board: str, region: str, pending: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if resp.status_code != 200:
            pending.append({
                "source": "greenhouse",
                "company": company,
                "url": f"https://boards.greenhouse.io/{board}",
                "api_url": url,
                "region": region,
                "reason": f"HTTP {resp.status_code}",
                "aside_cmd": f"aside fetch https://boards.greenhouse.io/{board} --output raw-data/{region}/greenhouse_{board}.json",
            })
            return []
        data = resp.json()
        jobs = data.get("jobs", [])
        results: List[Dict[str, Any]] = []
        for j in jobs:
            title = j.get("title", "")
            depts = ", ".join(d.get("name", "") for d in j.get("departments", []))
            desc = strip_html(j.get("content", ""))
            roles = classify_roles(title, depts, desc)
            if roles:
                results.append({
                    "source": "greenhouse",
                    "company": company,
                    "region": region,
                    "id": str(j.get("id", "")),
                    "title": title,
                    "department": depts,
                    "location": (j.get("location") or {}).get("name", ""),
                    "url": j.get("absolute_url", ""),
                    "matched_roles": roles,
                    "description_excerpt": desc[:3500],
                })
        return results
    except Exception as exc:
        pending.append({
            "source": "greenhouse",
            "company": company,
            "url": f"https://boards.greenhouse.io/{board}",
            "api_url": url,
            "region": region,
            "reason": str(exc),
            "aside_cmd": f"aside fetch https://boards.greenhouse.io/{board} --output raw-data/{region}/greenhouse_{board}.json",
        })
        return []


def fetch_lever(company: str, board: str, pending: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    url = f"https://api.lever.co/v0/postings/{board}?mode=json"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if resp.status_code != 200:
            pending.append({
                "source": "lever",
                "company": company,
                "url": f"https://jobs.lever.co/{board}",
                "api_url": url,
                "region": "global",
                "reason": f"HTTP {resp.status_code}",
                "aside_cmd": f"aside fetch https://jobs.lever.co/{board} --output raw-data/global/lever_{board}.json",
            })
            return []
        jobs = resp.json()
        results: List[Dict[str, Any]] = []
        for j in jobs:
            title = j.get("text", "")
            cats = j.get("categories") or {}
            dept = f"{cats.get('department', '')} {cats.get('team', '')}".strip()
            desc = strip_html(j.get("description", "")) + "\n" + strip_html(
                "\n".join(lst.get("content", "") for lst in j.get("lists", []))
            )
            roles = classify_roles(title, dept, desc)
            if roles:
                results.append({
                    "source": "lever",
                    "company": company,
                    "region": "global",
                    "id": str(j.get("id", "")),
                    "title": title,
                    "department": dept,
                    "location": cats.get("location", ""),
                    "url": j.get("hostedUrl", ""),
                    "matched_roles": roles,
                    "description_excerpt": desc[:3500],
                })
        return results
    except Exception as exc:
        pending.append({
            "source": "lever",
            "company": company,
            "url": f"https://jobs.lever.co/{board}",
            "api_url": url,
            "region": "global",
            "reason": str(exc),
            "aside_cmd": f"aside fetch https://jobs.lever.co/{board} --output raw-data/global/lever_{board}.json",
        })
        return []


def fetch_wanted_kr(pending: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Fetch KR jobs from Wanted public API v4 across marketing, business, PM, design, data, dev."""
    queries = [
        ("마케팅", 523),
        ("브랜드 마케터", 523),
        ("퍼포먼스 마케터", 523),
        ("인플루언서", 523),
        ("CRM 마케터", 523),
        ("콘텐츠 마케터", 523),
        ("리서치", 507),
        ("B2B 영업", 507),
        ("전략기획", 507),
        ("프로덕트 매니저", 518),
        ("데이터 분석가", 518),
        ("프로덕트 디자이너", 511),
        ("AI 엔지니어", 518),
    ]
    seen_ids = set()
    results: List[Dict[str, Any]] = []
    wanted_headers = {**HEADERS, "Referer": "https://www.wanted.co.kr/"}

    for kw, tag_id in queries:
        list_url = f"https://www.wanted.co.kr/api/v4/jobs?country=kr&query={quote_plus(kw)}&limit=15&job_sort=job.latest_order"
        try:
            resp = requests.get(list_url, headers=wanted_headers, timeout=TIMEOUT)
            if resp.status_code != 200:
                # Fallback to tag_type_ids endpoint
                list_url2 = f"https://www.wanted.co.kr/api/v4/jobs?country=kr&tag_type_ids={tag_id}&limit=15"
                resp = requests.get(list_url2, headers=wanted_headers, timeout=TIMEOUT)
            if resp.status_code != 200:
                pending.append({
                    "source": "wanted",
                    "company": f"Wanted Query: {kw}",
                    "url": f"https://www.wanted.co.kr/search?query={quote_plus(kw)}",
                    "api_url": list_url,
                    "region": "kr",
                    "reason": f"HTTP {resp.status_code}",
                    "aside_cmd": f"aside fetch 'https://www.wanted.co.kr/search?query={quote_plus(kw)}' --output raw-data/kr/wanted_{kw}.json",
                })
                continue

            data = resp.json()
            jobs = data.get("data", [])
            for item in jobs[:6]:
                jid = item.get("id")
                if not jid or jid in seen_ids:
                    continue
                seen_ids.add(jid)
                title = item.get("position", "")
                company = (item.get("company") or {}).get("name", "")
                detail_url = f"https://www.wanted.co.kr/api/v4/jobs/{jid}"
                desc_parts = []
                try:
                    dresp = requests.get(detail_url, headers=wanted_headers, timeout=TIMEOUT)
                    if dresp.status_code == 200:
                        job_obj = (dresp.json() or {}).get("job", {})
                        detail = job_obj.get("detail") or {}
                        for k in ["intro", "main_tasks", "requirements", "preferred_points"]:
                            if detail.get(k):
                                desc_parts.append(f"[{k}]\n{detail[k]}")
                except Exception:
                    pass
                desc = "\n\n".join(desc_parts)
                roles = classify_roles(title, kw, desc)
                if not roles:
                    # Fallback mapping by query keyword
                    roles = classify_roles(kw, "", "")
                results.append({
                    "source": "wanted",
                    "company": company,
                    "region": "kr",
                    "id": str(jid),
                    "title": title,
                    "department": kw,
                    "location": (item.get("address") or {}).get("location", "KR"),
                    "url": f"https://www.wanted.co.kr/wd/{jid}",
                    "matched_roles": roles,
                    "description_excerpt": desc[:3500],
                })
                time.sleep(0.15)
        except Exception as exc:
            pending.append({
                "source": "wanted",
                "company": f"Wanted Query: {kw}",
                "url": f"https://www.wanted.co.kr/search?query={quote_plus(kw)}",
                "api_url": list_url,
                "region": "kr",
                "reason": str(exc),
                "aside_cmd": f"aside fetch 'https://www.wanted.co.kr/search?query={quote_plus(kw)}' --output raw-data/kr/wanted_{kw}.json",
            })
    return results


def fetch_toss_kr(pending: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    url = "https://api-public.toss.im/api/v3/ipd-eggnog/career/jobs"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if resp.status_code != 200:
            pending.append({
                "source": "toss-careers",
                "company": "Toss (Viva Republica)",
                "url": "https://toss.im/career/jobs",
                "api_url": url,
                "region": "kr",
                "reason": f"HTTP {resp.status_code}",
                "aside_cmd": "aside fetch https://toss.im/career/jobs --output raw-data/kr/toss_jobs.json",
            })
            return []
        payload = resp.json()
        jobs = payload.get("success", []) if isinstance(payload, dict) else payload
        if not isinstance(jobs, list):
            jobs = []
        results: List[Dict[str, Any]] = []
        for j in jobs:
            title = j.get("title", "")
            dept = j.get("subsidiary", "") or j.get("category", "")
            roles = classify_roles(title, str(dept), "")
            if roles:
                results.append({
                    "source": "toss-careers",
                    "company": f"Toss ({j.get('subsidiary', 'Toss')})",
                    "region": "kr",
                    "id": str(j.get("id", "")),
                    "title": title,
                    "department": str(dept),
                    "location": "Seoul, KR",
                    "url": f"https://toss.im/career/job-detail?job_id={j.get('id', '')}",
                    "matched_roles": roles,
                    "description_excerpt": strip_html(str(j.get("summary", "") or j.get("description", "")))[:2000],
                })
        return results
    except Exception as exc:
        pending.append({
            "source": "toss-careers",
            "company": "Toss (Viva Republica)",
            "url": "https://toss.im/career/jobs",
            "api_url": url,
            "region": "kr",
            "reason": str(exc),
            "aside_cmd": "aside fetch https://toss.im/career/jobs --output raw-data/kr/toss_jobs.json",
        })
        return []


def fetch_saramin_kr(pending: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    keywords = ["마케팅", "브랜드 마케터", "인플루언서", "리서치", "B2B 영업", "CMO"]
    results: List[Dict[str, Any]] = []
    seen = set()
    for kw in keywords:
        url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword={quote_plus(kw)}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            if resp.status_code != 200 or "Access Denied" in resp.text or len(resp.text) < 2000:
                pending.append({
                    "source": "saramin",
                    "company": f"Saramin Search: {kw}",
                    "url": url,
                    "api_url": url,
                    "region": "kr",
                    "reason": f"HTTP {resp.status_code} / Anti-bot or thin HTML ({len(resp.text)} bytes)",
                    "aside_cmd": f"aside fetch '{url}' --output raw-data/kr/saramin_{kw}.json",
                })
                continue
            soup = BeautifulSoup(resp.text, "html.parser")
            items = soup.select(".item_recruit")
            if not items:
                pending.append({
                    "source": "saramin",
                    "company": f"Saramin Search: {kw}",
                    "url": url,
                    "api_url": url,
                    "region": "kr",
                    "reason": "Dynamic JS rendering or selector mismatch (0 .item_recruit nodes)",
                    "aside_cmd": f"aside fetch '{url}' --output raw-data/kr/saramin_{kw}.json",
                })
                continue
            for it in items[:8]:
                a_tag = it.select_one(".job_tit a")
                comp_tag = it.select_one(".corp_name a")
                cond_tags = [c.get_text(strip=True) for c in it.select(".job_condition span")]
                sector_tags = [s.get_text(strip=True) for s in it.select(".job_sector a")]
                if not a_tag:
                    continue
                title = a_tag.get_text(strip=True)
                href = a_tag.get("href", "")
                if href.startswith("/"):
                    href = "https://www.saramin.co.kr" + href
                if href in seen:
                    continue
                seen.add(href)
                company = comp_tag.get_text(strip=True) if comp_tag else "Unknown"
                roles = classify_roles(title, kw + " " + " ".join(sector_tags), "")
                if not roles:
                    roles = classify_roles(kw, "", "")
                results.append({
                    "source": "saramin",
                    "company": company,
                    "region": "kr",
                    "id": href.split("rec_idx=")[-1].split("&")[0],
                    "title": title,
                    "department": ", ".join(sector_tags[:5]),
                    "location": cond_tags[0] if cond_tags else "KR",
                    "url": href,
                    "matched_roles": roles,
                    "description_excerpt": f"Conditions: {' | '.join(cond_tags)}\nSectors: {', '.join(sector_tags)}",
                })
        except Exception as exc:
            pending.append({
                "source": "saramin",
                "company": f"Saramin Search: {kw}",
                "url": url,
                "api_url": url,
                "region": "kr",
                "reason": str(exc),
                "aside_cmd": f"aside fetch '{url}' --output raw-data/kr/saramin_{kw}.json",
            })
    return results


def default_gated_aside_targets() -> List[Dict[str, Any]]:
    """Platforms known to require login, JS rendering, or aside CLI."""
    return [
        {
            "source": "remember-career",
            "company": "Remember Career (리멤버 커리어 - 시니어/C레벨)",
            "url": "https://career.rememberapp.co.kr/job/postings",
            "api_url": "N/A (Login/SPA gated)",
            "region": "kr",
            "reason": "Requires authenticated session / dynamic SPA rendering (queued for aside CLI)",
            "aside_cmd": "aside fetch https://career.rememberapp.co.kr/job/postings --render --output raw-data/kr/remember_postings.json",
        },
        {
            "source": "linkedin-jobs",
            "company": "LinkedIn Jobs (Global C-Level / Marketing / AI)",
            "url": "https://www.linkedin.com/jobs/search/?keywords=Chief%20Marketing%20Officer%20OR%20Influencer%20Marketing",
            "api_url": "N/A (Auth-walled)",
            "region": "global",
            "reason": "Requires authenticated session (queued for aside CLI)",
            "aside_cmd": "aside fetch 'https://www.linkedin.com/jobs/search/?keywords=CMO%20OR%20Brand%20Marketing' --output raw-data/global/linkedin_jobs.json",
        },
        {
            "source": "karrot-careers",
            "company": "Karrot (당근마켓 채용)",
            "url": "https://about.daangn.com/jobs/",
            "api_url": "https://about.daangn.com/jobs/",
            "region": "kr",
            "reason": "Next.js / Greenhouse hybrid SPA; queued for aside CLI deep extraction",
            "aside_cmd": "aside fetch https://about.daangn.com/jobs/ --render --output raw-data/kr/karrot_jobs.json",
        },
        {
            "source": "jumpit",
            "company": "Jumpit (점핏 - IT/개발/데이터/PM)",
            "url": "https://www.jumpit.co.kr/positions",
            "api_url": "https://api.jumpit.co.kr/api/positions",
            "region": "kr",
            "reason": "SPA / header-protected endpoint; queued for aside CLI verification",
            "aside_cmd": "aside fetch https://www.jumpit.co.kr/positions --render --output raw-data/kr/jumpit_jobs.json",
        },
    ]


def write_pending_markdown(pending: List[Dict[str, Any]]) -> None:
    lines = [
        "# Pending Targets for `aside` CLI (`PENDING_ASIDE_CLI.md`)",
        "",
        f"- **Generated At:** {datetime.now(timezone.utc).isoformat()}",
        f"- **Total Pending Targets:** {len(pending)}",
        "- **Why Pending:** 로컬 환경에 `aside` CLI가 아직 설치되어 있지 않으며, 아래 타겟들은 로그인 월(Auth-wall), 봇 차단(HTTP 403/404), 또는 동적 SPA 렌더링이 필요해 기본 HTTP 수집에서 제외/실패되었습니다.",
        "",
        "## 집에서 `aside` CLI 세팅 후 재수집 실행 방법",
        "",
        "```bash",
        "# 1. aside CLI 설치/경로 확인",
        "which aside",
        "",
        "# 2. 준비된 자동 재수집 스크립트 실행",
        "python3 scripts/retry_with_aside.py",
        "```",
        "",
        "## 대기 중인 수집 타겟 목록",
        "",
        "| Region | Source | Company / Query | Reason | Target URL | Recommended `aside` Command |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for item in pending:
        reason = str(item.get("reason", "")).replace("|", "/")[:90]
        cmd = str(item.get("aside_cmd", "")).replace("|", "/")
        lines.append(
            f"| `{item.get('region', '')}` | `{item.get('source', '')}` | {item.get('company', '')} | {reason} | {item.get('url', '')} | `{cmd}` |"
        )
    (RAW_DIR / "PENDING_ASIDE_CLI.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    KR_DIR.mkdir(parents=True, exist_ok=True)
    GLOBAL_DIR.mkdir(parents=True, exist_ok=True)

    pending: List[Dict[str, Any]] = []
    all_global: List[Dict[str, Any]] = []
    all_kr: List[Dict[str, Any]] = []

    ashby_boards = [
        ("OpenAI", "openai"),
        ("Linear", "linear"),
        ("Ramp", "ramp"),
        ("Perplexity", "perplexity"),
        ("Notion", "notion"),
        ("ElevenLabs", "elevenlabs"),
        ("Sierra", "sierra"),
        ("Supabase", "supabase"),
        ("Cohere", "cohere"),
        ("Cursor (Anysphere)", "anysphere"),
    ]

    greenhouse_boards = [
        ("Anthropic", "anthropic", "global"),
        ("Stripe", "stripe", "global"),
        ("Airbnb", "airbnb", "global"),
        ("Scale AI", "scaleai", "global"),
        ("Figma", "figma", "global"),
        ("Vercel", "vercel", "global"),
        ("Glean", "glean", "global"),
        ("Reddit", "reddit", "global"),
        ("Coupang", "coupang", "kr"),
        ("Sendbird", "sendbird", "kr"),
    ]

    lever_boards = [
        ("Palantir", "palantir"),
        ("Mistral AI", "mistral"),
    ]

    print("[1/5] Fetching Ashby global boards...")
    for comp, board in ashby_boards:
        jobs = fetch_ashby(comp, board, pending)
        if jobs:
            (GLOBAL_DIR / f"ashby_{board}.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
            all_global.extend(jobs)
        print(f"  - {comp} ({board}): {len(jobs)} matched postings")

    print("[2/5] Fetching Greenhouse boards...")
    for comp, board, region in greenhouse_boards:
        jobs = fetch_greenhouse(comp, board, region, pending)
        if jobs:
            target_dir = KR_DIR if region == "kr" else GLOBAL_DIR
            (target_dir / f"greenhouse_{board}.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
            if region == "kr":
                all_kr.extend(jobs)
            else:
                all_global.extend(jobs)
        print(f"  - {comp} ({board}, {region}): {len(jobs)} matched postings")

    print("[3/5] Fetching Lever global boards...")
    for comp, board in lever_boards:
        jobs = fetch_lever(comp, board, pending)
        if jobs:
            (GLOBAL_DIR / f"lever_{board}.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
            all_global.extend(jobs)
        print(f"  - {comp} ({board}): {len(jobs)} matched postings")

    print("[4/5] Fetching Wanted KR & Toss KR...")
    wanted_jobs = fetch_wanted_kr(pending)
    if wanted_jobs:
        (KR_DIR / "wanted_kr.json").write_text(json.dumps(wanted_jobs, ensure_ascii=False, indent=2), encoding="utf-8")
        all_kr.extend(wanted_jobs)
    print(f"  - Wanted KR: {len(wanted_jobs)} matched postings")

    toss_jobs = fetch_toss_kr(pending)
    if toss_jobs:
        (KR_DIR / "toss_kr.json").write_text(json.dumps(toss_jobs, ensure_ascii=False, indent=2), encoding="utf-8")
        all_kr.extend(toss_jobs)
    print(f"  - Toss KR: {len(toss_jobs)} matched postings")

    print("[5/5] Fetching Saramin KR & logging gated targets...")
    saramin_jobs = fetch_saramin_kr(pending)
    if saramin_jobs:
        (KR_DIR / "saramin_kr.json").write_text(json.dumps(saramin_jobs, ensure_ascii=False, indent=2), encoding="utf-8")
        all_kr.extend(saramin_jobs)
    print(f"  - Saramin KR: {len(saramin_jobs)} matched postings")

    # Add known auth/SPA gated targets for aside CLI
    pending.extend(default_gated_aside_targets())

    # Build per-role index
    by_role: Dict[str, Dict[str, List[Dict[str, str]]]] = {
        r: {"kr": [], "global": []} for r in ROLE_KEYWORDS
    }
    for job in all_kr + all_global:
        region = job["region"]
        entry = {
            "company": job["company"],
            "title": job["title"],
            "source": job["source"],
            "url": job["url"],
            "excerpt": job.get("description_excerpt", "")[:500],
        }
        for r in job.get("matched_roles", []):
            if r in by_role:
                by_role[r][region].append(entry)

    (RAW_DIR / "by_role_index.json").write_text(json.dumps(by_role, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_kr_postings": len(all_kr),
        "total_global_postings": len(all_global),
        "total_postings": len(all_kr) + len(all_global),
        "pending_aside_targets_count": len(pending),
        "role_counts": {
            r: {"kr": len(v["kr"]), "global": len(v["global"])} for r, v in by_role.items()
        },
    }
    (RAW_DIR / "collection_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (RAW_DIR / "pending_aside_targets.json").write_text(json.dumps(pending, ensure_ascii=False, indent=2), encoding="utf-8")
    write_pending_markdown(pending)

    print("\n=== COLLECTION COMPLETE ===")
    print(json.dumps({
        "total_kr": len(all_kr),
        "total_global": len(all_global),
        "pending_for_aside_cli": len(pending),
    }, indent=2))


if __name__ == "__main__":
    main()
