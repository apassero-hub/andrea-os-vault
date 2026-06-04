---
title: "Lunghezza password Dropbox"
created: 2026-04-24
updated: 2026-04-24
model: gpt-5-3
messages: 6
source: chatgpt-import
tags: []
---

# Lunghezza password Dropbox

> Importato da ChatGPT export · 6 messaggi · gpt-5-3 · 2026-04-24

## 🧑 User

quanto può essere lunga una password di un link di dropbox

---

## 🤖 Assistant

Le password dei link condivisi su entity["software","Dropbox","file hosting service"] non hanno un limite “visibile” per l’utente come potrebbe avere, ad esempio, un campo di input con contatore caratteri. Tuttavia, nella pratica:

- **Lunghezza massima supportata**: fino a circa **1.000 caratteri**
- **Lunghezza consigliata**: tra **12 e 32 caratteri** (oltre non porta benefici reali in termini di sicurezza operativa)
- **Caratteri supportati**: lettere maiuscole/minuscole, numeri e simboli

### Considerazioni concrete
- Dropbox usa hashing lato server, quindi non è la lunghezza estrema a fare la differenza, ma **entropia e complessità reale**
- Password troppo lunghe diventano solo **scomode da condividere** (soprattutto con clienti)
- Per un uso professionale (come il tuo, con clienti), la soluzione più efficiente è:
- password di **16–20 caratteri**
- generata casualmente
- condivisa su canale separato (es. WhatsApp o telefono)

### Sintesi
Puoi teoricamente inserire password molto lunghe, ma **oltre i 30–40 caratteri è inutile** nella pratica e peggiora solo l’usabilità.

---

## 🧑 User

come faccio a disattivare i comenti da una cartella su dropbox e i suoi contenuti?

---

## 🤖 Assistant

Non esiste un interruttore diretto in entity["software","Dropbox","file hosting service"] per “disattivare i commenti” su una cartella e tutti i file al suo interno. I commenti sono legati ai **permessi di accesso**, non a un’impostazione separata.

### Cosa puoi fare davvero (funziona)
Per impedire i commenti devi limitare i permessi:

#### 1) Usa link in sola visualizzazione
- Vai sulla cartella → **Condividi**
- Imposta il link su **“Chiunque con il link può visualizzare”**
- Assicurati che **modifica sia disattivata**

✔ Risultato:
gli utenti possono **vedere e scaricare**, ma **non possono commentare**

---

#### 2) Rimuovi accessi con permessi elevati
Se qualcuno è invitato come collaboratore:
- Apri **Gestisci accesso**
- Cambia da **“Può modificare”** a **“Può visualizzare”** oppure rimuovilo

✔ Risultato:
niente commenti, perché il commento è considerato un’azione “attiva”

---

#### 3) Disattiva completamente il link (se serve controllo totale)
- Disattiva il link condiviso
- Condividi solo con utenti specifici con permessi limitati

---

### Limite strutturale (da sapere)
Dropbox non ha una funzione tipo:
- “blocca commenti”
- “disabilita feedback”

Se una persona ha **accesso collaborativo**, può commentare. Punto.

---

### Strategia consigliata (per lavoro con clienti)
Per evitare caos:
- usa sempre **link view-only**
- raccogli feedback **fuori da Dropbox** (mail o PDF annotabile)

Se vuoi, ti costruisco un flusso preciso per consegna lavori + feedback clienti senza commenti sparsi.

---

## 🧑 User

col mio profilo personale mi fa commentare lo stesso sulle foto anche se ho il link solo in visualizzazione

---

## 🤖 Assistant

Hai ragione a segnalarlo: non è un errore, è proprio come funziona entity["software","Dropbox","file hosting service"].

### Perché riesci comunque a commentare
Se sei **loggato con un account Dropbox**, anche con link “solo visualizzazione” puoi:
- aggiungere commenti
- mettere reaction
- taggare persone

Questo perché Dropbox considera il commento come **feedback leggero**, non come modifica al file.

---

### Cosa NON puoi fare
Con link view-only:
- non puoi modificare file
- non puoi caricare
- non puoi eliminare

Ma i commenti restano attivi.

---

### Come bloccarli davvero (soluzioni pratiche)

#### 1) Forzare accesso senza account
Non è una vera impostazione, ma funziona:
- chi apre il link **senza login** → non può commentare
- soluzione operativa: chiedere ai clienti di aprire il link in incognito

✔ poco elegante, ma efficace

---

#### 2) Disattivare download + usare presentazione
- Attiva modalità **sola visualizzazione**
- Disattiva download (se necessario)

Non elimina sempre i commenti, ma riduce molto le interazioni

---

#### 3) Cambiare strumento per il feedback (soluzione seria)
Se vuoi controllo reale:
- esporti una gallery (PDF o web)
- feedback via:
- email strutturata
- strumenti dedicati (Frame.io, Pixieset, ecc.)

---

### Sintesi chiara
Con Dropbox:
- **non puoi disattivare i commenti in modo assoluto**
- puoi solo **limitare il contesto in cui avvengono**

---

Se vuoi lavorare in modo pulito con clienti (zero casino nei commenti), Dropbox non è lo strumento ideale per il feedback. Posso suggerirti un setup preciso più professionale in base a come consegni i lavori.