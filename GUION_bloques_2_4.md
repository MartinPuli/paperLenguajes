# Guion hablado EXTENDIDO (~5 min por bloque) — Bloques 2 y 4

> Cada bloque ≈ **700-750 palabras ≈ 5 min** hablando tranquilo (~145 palabras/min).
> Las **[pausa]** son para respirar y dejar que cale el dato. Lo **negrita** es lo que no podés saltear.
> Practicá en voz alta con cronómetro: si te sobra, sumás un ejemplo; si te falta, recortás una explicación.

---

# 🎙️ BLOQUE 2 — “El presente: qué puede y qué no la IA (2021-2026)” · ~5 min

**Entrada (~30 s)**
> “Gracias, [compañero]. Recién vimos que la historia del software es subir escalones de abstracción, y que la IA es el próximo escalón. Ahora la pregunta se vuelve concreta: **¿qué puede y qué no puede hacer la IA hoy?** Porque una cosa es el discurso y otra son los datos. Y los datos de los últimos dos años son impactantes… pero más matizados de lo que parece.”

**Slide · El presente · 2024-2026 (~1 min 20 s)**
> “Empecemos por la capacidad pura. Hay un test estándar en la industria, **SWE-bench Verified**: agarra problemas **reales** —issues de proyectos de software de verdad— y mide qué porcentaje resuelve un sistema de IA de punta a punta. Bueno: a comienzos de 2024 los mejores modelos resolvían **alrededor del 14 %** —uno de cada siete. A mediados de 2026 están en **casi el 89 %** —casi nueve de cada diez. **En dos años.** De hecho el benchmark prácticamente **se saturó**: nos quedamos sin problemas difíciles para medir. [pausa] Y esto no es laboratorio, ya está en producción: GitHub Copilot superó los **veinte millones** de usuarios; Microsoft dice que **20-30 %** de su código lo escribe la IA; y Google fue más lejos —en 2026 su CEO declaró que el **75 % del código nuevo** lo genera la IA, *aprobado por ingenieros*. Esa coletilla, ‘aprobado por ingenieros’, **guárdenla**, porque es la clave de todo el trabajo.”

**Slide · El contexto lo cambia todo (~1 min 30 s)**
> “Ahora viene el matiz que casi todos se saltean. Uno escucha 89 % y piensa: ‘listo, nos reemplazan’. Pero la evidencia rigurosa cuenta otra historia. En tareas **acotadas** —por ejemplo, programar un servidor desde cero— la IA acelera muchísimo: un estudio controlado midió **+55,8 %** más rápido con Copilot. Hasta ahí, perfecto. **PERO** hubo otro ensayo controlado, de una organización independiente llamada **METR**, que tomó a desarrolladores **expertos**, trabajando en sus **propios** repositorios —grandes, maduros, el código real de todos los días. ¿Resultado? Con IA tardaron un **19 % MÁS**. Más lentos. [pausa] Y lo más fuerte: ellos **creían** que habían ido un 20 % más rápido. Ni lo percibían. La conclusión es potente: **el contexto lo cambia todo.** La IA amplifica al que arranca o está aprendiendo, pero puede **estorbar al experto** en un sistema complejo que ya conoce de memoria. No es una herramienta mágica y uniforme: depende de **quién** la use y **para qué**.”

**Slide · El 30 % que importa (~1 min 30 s)**
> “Y esto nos lleva al corazón del bloque: una idea de Addy Osmani, ingeniero de Google, **‘el problema del 70 %’**. La IA te resuelve rapidísimo el **70 % fácil**: el esqueleto, lo repetitivo, lo que ya se hizo mil veces. Pero el **30 % que queda** —los casos límite, la depuración, la integración con lo que ya existe, la seguridad— ese 30 % sigue necesitando a un ingeniero que sepa. Y no es un detalle, porque ahí están los riesgos. Los datos asustan un poco: un estudio de **Stanford** encontró que los que usaban un asistente de IA escribían código **menos seguro**… y encima confiaban **más** en él —una falsa sensación de seguridad. Cerca del **40 %** de las sugerencias en escenarios de seguridad traían vulnerabilidades conocidas. Y una más, casi de ciencia ficción: **1 de cada 5 paquetes** que la IA recomienda instalar… **no existe**. Se los inventa. Eso abre un agujero de seguridad nuevo que ya tiene nombre: *slopsquatting*. [pausa] Entonces, la frase que resume todo el bloque: **la IA acelera la producción, pero no garantiza la corrección.** Y por eso el cuello de botella del trabajo se corre: ya no es escribir el código, es **verificarlo**.”

**Pase al Bloque 3 (~15 s)**
> “Y acá está la pregunta del millón: ¿**por qué** esa verificación no se puede automatizar del todo? ¿Por qué siempre va a hacer falta un humano? Eso no es opinión: es **matemática**. Y se los explica [compañero].”

---

# 🎙️ BLOQUE 4 — “El nuevo rol, el empleo y la conclusión” · ~5 min

**Entrada (~30 s)**
> “Gracias, [compañero]. Recapitulemos: la IA es potentísima pero no garantiza corrección, y hay **límites matemáticos** —Turing, Rice, P vs. NP, Chomsky— que aseguran que siempre hará falta criterio humano. La pregunta ahora es práctica: si eso es así, **¿en qué se convierte el ingeniero?** ¿Y qué pasa con el empleo? Porque acá el trabajo deja de ser optimista y se pone **honesto**.”

**Slide · El nuevo rol (~1 min 20 s)**
> “El rol se desplaza. El ingeniero escribe **menos código** línea por línea y dedica su tiempo a cuatro cosas: **especificar** con precisión qué tiene que hacer el sistema; **diseñar** la arquitectura e integrar piezas —incluidos los propios modelos de IA—; **validar** lo que las máquinas producen; y **decidir** bajo restricciones y con criterios de valor. Y fíjense que cada una se apoya en los límites del bloque anterior: validar, porque Rice y Turing prueban que la verificación total es indecidible; decidir, porque P vs. NP dice que no hay atajos mágicos; y traducir la intención humana —ambigua— a una especificación formal, que es el problema de Chomsky. Lo podemos resumir en **tres perfiles que crecen**: el **arquitecto**, que define el qué; el **auditor**, que valida lo que la IA produce; y el **responsable**, que firma y rinde cuentas. Dicho simple: ese **30 % difícil pasa a ser el centro** de la profesión.”

**Slide · Empleo y economía (~1 min 40 s)**
> “¿Y el empleo? Acá hay que ser honesto, porque **no es todo color de rosa**. Los números grandes son positivos: el **Foro Económico Mundial** proyecta a 2030 unos **+170 millones** de empleos creados, **−92 millones** desplazados, **saldo neto +78 millones**. Y en software, la oficina de estadísticas de EE. UU. proyecta que ‘**desarrollador**’ crece un **15 %**, mientras ‘**programador puro**’ —el que solo teclea— cae un **6 %**. La lección: **no muere la profesión, muere la tarea.** Hay un concepto que lo explica, la **paradoja de Jevons**: cuando algo se abarata, se usa más. Los cajeros automáticos no eliminaron a los bancarios —abarataron la sucursal, los bancos abrieron más, y por dos décadas hubo más empleados. **PERO** —y acá viene la parte dura— eso no es parejo: la **puerta de entrada se cierra para los juniors**. La contratación de recién recibidos en las grandes tecnológicas cayó cerca del **65 %**. Salesforce directamente anunció que **no suma ingenieros** este año porque subió su productividad más del 30 % con IA. Y los datos muestran que los puestos junior se contraen mucho más que los senior. **Se vacía la base.**”

**Slide · Las dos miradas (~1 min 10 s)**
> “En el debate hay dos campos. Los **optimistas**: Amodei, de Anthropic, dice que la IA va a escribir el **90 %** del código; Altman, que **amplifica al que sabe usarla**. Y los **cautos**: Grady Booch, una eminencia, dice que pronosticar el reemplazo es ‘un disparate’ y que revela ‘no entender qué es la ingeniería de software’; Stroustrup, el creador de C++, advierte que la IA genera más errores y más agujeros de seguridad, código difícil de validar… justo cuando los seniors que sabrían validarlo **se están jubilando**. Pero el **punto en común** es clave: hasta los más optimistas reservan para el humano **especificar, decidir y juzgar**. Nadie, en ningún campo, dice que eso lo hace la máquina sola.”

**Slide · Síntesis (~1 min)**
> “Entonces, ¿la síntesis del paper? No es reemplazo, pero tampoco ‘todo sigue igual’. Es **POLARIZACIÓN**. Se vacía el medio: el programador del montón cae, pero el desarrollador con criterio crece, y los puestos que saben usar IA pagan **prima**. En diez años habrá **menos ingenieros ‘del montón’ y más ingenieros PRO**. **Sobreviven y crecen los mejores**: los que dan el salto de ejecutar a especificar, validar y decidir. Y hay una razón de fondo por la que el que queda es un **humano** y no otra IA: porque alguien tiene que **responder** —asumir la responsabilidad, decidir los fines—. Y eso no es un cálculo más difícil: es una categoría distinta, que ninguna máquina asume.”

**Cierre (~20 s)**
> “Cierro con una frase: la teoría de la computación, lejos de anunciar el fin de la profesión, traza el contorno —exigente— de su porvenir. **La IA no anuncia el fin del ingeniero: redefine quién lo es.** Gracias. ¿Preguntas?”

---

## ⏱️ Para clavar los 5 minutos
- **Si te SOBRA tiempo** (vas corto): en el Bloque 2 sumá el dato de **Liu** (“cuando se endurecen los tests, la corrección del código cae entre 19 y 29 puntos”); en el Bloque 4 sumá **Brynjolfsson** (“empleo joven −13 a −16 % en ocupaciones expuestas”) o el chiste de Claude.
- **Si te FALTA tiempo** (te pasás): en el Bloque 2 resumí “El contexto lo cambia todo” en una frase (+55,8 % en tareas fáciles, −19 % con expertos); en el Bloque 4 cortá la lista de escépticos a solo Booch.
- **Repreguntas frecuentes y de dónde sale cada dato:** 89 % = SWE-bench (Anthropic, Opus 4.8, 2026); −19 % = METR (2025); +15 %/−6 % = BLS; +78 M = WEF 2030; 75 % Google = Pichai (2026); −65 % juniors = SignalFire (2026).
- **Defensa de la “tensión”:** si te dicen “pero la BLS dice que CRECE +15 %”, respondés: *“sí, la categoría amplia crece de la mano de los skilled; lo que se derrumba es la base junior y el programador puro. Por eso es polarización, no reemplazo.”*
