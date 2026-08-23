"""Convert the report's constrained Markdown subset into ReportLab flowables."""

from __future__ import annotations

import html
import re

from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle


def inline_markdown(text: str) -> str:
    value = html.escape(text.strip())
    value = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" color="#2F63F5"><u>\1</u></a>',
        value,
    )
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


def make_table(rows, *, styles, content_width, ink, line, soft) -> Table:
    rows = [row for index, row in enumerate(rows) if index != 1]
    columns = len(rows[0])
    if columns == 5:
        widths = [0.17, 0.19, 0.23, 0.23, 0.18]
    elif columns == 3:
        widths = [0.27, 0.28, 0.45]
    else:
        widths = [1 / columns] * columns
    data = []
    for row_index, row in enumerate(rows):
        style = styles["table_head"] if row_index == 0 else styles["table"]
        padded = row + [""] * (columns - len(row))
        data.append([Paragraph(inline_markdown(cell), style) for cell in padded[:columns]])
    table = Table(data, colWidths=[content_width * width for width in widths], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ink),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, soft]),
                ("GRID", (0, 0), (-1, -1), 0.4, line),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    table.spaceBefore = 4
    table.spaceAfter = 10
    return table


def parse_body(source: str, *, styles, content_width, ink, line, soft) -> list:
    lines = source.splitlines()
    start = next(index for index, value in enumerate(lines) if value == "## Abstract")
    lines = lines[start:]
    story: list = []
    index = 0
    while index < len(lines):
        value = lines[index].rstrip()
        if not value:
            index += 1
            continue
        if value.startswith("```"):
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            story.append(Paragraph("<br/>".join(html.escape(item) for item in code_lines), styles["code"]))
            index += 1
            continue
        if value.startswith("| "):
            rows = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            story.append(
                make_table(
                    rows,
                    styles=styles,
                    content_width=content_width,
                    ink=ink,
                    line=line,
                    soft=soft,
                )
            )
            continue
        if value.startswith("## "):
            story.append(Paragraph(inline_markdown(value[3:]), styles["h2"]))
            index += 1
            continue
        if value.startswith("### "):
            story.append(Paragraph(inline_markdown(value[4:]), styles["h3"]))
            index += 1
            continue
        if value.startswith("> "):
            quote = []
            while index < len(lines) and lines[index].startswith("> "):
                quote.append(lines[index][2:].strip())
                index += 1
            story.append(Paragraph(inline_markdown(" ".join(quote)), styles["quote"]))
            continue
        if re.match(r"^- ", value):
            while index < len(lines) and re.match(r"^- ", lines[index]):
                story.append(Paragraph(inline_markdown(lines[index][2:]), styles["bullet"], bulletText="•"))
                index += 1
            story.append(Spacer(1, 3))
            continue
        if re.match(r"^\d+\. ", value):
            while index < len(lines) and re.match(r"^\d+\. ", lines[index]):
                number = re.match(r"^(\d+)\. ", lines[index]).group(1)
                item_text = re.sub(r"^\d+\. ", "", lines[index])
                story.append(Paragraph(inline_markdown(item_text), styles["bullet"], bulletText=f"{number}."))
                index += 1
            story.append(Spacer(1, 3))
            continue

        paragraph = [value.strip()]
        index += 1
        while index < len(lines):
            candidate = lines[index].rstrip()
            if not candidate or candidate.startswith(("## ", "### ", "```", "> ", "| ")):
                break
            if re.match(r"^(?:- |\d+\. )", candidate):
                break
            paragraph.append(candidate.strip())
            index += 1
        story.append(Paragraph(inline_markdown(" ".join(paragraph)), styles["body"]))
    return story
