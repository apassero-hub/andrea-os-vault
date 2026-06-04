---
title: "Impostare Auto Record Shogun"
created: 2026-05-11
updated: 2026-05-11
model: gpt-5-5
messages: 2
source: chatgpt-import
tags: []
---

# Impostare Auto Record Shogun

> Importato da ChatGPT export · 2 messaggi · gpt-5-5 · 2026-05-11

## 🧑 User

Shogun flame autorec come lo setto?

---

## 🤖 Assistant

Su entity["product","Atomos Shogun Flame","Atomos monitor recorder"] l’Auto Record si imposta dal menu dedicato ai trigger SDI/HDMI.
Il funzionamento dipende da **che camera stai usando** e da **come è collegata**.

### Procedura base

1. Vai su **MENU**
2. Apri la sezione **REC**
3. Cerca **Trigger**
4. Attiva:
- **HDMI Trigger** se sei via HDMI
- **SDI Trigger** se sei via SDI
5. Imposta su:
- **Sony**
- **ARRI**
- **Canon**
- oppure generic **Timecode Trigger**, in base alla camera

---

### Con Alexa 35
Con entity["product","ARRI Alexa 35","Cinema camera"] normalmente lavori in **SDI**.

Quindi:

- REC → Trigger → **SDI**
- Protocollo → **ARRI**
- Verifica che la camera stia inviando:
- Rec Flag
- oppure Timecode Run

---

### Controlli importanti
Se non parte automaticamente:

#### 1. Verifica che il segnale sia “clean”
Alcuni output SDI con overlay possono creare problemi.

#### 2. Timecode
Nel menu TC del recorder:
- controlla che stia ricevendo TC dalla camera.

#### 3. Firmware
Gli Shogun Flame vecchi a volte hanno bug con camere recenti. Aggiorna firmware se possibile.

#### 4. Trigger via Teradek
Se stai ricevendo il video tramite entity["brand","Teradek","Wireless video systems"]:
- spesso il REC trigger NON passa correttamente.
- Dipende dal modello TX/RX e dal setup.

In molti set:
- il trigger funziona bene con SDI diretto camera → recorder
- mentre via wireless si perde il flag REC.

---

### Come capire se funziona
Quando premi REC sulla camera:
- sullo Shogun compare automaticamente il bordo rosso REC
- e parte la registrazione senza toccarlo.

Se vuoi, posso anche dirti:
- il setup corretto Alexa 35 + Teradek + Shogun
- oppure come fare autorec via timecode invece che via REC flag, che spesso è più stabile.