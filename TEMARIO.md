# Temario completo — *El rol del ingeniero informático en los próximos diez años*

**Materia:** Lenguajes Formales y Teoría de la Computación · UCEMA (3.er año, Ing. Informática)
**Profesor:** Mario Moreno · **Integrantes:** Martín Ezequiel Pulitano y Nicolás Silva
**Subtítulo:** automatización de la base, polarización del oficio y un núcleo humano irreductible

> Guía de estudio con **todos los temas** del paper, el debate y la presentación: ideas clave, datos con fuente y glosario teórico. Pensado para repasar antes de exponer.

---

## 🎯 Tesis central (hay que poder decirla en una frase)

El ingeniero **no será reemplazado por la IA**, pero su rol **se transforma**: deja de centrarse en *escribir código* y pasa a **especificar, diseñar, validar, supervisar y decidir**. El cambio **no es parejo**: la **base** (codificar rutinario) se automatiza y el valor se **concentra arriba** → el oficio se **polariza** (se vacía el medio). El límite es **matemático, no temporal**: hay cosas que **ninguna** máquina podrá hacer, y por eso siempre hace falta un humano que valide y **se haga responsable**.

**Frase de cierre (síntesis propia):**
> *Cuanto más poderosa se vuelve la automatización, más valioso se vuelve el juicio humano que decide qué automatizar, cómo controlarlo y para qué.*

---

## 🗺️ Mapa del argumento (de qué va cada sección)

| # | Sección | Idea en una línea |
|---|---|---|
| I | Introducción | La pregunta y la hipótesis. |
| II | Escalera de abstracción | Cada tecnología nueva subió al ingeniero un escalón; la IA es el más nuevo. |
| III | El presente (2021–2026) | Qué puede y qué **no** puede la IA hoy, con datos. |
| IV | Marco teórico | Límites **demostrados** (Turing, Rice, P vs NP, Chomsky). El corazón de la materia. |
| V | El nuevo rol | El "30 % difícil" pasa a ser el centro del trabajo. |
| VI | Visiones de expertos | Optimistas y cautos coinciden: amplifica al que sabe. |
| VII | Empleo y economía | El empleo se recompone y se polariza. |
| VIII | Conclusión | Confirma la hipótesis: arquitecto, auditor y responsable. |

---

## I. Introducción

- **La pregunta gancho:** *¿La IA va a reemplazar a los programadores?*
- Muchos referentes dicen que **sí** (el CEO de Anthropic, Dario Amodei, llegó a predecir el **90 %** del código escrito por IA).
- **Hipótesis del trabajo:** no reemplazo → **transformación + polarización**.
- Qué es **polarización**: crecen los roles **de arriba** (diseñar/decidir) y se achica la **base** (codificar rutinario); *se vacía el medio*.

## II. La escalera de abstracción

- **Idea:** cada vez que una tecnología automatizó lo tedioso, el ingeniero **no desapareció: subió de nivel**.
- Recorrido: **lenguaje de máquina (0 y 1) → lenguajes de alto nivel → compiladores → frameworks y nube → IA**.
- Su "fin" ya se anunció con el **COBOL**, los **lenguajes de 4.ª generación** y el **"no-code"**. Nunca pasó.
- **Cierre:** *la IA es el escalón más nuevo de una escalera muy larga* — no es la excepción a la historia, es su continuación.

## III. El presente: IA agéntica (2021–2026)

**Lo que mejoró (impresionante):**
- **SWE-bench Verified** (test estándar de problemas reales): pasó de **~14 % (inicios 2024) a ~95 % (mediados 2026)** → *de 1 de cada 7 a más de 9 de cada 10*. El benchmark **se saturó** ("ya no mide capacidades de frontera").
- **Microsoft:** la IA escribe el **20–30 %** del código (Nadella). **Google:** *más de una cuarta parte* (Pichai).

**El giro — no es mágica (el contexto lo cambia todo):**
- **Copilot, tarea acotada:** **+55,8 %** de velocidad (Peng et al., 2023).
- **METR, expertos en repos propios maduros:** **−19 %** (más **lentos**)… y **creían** que iban más rápido (2025).
- Lección: la IA **amplifica al que sabe**, pero **estorba** en el trabajo experto.

**Los problemas serios:**
- **"Problema del 70 %"** (Osmani): hace rápido el 70 % fácil; el **30 % difícil** (detalles, casos raros, seguridad) necesita a alguien que **sepa**.
- **Seguridad:** ~**40 %** del código de IA trae vulnerabilidades conocidas (Pearce et al., 2022); ~45 % con fallas (Veracode, 2025).
- **Slopsquatting:** ~**1 de cada 5** paquetes que recomienda **no existe** (Spracklen et al., 2025) → puerta para malware.

## IV. Marco teórico: los límites computacionales ⭐ (lo más de la materia)

> **Idea central:** no es que la IA "todavía no pueda" — hay **límites matemáticos demostrados** que dicen que **NUNCA** podrá. Probados **antes** de que existiera la primera computadora.

**① No se puede verificar todo — Turing y Rice**
- **Problema de la parada (Turing, 1936):** no existe ni puede existir un algoritmo que decida, para **todo** programa, si **termina**.
- **Teorema de Rice (1953):** lo generaliza → **ninguna** propiedad no trivial del comportamiento de un programa es decidible automáticamente (incluido *"¿cumple su especificación?"*).
- **Consecuencia:** la IA escribe el código pero **no puede certificarlo** → siempre hace falta un **humano que valide y firme**.

**② Hay problemas imposibles de resolver rápido — P vs NP**
- **P** = se resuelve rápido; **NP** = la solución se **verifica** rápido pero (se cree) no se **encuentra** rápido. Nadie probó que sean iguales… ni distintos (problema del milenio).
- Muchos problemas de ingeniería no tienen solución rápida y perfecta → hay que **decidir qué sacrificar** (tiempo, optimalidad, recursos): **criterio humano**, no cálculo.

**③ Traducir lo ambiguo a lo exacto — jerarquía de Chomsky**
- La **jerarquía de Chomsky** ordena los lenguajes por su poder expresivo (regulares ⊂ libres de contexto ⊂ … ⊂ recursivamente enumerables / Turing).
- Los **transformers** ≈ clase **TC⁰**: por su arquitectura no reconocen gramáticas libres de contexto arbitrarias → **por debajo** de una computadora común. *Más datos no lo arreglan: es estructural.*
- El lenguaje humano es **ambiguo**; el de la máquina, **exacto**. El ingeniero es el **traductor** entre los dos mundos.

**Dato que cierra todo:**
- **Alucinación inevitable (Xu et al., 2024):** está demostrado que un LLM producirá errores que **no detecta por sí mismo** → **no puede autoverificarse**.

**Lo de fondo (clásicos):**
- **Brooks — "No Silver Bullet" (1986):** la IA reduce la complejidad **accidental** (código repetitivo); la **esencial** —decidir **qué** construir— es humana.
- **Naur — "Programming as Theory Building" (1985):** programar es **construir una teoría** del sistema en la mente del equipo; el código es solo su **sombra/reflejo**. Quien entiende el *porqué* es irreemplazable.

## V. El nuevo rol del ingeniero

- Menos **escribir código**; más **especificar, diseñar, validar, supervisar y decidir**.
- El **"30 % difícil"** de la Sección III se convierte en el **centro** del trabajo.
- Perfiles que crecen: **arquitecto** (diseña), **auditor** (valida) y **responsable** (firma y rinde cuentas).

## VI. Visiones de expertos (optimistas vs. cautos)

- **Optimistas:** Amodei (90 % del código), Altman (*la IA amplifica al que sabe usarla*).
- **Cautos / críticos:** voces que advierten sobre el colapso del empleo junior y la deuda técnica (código que nadie entiende).
- **Punto común:** la IA **potencia al ingeniero que sabe usarla, no lo reemplaza**.

## VII. Empleo y economía: el oficio se recompone

- **BLS (proyección 2024–2034):** crece **"desarrollador" (+15 %)**, cae **"programador" puro (−6 %)** → *no muere la profesión, muere la tarea*.
- **Empleo joven (Stanford, 2025):** cae **~20 %** en 22–25 años en ocupaciones expuestas; desempleo de recién recibidos de Computación ~**6,1 %** (Fed NY). En 2025, ~**142 mil** despidos tecnológicos (causa **discutible**: tasas + sobrecontratación pandémica + IA).
- **Paradoja de Jevons:** cuando algo se abarata, se **usa más**. Los **cajeros automáticos** no eliminaron bancarios → abrieron **más sucursales** (Bessen).
- **Contrapeso (Acemoglu y Restrepo, 2019):** si la automatización **no crea tarea nueva**, puede **hundir salarios** → la transición es **dura y desigual**.
- **WEF 2030:** **+170 M** empleos creados, **−92 M** desplazados → **saldo +78 M**. *No es "cero gente": es otra gente, en otra tarea.*
- **Prima salarial:** los puestos que piden IA pagan **primas muy por encima del promedio** (Stanford HAI, 2026) → *dónde* esforzarse importa.

## VIII. Limitaciones del trabajo y conclusión

- Es una **proyección a 10 años**: una **estimación fundada**, no una bola de cristal. Lo único que **no caduca** con la próxima versión del modelo es el **teorema**.
- **Conclusión:** el ingeniero **no desaparece** → se transforma en **arquitecto, auditor y responsable**. Lo respalda la **historia**, lo matiza la **evidencia** y lo demuestra la **teoría**.
- **Cierre del círculo:** *cuanto más poderosa la automatización, más vale el juicio humano que decide qué automatizar, cómo controlarlo y para qué.*

---

## 📊 Tabla rápida de cifras (para no equivocarse en vivo)

| Dato | Valor | Fuente |
|---|---|---|
| SWE-bench (inicios 2024 → mediados 2026) | ~14 % → ~95 % (1/7 → 9/10) | SWE-bench Verified |
| Código por IA en Microsoft / Google | 20–30 % / >25 % | Nadella; Pichai |
| Predicción de Amodei | 90 % del código | Anthropic, 2025 |
| Productividad — tarea acotada | **+55,8 %** | Peng et al., 2023 |
| Productividad — expertos, repos maduros | **−19 %** | METR, 2025 |
| Problema del 70 % | 70 % fácil / 30 % difícil humano | Osmani |
| Código de IA con vulnerabilidades | ~40 % | Pearce et al., 2022 |
| Paquetes recomendados inexistentes | ~20 % (1 de 5) | Spracklen et al., 2025 |
| Empleo: desarrollador / programador (2024–34) | +15 % / −6 % | BLS |
| Empleo joven (22–25, expuestos) | ~−20 % | Stanford, 2025 |
| Despidos tecnológicos 2025 | ~142 mil | (causa discutible) |
| WEF 2030 (creados / desplazados / neto) | +170 M / −92 M / **+78 M** | WEF, 2025 |

---

## 📚 Glosario teórico (términos que el profe puede preguntar)

- **Indecidibilidad:** existen problemas que **ningún** algoritmo puede resolver para *todas* las entradas.
- **Problema de la parada (halting, Turing 1936):** decidir si un programa arbitrario **termina**; es indecidible.
- **Teorema de Rice (1953):** **toda** propiedad no trivial del comportamiento de un programa es indecidible. Generaliza el de la parada.
- **P vs NP:** ¿todo lo que se **verifica** rápido se puede **resolver** rápido? Abierto. La intuición (P≠NP): encontrar puede ser mucho más caro que verificar.
- **Jerarquía de Chomsky:** clasificación de lenguajes/gramáticas por poder: **regulares ⊂ libres de contexto ⊂ sensibles al contexto ⊂ recursivamente enumerables**.
- **TC⁰:** clase de circuitos muy limitada donde "caen" los transformers a precisión realista → no deciden ciertos lenguajes simples (ej.: paréntesis balanceados arbitrarios).
- **Complejidad esencial vs. accidental (Brooks):** *esencial* = la dificultad inherente de **decidir qué** construir (no se automatiza); *accidental* = la del **cómo** (herramientas la reducen).
- **Theory building (Naur):** el verdadero producto de programar es una **teoría** del sistema en la mente del equipo, no el código.
- **Paradoja de Jevons:** abaratar un recurso **aumenta** su consumo total.
- **Polarización del empleo:** crecen los extremos (alta y baja calificación) y **se vacía el medio**.

---

## 🎤 Para la exposición (los dos formatos disponibles)

- **`debate_en_vivo.html`** — debate (🔴 Martín = extinción · 🟢 Nico = cambio), con memes y cameo de la IA, **dividido en 4 bloques de ~5 min** y cronómetro por bloque.
- **`presentacion_4bloques.html`** — versión expositiva clásica en 4 bloques (🔵 A: 1 y 3 · 🟢 B: 2 y 4), con las 6 figuras del paper.
- **`Paper_Rol_del_ingeniero_informatico_en_10_anios.pdf`** — el paper final para entregar.
