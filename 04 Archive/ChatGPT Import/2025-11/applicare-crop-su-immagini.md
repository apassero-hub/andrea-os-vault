---
title: "Applicare crop su immagini"
created: 2025-11-21
updated: 2025-11-21
model: gpt-5-1
messages: 2
source: chatgpt-import
tags: []
---

# Applicare crop su immagini

> Importato da ChatGPT export · 2 messaggi · gpt-5-1 · 2025-11-21

## 🧑 User

se faccio un crop su photo mechanic come faccio poi ad applicarlo alle immagini non soltanto sui metadati?

---

## 🤖 Assistant

Photo Mechanic **non applica mai i crop ai pixel**.
Il crop è **solo un’informazione XMP**, un’anteprima “virtuale” che Lightroom/ACR può leggere e tradurre in un crop reale durante l’import.

Se vuoi trasformare il crop in un file effettivamente ritagliato, hai tre opzioni concrete:

---

## 1. **Usare Lightroom / Adobe Camera Raw**
Photo Mechanic scrive il crop nei metadati XMP.
Quando importi i RAW in Lightroom (con “Read Metadata from File” se necessario), il crop viene **riconosciuto e applicato automaticamente**.
Da lì, esportando i JPEG/TIFF avrai il ritaglio definitivo.

**È il flusso corretto.**

---

## 2. **Esportare direttamente da Photo Mechanic**
PM può creare dei JPEG già croppati:

**File → Export… → Processor**
Nelle impostazioni, attiva **“Apply Ingest/Metadata Edits including Crop”**.

Il JPEG generato avrà il crop “baked in”, ma:
- **non vale per i RAW**, solo per il file esportato.
- il RAW originale resta non modificabile (Photo Mechanic non modifica mai i RAW a livello pixel).

---

## 3. **Usare Photo Mechanic Plus + un engine esterno (raro)**
Alcuni workflow custom usano script o plugin di terze parti per leggere il crop e generare file TIFF/JPEG pre-croppati.
Non è una soluzione nativa, né consigliabile.

---

## Quindi, risposta secca:
**Non puoi applicare il crop ai pixel direttamente in Photo Mechanic.
Puoi solo esportare un JPEG/TIFF croppato oppure far applicare il crop a Lightroom/ACR.**

Se vuoi, ti preparo un flusso ottimizzato PM → LR così eviti perdita di tempo.