---
title: "Problemi di lentezza Lightroom"
created: 2025-08-30
updated: 2025-08-30
model: gpt-5
messages: 6
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Problemi di lentezza Lightroom

> Importato da ChatGPT export · 6 messaggi · gpt-5 · 2025-08-30

## 🧑 User

Ho notato che ultimamente Lightroom si è rallentato parecchio nella fase di sviluppo, cioè passate da una foto all'altra, nonostante io stia editando delle foto fatte con un Alpha 9 II, quindi 24 megapixel. E' proprio lento, delle volte si sposta, ma mi mantiene all'anteprima della foto precedente. Considera che io ho un MacBook Pro M1 Pro con 1TB di harddisk, 16GB di RAM, e appunto il processore M1 Pro per editare le foto è decisamente molto più che sufficiente. Ma è diventato lento, non so per quale motivo. Riesci a darmi qualche dritta?

---

## 🤖 Assistant

Chiaro, Andrea. La tua macchina non è assolutamente il collo di bottiglia: un M1 Pro con 16 GB RAM regge senza problemi i RAW da 24MP. Quindi il problema è quasi sicuramente di **ottimizzazione del catalogo o delle anteprime di Lightroom**, non di hardware. Ti elenco i punti da controllare in ordine di priorità:

---

### 1. **Anteprime e cache**
- Vai in **Preferenze → Prestazioni** e controlla che la cache Camera RAW non sia satura.
- Porta la cache a **20–30 GB** (di default è spesso ridicola, tipo 5 GB).
- In **Gestione file**, assicurati di generare **Anteprime 1:1** o **Anteprime standard ad alta qualità** se fai molto zoom. Se usi le “Smart Previews” per sviluppare, Lightroom sarà più fluido (lavora su file compressi e applica le modifiche ai RAW solo al salvataggio).
- Cancella le **anteprime obsolete**: nel menu `Catalog Settings → File Handling` puoi rigenerarle.

---

### 2. **Catalogo**
- Fai una **ottimizzazione del catalogo** (`File → Ottimizza catalogo`).
- Se lavori sempre con lo stesso catalogo da anni e pesa decine di GB, valuta di dividerlo (ad esempio un catalogo annuale). I cataloghi enormi rallentano molto la navigazione.

---

### 3. **GPU**
- In **Preferenze → Prestazioni**, verifica l’impostazione GPU. Su M1 Pro funziona bene il “**Usa GPU per display e sviluppo**”. Se è su “auto” ma noti rallentamenti, prova a forzarlo su **Attiva per Sviluppo**.
- Al contrario, se noti bug grafici (anteprima che resta della foto precedente), prova a disattivare temporaneamente la GPU: se sparisce, è un problema di accelerazione hardware di quella versione di Lightroom.

---

### 4. **Disco e memoria**
- Anche se hai 1 TB, Lightroom scrive molto in cache e nei file temporanei. Verifica che tu abbia almeno **100–150 GB liberi**.
- Metti il **catalogo e la cache** sul disco interno, non su SSD esterni (anche veloci, tipo NVMe USB-C). Gli M1 hanno I/O interno molto più veloce.

---

### 5. **Versione di Lightroom**
- Controlla se sei aggiornato all’ultima release. Alcune versioni recenti hanno avuto bug proprio nella gestione GPU e anteprime. Adobe rilascia fix silenziosi quasi ogni mese.

---

### 6. **Routine di pulizia**
- Vuota la cache delle anteprime video se usi anche file video.
- Disattiva plugin inutilizzati (`Gestione plugin`).
- Chiudi app pesanti in background: Lightroom M1 scala bene, ma se hai Final Cut, Chrome con 50 tab o Capture One aperti insieme, rallenta.

---

👉 Ti consiglio di partire da: **(1) aumentare la cache Camera RAW, (2) rigenerare le anteprime, (3) ottimizzare il catalogo**.
Spesso già questo fa un’enorme differenza.

Vuoi che ti prepari una **procedura step-by-step** ottimizzata per MacBook Pro M1 Pro (cioè un check in sequenza per capire dove sta il collo di bottiglia e risolverlo in mezz’ora)?

---

## 🧑 User

Allora, la cache ce l'avevo già impostata a 50 GB, però visto che c'erano le parti di accelerazione GPU e compagnia Bella, per cui avevo attivo soltanto l'uso del GPU per la visualizzazione, adesso l'ho attivato anche per l'elaborazione dell'immagine e per l'esportazione. Effettivamente è già diventato un po' più fluido. Poi ho impostazione cache video, limito a dimensione cache video a 20 GB, attiva visualizzazione di anteprime predefiniti, cronologista talentino. Non ho quella parte che mi dicevi tu sulla gestione del file per quanto riguarda le anteprime.

---

## 🤖 Assistant

Perfetto, già il fatto che abilitando la GPU anche per sviluppo ed esportazione tu abbia percepito più fluidità conferma che **era un collo di bottiglia lato accelerazione hardware**. Su M1 Pro conviene sempre tenerla attiva.

Ti chiarisco le altre voci che ti mancano, così capiamo se è solo un discorso di **anteprime**:

---

### Dove si gestiscono le anteprime
Non è nelle **Preferenze**, ma in:
- **Menu → Catalog Settings → File Handling**
- Qui hai “Anteprime standard” → scegli **Qualità alta**.
- Dimensione anteprime → imposta su **Lato lungo pari alla risoluzione del tuo monitor** (es. se lavori sul MacBook da 3024 px di lato lungo, metti quello).
- Sotto puoi anche impostare l’eliminazione automatica delle **1:1 previews** (di default 30 giorni, puoi anche metterle a “mai” se vuoi tenerle).

Quando importi le foto:
- Nella finestra di importazione, puoi scegliere di generare subito **Anteprime 1:1** o **Anteprime standard**.
- Se salti questo passaggio, Lightroom te le crea “al volo” mentre sfogli, ed è quello che dà la sensazione di scatto lento o anteprima che rimane bloccata sulla foto precedente.

---

### Video cache
Il limite 20 GB va bene se usi poco video, ma se ti capita di lavorare con clip (anche solo preview GoPro o A7SIII), alza pure a 40–50 GB. Non incide sulle foto, ma ti evita rallentamenti quando apri progetti misti.

---

### Routine consigliata per velocizzare Lightroom (M1)
1. **Rigenera anteprime**: seleziona la cartella attuale e fai `Libreria → Anteprime → Crea anteprime 1:1`. Lascialo lavorare un po’. Dopo la prima volta, la navigazione sarà istantanea.
2. **Ottimizza catalogo**: `File → Ottimizza catalogo`.
3. **Controlla spazio disco**: almeno 15–20% libero.
4. **GPU**: tieni attiva per sviluppo ed esportazione (come hai fatto).
5. **Chiudi app in background**: soprattutto Chrome e Final Cut, che mangiano RAM.

---

👉 Se vuoi, ti preparo una **sequenza step-by-step rapida** da fare ogni 2–3 mesi, così Lightroom resta sempre veloce senza doverlo “ripulire” quando ormai si è incasinato. Vuoi che te la scriva in stile checklist?

---

## 🧑 User

Sul catalog settings, su generali mi da il percorso, non mi dice niente di che, su anteprime, dimensione totale, cache anteprime 35 giga, lato maggiore anteprima standard 1440, qualità anteprima media, elimina automaticamente anteprime 1 a 1 dopo 30 giorni, limita dimensione di cache in anteprima, non è attivato, e tra i dati che credo che non interessi non capisco neanche, ma quella parte che mi cito non c'è.

---

## 🤖 Assistant

Perfetto, adesso capisco cosa stai vedendo.
La schermata che descrivi è **giusta**, solo che Lightroom su Mac con lingua italiana ti mostra i nomi leggermente diversi da come li ricordavo in inglese. In pratica:

- **“Lato maggiore anteprima standard: 1440”** → qui puoi alzare il valore. Con il tuo MacBook Pro (3024 px lato lungo) conviene impostarlo almeno a **2880**. A 1440 Lightroom deve ridimensionare ogni volta per mostrarti l’immagine, ed è lì che senti lag.
- **“Qualità anteprima: media”** → mettila su **Alta**. Sì, occupa un po’ più spazio in cache, ma rende la navigazione molto più fluida.
- **“Elimina automaticamente anteprime 1:1 dopo 30 giorni”** → se lavori spesso su cartelle che riapri e riusi (ad esempio lavori che durano settimane), metti su **Mai**. Se invece preferisci risparmiare spazio, lascia 30 giorni ma sappi che Lightroom dovrà rigenerarle quando riapri vecchi lavori.

---

### Perché non vedi le voci che ti dicevo prima
Quelle (tipo “qualità alta” o “mai”) in realtà ci sono: corrispondono esattamente alle voci che hai elencato, solo tradotte diversamente. La sostanza è la stessa.

---

### Cosa ti consiglio di fare subito
1. Vai in **Catalog Settings → File Handling (Anteprime)**.
- Cambia **Lato maggiore anteprima standard** da 1440 → **2880**.
- Cambia **Qualità anteprima: Media → Alta**.
- Metti **Elimina anteprime 1:1 → Mai** (almeno per prova).
2. Poi seleziona una cartella di lavoro → `Libreria → Anteprime → Crea anteprime 1:1`.
- Lascialo macinare, poi naviga: vedrai che lo scorrimento diventa immediato, senza quell’effetto “resta sull’anteprima precedente”.

---

Vuoi che ti scriva una **configurazione ideale per il tuo MacBook Pro M1 Pro** (cioè valori consigliati per cache, anteprime e GPU, con motivazione per ciascuno) così setti una volta e non ci pensi più?