# Trabajo Práctico Final — Lenguajes Formales y Teoría de la Computación

**Tema:** El rol del ingeniero informático en los próximos diez años.

**Hipótesis:** el ingeniero no será reemplazado por la IA, sino que su rol se
transformará: dejará de centrarse en la ejecución técnica para enfocarse en la
especificación, la integración, la validación y la supervisión crítica de
sistemas automatizados.

## Archivos

| Archivo | Descripción |
|---|---|
| `paper.md` | Fuente del paper (Markdown, editable). ~2.998 palabras de cuerpo; 44 referencias APA 7. |
| `Paper_Rol_del_ingeniero_informatico_en_10_anios.pdf` | **Versión final para entregar** (portada con datos, cuerpo justificado, figuras y bibliografía APA con sangría francesa). |
| `Paper_Rol_del_ingeniero_informatico_en_10_anios.docx` | Misma versión en editable (Word). |
| `fuentes_adicionales.md` | Dossier de investigación: ~50 fuentes verificadas (papers, informes, artículos) con cita APA + DOI/URL + hallazgo clave, organizadas por eje temático. Base ampliada para profundizar cualquier sección. |
| `investigacion/` | **Toda** la información recopilada, por tema (8 archivos + índice): teoría de la computación, transformers↔lenguajes formales, IA en ingeniería de software, calidad/seguridad, visiones de expertos, economía/empleo, historia/precedentes, epistemología/surveys. Incluye citas exactas, cifras, fuentes y advertencias de fiabilidad. |
| `figuras/` | 6 figuras profesionales (PNG 300 dpi) generadas con datos verificados: SWE-bench, productividad lab vs. real, jerarquía de Chomsky/transformers, divergencia del empleo, empleo a 2030 (WEF) y seguridad del código. |
| `build_figures.py` | Genera las figuras (`pip install matplotlib`). |
| `build_docx.py` | Genera el `.docx` a partir de `paper.md` (embebe las figuras y agrega numeración de página). |
| `build_pdf.py` | Genera el `.pdf` final a partir de `paper.md` (Liberation Serif, figuras y numeración; `pip install reportlab pillow`). |

## Regenerar todo

```bash
pip install python-docx reportlab pillow matplotlib
python3 build_figures.py   # crea figuras/
python3 build_docx.py      # crea el .docx con figuras embebidas
python3 build_pdf.py       # crea el .pdf final
```

## Notas

- Portada: **Integrantes** (Martín Ezequiel Pulitano y Nicolás Silva), carrera y materia
  ya cargados; el campo **Profesor/a** quedó como línea para completar a mano.
- Extensión: cuerpo en prosa (Introducción → Conclusión) ≈ 2.998 palabras, dentro
  del máximo de 3.000. El resumen, los pies de figura y la bibliografía van aparte.
- 6 figuras embebidas + numeración de página. Todas las citas en APA 7, verificadas
  con fuentes primarias.
