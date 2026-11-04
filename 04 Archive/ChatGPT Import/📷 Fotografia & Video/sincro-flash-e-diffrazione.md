---
title: "Sincro flash e diffrazione"
created: 2026-04-08
updated: 2026-04-08
model: gpt-5-3
messages: 2
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Sincro flash e diffrazione

> Importato da ChatGPT export · 2 messaggi · gpt-5-3 · 2026-04-08

## 🧑 User

Qual è il massimo sincro flash della Canon R3 e soprattutto per evitare la diffrazione sul Canon 100 millimetri macro serie L, a quanti stop posso arrivare? Perché sto scattando un sacchettino di un imbrago, con doppio flash, su stativo, con timer di 2 secondi, eccetera eccetera, e comunque sembra sempre leggermente sfocato.

---

## 🤖 Assistant

Vado diretto ai punti, perché qui il problema non è “quanto chiudi” ma **perché ti sembra sfocato**.

---

## 1) Sincro flash Canon R3

Sulla entity["product","Canon EOS R3","mirrorless camera"]:

- **1/250s** → otturatore elettronico prima tendina (EFCS)
- **1/200s** → meccanico
- **1/180s** → completamente elettronico cite

Se vuoi massima qualità con flash:
👉 usa **EFCS a 1/250s**
👉 evita elettronico puro (rolling + limiti sync)

HSS puoi usarlo, ma:
- perdi potenza
- perdi consistenza
- non ti serve in studio macro

---

## 2) Diffrazione sul 100 Macro L

Sul entity["product","Canon RF 100mm f/2.8L IS Macro USM","macro lens"]:

- **sweet spot reale**: f/5.6 – f/8
- **ancora molto buono**: f/11
- **inizio diffrazione visibile**: f/13–f/16
- **oltre f/16**: perdita evidente di microcontrasto cite

Nota importante:
- a livello teorico la diffrazione “inizia” già prima
- ma diventa **visivamente fastidiosa da f/11 in su**

---

## 3) Macro: la verità che ti frega

Stai fotografando un oggetto piccolo → quindi sei vicino → quindi:

👉 la profondità di campo è **ridicola anche a f/11**

Risultato:
- tu chiudi → perdi nitidezza per diffrazione
- ma NON guadagni abbastanza DOF
→ quindi l’immagine sembra “molle”

---

## 4) Perché ti sembra sfocato (probabile causa reale)

Con quello che descrivi (treppiede, timer, flash), le cause realistiche sono queste:

### 1. **Micromosso NON da camera, ma da soggetto**
- sacchettino = leggerissimo
- doppio flash = possibile spostamento aria
- vibrazione del pavimento / stativo

👉 soluzione: appesantisci o blocca il soggetto

---

### 2. **Profondità di campo insufficiente**
- non è sfocato → è **fuori fuoco progressivo**
- tipico del macro

👉 soluzione vera:
- focus stacking
- oppure accetta f/8–f/11 e gestisci il piano

---

### 3. **Diffrazione + sharpening insufficiente**
- a f/16+ perdi microcontrasto
- sembra “soft”, non fuori fuoco

👉 soluzione:
- resta tra **f/8 e f/11**
- poi sharpening serio in post

---

### 4. **Errore di piano di fuoco**
- su oggetti tridimensionali piccoli è facilissimo

👉 soluzione:
- allinea il sensore al piano del soggetto
- o usa stacking

---

### 5. **Stabilizzatore attivo su cavalletto**
- IBIS + IS attivi → micro blur

👉 spegni tutto su treppiede

---

## 5) Setup corretto (pratico, senza fronzoli)

Per quello che stai facendo:

- ISO 100
- **1/200–1/250**
- **f/8 o f/11**
- flash come luce principale
- IBIS OFF
- stabilizzazione lente OFF
- scatto remoto o 2s ok
- luce ambiente quasi zero

Se non è nitido così:
👉 non è diffrazione, è setup o fuoco

---

## Conclusione

- La R3 è ok fino a **1/250 sync**
- Il tuo limite NON è il diaframma
- Il problema è quasi sicuramente:
- DOF macro
- piano di fuoco
- micro-movimenti

Se vuoi, mandami uno scatto: in 10 secondi ti dico esattamente dov’è il problema.