# 02 — Transformers / LLMs y la teoría de lenguajes formales

El subcampo que conecta directamente la IA moderna con la materia. Todas las citas verificadas contra fuentes primarias (arXiv, ACL Anthology, JMLR, TACL, PMLR, OpenReview).

> Tensión central (a presentar con cuidado): hay resultados de **Turing-completitud** (con precisión *infinita*, ítem 2) y resultados de **TC⁰** (con precisión *finita/logarítmica*, ítem 3). No es contradicción: son supuestos distintos. El survey (ítem 4) lo explica.

---

## 1. Delétang et al. — Neural Networks and the Chomsky Hierarchy (EL PAPER CLAVE)

**APA.** Delétang, G., Ruoss, A., Grau-Moya, J., Genewein, T., Wenliang, L. K., Catt, E., Cundy, C., Hutter, M., Legg, S., Veness, J., & Ortega, P. A. (2023). *Neural networks and the Chomsky hierarchy* (ICLR 2023; arXiv:2207.02098). https://doi.org/10.48550/arXiv.2207.02098

**Hallazgos (estudio empírico: 20.910 modelos, 15 tareas).**
- Transformers y RNNs **fallan en tareas no regulares** (no generalizan a secuencias más largas); los transformers tienen dificultades incluso en ciertas tareas regulares de este marco.
- LSTMs resuelven lenguajes regulares y de tipo "counter".
- Solo redes con **memoria estructurada** (Stack-RNN, Tape-RNN) resuelven lenguajes libres de contexto / sensibles al contexto.
- Más datos/entrenamiento **nunca** producen generalización en tareas que exceden el poder computacional de la arquitectura.

**Implicación.** La jerarquía de Chomsky predice qué NO puede aprender un modelo moderno. El ingeniero que conoce la teoría sabe de antemano dónde fallará la herramienta.

---

## 2. Pérez, Barceló & Marinković — Attention is Turing-Complete

**APA.** Pérez, J., Barceló, P., & Marinković, J. (2021). Attention is Turing-complete. *Journal of Machine Learning Research, 22*(75), 1–35. https://jmlr.org/papers/v22/20-302.html
- Previo: Pérez, J., Marinković, J., & Barceló, P. (2019). *On the Turing completeness of modern neural network architectures* (ICLR 2019; arXiv:1901.03429).

**Resultado.** El transformer con *hard attention* es Turing-completo **asumiendo precisión aritmética arbitraria/infinita**. Es expresividad teórica idealizada, no los modelos reales (precisión finita).

---

## 3. Merrill & Sabharwal — límites con precisión realista (TC⁰)

**APA.**
- Merrill, W., & Sabharwal, A. (2023). The parallelism tradeoff: Limitations of log-precision transformers. *TACL, 11*, 531–545. https://doi.org/10.1162/tacl_a_00562
- Merrill, W., Sabharwal, A., & Smith, N. A. (2022). Saturated transformers are constant-depth threshold circuits. *TACL, 10*, 843–856. https://doi.org/10.1162/tacl_a_00493

**Resultado.** Los transformers con **precisión logarítmica** se simulan con circuitos de umbral uniformes de profundidad constante (**TC⁰**). Consecuencia: si **L ≠ P**, no pueden resolver con exactitud igualdades lineales ni verificar pertenencia a una gramática libre de contexto arbitraria. "Parallelism tradeoff": toda arquitectura tan paralelizable como el transformer hereda estas limitaciones.

**Implicación.** Bajo supuestos realistas, los transformers viven en una clase de complejidad muy estrecha. Hay tareas de razonamiento que la arquitectura nunca resolverá por escala bruta.

---

## 4. Strobl et al. — Survey

**APA.** Strobl, L., Merrill, W., Weiss, G., Chiang, D., & Angluin, D. (2024). What formal languages can transformers express? A survey. *TACL, 12*, 543–561. https://doi.org/10.1162/tacl_a_00663

Reconcilia resultados aparentemente contradictorios mostrando que dependen de supuestos (precisión, tipo de atención, profundidad, codificación posicional). Referencia "paraguas" del consenso del campo.

---

## 5. Hahn — Limitaciones teóricas del self-attention

**APA.** Hahn, M. (2020). Theoretical limitations of self-attention in neural sequence models. *TACL, 8*, 156–171. https://doi.org/10.1162/tacl_a_00306

El self-attention (hard) **no modela PARITY ni Dyck-2** (estructura jerárquica) salvo que capas/cabezas crezcan con la longitud. Primer resultado negativo fundacional.

---

## 6. Weiss, Goldberg & Yahav — RASP

**APA.** Weiss, G., Goldberg, Y., & Yahav, E. (2021). Thinking like transformers. *ICML (PMLR 139)*, 11080–11090. https://proceedings.mlr.press/v139/weiss21a.html

Definen **RASP**, un modelo computacional/lenguaje para el transformer-encoder (como los RNN se mapean a autómatas finitos). Hace tangible que el transformer es una "máquina" caracterizable.

---

## 7. Bhattamishra, Ahuja & Goyal — capacidad y límites empíricos

**APA.** Bhattamishra, S., Ahuja, K., & Goyal, N. (2020). On the ability and limitations of transformers to recognize formal languages. *EMNLP 2020*, 7096–7116. https://doi.org/10.18653/v1/2020.emnlp-main.576

Los transformers funcionan bien solo en un **subconjunto** de lenguajes regulares y se **degradan** al aumentar la complejidad (a diferencia de los LSTM).

---

## 8. Complementos

- **Chiang, D., & Cholak, P. (2022).** Overcoming a theoretical limitation of self-attention. *ACL 2022*, 7654–7664. https://doi.org/10.18653/v1/2022.acl-long.527 — Construyen un transformer que reconoce PARITY; pero la generalización a longitudes mayores sigue siendo frágil. Matiza honestamente el debate.
- **Merrill, W., & Sabharwal, A. (2024).** *The expressive power of transformers with chain of thought* (ICLR 2024; arXiv:2310.07923). https://arxiv.org/abs/2310.07923 — CoT con pasos **logarítmicos** apenas amplía el poder; **lineales** → lenguajes sensibles al contexto; **polinomiales** → exactamente la clase **P**.

---

## Síntesis

Con matemática revisada por pares: (1) los modelos modernos son caracterizables por las mismas clases de la teoría del curso (jerarquía de Chomsky, TC⁰, NC¹, P); (2) bajo supuestos realistas viven en TC⁰ y fallan predeciblemente en familias enteras de problemas; (3) ni la escala bruta ni el chain-of-thought eliminan estos límites estructurales.
