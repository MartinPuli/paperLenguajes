# 08 — Qué es la ingeniería de software (epistemología) y surveys de LLM4SE

Por qué la especificación, el diseño y la comprensión son irreduciblemente humanos. Citas verificadas contra ACM DL, IEEE Xplore, ScienceDirect, MIT Press.

---

## A. La naturaleza de la ingeniería de software

- **Naur, P. (1985).** Programming as theory building. *Microprocessing and Microprogramming, 15*(5), 253–261. https://doi.org/10.1016/0165-6074(85)90032-8
  - El producto real del programar es una **teoría** del problema y su solución que reside en la mente del equipo y **no puede reconstruirse** desde el código y la documentación. Soporte clásico más fuerte de la tesis: la IA genera código, no la teoría.
- **Brooks, F. P. (1987).** No silver bullet: Essence and accidents… *Computer, 20*(4), 10–19. https://doi.org/10.1109/MC.1987.1663532 — complejidad **esencial** vs. **accidental**; *"The hardest single part of building a software system is deciding precisely what to build."* (También *The Mythical Man-Month*, 1975/1995, Addison-Wesley.)
- **Parnas, D. L. (1972).** On the criteria to be used in decomposing systems into modules. *CACM, 15*(12), 1053–1058. https://doi.org/10.1145/361598.361623 — **information hiding**: encapsular las decisiones de diseño que probablemente cambien (juicio humano sobre qué es volátil).
- **Parnas, D. L. (1985).** Software aspects of strategic defense systems. *CACM, 28*(12), 1326–1335. https://doi.org/10.1145/214956.214961 — la "programación automática" no elimina la carga humana de especificar y diseñar correctamente; los sistemas grandes no se hacen confiables por IA.
- **Dijkstra, E. W. (1972, 1968).** Ver `07_historia_y_precedentes.md` (la programación como gestión del límite cognitivo humano).
- **Lehman, M. M. (1980).** Programs, life cycles, and laws of software evolution. *Proceedings of the IEEE, 68*(9), 1060–1076. https://doi.org/10.1109/PROC.1980.11805 — el software del mundo real (tipo E) debe **evolucionar continuamente** o se vuelve obsoleto; decidir cómo evolucionar es juicio humano.
- **Ensmenger, N. (2010).** *The computer boys take over.* MIT Press. — patrón histórico de 60 años: el "reemplazo del programador" se anuncia con regularidad ritual.
- **Washizaki, H. (Ed.). (2024).** *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide), Version 4.0.* IEEE Computer Society (15-oct-2024; 18 áreas de conocimiento, incluye arquitectura, operaciones y seguridad). https://www.computer.org/education/bodies-of-knowledge/software-engineering — definición autoritativa de que codificar es **una porción** de la disciplina (requisitos, diseño, arquitectura, pruebas, mantenimiento, calidad, práctica profesional, economía).

## B. Surveys académicos de LLM para ingeniería de software

- **Hou, X., et al. (2024).** Large language models for software engineering: A systematic literature review. *ACM TOSEM, 33*(8), Art. 220. https://doi.org/10.1145/3695988 (preprint arXiv:2308.10620) — 395 papers (2017-2024); calidad de datos y rigor de evaluación como problemas abiertos.
- **Fan, A., et al. (2023).** Large language models for software engineering: Survey and open problems. *ICSE-FoSE 2023*, 31–53. https://arxiv.org/abs/2310.03533 — las **técnicas híbridas** (SE clásica + LLMs) son clave para confiabilidad; abre retos de alucinación, evaluación y fiabilidad.

## C. Datos bibliográficos canónicos (verificados) de los resultados teóricos clave

- **Rice, H. G. (1953).** *Trans. AMS, 74*(2), 358–366. https://doi.org/10.1090/S0002-9947-1953-0053041-6
- **Turing, A. M. (1936).** *Proc. London Math. Soc., s2-42*(1), 230–265. https://doi.org/10.1112/plms/s2-42.1.230 (corrección 1938, s2-43(6), 544–546). Nota: volumen fechado 1937; se cita 1936 por convención.

> Conclusión transversal: la IA reduce la complejidad **accidental** (escribir y traducir código), pero la complejidad **esencial** —decidir qué construir, modelar el dominio, mantener la teoría del sistema y validarlo— permanece humana. Es el sustento epistemológico de que el rol asciende en la escalera de abstracción en vez de desaparecer.
