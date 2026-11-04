---
title: "eGPU su Mac"
created: 2025-11-10
updated: 2025-11-10
model: gpt-5
messages: 2
source: chatgpt-import
tags: [storage-it]
category: "💾 Storage & IT"
---

# eGPU su Mac

> Importato da ChatGPT export · 2 messaggi · gpt-5 · 2025-11-10

## 🧑 User

Utilizzare una gpu esterna su mac ha senso?

---

## 🤖 Assistant

Dipende dal modello di Mac e dallo scopo. Ti spiego in sintesi:

### 1. **Compatibilità**
- Solo i **Mac con processore Intel** e porte **Thunderbolt 3** supportano ufficialmente le **eGPU** (schede grafiche esterne).
- I **Mac con chip Apple Silicon (M1, M2, M3)** **non supportano le eGPU**: la GPU è integrata nel SoC e non può essere bypassata.
- Quindi, se hai un Mac con chip Apple (M1/M2/M3), la risposta è **no, non ha senso** perché **non funziona proprio**.

### 2. **Prestazioni (solo su Intel)**
- Su Intel, una eGPU può migliorare sensibilmente le prestazioni grafiche in app come **DaVinci Resolve**, **Final Cut Pro**, **Premiere**, **Blender**, ecc.
- Tuttavia, il **collo di bottiglia della connessione Thunderbolt 3** (40 Gbps) riduce parte delle prestazioni: una GPU esterna lavora al **70-80% della sua potenza reale**, a volte meno.
- È utile per chi lavora con software che sfruttano bene OpenCL o Metal, ma oggi è una soluzione di **transizione o di nicchia**.

### 3. **Costi e alternative**
- Un box eGPU costa 300–400 €, a cui va aggiunta la GPU (spesso altri 400–1000 €).
- A parità di costo, un **Mac con chip M1/M2/M3 Pro o Max** offre prestazioni GPU superiori e integrate, senza complicazioni.
- Inoltre, le eGPU **non sono più supportate da Apple** nei nuovi macOS (da Ventura in avanti è tutto fermo al supporto legacy).

### 4. **Quando ha ancora senso**
- Solo se hai un **Mac Intel Thunderbolt 3** (es. Mac mini 2018, MacBook Pro 2019, iMac 2019) e vuoi **allungargli la vita** per lavori video o 3D.
- In tutti gli altri casi (soprattutto su Apple Silicon): **no**, non vale la pena.

Se mi dici il modello preciso del tuo Mac (anno e chip), ti dico in due righe se è compatibile e quale configurazione avrebbe eventualmente senso. Vuoi che controlli?