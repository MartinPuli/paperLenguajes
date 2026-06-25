# Guion EXTENDIDO con munición de datos — Bloques 2 y 4

> Cada bloque trae **material para 5-6 min** (elegís qué decir). Lo **negrita** es lo que no podés saltear; **[pausa]** = respirá y dejá que cale; *(extra)* = dato del dossier que **no** estaba en el paper, para sumar profundidad.
> Al final de cada bloque hay un **BANCO DE DATOS** para estirar y un **BLINDAJE** para repreguntas.

---

# 🎙️ BLOQUE 2 — “El presente: qué puede y qué no la IA (2021-2026)” · ~5-6 min

**Entrada (~25 s)**
> “Gracias, [compañero]. Vimos que la IA es el próximo escalón de abstracción. Ahora, la pregunta concreta: **¿qué puede y qué no puede hacer hoy?** Porque los datos de los últimos dos años son impactantes… pero cuentan una historia más interesante de lo que parece.”

## Slide · El presente · 2024-2026 — capacidad y adopción (~1 min 50 s)
> “Arranco con un solo número para dimensionar la velocidad: en 2023, el mejor modelo del mundo resolvía **menos del 2 %** de los bugs reales de GitHub —*1,96 %, para ser exactos (extra)*. Hoy, mediados de 2026, resuelve **casi el 89 %**. De uno de cada cincuenta a casi **nueve de cada diez**, en tres años. [pausa] El test se llama **SWE-bench Verified** y usa problemas reales de proyectos de verdad. De hecho, ya **se saturó**: nos quedamos sin problemas difíciles para medir. *Y para cerrar la cronología: en junio de 2026 aparecieron modelos todavía más potentes —Fable 5 y Mythos 5— y a los pocos días una directiva del gobierno de EE. UU. les suspendió el acceso. La capacidad ya choca con lo regulatorio. (extra)*
>
> Y esto **no es laboratorio, está en producción**: Copilot superó los **20 millones** de usuarios —*77 mil empresas pagan por él, 180 % más en un año (extra)*. Microsoft dice que **20-30 %** de su código lo escribe la IA. Y Google pasó de *‘más de un cuarto’ en 2024 (extra)* al **75 % en 2026** —eso sí, **‘aprobado por ingenieros’**. Esa coletilla, ‘aprobado por ingenieros’, **guárdenla**: es la clave de todo el trabajo.”

## Slide · El contexto lo cambia todo — la productividad real (~2 min)
> “Ahora, uno escucha 89 % y piensa ‘listo, nos reemplazan’. Pero la evidencia rigurosa dice otra cosa. En una tarea **acotada** —programar un servidor desde cero— Copilot acelera **+55,8 %**: *terminaron en 1 hora y cuarto lo que a los demás les llevó casi 3 horas (extra)*. **PERO** un ensayo independiente, de una organización llamada **METR**, tomó a desarrolladores **expertos** en sus **propios** repos maduros —el código real de todos los días— y midió que con IA tardaron un **19 % MÁS**. Más lentos. [pausa] Y lo más fuerte: *ellos creían que habían ido un 20 % más rápido; los economistas predecían una mejora del 39 %, los de machine learning del 38 %… y la realidad fue −19 %. **Todos se equivocaron en el signo.** (extra)*
>
> ¿La lección? **El contexto lo cambia todo.** *De hecho, el experimento de campo más grande —casi 5.000 desarrolladores en el MIT— encontró +26 % de tareas completadas, pero el beneficio fue para los **juniors**, no para los seniors (extra)*. La IA amplifica al que arranca y en tareas simples; pero puede **estorbar al experto** en un sistema complejo que ya conoce. No es magia uniforme: depende de **quién** la usa y **para qué**.”

## Slide · El 30 % que importa — calidad, seguridad y el cuello de botella (~2 min)
> “Y acá está el corazón del bloque: el **‘problema del 70 %’** de Addy Osmani, ingeniero de Google. La IA te da el 70 % fácil rapidísimo; pero el **30 % que queda** —casos límite, depuración, mantenibilidad— sigue necesitando criterio. Osmani lo remató así: *‘la calidad del software nunca estuvo limitada por la velocidad de tipeo’ (extra)*. Y ahí están los riesgos. **Stanford** encontró lo más peligroso: con un asistente de IA la gente escribía código **menos seguro**… y confiaba **más** en él. La **falsa confianza** es el verdadero riesgo. [pausa]
>
> ¿Y mejora con el tiempo? No. *En 2025, **Veracode** probó **más de 100 modelos**: el **45 %** del código tenía una vulnerabilidad —en Java, el **72 %**— y los modelos **más nuevos NO fueron más seguros** (extra)*. Dos datos más que sorprenden: cuando se endurecen los tests, la corrección reportada **se desploma hasta 29 puntos** —los benchmarks sobreestiman—; y **1 de cada 5 paquetes** que la IA recomienda instalar… **no existe**: *el 19,7 % exacto (extra)*. Los atacantes ya registran esos nombres inventados con malware —se llama **slopsquatting**, un agujero de seguridad creado por la IA. [pausa]
>
> Hay un dato que cierra todo, de 2015: *la mayoría del código que ‘pasa los tests’ resultó ser **incorrecto** —pasar los tests no es ser correcto (extra)*. Por eso la frase del bloque: **la IA acelera la producción, pero no garantiza la corrección.** El cuello de botella se corre: ya no es escribir el código, es **verificarlo**.”

**Pase al Bloque 3 (~15 s)**
> “Y la pregunta del millón: ¿**por qué** esa verificación no se puede automatizar del todo? No es opinión, es **matemática**. Te paso, [compañero].”

### 🔋 BANCO DE DATOS Bloque 2 (para estirar o repreguntas)
- **GitClear:** con IA el copy-paste subió y el refactor cayó; **2024 fue el primer año con más copy-paste que refactorización** → deuda técnica.
- **DORA (Google):** más adopción de IA se asoció con **−7,2 % de estabilidad** de entrega, dos años seguidos *(es correlación, no causa)*.
- **Stack Overflow 2025:** 84 % usa IA, pero **solo ~1/3 confía** en su exactitud y **45 % dice que depurar código de IA lleva más tiempo**.
- **Pearce (MITRE, 2022):** ~40 % de sugerencias con vulnerabilidades (modelo viejo; Veracode 2025 es la versión actualizada).

### 🛡️ BLINDAJE (si te repreguntan)
- *“Peng +55,8 % y METR −19 % se contradicen”* → **No**: tarea greenfield acotada vs. mantenimiento en repos maduros; vendor vs. independiente. No son comparables, son **contextos distintos**.
- *“¿De dónde sale el 89 %?”* → SWE-bench Verified, modelo Opus 4.8 de Anthropic, 2026.
- Casi todos los % de “código por IA” (Google, Microsoft) son **auto-reportados por empresas** → decí “según Google/Microsoft”. METR aclaró que su −19 % es de **inicios de 2025**.

---

# 🎙️ BLOQUE 4 — “El nuevo rol, el empleo y la conclusión” · ~5-6 min

**Entrada (~25 s)**
> “Gracias, [compañero]. Recapitulando: la IA es potentísima pero no garantiza corrección, y hay **límites matemáticos** —Turing, Rice, P vs. NP, Chomsky— que aseguran que siempre hará falta criterio humano. La pregunta ahora es práctica: **¿en qué se convierte el ingeniero?** ¿Y qué pasa con el empleo? Acá el trabajo se pone **honesto**.”

## Slide · El nuevo rol (~1 min 30 s)
> “El rol se desplaza: el ingeniero escribe **menos código** y dedica su tiempo a **especificar, diseñar, validar y decidir**. Y cada tarea se apoya en los límites del bloque anterior: **validar**, porque Rice y Turing prueban que la verificación total es indecidible; **decidir**, porque P vs. NP dice que no hay atajos; **traducir** la intención humana —ambigua— a una especificación formal, que es Chomsky. Lo resumo en tres perfiles que crecen: el **arquitecto** (define el qué), el **auditor** (valida lo que la IA produce) y el **responsable** (firma y rinde cuentas). *Brooks ya lo había dicho en 1987: ‘lo más difícil de construir software es decidir con precisión qué construir’. Y el cuerpo oficial de la disciplina, el **SWEBOK**, tiene **18 áreas** de conocimiento; codificar es apenas una (extra)*. En una frase: **ese 30 % difícil pasa a ser el centro** de la profesión.”

## Slide · Empleo y economía (~2 min)
> “¿Y el empleo? Acá hay que ser **honesto**, porque no es color de rosa. Los números grandes son positivos: el **Foro Económico Mundial** proyecta a 2030 **+170 millones** de empleos creados, **−92 millones** desplazados, **saldo neto +78 millones** —y que **el 40 % de las habilidades cambian**. En software, la **BLS** proyecta ‘**desarrollador +15 %**’ frente a ‘**programador puro −6 %**’: no muere la profesión, **muere la tarea**. Es la **paradoja de Jevons**: los cajeros automáticos no eliminaron a los bancarios —*bajaron de 21 a 13 cajeros por sucursal, pero los bancos abrieron 43 % más sucursales, y por dos décadas hubo más empleo (extra)*. Cuando algo se abarata, se usa más. [pausa]
>
> **PERO** —y esta es la parte dura— no es parejo: **la puerta de entrada se cierra para los juniors**. La contratación de recién recibidos cayó **~65 % en las big tech** y **76 % en las startups**. Stanford midió, con datos de nómina reales, que el empleo de los de **22 a 25 años** en trabajos expuestos cayó **hasta un 16 %**, mientras los experimentados quedaron estables. Indeed: los puestos junior se contrajeron **34 %**, casi el doble que los senior. Y Salesforce lo dijo sin filtro: subió su productividad **más del 30 %** con IA, así que en 2025 **no contrata ingenieros**. **Se vacía la base.** [pausa] *Y acá la paradoja más honesta: los estudios muestran que la IA ayuda **más al novato** que al experto —hasta +34 %—, pero el mercado se cierra justo para el novato, porque la IA le come las tareas con las que aprendía (extra).*”

## Slide · Las dos miradas (~1 min 30 s)
> “En el debate hay dos campos. **Optimistas**: Amodei dice que la IA escribirá el 90 % del código… pero en la **misma frase** aclara: *‘el programador todavía tiene que especificar las decisiones de diseño’*. Altman lo dice más claro todavía: *‘los expertos seguirán siendo mucho mejores que los novatos, **siempre que adopten las herramientas**’* — esa es la polarización en boca del CEO de OpenAI. Y **cautos**: Grady Booch, el padre del UML, le contesta con una frase que vale toda la charla: *‘tus herramientas están cambiando, pero tus problemas no’*. Stroustrup, el creador de C++, avisa que la IA genera más bugs y agujeros de seguridad **justo cuando los seniors que sabrían validarlos se jubilan**. [pausa] Pero el **punto en común** es clave: **hasta los más optimistas** reservan para el humano especificar, decidir y juzgar. **Nadie** dice que eso lo hace la máquina sola.”

## Slide · Síntesis (~1 min 10 s)
> “Entonces, la síntesis: no es reemplazo, pero tampoco ‘todo sigue igual’. Es **POLARIZACIÓN**. **Se vacía el medio**: el programador del montón cae, pero el desarrollador con criterio crece y los puestos con IA pagan **prima**. Lo dijo brutal **Kent Beck**, el inventor del TDD: *‘el 90 % de mis habilidades ahora valen cero dólares; pero el otro 10 % —el criterio, el diseño— vale **mil veces más**’*. Esa es la polarización dentro de una misma cabeza. En diez años habrá **menos ingenieros del montón y más ingenieros PRO** — **sobreviven y crecen los mejores**. ¿Y por qué el que queda es un **humano** y no otra IA? Porque alguien tiene que **responder**: asumir la responsabilidad y decidir los fines. Y eso no es un cálculo más difícil —es una categoría distinta, que ninguna máquina asume.”

**Cierre (~20 s)**
> “Cierro: la teoría de la computación, lejos de anunciar el fin de la profesión, traza el contorno —**exigente**— de su porvenir. **La IA no anuncia el fin del ingeniero: redefine quién lo es.** Gracias. ¿Preguntas?”

### 🔋 BANCO DE DATOS Bloque 4 (para estirar o repreguntas)
- **Fowler:** los LLM son un salto como el de assembler a los lenguajes de alto nivel, pero son la **primera abstracción no determinista** de la historia —y lo no determinista hay que **vigilarlo**.
- **Huang (NVIDIA):** *“nadie tiene que programar… todos somos programadores”* — la versión más extrema del optimismo (que Chomsky relativiza: el lenguaje humano es ambiguo).
- **SignalFire:** mientras los recién recibidos caen, los puestos **mid-level subieron +27 %** → la demanda se corre hacia perfiles con criterio.
- **Acemoglu-Restrepo / Autor:** la tecnología **recompone tareas**, no elimina empleos; automatizar unas tareas **eleva el valor** de las humanas.

### 🛡️ BLINDAJE (si te repreguntan)
- *“Pero la BLS dice que CRECE +15 %”* → *“Sí: la categoría amplia crece **de la mano de los skilled**; lo que se derrumba es la base junior y el programador puro. Por eso es **polarización, no reemplazo**.”*
- *“¿No es todo optimismo?”* → *“No: hay **perdedores concretos** —la puerta junior se estrecha— y lo digo en la conclusión.”*
- *“¿La IA no causa el desempleo junior?”* → *“La causalidad está en disputa: puede ser IA o el **fin del crédito barato** post-2021. Por eso hablo de **tendencia convergente**, no de prueba cerrada.”* *(blindaje de oro)*
- ⚠️ **No uses** una cita de **Tom DeMarco** (no está en nuestras fuentes) ni inventes una “prima salarial de X %” (no la tenemos medida; usá Altman + Beck).

---

## ⏱️ Cómo clavar 5 minutos (presentación = ~120-130 palabras/min con pausas)
- **Si vas justo de tiempo:** decí solo las líneas en **negrita** + una *(extra)* por slide.
- **Si te sobra:** sumá del **BANCO DE DATOS**.
- **Los 4 remates que tienen que quedar:** Bloque 2 → *“89 % de capacidad / 19 % más lentos los expertos”* (pausa entre los dos) y *“pasar los tests no es ser correcto”*. Bloque 4 → *Beck: “90 % vale $0, el 10 % vale 1000×”* y *“menos del montón, más PRO”*.
