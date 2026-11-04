---
title: "Convertire sottotitoli in testo"
created: 2025-11-12
updated: 2025-11-12
model: gpt-5
messages: 2
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Convertire sottotitoli in testo

> Importato da ChatGPT export · 2 messaggi · gpt-5 · 2025-11-12

## 🧑 User

come posso trasformare i sottotitoli generato di final cut in testo semplice?

---

## 🤖 Assistant

Dipende da come li hai esportati o dove si trovano ora. Ti riassumo le opzioni principali:

---

### **1. Se hai già esportato i sottotitoli**
Final Cut può esportarli in diversi formati:
- **.srt**
- **.vtt**
- **.itt** (iTunes Timed Text)
- **.stl**

In questo caso basta **aprire il file con un editor di testo (TextEdit, VS Code, Sublime, ecc.)** e poi:
- eliminare manualmente le righe con numeri e timecode, oppure
- usare un servizio o uno script per **convertire da.srt a testo pulito**.

Ad esempio, puoi usare strumenti online gratuiti come:
- [https://toolslick.com/conversion/subtitle/srt-to-text](https://toolslick.com/conversion/subtitle/srt-to-text)
- [https://gotranscript.com/subtitle-converter](https://gotranscript.com/subtitle-converter) (scegli “Plain text” come output)

Oppure, se preferisci farlo in locale:
- Apri il file `.srt` in **TextEdit**, seleziona **Trova > Sostituisci** e rimuovi con una regex:
```
^\d+\s*\n\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\n
```
lasciando solo il testo parlato.

---

### **2. Se i sottotitoli sono ancora dentro Final Cut**
Puoi:
1. Selezionare la **pista dei sottotitoli** nella timeline.
2. Dal menu: **File > Esporta > File multimediale (⌘E)**.
3. Nella finestra, sotto “Ruoli”, scegli **Solo sottotitoli** → **Formato: SRT**.
4. Poi segui il punto 1 per pulire il file.

---

### **3. Metodo rapido in Final Cut (senza esportare file)**
Se vuoi solo estrarre il testo:
- Vai nel **pannello “Timeline Index” (Comando + F)**
- Filtra per **“Captions”**
- Seleziona tutte le righe (clic su una, poi ⌘A)
- Copiale (⌘C) e incollale in un editor di testo.
Questo ti darà già il testo sequenziale (spesso con i timecode, ma più facile da ripulire).

---

Vuoi che ti prepari uno **script o un comando da Terminale/Mac** che prenda un file `.srt` e lo trasformi automaticamente in testo pulito in un file `.txt`?