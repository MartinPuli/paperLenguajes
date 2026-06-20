#!/usr/bin/env python3
"""Genera el PDF del paper a partir de paper.md (portada, cuerpo justificado,
figuras embebidas, bibliografía con sangría francesa y numeración de página).
No requiere LibreOffice. Uso: python3 build_pdf.py"""
import re, os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import black, Color
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Image, PageBreak, NextPageTemplate)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SRC, OUT = "paper.md", "Paper_Rol_del_ingeniero_informatico_en_10_anios.pdf"

# --- Liberation Serif (métricamente idéntica a Times New Roman) + DejaVu para símbolos
LIB = "/usr/share/fonts/truetype/liberation"
pdfmetrics.registerFont(TTFont("Serif", f"{LIB}/LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-B", f"{LIB}/LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-I", f"{LIB}/LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Serif-BI", f"{LIB}/LiberationSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-B",
                              italic="Serif-I", boldItalic="Serif-BI")
pdfmetrics.registerFont(TTFont("Deja", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))

GRAY = Color(0.25, 0.25, 0.25)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(text):
    t = esc(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = t.replace("⁰", "<super>0</super>")               # TC⁰
    t = t.replace("≠", '<font name="Deja">≠</font>')      # P ≠ NP
    t = t.replace("−", '<font name="Deja">−</font>')      # signo menos
    return t

# --- estilos
body = ParagraphStyle("body", fontName="Serif", fontSize=11.5, leading=18,
                      alignment=TA_JUSTIFY, firstLineIndent=0.4*cm, spaceAfter=6)
h1 = ParagraphStyle("h1", fontName="Serif-B", fontSize=13, leading=17,
                    spaceBefore=14, spaceAfter=6, textColor=black)
cap = ParagraphStyle("cap", fontName="Serif-I", fontSize=9, leading=12,
                     alignment=TA_CENTER, textColor=GRAY, spaceAfter=12, spaceBefore=4)
biblio = ParagraphStyle("biblio", fontName="Serif", fontSize=10.5, leading=15,
                        alignment=TA_LEFT, leftIndent=0.5*cm, firstLineIndent=-0.5*cm,
                        spaceAfter=5)
def cs(size, bold=False):  # estilo centrado para portada
    return ParagraphStyle(f"c{size}{bold}", fontName="Serif-B" if bold else "Serif",
                          fontSize=size, leading=size*1.3, alignment=TA_CENTER)

# --- leer markdown
lines = open(SRC, encoding="utf-8").read().split("\n")
title = lines[0].lstrip("# ").strip()
IMG = re.compile(r"^!\[(.*)\]\(([^()]+)\)\s*$")
CONTENT_W = A4[0] - 2*2.5*cm

story = []
# ---------- portada ----------
story += [Spacer(1, 3.2*cm),
          Paragraph("UNIVERSIDAD DEL CEMA", cs(15, True)), Spacer(1, 0.2*cm),
          Paragraph("Buenos Aires, Argentina", cs(12)), Spacer(1, 1.6*cm),
          Paragraph(inline(title), cs(15, True)), Spacer(1, 0.9*cm),
          Paragraph("Trabajo Práctico Final", cs(12)), Spacer(1, 1.8*cm),
          Paragraph("Carrera: Ingeniería Informática (3.er año)", cs(12)), Spacer(1, 0.25*cm),
          Paragraph("Materia: Lenguajes Formales y Teoría de la Computación", cs(12)), Spacer(1, 0.25*cm),
          Paragraph("Profesor/a: ______________________________", cs(12)), Spacer(1, 0.25*cm),
          Paragraph("Integrantes: Martín Ezequiel Pulitano y Nicolás Silva", cs(12)), Spacer(1, 1.6*cm),
          Paragraph("Junio de 2026", cs(12)),
          NextPageTemplate("body"), PageBreak()]

# ---------- cuerpo ----------
in_biblio = False
for raw in lines[1:]:
    s = raw.strip()
    if not s:
        continue
    if s.startswith("## "):
        txt = s[3:].strip()
        in_biblio = txt.lower().startswith(("bibliograf", "referencia"))
        story.append(Paragraph(inline(txt), h1))
        continue
    m = IMG.match(s)
    if m:
        caption, path = m.group(1), m.group(2)
        if os.path.exists(path):
            iw, ih = PILImage.open(path).size
            w = min(CONTENT_W, 15.5*cm)
            story.append(Image(path, width=w, height=w*ih/iw))
            story.append(Paragraph(inline(caption), cap))
        continue
    story.append(Paragraph(inline(s), biblio if in_biblio else body))

# ---------- numeración de página (salvo portada) ----------
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Serif", 10)
    canvas.drawCentredString(A4[0]/2, 1.3*cm, str(canvas.getPageNumber()))
    canvas.restoreState()

frame = Frame(2.5*cm, 2.2*cm, CONTENT_W, A4[1]-2.2*cm-2.2*cm, id="f")
doc = BaseDocTemplate(OUT, pagesize=A4,
                      pageTemplates=[PageTemplate(id="cover", frames=[frame]),
                                     PageTemplate(id="body", frames=[frame], onPage=footer)])
doc.title = title
doc.build(story)
print("Escrito:", OUT)
