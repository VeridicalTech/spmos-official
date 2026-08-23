#!/usr/bin/env python3
"""Build the publication-ready English SPM-Polaris technical report PDF."""

from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from report_pdf_markdown import parse_body


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "publications" / "2026-08-23" / "technical-report-en.md"
OUTPUT = ROOT / "output" / "pdf" / "SPM-Polaris-Technical-Report-v1.0-2026-08-23.pdf"
LOGO_URL = "https://docs.spmos.ai/assets/orbit-light-transparent.png"
LOGO_SHA256 = "ff2dfef04166995bdf47013f7259a0158d0ae434aeaa97ef26918eff9db8227e"
LOGO_CACHE = ROOT / "output" / "assets" / "orbit-light-transparent.png"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 18 * mm
MARGIN_TOP = 19 * mm
MARGIN_BOTTOM = 18 * mm
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN_X

INK = HexColor("#0B0B0C")
MUTED = HexColor("#5D6069")
LINE = HexColor("#D9DBE1")
SOFT = HexColor("#F5F6F8")
BLUE = HexColor("#2F63F5")


def register_fonts() -> tuple[str, str, str, str]:
    candidates = [
        (
            Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Italic.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"),
        ),
    ]
    for regular, bold, italic, bold_italic in candidates:
        if all(path.exists() for path in (regular, bold, italic, bold_italic)):
            pdfmetrics.registerFont(TTFont("SPM-Regular", regular))
            pdfmetrics.registerFont(TTFont("SPM-Bold", bold))
            pdfmetrics.registerFont(TTFont("SPM-Italic", italic))
            pdfmetrics.registerFont(TTFont("SPM-BoldItalic", bold_italic))
            pdfmetrics.registerFontFamily(
                "SPM-Regular",
                normal="SPM-Regular",
                bold="SPM-Bold",
                italic="SPM-Italic",
                boldItalic="SPM-BoldItalic",
            )
            return "SPM-Regular", "SPM-Bold", "SPM-Italic", "SPM-BoldItalic"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique"


REGULAR, BOLD, ITALIC, BOLD_ITALIC = register_fonts()


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle(
            "CoverKicker",
            parent=base["Normal"],
            fontName=BOLD,
            fontSize=8,
            leading=10,
            textColor=MUTED,
            tracking=1.6,
            spaceAfter=10,
        ),
        "cover_title": ParagraphStyle(
            "CoverTitle",
            parent=base["Title"],
            fontName=BOLD,
            fontSize=28,
            leading=32,
            alignment=TA_LEFT,
            textColor=INK,
            spaceAfter=12,
        ),
        "cover_deck": ParagraphStyle(
            "CoverDeck",
            parent=base["Normal"],
            fontName=REGULAR,
            fontSize=12,
            leading=17,
            textColor=MUTED,
            spaceAfter=18,
        ),
        "cover_meta": ParagraphStyle(
            "CoverMeta",
            parent=base["Normal"],
            fontName=REGULAR,
            fontSize=9,
            leading=13,
            textColor=INK,
        ),
        "cover_note": ParagraphStyle(
            "CoverNote",
            parent=base["Normal"],
            fontName=ITALIC,
            fontSize=8.5,
            leading=12.5,
            textColor=MUTED,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName=BOLD,
            fontSize=15.2,
            leading=18.5,
            textColor=INK,
            spaceBefore=12,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName=BOLD,
            fontSize=11.2,
            leading=14.4,
            textColor=INK,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName=REGULAR,
            fontSize=8.9,
            leading=13.1,
            textColor=INK,
            spaceAfter=7,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName=REGULAR,
            fontSize=8.85,
            leading=12.8,
            textColor=INK,
            leftIndent=16,
            firstLineIndent=-10,
            bulletIndent=0,
            spaceAfter=3.5,
        ),
        "quote": ParagraphStyle(
            "Quote",
            parent=base["BodyText"],
            fontName=ITALIC,
            fontSize=8.8,
            leading=13,
            leftIndent=10,
            rightIndent=6,
            borderColor=BLUE,
            borderWidth=1.5,
            borderPadding=(5, 8, 5, 9),
            textColor=MUTED,
            backColor=SOFT,
            spaceBefore=4,
            spaceAfter=9,
        ),
        "code": ParagraphStyle(
            "Code",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.8,
            leading=10.5,
            leftIndent=8,
            rightIndent=8,
            borderColor=LINE,
            borderWidth=0.6,
            borderPadding=7,
            backColor=SOFT,
            textColor=INK,
            spaceBefore=4,
            spaceAfter=9,
        ),
        "table": ParagraphStyle(
            "Table",
            parent=base["BodyText"],
            fontName=REGULAR,
            fontSize=7.25,
            leading=9.4,
            textColor=INK,
        ),
        "table_head": ParagraphStyle(
            "TableHead",
            parent=base["BodyText"],
            fontName=BOLD,
            fontSize=7.25,
            leading=9.4,
            textColor=colors.white,
        ),
    }


STYLES = make_styles()


def official_logo_path() -> Path:
    if LOGO_CACHE.exists() and hashlib.sha256(LOGO_CACHE.read_bytes()).hexdigest() == LOGO_SHA256:
        return LOGO_CACHE
    request = Request(LOGO_URL, headers={"User-Agent": "SPMOS technical report builder/1.0"})
    with urlopen(request, timeout=20) as response:
        content = response.read()
    digest = hashlib.sha256(content).hexdigest()
    if digest != LOGO_SHA256:
        raise RuntimeError(f"Official logo digest mismatch: {digest}")
    LOGO_CACHE.parent.mkdir(parents=True, exist_ok=True)
    LOGO_CACHE.write_bytes(content)
    return LOGO_CACHE


def page_chrome(canvas, doc) -> None:
    canvas.saveState()
    canvas.setTitle("SPM-Polaris: Evidence-Governed Memory and Context Management for Long-Horizon AI Agents")
    canvas.setAuthor("Veridical Tech, Inc.")
    canvas.setSubject("SPM-Polaris technical report v1.0")
    canvas.setCreator("Veridical Tech, Inc.")
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN_X, PAGE_HEIGHT - 13 * mm, PAGE_WIDTH - MARGIN_X, PAGE_HEIGHT - 13 * mm)
        canvas.setFont(REGULAR, 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN_X, PAGE_HEIGHT - 10.3 * mm, "SPM-POLARIS TECHNICAL REPORT · VERSION 1.0")
    canvas.setFont(REGULAR, 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN_X, 9.5 * mm, "VERIDICAL TECH, INC. · EVIDENCE CUTOFF 2026-08-23")
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 9.5 * mm, str(doc.page))
    canvas.restoreState()


def cover_story() -> list:
    meta = [
        [Paragraph("VERSION", STYLES["cover_kicker"]), Paragraph("1.0", STYLES["cover_meta"])],
        [Paragraph("PUBLICATION DATE", STYLES["cover_kicker"]), Paragraph("August 23, 2026", STYLES["cover_meta"])],
        [Paragraph("EVIDENCE CUTOFF", STYLES["cover_kicker"]), Paragraph("August 23, 2026", STYLES["cover_meta"])],
        [Paragraph("AUTHOR & PUBLISHER", STYLES["cover_kicker"]), Paragraph("Veridical Tech, Inc.", STYLES["cover_meta"])],
        [Paragraph("CANONICAL EDITION", STYLES["cover_kicker"]), Paragraph("docs.spmos.ai/technical-report", STYLES["cover_meta"])],
    ]
    meta_table = Table(meta, colWidths=[47 * mm, 89 * mm], hAlign="LEFT")
    meta_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return [
        Spacer(1, 5 * mm),
        Image(str(official_logo_path()), width=48 * mm, height=(48 * 227 / 480) * mm, hAlign="LEFT"),
        Spacer(1, 6 * mm),
        Paragraph("SPM · STELLARPATH MEMORY OPERATING SYSTEM", STYLES["cover_kicker"]),
        HRFlowable(width=30 * mm, thickness=3, color=BLUE, hAlign="LEFT", spaceAfter=15),
        Paragraph("SPM-Polaris: Evidence-Governed Memory and Context Management for Long-Horizon AI Agents", STYLES["cover_title"]),
        Paragraph("A first-party technical report on governed long-term memory, protected context compilation, integration boundaries, deletion, current observations, and the evaluation work still required.", STYLES["cover_deck"]),
        Spacer(1, 8 * mm),
        meta_table,
        Spacer(1, 13 * mm),
        KeepTogether(
            [
                Paragraph("PUBLICATION STATUS", STYLES["cover_kicker"]),
                Paragraph("First-party technical report; not peer reviewed or independently evaluated. This report is not an SLA, compliance certification, legal opinion, investment memorandum, or universal performance guarantee.", STYLES["cover_note"]),
            ]
        ),
        PageBreak(),
    ]


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    frame = Frame(
        MARGIN_X,
        MARGIN_BOTTOM,
        CONTENT_WIDTH,
        PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    document = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title="SPM-Polaris: Evidence-Governed Memory and Context Management for Long-Horizon AI Agents",
        author="Veridical Tech, Inc.",
    )
    document.addPageTemplates([PageTemplate(id="report", frames=[frame], onPage=page_chrome)])
    document.build(
        cover_story()
        + parse_body(
            source,
            styles=STYLES,
            content_width=CONTENT_WIDTH,
            ink=INK,
            line=LINE,
            soft=SOFT,
        )
    )
    print(OUTPUT)


if __name__ == "__main__":
    main()
