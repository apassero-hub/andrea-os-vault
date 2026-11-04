---
title: "Trasferire seriale DaVinci"
created: 2026-03-17
updated: 2026-03-17
model: gpt-5-3
messages: 2
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Trasferire seriale DaVinci

> Importato da ChatGPT export · 2 messaggi · gpt-5-3 · 2026-03-17

## 🧑 User

come faccio a cambiare il computer collegato ad un seriale davinci? ho venduto la macchina e vorrei trasferire il seriale

---

## 🤖 Assistant

Vai dritto: non devi “trasferire” manualmente il seriale, devi **liberare una delle attivazioni**.

### Come funziona DaVinci Resolve Studio
Il seriale permette **2 attivazioni contemporanee**.
Quando ne aggiungi una terza, Resolve ti forza automaticamente a disattivare le altre.

---

## Metodo corretto (se NON hai più il vecchio Mac)
1. Installa **entity["software","DaVinci Resolve Studio","Blackmagic Design video editing software"]** sul nuovo computer
2. Aprilo
3. Inserisci il tuo **seriale**
4. Ti comparirà un messaggio tipo:
> “Hai già raggiunto il numero massimo di attivazioni”
5. Clicca su **“Deactivate other computers” / “Deauthorize all”**

👉 Questo resetta le attivazioni precedenti (incluso il Mac venduto)
👉 Il nuovo computer rimane attivo

---

## Metodo alternativo (se avessi ancora il vecchio)
- Apri Resolve
- Vai su **Help → Deactivate License**

---

## Nota importante (che molti ignorano)
- Non esiste un pannello online per gestire le licenze
- Il reset avviene **solo al momento della nuova attivazione**
- Il processo è immediato e non perdi nulla (progetti, ecc.)

---

## Consiglio pratico
Fallo subito prima che l’acquirente accenda la macchina e provi ad aprire Resolve.
Non succede nulla di grave, ma eviti rotture.

---

Se vuoi ti spiego anche la differenza tra seriale e dongle (USB): cambia completamente la gestione e può avere senso nel tuo caso.