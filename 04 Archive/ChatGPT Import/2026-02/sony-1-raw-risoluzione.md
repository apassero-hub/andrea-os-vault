---
title: "Sony 1 RAW risoluzione"
created: 2026-02-01
updated: 2026-02-01
model: gpt-5-2
messages: 4
source: chatgpt-import
tags: []
---

# Sony 1 RAW risoluzione

> Importato da ChatGPT export · 4 messaggi · gpt-5-2 · 2026-02-01

## 🧑 User

La Sony 1 prima serie ha la possibilità di selezionare i RAW in grandezza tipo lossless M, S, L o scatta soltanto in una risoluzione?

---

## 🤖 Assistant

La **entity["","Sony Alpha 1",1]** (prima serie) *può* selezionare diverse modalità di RAW con differenti dimensioni e tipi di compressione — non è limitata a un’unica risoluzione RAW fissa.

Dettagli operativi:

- **Tipi di RAW**: puoi scegliere tra **Non compresso**, **Compresso lossless** e **Compresso**.
- **Dimensioni lossless**: all’interno del **RAW compresso lossless** puoi scegliere tra **L / M / S** (Large, Medium, Small).
- **L** = massima risoluzione (utilizza praticamente tutti i 50 MP del sensore).
- **M / S** = risoluzioni più basse (riduce numero di pixel e peso dei file), mantenendo *compressione lossless* senza perdita qualitativa.
- Il numero di pixel effettivo dei RAW M e S corrisponde a quello delle rispettive immagini JPEG/HEIF M e S dopo sviluppo. cite

In sostanza: puoi **scattare RAW con risoluzioni diverse**, non solo al massimo (L). Le opzioni di menu permettono di scegliere tra grande, medio e piccolo **anche in modalità RAW compresso senza perdita**, quindi file RAW “più leggeri” per workflow più veloce o almacenamiento ridotto. cite

Se hai firmware aggiornato (≥ Ver. 1.30), queste opzioni sono disponibili direttamente dal menu qualità immagine. cite

---

## 🧑 User

Quanti mpx ha la m?

---

## 🤖 Assistant

Sulla **entity["company","Sony Alpha 1","mirrorless camera model"]**, il **RAW lossless M** è da **circa 21 megapixel**.

Per completezza:
- **RAW L**: ~50,1 MP
- **RAW M**: ~21 MP
- **RAW S**: ~12,5 MP

Il RAW M è un vero downsample lossless: meno pixel, stessi 14 bit, stessa qualità tonale del L. Ideale se non ti servono sempre i 50 MP.