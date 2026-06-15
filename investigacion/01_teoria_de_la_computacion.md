# 01 — Límites fundamentales de la computación

Columna vertebral teórica del paper: por qué ninguna IA (que es un proceso computable) puede automatizar por completo la verificación, la resolución eficiente ni la traducción de la intención humana a especificación formal.

---

## 1. Problema de la detención (Halting Problem) — Turing (1936)

**Enunciado.** No existe ningún algoritmo (máquina de Turing) que, dado un programa arbitrario y una entrada arbitraria, decida en todos los casos si ese programa se detendrá o se ejecutará indefinidamente. El conjunto `K = {n | M_n(n)↓}` no es decidible; se prueba por diagonalización. Turing lo demostró para deducir la indecidibilidad del Entscheidungsproblem.

**Cita (APA).** Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, s2-42*(1), 230–265. https://doi.org/10.1112/plms/s2-42.1.230
- Corrección: Turing, A. M. (1938). …A correction. *PLMS, s2-43*(6), 544–546. https://doi.org/10.1112/plms/s2-43.6.544
- Nota de fecha: el paper se recibió en 1936; el volumen está fechado 1937. Por convención se cita **1936**.
- Fuente autoritativa de apoyo: SEP, "Computability and Complexity": https://plato.stanford.edu/entries/computability/

**Implicación.** Hay propiedades del comportamiento de un programa que ningún sistema computacional (incluida cualquier IA) puede determinar de forma general y automática. La verificación universal del software es imposible en principio.

---

## 2. Teorema de Rice (1953)

**Enunciado.** Toda propiedad **semántica no trivial** de los programas (referida a la función que computan, no a su forma sintáctica) es **indecidible**. Generaliza el problema de la detención.

**Cita (APA).** Rice, H. G. (1953). Classes of recursively enumerable sets and their decision problems. *Transactions of the American Mathematical Society, 74*(2), 358–366. https://doi.org/10.1090/S0002-9947-1953-0053041-6
- (Probado en su tesis de 1951; la publicación de 1953 es la referencia estándar.)

**Implicación clave.** Es imposible escribir un programa que verifique, de forma totalmente general y automática, si un programa arbitrario satisface su especificación. Una IA **no puede demostrar la corrección de código arbitrario** en el caso general. Las herramientas reales (tipos, model checking, interpretación abstracta, lógica de Hoare) funcionan solo restringiendo el problema, exigiendo anotaciones humanas o renunciando a la completitud.

---

## 3. P vs NP y NP-completitud — Cook (1971), Karp (1972)

**Enunciado.** ¿Es P = NP? ¿Todo problema cuya solución se **verifica** rápido se puede también **resolver** rápido? Cook (y Levin, de forma independiente) probó que SAT es NP-completo; Karp extendió la NP-completitud a 21 problemas. Uno de los siete Problemas del Milenio (Clay Institute, premio de USD 1.000.000).

**Citas (APA).**
- Cook, S. A. (1971). The complexity of theorem-proving procedures. *STOC '71* (pp. 151–158). ACM. https://doi.org/10.1145/800157.805047
- Karp, R. M. (1972). Reducibility among combinatorial problems. En *Complexity of Computer Computations* (pp. 85–103). Plenum. https://doi.org/10.1007/978-1-4684-2001-2_9
- Clay Mathematics Institute: https://www.claymath.org/millennium/p-vs-np/

**Implicación.** Muchos problemas reales de ingeniería (scheduling, ruteo, satisfacción de restricciones, verificación) son NP-difíciles. Bajo P ≠ NP, ninguna IA los resuelve eficientemente en el peor caso; el límite es matemático. El ingeniero elige heurísticas, aproximaciones y trade-offs: decidir qué sacrificar es juicio, no cálculo automatizable.

---

## 4. Jerarquía de Chomsky (1956)

**Enunciado.** Jerarquía de gramáticas formales anidadas: Tipo 3 regulares (autómatas finitos) ⊊ Tipo 2 libres de contexto (autómatas con pila) ⊊ Tipo 1 sensibles al contexto (autómatas linealmente acotados) ⊊ Tipo 0 recursivamente enumerables (máquinas de Turing).

**Cita (APA).** Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory, 2*(3), 113–124. https://doi.org/10.1109/TIT.1956.1056813

**Implicación.** Los lenguajes de programación son lenguajes formales (sintaxis típicamente libre de contexto), analizados de forma determinista y sin ambigüedad. El lenguaje natural —y los prompts a un LLM— es ambiguo, dependiente del contexto y no es un lenguaje formal. El rol perdurable del ingeniero es traducir la intención informal a especificación formal. (Ver `02_transformers_y_lenguajes_formales.md` para cómo los propios transformers quedan acotados por esta jerarquía.)

---

## 5. Alucinación inevitable de los LLM (computabilidad aplicada a la IA)

- **Xu, Z., Jain, S., & Kankanhalli, M. (2024).** *Hallucination is inevitable: An innate limitation of large language models* (arXiv:2401.11817). https://arxiv.org/abs/2401.11817
  - Mediante diagonalización apoyada en la indecidibilidad de la parada: ningún LLM (máquina de Turing) puede aprender todas las funciones computables; por tanto, inevitablemente alucina. No es un defecto corregible sino un límite computacional.
- **Suzuki, A., He, Y., Tian, F., & Wang, Z. (2025).** *Hallucinations are inevitable but can be made statistically negligible* (arXiv:2502.12187). https://arxiv.org/abs/2502.12187
  - Confirma vía diagonalización que todo modelo alucina sobre infinitas entradas; el error puede reducirse hasta ser estadísticamente despreciable, pero no eliminarse en principio.
- **Banerjee, Agarwal & Singla (2024).** *LLMs Will Always Hallucinate, and We Need to Live with This* (arXiv:2409.05746). Invoca explícitamente el halting problem, el emptiness problem y el acceptance problem.

**Implicación.** Un LLM no puede garantizar ni autoverificar la corrección de su salida (misma barrera Rice/Turing aplicada al modelo). Necesita un agente externo —el ingeniero— que valide y asuma responsabilidad.

---

## 6. Sintaxis vs. semántica; la especificación como tarea humana — Brooks (1987)

- **Sintaxis** (forma, decidible para lenguajes libres de contexto) vs. **semántica** (significado/comportamiento; indecidible por Rice).
- Decidir **qué** construir no es un problema de decisión sobre un alfabeto: es una tarea humana, contextual y cargada de valores. No hay un "ground truth" formal previo que un algoritmo pueda consultar.

**Cita (APA).** Brooks, F. P. (1987). No silver bullet: Essence and accidents of software engineering. *Computer, 20*(4), 10–19. https://doi.org/10.1109/MC.1987.1663532
- PDF público: https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf
- Frase textual: *"The hardest single part of building a software system is deciding precisely what to build."*
- Distinción complejidad **esencial** (irreducible, conceptual) vs. **accidental** (de implementación, reducible por herramientas). La IA ataca lo accidental; lo esencial permanece humano.

---

## Tabla síntesis

| Resultado | Cita | Límite | Por qué la IA no reemplaza al ingeniero |
|---|---|---|---|
| Halting Problem | Turing (1936) | Indecidibilidad de la terminación | No se decide el comportamiento de software en general |
| Teorema de Rice | Rice (1953) | Toda propiedad semántica no trivial es indecidible | No hay verificación universal automática contra especificación |
| P vs NP | Cook (1971); Karp (1972) | Intratabilidad en el peor caso | Hacen falta heurísticas y trade-offs (juicio) |
| Jerarquía de Chomsky | Chomsky (1956) | Formal vs. lenguaje natural ambiguo | El ingeniero traduce intención informal → especificación formal |
| Alucinación inevitable | Xu et al. (2024); Suzuki et al. (2025) | Diagonalización aplicada a LLMs | La IA no garantiza ni autoverifica su corrección |
| Sintaxis vs. semántica | Brooks (1987) | Decidir QUÉ construir no es computable | La especificación es humana y cargada de valores |
