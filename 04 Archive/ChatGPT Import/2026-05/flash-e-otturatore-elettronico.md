---
title: "Flash e otturatore elettronico"
created: 2026-05-10
updated: 2026-05-10
model: gpt-5-5
messages: 4
source: chatgpt-import
tags: []
---

# Flash e otturatore elettronico

> Importato da ChatGPT export · 4 messaggi · gpt-5-5 · 2026-05-10

## 🧑 User

Con sony a7v e a1 si può scattare col flash in otturatore elettronico?

---

## 🤖 Assistant

No. Sia con entity["product","Sony A7 V","Sony mirrorless camera"] (ipotizzando tu intenda la futura A7 V) sia con entity["product","Sony A1","Sony mirrorless camera"] il flash non funziona realmente in otturatore elettronico “puro” come sulle medio formato o su alcune stacked molto recenti.

La situazione reale è questa:

- Su entity["product","Sony A1","Sony mirrorless camera"] puoi usare il flash con otturatore elettronico solo in condizioni molto specifiche grazie al sensore stacked velocissimo, ma:
- hai limitazioni importanti
- il sync speed è ridotto
- con molti flash possono comparire bande o esposizione non uniforme
- spesso la macchina passa comunque a una modalità ibrida/anti-distorsione
- non hai la stessa affidabilità del meccanico

Per lavoro serio con flash, praticamente tutti usano:
- otturatore meccanico
oppure
- EFCS (Electronic First Curtain Shutter)

Sulla futura entity["product","Sony A7 V","Sony mirrorless camera"], salvo rivoluzioni hardware, sarà molto probabilmente la stessa cosa o persino più limitata della A1, perché non dovrebbe avere un readout veloce come il stacked della A1.

La vera discriminante è:
- sensore stacked ultra fast → possibilità parziale
- sensore tradizionale → flash + elettronico praticamente no

Per capirci:
- entity["product","Sony A9 III","Sony mirrorless camera"] è la prima Sony dove il discorso cambia davvero, perché il global shutter permette flash sync reale anche in elettronico e a tempi assurdi.
- entity["product","Sony A1","Sony mirrorless camera"] invece è “quasi”, ma non completamente.

Quindi, in pratica:
- shooting flash affidabile → usa meccanico/EFCS
- elettronico → bene per silenzio e raffica, non per workflow flash professionale standard.

---

## 🧑 User

E con la nikon z8/z9?

---

## 🤖 Assistant

Con entity["product","Nikon Z8","Nikon mirrorless camera"] e entity["product","Nikon Z9","Nikon mirrorless camera"] il discorso è diverso rispetto a quasi tutte le altre mirrorless, perché sono camere senza otturatore meccanico per gli scatti fotografici: lavorano sempre in elettronico. cite

Quindi sì:
flash e “otturatore elettronico” funzionano normalmente su Z8/Z9. Anzi, è proprio il funzionamento standard della camera.

Però ci sono alcuni limiti pratici importanti:

- sync standard:
- circa 1/200s reale
- HSS/FP fino a 1/8000s con flash compatibili cite
- il sensore stacked ha un readout molto veloce, quindi:
- rolling shutter molto ridotto
- flash utilizzabile in modo affidabile
- esperienza molto più vicina a una reflex pro rispetto alla maggior parte delle mirrorless cite
- però non è global shutter:
- in alcuni casi estremi puoi ancora vedere micro-banding o artefatti
- soprattutto con certi trigger o flash third-party
- oppure con luci LED/PWM problematiche cite

In pratica:

| Camera | Flash in elettronico | Affidabilità |
|---|---|---|
| entity["product","Sony A1","Sony mirrorless camera"] | Sì, ma limitato | Buona ma non “trasparente” |
| entity["product","Nikon Z8","Nikon mirrorless camera"] | Sì, nativo | Molto buona |
| entity["product","Nikon Z9","Nikon mirrorless camera"] | Sì, nativo | Molto buona |
| entity["product","Sony A9 III","Sony mirrorless camera"] | Sì, global shutter | Attualmente il riferimento |

La cosa interessante è che molti fotografi sportivi/eventi stanno usando Z8/Z9 con flash senza percepire particolari differenze operative rispetto alle reflex flagship Nikon precedenti. È una delle poche implementazioni “electronic shutter only” davvero mature.