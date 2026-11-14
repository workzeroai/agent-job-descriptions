# Agent-Ready Job Descriptions (`agent-job-descriptions`)

클라우드 컴퓨팅과 실행 환경(Shell, Browser, MCP, API)을 부여받은 AI 에이전트들을 **실제 회사 조직과 동일한 직무·직급·도메인 체계**로 설계하고 오케스트레이션하기 위한 **표준 직무기술서(Agent-Ready JD) 레포지토리**입니다.

국내(원티드, 사람인, 토스, 쿠팡, 센드버드 등)와 해외(OpenAI, Anthropic, Stripe, Ramp, Perplexity, Notion, ElevenLabs, Linear, Figma, Vercel, Airbnb 등)의 **실제 최신 채용 공고 원문을 수집·교차검증**하여, 사람용 HR 수사구를 제거하고 에이전트 시스템 프롬프트·I/O 규격·권한 가드레일로 변환했습니다.

> 📱 **모바일에서 읽으시나요?** 가로 스크롤 없는 세로 카드형 통합 문서 [**`MOBILE_READER.md` 바로 보기**](MOBILE_READER.md)를 추천합니다!

---

## 핵심 설계 철학

1. **100% 자율 마케팅 엔진 + 전사 호환 (Interoperable Agent Suite)**
   - **C-Level (3)** → **Marketing & Research (9)** → **Business/Sales/Ops (2)** → **Product/Data/Design/AI Tech (4)** 총 **18개 직무**가 동일한 `io_contract`로 연결됩니다.
   - 리서치 → 브랜드 전략 → 카피/크리에이티브 → 퍼포먼스/인플루언서 시딩/바이럴 숏폼/SEO·AEO/PR → CRM 리텐션/B2B 세일즈 → 데이터 어트리뷰션까지 마케팅 전 주기를 에이전트 파이프라인으로 돌릴 수 있습니다.
2. **직급 = 에이전트 계층 (4-Tier Seniority Architecture)**
   - `L1 Junior` (`Execution Worker`): 명확한 SOP 기반 실행, 데이터 수집, 초안 작성
   - `L2 Senior` (`Autonomous Specialist & Critic`): 가설·실험 설계, 트러블슈팅, L1 산출물 품질 검수
   - `L3 Lead/Head` (`Squad Orchestrator`): 목표 분해, 워커 에이전트 배분, 크로스 펑셔널 조율
   - `L4 C-Level` (`Executive Governor`): 전사 OKR·예산·리스크 거버넌스
3. **모듈형 보정 (Composable Overlays)**
   - 어떤 직무에도 `도메인(Fintech / E-Commerce D2C / B2B SaaS / AI-Native / Consumer App)` + `기업 단계(0→1 Startup / Scale-up / Big Tech)` + `로컬(KR / Global US)` 모듈을 조합해 주입할 수 있습니다.
4. **Dual Format (Markdown + YAML/JSON)**
   - 사람/아키텍트 가독용 `roles/{category}/{role_id}.md`
   - 에이전트 런타임/프레임워크 주입용 `specs/{category}/{role_id}.agent.yaml` & `.agent.json`

---

## 레포지토리 구조

```text
agent-job-descriptions/
├── README.md
├── taxonomy.yaml                          # 18개 직무·4단계 직급·오버레이 마스터 인덱스
├── schemas/
│   ├── agent-spec.schema.json             # YAML/JSON 에이전트 스펙 표준 JSON Schema
│   └── role-template.md                   # 직무기술서 Markdown 표준 템플릿
├── workflows/
│   └── full-marketing-engine.yaml         # CMO + 9개 마케팅 + BI/디자인/세일즈 연동 블루프린트
├── seniority-levels/                      # 직급별 에이전트 행동/권한 모듈 (L1~L4)
├── overlays/
│   ├── domains/                           # 산업별 보정 (fintech, ecommerce-d2c, b2b-saas, ai-native, consumer-app)
│   ├── stages/                            # 성장단계별 보정 (early-startup-0to1, scaleup-unicorn, global-bigtech)
│   └── locales/                           # 지역/규제별 보정 (kr-market, global-us-market)
├── roles/                                 # [Human-Readable] 18개 직무기술서 (.md)
│   ├── c-level/
│   ├── marketing/
│   ├── business/
│   └── product-tech/
├── specs/                                 # [Agent-Injectable] 18개 직무 스펙 (.agent.yaml / .agent.json)
│   ├── c-level/
│   ├── marketing/
│   ├── business/
│   └── product-tech/
├── raw-data/                              # 실제 수집한 국내/해외 채용 공고 원문 & 인덱스
│   ├── kr/
│   ├── global/
│   ├── collection_summary.json
│   ├── by_role_index.json
│   ├── pending_aside_targets.json         # aside CLI 재수집 대기 타겟
│   └── PENDING_ASIDE_CLI.md               # 재수집 가이드 및 타겟 목록
└── scripts/
    ├── collect_jobs.py                    # 실제 채용 공고 수집기 (Ashby/Greenhouse/Lever/Wanted/Toss/Saramin)
    ├── retry_with_aside.py                # aside CLI 설치 환경에서 미수집 타겟 재시도 스크립트
    ├── build_roles.py                     # 수집 데이터 교차검증 기반 18개 직무 문서/스펙 빌더
    └── validate_repo.py                   # 스키마·링크·에이전트 간 호환성 전수 검증기
```

---

## 전체 18대 직무 카탈로그

### A. C-Level Executive Orchestrators (`c-level/`)
| Role ID | 직무명 | 핵심 오케스트레이션 역할 | 문서 / 스펙 |
| :--- | :--- | :--- | :--- |
| `cmo-chief-marketing-officer` | CMO (마케팅 최고책임자) | 전사 브랜드·퍼널·예산 배분 및 9개 마케팅 에이전트 총괄 | [MD](roles/c-level/cmo-chief-marketing-officer.md) · [YAML](specs/c-level/cmo-chief-marketing-officer.agent.yaml) |
| `cro-chief-revenue-officer` | CRO / CBO (매출·사업 최고책임자) | 마케팅→세일즈→리텐션 전 매출 파이프라인·가격 전략 총괄 | [MD](roles/c-level/cro-chief-revenue-officer.md) · [YAML](specs/c-level/cro-chief-revenue-officer.agent.yaml) |
| `cpo-cto-product-tech-executive` | CPO / CTO (프로덕트·기술 최고책임자) | 제품 로드맵, 아키텍처·AI 인프라 및 R&D 리소스 총괄 | [MD](roles/c-level/cpo-cto-product-tech-executive.md) · [YAML](specs/c-level/cpo-cto-product-tech-executive.agent.yaml) |

### B. End-to-End Marketing & Research Suite (`marketing/`)
| Role ID | 직무명 | 핵심 자동화 영역 | 문서 / 스펙 |
| :--- | :--- | :--- | :--- |
| `market-trend-consumer-researcher` | 시장·트렌드·소비자 리서처 | 경쟁사 모니터링, VOC 마이닝, 밈/트렌드 발굴, ICP 정의 | [MD](roles/marketing/market-trend-consumer-researcher.md) · [YAML](specs/marketing/market-trend-consumer-researcher.agent.yaml) |
| `brand-marketer-strategist` | 브랜드 마케터 & 캠페인 전략가 | 브랜드 포지셔닝, 톤앤매너 가드레일, 통합 캠페인 브리프 | [MD](roles/marketing/brand-marketer-strategist.md) · [YAML](specs/marketing/brand-marketer-strategist.agent.yaml) |
| `influencer-seeding-affiliate-marketer` | 인플루언서 시딩 & 어필리에이트 마케터 | KOL 발굴·검증, 콜드 아웃리치, 시딩 운영, UTM ROI 정산 | [MD](roles/marketing/influencer-seeding-affiliate-marketer.md) · [YAML](specs/marketing/influencer-seeding-affiliate-marketer.agent.yaml) |
| `social-viral-community-marketer` | 소셜·바이럴·숏폼 & 커뮤니티 마케터 | 릴스/틱톡/쇼츠/X/레딧/국내 커뮤니티 바이럴 및 댓글 운영 | [MD](roles/marketing/social-viral-community-marketer.md) · [YAML](specs/marketing/social-viral-community-marketer.agent.yaml) |
| `content-copywriter-creative` | 콘텐츠 마케터·카피라이터 & 크리에이티브 | 광고 카피, 상세페이지(LP), 숏폼 대본, 크리에이티브 브리프 | [MD](roles/marketing/content-copywriter-creative.md) · [YAML](specs/marketing/content-copywriter-creative.agent.yaml) |
| `seo-aeo-geo-marketer` | SEO & AEO/GEO 최적화 마케터 | 구글/네이버 SEO + ChatGPT/Perplexity/Gemini 인용 최적화 | [MD](roles/marketing/seo-aeo-geo-marketer.md) · [YAML](specs/marketing/seo-aeo-geo-marketer.agent.yaml) |
| `growth-performance-marketer` | 퍼포먼스·그로스 마케터 | Meta/Google/TikTok/Naver/Kakao 유료 매체 운영, CRO, ROAS/CAC | [MD](roles/marketing/growth-performance-marketer.md) · [YAML](specs/marketing/growth-performance-marketer.agent.yaml) |
| `crm-lifecycle-retention-marketer` | CRM·라이프사이클 & 리텐션 마케터 | RFM 세그멘테이션, 온보딩·이탈방지 알림톡/푸시/이메일 자동화 | [MD](roles/marketing/crm-lifecycle-retention-marketer.md) · [YAML](specs/marketing/crm-lifecycle-retention-marketer.agent.yaml) |
| `pr-communications-event-marketer` | PR·언론홍보 & 이벤트/웨비나 마케터 | 보도자료, 미디어 피칭, 런칭(Product Hunt) 및 위기관리 | [MD](roles/marketing/pr-communications-event-marketer.md) · [YAML](specs/marketing/pr-communications-event-marketer.agent.yaml) |

### C. Business, Sales & Operations (`business/`)
| Role ID | 직무명 | 핵심 자동화 영역 | 문서 / 스펙 |
| :--- | :--- | :--- | :--- |
| `b2b-sales-sdr-ae` | B2B 세일즈 (SDR & AE) | 리드 인리치먼트, 맞춤형 아웃바운드 시퀀스, 제안서/CRM 파이프라인 | [MD](roles/business/b2b-sales-sdr-ae.md) · [YAML](specs/business/b2b-sales-sdr-ae.agent.yaml) |
| `biz-ops-strategy-cos` | 비즈니스 오퍼레이션 & Chief of Staff | 경영 KPI 모니터링, 부서 간 병목 해소, 신사업 검증, SOP 자동화 | [MD](roles/business/biz-ops-strategy-cos.md) · [YAML](specs/business/biz-ops-strategy-cos.agent.yaml) |

### D. Core Product, Data, Design & Engineering (`product-tech/`)
| Role ID | 직무명 | 핵심 자동화 영역 | 문서 / 스펙 |
| :--- | :--- | :--- | :--- |
| `product-manager` | 프로덕트 매니저 (PM / PO) | 고객 문제 정의, PRD 작성, 백로그 우선순위, GTM 릴리즈 조율 | [MD](roles/product-tech/product-manager.md) · [YAML](specs/product-tech/product-manager.agent.yaml) |
| `data-analyst-bi` | 데이터 애널리스트 (BI) | SQL 마트 구축, 퍼널/코호트/어트리뷰션 분석, A/B 테스트 검증 | [MD](roles/product-tech/data-analyst-bi.md) · [YAML](specs/product-tech/data-analyst-bi.agent.yaml) |
| `product-creative-designer` | 프로덕트 UI/UX & BX 디자이너 | UI/UX, 디자인 시스템, 광고 소재/배너/상세페이지 비주얼 생성 스펙 | [MD](roles/product-tech/product-creative-designer.md) · [YAML](specs/product-tech/product-creative-designer.agent.yaml) |
| `software-ai-engineer` | 소프트웨어 & AI 에이전트 엔지니어 | 풀스택 개발, API/MCP 연동, 에이전트/Eval 파이프라인, CI/CD | [MD](roles/product-tech/software-ai-engineer.md) · [YAML](specs/product-tech/software-ai-engineer.agent.yaml) |

---

## 에이전트 조립(Composition) 가이드

에이전트를 생성할 때 아래 3가지 레이어를 조합해 시스템 프롬프트와 도구 권한을 구성합니다:

```text
[Base Role Spec]       specs/marketing/influencer-seeding-affiliate-marketer.agent.yaml
  + [Seniority Tier]   seniority-levels/l2-senior-specialist.yaml
  + [Domain Overlay]   overlays/domains/ecommerce-d2c.yaml
  + [Stage & Locale]   overlays/stages/early-startup-0to1.yaml + overlays/locales/kr-market.yaml
```

---

## `aside` CLI 미수집 타겟 재시도 및 레포지토리 검증

```bash
# 1. 현재 환경에서 aside CLI 설치 후 로그인/SPA 차단 타겟 재수집
python3 scripts/retry_with_aside.py

# 2. 전체 레포지토리 스키마·호환성 검증
python3 scripts/validate_repo.py
```

미수집된 타겟 목록과 사유는 [`raw-data/PENDING_ASIDE_CLI.md`](raw-data/PENDING_ASIDE_CLI.md)에서 확인할 수 있습니다.
