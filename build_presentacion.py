#!/usr/bin/env python3
"""Genera presentacion_4bloques.html: teleprompter en vivo para la exposición
oral de 20 min dividida en 4 bloques (~5 min c/u), dos personas (A: bloques 1 y 3,
B: bloques 2 y 4). Embebe las 6 figuras del paper como data-URI (archivo autónomo)."""
import base64, json, os

FIGS = {
    "fig1": "figuras/fig1_swebench.png",
    "fig2": "figuras/fig2_productividad.png",
    "fig3": "figuras/fig3_chomsky.png",
    "fig4": "figuras/fig4_empleo.png",
    "fig5": "figuras/fig5_wef.png",
    "fig6": "figuras/fig6_seguridad.png",
}
IMG = {}
for k, p in FIGS.items():
    with open(p, "rb") as f:
        IMG[k] = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

HTML = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>El rol del ingeniero informático — Presentación (20 min · 4 bloques)</title>
<style>
  :root{
    --bg:#0d1117; --bg2:#161b22; --card:#1b232e; --card2:#202b38;
    --ink:#e6edf3; --muted:#9aa7b4; --line:#2a3441;
    --a:#3b82f6; --a2:#1d4ed8;            /* Persona A — azul */
    --b:#22c55e; --b2:#15803d;            /* Persona B — verde */
    --acc:#e8743b;                         /* naranja acento */
    --gold:#f4c95d;
  }
  *{box-sizing:border-box}
  html,body{margin:0;height:100%}
  body{background:radial-gradient(1200px 700px at 50% -10%, #182230 0%, var(--bg) 60%);
       color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       height:100vh; overflow:hidden; display:flex; flex-direction:column}
  /* top bar */
  .top{display:flex; align-items:center; gap:14px; padding:10px 18px; border-bottom:1px solid var(--line); background:rgba(13,17,23,.6)}
  .brand{font-weight:800; letter-spacing:.3px; font-size:14px; color:#c8d3df}
  .brand small{color:var(--muted); font-weight:600}
  .dots{display:flex; gap:7px; margin-left:6px}
  .dots .d{display:flex; align-items:center; gap:6px; font-size:11.5px; color:var(--muted); padding:3px 9px; border:1px solid var(--line); border-radius:999px; background:var(--bg2)}
  .dots .d .pip{width:9px;height:9px;border-radius:50%;background:#3a4658}
  .dots .d.a .pip{background:var(--a)} .dots .d.b .pip{background:var(--b)}
  .dots .d.on{color:var(--ink); border-color:#3d4b5c; box-shadow:0 0 0 1px rgba(255,255,255,.04) inset}
  .dots .d.on.a{border-color:var(--a)} .dots .d.on.b{border-color:var(--b)}
  .spacer{flex:1}
  .timer{font-variant-numeric:tabular-nums; font-weight:800; padding:6px 13px; border-radius:999px; border:1px solid var(--line); background:var(--bg2); cursor:pointer; font-size:15px}
  .timer.warn{color:var(--gold); border-color:#6a5a1e} .timer.over{color:#ff6b5e; border-color:#7a2a24}
  .help{font-size:11px; color:var(--muted); white-space:nowrap}
  /* stage */
  .stage{flex:1; position:relative; display:flex; align-items:center; justify-content:center; padding:30px; transition:box-shadow .25s}
  .stage.side-a{box-shadow:inset 7px 0 60px -30px var(--a)}
  .stage.side-b{box-shadow:inset 7px 0 60px -30px var(--b)}
  .card{width:min(1080px,94vw); max-height:82vh; overflow:auto; background:linear-gradient(180deg,var(--card),var(--card2)); border:1px solid var(--line);
        border-radius:20px; padding:40px 48px; box-shadow:0 24px 70px -30px rgba(0,0,0,.8)}
  .who{display:inline-flex; align-items:center; gap:8px; font-weight:800; font-size:13.5px; letter-spacing:.4px; text-transform:uppercase; padding:5px 12px; border-radius:999px; margin-bottom:18px}
  .who.a{color:#cfe0ff; background:rgba(59,130,246,.14); border:1px solid rgba(59,130,246,.4)}
  .who.b{color:#c7f4d6; background:rgba(34,197,94,.13); border:1px solid rgba(34,197,94,.4)}
  h1{font-size:40px; line-height:1.12; margin:.1em 0 .25em}
  h2{font-size:30px; line-height:1.18; margin:.1em 0 .55em}
  .lead{font-size:20px; color:#cdd8e4; margin-bottom:10px}
  ul.points{list-style:none; padding:0; margin:.2em 0 0}
  ul.points li{position:relative; padding:10px 6px 10px 30px; font-size:20px; line-height:1.4; border-top:1px solid rgba(255,255,255,.05)}
  ul.points li:first-child{border-top:none}
  ul.points li::before{content:"▸"; position:absolute; left:4px; top:11px; color:var(--acc); font-weight:900}
  b{color:#fff}
  .who.a ~ * b{}
  /* cover */
  .cover h1{font-size:44px; margin-top:6px}
  .cover .sub{color:var(--acc); font-weight:700; font-size:18px; margin:6px 0 22px}
  .vs{display:flex; gap:14px; align-items:stretch; margin:18px 0}
  .vs .p{flex:1; border:1px solid var(--line); border-radius:14px; padding:16px 18px; background:var(--bg2)}
  .vs .p.a{border-color:rgba(59,130,246,.5)} .vs .p.b{border-color:rgba(34,197,94,.5)}
  .vs .p .nm{font-weight:800; font-size:18px} .vs .p small{display:block; color:var(--muted); margin-top:3px; font-size:13px}
  .meta{color:var(--muted); font-size:14px; line-height:1.7; margin-top:14px}
  .meta b{color:#d7e0ea}
  /* block title */
  .blockcard{text-align:center}
  .blockcard .num{font-size:120px; font-weight:900; line-height:.9; background:linear-gradient(180deg,#fff,#7f8ea0); -webkit-background-clip:text; background-clip:text; color:transparent}
  .blockcard .sec{color:var(--muted); font-size:15px; letter-spacing:.6px; text-transform:uppercase; margin:10px 0 4px}
  .blockcard h1{font-size:38px}
  .blockcard .budget{display:inline-block; margin-top:16px; font-size:15px; font-weight:800; letter-spacing:1px; color:#dbe4ee; border:1px dashed #4a5868; padding:7px 16px; border-radius:999px}
  /* figure */
  .figwrap{background:#fff; border-radius:14px; padding:14px; text-align:center; margin:4px 0 12px}
  .figwrap img{max-width:100%; max-height:54vh; display:block; margin:0 auto}
  .cap{color:var(--muted); font-size:13.5px; font-style:italic; margin-bottom:6px}
  .say{font-size:16.5px; color:#d9e3ee; background:rgba(232,116,59,.1); border-left:3px solid var(--acc); padding:10px 14px; border-radius:0 10px 10px 0}
  .say b{color:#ffd9c4}
  /* puente */
  .puente{text-align:center}
  .puente .tag{font-size:13px; letter-spacing:2px; text-transform:uppercase; color:var(--acc); font-weight:800}
  .puente .line{font-size:27px; line-height:1.35; margin:18px auto; max-width:880px; color:#eef3f8}
  .puente .hand{color:var(--muted); font-size:15px}
  .puente .hand b{color:#d7e0ea}
  /* quote/conclusión */
  .quote{text-align:center}
  .quote .lead{font-size:23px}
  .quote blockquote{font-size:30px; line-height:1.3; font-weight:700; margin:22px auto; max-width:920px; color:#fff;
        border:none; position:relative; padding:0 18px}
  .quote blockquote::before{content:"“"; color:var(--gold); font-size:54px; line-height:0; vertical-align:-14px; margin-right:6px}
  .quote blockquote::after{content:"”"; color:var(--gold); font-size:54px; line-height:0; vertical-align:-30px; margin-left:4px}
  .quote .foot{color:var(--muted); font-size:16px; margin-top:8px}
  /* bottom */
  .bottom{border-top:1px solid var(--line); padding:8px 18px; display:flex; align-items:center; gap:14px; background:rgba(13,17,23,.6)}
  .progress{flex:1; height:8px; background:#10161e; border-radius:999px; position:relative; overflow:visible}
  .fill{position:absolute; left:0; top:0; bottom:0; background:linear-gradient(90deg,var(--a),var(--b)); border-radius:999px; width:0}
  .marker{position:absolute; top:50%; transform:translate(-50%,-50%); font-size:18px; transition:left .2s}
  .count{font-variant-numeric:tabular-nums; color:var(--muted); font-size:13px; min-width:64px; text-align:right}
  .next{color:var(--muted); font-size:13px; max-width:46%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
  .next b{color:#cdd8e4}
  kbd{background:#0b0f14; border:1px solid var(--line); border-bottom-width:2px; border-radius:6px; padding:1px 7px; font-size:12px; color:#cdd8e4}
  /* índice */
  .toc{position:fixed; inset:0; background:rgba(5,8,12,.82); backdrop-filter:blur(4px); display:none; align-items:center; justify-content:center; z-index:30}
  .toc.open{display:flex}
  .tocbox{background:var(--bg2); border:1px solid var(--line); border-radius:16px; padding:22px; width:min(680px,92vw)}
  .tocbox h3{margin:0 0 12px; font-size:15px; color:var(--muted); letter-spacing:1px; text-transform:uppercase}
  .toc .item{display:flex; gap:12px; align-items:center; padding:13px 14px; border:1px solid var(--line); border-radius:11px; margin-bottom:9px; cursor:pointer}
  .toc .item:hover{border-color:#3d4b5c; background:var(--card)}
  .toc .item .n{font-weight:900; font-size:20px; width:30px; text-align:center}
  .toc .item.a .n{color:var(--a)} .toc .item.b .n{color:var(--b)}
  .toc .item .k{font-weight:700} .toc .item small{display:block; color:var(--muted); font-weight:500; margin-top:2px}
  @media (max-width:640px){ h1{font-size:30px} h2{font-size:23px} ul.points li{font-size:17px} .card{padding:26px 22px} .help{display:none} }
</style>
</head>
<body>
  <div class="top">
    <div class="brand">El rol del ingeniero informático <small>· 20 min · 4 bloques</small></div>
    <div class="dots" id="dots"></div>
    <div class="spacer"></div>
    <div class="help"><kbd>←</kbd> <kbd>→</kbd> navegar · <kbd>T</kbd> timer · <kbd>R</kbd> reset · <kbd>M</kbd> índice · <kbd>F</kbd> pantalla</div>
    <div class="timer" id="btimer" title="Tiempo transcurrido en el bloque actual" style="font-size:13px;opacity:.9">—</div>
    <div class="timer" id="timer" title="Click para iniciar / pausar (total)">20:00</div>
  </div>

  <div class="stage" id="stage"><div class="card" id="card"></div></div>

  <div class="bottom">
    <div class="next" id="next"></div>
    <div class="progress"><div class="fill" id="fill"></div><div class="marker" id="marker">①</div></div>
    <div class="count" id="count"></div>
  </div>

  <div class="toc" id="toc"><div class="tocbox"><h3>Índice — saltar a un bloque</h3><div id="tocGrid"></div></div></div>

<script>
const IMG = __IMG_JSON__;
const PA = '<span class="who a">🔵 Persona A</span>', PB = '<span class="who b">🟢 Persona B</span>';

const S = [
 {kind:'cover'},

 // ───────────────────────── BLOQUE 1 — Persona A
 {kind:'block', blk:1, who:'a', num:'1', sec:'Introducción (I) · Escalera de abstracción (II)', kicker:'El ingeniero no desaparece, cambia', min:'5:00', acc:'al terminar ≈ 5:00'},
 {kind:'point', blk:1, who:'a', t:'La pregunta que engancha', b:[
   '«¿La inteligencia artificial va a <b>reemplazar</b> a los programadores?»',
   'Muchos referentes dicen que sí: el CEO de Anthropic llegó a predecir que la IA escribiría el <b>90 %</b> del código.',
   'La respuesta de este trabajo: <b>no… pero el trabajo se transforma</b>.']},
 {kind:'point', blk:1, who:'a', t:'La hipótesis del trabajo', b:[
   'El ingeniero <b>no será reemplazado</b>; su rol se <b>desplaza</b>.',
   'Deja de «escribir código a mano» y pasa a <b>decidir qué construir, diseñarlo, validarlo y controlarlo</b>.',
   'Matiz honesto: el oficio se <b>polariza</b> — crecen los roles de <b>arriba</b> (diseñar/decidir) y se achica la <b>base</b> (codificar rutinario), vaciando el medio.']},
 {kind:'point', blk:1, who:'a', t:'La escalera de abstracción', b:[
   'Lenguaje de máquina (0 y 1) → lenguajes de alto nivel → compiladores → frameworks y nube → <b>IA</b>.',
   'Cada vez que se automatizó lo tedioso, el ingeniero <b>subió un escalón</b>, no desapareció.',
   'Ya se anunció su «fin» con el COBOL, los lenguajes de 4.ª generación y el «no-code». Nunca pasó.']},
 {kind:'point', blk:1, who:'a', t:'La idea para fijar', b:[
   '<b>La IA es el escalón más nuevo de una escalera muy larga.</b>',
   'No es la excepción a la historia: es su continuación.']},
 {kind:'point', blk:1, who:'a', t:'¿Y hoy? La IA pegó un salto enorme', b:[
   'En un examen de problemas <b>reales</b> de programación pasó de <b>1 de cada 7</b> a <b>más de 9 de cada 10</b> en ~2 años.',
   'En <b>Microsoft</b> ya escribe el <b>20–30 %</b> del código; en <b>Google</b>, más de <b>una cuarta parte</b>.',
   'Parece que esta vez sí nos reemplaza… <b>¿o no?</b> Veámoslo en detalle.']},
 {kind:'puente', blk:1, from:'a', to:'b', t:'«Esto ya pasó muchas veces antes, y nunca eliminó la profesión. Veamos en detalle qué puede —y qué no— hacer la IA hoy.»'},

 // ───────────────────────── BLOQUE 2 — Persona B
 {kind:'block', blk:2, who:'b', num:'2', sec:'El presente (III): IA agéntica, 2021–2026', kicker:'Qué puede y qué NO puede hacer la IA hoy', min:'5:00', acc:'al terminar ≈ 10:00'},
 {kind:'fig', blk:2, who:'b', img:'fig1', t:'La capacidad para programar se disparó', cap:'SWE-bench Verified — un test estándar de la industria. Hacia 2026 el examen se satura.', say:'Retomá el dato de A y mostrá la curva, pero aclará: ese examen lo escribieron <b>ellos</b> y mide problemas <b>ya planteados</b>. Falta saber qué quería el cliente.'},
 {kind:'point', blk:2, who:'b', t:'Pero no es mágica: el contexto lo cambia todo', b:[
   'En una tarea <b>acotada</b>: <b>+55,8 %</b> de velocidad.',
   'Expertos en <b>sus propios repos</b>: <b>−19 %</b> (más LENTOS)… y encima <b>creían</b> que iban más rápido.',
   'La <b>sensación engaña</b>: la IA amplifica al que sabe, pero estorba en el trabajo experto.']},
 {kind:'fig', blk:2, who:'b', img:'fig2', t:'Productividad: laboratorio vs. realidad', cap:'Peng et al. (2023) vs. METR (2025). No comparables: tarea y experiencia distintas.', say:'El contraste <b>+56 % / −19 %</b> es el corazón del bloque. No te quedes solo con el número bueno.'},
 {kind:'point', blk:2, who:'b', t:'El «problema del 70 %»', b:[
   'La IA hace rápido el <b>70 % fácil</b>; el <b>30 % difícil</b> (detalles, casos raros, seguridad) sigue necesitando a alguien que <b>sepa</b>.',
   'Y su código suele ser <b>inseguro</b>: cerca del <b>40 %</b> trae fallas de seguridad conocidas.']},
 {kind:'fig', blk:2, who:'b', img:'fig6', t:'La IA acelera, pero la verificación sigue siendo humana', cap:'Pearce et al. (2022); Veracode (2025); Spracklen et al. (2025).', say:'Y «alucina» hasta las dependencias: ~<b>1 de cada 5</b> paquetes que recomienda <b>no existe</b> (riesgo de malware). Cerrá: velocidad <b>sin garantía</b>; alguien tiene que revisar.'},
 {kind:'puente', blk:2, from:'b', to:'a', t:'«Entonces la IA escribe rápido, pero alguien tiene que revisar. ¿Por qué una máquina no puede revisarse a sí misma? Eso lo explica la matemática.»'},

 // ───────────────────────── BLOQUE 3 — Persona A
 {kind:'block', blk:3, who:'a', num:'3', sec:'Marco teórico (IV): los límites computacionales', kicker:'Por qué hay cosas que NINGUNA máquina podrá hacer', min:'5:00', acc:'al terminar ≈ 15:00'},
 {kind:'point', blk:3, who:'a', t:'La idea central (lo más teórico)', b:[
   'No es que la IA «todavía no pueda»: hay <b>límites matemáticos demostrados</b> que dicen que <b>NUNCA</b> podrá.',
   'Tres límites, probados antes de que existiera la primera computadora. Esto es lo que conecta con la materia.']},
 {kind:'point', blk:3, who:'a', t:'① No se puede verificar todo · Turing y Rice', b:[
   '<b>Indecidibilidad</b> (Turing, 1936): no existe ni puede existir un programa que decida, para <b>todo</b> programa, si <b>termina</b> —el <b>problema de la parada</b>—.',
   '<b>Rice</b> lo generaliza: tampoco se puede decidir <b>ninguna</b> propiedad del comportamiento, incluido «¿cumple lo que debe?».',
   '→ Siempre hará falta un <b>humano que valide y se haga responsable</b>. Y como además la IA <b>alucina</b> —inventa con seguridad, y se demostró que es inevitable—, <b>no puede revisarse sola</b>.']},
 {kind:'point', blk:3, who:'a', t:'② Hay problemas imposibles de resolver rápido · P vs NP', b:[
   '<b>P</b> = se resuelve rápido; <b>NP</b> = la solución se <b>verifica</b> rápido, pero (se cree) no se <b>encuentra</b> rápido. Nadie probó que sean iguales… ni distintos.',
   'Muchos problemas de ingeniería no tienen una solución rápida y perfecta —ni la tendrán—.',
   'Alguien tiene que <b>decidir qué sacrificar</b> (velocidad, precisión, recursos): es un <b>criterio humano</b>, no un cálculo.']},
 {kind:'fig', blk:3, who:'a', img:'fig3', t:'③ Traducir lo humano a lo exacto · jerarquía de Chomsky', cap:'La jerarquía de Chomsky ordena los lenguajes por su poder; los transformers ≈ clase TC⁰.', say:'El humano habla <b>ambiguo</b>; la máquina, <b>exacto</b> — el ingeniero es el <b>traductor</b>. Dato fino: por su arquitectura (clase <b>TC⁰</b>), un transformer no puede ni chequear solo si unos <b>paréntesis están bien cerrados</b>; está <b>por debajo</b> de una computadora común. No «razona» como una máquina universal.'},
 {kind:'point', blk:3, who:'a', t:'Lo esencial es humano · Brooks y Naur', b:[
   '<b>Brooks</b>: la IA reduce la complejidad <b>accidental</b> (el código repetitivo); la <b>esencial</b> —decidir qué construir— es humana.',
   '<b>Naur</b>: programar es <b>construir una teoría</b> del sistema en la mente del equipo; el código es solo su <b>sombra</b>.',
   'La parte difícil no es teclear: es <b>entender y decidir</b>.']},
 {kind:'puente', blk:3, from:'a', to:'b', t:'«La parte más difícil no es escribir el código, es decidir qué construir. Y eso es profundamente humano.»'},

 // ───────────────────────── BLOQUE 4 — Persona B
 {kind:'block', blk:4, who:'b', num:'4', sec:'Nuevo rol (V) · Expertos (VI) · Límites (VII) · Conclusión (VIII)', kicker:'Cómo queda el nuevo ingeniero + Conclusión', min:'5:00', acc:'al terminar ≈ 20:00'},
 {kind:'point', blk:4, who:'b', t:'El ingeniero del futuro', b:[
   'Menos «escribir código»; más <b>especificar, diseñar, validar, supervisar y decidir</b>.',
   'El «<b>30 % difícil</b>» del bloque 2 se convierte en el <b>centro</b> de su trabajo.']},
 {kind:'fig', blk:4, who:'b', img:'fig4', t:'El empleo se recompone', cap:'BLS (2024–34); Stanford (2025). Crece «desarrollador», cae «programador» puro.', say:'Se automatiza <b>codificar</b>, no <b>diseñar y decidir</b>. A los más jóvenes les cuesta entrar → <b>polarización</b>.'},
 {kind:'point', blk:4, who:'b', t:'Un dato esperanzador (y su matiz)', b:[
   'Cuando algo se abarata, se <b>produce más</b> (paradoja de Jevons): los cajeros automáticos no eliminaron bancarios… abrieron <b>más sucursales</b>.',
   'Contrapeso honesto (leyendo a <b>Acemoglu</b>): si no se crea <b>tarea nueva</b>, la transición puede ser <b>dura y desigual</b>.']},
 {kind:'fig', blk:4, who:'b', img:'fig5', t:'Proyección global de empleo a 2030 (WEF)', cap:'World Economic Forum, Future of Jobs Report 2025.', say:'<b>170 M creados − 92 M desplazados = +78 M neto</b>. No es «cero gente»: es <b>otra</b> gente, en <b>otra</b> tarea.'},
 {kind:'point', blk:4, who:'b', t:'Qué dicen los expertos', b:[
   'Optimistas (Amodei, Altman) y cautos coinciden en algo: la IA <b>potencia al que sabe usarla</b>, no lo reemplaza.',
   'El mercado lo paga: los puestos que piden IA ofrecen <b>primas por encima del promedio</b>.',
   'Y es una <b>proyección a 10 años</b>: estimación fundada, no bola de cristal. Lo que no caduca es el <b>teorema</b>.']},
 {kind:'quote', blk:4, who:'b', lead:'El ingeniero no desaparece: se transforma en <b>arquitecto, auditor y responsable</b> de los sistemas. Lo resumimos en una frase:',
   q:'Cuanto más poderosa se vuelve la automatización, más valioso se vuelve el juicio humano que decide qué automatizar, cómo controlarlo y para qué.',
   foot:'(síntesis propia) — y así se cierra el círculo con la pregunta del Bloque 1.'},
];

const card=document.getElementById('card'), stage=document.getElementById('stage'),
      fill=document.getElementById('fill'), marker=document.getElementById('marker'),
      count=document.getElementById('count'), nextEl=document.getElementById('next'),
      dotsEl=document.getElementById('dots');
let i=0;
const strip=h=>(h||'').replace(/<[^>]+>/g,'');
const CIRC=['①','②','③','④'];

function blockMeta(b){ return {1:['a','Bloque 1'],2:['b','Bloque 2'],3:['a','Bloque 3'],4:['b','Bloque 4']}[b]||null; }

function render(){
  const s=S[i]; let h='', cls='card';
  if(s.kind==='cover'){
    cls='card cover';
    h=`<div class="who a" style="background:none;border:none;color:#8b98a8;letter-spacing:4px;padding-left:0">PRESENTACIÓN · 20 MIN</div>
       <h1>El rol del ingeniero informático en los próximos diez años</h1>
       <div class="sub">Automatización de la base, polarización del oficio y un núcleo humano irreductible</div>
       <div class="vs">
         <div class="p a"><div class="nm">🔵 Persona A</div><small>Bloques 1 y 3 · abre con la hipótesis</small></div>
         <div class="p b"><div class="nm">🟢 Persona B</div><small>Bloques 2 y 4 · cierra con la conclusión</small></div>
       </div>
       <div class="meta"><b>Materia:</b> Lenguajes Formales y Teoría de la Computación · <b>UCEMA</b> (3.er año, Ing. Informática)<br>
       <b>Profesor:</b> Mario Moreno &nbsp;·&nbsp; <b>Integrantes:</b> Martín Ezequiel Pulitano y Nicolás Silva<br>
       <span style="color:#8b98a8">4 bloques de ~5 min · <kbd>→</kbd> o click para empezar</span></div>`;
  } else if(s.kind==='block'){
    cls='card blockcard';
    h=`<div class="who ${s.who}">${s.who==='a'?'🔵 Persona A':'🟢 Persona B'}</div>
       <div class="num">${s.num}</div>
       <div class="sec">${s.sec}</div>
       <h1>${s.kicker}</h1>
       <div class="budget">⏱ objetivo ${s.min} &nbsp;·&nbsp; ${s.acc}</div>`;
  } else if(s.kind==='point'){
    cls='card';
    h=`<div class="who ${s.who}">${s.who==='a'?'🔵 Persona A':'🟢 Persona B'}</div>
       <h2>${s.t}</h2><ul class="points">${s.b.map(x=>`<li>${x}</li>`).join('')}</ul>`;
  } else if(s.kind==='fig'){
    cls='card';
    h=`<div class="who ${s.who}">${s.who==='a'?'🔵 Persona A':'🟢 Persona B'}</div>
       <h2>${s.t}</h2>
       <div class="figwrap"><img src="${IMG[s.img]}" alt="${s.t}"></div>
       <div class="cap">${s.cap}</div>
       <div class="say">🎙️ <b>Qué decir:</b> ${s.say}</div>`;
  } else if(s.kind==='puente'){
    cls='card puente';
    h=`<div class="tag">🔗 Puente</div>
       <div class="line">${s.t}</div>
       <div class="hand">Pasa la palabra: <b>${s.from==='a'?'🔵 Persona A':'🟢 Persona B'}</b> → <b>${s.to==='a'?'🔵 Persona A':'🟢 Persona B'}</b></div>`;
  } else if(s.kind==='quote'){
    cls='card quote';
    h=`<div class="who ${s.who}">${s.who==='a'?'🔵 Persona A':'🟢 Persona B'}</div>
       <div class="lead">${s.lead}</div>
       <blockquote>${s.q}</blockquote>
       <div class="foot">${s.foot}</div>`;
  }
  card.className=cls; card.innerHTML=h;
  stage.className = 'stage'+(s.who?(' side-'+s.who):'');
  count.textContent = `${i+1} / ${S.length}`;
  const pct = i/(S.length-1)*100;
  fill.style.width = pct+'%'; marker.style.left = pct+'%';
  // marcador = número del bloque actual (o bandera al final)
  marker.textContent = i===S.length-1 ? '🏁' : (s.blk?CIRC[s.blk-1]:'▶');
  // dots de bloque
  [...dotsEl.children].forEach((d,idx)=>{ d.classList.toggle('on', s.blk===idx+1); });
  // cronómetro por bloque: reinicia al entrar a un bloque nuevo
  if(s.blk && s.blk!==curBlk){ curBlk=s.blk; blkSecs=0; }
  if(!s.blk && i===0){ curBlk=null; blkSecs=0; }
  updateBTimer();
  // próximo
  const nx=S[i+1];
  if(nx){
    const lbl = nx.kind==='block'?('▸ Bloque '+nx.num+' — '+nx.kicker)
      : nx.kind==='puente'?'🔗 Puente'
      : nx.kind==='fig'?('📊 '+nx.t)
      : nx.kind==='quote'?'★ Conclusión'
      : (nx.who==='a'?'🔵 A':'🟢 B')+' · '+(nx.t||'');
    nextEl.innerHTML = `sigue → <b>${lbl}</b>`;
  } else nextEl.textContent = '— fin —';
}
function go(d){ i=Math.max(0,Math.min(S.length-1,i+d)); render(); }

/* cronómetro 20:00 (total) + cronómetro por bloque (objetivo 5:00) */
let secs=20*60, tHandle=null, running=false, blkSecs=0, curBlk=null;
const tEl=document.getElementById('timer'), btEl=document.getElementById('btimer');
function fmt(s){const m=Math.floor(Math.abs(s)/60),x=Math.abs(s)%60;return (s<0?'-':'')+m+':'+String(x).padStart(2,'0');}
function updateBTimer(){ if(!curBlk){ btEl.textContent='—'; btEl.classList.remove('warn','over'); return; }
  btEl.textContent='B'+curBlk+' '+fmt(blkSecs)+' / 5:00';
  btEl.classList.toggle('warn', blkSecs>=240 && blkSecs<300);
  btEl.classList.toggle('over', blkSecs>=300); }
function tick(){ secs--; tEl.textContent=fmt(secs);
  tEl.classList.toggle('warn', secs<=180 && secs>0); tEl.classList.toggle('over', secs<=0);
  if(curBlk){ blkSecs++; updateBTimer(); } }
function toggleTimer(){ if(running){clearInterval(tHandle);running=false;} else {tHandle=setInterval(tick,1000);running=true;} }
tEl.onclick=toggleTimer;

/* dots iniciales */
[1,2,3,4].forEach(b=>{ const m=blockMeta(b); const d=document.createElement('div');
  d.className='d '+m[0]; d.innerHTML=`<span class="pip"></span>${m[1]}`; dotsEl.appendChild(d); });

stage.addEventListener('click',()=>{ if(!running && i===0) toggleTimer(); go(1); });
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault(); if(!running&&i===0)toggleTimer(); go(1);}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(-1);}
  else if(e.key==='Home'){i=0;render();}
  else if(e.key==='End'){i=S.length-1;render();}
  else if(e.key.toLowerCase()==='f'){ if(!document.fullscreenElement){document.documentElement.requestFullscreen().catch(()=>{});} else document.exitFullscreen(); }
  else if(e.key.toLowerCase()==='t'){toggleTimer();}
  else if(e.key.toLowerCase()==='r'){clearInterval(tHandle);running=false;secs=20*60;blkSecs=0;tEl.textContent=fmt(secs);tEl.classList.remove('warn','over');updateBTimer();}
  else if(e.key.toLowerCase()==='m'){toggleToc();}
  else if(e.key==='Escape'){toc.classList.remove('open');}
});

const toc=document.getElementById('toc'), grid=document.getElementById('tocGrid');
S.forEach((s,idx)=>{ if(s.kind==='block'){ const d=document.createElement('div');
  d.className='item '+s.who;
  d.innerHTML=`<span class="n">${s.num}</span><span><span class="k">${s.kicker}</span><small>${s.who==='a'?'🔵 Persona A':'🟢 Persona B'} · ${s.sec}</small></span>`;
  d.onclick=()=>{ i=idx; render(); toggleToc(); }; grid.appendChild(d); } });
function toggleToc(){ toc.classList.toggle('open'); }
toc.addEventListener('click',e=>{ if(e.target===toc) toc.classList.remove('open'); });

render();
</script>
</body>
</html>
"""

out = HTML.replace("__IMG_JSON__", json.dumps(IMG))
with open("presentacion_4bloques.html", "w", encoding="utf-8") as f:
    f.write(out)
print("OK -> presentacion_4bloques.html  (%.2f MB, %d figuras embebidas)" % (len(out)/1e6, len(IMG)))
