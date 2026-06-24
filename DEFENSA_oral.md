# Hoja de defensa oral — *El rol del ingeniero informático en los próximos diez años*

> Materia: Lenguajes Formales y Teoría de la Computación (UCEMA). Integrantes: Martín Ezequiel Pulitano y Nicolás Ulises Silva.

## 1. La tesis en una frase
La IA **no hace desaparecer la profesión, pero la reduce y polariza**: habrá **menos ingenieros** —sobre todo en la base rutinaria/junior— y el valor **se concentra en los mejores**. ¿Por qué persiste un núcleo humano? Porque hay **límites de la computación** que ninguna máquina sortea: la verificación universal (Rice/Turing), la resolución eficiente (P vs. NP) y la traducción de la intención ambigua a lo formal (Chomsky).

## 2. Los 4 conceptos teóricos que TENÉS que poder explicar

**a) Problema de la detención + diagonalización (Turing, 1936).**
Supongamos que existe `H(p,x)` que decide si el programa `p` con entrada `x` termina. Construyo `D(p)`: *si `H(p,p)` dice "termina", entro en un bucle infinito; si dice "no termina", termino*. Ahora corro `D(D)`: si `H` dice que `D(D)` termina → `D` entra en bucle (no termina) → **contradicción**; si dice que no termina → `D` termina → **contradicción**. Por lo tanto `H` no puede existir: la detención es **indecidible**. (Es **semidecidible**: ejecutando el programa puedo *confirmar* que para, pero no, en general, que *no* para.)

**b) Teorema de Rice (1953).**
*Toda propiedad **semántica** (sobre lo que el programa **hace**, no sobre su texto) y **no trivial** (que algunos programas cumplan y otros no) es indecidible.* Se prueba por reducción del halting. **Ojo en la repregunta:** Rice NO dice que toda pregunta sobre un programa sea indecidible — las propiedades **sintácticas** ("¿el código contiene un `for`?") **sí** son decidibles. Por eso el ejemplo correcto es "¿cumple su especificación?" (semántico), no "¿tiene tal palabra clave?".

**c) P vs. NP (Cook 1971; Karp 1972).**
P = se **resuelve** rápido; NP = se **verifica** rápido. La pregunta es si P = NP. **Trampa clásica:** *NP-difícil ≠ indecidible*. Los problemas NP-difíciles **sí tienen algoritmo** (son decidibles), solo que —si P ≠ NP— **no eficiente** en el peor caso. "Intratable" (tarda exponencial pero se puede) es distinto de "indecidible" (no hay algoritmo). Cook-Levin probó que SAT es NP-completo; Karp lo extendió a 21 problemas.

**d) Jerarquía de Chomsky + transformers/TC⁰.**
Regular ⊂ libre de contexto ⊂ sensible al contexto ⊂ recursivamente enumerable. La **sintaxis** de un lenguaje de programación es *esencialmente* libre de contexto (léxico regular; algunas reglas —tipos, declaración previa— son sensibles al contexto). El lenguaje natural **no** se captura limpio por la jerarquía. Sobre transformers: el **cómputo interno** de un transformer de precisión logarítmica está acotado por **TC⁰** y —salvo que se caigan conjeturas estándar (L ≠ P)— no reconoce gramáticas libres de contexto arbitrarias. **Clave defensiva:** eso acota la **arquitectura actual** como *reconocedor*; no dice que la IA no pueda *emitir* código, ni es un límite eterno como Turing/Rice.

**Bonus:** *Alucinación inevitable* (Xu et al. 2024): por diagonalización, ningún LLM aprende todas las funciones computables → siempre produce errores que no autodetecta. *Brooks*: complejidad **esencial** (decidir qué construir) vs **accidental** (la IA solo reduce la accidental). *Naur*: programar es construir una **teoría** del problema que el código no captura.

## 3. La tensión que te pueden marcar (y cómo responder)
**"Decís 'menos ingenieros' pero la BLS proyecta +15 % para 'desarrolladores'."**
→ Es **polarización, no contradicción**: la categoría amplia crece despacio *de la mano de los skilled* (los "mejores"), mientras **la base se derrumba** — "programadores" −6 % (BLS), empleo joven −13-16 % (Brynjolfsson), contratación de recién recibidos −50 % (SignalFire). No es "menos en bloque": es **se vacía la base y se concentra arriba**. Por eso la hipótesis dice "menos, **sobre todo en puestos rutinarios y de nivel inicial**".

## 4. Preguntas incómodas más probables
- **"Si los límites valen para todo proceso computable, ¿no atrapan también al humano?"**
  → Sí, probablemente. La ventaja del ingeniero **no es escapar a los teoremas**, sino **asumir responsabilidad y decidir fines** —una categoría jurídico-moral, no computacional—. Lo inautomatizable no es un cómputo más difícil: es responder por el resultado.
- **"¿No es esto optimismo / cope?"**
  → No: el trabajo muestra la cara dura (−50 % juniors, "house of cards code", METR: −19 % en seniors, la transición "no es color de rosa, con perdedores concretos").
- **"Tus fuentes son CEOs interesados."**
  → Lo decimos explícitamente en VII. Las afirmaciones fuertes se apoyan en **RCT (METR), BLS y Stanford**, no en ejecutivos.
- **"¿Por qué el que queda es un humano y no otra IA supervisora?"**
  → Porque alguien tiene que **responder** (responsabilidad) y **fijar los fines/valores**; una IA supervisora hereda los mismos límites (Rice/Xu) y no asume responsabilidad.

## 5. Pitch de 30 segundos
> "La historia muestra que cada abstracción elevó al ingeniero. Hoy la IA es la abstracción más potente, pero choca con muros matemáticos —Turing, Rice, P vs. NP, Chomsky— que garantizan un núcleo humano de juicio. La consecuencia no es color de rosa: habrá **muchos menos** ingenieros, se vacía la base junior y el valor se concentra en **los mejores**, los que pasan de ejecutar a especificar, validar y decidir. No desaparece la profesión; se achica y se vuelve más exigente."
