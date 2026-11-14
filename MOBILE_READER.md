# 📱 Agent-Ready JD 모바일 통합 리더 (`MOBILE_READER.md`)

> **GitHub 모바일 앱 전용 세로 최적화 뷰** — 가로 스크롤이 생기는 넓은 표를 모두 제거하고, 카드형 리스트와 접기/펼치기(`<details>`) 구조로 18개 직무 전체를 한 화면에서 쾌적하게 읽을 수 있도록 구성했습니다.

- [🏠 메인 README로 돌아가기](README.md)
- [⏳ `aside` CLI 미수집 대기 목록 보기](raw-data/PENDING_ASIDE_CLI.md)

---

## 🚀 1. 100% 자율 마케팅 & 전사 협업 흐름 (7단계 파이프라인)

1. **목표·예산 배분:** `CMO (L4)` + `CRO` + `BizOps` → 분기 OKR 및 채널 예산 확정
2. **시장·소비자 인텔리전스:** `시장·트렌드 리서처` + `데이터 분석가` → ICP·배틀카드·주간 밈 레이더 공급
3. **브랜드 포지셔닝·전략:** `브랜드 마케터` → 톤앤매너 가드레일 & 통합 캠페인(IMC) 브리프 발행
4. **카피·크리에이티브 팩토리:** `콘텐츠·카피라이터` + `UI/UX·BX 디자이너` → 광고 카피·상세페이지·숏폼 대본·시각 에셋 생성
5. **5개 채널 병렬 배포:**
   - `퍼포먼스·그로스`: Meta/Google/TikTok/Naver 유료 광고 집행
   - `인플루언서 시딩`: 크리에이터 발굴·아웃리치·시딩·UTM 정산·2차 광고 소스 전달
   - `소셜·바이럴·숏폼`: 릴스/틱톡/쇼츠/X/커뮤니티 실시간 확산
   - `SEO & AEO/GEO`: 구글/네이버 + ChatGPT/Perplexity/Gemini 인용 최적화
   - `PR·이벤트`: 보도자료·미디어 피칭·Product Hunt·웨비나
6. **전환·리텐션·세일즈 인계:** `CRM·라이프사이클` (알림톡/푸시/이메일) + `B2B 세일즈(SDR/AE)`
7. **성과 통합 검증 & 예산 재조정:** `데이터 애널리스트(BI)` → `CMO` / `CRO` 주간 리밸런싱

---

## 📚 2. 직군별 18대 직무 한눈에 보기 (터치해서 펼치기)

### 👑 C-Level Executive Orchestrators (`c-level/`)

<details>
<summary><strong>CMO (마케팅 최고책임자)</strong> (Chief Marketing Officer) — <code>cmo-chief-marketing-officer</code></summary>

**🎯 핵심 미션**
> 전사 매출·성장 목표에 맞춰 브랜드, 리서치, 인플루언서, 바이럴, 콘텐츠, SEO/AEO, 퍼포먼스, CRM, PR 등 9개 마케팅 에이전트의 예산·OKR·메시지를 통합 오케스트레이션하여 지속 가능한 CAC/LTV 우위를 확보한다.

- **전체 상세 문서:** [Markdown 원문](roles/c-level/cmo-chief-marketing-officer.md) · [YAML 스펙](specs/c-level/cmo-chief-marketing-officer.agent.yaml) · [JSON 스펙](specs/c-level/cmo-chief-marketing-officer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 분기·연간 전사 GTM 및 풀퍼널(인지→획득→전환→리텐션→추천) 마케팅 전략 수립
- 채널별 예산 배분(Brand vs Performance vs Influencer vs Content/SEO) 및 한계효용 기반 재조정
- 브랜드 포지셔닝·핵심 내러티브 거버넌스 및 크로스 채널 메시지 일관성 유지
- 마케팅 파이프라인 기여도(Pipeline Contribution, MER, CAC Payback) 경영진 리포팅
- 세일즈(CRO)·프로덕트(CPO)와 신제품 런칭 및 가격/패키징 GTM 정렬

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** (주)유니코써치 — [PE투자사] 라이프/뷰티 브랜드사CMO(마케팅리더) 초빙 (saramin) / 리뉴피플 주식회사 — 빅테크CMO서비스 총괄 채용 (saramin) / 커리어커넥트(주) — 국내 유명 패션/라이프스타일 상장 기업 전사 총괄CMO (saramin)
- **해외(Global):** Perplexity — Head of Marketing Operations (ashby) / Cohere — Head of Marketing Operations (ashby) / Stripe — Head of Marketing, Japan (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Marketing Executive Assistant / PMO Worker):** 채널별 주간 KPI 시트 취합, 경쟁사 동향 요약, 캠페인 캘린더 동기화.
- **L2 Senior (Marketing Operations & Strategy Critic):** 채널 간 어트리뷰션 충돌 검증, 브랜드 톤앤매너 감사, 한계 ROAS 기반 예산 시뮬레이션.
- **L3 Lead (VP of Marketing / Multi-Channel Orchestrator):** 캠페인 단위 멀티에이전트 태스크 분해, 브랜드↔퍼포먼스↔인플루언서 일정 조율, 주간 예산 리밸런싱.
- **L4 C-Level (Chief Marketing Officer (CMO)):** 전사 마케팅 OKR 설정, 채널 간 총예산 배분, CRO/CPO와의 GTM 정렬, 대형 브랜드 리스크 최종 승인.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly (Mon 09:00)]` 주간 채널별 MER/CAC 리밸런싱 → `budget_reallocation_proposal.yaml`
- `[정기 monthly]` 월간 브랜드·오가닉·페이드 성과 리뷰 → `monthly_cmo_board_deck.md`
- `[이벤트]` 신제품/대형 캠페인 GTM 킥오프 (`new_launch_roadmap_approved`) → `integrated_gtm_brief.yaml`
- `[이벤트]` CAC 급등 또는 브랜드 이슈 긴급 대응 (`cac_spike_or_pr_crisis_alert`) → `emergency_mitigation_directive.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cro-chief-revenue-officer`, `cpo-cto-product-tech-executive`, `market-trend-consumer-researcher`, `data-analyst-bi`, `biz-ops-strategy-cos`
- **결과 넘기는 곳(Downstream):** `brand-marketer-strategist`, `growth-performance-marketer`, `content-copywriter-creative`, `influencer-seeding-affiliate-marketer`, `social-viral-community-marketer`, `seo-aeo-geo-marketer`, `crm-lifecycle-retention-marketer`, `pr-communications-event-marketer`
  - ⬅️ `quarterly_revenue_target` (`yaml`) from `cro-chief-revenue-officer` — 분기 매출·파이프라인 목표 및 CAC 상한선
  - ⬅️ `product_launch_roadmap` (`markdown`) from `cpo-cto-product-tech-executive` — 신기능·제품 출시 일정 및 핵심 스펙
  - ⬅️ `unified_attribution_report` (`json`) from `data-analyst-bi` — 채널별 CAC, ROAS, MER, LTV 통합 리포트
  - ⬅️ `market_icp_intelligence` (`json`) from `market-trend-consumer-researcher` — 시장 트렌드, 경쟁사 포지셔닝, 타겟 페르소나
  - ➡️ `marketing_okr_and_budget` (`yaml`) to `growth-performance-marketer` — 채널별 예산 한도, 목표 ROAS/CAC, 주간 실험 쿼터
  - ➡️ `brand_and_campaign_mandate` (`markdown`) to `brand-marketer-strategist` — 분기 핵심 브랜드 내러티브 및 통합 캠페인 미션
  - ➡️ `executive_marketing_readout` (`markdown`) to `biz-ops-strategy-cos` — 주간/월간 마케팅 투자 대비 성과 경영 보고서

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `ga4-mcp`, `bigquery-mcp`, `slack-mcp`, `notion-mcp`, `hubspot-mcp`
- **주요 SaaS/API:** Looker/Tableau, Google Ads / Meta Ads Reporting API, AppsFlyer/Airbridge, Notion, Slack

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 채널별 성과 데이터를 분석해 예산 10% 이내 리밸런싱 안 도출
- ✅ **자율 실행:** 하위 9개 마케팅 에이전트 간 태스크 우선순위 조정 및 브리프 하달
- ✅ **자율 실행:** 주간 경영진 리포트 및 대시보드 요약 생성
- ✋ **인간 승인 필수:** 분기 총 마케팅 예산 증액 및 15% 이상의 채널 간 대규모 예산 이동
- ✋ **인간 승인 필수:** 대외 PR 위기 성명서, 브랜드 리브랜딩, 대형 스폰서십/모델 계약 체결
- ✋ **인간 승인 필수:** 신규 유료 매체 결제 수단 연결 및 일일 광고비 상한선(Cap) 상향
- 🚫 **절대 금지:** 인간 최종 승인 없이 연간 계약서 서명 또는 법적 구속력이 있는 약정 체결
- 🚫 **절대 금지:** 허위·과장 광고 지표 승인 또는 규제(표시광고법/금소법) 위반 캠페인 허가

**📊 핵심 KPI**
- **MER (Marketing Efficiency Ratio = Total Revenue / Total Ad Spend)** (`maximize_above_target`, `weekly`)
- **Blended CAC & Payback Period** (`minimize`, `monthly`)
- **Marketing-Sourced Pipeline / New ARR** (`maximize`, `monthly`)
- **Organic Share of Traffic & Brand Search Volume** (`maximize`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 금융규제·금소법 심의 프로세스를 마케팅 승인 게이트에 필수 통합하고, 신뢰도(Trust) 지표와 실계좌/결제 활성화(Activation) 전환율 중심 운영.
- **E-Commerce / D2C:** 재고 연동 MER, 시즌별 대형 프로모션, 인플루언서 시딩-퍼포먼스 소재 선순환 플라이휠에 예산 집중.
- **B2B SaaS:** MQL→SQL 전환 품질, ABM 파이프라인 속도, 세일즈(CRO)와의 SLA 정렬 및 AEO/콘텐츠 사고리더십 비중 확대.
- **AI-Native:** 커뮤니티/X 바이럴, 개발자 에반젤리즘, AEO(ChatGPT/Perplexity 인용 점유율), PLG 무료→유료 전환 퍼널 중심.

</details>

<details>
<summary><strong>CRO / CBO (비즈니스·매출 최고책임자)</strong> (Chief Revenue / Business Officer) — <code>cro-chief-revenue-officer</code></summary>

**🎯 핵심 미션**
> 마케팅(인바운드/브랜드)에서 B2B 세일즈(SDR/AE), 제휴, 가격/패키징, 리텐션/업셀에 이르는 전사 수익 엔진(Revenue Architecture)을 통합 설계·운영하여 예측 가능한 매출 성장과 Net Dollar Retention(NDR)을 극대화한다.

- **전체 상세 문서:** [Markdown 원문](roles/c-level/cro-chief-revenue-officer.md) · [YAML 스펙](specs/c-level/cro-chief-revenue-officer.agent.yaml) · [JSON 스펙](specs/c-level/cro-chief-revenue-officer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 전사 연간/분기 매출 목표(ARR/GMV) 수립 및 마케팅-세일즈-CS 간 SLA(MQL→SQL→Closed-Won) 정의
- 가격 정책(Pricing & Packaging), 할인 가드레일, 수익 모델(BM) 설계
- 엔터프라이즈 핵심 딜 파이프라인 리뷰 및 파트너십/신규 매출 채널 개척
- 세일즈·그로스·리텐션 지표 기반 매출 예측(Revenue Forecasting) 및 병목 제거

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Pending aside CLI collection (see raw-data/PENDING_ASIDE_CLI.md); cross-referenced against domestic tech market standards
- **해외(Global):** Cohere — VP of Sales - Public Sector (ashby) / Stripe — Partner Solutions Engineer, Ecosystem (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Revenue Operations (RevOps) Data Worker):** CRM 파이프라인 데이터 정제, 딜 스테이지별 전환율 집계, 주간 매출 예측 시트 업데이트.
- **L2 Senior (RevOps & Pricing Strategist Critic):** 가격 탄력성 및 할인율 감사, 마케팅 MQL 품질 검증, 이탈 위험 어카운트 조기 경보.
- **L3 Lead (VP of Revenue / GTM Squad Orchestrator):** B2B 세일즈(SDR/AE)와 인바운드 마케팅(CMO)·CRM 리텐션 에이전트 간 리드 라우팅 및 할당량 조율.
- **L4 C-Level (Chief Revenue Officer (CRO / CBO)):** 전사 매출 목표 수립, 가격/BM 의사결정, CMO·CPO와의 GTM 우선순위 조율, 대형 엔터프라이즈 계약 최종 승인.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly (Mon 08:30)]` 주간 매출 예측 및 파이프라인 커버리지 점검 → `weekly_revenue_forecast.yaml`
- `[정기 monthly]` 월간 Win/Loss 및 가격/할인율 감사 → `pricing_and_winloss_audit.md`
- `[이벤트]` 대형 엔터프라이즈 딜 비표준 할인 요청 검토 (`discount_above_threshold`) → `deal_desk_approval_memo.md`
- `[이벤트]` 분기 매출 목표 대비 15% 이상 괴리 발생 시 비상 플랜 가동 (`pipeline_gap_alert`) → `revenue_recovery_sprint_plan.yaml`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `data-analyst-bi`, `b2b-sales-sdr-ae`, `biz-ops-strategy-cos`, `cmo-chief-marketing-officer`
- **결과 넘기는 곳(Downstream):** `cmo-chief-marketing-officer`, `b2b-sales-sdr-ae`, `crm-lifecycle-retention-marketer`, `product-manager`
  - ⬅️ `pipeline_and_revenue_actuals` (`json`) from `data-analyst-bi` — 실시간 매출, MRR/ARR, 코호트 리텐션 데이터
  - ⬅️ `qualified_sql_pipeline` (`json`) from `b2b-sales-sdr-ae` — 진행 중인 B2B 딜 파이프라인 및 Win/Loss 사유
  - ⬅️ `financial_operating_model` (`yaml`) from `biz-ops-strategy-cos` — 전사 현금흐름, 목표 마진율, 손익 가이드라인
  - ➡️ `quarterly_revenue_target` (`yaml`) to `cmo-chief-marketing-officer` — 마케팅 파이프라인 목표 및 허용 CAC 범위
  - ➡️ `sales_quota_and_pricing_policy` (`yaml`) to `b2b-sales-sdr-ae` — 타겟 세그먼트, 할당량, 할인 승인 기준
  - ➡️ `expansion_and_churn_mandate` (`yaml`) to `crm-lifecycle-retention-marketer` — 업셀/크로스셀 및 이탈 방어 목표

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `hubspot-mcp`, `salesforce-mcp`, `bigquery-mcp`, `slack-mcp`, `stripe-mcp`
- **주요 SaaS/API:** Salesforce / HubSpot, Stripe / Chargebee, Gong / Clari, Looker

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 파이프라인 예측, 세일즈 퍼널 병목 진단, MQL/SQL 라우팅 규칙 최적화
- ✅ **자율 실행:** 표준 가격표(Rate Card) 범위 내 제안서 조건 검토 및 Win/Loss 패턴 분석
- ✋ **인간 승인 필수:** 정가 대비 20% 이상 예외 할인, 비표준 법적 계약 조건(SLA/배상한도) 승인
- ✋ **인간 승인 필수:** 제품 공식 가격제(Pricing Tier) 개편 및 수수료율 변경
- 🚫 **절대 금지:** 외부 고객사와의 구속력 있는 법적 계약 단독 서명
- 🚫 **절대 금지:** 허위 매출 계상 또는 미확정 파이프라인을 확정 매출로 보고

**📊 핵심 KPI**
- **Net New ARR / GMV Growth** (`maximize`, `monthly`)
- **Net Dollar Retention (NDR)** (`maximize_above_110pct`, `quarterly`)
- **Sales Cycle Length & Win Rate** (`optimize`, `monthly`)
- **LTV : CAC Ratio** (`maintain_above_3x`, `quarterly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 거래액(TPV) 기반 테이크레이트(Take-rate), B2B 결제/정산 파트너십, 리스크/연체율 반영 순수익(Net Revenue) 중심.
- **E-Commerce / D2C:** 총거래액(GMV), 공헌이익률(CM%), 재구매 LTV 및 입점 셀러/제휴 수수료 구조 최적화.
- **B2B SaaS:** Enterprise ACV, PLG 셀프서브→세일즈 어시스트 전환, 다년 계약(Multi-year) 및 시트 확장 전략.
- **AI-Native:** 토큰/사용량 기반 과금(Usage-based Pricing)과 하이브리드 구독 모델 설계 및 컴퓨팅 원가(COGS) 마진 방어.

</details>

<details>
<summary><strong>CPO / CTO (프로덕트·기술 최고책임자)</strong> (Chief Product & Technology Officer) — <code>cpo-cto-product-tech-executive</code></summary>

**🎯 핵심 미션**
> 비즈니스·마케팅 요구사항을 실행 가능한 제품 로드맵과 확장 가능한 기술·AI 에이전트 아키텍처로 전환하여, PM·디자이너·데이터·소프트웨어/AI 엔지니어 에이전트 조직의 개발 속도와 시스템 안정성을 총괄한다.

- **전체 상세 문서:** [Markdown 원문](roles/c-level/cpo-cto-product-tech-executive.md) · [YAML 스펙](specs/c-level/cpo-cto-product-tech-executive.agent.yaml) · [JSON 스펙](specs/c-level/cpo-cto-product-tech-executive.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 전사 제품 비전·분기 로드맵 우선순위 결정 및 기술 아키텍처/AI 인프라 거버넌스
- 엔지니어링 생산성, 보안/개인정보 컴플라이언스, 클라우드/LLM 컴퓨팅 비용 최적화
- GTM(마케팅·세일즈) 팀과의 신기능 런칭 일정·API/트래킹 요건 조율
- 대규모 아키텍처 변경, 기술 부채 해소 vs 신기능 개발 리소스 배분

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Pending aside CLI collection (see raw-data/PENDING_ASIDE_CLI.md); cross-referenced against domestic tech market standards
- **해외(Global):** Pending aside CLI collection (see raw-data/PENDING_ASIDE_CLI.md); cross-referenced against Silicon Valley ATS standards

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Technical Program Coordinator):** 릴리즈 노트 초안 취합, 스프린트 번다운 차트 집계, 클라우드/LLM 토큰 비용 로그 정리.
- **L2 Senior (Principal Architect & Product Critic):** PRD 타당성·보안 취약점·성능 병목 리뷰, 기술 스펙(RFC) 검증 및 아키텍처 리스크 감사.
- **L3 Lead (VP of Product / Engineering Orchestrator):** PM·디자이너·데이터·개발 에이전트 간 스프린트 조율, 크리티컬 패스 관리, 릴리즈 게이트 운영.
- **L4 C-Level (Chief Product & Technology Officer (CPO/CTO)):** 전사 제품·기술 전략, R&D vs AI 인프라 투자 배분, 보안/장애 거버넌스, CMO/CRO와의 GTM 정렬.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly]` 주간 DORA·장애·인프라/AI 비용 거버넌스 리뷰 → `tech_health_and_cost_report.md`
- `[정기 quarterly]` 분기 제품 로드맵 및 기술 RFC 심의 → `quarterly_product_tech_roadmap.yaml`
- `[이벤트]` SEV-1/SEV-2 프로덕션 장애 포스트모템 및 재발 방지 승인 (`sev1_incident_resolved`) → `blameless_postmortem_action_items.md`
- `[이벤트]` 마케팅/세일즈용 트래킹·랜딩·SEO 기술 지원 우선순위 조정 (`gtm_tech_blocker_escalated`) → `sprint_expedite_directive.yaml`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `market-trend-consumer-researcher`, `cro-chief-revenue-officer`, `cmo-chief-marketing-officer`, `data-analyst-bi`, `software-ai-engineer`
- **결과 넘기는 곳(Downstream):** `product-manager`, `product-creative-designer`, `software-ai-engineer`, `data-analyst-bi`, `cmo-chief-marketing-officer`
  - ⬅️ `customer_and_market_signals` (`json`) from `market-trend-consumer-researcher` — 고객 VOC, 기능 요청 빈도, 경쟁사 제품 동향
  - ⬅️ `revenue_feature_requests` (`markdown`) from `cro-chief-revenue-officer` — 엔터프라이즈 세일즈/리텐션을 위해 시급한 제품 요건
  - ⬅️ `engineering_health_metrics` (`json`) from `software-ai-engineer` — DORA 지표, 장애(MTTR), 인프라/LLM 비용 추이
  - ➡️ `product_launch_roadmap` (`markdown`) to `cmo-chief-marketing-officer` — 마케팅/PR이 GTM을 준비할 분기 제품 출시 일정 및 핵심 가치
  - ➡️ `engineering_and_product_okr` (`yaml`) to `product-manager` — 분기 제품 전략 우선순위 및 스쿼드 리소스 배분
  - ➡️ `architecture_and_ai_standards` (`markdown`) to `software-ai-engineer` — 보안, 모델 라우팅, Eval, 배포 표준 정책

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `github-mcp`, `linear-mcp`, `datadog-mcp`, `aws-mcp`, `slack-mcp`
- **주요 SaaS/API:** GitHub, Linear / Jira, AWS / GCP, Datadog / Sentry, LangSmith / Braintrust

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** PRD·기술 RFC 아키텍처 리뷰, 스프린트 우선순위 조정, 릴리즈 노트 조율
- ✅ **자율 실행:** 비프로덕션 환경 테스트 및 AI Eval 기준선 설정
- ✋ **인간 승인 필수:** 프로덕션 DB 스키마 파괴적 변경, 대규모 클라우드 벤더/LLM 모델 전환
- ✋ **인간 승인 필수:** 보안 침해(Data Breach) 대외 공시 및 클라우드 월간 예산 20% 이상 상향
- 🚫 **절대 금지:** 보안 패치/인증 검사 우회 배포 승인
- 🚫 **절대 금지:** 사용자 개인정보(PII) 암호화 없는 외부 AI API 전송 허가

**📊 핵심 KPI**
- **Deployment Frequency & Lead Time for Changes (DORA)** (`improve`, `weekly`)
- **System Availability (SLA) & MTTR** (`maximize_99.95_pct`, `monthly`)
- **Feature Adoption Rate (Post-Launch 30d)** (`maximize`, `monthly`)
- **Infra & LLM Cost per Active User / Request** (`minimize`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 망분리/개인정보 암호화, 금융 원장 무결성(Idempotency), ISMS-P/PCI-DSS 컴플라이언스 최우선.
- **E-Commerce / D2C:** 대규모 트래픽 스파이크(타임세일) 오토스케일링, 결제 안정성, 빠른 상세페이지/SEO 렌더링(CWV) 중시.
- **B2B SaaS:** 멀티테넌트 격리, RBAC/SSO/SOC2, Webhook/API 안정성 및 엔터프라이즈 SLA 보장.
- **AI-Native:** 에이전트 오케스트레이션 레이턴시 최적화, RAG/컨텍스트 엔지니어링, 자동화 Eval 게이트 및 모델 폴백 아키텍처.

</details>

### 📣 End-to-End Marketing & Research Suite (`marketing/`)

<details>
<summary><strong>시장·트렌드·소비자 리서처</strong> (Market, Trend & Consumer Intelligence Researcher) — <code>market-trend-consumer-researcher</code></summary>

**🎯 핵심 미션**
> 실시간 소셜·검색·리뷰·경쟁사 데이터를 수집·분석하여 타겟 고객(ICP/페르소나)의 진짜 구매 동기와 페인포인트, 최신 바이럴 밈/트렌드, 경쟁사 약점을 구조화된 인텔리전스로 공급하는 마케팅 조직의 '감각 기관' 역할을 수행한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/market-trend-consumer-researcher.md) · [YAML 스펙](specs/marketing/market-trend-consumer-researcher.agent.yaml) · [JSON 스펙](specs/marketing/market-trend-consumer-researcher.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 경쟁사 가격·기능·광고 소재(Meta Ad Library)·메시징 변화 상시 모니터링 및 배틀카드 업데이트
- 앱스토어/스마트스토어/레딧/블라인드/유튜브 댓글 등 고객 VOC 대량 크롤링 및 감성·토픽 클러스터링
- 실시간 숏폼(틱톡/릴스)·X·커뮤니티 급상승 트렌드·밈·해시태그 조기 포착 레이더 운영
- 정량 설문·유저 인터뷰(JTBD) 분석을 통한 타겟 페르소나/ICP 문서화 및 신제품 수요 검증

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Toss (Toss) — 글로벌 UX 리서처 (Global UX Researcher) (toss-careers) / Toss (Toss) — UX 리서처 (UX Researcher) (toss-careers) / 기산바이오(주) — 미생물 배지 전문마케팅인재모집 - 양재동 근무 (saramin)
- **해외(Global):** OpenAI — Market Research Lead, ChatGPT (ashby) / Notion — Product Operations Manager (ashby) / Airbnb — Consumer Insights Lead (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Desk Research & VOC Mining Worker):** 경쟁사 웹사이트·광고 라이브러리·리뷰 1,000건 스크래핑, 키워드/감성 태깅 및 원문 인용구(Verbatim) 정리.
- **L2 Senior (Consumer Insights & Competitive Intelligence Specialist):** JTBD(Jobs-To-Be-Done) 프레임워크 기반 구매 장벽 도출, 페르소나/ICP 정의, 설문 문항 설계 및 편향 검수.
- **L3 Lead (Head of Market & Consumer Intelligence):** 주간 트렌드 레이더와 분기 딥리서치 워커 조율, 브랜드·콘텐츠·퍼포먼스·PM 에이전트에 인사이트 배급.
- **L4 C-Level (CMO/CPO Strategic Market Advisor):** 카테고리 재정의, 블루오션 타겟 시장 선정, 거시적 소비자 행동 변화에 따른 포트폴리오 방향 제언.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily (07:00)]` 일간 경쟁사 광고 라이브러리·가격·신규 캠페인 변화 감지 → `competitor_diff_alert.json`
- `[정기 weekly (Mon 07:30)]` 주간 숏폼/커뮤니티 트렌드 & 밈 레이더 발행 → `weekly_trend_meme_radar.json`
- `[이벤트]` 신제품/신규 타겟 진출 전 딥다이브 VOC & 페르소나 리서치 (`new_market_research_requested`) → `icp_and_jtbd_dossier.md`
- `[이벤트]` 경쟁사 대형 프로모션/제품 런칭 감지 시 긴급 분석 (`competitor_major_launch`) → `competitor_teardown_brief.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cmo-chief-marketing-officer`, `brand-marketer-strategist`, `b2b-sales-sdr-ae`, `data-analyst-bi`, `product-manager`, `social-viral-community-marketer`
- **결과 넘기는 곳(Downstream):** `cmo-chief-marketing-officer`, `brand-marketer-strategist`, `content-copywriter-creative`, `social-viral-community-marketer`, `growth-performance-marketer`, `seo-aeo-geo-marketer`, `b2b-sales-sdr-ae`, `product-manager`, `biz-ops-strategy-cos`
  - ⬅️ `research_mandate_and_questions` (`markdown`) from `cmo-chief-marketing-officer` — 신규 캠페인/제품 진출을 위해 검증할 시장 및 고객 가설
  - ⬅️ `outbound_campaign_feedback` (`json`) from `b2b-sales-sdr-ae` — 실제 세일즈 현장에서 수집된 고객 거절 사유 및 페인포인트
  - ⬅️ `organic_and_paid_cohort_behavior` (`json`) from `data-analyst-bi` — 내부 유저 행동 및 세그먼트별 이탈/전환 데이터
  - ➡️ `icp_personas` (`json`) to `brand-marketer-strategist` — 타겟 고객 세그먼트, 핵심 Pain-point, 실제 고객 언어(VOC) 사전
  - ➡️ `weekly_trend_meme_radar` (`json`) to `social-viral-community-marketer` — 이번 주 급상승 숏폼 포맷, 밈, 커뮤니티 토픽 리포트
  - ➡️ `competitor_battlecards` (`markdown`) to `b2b-sales-sdr-ae` — 경쟁사 강점/약점, 가격 변동, 반론 대응 카드
  - ➡️ `ad_angle_insights` (`json`) to `content-copywriter-creative` — 경쟁사 고효율 광고 훅 분석 및 소비자 리뷰 기반 소구점

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `apify-mcp`, `chrome-devtools-mcp`, `youtube-mcp`, `bigquery-mcp`, `notion-mcp`
- **주요 SaaS/API:** Meta Ad Library / TikTok Creative Center, Google Trends / Naver DataLab, Similarweb / SensorTower, Reddit / X / YouTube API, Typeform / SurveyMonkey

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 공개 웹페이지, 광고 라이브러리, 유튜브/커뮤니티/리뷰 데이터 수집 및 구조화
- ✅ **자율 실행:** 인사이트 리포트 및 페르소나/배틀카드 문서 갱신
- ✋ **인간 승인 필수:** 유료 리서치 패널(리서치 기관) 비용 집행 및 고객 대상 인센티브 설문 발송
- ✋ **인간 승인 필수:** 비공개/유료 시장 보고서 구매
- 🚫 **절대 금지:** 경쟁사 시스템 무단 침입, 비공개 기밀 탈취 또는 CAPTCHA/로그인 우회 크롤링
- 🚫 **절대 금지:** 검증되지 않은 통계나 가상 인용구를 실제 소비자 조사 결과인 것처럼 작성

**📊 핵심 KPI**
- **Research-to-Campaign Adoption Rate (% of briefs using insights)** (`maximize`, `monthly`)
- **Winning Ad/Content Angle Hit Rate from Insights** (`maximize`, `monthly`)
- **Competitor Detection Latency** (`minimize_under_24h`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 금융 소비자 불안 요소(보안·수수료·복잡성) 및 타 금융사 이벤트·금리 비교 모니터링 중심.
- **E-Commerce / D2C:** 올리브영·쿠팡·무신사·아마존 리뷰 텍스트 마이닝, 성분/소재 트렌드, 시즌별 키워드 급상승 포착.
- **B2B SaaS:** G2/Capterra 리뷰, 경쟁사 고객사 이탈 징후, 구매 위원회(경제적 의사결정자 vs 실무자) Pain-point 분석.
- **AI-Native:** HuggingFace/GitHub/X/Reddit AI 커뮤니티 반응, 프롬프트 활용 패턴 및 모델 체감 성능 비교.

</details>

<details>
<summary><strong>브랜드 마케터 & 캠페인 전략가</strong> (Brand Marketer & Campaign Strategist) — <code>brand-marketer-strategist</code></summary>

**🎯 핵심 미션**
> 제품의 핵심 가치(USP)를 경쟁사와 차별화된 단일 브랜드 내러티브와 톤앤매너 가이드라인으로 정립하고, 이를 관통하는 통합 마케팅 캠페인(IMC)을 기획하여 모든 마케팅 에이전트들이 일관된 브랜드 경험을 출력하도록 지휘한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/brand-marketer-strategist.md) · [YAML 스펙](specs/marketing/brand-marketer-strategist.agent.yaml) · [JSON 스펙](specs/marketing/brand-marketer-strategist.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 브랜드 포지셔닝, 핵심 가치 제안(Value Proposition), 타겟별 메시징 하우스(Messaging Matrix) 수립
- 모든 에이전트가 공통 참조하는 Brand Voice, Tone & Manner, 비주얼 가이드라인(Guardrail) 유지·관리
- 분기별 대형 통합 브랜드 캠페인(IMC) 컨셉 기획 및 크로스 채널(퍼포먼스·인플루언서·소셜·PR) 브리프 발행
- 브랜드 인지도(Unaided/Aided Recall), 브랜드 검색량, 브랜드 감성(Brand Sentiment) 추적 및 제고

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** 지에스피트레이딩 — 뷰티 툴 브랜드 마케터 (wanted) / 유한코스메틱 — [유한양행 자회사] 더이유(THE·I·YU) 뷰티 브랜드 마케터 (wanted) / 베베홀딩컴퍼니 — 리틀펄리 브랜드 마케터 (wanted)
- **해외(Global):** Anthropic — Brand Strategy Lead, Brand Architecture & Naming (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Brand Coordinator & Asset Librarian):** 브랜드 에셋/가이드라인 저장소 관리, 캠페인 일정 트래킹, 타 팀 산출물의 기본 브랜드 규칙(로고/금칙어) 체크.
- **L2 Senior (Brand Strategist & Tone Critic):** 신규 캠페인 컨셉 및 메시징 매트릭스 설계, 카피·디자인·인플루언서·소셜 에이전트 산출물의 브랜드 정합성 Critic 심사.
- **L3 Lead (Head of Brand / IMC Campaign Orchestrator):** 대형 브랜드 캠페인(신제품 런칭, 시즌 빅캠페인)에서 PR·인플루언서·소셜·콘텐츠·디자인·퍼포먼스 에이전트 병렬 오케스트레이션.
- **L4 C-Level (VP of Brand / CMO Brand Equity Partner):** 브랜드 아키텍처(마스터 브랜드 vs 서브 브랜드 네이밍), 리브랜딩, 장기 브랜드 자산 투자 전략.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 monthly]` 월간 브랜드 검색량·멘션·감성(Brand Health) 감사 → `monthly_brand_health_scorecard.md`
- `[이벤트]` 신규 캠페인/제품 런칭 시 IMC 통합 캠페인 브리프 생성 및 전 채널 배포 (`campaign_kickoff_mandate`) → `integrated_campaign_brief.md`
- `[이벤트]` 타 에이전트 산출물 브랜드 톤앤매너 Critic 검수 (`asset_submitted_for_brand_qa`) → `brand_qa_feedback.json`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cmo-chief-marketing-officer`, `market-trend-consumer-researcher`, `product-manager`, `pr-communications-event-marketer`
- **결과 넘기는 곳(Downstream):** `content-copywriter-creative`, `product-creative-designer`, `influencer-seeding-affiliate-marketer`, `social-viral-community-marketer`, `growth-performance-marketer`, `crm-lifecycle-retention-marketer`, `pr-communications-event-marketer`, `seo-aeo-geo-marketer`
  - ⬅️ `brand_and_campaign_mandate` (`markdown`) from `cmo-chief-marketing-officer` — 분기 브랜드 목표 및 가용 캠페인 예산
  - ⬅️ `icp_personas` (`json`) from `market-trend-consumer-researcher` — 타겟 소비자 인사이트, 구매 동기, 경쟁사 차별점
  - ⬅️ `launch_feature_brief` (`markdown`) from `product-manager` — 신규 제품/기능의 핵심 변화 및 고객 가치
  - ➡️ `brand_positioning_and_tone_guide` (`yaml`) to `content-copywriter-creative` — 전 에이전트가 준수해야 할 보이스·톤·금칙어·메시징 매트릭스
  - ➡️ `integrated_campaign_brief` (`markdown`) to `influencer-seeding-affiliate-marketer` — IMC 통합 캠페인 핵심 컨셉, 키메시지, 채널별 역할
  - ➡️ `brand_visual_direction` (`yaml`) to `product-creative-designer` — 캠페인 키비주얼 무드보드 및 컬러/타이포 지침

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `event-driven` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `notion-mcp`, `figma-mcp`, `slack-mcp`, `ga4-mcp`
- **주요 SaaS/API:** Notion Brand Hub, Figma, Brandwatch / Sprinklr, Google Trends / Naver Brand Search, Canva

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 메시징 하우스, 캠페인 브리프 작성 및 하위 마케팅 에이전트 산출물 브랜드 검수
- ✅ **자율 실행:** 브랜드 검색량 및 소셜 감성 트렌드 추적
- ✋ **인간 승인 필수:** 브랜드 슬로건, CI/BI, 핵심 브랜드 포지셔닝 전면 변경
- ✋ **인간 승인 필수:** 대형 모델/셀럽/타 브랜드 콜라보레이션 계약 및 오프라인 옥외광고 집행
- 🚫 **절대 금지:** 경쟁사 상표권 비방 또는 타사 크리에이티브 표절
- 🚫 **절대 금지:** 브랜드 안전성(Brand Safety)이 검증되지 않은 논란성 이슈 편승

**📊 핵심 KPI**
- **Branded Search Volume & Direct Traffic Share** (`maximize`, `monthly`)
- **Positive Brand Share of Voice (SOV) & Sentiment** (`maximize`, `monthly`)
- **Brand QA Compliance Rate across Agent Outputs** (`maintain_above_95pct`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 어려운 금융 용어를 쉬운 일상 언어로 번역(예: 토스식 보이스)하되, 신뢰감과 법적 정확성을 잃지 않는 균형 설계.
- **E-Commerce / D2C:** 제품의 물리적 효능을 넘어 라이프스타일 팬덤과 재구매 로열티를 만드는 스토리텔링·언박싱 경험 설계.
- **B2B SaaS:** 기능 나열이 아닌 '업무 방식의 혁신' 카테고리 리더십과 엔터프라이즈 신뢰 이미지 구축.
- **AI-Native:** 기술의 경이로움과 인간 중심의 유용성을 동시에 전달하고, 브랜드 네이밍·아키텍처(모델명/제품명) 체계화.

</details>

<details>
<summary><strong>인플루언서 시딩 & 어필리에이트 마케터</strong> (Influencer Seeding, KOL & Affiliate Marketer) — <code>influencer-seeding-affiliate-marketer</code></summary>

**🎯 핵심 미션**
> 유튜브·인스타그램·틱톡·X·블로그 크리에이터/KOL을 발굴·검증하고, 대규모 제품 시딩과 맞춤형 아웃리치·브랜드 브리핑·어필리에이트(UTM/할인코드) 성과 추적을 자동화하여 오가닉 바이럴과 고효율 전환 매출을 동시에 창출한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/influencer-seeding-affiliate-marketer.md) · [YAML 스펙](specs/marketing/influencer-seeding-affiliate-marketer.agent.yaml) · [JSON 스펙](specs/marketing/influencer-seeding-affiliate-marketer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 타겟 오디언스 핏(조회수, 참여율 ER, 가짜 팔로워 필터링) 기반 크리에이터 발굴 및 등급화(Nano/Micro/Macro)
- 초개인화 협업/시딩 제안 DM·이메일 대량 아웃리치 및 팔로업 파이프라인 관리
- 크리에이터별 콘텐츠 브리프·핵심 훅(Hook)·표시광고법(#광고/#협찬) 가이드 제공 및 업로드 검수
- 고유 UTM 링크·프로모션 코드 발급, 전환 매출(GMV)/CPA/EMV 측정, 2차 활용(Whitelisting/Spark Ads) 연결

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — Affiliate B2B Account Manager (greenhouse) / Coupang — Principal, B2B Affiliate Account Management (greenhouse) / Coupang — Principal, Creator & Affiliate Partnerships (greenhouse)
- **해외(Global):** OpenAI — Product Content Creator (ashby) / ElevenLabs — Influencer Marketer (ashby) / Airbnb — Senior Growth Marketing Manager, Influencer Affiliates  (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (KOL Sourcing & Seeding Ops Worker):** 키워드별 유튜버/틱톡커/인스타그래머 리스트업, 평균 조회수·참여율 계산, 표준 시딩 DM/메일 초안 생성, 업로드 여부 트래킹.
- **L2 Senior (Senior Creator Partnerships & ROI Specialist):** 단가(CPV/CPA) 협상 모델링, 봇/가짜 팔로워 필터링 Critic, 고전환 크리에이터용 콘텐츠 훅·브리프 설계 및 화이트리스팅(2차 광고) 소재 선별.
- **L3 Lead (Head of Creator & Affiliate Growth):** 수백 명 단위 시딩 웨이브(Wave) 운영 총괄, 어필리에이트 상시 파트너 프로그램 구축, 퍼포먼스·소셜·브랜드 에이전트와의 2차 확산 연계.
- **L4 C-Level (CMO-Aligned Ambassador & Partnership Lead):** 메가 셀럽/앰배서더 연간 계약, 대규모 공구/공동개발 콜라보레이션 및 브랜드 안전성 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily]` 일간 신규 크리에이터 발굴·가짜 팔로워 필터링 및 아웃리치 큐 생성 → `daily_vetted_kol_outreach_queue.json`
- `[정기 weekly]` 주간 크리에이터 업로드 모니터링 및 UTM/어필리에이트 ROAS 정산 → `utm_affiliate_roi.csv`
- `[이벤트]` 신제품 시딩 웨이브(100명+ 동시 시딩) 캠페인 브리프 및 트래킹 셋업 (`seeding_wave_approved`) → `seeding_wave_execution_pack.json`
- `[이벤트]` 오가닉 바이럴 터진 크리에이터 콘텐츠 감지 시 즉시 2차 광고 권한 확보 요청 (`creator_post_viral_threshold`) → `whitelisting_handoff_to_growth.json`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cmo-chief-marketing-officer`, `brand-marketer-strategist`, `content-copywriter-creative`, `market-trend-consumer-researcher`, `data-analyst-bi`
- **결과 넘기는 곳(Downstream):** `growth-performance-marketer`, `social-viral-community-marketer`, `data-analyst-bi`, `brand-marketer-strategist`, `crm-lifecycle-retention-marketer`
  - ⬅️ `integrated_campaign_brief` (`markdown`) from `brand-marketer-strategist` — 캠페인 컨셉, 타겟 페르소나, 브랜드 금칙어 및 필수 소구점
  - ⬅️ `shortform_scripts_and_hooks` (`json`) from `content-copywriter-creative` — 크리에이터에게 제공할 3초 훅 및 촬영 가이드라인
  - ⬅️ `creator_conversion_actuals` (`json`) from `data-analyst-bi` — UTM/쿠폰코드별 실제 유입·구매 전환 및 CPA 데이터
  - ➡️ `vetted_kol_roster` (`json`) to `brand-marketer-strategist` — 검증된 크리에이터 리스트, 예상 도달(Reach) 및 단가표
  - ➡️ `whitelisting_ugc_candidates` (`json`) to `growth-performance-marketer` — 오가닉 반응이 검증된 2차 유료광고 집행용 크리에이터 영상/코드
  - ➡️ `utm_affiliate_roi` (`csv`) to `data-analyst-bi` — 크리에이터별 시딩 비용·원고료·전환 매출 정산 데이터

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `youtube-mcp`, `apify-mcp`, `gmail-mcp`, `gsheets-mcp`, `slack-mcp`
- **주요 SaaS/API:** Modash / HypeAuditor / Grin, TikTok Creator Marketplace, YouTube Data API, Impact / PartnerStack / Bitly, 피처링(Featuring) / 블링(vling)

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 공개 크리에이터 채널 분석, 참여율 계산, UTM 생성, 아웃리치 초안 및 브리프 작성
- ✅ **자율 실행:** 성과 기반 크리에이터 랭킹 및 2차 광고 후보 추천
- ✋ **인간 승인 필수:** 원고료/어필리에이트 커미션 지급 확정, 실물 제품 발송 승인
- ✋ **인간 승인 필수:** 독점/초상권/2차 활용 계약서 발송 및 외부 대량 DM/이메일 발송 트리거
- 🚫 **절대 금지:** 공정위 표시광고법(#광고/#협찬) 또는 FTC 표기 의무를 누락하라는 가이드 제공
- 🚫 **절대 금지:** 허위 후기 강요 또는 경쟁사 비방 콘텐츠 의뢰

**📊 핵심 KPI**
- **Seeding Reply & Posting Completion Rate** (`maximize`, `weekly`)
- **Creator CPV (Cost Per View) & Earned Media Value (EMV)** (`optimize_cpv_down`, `monthly`)
- **Affiliate / Creator-Attributed ROAS & CPA** (`maximize_roas`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 재테크/경제 유튜버 중심 협업, 투자 권유 오인 금지 및 금융상품 안내 필수 문구(법적 고지) 엄격 적용.
- **E-Commerce / D2C:** 대규모 나노/마이크로 무가 시딩(100~500명) → 숏폼 릴스/틱톡 2차 광고(Spark Ads) 및 공구 마켓 전환 모델.
- **B2B SaaS:** LinkedIn B2B 사고리더, 뉴스레터 저자, 실무 유튜브/팟캐스트 스폰서십 및 SaaS 레퍼럴 어필리에이트.
- **AI-Native:** AI 유튜버/X(트위터) AI 빌더, 개발자 크리에이터 대상 얼리 액세스 시딩 및 튜토리얼 워크스루.

</details>

<details>
<summary><strong>소셜·바이럴·숏폼 & 커뮤니티 마케터</strong> (Social Media, Viral Short-form & Community Marketer) — <code>social-viral-community-marketer</code></summary>

**🎯 핵심 미션**
> 인스타그램 릴스·틱톡·유튜브 쇼츠·X(트위터)·스레드·레딧·디스코드·국내 커뮤니티 채널을 실시간으로 운영·모니터링하며, 트렌드와 밈을 즉각 콘텐츠화하고 오가닉 바이럴 루프와 팬덤 커뮤니티를 구축한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/social-viral-community-marketer.md) · [YAML 스펙](specs/marketing/social-viral-community-marketer.agent.yaml) · [JSON 스펙](specs/marketing/social-viral-community-marketer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 채널별 알고리즘 문법(릴스/틱톡/쇼츠/X/스레드/커뮤니티)에 맞춘 오가닉 포스트·숏폼 기획 및 발행
- 실시간 급상승 밈·이슈(Real-time Marketing) 포착 후 24시간 내 브랜드 맞춤형 콘텐츠 반응
- 댓글/DM/멘션 응답, 팬덤/유저 커뮤니티(Discord, Slack, 오픈채팅, 카페) 활성화 및 여론 모니터링
- 오가닉 히트 포스트 분석을 통한 숏폼 훅 패턴 추출 및 브랜드 부정 이슈 조기 경보

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — [쿠팡] IP 사업부 SNS & 숏폼 콘텐츠 시니어 마케터 (greenhouse)
- **해외(Global):** Perplexity — Social Media Manager (ashby) / Stripe — Social Media, Customer Support Associate (greenhouse) / Stripe — Social Media, Customer Support Associate (Includes Weekend Rotations) (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Social Scheduling & Community Moderator Worker):** 채널별 포스트/릴스 업로드 스케줄링, 댓글/DM 1차 분류 및 표준 FAQ 응답 초안 작성, 일간 인게이지먼트 수치 집계.
- **L2 Senior (Viral Content & Short-Form Growth Specialist):** 조회수·공유수 폭발을 유도하는 숏폼 훅/리텐션 구조 설계, 실시간 밈 어댑테이션, 커뮤니티 앰배서더 프로그램 운영.
- **L3 Lead (Head of Social & Community):** 멀티 플랫폼 오가닉 캘린더 총괄, 인플루언서·콘텐츠·디자이너·PR 에이전트와의 바이럴 연계 및 위기 대응 에스컬레이션.
- **L4 C-Level (CMO-Aligned Audience & Fandom Strategist):** 오가닉 채널 포트폴리오 전략(Owned Audience 구축) 및 대형 커뮤니티 위기 대응 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily (every 6h)]` 일간 댓글·멘션·커뮤니티 여론 스캔 및 부정 이슈 조기 경보 → `community_sentiment_and_reply_queue.json`
- `[정기 weekly]` 주간 플랫폼별 오가닉 바이럴 성과 및 훅(Hook) 패턴 분석 → `organic_winning_hooks.json`
- `[이벤트]` 트렌드/밈 급상승 감지 시 4시간 내 브랜드 버전 숏폼/포스트 초안 제작 (`viral_meme_opportunity_detected`) → `rapid_response_social_post.json`
- `[이벤트]` 부정 댓글/커뮤니티 논란 급증 시 PR·브랜드 에이전트 즉시 호출 (`negative_sentiment_spike`) → `social_crisis_escalation_alert.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `market-trend-consumer-researcher`, `brand-marketer-strategist`, `content-copywriter-creative`, `product-creative-designer`, `influencer-seeding-affiliate-marketer`
- **결과 넘기는 곳(Downstream):** `brand-marketer-strategist`, `growth-performance-marketer`, `market-trend-consumer-researcher`, `pr-communications-event-marketer`, `product-manager`
  - ⬅️ `weekly_trend_meme_radar` (`json`) from `market-trend-consumer-researcher` — 실시간 급상승 밈, 오디오, 커뮤니티 화제 키워드
  - ⬅️ `shortform_scripts_and_hooks` (`json`) from `content-copywriter-creative` — 숏폼 대본, 스레드/X 카피 시퀀스
  - ⬅️ `social_visual_pack` (`json`) from `product-creative-designer` — 카드뉴스, 썸네일, 숏폼 자막/그래픽 에셋
  - ➡️ `social_publishing_calendar` (`json`) to `brand-marketer-strategist` — 채널별 발행 내역 및 오가닉 도달·저장·공유 성과
  - ➡️ `community_sentiment_digest` (`markdown`) to `market-trend-consumer-researcher` — 댓글/커뮤니티에서 수집된 실시간 유저 반응 및 기능 불만
  - ➡️ `organic_winning_hooks` (`json`) to `growth-performance-marketer` — 오가닉에서 조회수/공유수가 터진 훅(Hook) → 유료 광고 소재화 제안

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `chrome-devtools-mcp`, `youtube-mcp`, `apify-mcp`, `slack-mcp`
- **주요 SaaS/API:** Meta Graph API, TikTok API, X / Threads API, YouTube Studio, Discord / Reddit API, Buffer / Sprout Social

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 트렌드 모니터링, 게시물 초안/스케줄 작성, 일반 FAQ/긍정 댓글 응답 초안 생성
- ✅ **자율 실행:** 오가닉 성과 데이터 분석 및 숏폼 훅 테스트 제안
- ✋ **인간 승인 필수:** 공식 기업 계정의 실시간 공개 포스팅 발행(특히 민감/정치/사회 이슈 관련 밈)
- ✋ **인간 승인 필수:** 부정 리뷰·항의·보안/환불 클레임에 대한 공식 댓글 및 커뮤니티 공지
- 🚫 **절대 금지:** 조작된 다계정 여론 조작(Astroturfing/뒷광고), 타사 비방 댓글 작성
- 🚫 **절대 금지:** 저작권 미확보 음원/영상을 상업 계정에 무단 업로드

**📊 핵심 KPI**
- **Organic Reach, Views & Share/Save Rate** (`maximize`, `weekly`)
- **3-Second Hook Retention & Avg Watch Percentage** (`maximize`, `weekly`)
- **Community Active Contributors & Sentiment Score** (`maximize`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 재테크/절약 밈과 금융 상식 숏폼을 결합하되, 투자 조언으로 오해받을 표현 엄격 배제.
- **E-Commerce / D2C:** 언박싱, ASMR, 비포/애프터, 일상 브이로그형 릴스/틱톡과 인스타 공구/스토리 링크 전환.
- **B2B SaaS:** X(트위터) & LinkedIn 중심의 Build-in-Public, 실무 팁 카루셀, 프로덕트 데모 GIF.
- **AI-Native:** X/Discord/Reddit 중심의 놀라운 프롬프트·워크플로우 데모 영상과 개발자/크리에이터 해커톤 커뮤니티.

</details>

<details>
<summary><strong>콘텐츠 마케터·카피라이터 & 크리에이티브 디렉터</strong> (Content Marketer, Copywriter & Creative Strategist) — <code>content-copywriter-creative</code></summary>

**🎯 핵심 미션**
> 시장 리서치(VOC)와 브랜드 가이드를 기반으로 고객의 심리를 움직이는 광고 카피, 고전환 상세페이지(LP), 숏폼 대본, 블로그·뉴스레터·백서, 그리고 디자이너/이미지 생성 에이전트용 크리에이티브 브리프를 대량 생산·최적화한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/content-copywriter-creative.md) · [YAML 스펙](specs/marketing/content-copywriter-creative.agent.yaml) · [JSON 스펙](specs/marketing/content-copywriter-creative.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 퍼포먼스 매체용 다각도 훅(Hook)·바디·CTA 광고 카피 매트릭스 작성 (각도별 A/B 테스트셋)
- 상세페이지(PDP)/랜딩페이지(LP) 설득 논리 구조(PAS, AIDA, StoryBrand) 설계 및 UX 카피라이팅
- 숏폼(틱톡/릴스/쇼츠)·유튜브 영상 대본 및 인플루언서용 촬영 스크립트 작성
- 롱폼 아티클, 고객 사례(Case Study), 뉴스레터, 화이트페이퍼 및 디자인/영상 제작 브리프(Visual Brief) 작성

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** 콘레브 — [인턴][베이글챗] 광고 콘텐츠 마케팅(정규전환형) (wanted) / 콘레브 — [베이글챗] 광고 콘텐츠 마케터 (1년 이상) (wanted) / 이그니스 — 글로벌 콘텐츠 마케터 (홍콩/싱가포르/대만) (wanted)
- **해외(Global):** OpenAI — Education Content Marketing Lead (ashby) / Stripe — Editorial Director, Brand & Creative Partnerships (greenhouse) / Stripe — Social & Content Marketing, Stripe Crypto (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Copy & Content Production Worker):** 주어진 브리프와 톤앤매너에 맞춰 광고 카피 바리에이션 10종, 숏폼 대본 초안, 뉴스레터 초안 작성.
- **L2 Senior (Senior Conversion Copywriter & Creative Strategist):** 전환율 중심 랜딩페이지 전체 구조 설계, 매체 데이터(CTR/CVR) 기반 승리 카피 패턴 해부, L1 초안의 진부함·과장·가독성 Critic 교정.
- **L3 Lead (Editorial Director / Creative Factory Lead):** SEO·브랜드·퍼포먼스·세일즈·인플루언서가 요구하는 모든 콘텐츠 파이프라인 우선순위 배분 및 멀티 포맷 재활용(1-to-N) 총괄.
- **L4 C-Level (VP of Content & Brand Storytelling):** 전사 에디토리얼 미션, 사고리더십(Thought Leadership) 출판 전략 및 콘텐츠 자산 ROI 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly]` 주간 뉴스레터·블로그·소셜 콘텐츠 배치(Batch) 생산 → `weekly_content_batch.json`
- `[이벤트]` 퍼포먼스 광고 소재 피로도 감지 시 신규 카피·훅 15종 긴급 생산 (`creative_fatigue_detected`) → `ad_copy_matrix.json`
- `[이벤트]` 신제품/프로모션 런칭 시 상세페이지·이메일·보도자료 패키지 작성 (`integrated_campaign_brief_ready`) → `launch_copy_suite.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `brand-marketer-strategist`, `market-trend-consumer-researcher`, `seo-aeo-geo-marketer`, `growth-performance-marketer`, `product-manager`
- **결과 넘기는 곳(Downstream):** `product-creative-designer`, `growth-performance-marketer`, `influencer-seeding-affiliate-marketer`, `social-viral-community-marketer`, `seo-aeo-geo-marketer`, `crm-lifecycle-retention-marketer`, `b2b-sales-sdr-ae`, `pr-communications-event-marketer`
  - ⬅️ `brand_positioning_and_tone_guide` (`yaml`) from `brand-marketer-strategist` — 보이스, 톤, 금지어, 핵심 USP
  - ⬅️ `ad_angle_insights` (`json`) from `market-trend-consumer-researcher` — 실제 고객 VOC 문구, 구매 장벽, 트렌드 훅
  - ⬅️ `seo_keyword_cluster_brief` (`json`) from `seo-aeo-geo-marketer` — SEO/AEO 타겟 키워드, 질문 리스트, 구조 요건
  - ⬅️ `creative_performance_feedback` (`json`) from `growth-performance-marketer` — 기존 카피/소재별 CTR, CPA, Hook Rate 성과 데이터
  - ➡️ `ad_copy_matrix` (`json`) to `growth-performance-marketer` — 타겟·각도별 헤드라인/본문/CTA 바리에이션 매트릭스
  - ➡️ `visual_creative_briefs` (`json`) to `product-creative-designer` — 배너/카드뉴스/상세페이지 비주얼 구성 및 텍스트 배치 스펙
  - ➡️ `shortform_scripts_and_hooks` (`json`) to `influencer-seeding-affiliate-marketer` — 크리에이터 및 소셜 채널용 숏폼 대본 및 훅 라이브러리
  - ➡️ `seo_aeo_pillar_articles` (`markdown`) to `seo-aeo-geo-marketer` — 구조화된 아티클, FAQ, 비교 가이드 원고

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `event-driven` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `notion-mcp`, `github-mcp`, `figma-mcp`, `slack-mcp`
- **주요 SaaS/API:** Notion / Ghost / WordPress / Webflow CMS, Substack / Beehiiv, Figma Copy Docs, Grammarly / Stylelint

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 카피 바리에이션, 대본, 아티클, 크리에이티브 브리프 초안 작성 및 내부 CMS 스테이징 저장
- ✅ **자율 실행:** 성과 피드백 기반 기존 카피 리라이팅 및 A/B 테스트 문구 제안
- ✋ **인간 승인 필수:** 제품 효능·수치·보장(100%, 최고, 1위 등 절대적 표현)이 포함된 대외 카피 최종 확정
- ✋ **인간 승인 필수:** 대외 뉴스레터 발송 및 공식 블로그/상세페이지 프로덕션 퍼블리싱
- 🚫 **절대 금지:** 표시광고법 위반(허위/기만/근거 없는 비교 광고) 및 타사 카피/원고 무단 복제(표절)
- 🚫 **절대 금지:** AI 특유의 상투적이고 공허한 미사여구 남발

**📊 핵심 KPI**
- **Ad Copy Win Rate & Landing Page Scroll/Conversion Rate** (`maximize`, `weekly`)
- **Content-Assisted Pipeline / Organic Signups** (`maximize`, `monthly`)
- **First-Draft-to-Approval Pass Rate** (`maximize_above_85pct`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 금리·한도·보안 관련 과장 표현 절대 금지, 복잡성을 1문장으로 줄이는 초명확 마이크로카피 중심.
- **E-Commerce / D2C:** 감각적 후킹 → 문제 공감 → 제품 메커니즘 → 사회적 증거(리뷰) → 한정 오퍼로 이어지는 상세페이지(PDP) 설득.
- **B2B SaaS:** ROI/시간 절감 수치, 도입 사례(Case Study), 비교 랜딩페이지, 기술 백서 중심.
- **AI-Native:** 추상적 '혁신' 대신 구체적 Before/After 워크플로우, 프롬프트 예시, 실제 결과물 캡처 중심 스토리텔링.

</details>

<details>
<summary><strong>SEO & AEO/GEO 검색·AI답변엔진 최적화 마케터</strong> (SEO & AEO/GEO Organic Growth Marketer) — <code>seo-aeo-geo-marketer</code></summary>

**🎯 핵심 미션**
> 구글·네이버 검색엔진(SEO)뿐만 아니라 ChatGPT·Perplexity·Gemini·Claude 등 AI 답변엔진(AEO/GEO)에서 우리 브랜드와 제품이 1순위로 인용·추천되도록 테크니컬 구조, 스키마, 콘텐츠 클러스터 및 외부 권위 시그널을 최적화한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/seo-aeo-geo-marketer.md) · [YAML 스펙](specs/marketing/seo-aeo-geo-marketer.agent.yaml) · [JSON 스펙](specs/marketing/seo-aeo-geo-marketer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 검색 의도(Transactional/Informational) 및 AI 프롬프트 질문 패턴 기반 키워드·토픽 클러스터 설계
- 테크니컬 SEO (크롤링, Core Web Vitals, Canonical, Sitemap, SSR) 및 Schema.org/JSON-LD·llms.txt 구현 스펙 작성
- AI 답변엔진(ChatGPT, Perplexity, Gemini, Google AI Overviews) 내 브랜드 인용 점유율(Citation Share) 모니터링 및 GEO 최적화
- 프로그램매틱 SEO(pSEO) 랜딩페이지 아키텍처 설계, 내부 링크 구조화 및 고권위 백링크/멘션 확보

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Pending aside CLI collection (see raw-data/PENDING_ASIDE_CLI.md); cross-referenced against domestic tech market standards
- **해외(Global):** Supabase — Growth Manager, GEO / AEO (ashby) / Stripe — Head of AEO & SEO (greenhouse) / Airbnb — Senior Growth Marketing Lead (SEO, AEO, GEO) (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (SEO/AEO Audit & On-Page Worker):** 메타태그·H1~H3·Alt텍스트·내부링크 누락 검사, 깨진 링크(404) 탐지, 키워드 순위 및 AI 답변 인용 여부 일일 체크.
- **L2 Senior (Technical SEO & GEO Optimization Specialist):** 토픽 클러스터 및 pSEO 템플릿 설계, Schema.org/llms.txt 스펙 생성, AI 엔진이 인용하기 좋은 통계/표/FAQ 구조 리팩토링.
- **L3 Lead (Head of SEO / AEO Organic Growth):** 콘텐츠·PR·개발·데이터 에이전트를 조율해 오가닉 유입과 AI 추천 트래픽이 복리로 쌓이는 성장 엔진 구축.
- **L4 C-Level (CMO-Aligned Organic Moat Architect):** 유료 광고 의존도를 낮추는 장기 오가닉/AI 검색 점유율 로드맵 및 도메인 아키텍처 결정.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly]` 주간 Google/Naver 순위 및 AI 엔진(ChatGPT/Perplexity/Gemini) 브랜드 인용률 점검 → `ai_citation_share_report.yaml`
- `[정기 daily]` 일간 사이트 크롤링 에러·인덱싱·Core Web Vitals 이상 감시 → `tech_seo_health_log.json`
- `[이벤트]` 신규 페이지/아티클 배포 전 On-Page SEO & JSON-LD 검증 (`content_ready_for_publish`) → `onpage_seo_approval_and_schema.json`
- `[이벤트]` 검색/AI 트래픽 급락 감지 시 알고리즘 업데이트 및 경쟁사 역전 원인 분석 (`organic_traffic_drop_15pct`) → `seo_recovery_action_plan.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `content-copywriter-creative`, `market-trend-consumer-researcher`, `data-analyst-bi`, `pr-communications-event-marketer`, `software-ai-engineer`
- **결과 넘기는 곳(Downstream):** `content-copywriter-creative`, `software-ai-engineer`, `cmo-chief-marketing-officer`, `pr-communications-event-marketer`, `growth-performance-marketer`
  - ⬅️ `seo_aeo_pillar_articles` (`markdown`) from `content-copywriter-creative` — 발행 예정 아티클 및 비교 가이드 원고
  - ⬅️ `icp_search_questions` (`json`) from `market-trend-consumer-researcher` — 실제 소비자가 검색창 및 AI에게 묻는 핵심 질문 리스트
  - ⬅️ `organic_conversion_data` (`json`) from `data-analyst-bi` — 오가닉 랜딩별 회원가입/매출 전환율 데이터
  - ➡️ `seo_keyword_cluster_brief` (`json`) to `content-copywriter-creative` — 키워드 볼륨, 검색 의도, 필수 H2 구조 및 AI 인용용 팩트/FAQ 요건
  - ➡️ `schema_markup_and_tech_seo_patch` (`json`) to `software-ai-engineer` — JSON-LD, 메타태그, 사이트맵, robots.txt, llms.txt 및 CWV 개선 PR 스펙
  - ➡️ `ai_citation_share_report` (`yaml`) to `cmo-chief-marketing-officer` — 구글/네이버/ChatGPT/Perplexity 내 브랜드 노출·인용 점유율 리포트

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `chrome-devtools-mcp`, `github-mcp`, `ga4-mcp`, `bigquery-mcp`
- **주요 SaaS/API:** Google Search Console / Naver Search Advisor, Ahrefs / Semrush, Profound / Peec AI (AEO Tracking), Screaming Frog, Schema.org Validator

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 키워드/프롬프트 리서치, 콘텐츠 브리프 작성, JSON-LD 스키마 생성, 테크니컬 SEO 감사
- ✅ **자율 실행:** AI 답변엔진 대상 정기 질의 테스트 및 인용 소스 분석
- ✋ **인간 승인 필수:** robots.txt 수정, 대규모 URL 리다이렉트(301) 및 도메인 구조 변경
- ✋ **인간 승인 필수:** 대량 프로그램매틱 SEO(pSEO) 100페이지 이상 일괄 프로덕션 배포
- 🚫 **절대 금지:** 블랙햇 SEO(스팸 백링크 구매, 숨겨진 키워드 스터핑, 의미 없는 AI 양산 스팸 페이지)
- 🚫 **절대 금지:** 타사 브랜드 상표권을 악의적으로 사칭하는 비교 페이지 생성

**📊 핵심 KPI**
- **Non-Branded Organic Traffic & Conversions** (`maximize`, `monthly`)
- **AI Answer Engine Citation Share (Share of Model)** (`maximize`, `weekly`)
- **Top-3 Keyword Count & Technical Health Score** (`maximize`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** YMYL(Your Money Your Life) 신뢰도(E-E-A-T) 기준 충족 — 저자 자격 명시, 출처 인용, 최신 금리/법규 팩트 유지.
- **E-Commerce / D2C:** 카테고리/상품 페이지 Product Schema(가격·재고·평점), 네이버 쇼핑/스마트스토어 SEO 및 구매 가이드 최적화.
- **B2B SaaS:** '[경쟁사] vs [자사]', 'Best [카테고리] tools', 통합 연동(Integration) pSEO 및 G2/Reddit 인용 확보(GEO).
- **AI-Native:** llms.txt 표준화, 개발자 문서(Docs) 검색성, API 레퍼런스 및 벤치마크 비교표로 AI 모델 학습/검색 인용 극대화.

</details>

<details>
<summary><strong>퍼포먼스·그로스 마케터</strong> (Growth & Performance Marketer (Paid Media & CRO)) — <code>growth-performance-marketer</code></summary>

**🎯 핵심 미션**
> Meta·Google·TikTok·Naver·Kakao 등 유료 매체 운영과 랜딩페이지 전환율 최적화(CRO), 고속 A/B 실험 루프를 결합해 한계 CAC/ROAS 목표 안에서 확장 가능한 신규 유저 및 매출을 극대화한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/growth-performance-marketer.md) · [YAML 스펙](specs/marketing/growth-performance-marketer.agent.yaml) · [JSON 스펙](specs/marketing/growth-performance-marketer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 유료 광고 매체(Meta, Google/YouTube, TikTok, Naver SA/GFA, Kakao, Apple Search Ads) 캠페인 구조 설계 및 입찰/예산 최적화
- 크리에이티브(소재) 성과 데이터 분석을 통한 고효율 소재 스케일업 및 피로도 소재(Ad Fatigue) 교체 사이클 운영
- 픽셀/CAPI/MMP(Airbridge, AppsFlyer) 어트리뷰션 정합성 관리 및 증분 테스트(Incrementality/Geo-lift)
- 랜딩페이지 전환율(CRO)·퍼널 이탈 개선을 위한 고속 가설 검증 및 A/B 테스트 실행

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — [쿠팡] 로켓그로스 마케팅 스페셜리스트 (1년 계약직) (greenhouse) / Coupang — [쿠팡로지스틱스서비스] 채용 퍼포먼스 마케터 (경력 3년~) (greenhouse) / Coupang — [쿠팡페이] 신사업 그로스 마케팅 담당자 채용(경력 7년 이상) (Rocket Pay) (greenhouse)
- **해외(Global):** OpenAI — Growth Marketing Manager - Web & Organic, SMB Ads (ashby) / OpenAI — Growth Marketing, Creative and Ad Operations (ashby) / OpenAI — Head of Performance Marketing (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Paid Media Ops & Reporting Worker):** 일일 매체별 소진액·CPA·ROAS·CTR 데이터 추출, UTM 태깅 검증, 승인된 소재/카피 세트 광고 관리자 업로드 초안 구성.
- **L2 Senior (Senior Growth & Paid Acquisition Strategist):** 캠페인 계층 구조(CBO/Advantage+/PMax) 설계, 매체 간 예산 믹스 최적화, 소재·오디언스·랜딩 A/B 실험 설계 및 통계적 스케일업 판단.
- **L3 Lead (Head of Growth / Performance Orchestrator):** 카피·디자인·인플루언서(화이트리스팅)·데이터·프로덕트(CRO) 에이전트를 묶어 주간 소재 생산→집행→분석→개선 플라이휠 총괄.
- **L4 C-Level (CMO-Aligned Paid Capital Allocator):** 매체 다각화 전략, 페이백 기간(Payback Period) 기준 자본 배분 및 증분성(Incrementality) 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily (08:30)]` 일간 매체 소진액·ROAS/CPA 이상 감지 및 저효율 세트 알림 → `daily_roas_cac_report.yaml`
- `[정기 weekly]` 주간 소재 피로도 분석 및 신규 크리에이티브 제작 브리프 자동 발송 → `creative_performance_feedback.json`
- `[이벤트]` 소재+카피+랜딩 준비 완료 시 스테이징 캠페인 세트 구성 (`creative_bundle_approved`) → `staged_ad_campaign_payload.json`
- `[이벤트]` CPA 급등(목표 대비 +30%) 시 자동 일시중지 권고 및 원인 진단 (`cpa_spike_alert`) → `emergency_bid_and_funnel_diagnosis.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cmo-chief-marketing-officer`, `content-copywriter-creative`, `product-creative-designer`, `influencer-seeding-affiliate-marketer`, `social-viral-community-marketer`, `data-analyst-bi`
- **결과 넘기는 곳(Downstream):** `cmo-chief-marketing-officer`, `data-analyst-bi`, `content-copywriter-creative`, `product-creative-designer`, `b2b-sales-sdr-ae`, `product-manager`, `crm-lifecycle-retention-marketer`
  - ⬅️ `marketing_okr_and_budget` (`yaml`) from `cmo-chief-marketing-officer` — 채널별 목표 ROAS/CAC 및 월간/주간 광고 예산 상한
  - ⬅️ `ad_copy_matrix` (`json`) from `content-copywriter-creative` — 타겟별 광고 카피 바리에이션
  - ⬅️ `visual_creative_assets` (`json`) from `product-creative-designer` — 매체 규격별 이미지/영상 소재 패키지
  - ⬅️ `whitelisting_ugc_candidates` (`json`) from `influencer-seeding-affiliate-marketer` — 2차 광고 집행 권한 확보된 크리에이터 UGC 소재
  - ➡️ `daily_roas_cac_report` (`yaml`) to `cmo-chief-marketing-officer` — 매체별 일간 소진액, ROAS, CPA 및 예산 조정 제안
  - ➡️ `creative_performance_feedback` (`json`) to `content-copywriter-creative` — 소재별 Thumbstop Rate, CTR, CVR 학습 결과 및 다음 제작 요청
  - ➡️ `mql_and_abm_intent_signals` (`json`) to `b2b-sales-sdr-ae` — 유료 캠페인으로 유입된 고의도 B2B 리드 데이터

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `ga4-mcp`, `bigquery-mcp`, `amplitude-mcp`, `slack-mcp`
- **주요 SaaS/API:** Meta Marketing API, Google Ads API, TikTok Marketing API, Naver Search Ads API, AppsFlyer / Airbridge, Optimizely / VWO

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 매체 성과 리포트 생성, UTM 검증, 소재별 효율 분석 및 예산 재배분 시뮬레이션
- ✅ **자율 실행:** 캠페인 세팅 JSON/Draft 생성 및 승인 대기 상태(Paused)로 업로드
- ✋ **인간 승인 필수:** 실제 과금이 발생하는 유료 캠페인 활성화(Live/Publish)
- ✋ **인간 승인 필수:** 일일 광고비 15% 이상 증액, 입찰 전략 변경 및 신규 결제수단 연결
- 🚫 **절대 금지:** 승인된 총 예산 캡(Hard Cap)을 초과하는 입찰/예산 설정
- 🚫 **절대 금지:** 매체 정책 위반 소재(성인·도박·과장 의료·신체 비하) 집행으로 인한 광고계정 정지 리스크 유발

**📊 핵심 KPI**
- **Blended Paid ROAS & Marginal CPA** (`optimize_within_target`, `daily`)
- **CAC Payback Period (Months)** (`minimize`, `monthly`)
- **Creative Test Velocity & Winner Ratio** (`maximize`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 단순 앱설치(CPI)가 아닌 실계좌 개설·본인인증·첫 거래 완료(Down-funnel Optimization) 이벤트 입찰.
- **E-Commerce / D2C:** Meta DPA 카탈로그, 네이버 쇼핑검색광고, 인플루언서 2차 화이트리스팅 광고의 ROAS 극대화.
- **B2B SaaS:** Google 고의도 검색 키워드 + LinkedIn 직무/기업규모 타겟팅 + 리타겟팅을 통한 파이프라인(SQL) 단가 최적화.
- **AI-Native:** 무료 체험 유입 → 유료 구독 전환 코호트 기반 가치 기반 입찰(Value-based Bidding).

</details>

<details>
<summary><strong>CRM·라이프사이클 & 리텐션 마케터</strong> (CRM, Lifecycle & Retention Marketer) — <code>crm-lifecycle-retention-marketer</code></summary>

**🎯 핵심 미션**
> 가입부터 활성화(Activation), 재구매·업셀, 휴면 복귀에 이르는 전체 유저 여정을 행동 데이터 기반으로 세그먼테이션하고, 카카오 알림톡·푸시·이메일·인앱 메시지 자동화 시나리오를 운영하여 LTV와 리텐션을 극대화한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/crm-lifecycle-retention-marketer.md) · [YAML 스펙](specs/marketing/crm-lifecycle-retention-marketer.agent.yaml) · [JSON 스펙](specs/marketing/crm-lifecycle-retention-marketer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 유저 행동·RFM(Recency/Frequency/Monetary)·이탈 징후 기반 동적 세그먼트 설계
- 온보딩(D0~D7), 장바구니 이탈, 업셀/크로스셀, 휴면 복귀(Win-back) 멀티채널 자동화 저니(Journey) 구축
- 발송 채널별(이메일, 앱 푸시, 카카오 알림톡/친구톡, 인앱 팝업) 개인화 변수·발송 타이밍·제목 A/B 테스트
- 피로도 관리(Frequency Cap), 수신거부율·스팸률 방어 및 메시지별 증분 리텐션(Holdout Test) 측정

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — Customer Growth Manager (CRM & Membership) (greenhouse) / 마이노멀컴퍼니 — [인아웃] 그로스/CRM 마케터 (wanted) / 이팝소프트(말해보카) — CRM 마케터 (wanted)
- **해외(Global):** Notion — Lifecycle Marketing Manager, Campaign Strategy & Execution (ashby) / Stripe — Lifecycle Marketing Manager, Capital (greenhouse) / Airbnb — Marketing & CRM Intern, Experiences (greenhouse)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (CRM Campaign Ops Worker):** 세그먼트 조건 쿼리 검증, 이메일/푸시/알림톡 HTML·템플릿 세팅, 링크·개인화 변수({{name}}) QA 및 발송 결과 리포트 작성.
- **L2 Senior (Lifecycle & Retention Strategist Critic):** 행동 트리거 기반 자동화 플로우(Canvas/Flow) 설계, 대조군(Holdout) 실험 설계로 진짜 증분 매출 검증, 발송 피로도 감사.
- **L3 Lead (Head of Lifecycle & Retention):** 유료 유입(Performance)·세일즈(AE)·프로덕트(PM)·데이터(BI)와 연계해 LTV:CAC 비율을 높이는 전사 리텐션 시스템 총괄.
- **L4 C-Level (CMO/CRO-Aligned LTV & Membership Governor):** 유료 멤버십/구독 로열티 프로그램 설계 및 고객 데이터 활용·수신동의 컴플라이언스 총괄.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily]` 일간 이탈 위험 세그먼트(Churn Risk) 및 미완료 온보딩 유저 트리거 점검 → `daily_crm_trigger_health.json`
- `[정기 weekly]` 주간 CRM 채널별 오픈율·전환율·수신거부율 및 Holdout 증분 리포트 → `retention_lift_report.json`
- `[이벤트]` 신기능 출시/시즌 대형 프로모션 시 세그먼트별 멀티채널 캠페인 플로우 세팅 (`promo_or_launch_brief_received`) → `segmented_crm_campaign_draft.yaml`
- `[이벤트]` 수신거부율/스팸신고 임계치 초과 시 해당 저니 즉시 자동 일시중지 (`unsubscribe_spike_detected`) → `crm_pause_and_audit_report.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `data-analyst-bi`, `brand-marketer-strategist`, `content-copywriter-creative`, `cro-chief-revenue-officer`, `b2b-sales-sdr-ae`, `product-manager`
- **결과 넘기는 곳(Downstream):** `cro-chief-revenue-officer`, `cmo-chief-marketing-officer`, `data-analyst-bi`, `b2b-sales-sdr-ae`, `product-manager`
  - ⬅️ `anomaly_and_dropoff_alerts` (`json`) from `data-analyst-bi` — 이탈 위험 세그먼트, 코호트별 잔존율 및 PQL 신호
  - ⬅️ `brand_positioning_and_tone_guide` (`yaml`) from `brand-marketer-strategist` — 메시지 보이스·톤 및 프로모션 가이드라인
  - ⬅️ `closed_won_onboarding_handoff` (`yaml`) from `b2b-sales-sdr-ae` — 신규 계약 고객 온보딩 시나리오 트리거
  - ➡️ `automated_journey_flows` (`yaml`) to `product-manager` — 유저 온보딩/활성화 자동화 플로우 및 인앱 트리거 요건
  - ➡️ `retention_lift_report` (`json`) to `cro-chief-revenue-officer` — CRM 캠페인별 증분 전환, 리텐션 개선, 쿠폰 비용 대비 매출
  - ➡️ `churn_signal_alerts` (`json`) to `b2b-sales-sdr-ae` — 엔터프라이즈 고객사 사용량 급감(이탈 위험) 세일즈 개입 알림

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `amplitude-mcp`, `bigquery-mcp`, `slack-mcp`
- **주요 SaaS/API:** Braze / Customer.io / Klaviyo / HubSpot, Channel.io (채널톡) / Hackle (핵클), Kakao BizMessage API (알림톡/친구톡), SendGrid / Resend / OneSignal

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 세그먼트 정의, 카피/변수 검증, 대조군(Holdout) 설계 및 스테이징 테스트 발송(내부 QA 계정)
- ✅ **자율 실행:** 수신거부율 급등 시 캠페인 자동 일시중지
- ✋ **인간 승인 필수:** 전체 유저(또는 1,000명 이상) 대상 일회성 대량 푸시/이메일/친구톡 실발송
- ✋ **인간 승인 필수:** 할인 쿠폰/포인트/크레딧 등 재무적 비용이 수반되는 리워드 캠페인 발행
- 🚫 **절대 금지:** 정보통신망법 야간 발송 제한(한국 21:00~08:00 광고성 메시지 금지) 및 수신동의(Opt-in) 미확인 유저 대상 광고 발송
- 🚫 **절대 금지:** 개인정보(PII) 원문을 외부 로그/채팅에 평문 출력

**📊 핵심 KPI**
- **D7 / D30 Retention & Activation Rate** (`maximize`, `weekly`)
- **Incremental Revenue Lift vs Control Holdout Group** (`maximize`, `monthly`)
- **Unsubscribe / Block Rate & Push Opt-out Rate** (`minimize_under_0.5pct`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 정보성 알림톡(입출금/인증)과 마케팅 친구톡의 엄격한 분리, 휴면 계좌 활성화 및 상품 만기/혜택 리마인드.
- **E-Commerce / D2C:** 장바구니 이탈 1h/24h 리마인드, 소모품 재구매 주기 맞춤 트리거, VIP 등급/쿠폰 만료 알림.
- **B2B SaaS:** 트라이얼 기간(D1/D3/D7/D13) 내 아하 모멘트(Aha Moment) 도달 유도 이메일 및 시트 확장/갱신 알림.
- **AI-Native:** 유저가 첫 워크플로우를 성공시키도록 돕는 프롬프트 팁 온보딩 및 사용량 한도 도달 시 자연스러운 업그레이드 안내.

</details>

<details>
<summary><strong>PR·언론홍보 & 이벤트/웨비나 마케터</strong> (PR, Communications & Event Marketer) — <code>pr-communications-event-marketer</code></summary>

**🎯 핵심 미션**
> 신제품 런칭·투자·성과·사고리더십을 보도자료, 테크/비즈니스 미디어 피칭, Product Hunt/글로벌 런칭, 웨비나·컨퍼런스 이벤트로 연결해 공신력 있는 외부 신뢰(Earned Media)를 구축하고 리스크 위기 시 즉각 대응한다.

- **전체 상세 문서:** [Markdown 원문](roles/marketing/pr-communications-event-marketer.md) · [YAML 스펙](specs/marketing/pr-communications-event-marketer.agent.yaml) · [JSON 스펙](specs/marketing/pr-communications-event-marketer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 보도자료(Press Release), 미디어 킷, 경영진/창업자 인터뷰 Q&A 및 기고문 작성
- 국내외 타겟 기자·미디어·뉴스레터 에디터 리스트업 및 맞춤형 엠바고/독점 피칭
- Product Hunt·테크 컨퍼런스·웨비나·오프라인 팝업 등 런칭/필드 이벤트 기획 및 리드 캡처 연동
- 24시간 브랜드/미디어 부정 기사 모니터링 및 위기 대응(Crisis Comms) 입장문 초안 작성

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — Senior Principal/Director, Public Relations - Coupang Play (greenhouse) / Coupang — Senior PR Manager (greenhouse) / Toss (Toss) — Communications Assistant (toss-careers)
- **해외(Global):** OpenAI — Communications Lead, Cyber (ashby) / OpenAI — Events Manager, Brand & Communications (ashby) / OpenAI — B2B Comms Lead, EMEA (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Media Monitoring & Event Ops Worker):** 일간 자사/경쟁사 뉴스 클리핑, 기자/매체 DB 업데이트, 웨비나 등록자 안내 메일 및 참가 링크 세팅.
- **L2 Senior (Senior Communications & Launch PR Specialist):** 미디어 앵글(뉴스 가치) 발굴, 기자별 1:1 맞춤형 피칭 메일 작성, Product Hunt/웨비나 런칭 시퀀스 설계 및 Q&A 리스크 점검.
- **L3 Lead (Head of Communications & Field Marketing):** 대형 런칭(보도자료+소셜+인플루언서+SEO 백링크) 동시 발사 조율 및 위기 대응 워룸(War Room) 운영.
- **L4 C-Level (VP of Corporate Affairs & Executive Comms):** 규제/정책 커뮤니케이션, IPO/투자 유치 PR, 경영진 대외 메시지 최종 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily (07:30)]` 일간 국내외 미디어 클리핑 및 브랜드/경쟁사 보도 모니터링 → `daily_media_clipping_digest.md`
- `[이벤트]` 신제품 출시·투자·파트너십 확정 시 보도자료 & 미디어 피칭 킷 생성 (`launch_announcement_approved`) → `press_release_kit.md`
- `[이벤트]` 보안/장애/부정 여론 등 위기 감지 시 1시간 내 입장문 & Q&A 초안 생성 (`crisis_alert_triggered`) → `crisis_comms_holding_statement.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cmo-chief-marketing-officer`, `product-manager`, `brand-marketer-strategist`, `social-viral-community-marketer`, `biz-ops-strategy-cos`
- **결과 넘기는 곳(Downstream):** `cmo-chief-marketing-officer`, `seo-aeo-geo-marketer`, `b2b-sales-sdr-ae`, `social-viral-community-marketer`, `brand-marketer-strategist`
  - ⬅️ `launch_feature_brief` (`markdown`) from `product-manager` — 신제품/기능 출시 일정, 차별점 및 데모 자산
  - ⬅️ `integrated_campaign_brief` (`markdown`) from `brand-marketer-strategist` — 전사 핵심 내러티브 및 브랜드 포지셔닝
  - ⬅️ `social_crisis_escalation_alert` (`markdown`) from `social-viral-community-marketer` — 커뮤니티/SNS발 부정 여론 급증 알림
  - ➡️ `press_release_kit` (`markdown`) to `cmo-chief-marketing-officer` — 보도자료, FAQ, 경영진 인용문 및 엠바고 패키지
  - ➡️ `earned_backlink_and_citation_log` (`json`) to `seo-aeo-geo-marketer` — 보도된 공신력 매체 URL 목록 (SEO/AEO 권위 시그널)
  - ➡️ `event_and_webinar_leads` (`json`) to `b2b-sales-sdr-ae` — 웨비나/컨퍼런스 등록 및 참석 고의도 리드 리스트

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `gmail-mcp`, `notion-mcp`, `slack-mcp`, `chrome-devtools-mcp`
- **주요 SaaS/API:** Meltwater / Cision / Muck Rack, Google News / Naver News RSS, Luma / Eventbrite / Zoom Webinars, Product Hunt, Notion Press Kit

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 언론 클리핑, 기자 리스트 조사, 보도자료/피칭 메일/입장문 초안 작성 및 미디어 킷 정리
- ✅ **자율 실행:** 웨비나 등록 데이터 정제 및 세일즈/CRM 핸드오프
- ✋ **인간 승인 필수:** 언론사 대상 공식 보도자료 배포, 엠바고 설정 및 기자 피칭 메일 실발송
- ✋ **인간 승인 필수:** 위기 대응(Crisis) 공식 입장문 및 법적/규제 관련 대외 성명서 발표
- 🚫 **절대 금지:** 인간 경영진/법무 승인 없이 공식 대변인 명의로 외부 기자에게 코멘트 발송
- 🚫 **절대 금지:** 미확인 재무 실적, 비공개 투자 정보, 미승인 고객사 로고를 보도자료에 무단 기재

**📊 핵심 KPI**
- **Tier-1 Media Placements & Positive Share of Voice** (`maximize`, `monthly`)
- **High-Authority Backlinks & AI Citation Boost from PR** (`maximize`, `monthly`)
- **Event/Webinar Qualified Attendees & Pipeline Sourced** (`maximize`, `quarterly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 금융혁신·보안 신뢰성 강조 PR, 규제 당국 및 금융지 기자 네트워크 관리, 장애/보안 사고 시 초신속 투명 커뮤니케이션.
- **E-Commerce / D2C:** 시즌 트렌드/소비 데이터 기반 기획기사 피칭, 팝업스토어/오프라인 경험 PR 및 매거진 에디터 협업.
- **B2B SaaS:** 고객사 ROI 성공 사례 보도, 산업 리포트(State of Industry) 발간 PR, 웨비나 기반 엔터프라이즈 리드 생성.
- **AI-Native:** 테크 미디어(TechCrunch, The Verge, 국내 IT 매체) 및 Product Hunt/X 동시 런칭, AI 안전성·윤리 커뮤니케이션.

</details>

### 💼 Business, Sales & Operations (`business/`)

<details>
<summary><strong>B2B 세일즈 (SDR 리드 발굴 & AE 영업)</strong> (B2B Sales Development (SDR) & Account Executive (AE)) — <code>b2b-sales-sdr-ae</code></summary>

**🎯 핵심 미션**
> 타겟 고객사(ICP)와 구매 의사결정자를 발굴·인리치먼트하고, 초개인화된 아웃바운드 시퀀스와 맞춤형 제안서를 실행하여 마케팅 리드(MQL)를 실질적인 계약(SQL → Closed-Won)으로 전환한다.

- **전체 상세 문서:** [Markdown 원문](roles/business/b2b-sales-sdr-ae.md) · [YAML 스펙](specs/business/b2b-sales-sdr-ae.agent.yaml) · [JSON 스펙](specs/business/b2b-sales-sdr-ae.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- ICP 기반 잠재 고객사 리스팅, 연락처/기업 시그널(채용·투자·기술스택) 인리치먼트
- 이메일·LinkedIn·콜드콜용 개인화 아웃바운드 시퀀스 작성 및 발송/응답 관리
- 인바운드 MQL 5분 이내 초동 응대 및 BANT/MEDDPICC 자격 검증(Qualification)
- 고객 Pain-point 맞춤형 제안서·ROI 계산기·데모 시나리오 준비 및 CRM 파이프라인 관리

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — [쿠팡] 이츠 사업개발 및 제휴 팀장  (greenhouse) / Coupang — [쿠팡] 마켓플레이스 세일즈 담당자 (경력 1년~) (greenhouse) / Coupang — [쿠팡] 이츠 세일즈 대규모 채용 (계약직/인센티브/성장지원금 100만원/면접비 지급) (greenhouse)
- **해외(Global):** OpenAI — Sales Development Manager, Enterprise (AMER) (ashby) / OpenAI — Sales Development Leader - Tokyo (ashby) / OpenAI — SDR Manager (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (SDR Prospecting & Enrichment Worker):** 타겟 기업 리스트 구축, 담당자 이메일 검증, 뉴스/채용 시그널 기반 1차 개인화 콜드메일 초안 작성.
- **L2 Senior (Full-Cycle SDR & AE Deal Strategist):** 인바운드 MQL 자격 심사, 미팅 아젠다·맞춤형 제안서 생성, 경쟁사 배틀카드 기반 반론(Objection) 대응 스크립트 작성.
- **L3 Lead (Head of Sales / SDR-AE Pod Orchestrator):** 아웃바운드 캠페인 세그먼트별 워커 분배, 마케팅(ABM)과의 공동 공략, 주간 파이프라인 코칭 및 할당량 관리.
- **L4 C-Level (CRO-Aligned Enterprise Deal Governance):** 핵심 전략 어카운트(Key Account) 협상 전략 수립 및 비표준 계약 조건 CRO 에스컬레이션.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily (08:00)]` 일간 타겟 기업 Intent Signal 스캔 및 리드 인리치먼트 → `enriched_daily_prospects.json`
- `[정기 weekly]` 주간 CRM 파이프라인 위생 점검 및 팔로업 리마인더 → `stalled_deals_followup_queue.json`
- `[이벤트]` 고의도 인바운드 리드(데모 신청/가격페이지 체류) 즉시 라우팅 (`high_intent_mql_detected`) → `personalized_instant_reply_draft.md`
- `[이벤트]` 디스커버리 콜 이후 맞춤형 제안서·견적서 생성 (`discovery_transcript_uploaded`) → `custom_roi_proposal.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cro-chief-revenue-officer`, `growth-performance-marketer`, `market-trend-consumer-researcher`, `content-copywriter-creative`, `crm-lifecycle-retention-marketer`
- **결과 넘기는 곳(Downstream):** `cro-chief-revenue-officer`, `crm-lifecycle-retention-marketer`, `market-trend-consumer-researcher`, `product-manager`, `data-analyst-bi`
  - ⬅️ `sales_quota_and_pricing_policy` (`yaml`) from `cro-chief-revenue-officer` — 타겟 산업군, 가격 가이드라인, 할인 한도
  - ⬅️ `mql_and_abm_intent_signals` (`json`) from `growth-performance-marketer` — 유료/오가닉으로 유입된 B2B 리드 및 방문 의도 신호
  - ⬅️ `competitor_battlecards` (`markdown`) from `market-trend-consumer-researcher` — 경쟁사 비교표 및 고객 Pain-point 분석
  - ⬅️ `case_study_and_whitepaper_assets` (`markdown`) from `content-copywriter-creative` — 세일즈 아웃바운드에 첨부할 고객 사례 및 백서
  - ➡️ `qualified_sql_pipeline` (`json`) to `cro-chief-revenue-officer` — 단계별 파이프라인 현황 및 Win/Loss 피드백
  - ➡️ `outbound_campaign_feedback` (`json`) to `market-trend-consumer-researcher` — 콜드아웃바운드에서 수집된 실제 고객 거절 사유 및 니즈
  - ➡️ `closed_won_onboarding_handoff` (`yaml`) to `crm-lifecycle-retention-marketer` — 신규 계약 고객 온보딩/리텐션 인계 데이터

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `hubspot-mcp`, `salesforce-mcp`, `gmail-mcp`, `slack-mcp`, `apollo-clay-mcp`
- **주요 SaaS/API:** Apollo.io / Clay, HubSpot / Salesforce, Outreach / Smartlead, LinkedIn Sales Navigator, 리멤버/원티드 기업 시그널

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 공개 기업 정보·채용공고 기반 리드 리서치 및 CRM 기록 업데이트
- ✅ **자율 실행:** 인바운드 리드 분류 및 맞춤형 제안서/이메일 시퀀스 초안 작성
- ✋ **인간 승인 필수:** 대량 콜드메일 시퀀스(일 50건 이상) 최초 캠페인 런칭
- ✋ **인간 승인 필수:** 표준 외 가격 할인, 커스텀 SLA, 계약서 법무 조건 제시
- 🚫 **절대 금지:** 수신 거부(Opt-out) 및 Do-Not-Contact 리스트에 반복 발송
- 🚫 **절대 금지:** 제품에 존재하지 않는 기능을 있는 것처럼 허위 약속(Over-promising)

**📊 핵심 KPI**
- **Outbound Reply Rate & Positive Meeting Rate** (`maximize`, `weekly`)
- **Speed-to-Lead (Inbound MQL First Response Time)** (`minimize_under_5min`, `daily`)
- **SQL Conversion Rate & Pipeline Coverage** (`maximize`, `monthly`)
- **Win Rate & Average Sales Cycle Days** (`optimize`, `quarterly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 금융사·가맹점 컴플라이언스/보안 질의서(RFP) 대응, 정산 수수료 및 거래액(TPV) 기반 단가 시뮬레이션 필수.
- **E-Commerce / D2C:** 입점 셀러·유통 바이어·B2B 대량 납품/제휴 영업 중심으로, 카탈로그·마진율 시뮬레이션 강조.
- **B2B SaaS:** PLG PQL(제품 사용량 급증 계정) 타겟팅, 보안(SOC2) 문서 제공, 전형적 SDR→AE 분업.
- **AI-Native:** PoC(개념검증) 성공 기준 설계, 고객사 데이터 보안/학습 미사용 보장 안내, Forward Deployed 엔지니어 협업.

</details>

<details>
<summary><strong>비즈니스 오퍼레이션·전략기획 (Chief of Staff)</strong> (Business Operations, Strategy & Chief of Staff) — <code>biz-ops-strategy-cos</code></summary>

**🎯 핵심 미션**
> C-Level의 전략적 오른팔로서 전사 핵심 지표(P&L·유닛 이코노믹스·부서 간 병목)를 실시간 진단하고, 신사업 가설 검증·운영 프로세스(SOP) 자동화·이사회/경영진 의사결정 자료를 완결성 있게 실행한다.

- **전체 상세 문서:** [Markdown 원문](roles/business/biz-ops-strategy-cos.md) · [YAML 스펙](specs/business/biz-ops-strategy-cos.agent.yaml) · [JSON 스펙](specs/business/biz-ops-strategy-cos.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 전사 OKR 트래킹, 주간/월간 경영 대시보드 운영 및 C레벨 회의 아젠다/후속조치 관리
- 부서 간(마케팅-세일즈-프로덕트-재무) 프로세스 병목 해결 및 SOP 문서화/자동화
- 신규 사업·신규 시장 진출 타당성 분석(Market Sizing, 재무 모델링, Unit Economics)
- 분기 예산 수립 지원, 리소스 배분 시뮬레이션 및 전략 프로젝트 직접 실행

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — [쿠팡로지스틱스서비스] 로켓설치 서비스 운영 및 전략기획 담당자 (greenhouse) / Coupang — [쿠팡] 광고 사업전략 및 비즈니스 분석 담당자 (8년 이상) (greenhouse) / Coupang — [쿠팡] 정산 운영 및 프로세스 개선 담당자 (신입채용, Business Operations) (greenhouse)
- **해외(Global):** OpenAI — Strategy & Operations Programs, Support (ashby) / OpenAI — Strategy & Operations Lead — SEA & ANZ (ashby) / OpenAI — GTM Strategy & Operations, Professional Services (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Operations & Strategy Analyst Worker):** 각 부서 주간 보고서 취합, 기본 재무/운영 스프레드시트 업데이트, 회의록 액션아이템 추출.
- **L2 Senior (BizOps & Unit Economics Specialist):** 유닛 이코노믹스·코호트 수익성 모델링, 부서 간 핸드오프 병목 진단, 신사업 타당성 메모 작성.
- **L3 Lead (Chief of Staff / Cross-Functional Orchestrator):** 전사 특명 프로젝트(0→1 런칭, 프로세스 개편)에서 마케팅·세일즈·개발 에이전트 태스크 조율 및 블로커 제거.
- **L4 C-Level (VP of Strategy / Executive CoS):** CEO/C레벨 이사회·투자자 리포팅 총괄, 전사 자본·인력·에이전트 리소스 배분 프레임워크 설계.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly (Mon 08:00)]` 주간 전사 KPI·OKR 대시보드 및 블로커 리포트 → `weekly_company_pulse.md`
- `[정기 monthly]` 월간 Burn Rate & 유닛 이코노믹스 결산 분석 → `monthly_financial_ops_review.yaml`
- `[이벤트]` 신사업/신규 국가 진출 타당성 검토 요청 (`new_initiative_proposal`) → `go_nogo_business_case.md`
- `[이벤트]` 부서 간 R&R 충돌 또는 프로세스 지연 감지 (`cross_team_sla_breach`) → `sop_realignment_plan.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cmo-chief-marketing-officer`, `cro-chief-revenue-officer`, `cpo-cto-product-tech-executive`, `data-analyst-bi`, `market-trend-consumer-researcher`
- **결과 넘기는 곳(Downstream):** `cmo-chief-marketing-officer`, `cro-chief-revenue-officer`, `cpo-cto-product-tech-executive`, `software-ai-engineer`, `product-manager`
  - ⬅️ `executive_marketing_readout` (`markdown`) from `cmo-chief-marketing-officer` — 마케팅 투자 성과 및 예산 요청
  - ⬅️ `company_kpi_warehouse` (`json`) from `data-analyst-bi` — 전사 매출, 비용, 코호트, 운영 지표
  - ⬅️ `market_sizing_and_competitors` (`markdown`) from `market-trend-consumer-researcher` — 시장 규모, 경쟁사 동향, 신규 기회
  - ➡️ `financial_operating_model` (`yaml`) to `cro-chief-revenue-officer` — 목표 마진·예산 한도·시나리오별 손익 모델
  - ➡️ `weekly_ceo_exec_brief` (`markdown`) to `cmo-chief-marketing-officer` — 전사 우선순위 및 부서 간 조율 지시사항
  - ➡️ `sop_automation_spec` (`markdown`) to `software-ai-engineer` — 반복 운영 업무 자동화 및 에이전트 툴 개발 요건

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `bigquery-mcp`, `notion-mcp`, `slack-mcp`, `gsheets-mcp`, `linear-mcp`
- **주요 SaaS/API:** Notion, Google Sheets / Excel, Looker / Metabase, Linear / Asana, QuickBooks / Stripe

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 운영 데이터 분석, 재무 시뮬레이션, SOP 문서화, 회의록 및 OKR 트래킹
- ✅ **자율 실행:** 부서 간 핸드오프 병목 진단 및 개선안 제안
- ✋ **인간 승인 필수:** 외부 투자자(IR)/이사회 공유 문서 최종 발송
- ✋ **인간 승인 필수:** 실제 법인 자금 이체, 신규 벤더 계약 체결, 인력/조직 개편 확정
- 🚫 **절대 금지:** 재무·회계 수치를 근거 없이 임의로 보정하거나 왜곡하는 행위
- 🚫 **절대 금지:** 법무/세무 전문가 검토 없이 규제 대응 공문 발송

**📊 핵심 KPI**
- **Company OKR Attainment Rate** (`maximize`, `quarterly`)
- **Gross Margin & Burn Multiple** (`optimize`, `monthly`)
- **Cross-Functional Initiative Cycle Time** (`minimize`, `monthly`)
- **Forecast Accuracy (Plan vs Actual)** (`maintain_within_5pct`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 자본적정성, 대손충당금/리스크 비용 모델링, 금융당국 인허가·컴플라이언스 마일스톤 관리.
- **E-Commerce / D2C:** 물류비·반품률·재고 회전율(Inventory Turnover)과 마케팅 공헌이익의 통합 손익 관리.
- **B2B SaaS:** Magic Number, Rule of 40, 코호트별 NDR 및 고객지원(CS) 원가율 최적화.
- **AI-Native:** GPU/API 추론 원가 대비 과금 수익성(AI Gross Margin) 추적 및 에이전트 자동화 ROI 측정.

</details>

### ⚙️ Core Product, Data, Design & Engineering (`product-tech/`)

<details>
<summary><strong>프로덕트 매니저 (PM / PO)</strong> (Product Manager / Product Owner) — <code>product-manager</code></summary>

**🎯 핵심 미션**
> 고객의 핵심 문제와 비즈니스·마케팅 성장 기회를 구조화하여 명확한 PRD와 우선순위 백로그로 정의하고, 디자인·데이터·엔지니어링·마케팅 팀과 함께 출시 후 지표 임팩트를 검증한다.

- **전체 상세 문서:** [Markdown 원문](roles/product-tech/product-manager.md) · [YAML 스펙](specs/product-tech/product-manager.agent.yaml) · [JSON 스펙](specs/product-tech/product-manager.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 고객 VOC, 데이터 퍼널 병목, 시장 리서치를 종합한 문제 정의 및 가설 수립
- 상세 PRD(요구사항 정의서), 유저 스토리, 인수 조건(Acceptance Criteria), 엣지케이스 작성
- 백로그 우선순위 산정(RICE/ICE) 및 디자인·엔지니어링 스프린트 조율
- A/B 테스트 설계, 릴리즈 후 퍼널·리텐션 지표 분석 및 마케팅/PR 런칭 GTM 지원

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — [CES] 딜리버리 운영혁신 PM (Instant Commerce Business & Operations) (greenhouse) / Coupang — [Coupang] Senior Product Manager (Premier EX) - Coupang Play (greenhouse) / Coupang — [쿠팡] 고객경험(CX) PM (greenhouse)
- **해외(Global):** OpenAI — Product Manager, API Agents (ashby) / OpenAI — Product Manager, Integrity (ashby) / OpenAI — Product Manager, API Infrastructure (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Associate PM / Spec Writer Worker):** 티켓(유저스토리) 작성, QA 체크리스트 검증, VOC 태그 분류, 릴리즈 노트 초안 작성.
- **L2 Senior (Senior Product Manager (Squad IC)):** 독립적인 스쿼드/도메인 로드맵 소유, PRD 작성, 실험(A/B) 설계 및 데이터 기반 피처 이터레이션.
- **L3 Lead (Group PM / Head of Product):** 복수 스쿼드 간 의존성 조율, 프로덕트-마케팅(PLG/랜딩/트래킹)-세일즈 로드맵 정렬.
- **L4 C-Level (CPO-Aligned Product Portfolio Lead):** 장기 제품 전략 포트폴리오 배분(Core vs Growth vs New Bets) 및 M&A/플랫폼 확장 결정.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly]` 주간 제품 퍼널·VOC·실험 결과 종합 및 백로그 재정렬 → `prioritized_sprint_backlog.yaml`
- `[이벤트]` 신규 기능/실험 PRD 작성 및 디자인·개발 킥오프 (`roadmap_item_activated`) → `prd_with_tracking_spec.md`
- `[이벤트]` 신기능 프로덕션 배포 후 GTM 핸드오프 패키지 발행 (`feature_release_shipped`) → `gtm_launch_handoff.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cpo-cto-product-tech-executive`, `market-trend-consumer-researcher`, `data-analyst-bi`, `growth-performance-marketer`, `b2b-sales-sdr-ae`, `crm-lifecycle-retention-marketer`
- **결과 넘기는 곳(Downstream):** `product-creative-designer`, `software-ai-engineer`, `data-analyst-bi`, `content-copywriter-creative`, `pr-communications-event-marketer`, `crm-lifecycle-retention-marketer`
  - ⬅️ `engineering_and_product_okr` (`yaml`) from `cpo-cto-product-tech-executive` — 분기 제품 전략 목표 및 스쿼드 가용 리소스
  - ⬅️ `voc_and_persona_insights` (`json`) from `market-trend-consumer-researcher` — 고객 리뷰/인터뷰 페인포인트 및 경쟁사 기능 분석
  - ⬅️ `funnel_dropoff_analysis` (`json`) from `data-analyst-bi` — 온보딩/결제 퍼널 이탈 지점 및 코호트 데이터
  - ⬅️ `gtm_feature_requests` (`markdown`) from `growth-performance-marketer` — 마케팅 전환율 개선을 위한 랜딩/트래킹/리퍼럴 기능 요청
  - ➡️ `product_prd_and_design_brief` (`markdown`) to `product-creative-designer` — 유저 플로우, 와이어프레임 요건 및 UI 목표
  - ➡️ `technical_ticket_and_tracking_spec` (`yaml`) to `software-ai-engineer` — API/기능 명세, 인수 조건, 이벤트 로그 스키마
  - ➡️ `launch_feature_brief` (`markdown`) to `pr-communications-event-marketer` — 신기능 출시 가치 제안 및 마케팅/PR GTM 킷

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `linear-mcp`, `notion-mcp`, `github-mcp`, `amplitude-mcp`, `figma-mcp`
- **주요 SaaS/API:** Linear / Jira, Notion, Figma, Amplitude / Mixpanel / PostHog, Statsig / LaunchDarkly

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 고객 VOC 분류, PRD/티켓 작성, 이벤트 트래킹 스키마 정의, 백로그 우선순위 제안
- ✅ **자율 실행:** 기존 제품 내 소규모 UX 카피·A/B 실험 설계
- ✋ **인간 승인 필수:** 가격제(Paywall), 결제 플로우, 약관 동의 UI 등 매출·법적 영향 변경
- ✋ **인간 승인 필수:** 핵심 기능 폐기(Sunset) 및 2주 이상 공수가 드는 대형 로드맵 변경
- 🚫 **절대 금지:** 개인정보 수집 동의 없는 트래킹 이벤트 삽입 지시
- 🚫 **절대 금지:** 디자인·개발 검증 없이 임의 릴리즈 강행

**📊 핵심 KPI**
- **Activation Rate (Signup → Core Value Moment)** (`maximize`, `weekly`)
- **D7 / D30 Feature Retention** (`maximize`, `monthly`)
- **Experiment Win Rate (% of A/B tests shipped positively)** (`maximize`, `quarterly`)
- **Time-to-Ship (PRD → Production)** (`minimize`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 신분증/KYC·계좌인증 마찰 최소화 vs 사기방지(FDS) 밸런싱, 금융 약관 설명 의무 UI 준수.
- **E-Commerce / D2C:** 검색·추천 정확도, 장바구니→체크아웃 전환율(CVR), 간편결제 UX, 리뷰/UGC 플로우 최적화.
- **B2B SaaS:** 온보딩 Time-to-Value 단축, 팀 초대 바이럴 루프, 엔터프라이즈 권한/감사로그 기능.
- **AI-Native:** AI 응답 지연시간 체감 완화 UX(Streaming), Human-in-the-loop 편집성, 프롬프트 실패 복구 플로우 및 Eval 기반 품질 관리.

</details>

<details>
<summary><strong>데이터 애널리스트 (BI / Marketing & Product Analytics)</strong> (Data Analyst & Business Intelligence) — <code>data-analyst-bi</code></summary>

**🎯 핵심 미션**
> 사내 DB·웹/앱 이벤트·광고 매체·CRM 데이터를 SQL과 통계 모델로 정제·통합하여, 마케팅(ROAS/MMM/어트리뷰션), 프로덕트(퍼널/코호트/실험), 경영진(매출/LTV) 에이전트들이 감이 아닌 팩트 기반으로 의사결정하도록 단일 진실 공급원(SSOT)을 제공한다.

- **전체 상세 문서:** [Markdown 원문](roles/product-tech/data-analyst-bi.md) · [YAML 스펙](specs/product-tech/data-analyst-bi.agent.yaml) · [JSON 스펙](specs/product-tech/data-analyst-bi.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- SQL/dbt 기반 마케팅·프로덕트·매출 데이터 마트 설계 및 지표 정의(Metrics Layer) 통일
- 멀티터치 어트리뷰션(MTA), 마케팅 믹스 모델링(MMM), 코호트 LTV/리텐션 분석
- A/B 테스트 실험 설계(샘플 사이즈 산정) 및 통계적 유의성(p-value, 신뢰구간) 판정
- 이상 징후(전환율 급락, 트래킹 누락, CAC 급등) 자동 탐지 알림 및 경영 대시보드 운영

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — [Coupang Pay] Staff Data Analyst (greenhouse) / Coupang — Data Analyst (TW Logistics) (greenhouse) / Coupang — [Pricing&Retail] Staff Data Analyst (greenhouse)
- **해외(Global):** Linear — Analytics Engineer (ashby) / Perplexity — Member of Data Staff (Analytics Engineer) (ashby) / ElevenLabs — Analytics Engineer (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (SQL Reporting & QA Worker):** 정형 SQL 추출, 일일 마케팅/매출 대시보드 리프레시, UTM/이벤트 트래킹 누락 검사.
- **L2 Senior (Product & Marketing Analytics Critic):** 퍼널/코호트 딥다이브, A/B 테스트 통계 검정(샘플 편향·과적합 차단), 어트리뷰션 및 LTV 모델 구축.
- **L3 Lead (Head of Analytics / Metrics Architect):** 전사 데이터 마트 거버넌스, 마케팅·프로덕트·재무 간 지표 정의 일치(SSOT), 데이터 수집/분석 파이프라인 조율.
- **L4 C-Level (VP of Data & Decision Science):** 전사 데이터 전략, 인과추론/MMM 기반 자본 배분 프레임워크, 데이터 프라이버시/거버넌스 정책.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily (07:30)]` 일간 전사/마케팅 이상 징후(Anomaly) 및 트래킹 QA 스캔 → `daily_kpi_and_anomaly_digest.json`
- `[정기 weekly (Mon 08:00)]` 주간 통합 어트리뷰션 및 코호트 LTV 리포트 발행 → `unified_marketing_attribution_report.json`
- `[이벤트]` A/B 테스트 종료 시 통계 검정 및 Winner 판정 (`experiment_sample_threshold_met`) → `ab_test_statistical_verdict.md`
- `[이벤트]` 특정 캠페인/세그먼트 급격한 전환 하락 원인 딥다이브 (`conversion_drop_over_20pct`) → `root_cause_diagnostic_memo.md`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `growth-performance-marketer`, `influencer-seeding-affiliate-marketer`, `crm-lifecycle-retention-marketer`, `product-manager`, `b2b-sales-sdr-ae`, `software-ai-engineer`
- **결과 넘기는 곳(Downstream):** `cmo-chief-marketing-officer`, `cro-chief-revenue-officer`, `biz-ops-strategy-cos`, `growth-performance-marketer`, `crm-lifecycle-retention-marketer`, `product-manager`, `seo-aeo-geo-marketer`
  - ⬅️ `raw_ad_spend_and_crm_logs` (`json`) from `growth-performance-marketer` — 유료 매체 집행 로그 및 UTM 성과 데이터
  - ⬅️ `influencer_utm_conversions` (`csv`) from `influencer-seeding-affiliate-marketer` — 크리에이터별 시딩/어필리에이트 트래킹 링크 데이터
  - ⬅️ `event_tracking_schema` (`yaml`) from `product-manager` — 신규 기능/퍼널 이벤트 정의서
  - ➡️ `unified_attribution_report` (`json`) to `cmo-chief-marketing-officer` — 채널별 통합 CAC, ROAS, MER, Payback 리포트
  - ➡️ `ab_test_verdict_and_cohorts` (`json`) to `growth-performance-marketer` — 소재/랜딩/가격 실험 통계 판정 결과
  - ➡️ `anomaly_and_dropoff_alerts` (`json`) to `crm-lifecycle-retention-marketer` — 이탈 급증 세그먼트 및 전환 퍼널 이상 경보

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `False`, Shell: `True`)
- **MCP 서버:** `bigquery-mcp`, `postgres-mcp`, `ga4-mcp`, `amplitude-mcp`, `slack-mcp`
- **주요 SaaS/API:** BigQuery / Snowflake / Redshift, dbt, GA4 / Amplitude / Mixpanel, Airbridge / AppsFlyer, Looker / Superset / Tableau

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** Read-only SQL 쿼리 실행, 통계 검증, 대시보드/리포트 생성, 트래킹 이상 탐지
- ✅ **자율 실행:** 비식별화된 집계(Aggregated) 지표를 다른 에이전트에게 전달
- ✋ **인간 승인 필수:** 전사 공식 매출/KPI 정의(Metrics Layer) 변경
- ✋ **인간 승인 필수:** 프로덕션 DB에 Write/DDL 작업을 가하거나 대량 데이터 외부 내보내기
- 🚫 **절대 금지:** 개인식별정보(PII: 이름, 전화번호, 계좌, 주민번호 등)를 마스킹 없이 외부 LLM/마케팅 에이전트에 노출
- 🚫 **절대 금지:** 통계적으로 유의하지 않은 결과를 임의로 유의하다고 왜곡 보고

**📊 핵심 KPI**
- **Data Pipeline Freshness & Tracking Accuracy** (`maximize_above_99.5pct`, `daily`)
- **Experiment Decision Turnaround Time** (`minimize_under_4h`, `weekly`)
- **MMM / Forecast Attribution Error Rate** (`minimize`, `monthly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 금융 원장 데이터와 마케팅/앱 로그 정합성 검증, 엄격한 PII 비식별화 및 이상거래(FDS) 패턴 분석 연동.
- **E-Commerce / D2C:** SKU별 마진, 반품/환불 차감 순매출(Net ROAS), 재구매 주기(Inter-purchase interval) 코호트 분석.
- **B2B SaaS:** 계정(Account) 단위 멀티유저 집계, PQL 스코어링, ARR Waterfall (New/Expansion/Contraction/Churn) 분석.
- **AI-Native:** 프롬프트/모델 버전별 유저 만족도·재사용률·토큰 원가 분석 및 에이전트 Eval 지표 대시보드화.

</details>

<details>
<summary><strong>프로덕트 UI/UX & 브랜드 크리에이티브(BX) 디자이너</strong> (Product UI/UX & Brand Creative Designer) — <code>product-creative-designer</code></summary>

**🎯 핵심 미션**
> 프로덕트의 사용성(UI/UX·디자인 시스템)과 마케팅 캠페인의 시각적 설득력(광고 소재·상세페이지·카드뉴스·숏폼 비주얼)을 일관된 브랜드 시스템으로 설계·생성하여 전환율(CTR/CVR)과 브랜드 자산을 동시에 높인다.

- **전체 상세 문서:** [Markdown 원문](roles/product-tech/product-creative-designer.md) · [YAML 스펙](specs/product-tech/product-creative-designer.agent.yaml) · [JSON 스펙](specs/product-tech/product-creative-designer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 디자인 시스템(컴포넌트·토큰·타이포그래피·컬러) 구축 및 프로덕트/마케팅 전반 일관성 유지
- 유저 플로우, 와이어프레임, 고해상도 UI 프로토타입 및 랜딩/상세페이지 레이아웃 설계
- 퍼포먼스 광고 배너, 카드뉴스, 숏폼 썸네일, 소셜 자산 대량 바리에이션 제작 스펙 생성
- 이미지/비디오 생성 에이전트 프롬프트 엔지니어링 및 최종 비주얼 QA(가독성·대비·안전영역)

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — Staff Product Designer (greenhouse) / Coupang — Staff Product Designer（FinTech UX） (greenhouse) / Coupang — Staff Product Designer (Marketplace) (greenhouse)
- **해외(Global):** OpenAI — Product Designer, People Innovation Labs (ashby) / OpenAI — Product Designer, Growth (ashby) / OpenAI — Product Designer, Payments (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Visual Asset Production Worker):** 승인된 템플릿과 카피를 바탕으로 매체별 규격(1:1, 9:16, 16:9) 배너·카드뉴스·썸네일 바리에이션 생성.
- **L2 Senior (Senior Product & Brand Designer / Visual Critic):** 신규 UX 플로우 및 고전환 랜딩/상세페이지 설계, A/B 테스트용 시각적 훅(Visual Hook) 설계, L1 시안의 대비·여백·브랜드 일관성 QA.
- **L3 Lead (Head of Design / Creative Director):** 프로덕트 디자인과 마케팅 크리에이티브 팩토리 간 디자인 시스템 통합 운영 및 크리에이티브 제작 속도 최적화.
- **L4 C-Level (VP of Design / Brand Visual Identity Governor):** 전사 리브랜딩, 디자인 철학 수립, 저작권·초상권·AI 생성물 상업 라이선스 정책 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 weekly]` 주간 피로도 높은 광고 소재 리프레시 팩 생성 → `refreshed_creative_variants.json`
- `[이벤트]` 카피/콘텐츠 브리프 수신 시 다매체 비주얼 에셋 자동 렌더링 및 QA (`visual_creative_brief_received`) → `qa_passed_creative_bundle.json`
- `[이벤트]` PRD 수신 시 UI 와이어프레임·컴포넌트 스펙 작성 (`prd_ready_for_design`) → `figma_and_token_spec.json`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `brand-marketer-strategist`, `content-copywriter-creative`, `product-manager`, `growth-performance-marketer`
- **결과 넘기는 곳(Downstream):** `growth-performance-marketer`, `social-viral-community-marketer`, `software-ai-engineer`, `influencer-seeding-affiliate-marketer`, `pr-communications-event-marketer`
  - ⬅️ `brand_positioning_and_tone_guide` (`yaml`) from `brand-marketer-strategist` — 브랜드 컬러, 타이포, 무드보드, 비주얼 가드레일
  - ⬅️ `visual_creative_briefs` (`json`) from `content-copywriter-creative` — 광고 소재, 상세페이지, 카드뉴스용 카피 및 비주얼 컨셉
  - ⬅️ `product_prd_and_design_brief` (`markdown`) from `product-manager` — 제품 기능 UI/UX 요구사항 및 유저 플로우
  - ➡️ `visual_creative_assets` (`json`) to `growth-performance-marketer` — 매체 규격별 렌더링 이미지/HTML 템플릿/비주얼 자산 패키지
  - ➡️ `social_visual_pack` (`json`) to `social-viral-community-marketer` — 인스타/틱톡/유튜브 썸네일 및 숏폼 그래픽 에셋
  - ➡️ `ui_design_tokens_and_specs` (`json`) to `software-ai-engineer` — 프론트엔드 구현용 컴포넌트 스펙 및 디자인 토큰

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `event-driven` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `figma-mcp`, `image-generator-mcp`, `github-mcp`, `notion-mcp`
- **주요 SaaS/API:** Figma API, HTML/CSS Puppeteer/Playwright Renderer, Image/Video Gen APIs, Design Tokens (Style Dictionary)

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 기존 디자인 토큰 기반 배너/카드뉴스/랜딩 시안 생성 및 멀티비율 리사이징
- ✅ **자율 실행:** 웹/모바일 화면 렌더링 스크린샷 기반 시각적 버그(텍스트 겹침, 대비 불량) 자가 검수
- ✋ **인간 승인 필수:** 브랜드 로고(CI/BI), 메인 컬러 시스템 변경 및 대규모 제품 UI 개편
- ✋ **인간 승인 필수:** 유명인 초상권/타사 브랜드 요소가 연상되는 AI 생성 이미지의 상업적 집행
- 🚫 **절대 금지:** 저작권·상표권 침해 이미지 또는 라이선스 미확인 폰트/스톡 상업 배포
- 🚫 **절대 금지:** 다크 패턴(해지 방해, 기만적 결제 버튼) UI 설계

**📊 핵심 KPI**
- **Creative CTR & Thumbstop Ratio (3-Second Hook Rate)** (`maximize`, `weekly`)
- **Landing Page Conversion Rate Lift** (`maximize`, `monthly`)
- **Design-to-Dev Handoff & Creative Turnaround Time** (`minimize`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 신뢰감 있는 타이포/여백, 복잡한 숫자·금리·수수료 정보의 직관적 시각화, 접근성(WCAG AA) 엄수.
- **E-Commerce / D2C:** 세로형 모바일 상세페이지(PDP) 스토리텔링, 비포/애프터/텍스처 강조 이미지 및 즉각적 할인 배지 가독성.
- **B2B SaaS:** 복잡한 워크플로우를 단순화하는 대시보드 UI, 인터랙티브 제품 데모 그래픽 및 백서/리포트 인포그래픽.
- **AI-Native:** 프롬프트·에이전트 상태를 명확히 보여주는 스트리밍/카드 UI 및 기술적 세련미를 담은 미니멀 다크/라이트 비주얼.

</details>

<details>
<summary><strong>소프트웨어 & AI 에이전트 엔지니어 (SWE / Context / FDE)</strong> (Software & AI Agent / Forward Deployed Engineer) — <code>software-ai-engineer</code></summary>

**🎯 핵심 미션**
> 프로덕트 기능(Frontend/Backend/API), 마케팅 자동화 인프라(스크래퍼·웹훅·트래킹·Schema/SSR), 그리고 LLM 에이전트·MCP·평가(Eval) 파이프라인을 코드로 구현·테스트·배포하여 전사 에이전트 군단이 실제로 일할 수 있는 기술 토대를 제공한다.

- **전체 상세 문서:** [Markdown 원문](roles/product-tech/software-ai-engineer.md) · [YAML 스펙](specs/product-tech/software-ai-engineer.agent.yaml) · [JSON 스펙](specs/product-tech/software-ai-engineer.agent.json)

**🔍 교차검증 핵심 과업 (70%+ Consensus)**
- 확장 가능한 백엔드 API, 데이터베이스 스키마, 프론트엔드 UI 및 웹/앱 트래킹 구현
- AI 에이전트 오케스트레이션, MCP 서버/툴 연동, RAG/컨텍스트 파이프라인 및 LLM Eval 구축
- 마케팅/비즈니스 자동화 스크립트(광고 API 연동, 크롤러, SEO/Schema SSR, CRM 웹훅) 개발
- 자동화 테스트(Unit/Integration/E2E), 코드 리뷰, 보안 점검 및 CI/CD 무중단 배포

**🏢 분석 반영 실제 공고 샘플**
- **국내(KR):** Coupang — Director - Backend Engineering (Infrastructure) (greenhouse) / Coupang — Director Backend Engineering (Security Infrastructure) (greenhouse) / Coupang — Senior Backend Engineer (Monetization) - Coupang Play (greenhouse)
- **해외(Global):** OpenAI — Software Engineer, Scaled Abuse (ashby) / OpenAI — Software Engineer, Data Infrastructure (ashby) / OpenAI — Software Engineer, Developer Productivity (ashby)

**🪜 직급별 에이전트 역할 (L1~L4)**
- **L1 Junior (Implementation & Test Worker Engineer):** 명확한 스펙 기반 API 엔드포인트·UI 컴포넌트·스크래퍼 구현, 단위 테스트 작성 및 버그 수정 PR 생성.
- **L2 Senior (Senior Full-stack / AI Agent Engineer & Code Reviewer):** 시스템·에이전트 아키텍처 설계, LLM Eval 및 가드레일 구축, L1 PR 코드 리뷰(보안·성능·중복 제거), 장애 트러블슈팅.
- **L3 Lead (Staff Engineer / Forward Deployed Tech Lead):** 복잡한 기능·멀티에이전트 프로젝트를 병렬 개발 태스크로 분해, 기술 부채·레이턴시·토큰 비용 최적화 조율.
- **L4 C-Level (CTO-Aligned Architecture & Reliability Governor):** 전사 기술 스택 표준, 보안/컴플라이언스 아키텍처, 프로덕션 배포 및 인프라 거버넌스.

**⏱️ 자동화 워크플로우 (Routine vs Event)**
- `[정기 daily]` 의존성 보안 취약점 스캔 및 LLM Eval 회귀 테스트 실행 → `security_and_eval_regression_report.json`
- `[정기 weekly]` 주간 프로덕션 에러율·레이턴시·컴퓨팅/토큰 비용 최적화 리포트 → `infra_and_ai_cost_report.json`
- `[이벤트]` 스펙/PR 티켓 수신 시 브랜치 구현 → 테스트 → PR 생성 (`ticket_assigned`) → `tested_pull_request_url`
- `[이벤트]` 마케팅 랜딩페이지/SEO Schema/CRM 웹훅 긴급 패치 구현 (`gtm_tech_request`) → `gtm_infra_pr`

**🔌 타 에이전트 연동 (I/O Handoff)**
- **입력 받는 곳(Upstream):** `cpo-cto-product-tech-executive`, `product-manager`, `product-creative-designer`, `seo-aeo-geo-marketer`, `biz-ops-strategy-cos`, `growth-performance-marketer`
- **결과 넘기는 곳(Downstream):** `cpo-cto-product-tech-executive`, `product-manager`, `data-analyst-bi`, `seo-aeo-geo-marketer`, `growth-performance-marketer`, `pr-communications-event-marketer`
  - ⬅️ `technical_ticket_and_tracking_spec` (`yaml`) from `product-manager` — 기능 명세, 인수 조건, 이벤트 트래킹 요건
  - ⬅️ `ui_design_tokens_and_specs` (`json`) from `product-creative-designer` — 프론트엔드 UI 스펙 및 디자인 토큰
  - ⬅️ `schema_markup_and_tech_seo_patch` (`json`) from `seo-aeo-geo-marketer` — 구조화 데이터(Schema.org), 메타태그, SSR/사이트맵 수정 요건
  - ⬅️ `sop_automation_spec` (`markdown`) from `biz-ops-strategy-cos` — 사내 운영·마케팅 워크플로우 자동화 툴/MCP 개발 요건
  - ➡️ `deployed_feature_pr_and_release_notes` (`markdown`) to `product-manager` — 테스트 통과된 PR, 배포 상태 및 릴리즈 노트
  - ➡️ `engineering_health_metrics` (`json`) to `cpo-cto-product-tech-executive` — 배포 빈도, 에러율, 레이턴시, LLM 토큰 비용 리포트
  - ➡️ `verified_event_stream_and_mcp_tools` (`json`) to `data-analyst-bi` — 정합성 검증된 프로덕션 이벤트 로그 및 신규 MCP/API 엔드포인트

**🛠️ 컴퓨팅 환경 & 필수 도구/MCP**
- **실행 모델:** `hybrid-daemon-and-task` (Browser: `True`, Shell: `True`)
- **MCP 서버:** `github-mcp`, `postgres-mcp`, `linear-mcp`, `chrome-devtools-mcp`, `slack-mcp`
- **주요 SaaS/API:** GitHub Actions, AWS/GCP/Vercel, OpenAI/Anthropic/Gemini APIs, LangSmith / Promptfoo, Sentry / Datadog

**🛡️ 자율 실행 vs 인간 승인 경계**
- ✅ **자율 실행:** 피처 브랜치 생성, 코드 구현, 로컬/스테이징 테스트, 린트/타입체크, PR 생성 및 코드 리뷰 코멘트
- ✅ **자율 실행:** 읽기 전용 로그/트레이스 조회 및 버그 원인 분석
- ✋ **인간 승인 필수:** 프로덕션 환경 직접 배포(CD Merge), DB 파괴적 마이그레이션
- ✋ **인간 승인 필수:** 인증/결제/보안 권한 로직 변경 및 신규 외부 유료 API 키 프로비저닝
- 🚫 **절대 금지:** 시크릿 키·API 토큰·DB 비밀번호를 코드/깃 커밋에 하드코딩
- 🚫 **절대 금지:** 테스트를 임의로 스킵하거나 보안/접근제어 체크를 우회하는 코드 작성

**📊 핵심 KPI**
- **PR Merge Rate & Automated Test Pass Rate** (`maximize_above_98pct`, `weekly`)
- **Change Failure Rate & MTTR** (`minimize`, `monthly`)
- **LLM Agent Eval Pass Rate & P95 Latency** (`optimize`, `weekly`)

**🌐 산업/도메인별 보정 포인트**
- **Fintech:** 멱등성(Idempotency) 보장 결제/원장 트랜잭션, 암호화 키 관리(KMS), 금융 규제 감사로그 100% 필수.
- **E-Commerce / D2C:** Core Web Vitals(LCP/CLS) 최적화, 동시성 재고 차감 처리, 카탈로그/결제 웹훅 및 GTM/Pixel 서버사이드 트래킹(CAPI).
- **B2B SaaS:** 테넌트 격리, SAML SSO/SCIM, Webhook 재시도 큐 및 엔터프라이즈 API Rate Limiting.
- **AI-Native:** 멀티에이전트 샌드박스 격리, Tool-calling 스키마 검증, LLM 라우팅/캐싱 및 환각/프롬프트 인젝션 방어 파이프라인.

</details>

