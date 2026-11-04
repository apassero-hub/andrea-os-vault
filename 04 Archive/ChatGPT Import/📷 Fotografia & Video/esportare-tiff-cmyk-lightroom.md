---
title: "Esportare TIFF CMYK Lightroom"
created: 2025-09-18
updated: 2025-09-18
model: gpt-5
messages: 10
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Esportare TIFF CMYK Lightroom

> Importato da ChatGPT export · 10 messaggi · gpt-5 · 2025-09-18

## 🧑 User

come esporto una foto in tiff cmyk da lightroom?

---

## 🤖 Assistant

Lightroom **non esporta direttamente in CMYK**. Ti spiego come funziona:

- **Lightroom Classic e Lightroom CC** permettono l’export solo in **sRGB, AdobeRGB e ProPhoto RGB**. Non esiste l’opzione CMYK.
- Questo perché Lightroom è pensato per il flusso digitale (schermo/web/stampa inkjet), mentre la conversione in **CMYK** serve solo in fase di prestampa tipografica, e Adobe ha lasciato questa funzione a **Photoshop** o ad Acrobat.

👉 Per ottenere un file **TIFF in CMYK** partendo da Lightroom:
1. **In Lightroom**:
- Fai `Esporta`
- Scegli formato **TIFF**
- Spazio colore: **AdobeRGB** (più ampio di sRGB e più gestibile in conversione tipografica)
- Profondità: 16 bit se devi fare lavorazioni, altrimenti 8 bit.

2. **Apri il TIFF in Photoshop**.
- Vai su **Immagine → Metodo → Colore CMYK**.
- Oppure meglio ancora: **Modifica → Converti in profilo…**, e scegli il profilo CMYK corretto fornito dalla tipografia (es. **ISO Coated v2 300%** o **FOGRA39**).

3. **Salva** come TIFF (o PSD/EPS se richiesto).

⚠️ Nota: non ha senso fare una conversione “a caso” in CMYK. Devi sempre chiedere alla tipografia quale profilo ICC usa, perché i risultati cambiano parecchio (soprattutto sui neri e sui verdi/azzurri).

Vuoi che ti prepari una **procedura ottimizzata per tipografia offset in Italia** (con i profili ICC standard usati qui), così hai un flusso “a prova di tipografo”?

---

## 🧑 User

qual è il miglior profilo di conversione cmyk per il giappone?

---

## 🤖 Assistant

In Giappone non si usano i profili **FOGRA/ISO** europei, ma degli standard propri.
Il più diffuso per la **stampa offset a quattro colori** è:

- **Japan Color 2001 Coated** → per carta patinata (quello più usato e accettato dalle tipografie giapponesi).
- **Japan Color 2001 Uncoated** → per carta non patinata.

Ci sono anche versioni più recenti:
- **Japan Color 2011 Coated / Uncoated**, introdotti per aggiornare i settaggi alle macchine da stampa più moderne.

👉 In pratica:
- Se non ti danno istruzioni precise, il **profilo di default in Giappone è “Japan Color 2001 Coated”**.
- Se lavori con una tipografia seria, chiedi sempre il loro **ICC specifico**: alcune richiedono proprio *Japan Color 2011*.

⚠️ Nota pratica: i profili **Japan Color** non sono installati di default su Photoshop/Lightroom in Europa. Puoi scaricarli gratuitamente dal sito ufficiale della **Japan Printing Machinery Association (JPMA)** o dai pacchetti ICC Adobe se hai Photoshop aggiornato.

Vuoi che ti recuperi il link diretto ai **profili ICC Japan Color 2001/2011** ufficiali così puoi installarli subito?

---

## 🧑 User

ce n'è uno standard che va bene anche in giappone?

---

## 🤖 Assistant

Sì, c’è un “minimo comune denominatore”: il profilo **Japan Color 2001 Coated**.
È considerato lo standard CMYK generico per la prestampa in Giappone, paragonabile al nostro **ISO Coated v2 (FOGRA39)** in Europa.

In pratica:
- **Se non ti danno indicazioni specifiche**, puoi convertire in **Japan Color 2001 Coated** e sei quasi sempre al sicuro.
- È accettato come standard di riferimento da tutte le tipografie giapponesi per la stampa offset su carta patinata.
- Se invece stampi su carta non patinata → **Japan Color 2001 Uncoated**.

⚠️ Se usi profili europei come **FOGRA39 / ISO Coated v2**, la stampa in Giappone verrà comunque accettata, ma i colori (in particolare i neri e i rossi) possono virare perché le curve di separazione non coincidono con i loro standard.

Vuoi che ti prepari una tabella di confronto **FOGRA vs Japan Color**, così vedi subito le differenze operative quando lavori con tipografie europee o giapponesi?

---

## 🧑 User

comunque non sapendo cosa devono farci nel dubbio lo metto comunque coated?

---

## 🤖 Assistant

Esatto: **meglio usare il Coated** se non ti hanno dato specifiche.

Motivi:
- Il **Japan Color 2001 Coated** è il profilo standard “di default” per la stampa offset in Giappone.
- Anche se poi stampassero su carta non patinata, il file rimane utilizzabile (loro possono ricampionare/convertere se serve).
- Se invece tu inviassi un file in *Uncoated* e loro stampassero su patinata, rischieresti colori spenti e neri poco profondi.

👉 Quindi sì: **usa Japan Color 2001 Coated come impostazione di sicurezza**.
Al massimo, se serve, la tipografia farà una riconversione al loro profilo di macchina.

Vuoi che ti scriva passo-passo come impostarlo correttamente in **Photoshop** quando converti da Lightroom, così non rischi errori di metodo?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

queste sono le uniche informazioni che ho ricevuto

---

## 🤖 Assistant

Perfetto, grazie per lo screenshot: la richiesta è molto chiara.
Ti chiedono **due versioni finali delle foto**:

1. **Per la stampa** → **TIFF in CMYK**
2. **Per il web** → **JPG in RGB**

Non ti hanno fornito nessun profilo ICC specifico. In questo caso la scelta più sicura è:

- **TIFF CMYK**: converti in **Japan Color 2001 Coated** (profilo standard giapponese per offset).
- **JPG RGB**: esporta in **sRGB** (è lo standard per web e social).

### Procedura rapida consigliata
1. **In Lightroom**
- Esporta i TIFF in **AdobeRGB**, 16 bit.
2. **In Photoshop**
- Apri i TIFF.
- Vai su **Modifica → Converti in profilo…**.
- Seleziona **Japan Color 2001 Coated.icc** come profilo di destinazione.
- Salva come TIFF (compressione LZW opzionale, ma di solito le agenzie preferiscono non compressi).
3. **Versione web**
- Sempre in Lightroom, esporta le stesse foto come **JPG, sRGB, 3000px lato lungo** (o in base alla loro richiesta).

👉 In questo modo hai un set conforme allo standard giapponese senza rischiare problemi in tipografia.

Vuoi che ti prepari direttamente un **workflow passo-passo in Lightroom + Photoshop**, con screenshot dei menu giusti per evitare errori nell’export e conversione?