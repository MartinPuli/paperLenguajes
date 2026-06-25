#!/usr/bin/env python3
"""Genera un PDF académico a partir de paper.md (portada, cuerpo justificado,
figuras, bibliografía con sangría francesa, numeración de página).
Uso: python3 build_pdf.py"""
import re, os
import matplotlib
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, PageBreak, NextPageTemplate, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SRC = "paper.md"
OUT = "Paper_Rol_del_ingeniero_informatico_en_10_anios.pdf"

# --- fuente serif con cobertura Unicode (DejaVu Serif, incluida con matplotlib) ---
FDIR = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")
pdfmetrics.registerFont(TTFont("Serif", os.path.join(FDIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Bold", os.path.join(FDIR, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Italic", os.path.join(FDIR, "DejaVuSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Serif-BoldItalic", os.path.join(FDIR, "DejaVuSerif-BoldItalic.ttf")))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                              italic="Serif-Italic", boldItalic="Serif-BoldItalic")

INLINE = re.compile(r'(\*\*.+?\*\*|\*[^*]+?\*)')
IMG = re.compile(r'^!\[(.*)\]\(([^()]+)\)\s*$')

def md_inline(text):
    def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    out, pos = [], 0
    for m in INLINE.finditer(text):
        if m.start() > pos: out.append(esc(text[pos:m.start()]))
        seg = m.group(0)
        if seg.startswith("**"): out.append("<b>" + esc(seg[2:-2]) + "</b>")
        else: out.append("<i>" + esc(seg[1:-1]) + "</i>")
        pos = m.end()
    if pos < len(text): out.append(esc(text[pos:]))
    return "".join(out)

# --- estilos ---------------------------------------------------------------
GRAY = HexColor("#404040")
body = ParagraphStyle("body", fontName="Serif", fontSize=11, leading=16.5,
                      alignment=TA_JUSTIFY, firstLineIndent=0.4 * cm, spaceAfter=6)
h1 = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=13, leading=16,
                    spaceBefore=14, spaceAfter=6, alignment=TA_LEFT)
h2 = ParagraphStyle("h2", fontName="Serif-Bold", fontSize=11.5, leading=15,
                    spaceBefore=10, spaceAfter=4, alignment=TA_LEFT)
cap = ParagraphStyle("cap", fontName="Serif-Italic", fontSize=9, leading=12,
                     alignment=TA_CENTER, textColor=GRAY, spaceBefore=4, spaceAfter=12)
biblio = ParagraphStyle("biblio", fontName="Serif", fontSize=10.5, leading=14,
                        alignment=TA_LEFT, leftIndent=1.1 * cm, firstLineIndent=-1.1 * cm,
                        spaceAfter=5)
kw = ParagraphStyle("kw", parent=body, firstLineIndent=0, spaceBefore=4)

def cen(size, bold=False, sb=0, sa=0):
    return ParagraphStyle(f"c{size}{bold}{sb}{sa}", fontName="Serif-Bold" if bold else "Serif",
                          fontSize=size, leading=size * 1.3, alignment=TA_CENTER,
                          spaceBefore=sb, spaceAfter=sa)

# --- leer markdown ---------------------------------------------------------
lines = open(SRC, encoding="utf-8").read().split("\n")
title = lines[0].lstrip("# ").strip()
rest = lines[1:]

story = []
# Portada
story += [
    Spacer(1, 1.4 * cm),
    Paragraph("UNIVERSIDAD DEL CEMA", cen(15, True)),
    Paragraph("Buenos Aires, Argentina", cen(11, sa=70)),
    Paragraph(title, cen(16, True, sb=40, sa=40)),
    Paragraph("Trabajo Práctico Final", cen(12, sa=90)),
    Paragraph("Carrera de grado: Ingeniería Informática", cen(11, sb=20)),
    Paragraph("Materia: Lenguajes Formales y Teoría de la Computación", cen(11)),
    Paragraph("Profesor: Mario Moreno", cen(11)),
    Paragraph("Integrantes: Martín Ezequiel Pulitano y Nicolás Ulises Silva", cen(11)),
    Paragraph("Junio de 2026", cen(11, sb=70)),
    NextPageTemplate("body"),
    PageBreak(),
]

FRAME_W = A4[0] - 2 * 2.4 * cm
in_biblio = False
for raw in rest:
    line = raw.strip()
    if not line:
        continue
    if line.startswith("# "):
        continue
    if line.startswith("## "):
        t = line[3:].strip()
        in_biblio = t.lower().startswith(("bibliograf", "referencia"))
        story.append(Paragraph(md_inline(t), h1))
        continue
    if line.startswith("### "):
        story.append(Paragraph(md_inline(line[4:].strip()), h2))
        continue
    if line.startswith("**Palabras clave"):
        story.append(Paragraph(md_inline(line), kw))
        continue
    mimg = IMG.match(line)
    if mimg:
        caption, path = mimg.group(1), mimg.group(2)
        iw, ih = PILImage.open(path).size
        w = min(15 * cm, FRAME_W)
        h = w * ih / iw
        story.append(KeepTogether([
            Spacer(1, 4),
            Image(path, width=w, height=h, hAlign="CENTER"),
            Paragraph(md_inline(caption), cap),
        ]))
        continue
    story.append(Paragraph(md_inline(line), biblio if in_biblio else body))

# --- plantillas de página (portada sin pie; resto con número) --------------
def make_frame():
    return Frame(2.4 * cm, 2.0 * cm, FRAME_W, A4[1] - 2.0 * cm - 2.2 * cm, id="f")

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Serif", 9)
    canvas.drawCentredString(A4[0] / 2, 1.2 * cm, str(doc.page))
    canvas.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, title=title,
                      author="Martín Ezequiel Pulitano; Nicolás Ulises Silva")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[make_frame()]),
    PageTemplate(id="body", frames=[make_frame()], onPage=footer),
])
doc.build(story)
print("Escrito:", OUT)
