#!/usr/bin/env python3
"""
Generate 6 Obsidian Excalidraw visualizations (.png + .excalidraw)
optimized for mobile vertical reading (1080px wide, crisp 2x supersampling).
"""

import json
import math
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "assets" / "excalidraw"

FONT_BOLD_PATH = "/Users/zero/projects/instargram Carousel/fonts/Pretendard-Bold.otf"
FONT_REG_PATH = "/Users/zero/projects/instargram Carousel/fonts/Pretendard-Regular.otf"
if not Path(FONT_BOLD_PATH).exists():
    FONT_BOLD_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    FONT_REG_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

BG_COLOR = "#FCFBF7"
DOT_COLOR = "#E2DDD1"
INK = "#1E1E1E"
MUTED = "#55524D"
SHADOW = "#E8E3D5"

PALETTE = {
    "yellow": ("#FFF3BF", "#F08C00"),
    "blue": ("#D0EBFF", "#1971C2"),
    "green": ("#D3F9D8", "#2B8A3E"),
    "orange": ("#FFE8CC", "#D9480F"),
    "purple": ("#E5DBFF", "#6741D9"),
    "red": ("#FFE3E3", "#C92A2A"),
    "gray": ("#F1F3F5", "#495057"),
    "white": ("#FFFFFF", "#1E1E1E"),
}

SCALE = 2  # Render 2x and downsample for ultra-crisp anti-aliased strokes & Korean text


class ExcalidrawCanvas:
    """Dual renderer outputting both high-res Excalidraw-styled PNG and valid .excalidraw JSON."""

    def __init__(self, name: str, title: str, subtitle: str, width: int = 1080, height: int = 1350, seed: int = 42):
        self.name = name
        self.width = width
        self.height = height
        self.rng = random.Random(seed)
        self.img = Image.new("RGB", (width * SCALE, height * SCALE), BG_COLOR)
        self.draw = ImageDraw.Draw(self.img, "RGBA")
        self.elements: List[Dict[str, Any]] = []
        self._id_counter = 1

        self.f_h1 = ImageFont.truetype(FONT_BOLD_PATH, 34 * SCALE)
        self.f_sub = ImageFont.truetype(FONT_REG_PATH, 19 * SCALE)
        self.f_title = ImageFont.truetype(FONT_BOLD_PATH, 22 * SCALE)
        self.f_body = ImageFont.truetype(FONT_REG_PATH, 17 * SCALE)
        self.f_badge = ImageFont.truetype(FONT_BOLD_PATH, 15 * SCALE)
        self.f_small = ImageFont.truetype(FONT_REG_PATH, 15 * SCALE)

        self._draw_dot_grid()
        self._draw_header(title, subtitle)

    def _next_id(self, prefix: str = "el") -> str:
        eid = f"{self.name}_{prefix}_{self._id_counter}"
        self._id_counter += 1
        return eid

    def _draw_dot_grid(self) -> None:
        step = 28 * SCALE
        r = 1.5 * SCALE
        for x in range(step, self.width * SCALE, step):
            for y in range(step, self.height * SCALE, step):
                self.draw.ellipse([x - r, y - r, x + r, y + r], fill=DOT_COLOR)

    def _draw_header(self, title: str, subtitle: str) -> None:
        # Subtle header band
        self.pill(48, 36, "OBSIDIAN EXCALIDRAW VISUAL", color="purple")
        self.text_line(48, 82, title, font=self.f_h1, color=INK)
        self.text_line(48, 128, subtitle, font=self.f_sub, color=MUTED)
        self.sketch_line(48, 166, self.width - 48, 166, color="#D8D2C5", width=2)
        self._add_excalidraw_text(48, 82, 960, 40, title, 28)
        self._add_excalidraw_text(48, 128, 960, 26, subtitle, 16)

    def _add_excalidraw_rect(
        self, x: float, y: float, w: float, h: float, bg: str, stroke: str, roundness: bool = True
    ) -> str:
        eid = self._next_id("rect")
        self.elements.append({
            "id": eid,
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "angle": 0,
            "strokeColor": stroke,
            "backgroundColor": bg,
            "fillStyle": "hachure" if bg != "#FFFFFF" else "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "roundness": {"type": 3} if roundness else None,
            "seed": self.rng.randint(1, 10**6),
            "version": 1,
            "versionNonce": self.rng.randint(1, 10**6),
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
        })
        return eid

    def _add_excalidraw_text(
        self, x: float, y: float, w: float, h: float, txt: str, font_size: int = 18, color: str = INK, align: str = "left"
    ) -> str:
        eid = self._next_id("txt")
        self.elements.append({
            "id": eid,
            "type": "text",
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "angle": 0,
            "strokeColor": color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "roundness": None,
            "seed": self.rng.randint(1, 10**6),
            "version": 1,
            "versionNonce": self.rng.randint(1, 10**6),
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
            "text": txt,
            "fontSize": font_size,
            "fontFamily": 1,
            "textAlign": align,
            "verticalAlign": "top",
            "baseline": font_size,
            "containerId": None,
            "originalText": txt,
            "lineHeight": 1.25,
        })
        return eid

    def _add_excalidraw_arrow(self, x1: float, y1: float, x2: float, y2: float, color: str = INK) -> str:
        eid = self._next_id("arr")
        self.elements.append({
            "id": eid,
            "type": "arrow",
            "x": x1,
            "y": y1,
            "width": abs(x2 - x1),
            "height": abs(y2 - y1),
            "angle": 0,
            "strokeColor": color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "roundness": {"type": 2},
            "seed": self.rng.randint(1, 10**6),
            "version": 1,
            "versionNonce": self.rng.randint(1, 10**6),
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
            "points": [[0, 0], [x2 - x1, y2 - y1]],
            "lastCommittedPoint": None,
            "startBinding": None,
            "endBinding": None,
            "startArrowhead": None,
            "endArrowhead": "arrow",
        })
        return eid

    def text_line(self, x: float, y: float, txt: str, font: ImageFont.FreeTypeFont, color: str = INK) -> None:
        self.draw.text((x * SCALE, y * SCALE), txt, font=font, fill=color)

    def _wrap_text(self, txt: str, font: ImageFont.FreeTypeFont, max_w_px: float) -> List[str]:
        out: List[str] = []
        for para in txt.split("\n"):
            if not para:
                out.append("")
                continue
            cur = ""
            for ch in para:
                test = cur + ch
                bbox = self.draw.textbbox((0, 0), test, font=font)
                if (bbox[2] - bbox[0]) <= max_w_px:
                    cur = test
                else:
                    if cur:
                        out.append(cur)
                    cur = ch
            if cur:
                out.append(cur)
        return out

    def pill(self, x: float, y: float, label: str, color: str = "blue") -> float:
        fill_c, stroke_c = PALETTE[color]
        bbox = self.draw.textbbox((0, 0), label, font=self.f_badge)
        tw = (bbox[2] - bbox[0]) / SCALE
        pw = tw + 26
        ph = 30
        sx, sy, sw, sh = x * SCALE, y * SCALE, pw * SCALE, ph * SCALE
        self.draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=15 * SCALE, fill=fill_c, outline=stroke_c, width=2 * SCALE)
        self.draw.text(((x + 13) * SCALE, (y + 6) * SCALE), label, font=self.f_badge, fill=stroke_c)
        self._add_excalidraw_rect(x, y, pw, ph, fill_c, stroke_c)
        self._add_excalidraw_text(x + 12, y + 6, pw - 20, ph - 10, label, 13, stroke_c)
        return pw

    def sketch_line(self, x1: float, y1: float, x2: float, y2: float, color: str = INK, width: float = 2.5) -> None:
        dist = math.hypot(x2 - x1, y2 - y1)
        steps = max(8, int(dist / 22))
        for pass_idx in range(2):
            pts = []
            for s in range(steps + 1):
                t = s / steps
                px = x1 + (x2 - x1) * t
                py = y1 + (y2 - y1) * t
                if 0 < s < steps:
                    wobble = 1.4 if pass_idx == 0 else 1.8
                    px += self.rng.uniform(-wobble, wobble)
                    py += self.rng.uniform(-wobble, wobble)
                pts.append((px * SCALE, py * SCALE))
            w = int((width if pass_idx == 0 else width * 0.65) * SCALE)
            c = color if pass_idx == 0 else color + "AA" if len(color) == 7 else color
            self.draw.line(pts, fill=color, width=max(1, w), joint="curve")

    def sketch_rect(
        self, x: float, y: float, w: float, h: float, fill_c: str, stroke_c: str, radius: float = 16
    ) -> None:
        sx, sy, sw, sh = x * SCALE, y * SCALE, w * SCALE, h * SCALE
        r = radius * SCALE
        # Soft Excalidraw shadow
        off = 5 * SCALE
        self.draw.rounded_rectangle([sx + off, sy + off, sx + sw + off, sy + sh + off], radius=r, fill=SHADOW)
        # Main fill
        self.draw.rounded_rectangle([sx, sy, sx + sw, sy + sh], radius=r, fill=fill_c, outline=stroke_c, width=int(2.4 * SCALE))
        # Subtle sketchy second border pass
        d = 1.6 * SCALE
        self.draw.rounded_rectangle(
            [sx - d, sy + d * 0.5, sx + sw + d * 0.5, sy + sh - d * 0.5],
            radius=r,
            outline=stroke_c,
            width=int(1.2 * SCALE),
        )
        self._add_excalidraw_rect(x, y, w, h, fill_c, stroke_c)

    def box(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        title: str,
        body: str,
        color: str = "blue",
        badge: Optional[str] = None,
        center: bool = False,
    ) -> None:
        fill_c, stroke_c = PALETTE[color]
        self.sketch_rect(x, y, w, h, fill_c, INK)

        # Left accent bar inside box
        ax = (x + 12) * SCALE
        self.draw.rounded_rectangle(
            [ax, (y + 16) * SCALE, ax + 5 * SCALE, (y + h - 16) * SCALE],
            radius=3 * SCALE,
            fill=stroke_c,
        )

        cur_y = y + 18
        tx = x + 28
        max_w = (w - 46) * SCALE

        if badge:
            self.draw.text((tx * SCALE, cur_y * SCALE), badge, font=self.f_badge, fill=stroke_c)
            cur_y += 24

        for ln in self._wrap_text(title, self.f_title, max_w):
            if center:
                bb = self.draw.textbbox((0, 0), ln, font=self.f_title)
                lw = (bb[2] - bb[0]) / SCALE
                self.draw.text(((x + (w - lw) / 2) * SCALE, cur_y * SCALE), ln, font=self.f_title, fill=INK)
            else:
                self.draw.text((tx * SCALE, cur_y * SCALE), ln, font=self.f_title, fill=INK)
            cur_y += 30

        cur_y += 4
        for ln in self._wrap_text(body, self.f_body, max_w):
            if center:
                bb = self.draw.textbbox((0, 0), ln, font=self.f_body)
                lw = (bb[2] - bb[0]) / SCALE
                self.draw.text(((x + (w - lw) / 2) * SCALE, cur_y * SCALE), ln, font=self.f_body, fill=MUTED)
            else:
                self.draw.text((tx * SCALE, cur_y * SCALE), ln, font=self.f_body, fill=MUTED)
            cur_y += 24

        self._add_excalidraw_text(tx, y + 16, w - 40, h - 24, f"{title}\n{body}", 16, INK)

    def arrow(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        label: Optional[str] = None,
        color: str = INK,
    ) -> None:
        self.sketch_line(x1, y1, x2, y2, color=color, width=2.8)
        ang = math.atan2(y2 - y1, x2 - x1)
        head_len = 14
        for delta in (2.6, -2.6):
            hx = x2 + head_len * math.cos(ang + delta)
            hy = y2 + head_len * math.sin(ang + delta)
            self.sketch_line(x2, y2, hx, hy, color=color, width=2.8)
        self._add_excalidraw_arrow(x1, y1, x2, y2, color)

        if label:
            mx = x1 + (x2 - x1) * 0.44
            my = y1 + (y2 - y1) * 0.42
            bb = self.draw.textbbox((0, 0), label, font=self.f_small)
            lw = (bb[2] - bb[0]) / SCALE
            lh = (bb[3] - bb[1]) / SCALE
            px = mx - lw / 2 - 10
            py = my - lh / 2 - 5
            self.draw.rounded_rectangle(
                [px * SCALE, py * SCALE, (px + lw + 20) * SCALE, (py + lh + 10) * SCALE],
                radius=10 * SCALE,
                fill="#FFFFFF",
                outline=color,
                width=int(1.6 * SCALE),
            )
            self.draw.text(((px + 10) * SCALE, (py + 4) * SCALE), label, font=self.f_small, fill=color)
            self._add_excalidraw_text(px + 8, py + 4, lw + 10, lh + 6, label, 13, color)

    def footer(self, note: str) -> None:
        y = self.height - 46
        self.sketch_line(48, y - 12, self.width - 48, y - 12, color="#D8D2C5", width=1.8)
        self.text_line(48, y, note, font=self.f_small, color=MUTED)

    def save(self) -> None:
        png_path = OUT_DIR / f"{self.name}.png"
        exc_path = OUT_DIR / f"{self.name}.excalidraw"
        resized = self.img.resize((self.width, self.height), Image.Resampling.LANCZOS)
        resized.save(png_path, format="PNG", optimize=True)

        exc_doc = {
            "type": "excalidraw",
            "version": 2,
            "source": "https://github.com/workzeroai/agent-job-descriptions",
            "elements": self.elements,
            "appState": {
                "viewBackgroundColor": BG_COLOR,
                "gridSize": 20,
            },
            "files": {},
        }
        exc_path.write_text(json.dumps(exc_doc, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Generated {png_path.name} ({self.width}x{self.height}) + {exc_path.name}")


def build_01_big_picture_stack() -> None:
    c = ExcalidrawCanvas(
        "01-big-picture-stack",
        "AI 에이전트 회사 5단계 아키텍처 (Big Picture)",
        "단순 챗봇을 넘어 '컴퓨터 자원 + 직무기술서 + 팀 오케스트레이션'이 결합되는 구조",
        width=1080,
        height=1340,
        seed=101,
    )
    layers = [
        ("STEP 1 · BRAIN (두뇌)", "초거대 언어모델 (LLM)", "ChatGPT, Claude, Gemini, Grok — 추론·계획·문서 작성의 기본 지능", "gray"),
        ("STEP 2 · HANDS & WORKSPACE (손과 발)", "클라우드 컴퓨팅 + MCP 도구", "리눅스 샌드박스, 브라우저, 터미널, Slack / GA4 / Meta Ads API 연결", "blue"),
        ("STEP 3 · JOB SPEC (바로 이 레포지토리!)", "표준 직무기술서 + 직급(L1~L4) + 가드레일", "실제 공고 2,132건 교차검증 · 역할 정의 · 입출력 계약(I/O) · 인간 승인 경계", "yellow"),
        ("STEP 4 · SWARM ORCHESTRATION (팀 협업)", "멀티 에이전트 조직 운영", "리서처 -> 브랜드 -> 카피 -> 디자인 -> L2 검수(Critic) -> 인간 최종 승인", "green"),
        ("STEP 5 · SELF-IMPROVING LOOP (자가 진화)", "암묵지 축적 & 자동 학습", "성공 사례 역공학 · Reflexion 오답노트 · Voyager 스킬 라이브러리 축적", "purple"),
    ]
    y = 200
    for idx, (badge, title, body, color) in enumerate(layers):
        c.box(72, y, 936, 152, title, body, color=color, badge=badge)
        if idx < len(layers) - 1:
            c.arrow(540, y + 152, 540, y + 206, label="다음 레이어 결합" if idx != 1 else "직무 규격 주입", color="#2B2B2B")
        y += 206

    c.footer("github.com/workzeroai/agent-job-descriptions · Excalidraw Source: 01-big-picture-stack.excalidraw")
    c.save()


def build_02_chatbot_vs_agent_vs_team() -> None:
    c = ExcalidrawCanvas(
        "02-chatbot-vs-agent-vs-team",
        "왜 혼자 일하게 두면 실패할까? (챗봇 vs 단일 봇 vs 팀)",
        "CMU TheAgentCompany & Anthropic 실전 에이전트 패턴 핵심 비교",
        width=1080,
        height=1380,
        seed=202,
    )
    # Zone 1: Chatbot
    c.box(
        64,
        196,
        952,
        185,
        "1. 일반 챗봇 (Chatbot) — '말만 하는 자문위원'",
        "• 질문하면 답변만 생성 (파일 수정·웹 로그인·광고 세팅 불가)\n• 사람이 직접 복사-붙여넣기해서 실행해야 끝남",
        color="gray",
        badge="구형 방식 · 수동 실행",
    )
    c.arrow(540, 381, 540, 425, label="컴퓨터 자원(PC/브라우저) 지급", color="#1971C2")

    # Zone 2: Single Agent
    c.box(
        64,
        425,
        952,
        240,
        "2. 단일 에이전트 (Single Agent) — '1인 다역 독박 직원'",
        "• 문제: 리서치 + 기획 + 카피 + 디자인 + 검수를 혼자 50단계 처리\n• 한계 1 (문맥 표류): 중반쯤 가면 초반 브랜드 지침을 까먹음\n• 한계 2 (자기 합리화): 자기가 만든 결과물을 무조건 '완료'로 통과시킴\n• CMU 가상회사 실험 기준 장기 업무 완수율: 약 24~30%",
        color="red",
        badge="단일 봇의 한계 · 성공률 ~30%",
    )
    c.arrow(540, 665, 540, 715, label="직무 분리 + I/O 규격 + Critic 도입", color="#2B8A3E")

    # Zone 3: Agent Team (Recommended)
    c.sketch_rect(64, 715, 952, 570, "#F3FBF4", "#2B8A3E")
    c.pill(90, 738, "3. 분업화된 에이전트 조직 (Agent Team) — 권장 아키텍처", color="green")

    c.box(96, 788, 410, 145, "L1 실행 워커 (Workers)", "짧은 단일 과업만 정확히 실행\n(리서치 · 카피 · 시딩 · SQL)", color="blue", badge="10단계 이하 짧은 호흡")
    c.box(574, 788, 410, 145, "L2 전문가 & Critic", "브랜드 톤 · 팩트 · ROAS 냉정 감사\n불합격 시 반려 및 수정 지시", color="orange", badge="독립 검수 게이트")
    c.arrow(506, 860, 574, 860, label="산출물", color="#1E1E1E")
    c.arrow(574, 905, 506, 905, label="반려", color="#C92A2A")

    c.box(96, 975, 410, 145, "L3 팀장 오케스트레이터", "목표를 쪼개 L1들에게 배분\nio_contract(JSON/MD) 연결", color="purple", badge="흐름 & 병목 조율")
    c.box(574, 975, 410, 145, "인간 최종 승인 (HITL)", "예산 결제 · 대량 발송 · 보도자료\n핵심 버튼만 스마트폰으로 승인", color="yellow", badge="리스크 0% 통제")

    c.arrow(779, 933, 779, 975, label="검수 통과", color="#2B8A3E")
    c.arrow(301, 975, 301, 933, label="작업 할당", color="#6741D9")

    c.box(96, 1148, 888, 112, "핵심 결과: 95% 밤새 자율 준비 + 5% 인간 승인", "컨텍스트가 섞이지 않고 상호 검증이 돌아가므로 실무 투입 가능한 품질 달성", color="white")

    c.footer("github.com/workzeroai/agent-job-descriptions · Excalidraw Source: 02-chatbot-vs-agent-vs-team.excalidraw")
    c.save()


def build_03_tacit_knowledge_loop() -> None:
    c = ExcalidrawCanvas(
        "03-tacit-knowledge-loop",
        "실무 고수가 아니어도 봇이 암묵지를 배우는 4대 루프",
        "프롬프트를 100줄 쓰는 대신, 시장 데이터·오답노트·스킬 저장소로 스스로 성장하는 구조",
        width=1080,
        height=1360,
        seed=303,
    )
    c.box(
        72,
        196,
        936,
        170,
        "1. 시장 최고 사례 역공학 (Reverse Engineering)",
        "내가 상세페이지나 광고 고수가 아니어도 OK!\n봇에게 '경쟁사 30일 이상 집행된 히트 광고 50개'를 긁어와 훅·논리·CTA 규칙 추출 지시",
        color="yellow",
        badge="STEP 1 · 암묵지 추출",
    )
    c.arrow(540, 366, 540, 420, label="추출된 체크리스트 적용", color="#1E1E1E")

    c.box(
        72,
        420,
        936,
        160,
        "2. 실무 태스크 실행 (Execution)",
        "광고 카피 15종, 인플루언서 시딩 메일, SEO 아티클 등 실제 산출물 제작 및 테스트",
        color="blue",
        badge="STEP 2 · 실전 투입",
    )
    c.arrow(540, 580, 540, 634, label="결과 제출", color="#1E1E1E")

    c.box(
        72,
        634,
        936,
        160,
        "3. L2 Critic & 실제 KPI 평가",
        "내부 검수 봇(Critic)의 브랜드 톤 심사 + 실제 시장 지표(CTR, 오픈율, ROAS, 에러율) 측정",
        color="orange",
        badge="STEP 3 · 냉정한 채점",
    )

    c.arrow(320, 794, 280, 868, label="실패 / 저성과 시", color="#C92A2A")
    c.arrow(760, 794, 800, 868, label="성공 / 고성과 시", color="#2B8A3E")

    c.box(
        64,
        868,
        446,
        240,
        "4A. Reflexion 오답노트",
        "• '왜 실패했는가'를 반성문으로 작성\n• lessons_learned.md 에 저장\n• 다음 작업 시작 전 자동 열람하여\n  같은 실수를 절대 반복하지 않음",
        color="red",
        badge="모델 재학습 없이 즉시 교정",
    )
    c.box(
        570,
        868,
        446,
        240,
        "4B. Voyager 스킬 라이브러리",
        "• 성공한 크롤러·카피·리포트 코드를\n  skills/ 폴더에 도구로 영구 저장\n• 다음 프로젝트에서 조립해 재사용\n• DSPy/TextGrad로 프롬프트 자동 진화",
        color="green",
        badge="봇의 무기 창고 축적",
    )

    c.arrow(287, 1108, 430, 1170, label="규칙 보강", color="#C92A2A")
    c.arrow(793, 1108, 650, 1170, label="도구 재사용", color="#2B8A3E")

    c.box(
        72,
        1170,
        936,
        115,
        "결과: 일할수록 노련한 시니어 직원처럼 진화하는 에이전트 조직",
        "설계자는 '평가 기준(KPI) + 오답노트 폴더 + 스킬 폴더' 구조만 잡아주면 됩니다.",
        color="purple",
    )

    c.footer("github.com/workzeroai/agent-job-descriptions · Excalidraw Source: 03-tacit-knowledge-loop.excalidraw")
    c.save()


def build_04_full_marketing_pipeline() -> None:
    c = ExcalidrawCanvas(
        "04-full-marketing-pipeline",
        "100% 자율 마케팅 & 전사 18대 직무 7단계 파이프라인",
        "workflows/full-marketing-engine.yaml 기반 에이전트 간 입출력(io_contract) 연동도",
        width=1080,
        height=1660,
        seed=404,
    )
    c.box(72, 192, 936, 132, "STAGE 1 · 목표 및 예산 총괄 (C-Level)", "CMO (마케팅 총괄) + CRO (매출 총괄) + BizOps (전략기획) -> 분기 OKR & 채널 예산 배분", color="purple", badge="L4 GOVERNANCE")
    c.arrow(540, 324, 540, 382, label="marketing_okr_and_budget.yaml")

    c.box(72, 382, 936, 132, "STAGE 2 · 시장 · 트렌드 · 소비자 인텔리전스", "시장·소비자 리서처 + 데이터 애널리스트 -> icp_personas.json & 주간 밈/경쟁사 레이더", color="blue", badge="INTELLIGENCE")
    c.arrow(540, 514, 540, 572, label="icp_personas.json + battlecards.md")

    c.box(72, 572, 936, 132, "STAGE 3 · 브랜드 포지셔닝 & 통합 캠페인 브리프", "브랜드 마케터 & 전략가 -> 톤앤매너 가드레일(YAML) & 통합 캠페인(IMC) 브리프 발행", color="yellow", badge="STRATEGY & GUARDRAIL")
    c.arrow(540, 704, 540, 762, label="integrated_campaign_brief.md")

    c.box(72, 762, 936, 132, "STAGE 4 · 카피 & 크리에이티브 팩토리", "콘텐츠·카피라이터 + UI/UX·BX 디자이너 -> 광고 카피 · 상세페이지 · 숏폼 대본 · 비주얼 에셋", color="orange", badge="CREATIVE PRODUCTION")
    c.arrow(540, 894, 540, 954, label="5대 채널 병렬 배포 (Fan-out)")

    # Stage 5: 5 parallel marketing channels (2 rows with generous padding)
    c.sketch_rect(64, 954, 952, 320, "#F8F9FA", "#495057")
    c.pill(86, 972, "STAGE 5 · 5개 마케팅 실행 에이전트 병렬 가동", color="gray")
    c.box(86, 1016, 290, 114, "퍼포먼스·그로스", "Meta·Google·TikTok\nNaver 유료 광고 & CRO", color="blue")
    c.box(395, 1016, 290, 114, "인플루언서 시딩", "KOL 발굴 · 아웃리치\nUTM 정산 · 2차 광고", color="green")
    c.box(704, 1016, 290, 114, "소셜·바이럴·숏폼", "릴스·틱톡·쇼츠·X\n커뮤니티 실시간 확산", color="yellow")
    c.box(160, 1144, 360, 110, "SEO & AEO/GEO", "구글/네이버 SEO + ChatGPT\nPerplexity AI 인용 최적화", color="purple")
    c.box(560, 1144, 360, 110, "PR·언론 & 이벤트", "보도자료 · 미디어 피칭\n웨비나 · 위기대응", color="orange")

    c.arrow(540, 1274, 540, 1334, label="유입 트래픽 & 리드 인계")

    c.box(72, 1334, 450, 122, "STAGE 6A · CRM 리텐션", "알림톡·푸시·이메일 온보딩 & 이탈 방어", color="green")
    c.box(558, 1334, 450, 122, "STAGE 6B · B2B 세일즈", "SDR 리드 인리치먼트 · 아웃바운드 · AE 계약", color="blue")

    c.arrow(297, 1456, 410, 1498)
    c.arrow(783, 1456, 670, 1498)

    c.box(72, 1498, 936, 102, "STAGE 7 · 데이터 애널리스트(BI) 통합 어트리뷰션 -> CMO 주간 예산 재조정", "전체 18개 직무가 동일한 JSON/YAML 계약으로 연결되어 닫힌 피드백 루프(Closed Loop) 완성", color="purple")

    c.footer("github.com/workzeroai/agent-job-descriptions · Excalidraw Source: 04-full-marketing-pipeline.excalidraw")
    c.save()


def build_05_seniority_hierarchy() -> None:
    c = ExcalidrawCanvas(
        "05-seniority-l1-to-l4-hierarchy",
        "직급(L1~L4) = 에이전트 계층 및 권한 거버넌스",
        "seniority-levels/*.yaml · 인간의 연차 체계를 에이전트의 자율성과 검수 구조로 1:1 매핑",
        width=1080,
        height=1340,
        seed=505,
    )
    tiers = [
        ("HUMAN HITL", "인간 대표 / 총괄 승인 게이트 (Human-in-the-Loop)", "최종 결제 · 법적 계약 서명 · 대외 PR 성명 · 대형 예산 15%+ 이동 승인", "red", "최종 통제권"),
        ("L4 C-LEVEL", "Executive Governor (CMO · CRO · CPO/CTO)", "전사 OKR 설정 · 부서 간 예산/컴퓨팅 배분 · 리스크 및 컴플라이언스 정책 총괄", "purple", "전사 목표·예산"),
        ("L3 LEAD / HEAD", "Squad Orchestrator (팀장 에이전트)", "상위 목표를 하위 워커 태스크로 분해 · I/O 계약 준수 관리 · 병목 해결", "orange", "작업 분해·조율"),
        ("L2 SENIOR", "Autonomous Specialist & Critic (전문가 & 검수자)", "실험 설계 · 트러블슈팅 · L1 산출물 냉정 감사(QA/브랜드/통계 유의성 판정)", "yellow", "전략·품질 검수"),
        ("L1 JUNIOR", "Execution Worker (실행 전담 워커)", "명확한 SOP 안에서 데이터 수집 · 초안 대량 생산 · UTM/SQL 추출 (단독 배포 불가)", "blue", "고속 반복 실행"),
    ]
    y = 198
    for idx, (badge, title, body, color, edge_lbl) in enumerate(tiers):
        c.box(72, y, 936, 152, title, body, color=color, badge=badge)
        if idx < len(tiers) - 1:
            # Upward reporting + downward delegation
            c.arrow(360, y + 152, 360, y + 206, label="목표·예산 하달", color="#495057")
            c.arrow(720, y + 206, 720, y + 152, label=f"보고·승인 요청 ({edge_lbl})", color="#1971C2")
        y += 206

    c.footer("github.com/workzeroai/agent-job-descriptions · Excalidraw Source: 05-seniority-l1-to-l4-hierarchy.excalidraw")
    c.save()


def build_06_agent_composition_and_squad() -> None:
    c = ExcalidrawCanvas(
        "06-agent-composition-and-squad",
        "에이전트 조립 공식 & 첫 '3인 마케팅 미니 스쿼드' 가이드",
        "4개 모듈 조합으로 어떤 회사에도 맞춤형 봇 생성 + 처음 시작할 때 가장 추천하는 3인 조합",
        width=1080,
        height=1400,
        seed=606,
    )
    # Top half: Modular Composition Formula
    c.sketch_rect(64, 192, 952, 508, "#F8F9FA", "#1E1E1E")
    c.pill(88, 212, "PART 1 · 모듈 조립 공식 (Role + Seniority + Domain + Stage/Locale)", color="purple")

    c.box(88, 262, 430, 145, "1. 기본 직무 스펙 (Role)", "specs/marketing/...agent.yaml\n미션 · 도구/MCP · I/O · 가드레일", color="blue")
    c.box(562, 262, 430, 145, "2. 직급 모듈 (Seniority)", "seniority-levels/l1~l4.yaml\n실행 워커 vs 검수 Critic vs 총괄", color="yellow")
    c.box(88, 434, 430, 145, "3. 산업 도메인 (Domain)", "overlays/domains/*.yaml\n핀테크 · 커머스D2C · B2B SaaS · AI", color="green")
    c.box(562, 434, 430, 145, "4. 규모 & 지역 (Stage/Locale)", "early-startup-0to1 + kr-market\n알림톡 · 네이버 · 표시광고법 보정", color="orange")

    c.box(88, 592, 904, 88, "4개 모듈 파일을 결합해 에이전트 System Prompt & Tool Config로 즉시 주입!", "도메인(Domain)과 기업 단계(Stage)가 바뀌어도 모듈만 갈아끼우면 즉시 적응합니다.", color="white")

    c.arrow(540, 700, 540, 756, label="초보자 실전 시작 추천 (3인 스쿼드)", color="#2B8A3E")

    # Bottom half: First 3-Agent Mini Squad
    c.sketch_rect(64, 756, 952, 556, "#FFFDF5", "#F08C00")
    c.pill(88, 774, "PART 2 · 18개 다 쓰지 말고 '이 3명'부터 바로 돌려보세요", color="orange")

    c.box(
        92,
        822,
        896,
        125,
        "1번 봇 · 시장·소비자 리서처 (L1 Worker)",
        "경쟁사 3곳의 랜딩페이지 + 리뷰 50개 분석 -> icp_personas.json 출력",
        color="blue",
        badge="INPUT: 우리 제품 설명 1장",
    )
    c.arrow(540, 947, 540, 998, label="icp_personas.json 전달")

    c.box(
        92,
        998,
        896,
        125,
        "2번 봇 · 콘텐츠·카피라이터 (L1 Worker)",
        "리서처가 뽑은 고객 언어로 광고 카피 10종 + 숏폼 훅 -> ad_copy_matrix.json 출력",
        color="green",
    )
    c.arrow(540, 1123, 540, 1174, label="ad_copy_matrix.json 검수 요청")

    c.box(
        92,
        1174,
        896,
        125,
        "3번 봇 · 브랜드 전략가 (L2 Critic 검수자)",
        "과장 광고 · 어색한 AI 말투 탈락시키고 Top 3 카피만 합격 처리 -> 대표(나)에게 보고",
        color="yellow",
        badge="OUTPUT: 바로 집행 가능한 Top 3 카피",
    )

    c.footer("github.com/workzeroai/agent-job-descriptions · Excalidraw Source: 06-agent-composition-and-squad.excalidraw")
    c.save()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Generating 6 Excalidraw PNG + .excalidraw diagrams...")
    build_01_big_picture_stack()
    build_02_chatbot_vs_agent_vs_team()
    build_03_tacit_knowledge_loop()
    build_04_full_marketing_pipeline()
    build_05_seniority_hierarchy()
    build_06_agent_composition_and_squad()
    print("Done! All assets written to:", OUT_DIR)


if __name__ == "__main__":
    main()
