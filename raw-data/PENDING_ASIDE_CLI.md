# Pending Targets for `aside` CLI (`PENDING_ASIDE_CLI.md`)

- **Generated At:** 2026-11-13T08:13:24.719209+00:00
- **Total Pending Targets:** 7
- **Why Pending:** 로컬 환경에 `aside` CLI가 아직 설치되어 있지 않으며, 아래 타겟들은 로그인 월(Auth-wall), 봇 차단(HTTP 403/404), 또는 동적 SPA 렌더링이 필요해 기본 HTTP 수집에서 제외/실패되었습니다.

## 집에서 `aside` CLI 세팅 후 재수집 실행 방법

```bash
# 1. aside CLI 설치/경로 확인
which aside

# 2. 준비된 자동 재수집 스크립트 실행
python3 scripts/retry_with_aside.py
```

## 대기 중인 수집 타겟 목록

| Region | Source | Company / Query | Reason | Target URL | Recommended `aside` Command |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `global` | `ashby` | Cursor (Anysphere) | HTTP 404 | https://jobs.ashbyhq.com/anysphere | `aside fetch https://jobs.ashbyhq.com/anysphere --output raw-data/global/ashby_anysphere.json` |
| `global` | `greenhouse` | Glean | HTTP 404 | https://boards.greenhouse.io/glean | `aside fetch https://boards.greenhouse.io/glean --output raw-data/global/greenhouse_glean.json` |
| `global` | `lever` | Mistral AI | HTTP 404 | https://jobs.lever.co/mistral | `aside fetch https://jobs.lever.co/mistral --output raw-data/global/lever_mistral.json` |
| `kr` | `remember-career` | Remember Career (리멤버 커리어 - 시니어/C레벨) | Requires authenticated session / dynamic SPA rendering (queued for aside CLI) | https://career.rememberapp.co.kr/job/postings | `aside fetch https://career.rememberapp.co.kr/job/postings --render --output raw-data/kr/remember_postings.json` |
| `global` | `linkedin-jobs` | LinkedIn Jobs (Global C-Level / Marketing / AI) | Requires authenticated session (queued for aside CLI) | https://www.linkedin.com/jobs/search/?keywords=Chief%20Marketing%20Officer%20OR%20Influencer%20Marketing | `aside fetch 'https://www.linkedin.com/jobs/search/?keywords=CMO%20OR%20Brand%20Marketing' --output raw-data/global/linkedin_jobs.json` |
| `kr` | `karrot-careers` | Karrot (당근마켓 채용) | Next.js / Greenhouse hybrid SPA; queued for aside CLI deep extraction | https://about.daangn.com/jobs/ | `aside fetch https://about.daangn.com/jobs/ --render --output raw-data/kr/karrot_jobs.json` |
| `kr` | `jumpit` | Jumpit (점핏 - IT/개발/데이터/PM) | SPA / header-protected endpoint; queued for aside CLI verification | https://www.jumpit.co.kr/positions | `aside fetch https://www.jumpit.co.kr/positions --render --output raw-data/kr/jumpit_jobs.json` |
