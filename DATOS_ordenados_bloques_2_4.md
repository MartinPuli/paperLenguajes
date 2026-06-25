# Todos los datos, en orden — Bloques 2 y 4

> Sin slides, sin guion: los datos de cada bloque, ordenados como conviene decirlos. Vos los decís con tus palabras.
> **negrita** = el dato/cifra · *(extra)* = no estaba en el paper · ⚠ = caveat (por si repreguntan) · entre paréntesis = fuente y año.

---

# 🔵 BLOQUE 2 — El presente de la IA (2021-2026)
**Hilo:** la capacidad sube → la adopción explota → pero la productividad real es mixta → la calidad/seguridad falla → el cuello de botella se mueve a verificar.

### — Capacidad —
1. **Punto de partida: 1,96 %** — en 2023 el mejor modelo resolvía menos del 2 % de los bugs reales de GitHub (SWE-bench original, Jimenez et al., 2024). *(extra)* ⚠ set original, no comparable 1:1 con Verified.
2. **SWE-bench Verified: ~14 % (inicios 2024) → ~89 % (2026)** — “de uno de cada siete a casi nueve de cada diez” (Anthropic, 2026).
3. **Trayectoria:** Devin 13,9 % (mar-24) → Sonnet 3.5 49 % (oct-24) → o3 71,7 % (dic-24) → Sonnet 3.7 63,7 % (feb-25) → Opus 4 / Sonnet 4 72,5/72,7 % (may-25) → GPT-5 74,9 % (ago-25) → Sonnet 4.5 77,2 % (sep-25). *(extra)* ⚠ los “high-compute” no son comparables.
4. **El benchmark se saturó** — OpenAI: “SWE-bench Verified ya no mide la frontera”. *(extra)*
5. **Junio 2026: Fable 5 y Mythos 5**, más capaces, pero EE. UU. **suspendió su acceso a los pocos días** (Anthropic, 2026). ⚠ cronología, no cifra de benchmark.

### — Adopción —
6. **GitHub Copilot: 20 millones de usuarios** (2025) — adopción más rápida de la historia. ⚠ acumulados.
7. **>1,8 M suscriptores pagos, >77.000 empresas (+180 % interanual)** (GitHub/SEC, 2024). *(extra)*
8. **Copilot escribía el 46 % del código** en los archivos donde está activo (Dohmke, 2023). *(extra)* ⚠ métrica de aceptación.
9. **Microsoft: 20-30 % de su código lo escribe la IA** (Nadella, vía Zeff, 2025).
10. **Google: de “más de un cuarto” (2024) al 75 % del código nuevo** generado por IA y **“aprobado por ingenieros”** (Pichai, 2026). ← guardá “aprobado por ingenieros”.
11. **84 % de los devs usa o planea usar IA** (Stack Overflow, 2025). *(extra)*

### — Productividad real (el contraste clave) —
12. **Peng/Copilot: +55,8 % más rápido** en tarea acotada (1 h 11 vs 2 h 41; IC 21-89 %; n=95; servidor HTTP) (2023). *(detalles extra)*
13. **METR: expertos −19 % MÁS LENTOS** en sus propios repos maduros con IA (n=16; 246 tareas; Cursor) (2025). *(detalles extra)*
14. **Brecha percepción/realidad: creían +20 %, economistas preveían −39 %, ML −38 %… real −19 %.** “Todos se equivocaron en el signo.” *(extra)*
15. **MIT/Cui: +26 % de tareas completadas** (n=4.867); **beneficia a los juniors, no a los seniors** (2025). *(extra)*
16. **McKinsey: hasta 2× más rápido** (documentar −45/50 %, escribir −35/45 %); **<10 % en tareas complejas** (2023). *(extra)* ⚠ consultora.
17. **DORA: +25 % de adopción de IA → −7,2 % de estabilidad de entrega**, dos años seguidos (Google, 2024). *(extra)* ⚠ correlación.
> ⚠ Peng (+55,8 %) y METR (−19 %) NO son comparables: tarea fácil vs repo maduro; vendor vs independiente. Es “el contexto lo cambia todo”.

### — Calidad y seguridad —
18. **Osmani, “problema del 70 %”:** la IA da el 70 % rápido; el **30 % final** (casos límite, depuración, mantenibilidad) son rendimientos decrecientes (2024).
19. **Osmani: “la calidad del software nunca estuvo limitada por la velocidad de tipeo.”** *(extra)*
20. **Osmani, paradoja del conocimiento:** ayuda más al senior; el junior acepta código frágil (“house of cards”). *(extra)*
21. **Stanford/Perry: con IA se escribe código menos seguro y se confía MÁS** (falsa seguridad; n=47, Codex) (2023). *(detalle extra)*
22. **Pearce/MITRE: ~40 % de las sugerencias con vulnerabilidades** (89 escenarios, 1.689 programas) (2022). *(detalle extra)*
23. **Veracode: 45 % del código con vulnerabilidad; Java 72 %, XSS 86 %; los modelos más nuevos NO fueron más seguros** (100+ LLMs) (2025). *(extra)*
24. **Liu: la corrección cae 19-29 puntos al endurecer los tests ×80** (26 LLMs) (2023) — los benchmarks sobreestiman. *(detalle extra)*
25. **Spracklen / slopsquatting: 19,7 % de los paquetes recomendados NO existen** (205.474 nombres falsos; ~5,2 % comerciales vs ~21,7 % open-source); los atacantes los registran con malware (2025). *(dato extra)*
26. **GitClear: subió el copy-paste (8,3→12,3 %), cayó el refactor; 2024, primer año con más copy-paste que refactorización**; churn 3,1→5,7 % → deuda técnica (2024). *(extra)* ⚠ correlación.
27. **Stack Overflow: solo ~1/3 confía en la exactitud; 45 % dice que depurar código de IA lleva más tiempo** (2025). *(extra)*
28. **Anthropic/Shen & Tamkin: los que aprenden con IA sacan −17 puntos en un examen sin IA** (n=52) (2026). *(extra)*

### — Cierre del bloque —
29. **Qi (2015): la mayoría del código que “pasa los tests” es incorrecto** (overfitting al test). *(extra)* ← puente a la teoría (Rice/Turing).
30. **“La IA acelera la producción, pero no garantiza la corrección: traslada el cuello de botella de escribir a verificar.”** → ¿por qué no se puede automatizar la verificación? Matemática.

---

# 🟢 BLOQUE 4 — Nuevo rol, empleo y conclusión
**Hilo:** cómo queda el rol → empleo (macro positivo, base junior dura) → expertos (optimistas vs cautos) → polarización → cierre.

### — El nuevo rol —
1. **El desplazamiento:** de escribir código a **especificar, diseñar, validar y decidir.**
2. **Mapeo a las barreras:** validar ↔ Rice/Turing; decidir ↔ P vs. NP; traducir intención → spec ↔ Chomsky.
3. **Tres perfiles que crecen: arquitecto (el qué), auditor (valida la IA), responsable (firma y rinde cuentas).**
4. **Brooks (1987): “lo más difícil de construir software es decidir con precisión qué construir.”** La IA ataca lo accidental; lo esencial es humano.
5. **Naur (1985): el producto real de programar es una “teoría” del problema** que vive en el equipo; el código no la captura.
6. **SWEBOK: la ingeniería de software tiene 18 áreas; codificar es solo una** (2024). *(“18” extra)*
7. **La IA no se autoverifica → necesita un verificador humano** (alucinación inevitable, Xu, 2024).

### — Empleo y economía —
8. **WEF 2030: −92 M desplazados / +170 M creados / neto +78 M; 22 % de churn; ~40 % de las skills cambian** (2025).
9. **BLS 2024-2034: “desarrollador” +15 % / “programador puro” −6 %** — se automatiza la tarea, no la profesión.
10. **Jevons + cajeros (Bessen, 2015): de 21 a 13 cajeros por sucursal, pero +43 % sucursales → más empleo por 20 años.** *(cifras extra)* ⚠ se revirtió tras 2010 (banca móvil).
11. **Acemoglu-Restrepo (2019) / Autor (2015): la tecnología recompone tareas, no elimina empleos; automatizar unas eleva el valor de las humanas.**
12. **Stanford/Brynjolfsson (2025): empleo joven (22-25) −13 a −16 % en ocupaciones expuestas; experimentados estables** (devs jóvenes ~−20 % desde fin-2022). ⚠ causalidad disputada.
13. **SignalFire: recién recibidos −65 % big tech / −76 % startups (vs 2019); +27 % mid-level.** ⚠ ellos lo atribuyen primero al fin del crédito barato.
14. **Indeed: puestos junior −34 % vs senior −19 %; ofertas de software −36 % vs 2020; piden 5+ años (37→42 %).**
15. **Salesforce/Benioff: +30 % de productividad con IA → en 2025 “no contratamos ingenieros”** (2024). ⚠ CEO interesado.
16. **La paradoja honesta (Brynjolfsson, 2023): la IA ayuda MÁS al novato (+34 %)… pero el mercado se cierra justo para el novato**, porque le come las tareas con las que aprendía. *(extra)*
17. **Dohmke (GitHub): “mil millones de desarrolladores habilitados por miles de millones de agentes”** (2025). ⚠ proyección de CEO.

### — Las dos miradas (expertos) —
18. **Amodei: “90 % del código en 3-6 meses… pero el programador todavía tiene que especificar las decisiones de diseño”** (2025). ← el optimista máximo concede la tesis.
19. **Altman: “los expertos seguirán siendo mucho mejores que los novatos, siempre que adopten las herramientas”** + “quizá necesitemos menos ingenieros” (2025). ← polarización dicha por OpenAI.
20. **Karpathy: “Software 3.0”, “programamos en inglés”, vibe coding** (2025). ⚠ “the hottest new programming language is English” es un tweet de 2023, no del talk.
21. **Huang (NVIDIA): “nadie tiene que programar… todos somos programadores”** (2024). *(extra)*
22. **Nadella: “la paradoja de Jevons ataca de nuevo: cuanto más eficiente la IA, más se dispara su uso”** (2025). *(extra)*
23. **Booch: “es un disparate / profundamente equivocado”; “tus herramientas están cambiando, pero tus problemas no”** (2026). *(el “utter bullshit” es extra)*
24. **Stroustrup: la IA genera más bugs y agujeros de seguridad, código difícil de validar, justo cuando los seniors que validan se jubilan** (2026).
25. **Kent Beck: “el 90 % de mis habilidades ahora vale $0; el otro 10 % —criterio, diseño— vale 1000×”** (2023). *(extra)* ← la mejor frase de polarización.
26. **Fowler: salto tan grande como assembler→alto nivel, pero es la primera abstracción NO determinista** (2025). *(extra)*
27. **Welsh: “el software será entrenado, no programado”** (2023) — la postura a refutar.
28. **Punto en común: hasta los más optimistas reservan especificar, decidir y juzgar para el humano.**

### — Síntesis y cierre —
29. **Tesis: “la IA reducirá y polarizará la profesión; el que solo codifica queda expuesto, el que asciende en abstracción no.”**
30. **Se vacía el medio: menos ingenieros “del montón”, más ingenieros PRO; los puestos con IA pagan prima** (Beck: 90 % $0 / 10 % 1000×).
31. **Por qué un humano y no otra IA: porque alguien tiene que RESPONDER** —asumir responsabilidad, decidir fines—; categoría jurídico-moral, no un cómputo.
32. **Paradoja esperanzadora: cuanto más poderosa la automatización, más vale el juicio humano** que decide qué automatizar, cómo validar y para qué.
33. **Honestidad: hay perdedores concretos; la puerta de entrada junior se estrecha** (te blinda contra “esto es optimismo ingenuo”).
34. ⚠ **Causalidad:** el cierre junior puede ser IA o el fin del crédito barato post-2021 → “tendencia convergente, no prueba cerrada”.
35. **Cierre: “la IA no anuncia el fin del ingeniero: redefine quién lo es.”**

---

## ⚠️ Tres avisos de honestidad (para toda la charla)
- Casi todos los % de “código por IA” (Google, Microsoft) son **auto-reportados por empresas** → decí “según…”.
- **No** uses cita de **Tom DeMarco** (no está en las fuentes) ni inventes una **“prima salarial de X %”** (no la tenemos medida).
- *“O adoptás la IA o te vas de esta carrera”* es de un **dev anónimo** de un estudio de GitHub, no de Dohmke.
