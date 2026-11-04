---
title: "Regolazioni Lightroom maschere vs base"
created: 2025-05-18
updated: 2025-05-18
model: gpt-4o
messages: 2
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Regolazioni Lightroom maschere vs base

> Importato da ChatGPT export · 2 messaggi · gpt-4o · 2025-05-18

## 🧑 User

perchè su lightroom gli strumenti di regolazione del punto di bianco e di nero nelle maschere funzionano in maniera diversa da quelli delle regolazione di base?

---

## 🤖 Assistant

Ottima domanda — e sì, è vero: **su Lightroom gli strumenti di regolazione del punto di bianco e del punto di nero funzionano in modo leggermente diverso all'interno delle maschere rispetto al pannello “Regolazioni di base”**. Vediamo in modo chiaro il **perché**.

---

### 🔧 **1. Regolazioni di base (globali):**
Nel pannello *“Regolazioni di base”*, i cursori **Bianchi** e **Neri** agiscono sull’intera immagine e regolano:

- **Bianchi** = quanto brillanti devono essere le aree più chiare dell’immagine (i pixel più luminosi).
- **Neri** = quanto scuri devono essere i pixel più scuri.

Agiscono in modo **più lineare e ancorato all’istogramma**, spingendo o tirando il punto di bianco/nero sull’intero intervallo dinamico dell’immagine. Hanno anche **un impatto più profondo sul contrasto** generale e sulla distribuzione tonale.

---

### 🎭 **2. Regolazioni locali (maschere):**
Quando usi **Bianchi** e **Neri** all’interno di una maschera, il loro comportamento è **più simile a un contrasto fine**.

- **Non ridefiniscono davvero il punto di bianco/nero globale**, ma agiscono **sui valori locali selezionati dalla maschera**.
- Sono più “contenuti”: ad esempio, anche al massimo non provocano clipping violento come nel pannello base.
- È come se agissero su una curva tonale ristretta *solo* sulla parte dell’immagine selezionata dalla maschera.

---

### 📌 Perché c’è questa differenza?

Perché **Lightroom applica le regolazioni locali in modo “non distruttivo” e selettivo**, evitando che una maschera alteri radicalmente l’intera struttura tonale. Inoltre:

- Il comportamento **dipende dalla maschera stessa**: se selezioni solo le alte luci, “bianchi” si comporterà in modo diverso rispetto a una selezione più ampia.
- Alcuni slider (come *Esposizione*, *Contrasto*, *Texture*, ecc.) sono stati adattati per funzionare “in miniatura” nelle maschere.

---

### ✅ Consiglio operativo:
Se vuoi un controllo più simile al pannello “Base”, **usa Curve o l'istogramma delle maschere**. Oppure lavora prima globalmente e poi fai aggiustamenti locali mirati.

---

Fammi sapere se vuoi un esempio visivo o un mini test da fare su un file per vedere la differenza in pratica.