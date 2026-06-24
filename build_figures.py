#!/usr/bin/env python3
"""Genera las figuras del paper (PNG 300 dpi) en figuras/. Datos verificados;
ver investigacion/ y fuentes_adicionales.md para las fuentes de cada cifra."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

os.makedirs("figuras", exist_ok=True)

PRIMARY = "#1F4E79"   # azul profundo
ACCENT  = "#E8743B"   # naranja
GREEN   = "#2E8B57"
RED     = "#C0392B"
GRAY    = "#7F8C8D"
BLUE    = "#2E6FB0"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "axes.edgecolor": "#444444",
    "axes.linewidth": 0.8,
    "figure.dpi": 300,
})

def finish(ax, source):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.figure.text(0.01, 0.005, source, fontsize=7.5, color=GRAY, style="italic")

def barlabels(ax, bars, fmt="{:+.0f}", dy=0.0):
    for b in bars:
        h = b.get_height()
        va = "bottom" if h >= 0 else "top"
        ax.annotate(fmt.format(h), (b.get_x()+b.get_width()/2, h+dy),
                    ha="center", va=va, fontsize=10, fontweight="bold")

# ---------------------------------------------------------------- Fig 1
def fig1():
    pts = [("mar 2024\nDevin", 13.9), ("oct 2024\nClaude 3.5", 49.0),
           ("dic 2024\no3", 71.7), ("may 2025\nSonnet 4", 72.7),
           ("sep 2025\nSonnet 4.5", 77.2)]
    x = list(range(len(pts))); y = [p[1] for p in pts]
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.plot(x, y, "-o", color=PRIMARY, lw=2.5, markersize=8, markerfacecolor=ACCENT,
            markeredgecolor=PRIMARY, zorder=3)
    ax.fill_between(x, y, color=PRIMARY, alpha=0.07)
    for xi, (lbl, yi) in zip(x, pts):
        ax.annotate(f"{yi:.0f}%", (xi, yi), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=10, fontweight="bold", color=PRIMARY)
    ax.set_xticks(x); ax.set_xticklabels([p[0] for p in pts], fontsize=9)
    ax.set_ylim(0, 90); ax.set_ylabel("Issues resueltos (%)")
    ax.set_title("Crecimiento de la capacidad de la IA para programar\n(SWE-bench, estado del arte)")
    ax.grid(axis="y", ls=":", alpha=0.5)
    finish(ax, "Fuente: SWE-bench Verified (Anthropic, OpenAI). El punto de mar. 2024 (Devin) es sobre otro subconjunto.")
    fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.savefig("figuras/fig1_swebench.png"); plt.close(fig)

# ---------------------------------------------------------------- Fig 2
def fig2():
    labels = ["Copilot — RCT 2023\n(tarea acotada,\ncódigo nuevo)",
              "METR — RCT 2025\n(seniors, repos\npropios maduros)"]
    vals = [55.8, -19.0]; colors = [GREEN, RED]
    fig, ax = plt.subplots(figsize=(7, 4.6))
    bars = ax.bar(labels, vals, color=colors, width=0.55, edgecolor="white")
    barlabels(ax, bars, fmt="{:+.1f}%")
    ax.axhline(0, color="#333333", lw=1)
    ax.set_ylim(-35, 70); ax.set_ylabel("Cambio en la velocidad de trabajo (%)")
    ax.set_title("La IA en productividad: el contexto lo cambia todo")
    ax.grid(axis="y", ls=":", alpha=0.5)
    finish(ax, "Fuente: Peng et al. (2023); METR (2025). Estudios no comparables directamente (tarea y experiencia distintas).")
    fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.savefig("figuras/fig2_productividad.png"); plt.close(fig)

# ---------------------------------------------------------------- Fig 3 (Chomsky)
def fig4():
    fig, ax = plt.subplots(figsize=(8, 5.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    bands = [
        (0.5, 9.0, "Tipo 0 · Recursivamente enumerables  (Máquinas de Turing)", "#1F4E79"),
        (1.7, 6.6, "Tipo 1 · Sensibles al contexto", "#2E6FB0"),
        (2.9, 4.2, "Tipo 2 · Libres de contexto", "#5B9BD5"),
        (4.0, 2.0, "Tipo 3 · Regulares", "#A9CCE3"),
    ]
    base_y = 2.1
    for i, (x0, w, label, color) in enumerate(bands):
        h = 7.1 - i*1.35
        box = FancyBboxPatch((x0, base_y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                             linewidth=1.4, edgecolor="white", facecolor=color, alpha=0.92, zorder=i)
        ax.add_patch(box)
        ax.text(x0 + w/2, base_y + h - 0.40, label, ha="center", va="top",
                fontsize=10.5 if i == 0 else 9.5, color="white", fontweight="bold", zorder=10)
    ax.set_title("Los transformers, dentro de la jerarquía de Chomsky", pad=10)
    # annotations placed in the clear strip BELOW the bands
    ax.annotate("Transformers con precisión\nrealista ≈ TC⁰: no reconocen\ngramáticas libres de contexto\narbitrarias",
                xy=(5.0, 2.6), xytext=(0.4, 1.5), fontsize=8.8, color=RED, fontweight="bold",
                ha="left", va="top",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
    ax.annotate("Transformers con precisión\ninfinita = Turing-completos\n(límite ideal)",
                xy=(9.0, 5.5), xytext=(6.3, 1.5), fontsize=8.8, color="#145A32", fontweight="bold",
                ha="left", va="top",
                arrowprops=dict(arrowstyle="->", color="#145A32", lw=1.6))
    fig.text(0.01, 0.01, "Fuente: Chomsky (1956); Delétang et al. (2023); Merrill & Sabharwal (2023); Pérez et al. (2021).",
             fontsize=7.5, color=GRAY, style="italic")
    fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.savefig("figuras/fig4_chomsky.png"); plt.close(fig)

# ---------------------------------------------------------------- Fig 4
def fig5():
    labels = ["Desarrolladores\nde software\n(BLS, 2024-34)",
              "Programadores\n(BLS, 2024-34)",
              "Empleo 22-25 años,\nocupaciones expuestas\n(Stanford, 2025)"]
    vals = [15, -6, -13]; colors = [GREEN, RED, RED]
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    bars = ax.bar(labels, vals, color=colors, width=0.55, edgecolor="white")
    barlabels(ax, bars, fmt="{:+.0f}%")
    ax.axhline(0, color="#333333", lw=1)
    ax.set_ylim(-22, 24); ax.set_ylabel("Variación del empleo (%)")
    ax.set_title("El empleo se recompone: se automatiza codificar,\nno diseñar y decidir")
    ax.grid(axis="y", ls=":", alpha=0.5)
    finish(ax, "Fuente: U.S. Bureau of Labor Statistics (2025); Brynjolfsson, Chandar & Chen (2025).")
    fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.savefig("figuras/fig5_empleo.png"); plt.close(fig)

# ---------------------------------------------------------------- Fig 5
def fig6():
    labels = ["Creados", "Desplazados", "Saldo neto"]
    vals = [170, -92, 78]; colors = [GREEN, RED, PRIMARY]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(labels, vals, color=colors, width=0.55, edgecolor="white")
    barlabels(ax, bars, fmt="{:+.0f}")
    ax.axhline(0, color="#333333", lw=1)
    ax.set_ylim(-120, 200); ax.set_ylabel("Millones de empleos a 2030")
    ax.set_title("Proyección global de empleo por IA y automatización a 2030")
    ax.grid(axis="y", ls=":", alpha=0.5)
    finish(ax, "Fuente: World Economic Forum, Future of Jobs Report 2025.")
    fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.savefig("figuras/fig6_wef.png"); plt.close(fig)

# ---------------------------------------------------------------- Fig 6
def fig3():
    labels = ["Código de Copilot\ncon vulnerabilidad\n(Pearce, 2022)",
              "Código de IA con\nfallo de seguridad\n(Veracode, 2025)",
              "Paquetes sugeridos\ninexistentes\n(Spracklen, 2025)"]
    vals = [40, 45, 19.7]
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    bars = ax.bar(labels, vals, color=ACCENT, width=0.55, edgecolor="white")
    barlabels(ax, bars, fmt="{:.0f}%")
    ax.set_ylim(0, 60); ax.set_ylabel("Porcentaje (%)")
    ax.set_title("La IA acelera, pero la verificación sigue siendo humana")
    ax.grid(axis="y", ls=":", alpha=0.5)
    finish(ax, "Fuente: Pearce et al. (2022); Veracode (2025); Spracklen et al. (2025).")
    fig.tight_layout(rect=[0, 0.03, 1, 1]); fig.savefig("figuras/fig3_seguridad.png"); plt.close(fig)

for f in (fig1, fig2, fig3, fig4, fig5, fig6):
    f()
print("Figuras generadas en figuras/")
