---
title: "Atomos Shogun Flame Audio"
created: 2026-05-11
updated: 2026-05-11
model: gpt-5-5
messages: 2
source: chatgpt-import
tags: []
---

# Atomos Shogun Flame Audio

> Importato da ChatGPT export · 2 messaggi · gpt-5-5 · 2026-05-11

## 🧑 User

Se abbiamo un atomos shogun flame da utilizzare per il record playback. Coi theradeck abbiamo anche l'invio dell'audio?

---

## 🤖 Assistant

Sì, normalmente con un sistema entity["company","Teradek",""] l’audio può essere trasmesso insieme al video, ma dipende da come è configurata la catena SDI/HDMI e da cosa sta uscendo dalla camera.

Nel setup che descrivi:
- entity["product","ARRI Alexa 35",""] → manda video + audio embedded via SDI.
- entity["company","Teradek",""] → trasmette anche i canali audio embedded presenti nel segnale SDI.
- entity["product","Atomos Shogun Flame",""] → può ricevere e riprodurre quell’audio.

Quindi in teoria sì, puoi avere playback con audio.

Però occhio a questi punti pratici da set:

- Molti setup video village usano il wireless solo per immagine, e l’audio viene ignorato o mutato.
- Alcuni operatori disattivano embedded audio per ridurre problemi di sync o configurazione.
- Se il playback serve davvero “cliente-style”, conviene verificare:
- che l’Alexa stia embedando audio sui canali SDI;
- che il Teradek TX/RX non stia filtrando audio;
- che lo Shogun abbia audio monitoring attivo;
- che il monitor abbia speaker o uscita cuffie disponibile.

Sul set il problema più comune è banalmente:
- audio presente nel segnale,
- ma monitor senza speaker,
- oppure volume interno dello Shogun a zero.

Altra cosa importante: il playback registrato sullo Shogun può avere audio anche se il monitoraggio live non lo senti. Sono due cose separate.

Da second AC ti conviene sapere:
- dove entra l’audio,
- se è embedded SDI,
- chi gestisce il playback,
- e se produzione/regia si aspetta audio live oppure solo in replay.