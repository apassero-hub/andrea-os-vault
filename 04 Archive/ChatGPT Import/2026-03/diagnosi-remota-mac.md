---
title: "Diagnosi remota Mac"
created: 2026-03-31
updated: 2026-03-31
model: gpt-5-3
messages: 2
source: chatgpt-import
tags: []
---

# Diagnosi remota Mac

> Importato da ChatGPT export · 2 messaggi · gpt-5-3 · 2026-03-31

## 🧑 User

posso fare la diagnosi di un mac apple silicon da un altro mac?

---

## 🤖 Assistant

Sì, ma con dei limiti chiari: non esiste un vero “remote diagnostics completo” ufficiale Apple come su altri sistemi enterprise. Puoi però fare alcune cose utili.

### 1) Apple Diagnostics (NO, da remoto)
Il tool ufficiale Apple (Apple Diagnostics) **non si può avviare da un altro Mac**.
Va eseguito direttamente sulla macchina:

- Spegni il Mac
- Tieni premuto il tasto di accensione
- Entra in “Opzioni” → continua → oppure tieni premuto finché parte la diagnostica

👉 Questo resta l’unico modo per test hardware “certificato Apple”.

---

### 2) Condivisione schermo (SÌ, ma assistita)
Puoi controllare il Mac da remoto con:

- **entity["software","Screen Sharing","macOS built-in feature"]**
- oppure **entity["software","Apple Remote Desktop","Apple remote management software"]**

Questo ti permette di:
- vedere cosa succede
- guidare test manuali
- aprire utility (Monitor Attività, Console, ecc.)

👉 Ma serve che qualcuno accetti la connessione o che sia già configurato.

---

### 3) SSH / Terminale remoto (SÌ, se attivo)
Se sul Mac è attivo “Accesso remoto”:

- puoi collegarti via SSH
- controllare log, dischi, processi, temperature (con tool terzi)

Esempi:
- `log show`
- `diskutil verifyVolume`
- `top` / `htop`

👉 Questo è il metodo più “tecnico” e potente.

---

### 4) Utility Disco e log (SÌ, indirettamente)
Sempre via remoto puoi:
- verificare stato SSD
- controllare errori kernel
- analizzare crash

---

### 5) Modalità Target Disk (LIMITATA su Apple Silicon)
Con Apple Silicon:
- niente più Target Disk Mode classico
- c’è **Share Disk da recovery**

👉 Devi comunque:
- avere accesso fisico al Mac
- collegarlo via cavo a un altro Mac

---

## In sintesi (senza girarci intorno)
- Diagnostica hardware Apple → **NO da remoto**
- Debug software/log → **SÌ da remoto**
- Controllo completo → **solo con accesso fisico o setup remoto già attivo**

---

Se vuoi, dimmi:
- che problema stai cercando di diagnosticare
- se hai accesso fisico o solo remoto

e ti dico il setup più efficace senza perdere tempo.