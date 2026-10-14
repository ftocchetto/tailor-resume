#!/usr/bin/env python3

"""Minimal Markdown resume -> 1-page PDF renderer.

Supports a small subset of Markdown used in this repo:
- "# " title line (name)
- plain contact line(s)
- "## " section headers
- "**...**" emphasis (stripped)
- "- " bullets

Goal: generate an ATS-friendly, single-page PDF with conservative styling.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


MD_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def strip_md(s: str) -> str:
    s = s.rstrip("\n")
    s = MD_BOLD_RE.sub(r"\1", s)
    return s


def wrap_text(text: str, font_name: str, font_size: float, max_width: float) -> List[str]:
    """Greedy word wrap using reportlab stringWidth."""
    text = text.strip()
    if not text:
        return [""]

    words = text.split()
    lines: List[str] = []
    current: List[str] = []

    for w in words:
        trial = (" ".join(current + [w])).strip()
        if stringWidth(trial, font_name, font_size) <= max_width or not current:
            current.append(w)
        else:
            lines.append(" ".join(current))
            current = [w]

    if current:
        lines.append(" ".join(current))
    return lines


@dataclass
class Style:
    font: str
    size: float
    leading: float
    bold: bool = False


@dataclass
class Block:
    kind: str  # title, contact, h2, job, bullet, para, spacer
    text: str


def parse_blocks(md_lines: Iterable[str]) -> List[Block]:
    blocks: List[Block] = []

    for raw in md_lines:
        line = raw.rstrip("\n")
        if not line.strip():
            blocks.append(Block("spacer", ""))
            continue

        if line.startswith("# "):
            blocks.append(Block("title", strip_md(line[2:].strip())))
            continue

        if line.startswith("## "):
            blocks.append(Block("h2", strip_md(line[3:].strip())))
            continue

        if line.startswith("### "):
            blocks.append(Block("job", strip_md(line[4:].strip())))
            continue

        if line.startswith("- "):
            blocks.append(Block("bullet", strip_md(line[2:].strip())))
            continue

        # Job/header lines are bolded in the source (e.g., **Role** | Company | Dates)
        if line.lstrip().startswith("**") and "|" in line:
            blocks.append(Block("job", strip_md(line.strip())))
            continue

        # Everything else is a paragraph/contact line
        blocks.append(Block("para", strip_md(line.strip())))

    # Trim leading/trailing spacers
    while blocks and blocks[0].kind == "spacer":
        blocks.pop(0)
    while blocks and blocks[-1].kind == "spacer":
        blocks.pop()
    return blocks


def layout_height(
    blocks: List[Block],
    page_width: float,
    page_height: float,
    margin: float,
    body_size: float,
) -> float:
    content_width = page_width - 2 * margin
    y = page_height - margin

    # Derived sizes
    name_size = max(14.0, body_size * 1.75)
    h2_size = body_size + 1.2
    job_size = body_size + 0.3
    para_leading = body_size + 2.0
    tight_leading = body_size + 1.4
    h2_leading = h2_size + 2.0
    name_leading = name_size + 3.0

    for b in blocks:
        if b.kind == "spacer":
            y -= body_size * 0.65
            continue

        if b.kind == "title":
            y -= name_leading
            continue

        if b.kind == "h2":
            y -= h2_leading
            y -= 2.0  # underline gap
            continue

        if b.kind == "job":
            lines = wrap_text(b.text, "Helvetica-Bold", job_size, content_width)
            y -= len(lines) * tight_leading
            y -= body_size * 0.25
            continue

        if b.kind == "bullet":
            bullet_indent = 12.0
            lines = wrap_text(b.text, "Helvetica", body_size, content_width - bullet_indent)
            y -= len(lines) * tight_leading
            continue

        # para
        lines = wrap_text(b.text, "Helvetica", body_size, content_width)
        y -= len(lines) * para_leading
        continue

    return y


def block_height(block: Block, content_width: float, body_size: float) -> float:
    name_size = max(14.0, body_size * 1.75)
    h2_size = body_size + 1.2
    job_size = body_size + 0.3
    para_leading = body_size + 2.0
    tight_leading = body_size + 1.4
    h2_leading = h2_size + 2.0
    name_leading = name_size + 3.0

    if block.kind == "spacer":
        return body_size * 0.65

    if block.kind == "title":
        return name_leading

    if block.kind == "h2":
        return h2_leading + 4.0

    if block.kind == "job":
        lines = wrap_text(block.text, "Helvetica-Bold", job_size, content_width)
        return len(lines) * tight_leading + body_size * 0.25

    if block.kind == "bullet":
        bullet_indent = 12.0
        lines = wrap_text(block.text, "Helvetica", body_size, content_width - bullet_indent)
        return len(lines) * tight_leading

    lines = wrap_text(block.text, "Helvetica", body_size, content_width)
    return len(lines) * para_leading


def render_pdf(md_path: Path, pdf_path: Path) -> None:
    blocks = parse_blocks(md_path.read_text(encoding="utf-8").splitlines(True))

    page_w, page_h = letter
    margin = 0.60 * inch

    # Fit-to-one-page: start at a readable size, reduce if needed
    body = 9.2
    min_body = 7.4
    safety_padding = 24.0
    while True:
        bottom_y = layout_height(blocks, page_w, page_h, margin, body)
        if bottom_y >= margin + body * 1.6 + safety_padding:
            break
        body -= 0.2
        if body < min_body:
            # Render anyway; caller can adjust content.
            break

    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    content_w = page_w - 2 * margin
    y = page_h - margin

    name_size = max(14.0, body * 1.75)
    h2_size = body + 1.2
    job_size = body + 0.3
    para_leading = body + 2.0
    tight_leading = body + 1.4
    h2_leading = h2_size + 2.0
    name_leading = name_size + 3.0

    for b in blocks:
        needed = block_height(b, content_w, body)
        if y - needed < margin:
            c.showPage()
            y = page_h - margin

        if b.kind == "spacer":
            y -= body * 0.65
            continue

        if b.kind == "title":
            c.setFont("Helvetica-Bold", name_size)
            c.drawCentredString(page_w / 2.0, y - name_size, b.text)
            y -= name_leading
            continue

        if b.kind == "h2":
            c.setFont("Helvetica-Bold", h2_size)
            text = b.text.upper()
            c.drawString(margin, y - h2_size, text)
            y -= h2_leading
            # underline
            c.setLineWidth(0.6)
            c.line(margin, y, margin + content_w, y)
            y -= 4.0
            continue

        if b.kind == "job":
            c.setFont("Helvetica-Bold", job_size)
            for line in wrap_text(b.text, "Helvetica-Bold", job_size, content_w):
                c.drawString(margin, y - job_size, line)
                y -= tight_leading
            y -= body * 0.25
            continue

        if b.kind == "bullet":
            bullet_indent = 12.0
            c.setFont("Helvetica", body)
            c.drawString(margin, y - body, "-")
            x = margin + bullet_indent
            for i, line in enumerate(wrap_text(b.text, "Helvetica", body, content_w - bullet_indent)):
                c.drawString(x, y - body, line)
                y -= tight_leading
            continue

        # para
        c.setFont("Helvetica", body)
        for line in wrap_text(b.text, "Helvetica", body, content_w):
            c.drawString(margin, y - body, line)
            y -= para_leading

    c.showPage()
    c.save()


def main(argv: List[str]) -> int:
    if len(argv) != 3:
        print("Usage: md_resume_to_pdf.py INPUT.md OUTPUT.pdf", file=sys.stderr)
        return 2
    md_path = Path(argv[1]).expanduser().resolve()
    pdf_path = Path(argv[2]).expanduser().resolve()
    if not md_path.exists():
        print(f"Input not found: {md_path}", file=sys.stderr)
        return 2
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    render_pdf(md_path, pdf_path)
    print(str(pdf_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
