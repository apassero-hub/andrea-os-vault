---
title: "Differenza colori foto ZV-1"
created: 2025-08-20
updated: 2025-08-20
model: gpt-5
messages: 2
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Differenza colori foto ZV-1

> Importato da ChatGPT export · 2 messaggi · gpt-5 · 2025-08-20

## 🧑 User

ho la sony zv-1 e le foto come vengono scattate e come le visualizzo sulla camera mi piacciono molto, anche col picture style disattivato. quando poi le scarico sul computer ovviamente in raw le vedo flat, ma anche se le scatto in jpg hanno dei colori molto differenti

---

## 🤖 Assistant

Quello che descrivi è un comportamento del tutto normale con la Sony ZV-1 (e in generale con tutte le fotocamere digitali). Ti spiego perché vedi questa differenza:

### 1. Differenza tra **anteprima in camera** e file su PC
- Quando scatti, sul display della ZV-1 non stai vedendo il **RAW nudo e crudo**, ma un’anteprima JPEG generata dalla fotocamera, con i profili colore e il processamento interni Sony (contrasto, nitidezza, saturazione, riduzione rumore ecc.).
- Anche se disattivi i **Creative Styles / Picture Profile**, la macchina applica comunque un minimo di interpretazione interna per rendere l’immagine più gradevole a video.
- Una volta importato il file **RAW** sul computer, quel processamento non c’è più: il RAW è volutamente piatto e neutro, serve come “negativo digitale” da sviluppare in post-produzione.
- Il **JPEG scaricato** mantiene parte della resa, ma su PC lo vedi attraverso il profilo colore del software che usi (es. macOS Preview, Lightroom, Capture One ecc.), che spesso non corrisponde al motore interno Sony → da qui la differenza.

### 2. Perché i JPEG ti sembrano diversi anche se sono JPEG
- Sony nel display della ZV-1 usa la propria pipeline di rendering ottimizzata (come una preview HDR compatibile con il monitor LCD della camera).
- Sul computer il JPEG viene interpretato da un altro viewer, che non sempre riproduce fedelmente gamma e profilo colore. Per esempio:
- **Windows Photo Viewer** o **Anteprima su Mac** usano profili ICC base → possono alterare leggermente saturazione/contrasto.
- Software come Lightroom o Capture One di default non applicano i “color science” Sony, ma un profilo Adobe standard.

### 3. Come ottenere la stessa resa della camera sul computer
- **In JPEG**:
- Assicurati che il monitor sia calibrato e che usi software che rispetti i profili colore ICC.
- Puoi impostare in camera uno **Creative Style** che ti piace (ad es. Standard, Vivid o Neutral personalizzato) e mantenere direttamente quei JPEG senza passare dal RAW.
- **In RAW**:
- In Lightroom, Capture One o altri software seleziona il profilo **Camera Standard / Camera Vivid / Camera Neutral** (sono simulazioni dei profili Sony) invece del default “Adobe Color”.
- In questo modo otterrai un punto di partenza molto più simile a quello che vedevi sul display.

---

👉 Ti chiedo: quando scarichi i JPEG sul computer, li stai guardando con un software tipo **Lightroom/Photoshop** o solo con il **visualizzatore di sistema**?
Da lì cambia molto la resa e posso dirti come settare il workflow più fedele alla ZV-1. Vuoi che ti prepari una **configurazione ideale per avere sul computer la stessa resa che vedi in camera**?