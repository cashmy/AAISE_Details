from __future__ import annotations

import html
import re
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


BASE_DIR = Path(__file__).resolve().parent
ARTICLE = BASE_DIR / "JavaScript_as_a_Gateway_Article.md"
OUTPUT = BASE_DIR / "JavaScript_as_a_Gateway_Article.pdf"


def inline_markup(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)

    def link(match: re.Match[str]) -> str:
        label = match.group(1)
        url = match.group(2)
        return f'<a href="{html.escape(url, quote=True)}" color="#174EA6">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", link, text)
    return text


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(inline_markup(text), style)


def image_flowable(markdown_line: str, caption_line: str | None, styles: dict[str, ParagraphStyle]):
    match = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", markdown_line)
    if not match:
        return []

    image_path = BASE_DIR / match.group(2)
    max_width = 7.0 * inch
    max_height = 3.95 * inch
    with PILImage.open(image_path) as img:
        width, height = img.size

    scale = min(max_width / width, max_height / height)
    flowables = [
        Image(str(image_path), width=width * scale, height=height * scale),
        Spacer(1, 0.08 * inch),
    ]
    if caption_line:
        caption = caption_line.strip()
        if caption.startswith("*") and caption.endswith("*"):
            caption = caption[1:-1]
        flowables.append(paragraph(caption, styles["Caption"]))
    return [KeepTogether(flowables), Spacer(1, 0.16 * inch)]


def table_flowable(rows: list[str], styles: dict[str, ParagraphStyle]) -> Table:
    parsed: list[list[Paragraph]] = []
    for row in rows:
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        parsed.append([Paragraph(inline_markup(cell), styles["TableCell"]) for cell in cells])

    table = Table(parsed, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAF2FF")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#0B2347")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D0D7E2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def build_story() -> list:
    styles = getSampleStyleSheet()
    custom = {
        "Title": ParagraphStyle(
            "Title",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=34,
            textColor=colors.HexColor("#0B2347"),
            alignment=TA_LEFT,
            spaceAfter=10,
        ),
        "Subtitle": ParagraphStyle(
            "Subtitle",
            parent=styles["Heading2"],
            fontName="Helvetica",
            fontSize=15,
            leading=20,
            textColor=colors.HexColor("#536B8C"),
            spaceAfter=18,
        ),
        "H1": ParagraphStyle(
            "H1",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=23,
            textColor=colors.HexColor("#0B2347"),
            spaceBefore=16,
            spaceAfter=8,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=colors.HexColor("#174EA6"),
            spaceBefore=10,
            spaceAfter=6,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=colors.HexColor("#1F2937"),
            spaceAfter=8,
        ),
        "Caption": ParagraphStyle(
            "Caption",
            parent=styles["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#536B8C"),
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "Quote": ParagraphStyle(
            "Quote",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#0B2347"),
            leftIndent=18,
            rightIndent=18,
            borderColor=colors.HexColor("#D7E6FA"),
            borderWidth=1,
            borderPadding=8,
            backColor=colors.HexColor("#F4F8FE"),
            spaceBefore=6,
            spaceAfter=10,
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.2,
            leading=14,
            textColor=colors.HexColor("#1F2937"),
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.6,
            textColor=colors.HexColor("#1F2937"),
        ),
    }

    lines = ARTICLE.read_text(encoding="utf-8").splitlines()
    story: list = []
    pending_para: list[str] = []
    pending_list: list[tuple[str, bool]] = []

    def flush_para():
        nonlocal pending_para
        if pending_para:
            story.append(paragraph(" ".join(pending_para), custom["Body"]))
            pending_para = []

    def flush_list():
        nonlocal pending_list
        if pending_list:
            ordered_count = 1
            for item, ordered in pending_list:
                if ordered:
                    marker = f"{ordered_count}. "
                    ordered_count += 1
                else:
                    marker = "- "
                story.append(paragraph(marker + item, custom["Bullet"]))
            story.append(Spacer(1, 0.05 * inch))
            pending_list = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_para()
            flush_list()
            i += 1
            continue

        if stripped == "---":
            flush_para()
            flush_list()
            story.append(Spacer(1, 0.08 * inch))
            i += 1
            continue

        if stripped.startswith("!["):
            flush_para()
            flush_list()
            caption = None
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("*Figure"):
                caption = lines[i + 1].strip()
                i += 1
            story.extend(image_flowable(stripped, caption, custom))
            i += 1
            continue

        if stripped.startswith("|"):
            flush_para()
            flush_list()
            rows: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                current = lines[i].strip()
                if not re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", current):
                    rows.append(current)
                i += 1
            story.append(table_flowable(rows, custom))
            story.append(Spacer(1, 0.14 * inch))
            continue

        bullet_match = re.match(r"^[-]\s+(.+)", stripped)
        number_match = re.match(r"^\d+\.\s+(.+)", stripped)
        if bullet_match or number_match:
            flush_para()
            ordered = bool(number_match)
            pending_list.append(((bullet_match or number_match).group(1), ordered))
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                next_match = re.match(r"^[-]\s+(.+)", next_line)
                next_num = re.match(r"^\d+\.\s+(.+)", next_line)
                if ordered and next_num:
                    pending_list.append((next_num.group(1), True))
                elif not ordered and next_match:
                    pending_list.append((next_match.group(1), False))
                else:
                    break
                i += 1
            flush_list()
            continue

        if stripped.startswith(">"):
            flush_para()
            flush_list()
            story.append(paragraph(stripped.lstrip("> "), custom["Quote"]))
            i += 1
            continue

        if stripped.startswith("# "):
            flush_para()
            flush_list()
            text = stripped[2:]
            if story:
                story.append(PageBreak())
            story.append(paragraph(text, custom["Title"] if not story else custom["H1"]))
            i += 1
            continue

        if stripped.startswith("## "):
            flush_para()
            flush_list()
            if stripped.startswith("## Figure"):
                if story:
                    story.append(PageBreak())
                story.append(paragraph(stripped[3:], custom["H2"]))
                i += 1
                while i < len(lines) and not lines[i].strip():
                    i += 1
                if i < len(lines) and lines[i].strip().startswith("!["):
                    image_line = lines[i].strip()
                    caption = None
                    if i + 1 < len(lines) and lines[i + 1].strip().startswith("*Figure"):
                        caption = lines[i + 1].strip()
                        i += 1
                    story.extend(image_flowable(image_line, caption, custom))
                    i += 1
                continue
            style = custom["Subtitle"] if len(story) == 1 else custom["H2"]
            story.append(paragraph(stripped[3:], style))
            i += 1
            continue

        pending_para.append(stripped)
        i += 1

    flush_para()
    flush_list()
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(doc.leftMargin, 0.38 * inch, "JavaScript as a Gateway")
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.38 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main() -> None:
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.65 * inch,
        title="JavaScript as a Gateway",
        author="Web Development Foundations",
    )
    doc.build(build_story(), onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    main()
