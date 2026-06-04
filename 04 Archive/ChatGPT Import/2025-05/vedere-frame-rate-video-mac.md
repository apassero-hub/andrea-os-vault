---
title: "Vedere frame rate video Mac"
created: 2025-05-22
updated: 2025-05-22
model: gpt-4o
messages: 2
source: chatgpt-import
tags: []
---

# Vedere frame rate video Mac

> Importato da ChatGPT export · 2 messaggi · gpt-4o · 2025-05-22

## 🧑 User

come vedere il frame rate di un video su mac

---

## 🤖 Assistant

Per vedere il **frame rate di un video su Mac**, hai diverse opzioni, a seconda di quanto ti serve essere preciso e del software che hai a disposizione. Ecco i metodi principali:

---

### ✅ **1. QuickTime Player (limitato)**
Apri il video in **QuickTime**, poi:
- Vai su `Composizione` (Command + I)
- Oppure `Finestra` > `Mostra informazioni filmato`

> ⚠️ **Limite**: mostra solo informazioni base, e il frame rate non è sempre visibile.

---

### ✅ **2. VLC Media Player (preciso e gratuito)**
Se non ce l'hai, scaricalo da [videolan.org](https://www.videolan.org/).

Una volta aperto il video in VLC:
- Vai su `Finestra` > `Informazioni media` (`Command + I`)
- Vai nella scheda **Codec**
- Troverai il **frame rate** (es. 23.976 fps, 25 fps, 29.97 fps, ecc.)

---

### ✅ **3. Terminale (per utenti esperti)**
Usa **`ffmpeg`** o **`mediainfo`**, se li hai installati (puoi usare Homebrew per installarli).

#### Con `ffmpeg`:
```bash
ffmpeg -i nomefile.mp4
```
> Troverai il frame rate indicato come `fps` nella parte video del log (es. `25 fps` o `29.97 tbr`).

#### Con `mediainfo`:
```bash
mediainfo nomefile.mp4
```
> Mostra un report chiaro con tutti i dettagli tecnici, incluso **frame rate**, **bitrate**, **risoluzione**, ecc.

---

### ✅ **4. Adobe Premiere Pro / Final Cut Pro**
Se usi software professionale di editing:
- In **Premiere Pro**, trascina il file nella timeline o nel bin, fai clic destro e scegli **Proprietà**.
- In **Final Cut**, basta selezionare la clip e guardare nel pannello **Info**.

---

Se vuoi ti posso dire anche come installare `mediainfo` con Homebrew o consigliarti il metodo più veloce in base a quello che già usi. Vuoi?