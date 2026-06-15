# 03 — IA en ingeniería de software: herramientas, agentes y productividad (2021–2026)

---

## A. Productividad medida (evidencia a favor y en contra)

### A favor — experimento controlado de GitHub/Microsoft (el "55 %")
- **Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023).** *The impact of AI on developer productivity: Evidence from GitHub Copilot* (arXiv:2302.06590). https://arxiv.org/abs/2302.06590
  - 95 desarrolladores; tarea: programar un servidor HTTP en JavaScript. Grupo con Copilot **55,8 % más rápido** (IC 95 %: 21 %–89 %; P=.0017). Tiempo: 1 h 11 min vs 2 h 41 min. Mayor beneficio para menos experimentados.
  - Blog GitHub (n=95): https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/

### Experimentos de campo a gran escala
- **Cui, Z. K., Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2025).** *The effects of generative AI on high-skilled work: Evidence from three field experiments with software developers.* MIT. https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf
  - 4.867 desarrolladores (Microsoft, Accenture, Fortune 100): **+26,08 %** de tareas completadas. "Copilot significantly raises task completion for more recent hires and those in more junior positions but not for… more senior positions."

### En contra — estudio independiente de METR (el "−19 %")
- **METR (2025, 10 de julio).** *Measuring the impact of early-2025 AI on experienced open-source developer productivity.* https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ · arXiv: https://arxiv.org/abs/2507.09089
  - 16 devs experimentados, 246 tareas en repos propios maduros (22k+ estrellas, 1M+ líneas), con Cursor Pro + Claude 3.5/3.7. Resultado: **19 % MÁS lentos** con IA.
  - Brecha percepción/realidad: preveían −24 % (más rápido), creyeron +20 % tras el estudio; en realidad −19 %. Expertos económicos preveían −39 %, ML −38 %.
  - Actualización (24-feb-2026): resultados de inicios de 2025; no extrapolar a herramientas de fines de 2025/2026. https://metr.org/blog/2026-02-24-uplift-update/

### Consultora
- **McKinsey & Company (2023).** *Unleashing developer productivity with generative AI.* https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai
  - Hasta 2× más rápido; documentar −45/50 %, escribir −35/45 %, refactorizar −20/30 %. **Las ganancias caen <10 % en tareas complejas y para menos experimentados.**

> Contraste rhetórico: los dos estudios NO son comparables (tarea greenfield acotada vs. mantenimiento en repos maduros; vendor vs. independiente). El −19 % aplica a seniors en código familiar.

---

## B. SWE-bench (benchmark de resolución de issues reales)

- **Jimenez, C. E., et al. (2024).** *SWE-bench: Can language models resolve real-world GitHub issues?* (ICLR 2024; arXiv:2310.06770). https://arxiv.org/abs/2310.06770 — 2.294 problemas de 12 repos Python; Claude 2 inicial: **1,96 %**.
- **SWE-bench Verified (OpenAI, ago. 2024):** 500 problemas validados por 93 desarrolladores. https://openai.com/index/introducing-swe-bench-verified/

**Trayectoria del estado del arte (Verified, scores estándar):**
| Fecha | Sistema | Score |
|---|---|---|
| mar. 2024 | Devin (subconjunto 25 % del set completo) | 13,86 % |
| oct. 2024 | Claude 3.5 Sonnet (new) | 49,0 % |
| dic. 2024 | OpenAI o3 | ~71,7 % |
| feb. 2025 | Claude 3.7 Sonnet | 63,7 % (70,3 % high-compute) |
| may. 2025 | Claude Opus 4 / Sonnet 4 | 72,5 % / 72,7 % |
| ago. 2025 | GPT-5 | 74,9 % |
| sep. 2025 | Claude Sonnet 4.5 | 77,2 % |

> Caveats: las cifras pre-ago-2024 son sobre otros splits (no Verified); los scores "high-compute" no son comparables con los estándar; OpenAI publicó "Why SWE-bench Verified no longer measures frontier coding capabilities" (saturación). Cifras 2026 con nombres de modelo no verificables fueron descartadas.

---

## C. Agentes de codificación autónomos

- **Devin (Cognition, 12-mar-2024):** "the first AI software engineer". https://cognition.ai/blog/introducing-devin
  - Reality-check: **Husain, Flath & Whitaker (2025), "Thoughts on a month with Devin"** — 3 éxitos / 20 tareas. https://www.answer.ai/posts/2025-01-08-devin.html
  - Valoración (prensa): ~$2 B (2024) → $10,2 B (sep. 2025).
- **Cursor (Anysphere):** Serie D $2,3 B a **$29,3 B** (13-nov-2025, CNBC), >$1 B ARR. https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html
- **Claude Code (Anthropic):** research preview 24-feb-2025; GA 22-may-2025. https://www.anthropic.com/news/claude-4
- **GitHub Copilot coding agent:** "agent mode" 6-feb-2025; coding agent GA sep. 2025. https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/

---

## D. Adopción y % de código generado por IA

- **GitHub Copilot:** >20 millones de usuarios acumulados (jul. 2025, Nadella en earnings; TechCrunch). https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/ — FY2024 (SEC): >1,8 M suscriptores pagos, >77.000 clientes enterprise (+180 % interanual).
- **GitHub (2023):** Copilot escribía en promedio el **46 %** del código en archivos con la herramienta activa (Dohmke). https://github.blog/ai-and-ml/github-copilot/github-copilot-now-has-a-better-ai-model-and-new-capabilities/ — (métrica de aceptación, no auditoría neutral).
- **Pichai (Google, Q3 2024):** "more than a quarter of all new code at Google is generated by AI, then reviewed and accepted by engineers".
- **Nadella (Microsoft, LlamaCon abr. 2025):** 20–30 % del código lo escribe software. https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/
- **Stack Overflow Developer Survey 2025:** 84 % usa o planea usar IA (76 % en 2024); confianza en la exactitud baja a ~29-33 %; 45 % dice que depurar código de IA lleva más tiempo. https://survey.stackoverflow.co/2025/ai/
