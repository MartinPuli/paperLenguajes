# Guion de debate — ¿El ingeniero informático va a dejar de existir o va a cambiar de rol?

**Exposición a dos voces · TP Final — Lenguajes Formales y Teoría de la Computación**
Universidad del CEMA · Pulitano & Silva · Prof. Mario Moreno

---

## Cómo se juega

| | Postura | Quién |
|---|---|---|
| 🟢 **CAMBIO** | "el ingeniero no desaparece, cambia de rol" *(abre)* | **Martín** |
| 🔴 **EXTINCIÓN** | "el ingeniero va a dejar de existir" | **Nicolás** |

> Pueden invertir los papeles si prefieren. Duración objetivo: **~10 min**.

**Reglas de actuación**
- 🔴 ataca fuerte y **se cree sus golpes** (si no, no hay tensión). 🟢 nunca se pone nervioso: contesta tranquilo y da vuelta cada golpe.
- La teoría (**Choque 5**) inclina la cancha. De ahí en adelante 🔴 ya pelea para "salvar algo".
- Al final **se encuentran en el medio**: los dos conceden algo y dejan la conclusión clara.
- Las marcas **[al público]** son apartes cortos para guiar al que escucha (se dicen mirando a la clase, no al rival).

---

## Apertura — 🟢 (Martín)

> "Buenas. La pregunta del trabajo es una sola: en los próximos diez años, ¿el ingeniero informático va a **desaparecer** o va a **cambiar**? Nicolás va a defender que desaparece. Yo voy a sostener la hipótesis del paper: el ingeniero **no va a ser reemplazado por la IA, pero su rol se va a transformar**. Va a dejar de centrarse en escribir código —la ejecución técnica— para pasar a **especificar qué construir, integrar, validar y supervisar** sistemas. Menos operativo, más estratégico. Esa es la cancha. Dale, Nico, atacá."

---

## Choque 1 — La velocidad del avance

🔴 **Nicolás:**
> "Te ataco con el dato más fuerte que hay. A la IA le dan problemas **reales** de programación, de proyectos de verdad. Hace dos años resolvía **1 de cada 7**. Hoy resuelve **más de 9 de cada 10**. A esa velocidad, en dos años hace todo sola. No hay 'transformación' que valga: sobra el ingeniero."

🟢 **Martín:**
> "Te concedo la velocidad, es real, no la discuto. Pero fijate **qué** mide esa prueba: resolver problemas que **ya están planteados**. Y lo difícil de este laburo nunca fue resolver el problema. Es **decidir qué problema vale la pena resolver**, y después revisar que la solución no rompa otra cosa. Eso el test no lo mide: le das el examen ya escrito; no le das la pregunta de qué examen tomar."

> **[al público]** "Quédense con dos cosas: la pregunta —¿desaparece o cambia?— y qué defiende cada uno."

---

## Choque 2 — "Hasta los dueños de la IA lo dicen"

🔴 **Nicolás:**
> "No es opinión mía. Los jefes de Google y de Microsoft ya dicen que la IA escribe entre **un cuarto y un tercio** de su código. Y el CEO de Anthropic, una de las líderes, predijo que iba a escribir el **90%**."

🟢 **Martín:**
> "Gracias por traer esa cita, porque me la dejaste servida. ¿Sabés cómo termina la frase del 90%? *'…pero el programador todavía tiene que especificar las decisiones generales de diseño'*. O sea: el tipo **más optimista del planeta** igual deja al humano decidiendo qué construir. Eso no es desaparecer: es **cambiar de tarea**. Y te tiro el dato de hoy: adentro de Anthropic ya es casi el 100%… pero en la industria sigue lejísimos. Una cosa es generar código; otra es saber **qué** código hace falta."

> **[al público]** "Este es el momento *'me hiciste el favor citándolo'*."

---

## Choque 3 — "Te hace ir más rápido"

🔴 **Nicolás:**
> "Números fríos: con IA, los programadores hicieron una tarea **56% más rápido**. Si cada uno rinde casi el doble, hacen falta menos. Es matemática de costos."

🟢 **Martín:**
> "Te traigo otro estudio, pero mirá la diferencia. A programadores **expertos, en sus propios proyectos reales**, la IA los hizo ir un **19% más LENTO**. Y lo mejor: ellos estaban **convencidos de que habían ido más rápido**. Creían +20%, en realidad −19%. La IA es brillante para *hacerte sentir* productivo —que no es lo mismo que serlo—. El +56% fue en una tarea de juguete, aislada. En el mundo real, con código que ya existe, se da vuelta."

> **[al público]** "El dato 'creían que iban rápido pero iban lento' es contraintuitivo: es el que se acuerdan."

---

## Choque 4 — Calidad y seguridad

🟢 **Martín** *(pasa al ataque):*
> "Ahora ataco yo. Existe el **'problema del 70%'**: la IA te hace rápido el 70% de un programa. Pero el 30% que falta —los errores escondidos, los casos raros, que ande en producción— sigue necesitando a alguien que sepa. Y en seguridad es peor: el código que sugiere la IA viene con **agujeros conocidos 4 de cada 10 veces**."

🔴 **Nicolás:**
> "Bueno, pero eso se va a arreglar con mejores modelos. Es cuestión de tiempo."

🟢 **Martín** *(sonríe):*
> "Ahí quería que cayeras."

> **[al público]** "Hizo la jugada obvia —'ya lo van a mejorar'— y me sirvió el golpe ganador en bandeja."

---

## Choque 5 — La matemática 🎯 *(clímax)*

🟢 **Martín:**
> "Porque hay cosas que **no se arreglan nunca**. No porque falte tecnología: porque son **imposibles, probadas con matemática**, antes de que existiera la primera computadora.
>
> **Uno.** En 1936, Turing demostró que **ningún programa puede revisar a otro y garantizar, en general, que está bien**. No es que no se inventó todavía: es imposible, como un triángulo de dos lados. Traducido: la máquina puede escribir código, pero **no puede garantizar que su propio código esté bien**. Siempre va a hacer falta un humano que valide y **se haga responsable**.
>
> **Dos.** Las IA 'alucinan' —inventan cosas con total seguridad— y está demostrado que eso es **inevitable**, no un bug que se parchea. Una IA no puede revisarse a sí misma: necesita a alguien **afuera** del sistema. Ese alguien es el ingeniero.
>
> **Tres** —y conecta justo con esta materia—: el código es un idioma **exacto**, sin doble sentido; lo que vos le pedís en español es **ambiguo**, lleno de sobreentendidos. El ingeniero es el **traductor** entre lo que el humano quiso decir y lo que la máquina entiende."

🔴 **Nicolás** *(cede):*
> "…Contra un teorema no puedo discutir. Te lo concedo."

> **[al público]** "Acá se inclina el debate. No es opinión ni 'esperemos a ver': es matemática de hace casi 100 años que **ninguna actualización va a derogar**."

---

## Choque 6 — Contraataque final: "ya están echando gente"

🔴 **Nicolás** *(se recupera, pega donde duele):*
> "Te compro la teoría. Pero la teoría no paga el alquiler. **Ya hay menos trabajo real.** El empleo de programadores jóvenes, de 22 a 25 años, cayó cerca del **20% desde 2024**. El desempleo de los recién recibidos en Computación está **por encima del de Historia del Arte**. Si los pibes no entran, la profesión se seca desde abajo. ¿De qué 'arquitecto' me hablás si nadie llega a serlo?"

🟢 **Martín** *(reconoce y reencuadra):*
> "Ese es tu mejor golpe, y te lo reconozco. Pero mirá el mismo dato de cerca. El puesto de 'programador' —el que **solo teclea** código— se achica un 6%. El de 'desarrollador de software' —el que **diseña y decide**— **crece un 15%**. No sobran ingenieros: cambió **qué se les pide**. ¿Te suena de algo? Los **cajeros automáticos**. Todos juraban que dejaban sin laburo a los cajeros. Pero abrir una sucursal salió más barato, los bancos abrieron **más** sucursales… y terminó habiendo **más** empleados, haciendo otra cosa. Eso sí, no te lo vendo de color: la transición es **brutal y desigual**. La base se desploma, la cima se concentra. La profesión no se extingue: **se polariza**."

> **[al público]** "La del cajero la entiende cualquiera y es contraintuitiva. Es el *'ahhh, claro'*."

---

## El cierre — síntesis (los dos en el medio)

🔴 **Nicolás:**
> "Te concedo lo principal: el ingeniero que **solo** teclea código, ese sí se extingue. Me equivoqué de víctima: muere la **tarea**, no la **profesión**."

🟢 **Martín:**
> "Y yo te concedo lo tuyo: no es un ascenso gratis ni para todos. La profesión sube de nivel, pero el de abajo la pasa mal. El centro se corre de escribir código línea por línea a **especificar qué construir, validar que esté bien y hacerse responsable** de sistemas cada vez más autónomos. **De obrero a arquitecto.** Y no es una corazonada: lo respalda la **historia**, lo matiza la **evidencia** y, sobre todo, lo demuestra la **teoría**."

**Remate a dúo** *(una frase cada uno, mirando al público):*

🔴 **Nicolás:**
> "Como dijo Booch: *'tus herramientas cambian, pero tus problemas no'*."

🟢 **Martín:**
> "Y la paradoja final: **cuanto más poderosa se vuelve la máquina, más vale el humano que decide qué hacer con ella.** Por eso el mensaje no es 'esfuércense más'. Es **esfuércense inteligentemente, y *dónde***: corran hacia el juicio que ninguna máquina puede tener sola. La competencia no es contra la máquina: es por el **lugar escaso** desde el cual se la maneja. Gracias."

---

## Chuleta (mapa rápido)

| Choque | Tema | Dato clave | Quién pega |
|--------|------|------------|------------|
| 1 | Planteo + velocidad | De 1/7 a +9/10 en SWE-bench | Abre 🟢, ataca 🔴 |
| 2 | "Los dueños lo dicen" | 90% del código… "pero el humano decide el diseño" | 🔴 → 🟢 lo devuelve |
| 3 | Productividad | +56% en tarea simple vs −19% en expertos reales | 🔴 → 🟢 |
| 4 | Calidad y seguridad | Problema del 70%; 4 de cada 10 con vulnerabilidades | 🟢 ataca |
| 5 | La matemática (clímax) | Imposible verificar; alucinación inevitable | 🟢 gana |
| 6 | Empleo | "Programador" −6% vs "desarrollador" +15%; cajeros | 🔴 pega, 🟢 reencuadra |
| Cierre | Síntesis | Muere la tarea, no la profesión: de obrero a arquitecto | Ambos |

---

## Datos y fuentes (por si los aprietan en preguntas)

- **SWE-bench:** ~14 % (2024) → ~95 % (2026, Claude Fable 5); el benchmark se saturó — *Anthropic (2026)*.
- **Amodei 90 %** + *"el programador todavía debe especificar el diseño"* — *Council on Foreign Relations (2025)*.
- **Productividad:** +55,8 % en tarea acotada *(Peng et al., 2023)* vs −19 % en expertos *(METR, 2025)*.
- **Problema del 70 %** *(Osmani, 2024)*; **40 %** de sugerencias con vulnerabilidades *(Pearce et al., 2022)*.
- **Indecidibilidad / Rice** *(Turing, 1936)*; **alucinación inevitable** *(Xu et al., 2024)*; **jerarquía de Chomsky** *(1956)*.
- **Empleo:** junior −20 % *(Stanford HAI, 2026)*; "programador" −6 % vs "desarrollador" +15 % *(Bureau of Labor Statistics, 2025)*; cajeros *(Bessen, 2015)*.

> Todas las cifras y citas están desarrolladas y referenciadas en el paper (`paper.md` / PDF).
