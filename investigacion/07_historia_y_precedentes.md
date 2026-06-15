# 07 — Historia de la profesión y precedentes de "el fin del programador"

---

## A. La crisis del software y el nacimiento de la disciplina

- **Conferencia NATO de Ingeniería de Software** — Garmisch, Alemania, **7–11 de octubre de 1968**. Presidente: Friedrich L. ("Fritz") Bauer. Acuñó (popularizó) el término "ingeniería de software" como título "deliberadamente provocador" y la expresión "crisis del software".
  - Informe: **Naur, P., & Randell, B. (Eds.). (1969).** *Software engineering: Report on a conference sponsored by the NATO Science Committee…* NATO. https://archive.org/details/softwareengineer0000unse
  - Nota: el término ya aparecía en 1965 (*Computers and Automation*) y 1966 (carta de A. Oettinger a la ACM); la conferencia lo popularizó. Atribución a veces disputada con Margaret Hamilton (Apollo).
- **Dijkstra, E. W. (1972).** The humble programmer. *CACM, 15*(10), 859–866. https://doi.org/10.1145/355604.361591 — *"…as long as there were no machines, programming was no problem at all; … now we have gigantic computers, programming has become an equally gigantic problem."* (Turing Award lecture, EWD340.)

## B. La escalera de abstracción (cada peldaño elevó al ingeniero, no lo eliminó)

| Año | Hito | Abstracción a… |
|---|---|---|
| ~1947-49 | Lenguaje ensamblador / ensambladores (Kathleen Booth; EDSAC Initial Orders) | mnemónicos sobre binario |
| 1952 | Compilador A-0 (Grace Hopper) | traducción automática |
| 1957 | FORTRAN (John Backus, IBM) | notación algebraica de alto nivel |
| 1959-60 | COBOL (CODASYL; influencia de FLOW-MATIC/Hopper) | lógica de negocios "legible en inglés" |
| 1968 | "Go To… Harmful" (Dijkstra, CACM 11(3), 147-148) | control de flujo estructurado |
| 1975/1983 | IDEs (Maestro I / Turbo Pascal) | herramientas integradas |
| 1991 | Linux (Torvalds) | desarrollo colaborativo abierto |
| 2005 | Git (Torvalds) | control de versiones distribuido |
| 2006 | AWS S3/EC2 | infraestructura como servicio |
| 2008 | Stack Overflow (Atwood, Spolsky) | conocimiento comunitario |
| 2009 | DevOps / DevOpsDays (Patrick Debois, Gante) | automatización dev+ops |
| 2021-22 | GitHub Copilot (con OpenAI Codex) | codificación a nivel de intención/lenguaje natural |

- Fuente académica del patrón: **Ensmenger, N. (2010).** *The computer boys take over.* MIT Press. — la promesa de "automatizar la programación" se repite desde los 50; el programador siempre siguió siendo esencial.
- **Parnas, D. L. (1985).** "automatic programming has always been a euphemism for programming in a higher-level language than was then available." (*American Scientist*, nov. 1985.)

## C. Precedentes de "el fin del programador" que no se cumplieron

- **FLOW-MATIC / COBOL (1955-60):** lenguajes "legibles en inglés" para que personas de negocio programaran. Grace Hopper: *"I was charged with the job of making it easy for businessmen to use our computers."* Resultado: creó una nueva profesión de programadores COBOL.
- **4GL / CASE (1980s):** **Martin, J. (1981).** *Application Development Without Programmers.* Prentice-Hall. Preface: *"…most computers in the future must be put to work at least in part without programmers."* No ocurrió. (Comentario moderno: Simon Willison, 2025 https://simonwillison.net/2025/Jul/14/application-development-without-programmers/)
- **No-code / low-code (2010s):** Gartner proyectó "citizen developers" 4:1 sobre profesionales; en la práctica, augmentación, no reemplazo. Contrapuntos (Stack Overflow Blog 2022; Built In 2023): *"there will always be a need for engineers who can fully manipulate software."*
- **"The End of Programming" (Welsh, CACM 2023):** la última profecía. https://doi.org/10.1145/3570220
- **Réplicas:** Tim O'Reilly (2025) — "There were more programmers, not fewer." https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it/ ; Joe McKendrick (ZDNet) cataloga CASE, 4GL, OOP, SOA, microservicios, cloud, PaaS, serverless, low/no-code como "fines de la programación" previos que fallaron; "The End Is Not Clear" (CACM jul. 2023).
- Predicción moderna equivalente: **Jensen Huang (NVIDIA, 2024)** "nadie tiene que programar". (Ver `05_visiones_de_expertos.md`.)

## D. Lectura para el paper

Cada abstracción automatizó la parte rutinaria y elevó al ingeniero a un nivel conceptual superior; la demanda total de software (y de quienes lo diseñan) creció (paradoja de Jevons; ver `06_economia_y_mercado_laboral.md`). La IA generativa es el peldaño más alto de una escalera muy larga, y el anuncio de la desaparición del programador es una constante histórica incumplida.
