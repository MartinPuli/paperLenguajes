# Dossier de investigación — El rol del ingeniero informático en los próximos 10 años

Compilación de fuentes verificadas (con cita APA 7, hallazgo clave y enlace) para ampliar o defender el paper. Organizado por ejes temáticos que responden a la pregunta central. Todas las fuentes fueron verificadas contra el origen primario salvo donde se indica. Las marcadas con ★ son las **integradas en el paper**; el resto es material adicional disponible.

> Nota de fiabilidad: las fuentes peer-reviewed (revistas/conferencias con DOI) son las más sólidas; los informes de empresa/consultora y la prensa se señalan como tales y conviene atribuirlos explícitamente ("según…").

---

## Eje A — Cómo evolucionó el rol del ingeniero (historia y "escalera de abstracción")

- ★ **Naur, P., & Randell, B. (Eds.). (1969).** *Software engineering: Report on a conference sponsored by the NATO Science Committee, Garmisch, Germany, 7th–11th October 1968.* NATO. — Conferencia que acuñó "ingeniería de software" y la "crisis del software". https://archive.org/details/softwareengineer0000unse
- ★ **Dijkstra, E. W. (1972).** The humble programmer. *Communications of the ACM, 15*(10), 859–866. https://doi.org/10.1145/355604.361591 — La complejidad crece con la potencia de la máquina; programar es gestionar el límite cognitivo humano.
- **Dijkstra, E. W. (1968).** Go to statement considered harmful. *CACM, 11*(3), 147–148. https://doi.org/10.1145/362929.362947 — Inicio de la programación estructurada.
- **Ensmenger, N. L. (2010).** *The computer boys take over: Computers, programmers, and the politics of technical expertise.* MIT Press. — El "reemplazo del programador" se anuncia con regularidad ritual desde los años 50; el programador siempre siguió siendo esencial.
- **Lehman, M. M. (1980).** Programs, life cycles, and laws of software evolution. *Proceedings of the IEEE, 68*(9), 1060–1076. https://doi.org/10.1109/PROC.1980.11805 — El software del mundo real (tipo E) debe evolucionar continuamente o se vuelve obsoleto.
- **Backus, J. (FORTRAN, 1957) / Hopper, G. (FLOW-MATIC→COBOL, 1959).** Cada lenguaje de alto nivel fue temido como "programación automática" que volvería innecesarios a los programadores; en cambio multiplicó su número. Contexto: https://en.wikipedia.org/wiki/History_of_programming_languages
- **GitHub Copilot (2021):** primer "programador en par" basado en IA. https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/

### Precedentes de "el fin de la programación" (que no se cumplieron)
- ★ **Welsh, M. (2023).** The end of programming. *CACM, 66*(1), 34–35. https://doi.org/10.1145/3570220 — Tesis disruptiva ("most software… will be replaced by AI systems that are trained rather than programmed"); útil como postura a refutar.
- **Martin, J. (1981).** *Application Development Without Programmers.* Prentice-Hall. — Promesa de los 4GL: aplicaciones "sin programadores". No ocurrió.
- **O'Reilly, T. (2025, 4 de febrero).** *The end of programming as we know it.* O'Reilly Radar. https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it/ — Cada ola de abstracción produjo MÁS programadores, no menos.
- **Parnas, D. L. (1985).** Software aspects of strategic defense systems. *CACM, 28*(12), 1326–1335. https://doi.org/10.1145/214956.214961 — La "programación automática" no elimina la carga humana de especificar bien.

---

## Eje B — Estado actual: IA agéntica, productividad y límites medidos (2021–2026)

- ★ **Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023).** *The impact of AI on developer productivity: Evidence from GitHub Copilot* (arXiv:2302.06590). — Grupo con Copilot completó una tarea acotada **55,8 % más rápido**. https://arxiv.org/abs/2302.06590
- **Cui, Z. K., Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2025).** *The effects of generative AI on high-skilled work: Evidence from three field experiments with software developers.* — +26,08 % de tareas completadas con Copilot (4.867 devs); los **juniors** se benefician más. https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf
- ★ **METR (2025, 10 de julio).** *Measuring the impact of early-2025 AI on experienced open-source developer productivity.* — Devs experimentados **19 % MÁS lentos** con IA en repos propios maduros, aunque creían ir 20 % más rápido. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- **Jimenez, C. E., et al. (2024).** *SWE-bench: Can language models resolve real-world GitHub issues?* (ICLR 2024; arXiv:2310.06770). — El benchmark; Claude 2 resolvía solo 1,96 % al inicio. SWE-bench Verified (OpenAI, 2024): 500 problemas validados por humanos. https://arxiv.org/abs/2310.06770
- ★ **Anthropic (2025).** *Claude Sonnet 4.5 / Claude 4* — Estado del arte en SWE-bench Verified: de ~14 % (Devin, mar. 2024) a ~77 % (Sonnet 4.5, sep. 2025). https://www.anthropic.com/news/claude-sonnet-4-5
- **Cognition (2024, 12 de marzo).** *Introducing Devin, the first AI software engineer.* https://cognition.ai/blog/introducing-devin — y el reality-check independiente: **Husain, Flath & Whitaker (2025), "Thoughts on a month with Devin"** (3 éxitos de 20 tareas). https://www.answer.ai/posts/2025-01-08-devin.html
- ★ **McKinsey & Company (2023).** *Unleashing developer productivity with generative AI.* — Hasta 2× más rápido en tareas acotadas; ganancias caen <10 % en tareas complejas y para menos expertos. https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai
- **Stack Overflow (2025).** *Developer Survey 2025 — AI.* — 84 % usa o planea usar IA, pero la confianza en su exactitud cayó a ~29-33 %; 45 % dice que depurar código de IA lleva más tiempo. https://survey.stackoverflow.co/2025/ai/
- **Penetración en el código (declaraciones citables):** Pichai (Google, 2024): >25 % del código nuevo lo genera la IA; Nadella (Microsoft, abr. 2025): 20-30 % (Zeff, TechCrunch). https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/

---

## Eje C — Fundamento teórico (la conexión con Lenguajes Formales y Computabilidad)

### Indecidibilidad, complejidad y especificación
- ★ **Turing, A. M. (1936).** On computable numbers… *Proc. London Math. Soc., s2-42*(1), 230–265. https://doi.org/10.1112/plms/s2-42.1.230 — Problema de la detención: indecidible.
- ★ **Rice, H. G. (1953).** Classes of recursively enumerable sets… *Trans. AMS, 74*(2), 358–366. https://doi.org/10.1090/S0002-9947-1953-0053041-6 — Toda propiedad semántica no trivial es indecidible ⇒ no hay verificación universal automática.
- ★ **Cook, S. A. (1971).** The complexity of theorem-proving procedures. *STOC '71*, 151–158. https://doi.org/10.1145/800157.805047 — NP-completitud; base de P vs NP.
- ★ **Chomsky, N. (1956).** Three models for the description of language. *IRE Trans. Inf. Theory, 2*(3), 113–124. https://doi.org/10.1109/TIT.1956.1056813 — La jerarquía de lenguajes formales.
- ★ **Brooks, F. P. (1987).** No silver bullet. *Computer, 20*(4), 10–19. https://doi.org/10.1109/MC.1987.1663532 — Complejidad esencial vs. accidental.
- ★ **Naur, P. (1985).** Programming as theory building. *Microprocessing and Microprogramming, 15*(5), 253–261. https://doi.org/10.1016/0165-6074(85)90032-8 — El producto real del programar es una *teoría* en la mente humana, no reconstruible desde el código.

### Transformers / LLMs frente a la teoría de la computación (lo más relevante para la materia)
- ★ **Delétang, G., et al. (2023).** *Neural networks and the Chomsky hierarchy* (ICLR 2023; arXiv:2207.02098). — 20.910 modelos: transformers y RNNs NO generalizan a tareas no regulares; solo redes con memoria estructurada alcanzan lenguajes libres/sensibles al contexto. https://arxiv.org/abs/2207.02098
- ★ **Merrill, W., & Sabharwal, A. (2023).** The parallelism tradeoff: Limitations of log-precision transformers. *TACL, 11*, 531–545. https://doi.org/10.1162/tacl_a_00562 — Con precisión realista, los transformers viven en **TC⁰**; no reconocen gramáticas libres de contexto arbitrarias si L≠P.
- **Pérez, J., Barceló, P., & Marinković, J. (2021).** Attention is Turing-complete. *JMLR, 22*(75), 1–35. https://jmlr.org/papers/v22/20-302.html — Turing-completos SOLO con precisión infinita (contrapunto idealizado).
- **Merrill, W., & Sabharwal, A. (2024).** *The expressive power of transformers with chain of thought* (ICLR 2024; arXiv:2310.07923). — CoT con pasos polinomiales = clase **P**; lineales = lenguajes sensibles al contexto. https://arxiv.org/abs/2310.07923
- **Hahn, M. (2020).** Theoretical limitations of self-attention… *TACL, 8*, 156–171. https://doi.org/10.1162/tacl_a_00306 — El self-attention de tamaño fijo no modela PARITY ni Dyck-2.
- **Strobl, L., Merrill, W., Weiss, G., Chiang, D., & Angluin, D. (2024).** What formal languages can transformers express? A survey. *TACL, 12*, 543–561. https://doi.org/10.1162/tacl_a_00663 — Referencia "paraguas" del subcampo.
- **Weiss, G., Goldberg, Y., & Yahav, E. (2021).** Thinking like transformers. *ICML (PMLR 139)*, 11080–11090. https://proceedings.mlr.press/v139/weiss21a.html — RASP: el transformer como modelo computacional caracterizable.
- **Xu, Z., Jain, S., & Kankanhalli, M. (2024).** *Hallucination is inevitable…* (arXiv:2401.11817). https://arxiv.org/abs/2401.11817 — La alucinación es una limitación innata (diagonalización sobre la indecidibilidad de la parada). ★ integrada.

---

## Eje D — Economía del empleo y proyecciones del rol futuro

- ★ **Acemoglu, D., & Restrepo, P. (2019).** Automation and new tasks… *JEP, 33*(2), 3–30. https://doi.org/10.1257/jep.33.2.3 — Marco desplazamiento vs. reinstauración: la tecnología recompone tareas.
- **Acemoglu, D., & Restrepo, P. (2018).** The race between man and machine. *AER, 108*(6), 1488–1542. https://doi.org/10.1257/aer.20160696 — Mecanismo autoestabilizador entre automatización y creación de tareas.
- ★ **Autor, D. H. (2015).** Why are there still so many jobs? *JEP, 29*(3), 3–30. https://doi.org/10.1257/jep.29.3.3 — Complementariedad y paradoja de Polanyi: automatizar unas tareas eleva el valor de las humanas.
- **Frey, C. B., & Osborne, M. A. (2017).** The future of employment… *Technological Forecasting and Social Change, 114*, 254–280. https://doi.org/10.1016/j.techfore.2016.08.019 — El clásico "47 % de empleos en riesgo" (contrapunto pesimista; mide ocupaciones, no tareas).
- **Acemoglu, D. (2025).** The simple macroeconomics of AI. *Economic Policy, 40*(121), 13–58. https://doi.org/10.1093/epolic/eiae042 — Estimación escéptica: TFP +0,66 % en 10 años.
- ★ **World Economic Forum (2025).** *The future of jobs report 2025.* https://www.weforum.org/publications/the-future-of-jobs-report-2025/ — A 2030: 170 M empleos creados, 92 M desplazados (**neto +78 M**); ~40 % de las skills cambian; *software developers* entre los 4 roles de mayor crecimiento.
- **Goldman Sachs (2023).** *The potentially large effects of AI on economic growth.* — ~300 M empleos expuestos globalmente; +7 % PIB mundial; históricamente el desplazamiento se compensa con nuevas ocupaciones. https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.pdf
- **OECD (2023).** *Employment Outlook 2023: AI and the labour market.* https://doi.org/10.1787/08785bba-en — "Más que reemplazar empleos, la IA los está cambiando".
- ★ **Bureau of Labor Statistics (2025).** *Software developers… (Occupational Outlook Handbook).* https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm — +15 % "software developers" (2024-2034) vs. −6 % "computer programmers".
- ★ **Brynjolfsson, E., Chandar, B., & Chen, R. (2025).** *Canaries in the coal mine?* Stanford Digital Economy Lab. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ — Caída de empleo del 13-16 % en jóvenes (22-25) de ocupaciones expuestas; estables los experimentados.
- **SignalFire (2025).** *State of Tech Talent Report 2025.* https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025 — New grads = 7 % de las contrataciones en Big Tech (−25 % vs 2023); +27 % en perfiles mid-level.
- ★ **Washizaki, H. (Ed.). (2024).** *SWEBOK Guide v4.0.* IEEE Computer Society. https://www.computer.org/education/bodies-of-knowledge/software-engineering — La ingeniería de software abarca requisitos, arquitectura, validación, seguridad… mucho más que codificar.

---

## Eje E — Visiones de expertos sobre el rol futuro

### Optimistas / disruptivos
- ★ **Amodei, D. (CFR, 2025, 10 de marzo).** "La IA escribirá el 90 % del código en 3-6 meses… pero el programador todavía debe especificar… las decisiones de diseño". https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic
- ★ **Altman, S. (2025).** *The gentle singularity* (blog) y entrevista en Stratechery (Thompson, 2025): "cada ingeniero hará muchísimo más"; "los expertos seguirán siendo mucho mejores que los novatos". https://blog.samaltman.com/the-gentle-singularity
- ★ **Karpathy, A. (2025).** *Software is changing (again)* — "Software 3.0", "programamos en inglés"; acuñó "vibe coding". https://www.youtube.com/watch?v=LCEmiRjPEtQ
- **Huang, J. (NVIDIA, 2024).** "Nadie tiene que programar… todos somos ahora programadores". https://blogs.nvidia.com/blog/world-governments-summit/
- ★ **Dohmke, T. (GitHub, 2025).** "Mil millones de desarrolladores habilitados por miles de millones de agentes de IA". https://github.blog/news-insights/company-news/goodbye-github/

### Cautos / escépticos (el rol humano perdura)
- ★ **Booch, G. (Pragmatic Engineer, 2026).** Sobre Amodei: "es una incomprensión fundamental de lo que es la ingeniería de software"; "tus herramientas cambian, pero tus problemas no". https://newsletter.pragmaticengineer.com/p/the-third-golden-age-of-software
- ★ **Stroustrup, B. (DevClass, 2025).** Riesgo de que los programadores "pierdan la capacidad de detectar problemas por estar acostumbrados a que se los resuelvan". https://devclass.com/2025/05/09/interview-bjarne-stroustrup-on-21st-century-c-ai-risks-and-why-the-language-is-hard-to-replace/
- **Osmani, A. (2024).** *The 70% problem* — la IA hace el 70 %; el 30 % final (depuración, casos límite, mantenibilidad) sigue siendo humano. https://addyo.substack.com/p/the-70-problem-hard-truths-about
- **Fowler, M. (2025).** *LLMs bring new nature of abstraction* — los LLM son un salto comparable a los lenguajes de alto nivel, pero introducen abstracción no determinista. https://martinfowler.com/articles/2025-nature-abstraction.html
- **Beck, K. (2023/2025).** "El 90 % de mis habilidades ahora valen $0… pero el otro 10 % vale 1000×" (el juicio y el diseño). https://newsletter.kentbeck.com/p/90-of-my-skills-are-now-worth-0

---

## Eje F — Calidad, corrección y seguridad del código generado por IA

- **Chen, M., et al. (2021).** *Evaluating large language models trained on code* (arXiv:2107.03374). — Codex: 28,8 % pass@1 en HumanEval (la corrección de un solo intento es modesta). https://arxiv.org/abs/2107.03374
- ★ **Liu, J., Xia, C. S., Wang, Y., & Zhang, L. (2023).** Is your code generated by ChatGPT really correct? *NeurIPS 36*, 21558–21572. https://arxiv.org/abs/2305.01210 — Con tests más rigurosos (EvalPlus), la corrección reportada cae hasta 20-29 puntos.
- ★ **Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2022).** Asleep at the keyboard? *IEEE S&P 2022*, 754–768. https://doi.org/10.1109/SP46214.2022.9833571 — ~40 % de los programas de Copilot en escenarios de seguridad contenían vulnerabilidades.
- ★ **Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023).** Do users write more insecure code with AI assistants? *ACM CCS 2023*, 2785–2799. https://doi.org/10.1145/3576915.3623157 — Con IA se escribe código menos seguro y se confía más (falsa sensación de seguridad).
- **Spracklen, J., et al. (2025).** We have a package for you! *USENIX Security 2025.* https://arxiv.org/abs/2406.10279 — 19,7 % de los paquetes recomendados por LLMs son inexistentes ("slopsquatting", riesgo de cadena de suministro).
- **Qi, Z., Long, F., Achour, S., & Rinard, M. (2015).** An analysis of patch plausibility and correctness… *ISSTA 2015*, 24–36. https://doi.org/10.1145/2771783.2771791 — "Pasa los tests" ≠ "es correcto" (overfitting al test): los tests son un proxy incompleto de la especificación.
- **Hou, X., et al. (2024).** Large language models for software engineering: A systematic literature review. *ACM TOSEM.* https://doi.org/10.1145/3695988 — Revisión de 395 estudios; señala calidad de datos y rigor de evaluación como problemas abiertos.
- **Fan, A., et al. (2023).** Large language models for software engineering: Survey and open problems. *ICSE-FoSE 2023*, 31–53. https://arxiv.org/abs/2310.03533 — Las técnicas híbridas (SE clásica + LLMs) son clave para confiabilidad.
- **DORA / Google Cloud (2024).** *Accelerate State of DevOps Report 2024.* https://dora.dev/research/2024/dora-report/ — +25 % de adopción de IA se asoció con −7,2 % de estabilidad de entrega.
- **GitClear (2025).** *AI copilot code quality (2024 data).* https://www.gitclear.com/ai_assistant_code_quality_2025_research — Sube la duplicación de código (8,3 %→12,3 %) y cae el refactor (≈25 %→<10 %).

---

## Cierre: cómo este material sostiene la tesis

El rol del ingeniero en 10 años no desaparece sino que **asciende en la escalera de abstracción** porque tres cuerpos de evidencia convergen: (1) la **historia** muestra que cada automatización transformó el oficio sin extinguirlo (Eje A); (2) la **evidencia empírica** muestra que la IA acelera la producción pero no garantiza corrección, seguridad ni mantenibilidad (Ejes B y F); y (3) la **teoría de la computación** demuestra límites permanentes —indecidibilidad, intratabilidad y las cotas de los propios transformers (TC⁰, jerarquía de Chomsky)— que reservan al humano la especificación, la validación y el juicio (Eje C). La economía (Eje D) y los propios protagonistas del cambio (Eje E) confirman ese desplazamiento del rol hacia tareas de mayor altitud.
