# Slides + diálogo — Bloques 2 y 4
> La forma creativa de contarlo. Cada slide = **una idea, un número/cita gigante, cero bullets**.
> Vos narrás; la slide solo *muestra la prueba*. El diálogo está para decirlo casi tal cual.

---

## 🎨 El concepto creativo (leé esto primero)

**Regla de oro: “aserción–evidencia”.** El título de cada slide NO es un sustantivo (“Adopción”), es **una frase con filo** (“La adopción más rápida de la historia”). Debajo, **un solo protagonista visual**: un número enorme, una cita, o un gráfico. Nada de listas. La slide afirma; vos demostrás.

**El motivo que une todo: el GIRO (setup → vuelta → remate).** Como un truco de magia. Cada bloque arranca con el “milagro” y a mitad de camino mete el “pero…”. Eso mantiene a la gente despierta y te hace ver honesto, no fan.

**Dos hilos visuales recurrentes (tu “marca” en el deck):**
- 🟦 **Bloque 2** → un *medidor de cuello de botella* arriba que se va desplazando de **ESCRIBIR → VERIFICAR**. Empieza a la izquierda y termina a la derecha. Es tu through-line.
- 🟢 **Bloque 4** → una *escalera de abstracción* en una esquina; en cada slide subís un peldaño y, sobre el final, **se vacía el escalón del medio**.

**Trucos baratos que rinden muchísimo:**
- **Un número que “crece” en pantalla** (1,96 % → 89 %) con animación de conteo. La gente recuerda el gesto.
- **Cita a pantalla completa, fondo negro, sin logo.** Para Osmani, Beck, el FMI. Silencio de 1 segundo antes de leerla.
- **Fun fact en un pos-it amarillo** en la esquina (“⚠ slopsquatting”): el ojo lo busca y vos lo soltás como bonus.
- **Antes/después en diagonal** para Peng (+55,8 %) vs METR (−19 %): misma tecnología, dos flechas opuestas.

**Número de slides:** 7 por bloque (≈40 s cada una = 5 min). Si vas corto, las slides 5 son “sacrificables”.

---

# 🟦 BLOQUE 2 — El presente de la IA (2021–2026)
**Arco:** el milagro → la fiebre → el truco (productividad) → la grieta (calidad) → ¿quién paga? → el cuello de botella se mudó.

---

### Slide 1 · “En dos años pasó algo que no había pasado nunca”
**En pantalla:** un número gigante que sube **1,96 % → 89 %**. Subtítulo chico: *SWE-bench (bugs reales de GitHub)*. Pos-it: *⚠ el benchmark se saturó*.
**Diálogo (≈45 s):**
> “Arranco con un número. En 2023, el mejor modelo de IA resolvía menos del **2 %** de los bugs reales de proyectos de software. Dos años después: **casi el 89 %**. De uno de cada siete… a casi nueve de cada diez. Para que se den una idea de la velocidad: Devin abría con 13,9 % a principios de 2024; en mayo de 2026, Opus llegó a 88,6. Y el dato más loco no es el número, es que **el benchmark se quedó chico**: OpenAI dice que ‘ya no mide la frontera’. Cuando tu examen deja de servir porque todos lo aprueban… algo cambió de verdad.”
**Transición:** “Y si la capacidad explotó, ¿la gente lo usa? Spoiler: como nunca.”

---

### Slide 2 · “La adopción más rápida de la historia del software”
**En pantalla:** **20.000.000** (usuarios de Copilot) de fondo; tres chips: *Google 75 % · Microsoft 20–30 % · 84 % de devs*. Pos-it: *“aprobado por ingenieros”*.
**Diálogo (≈40 s):**
> “GitHub Copilot superó los **20 millones** de usuarios: ninguna herramienta de programación creció tan rápido. Sundar Pichai dijo que el **75 % del código nuevo** en Google ‘se genera con IA’ —y, ojo con la frase, ‘**lo aprueban ingenieros**’—. Nadella lo puso entre 20 y 30 % en Microsoft. Y el 84 % de los desarrolladores ya usa o planea usar IA. Guárdense ese ‘aprobado por ingenieros’, porque es la grieta por donde se va a colar todo el resto de la charla.”
**Transición:** “Entonces, más rápido y todos lo usan… volamos, ¿no? Acá viene el truco.”

---

### Slide 3 · “La misma herramienta acelera… y frena”
**En pantalla:** dos flechas en diagonal: **+55,8 %** (verde, sube) vs **−19 %** (rojo, baja). Abajo: *Peng/Copilot vs METR (expertos, repos propios)*. Pos-it: *creían +20 %*.
**Diálogo (≈55 s):**
> “Acá está la magia. Un experimento de GitHub midió que con Copilot programar un servidor era **55,8 % más rápido**. Tomá: la IA vuela. Pero un ensayo independiente, METR, agarró a **expertos en sus propios repositorios maduros**… y con IA tardaron **un 19 % MÁS**. ¿Y saben qué es lo mejor? Ellos **creían** que habían ido un 20 % más rápido. Todos —ellos, los economistas, los expertos en machine learning— predijeron que iban a acelerar. **Todos se equivocaron en el signo.** La moraleja no es ‘la IA es mala’: es que **el contexto lo cambia todo**. Tarea fácil y nueva: vuela. Sistema real y complejo: se traba.”
**Transición:** “¿Por qué se traba? Por el famoso último tramo.”

---

### Slide 4 · “El último 30 % es el que duele”
**En pantalla:** una barra **70 / 30**; el 30 % en rojo dice *casos límite · depuración · mantenibilidad*. Cita abajo.
**Diálogo (≈45 s):**
> “Addy Osmani, ingeniero de Google, lo llamó **‘el problema del 70 %’**: la IA te da el primer 70 % de una solución a una velocidad pasmosa. Pero el **30 % final** —los casos límite, la depuración, que el código sea mantenible— sigue necesitando el criterio de alguien que sepa. Y tiró la frase que se las dejo de regalo: *‘la calidad del software nunca estuvo limitada por la velocidad de tipeo’*. O sea: escribir más rápido nunca fue el cuello de botella.”
**Transición:** “Y cuando ese 30 % se ignora, no es que falta una feature: aparecen agujeros.”

---

### Slide 5 · “Código que parece correcto y no lo es”
**En pantalla:** **45 %** (Veracode, código con vulnerabilidad) grande; abajo dos datos: *Stanford: confían MÁS · Slopsquatting: 19,7 % de paquetes inventados*. Pos-it: *⚠ los atacantes los registran con malware*.
**Diálogo (≈50 s):**
> “Stanford encontró algo perverso: los que programan con IA escriben código **menos** seguro… pero **confían más** en que es seguro. Falsa sensación de seguridad. Veracode revisó: el **45 %** del código generado trae alguna vulnerabilidad, y —dato clave— los modelos más nuevos **no fueron más seguros**. Y mi fun fact favorito: **slopsquatting**. La IA inventa nombres de librerías que no existen —casi el **20 %** de las que recomienda—. ¿Qué hacen los atacantes? **Registran esos nombres falsos con malware adentro**, esperando que vos copies y pegues. La alucinación de la máquina se convirtió en un vector de ataque.”
**Transición:** “Hasta acá: rápida pero frágil. Falta una pregunta incómoda que casi nadie hace.”

---

### Slide 6 · “El elefante en la sala: ¿quién está pagando esto?”
**En pantalla:** cita gigante de Altman: *“elegí yo el precio y pensé que ganaríamos plata.”* Abajo: *OpenAI pierde con el plan de US$200 · MIT: 95 % de pilotos sin ROI · FMI: “comparable al pico de la puntocom”*. Pos-it: *pero el token crudo SÍ es rentable*.
**Diálogo (≈55 s):**
> “Pregunta que el entusiasmo evita: **el precio que pagás hoy, ¿refleja el costo real?** El propio Altman admitió que OpenAI **pierde plata** hasta con su plan de 200 dólares al mes —‘la gente lo usa más de lo que esperábamos’—. Documentos a inversores hablan de quemar **115.000 millones** antes de ser rentable. El MIT dice que el **95 %** de los pilotos de IA en empresas no muestra retorno medible. Y el **FMI** comparó las valuaciones con ‘el pico de la burbuja puntocom’. Ahora, seamos honestos —porque si no, me lo desarman—: **no es el año 2000**. Hay ingresos reales, y el token crudo sí da margen. Pero parte de lo barato que es programar con IA hoy… **lo subsidia el capital de riesgo**. Y eso tiene una consecuencia que retomo en mi segundo bloque.”
**Transición:** “Dejando la plata de lado, hay un patrón técnico que se repite en todo lo que vimos.”

---

### Slide 7 · “El cuello de botella se mudó: de escribir a verificar”
**En pantalla:** el medidor llega al extremo derecho: **ESCRIBIR → ✅ VERIFICAR**. Cita chica: *Qi (2015): la mayoría del código que ‘pasa los tests’ es incorrecto*.
**Diálogo (≈40 s):**
> “Si junto todo: la IA **acelera producir**, pero **no garantiza que esté bien**. Lo que hace es **mudar el cuello de botella**: ya no cuesta escribir el código, cuesta **verificar** que hace lo que tiene que hacer. Y acá la bomba: ya en 2015 se mostró que la mayoría del código que ‘pasa los tests’… **igual es incorrecto**. Pasar los tests no es estar bien. Entonces la pregunta del millón: si verificar es el nuevo cuello de botella, **¿por qué no lo automatizamos también?** Y la respuesta no es de ingeniería. Es de **matemática**. Y de eso les va a hablar mi compañero.”
**(Pase a Bloque 3 — teoría.)**

---

# 🟢 BLOQUE 4 — Nuevo rol, empleo y conclusión
**Arco:** el nuevo rol → tres trabajos que nacen → la buena noticia y la trampa → la puerta junior → hasta los profetas conceden → se vacía el medio → la paradoja esperanzadora.

---

### Slide 1 · “El ingeniero no desaparece: sube de piso”
**En pantalla:** una flecha de **ESCRIBIR CÓDIGO → ESPECIFICAR · DISEÑAR · VALIDAR · DECIDIR**. Escalera en la esquina (peldaño 1 encendido).
**Diálogo (≈45 s):**
> “Si la teoría que vieron deja un núcleo humano, la pregunta es: ¿en qué se convierte el ingeniero? No desaparece: **se corre de actividad**. Pasa de escribir código línea por línea a **especificar** qué hay que construir, **diseñar** e integrar, **validar** lo que la máquina produjo y **decidir** con qué criterios. Y fíjense que cada una de esas tareas es, justamente, **una de las barreras matemáticas**: validar choca con Turing y Rice; decidir, con P vs NP; traducir la intención a una spec, con Chomsky. El nuevo rol es, literalmente, **pararse sobre los límites de la máquina**.”
**Transición:** “Eso, en el mercado, abre tres puestos concretos.”

---

### Slide 2 · “Tres trabajos que la IA hace nacer”
**En pantalla:** tres íconos: **ARQUITECTO** (el qué) · **AUDITOR** (valida a la IA) · **RESPONSABLE** (firma y rinde cuentas). Cita: *Brooks: “lo más difícil es decidir qué construir.”*
**Diálogo (≈45 s):**
> “Tres perfiles que crecen. El **arquitecto**, que decide *qué* construir y cómo encajan las piezas. El **auditor**, que **valida lo que la IA escupe** —porque alguien tiene que hacerlo—. Y el **responsable**, el que firma y rinde cuentas cuando algo sale mal. Brooks ya lo había dicho en el ’87: ‘**lo más difícil de construir software es decidir con precisión qué construir**’. La IA ataca la parte mecánica; **decidir qué y para quién sigue siendo humano**. Naur lo llevó más lejos: el producto real de programar es una **teoría del problema** que vive en la cabeza del equipo… y eso ningún archivo lo captura.”
**Transición:** “Ahora, la pregunta que todos se hacen: ¿esto destruye empleo?”

---

### Slide 3 · “La buena noticia (y la trampa de Jevons)”
**En pantalla:** **+78 M** (saldo neto de empleo a 2030, WEF) grande. Abajo: *desarrollador +15 % / programador −6 % (BLS)*. Ícono cajero automático.
**Diálogo (≈50 s):**
> “La foto macro es, sorprendentemente, **positiva**. El Foro Económico Mundial proyecta a 2030: 92 millones de empleos desplazados, **170 millones creados**, saldo neto **+78 millones**. Y miren este matiz fino de la Oficina de Estadísticas de EE. UU.: ‘**desarrollador de software**’ crece **15 %**, mientras ‘**programador**’ a secas **cae 6 %**. Se automatiza la **tarea** de codificar, no la **profesión** de diseñar. ¿Por qué crecería? Por la **paradoja de Jevons**: cuando algo se abarata, se usa más. Pasó con los cajeros automáticos: abarataron la sucursal, los bancos abrieron más sucursales, y **hubo más cajeros durante 20 años**. Ahora, ojo…”
**Transición:** “…porque ese promedio alegre esconde a un perdedor muy concreto.”

---

### Slide 4 · “La puerta de entrada se está cerrando”
**En pantalla:** **−65 % / −76 %** (contratación junior, big tech / startups) en rojo grande. Pos-it: *⚠ ¿IA o fin del crédito barato?*
**Diálogo (≈50 s):**
> “Acá es donde **no es color de rosa**. La contratación de recién recibidos cayó **65 %** en las grandes tecnológicas y **76 %** en las startups respecto de 2019. Stanford: el empleo de los más jóvenes, 22 a 25 años, en las ocupaciones expuestas a la IA, cayó entre 13 y 16 %, mientras los experimentados **ni se movieron**. Y la paradoja más cruel: Brynjolfsson mostró que **la IA ayuda MÁS al novato** —le sube la productividad un 34 %—… **pero el mercado se cierra justo para el novato**, porque la IA se come las tareas con las que el junior aprendía. Seamos honestos: parte de esto puede ser la IA y parte el fin del crédito barato post-2021. **Tendencia convergente, no prueba cerrada.** Pero la puerta, se estrecha.”
**Transición:** “¿Y qué dicen los que están construyendo esto? Lo interesante es en qué coinciden.”

---

### Slide 5 · “Hasta los profetas le reservan algo al humano”
**En pantalla:** cita de Amodei: *“90 % del código… pero el programador todavía tiene que especificar el diseño.”* Abajo, cita de Beck.
**Diálogo (≈50 s):**
> “El más optimista de todos, Dario Amodei, dijo que la IA escribiría el **90 % del código en meses**. Pero en la misma frase aclaró: ‘**el programador todavía tiene que especificar las decisiones de diseño**’. O sea, **el optimista máximo concede mi tesis**. Altman: ‘los expertos seguirán siendo mucho mejores que los novatos, **si adoptan las herramientas**’ —eso es polarización dicha por OpenAI—. Y mi cita favorita, de Kent Beck, leyenda del software: ‘**el 90 % de mis habilidades hoy vale cero dólares; el otro 10 % —criterio, diseño— vale mil veces más**’. Ahí está todo el argumento en una sola frase.”
**Transición:** “Y esa frase de Beck nos lleva a la tesis central.”

---

### Slide 6 · “Se vacía el medio: menos ingenieros, los mejores”
**En pantalla:** una curva que se **hunde en el centro** (forma de U): *menos ‘del montón’ · más PRO*. Escalera: **el peldaño del medio, vacío**.
**Diálogo (≈50 s):**
> “Mi tesis, en una imagen: **se vacía el medio**. El que solo **tecleaba código** queda expuesto, porque eso es justo lo que la IA hace barato. El que **sube en abstracción** —decide, valida, responde— vale más que nunca. Resultado: **menos ingenieros ‘del montón’ y más ingenieros PRO**, con una prima salarial para el que trabaja CON la IA. Y acá conecto con la plata del bloque 2: si hoy la IA está **subsidiada**, cuando el precio suba a costo real, **el valor se lo va a llevar el que extrae ventaja de verdad**, no el que abarata el tecleo. El ajuste no devuelve la profesión vieja: **acelera la depuración**. ¿Y por qué un humano y no otra IA validando? Porque alguien tiene que **RESPONDER**. Asumir la responsabilidad es una categoría jurídica y moral, **no un cálculo**.”
**Transición:** “Cierro con la paradoja que, para mí, es la más linda de todo el trabajo.”

---

### Slide 7 · “La paradoja esperanzadora”
**En pantalla:** cita final a pantalla completa, fondo negro: **“La IA no anuncia el fin del ingeniero: redefine quién lo es.”**
**Diálogo (≈40 s):**
> “La paradoja de fondo es esperanzadora: **cuanto más poderosa se vuelve la automatización, más vale el juicio humano** que decide qué automatizar, cómo validarlo y para qué. No estamos ante el fin del ingeniero. Estamos ante un ingeniero que será **menos escriba y más arquitecto, auditor y responsable** de sistemas que ni él ni la máquina entienden del todo. Por eso lo cierro así: **la IA no anuncia el fin del ingeniero… redefine quién lo es.** Gracias.”

---

## 🎒 Mochila de emergencia (si te repreguntan)
- **“¿No es esto puro optimismo?”** → No: te muestro la puerta junior cerrándose (−65/−76 %) y digo que parte puede ser el fin del crédito barato. *Tendencia, no prueba.*
- **“El 75 % de Google / 30 % de Microsoft”** → son **auto-reportados por las empresas**: decí “según…”. Y Pichai aclaró “aprobado por ingenieros”.
- **“¿Y si es una burbuja y se cae todo?”** → Reconocelo (FMI, MIT 95 %, Burry apostó >US$1.000 M contra Nvidia/Palantir) **pero** balanceá: ingresos reales, financiado con caja, no es 2000. Y un ajuste **refuerza** la tesis, no la rompe.
- **NO uses:** cita de Tom DeMarco (no la tenemos), ni una “prima salarial de X %” inventada. El “the hottest new programming language is English” es un **tweet de 2023**, no del talk de Karpathy.
