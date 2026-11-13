#!/usr/bin/env python3
"""
Retry blocked / SPA / auth-gated job sources using `aside` CLI.
Run this script once `aside` CLI is installed and configured on your machine:
    python3 scripts/retry_with_aside.py
"""

import json
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PENDING_FILE = BASE_DIR / "raw-data" / "pending_aside_targets.json"


def main() -> int:
    aside_bin = shutil.which("aside")
    if not aside_bin:
        print("[ERROR] `aside` CLI was not found in PATH.")
        print("Please install or configure `aside` CLI first, then re-run:")
        print("    python3 scripts/retry_with_aside.py")
        return 1

    if not PENDING_FILE.exists():
        print(f"[INFO] No pending targets file found at {PENDING_FILE}")
        return 0

    targets = json.loads(PENDING_FILE.read_text(encoding="utf-8"))
    print(f"[INFO] Found {len(targets)} pending targets. Using aside at: {aside_bin}")

    succeeded = []
    still_failed = []

    for idx, item in enumerate(targets, 1):
        cmd_str = item.get("aside_cmd", "")
        if not cmd_str:
            continue
        print(f"[{idx}/{len(targets)}] Running: {cmd_str}")
        try:
            args = shlex.split(cmd_str)
            proc = subprocess.run(args, cwd=BASE_DIR, capture_output=True, text=True, timeout=60)
            if proc.returncode == 0:
                print(f"  -> OK: {item.get('company')}")
                succeeded.append(item)
            else:
                print(f"  -> FAILED (code {proc.returncode}): {proc.stderr.strip()[:200]}")
                item["last_retry_error"] = proc.stderr.strip()[:300]
                still_failed.append(item)
        except Exception as exc:
            print(f"  -> EXCEPTION: {exc}")
            item["last_retry_error"] = str(exc)
            still_failed.append(item)

    PENDING_FILE.write_text(json.dumps(still_failed, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nDone. Succeeded: {len(succeeded)}, Remaining pending: {len(still_failed)}")
    return 0 if not still_failed else 2


if __name__ == "__main__":
    sys.exit(main())
