# Munición de datos — Bloques 1 y 3 (para el compañero)

> Datos verificados del paper + dossier. *(extra)* = no estaba en el paper, suma profundidad. Cada uno con cómo decirlo en voz alta.

---

# 🎙️ BLOQUE 1 — La escalera de abstracción (historia)

**Tesis:** la historia del software es subir escalones de abstracción; cada salto “mató” una tarea pero **elevó** al ingeniero; el “fin de la programación” se anunció muchas veces y **nunca pasó**.

## Los hitos (eje para una slide)
Ensamblador (~1947) → compilador A-0 / **Grace Hopper, 1952** *(extra)* → **FORTRAN / Backus, IBM, 1957** → COBOL (1959) → **crisis del software / OTAN Garmisch, oct-1968** → Dijkstra (programación estructurada, 1968; Turing 1972) → IDEs (1975-83) → **Git, 2005** → **AWS / la nube, 2006** → **Stack Overflow, 2008** → **DevOps, 2009** → **GitHub Copilot, 2021** → IA generativa (2023→).

## Los datos imperdibles
1. **💥 Parnas (1985, extra) — la frase que desarma todo:** *“la programación automática siempre ha sido un eufemismo para programar en un lenguaje de más alto nivel que el disponible en ese momento.”*
   > “Cada vez que ‘automatizamos la programación’, en realidad subimos un escalón de abstracción y seguimos programando.”
2. **Crisis del software + Dijkstra (paper):** en Garmisch, oct-1968, se acuñó ‘crisis del software’ y nació el término ‘ingeniería de software’. Dijkstra (Turing, 1972): *“mientras no había máquinas, programar no era ningún problema; ahora que tenemos computadoras gigantescas, programar se ha vuelto un problema igualmente gigantesco.”* → **más complejidad = más ingeniería, no menos.**
   > *Caveat honesto: ‘crisis del software’ ya circulaba en 1965-66; Garmisch lo **popularizó**, no lo inventó.*
3. **La cadena de profecías incumplidas (extra, columna vertebral):** Hopper/COBOL (1955-60) → **James Martin, “Application Development *Without Programmers*”, 1981** → 4GL/CASE → **Gartner: ‘citizen developers’ 4:1** (2010s) → Welsh “The End of Programming” (2023) → **Huang (NVIDIA): “nadie tiene que programar” (2024)**. Respaldo: **Ensmenger (2010)**: el anuncio se repite con “regularidad **ritual**”.
   > “Cada década, una voz famosa anuncia el fin del programador. Cada vez hubo **más** programadores.”
4. **🎯 Remate — O’Reilly (2025, extra):** cada ola de abstracción produjo *“más programadores, no menos.”*
5. **Cajeros automáticos (paper):** al abaratar la sucursal, los bancos abrieron más y hubo más cajeros **por 20 años** (la tarea viró a atención al cliente). *Caveat: se revirtió tras 2010 con la banca móvil — usalo con honestidad.*

---

# 🎙️ BLOQUE 3 — Los límites matemáticos (teoría)

**Tesis:** no es que la IA “todavía no sea bastante potente”; hay barreras **demostradas y permanentes** que ningún proceso computable sortea. Cada una reserva una tarea humana.

## Las barreras (tabla para una slide)
| Barrera | Fuente | Qué prohíbe | Tarea humana |
|---|---|---|---|
| **Halting problem** | Turing, 1936 | decidir si un programa cualquiera termina | (base) |
| **Teorema de Rice** | Rice, 1953 | verificar *automáticamente* cualquier propiedad de comportamiento | validar / juicio |
| **P vs. NP** | Cook 1971; Karp 1972 | resolver *eficientemente* (no imposible: lento) | elegir heurísticas |
| **Chomsky + TC⁰** | Chomsky 1956; Delétang 2023; Merrill-Sabharwal 2023 | que un transformer reconozca lenguajes > su clase | traducir intención → spec |
| **Alucinación inevitable** | Xu 2024; Guo-Li 2026 | que un LLM autoverifique su corrección | ser el verificador |
| **Esencial vs accidental** | Brooks 1987; Naur 1985 | *(no es teorema)* decidir qué construir | especificar |

## Cómo explicarlo y los errores a NO cometer
1. **Halting + diagonalización (Turing 1936):** “Imaginá un detector universal de cuelgues. Turing probó por **diagonalización** que no puede existir —como la paradoja del mentiroso, ‘esta frase es falsa’.”
   - ❌ NO digas “falta una computadora más rápida”: es imposible **en principio**, para cualquier máquina.
2. **Rice (1953):** “Cualquier pregunta sobre lo que un programa **hace** —‘¿cumple la especificación?’, ‘¿tiene este bug?’— no tiene algoritmo general.”
   - ❌ NO confundir **sintaxis** (‘¿tiene 100 líneas?’, decidible) con **semántica** (indecidible). Los verificadores existen, pero **restringen el problema** o renuncian a la completitud.
3. **⚠️ P vs. NP — EL error más importante:** **intratable ≠ indecidible.** Un problema NP-difícil **sí tiene solución**, solo que (si P≠NP) **lenta** en el peor caso. Indecidible = no hay **ningún** algoritmo. *Y P≠NP es **conjetura**, no demostrado —por eso vale el premio de **USD 1.000.000** de Clay (extra).*
4. **Chomsky + transformers (la munición fuerte):** la sintaxis de los lenguajes de programación es libre de contexto; el lenguaje natural es ambiguo y **no es formal** → el ingeniero **traduce** intención en especificación. *Delétang probó con **20.910 modelos** que más datos/entrenamiento **NUNCA** rompieron el techo teórico (extra).*
   - ❌ Si alguien dice “pero los transformers son Turing-completos”: sí, **con precisión infinita** (idealizado); con precisión real (logarítmica) viven en **TC⁰**. No es contradicción, son **supuestos distintos**.
5. **Alucinación inevitable (Xu 2024):** misma barrera de Turing apuntada contra la IA: no puede autoverificarse → necesita un **verificador externo, el ingeniero**.
   - Matiz honesto: “inevitable” ≠ “frecuente”: se puede reducir hasta ser despreciable, **no eliminar**.
6. **Brooks/Naur:** “lo más difícil es **decidir qué construir**” (Brooks); el producto real es una **teoría** del problema en la mente del equipo (Naur). *No son teoremas: son argumentos conceptuales que explican por qué, aun donde la teoría no prohíbe nada, la tarea sigue siendo humana.*

## Las 3 ideas que el público se tiene que llevar
1. **Son límites, no etapas** — no caducan con el próximo *release*.
2. **No confundir indecidible ≠ intratable** (el error que más desarma la exposición).
3. **Cada límite reserva una tarea humana** → el “30 % difícil” se vuelve el centro de la profesión.
