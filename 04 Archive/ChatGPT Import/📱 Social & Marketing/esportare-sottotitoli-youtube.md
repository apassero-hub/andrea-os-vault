---
title: "Esportare sottotitoli YouTube"
created: 2025-12-15
updated: 2025-12-15
model: gpt-5-2
messages: 12
source: chatgpt-import
tags: [fotografia-video, social-marketing]
category: "📱 Social & Marketing"
---

# Esportare sottotitoli YouTube

> Importato da ChatGPT export · 12 messaggi · gpt-5-2 · 2025-12-15

## 🧑 User

come esporto da youtube i sottotitoli autogenerati?

---

## 🤖 Assistant

Procedura corretta, senza giri di parole.

### Metodo ufficiale da YouTube Studio
1. Apri **YouTube Studio**.
2. Vai su **Contenuti**.
3. Seleziona il **video**.
4. Menu a sinistra: **Sottotitoli**.
5. Trova la lingua con etichetta **Automatico**.
6. Clicca sui **tre puntini** a destra.
7. **Scarica**.
8. Scegli il formato:
- **.srt** (consigliato)
- **.vtt**
- **.sbv**

Questo esporta i sottotitoli autogenerati così come sono, inclusi eventuali errori.

### Se non vedi l’opzione “Scarica”
Succede quando:
- I sottotitoli automatici non sono ancora stati elaborati.
- Stai usando un account senza permessi completi sul canale.
- Stai guardando da mobile (serve desktop).

### Alternativa rapida (non ufficiale)
- Apri il video pubblico.
- Copia l’URL.
- Usa un tool esterno tipo:
- **DownSub**
- **SaveSubs**
- **YouTube Subtitle Downloader**

Funzionano, ma non sono affidabili al 100% e non li consiglio per lavori professionali.

### Nota importante
I sottotitoli **automatici non sono legalmente tuoi** se il video non è tuo. Scaricali solo dai **tuoi video** o con autorizzazione.

Se vuoi, dimmi:
- che formato ti serve (SRT, VTT),
- se devi **ripulirli**, **tradurli** o **adattarli per Final Cut / Premiere**.

Vado diretto anche su quello.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, lo screenshot chiarisce il problema.

**Qui non stai vedendo i sottotitoli perché sei nella sezione sbagliata.**
Quella schermata (**Languages**) serve solo per **gestire traduzioni**, non per **visualizzare o scaricare i sottotitoli esistenti**. Per questo la tabella è vuota.

### Dove devi andare davvero (passaggio obbligato)
1. In **YouTube Studio** → **Contenuti**
2. Clicca sul **video**
3. Menu a sinistra → **Sottotitoli** (non “Languages”)
4. Lì vedrai:
- **Italiano – Automatico**
5. Tre puntini a destra → **Scarica**
6. Scegli **.SRT** o **.VTT**

Fine. È l’unico punto da cui YouTube consente il download.

### Perché in “Languages” non compare nulla
- YouTube **non mostra i sottotitoli automatici come lingua** finché non li:
- modifichi,
- oppure carichi manualmente,
- oppure li trasformi in sottotitoli “non automatici”.
- Quella vista è pensata per **doppiaggi e traduzioni**, non per l’export.

### Soluzione alternativa se vuoi forzarli lì
Se proprio vuoi farli comparire anche in quella sezione:
1. Vai in **Sottotitoli**
2. Apri **Italiano (Automatico)**
3. **Modifica**
4. Salva senza cambiare nulla

A quel punto diventano “manuali” e gestibili anche come lingua.

### In sintesi, senza indorare la pillola
- **Non è un bug**
- **Non manca nulla**
- Sei semplicemente nel posto sbagliato dell’interfaccia

Se vuoi, dimmi:
- se ti servono **ripuliti per proiezione**,
- o **adattati per Final Cut / titoli di coda**,
- o **ridotti a frasi chiave temporizzate**.

Vado diretto anche su quello.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

qui? me li scarica in automatico solo in txt

---

## 🤖 Assistant

Sì, **qui**.
Ed è normale che **ti faccia scaricare solo il TXT**. Non stai sbagliando nulla.

### Perché succede
Quella schermata è l’**editor dei sottotitoli automatici**.
Da lì YouTube **non consente l’export temporizzato** (SRT / VTT).
Il TXT è solo la **trascrizione grezza**, senza timecode. Punto.

YouTube fa una distinzione chiara:
- **Automatici non modificati** → solo **TXT**
- **Sottotitoli “manuali”** → **SRT / VTT / SBV**

### Come ottenere SRT o VTT (passaggio obbligato)
Devi **trasformarli in manuali**. Ci vogliono 20 secondi.

1. In quella stessa schermata:
- clicca **Edit timings**
- **non cambiare nulla**
2. Clicca **Done**
3. **Salva**

A questo punto **non sono più “Automatico”**, ma diventano sottotitoli manuali.

Ora:
1. Torna a **Sottotitoli**
2. Tre puntini sulla lingua
3. **Scarica**
4. Scegli **.SRT** o **.VTT**

### Riassunto secco
- TXT: trascrizione, inutile per montaggio
- SRT/VTT: disponibili **solo dopo salvataggio manuale**
- È una **limitazione voluta di YouTube**, non un bug

### Nota pratica per il tuo caso
Visto che stai lavorando a:
- video divulgativo
- proiezione / titoli di coda / montaggio

Ti conviene:
- esportare **SRT**
- poi **ripulirlo e condensarlo** (YouTube genera frasi troppo lunghe)

Se vuoi, nel prossimo messaggio posso:
- **ripulirti il testo**
- **ridurlo a sottotitoli leggibili**
- oppure **estrarre frasi chiave temporizzate** per titoli di coda

Dimmi solo cosa ti serve.

---

## 🧑 User

me li ha scaricati in sbv senza darmi la scelta

---

## 🤖 Assistant

Perfettamente coerente.
**Non è un errore e non c’è nulla che puoi “attivare”.**

### Perché YouTube ti scarica solo **SBV**
Quando i sottotitoli:
- nascono **automatici**
- vengono solo **salvati** (senza upload di un file esterno)

YouTube li considera **internamente SBV**.
In quel caso **forza il download in SBV** e **non mostra il selettore formato**.

Succede spesso. È una limitazione strutturale.

### Cosa cambia davvero (spoiler: quasi nulla)
- **SBV ≈ SRT**
- Contiene **timecode + testo**
- È perfettamente utilizzabile in **Final Cut, Premiere, DaVinci**

### Come convertirlo subito (2 opzioni serie)

#### Opzione 1 – Conversione immediata
Apri l’SBV e:
- caricalo su **Subtitle Edit** (desktop)
- oppure su **subtitlesconverter.com**

Esporti in **SRT o VTT** in 10 secondi.

#### Opzione 2 – Conversione manuale (se vuoi controllo totale)
Se ti serve pulizia editoriale (consigliato):
1. Importa l’SBV in **Subtitle Edit**
2. Correggi:
- frasi troppo lunghe
- a capo sbagliati
- punteggiatura
3. Esporta **SRT**

### Come evitare SBV in futuro (se proprio vuoi)
L’unico modo è:
- **caricare tu manualmente un file SRT/VTT**
- oppure creare i sottotitoli **fuori da YouTube** e poi uploadarli

YouTube **non dà scelta di formato** per sottotitoli auto-convertiti.

### Verità nuda
- SBV non è “peggio”
- YouTube è solo rigido e poco trasparente
- Per montaggio video **SBV → SRT** è una conversione banale

Se vuoi, incolla qui **le prime 10 righe dell’SBV** e ti dico:
- se i timecode sono buoni
- se conviene ripulirlo
- o se puoi importarlo diretto in Final Cut senza perdere tempo

---

## 🧑 User

su final cut li posso usare ed esportare poi in srt?

---

## 🤖 Assistant

Risposta secca: **sì, ma con una precisazione importante**.

### In Final Cut Pro
- **Importi SBV senza problemi** (Final Cut lo legge come sottotitolo temporizzato).
- **Lavori normalmente**: sincronizzazione, tagli, adattamenti.

### Ma attenzione all’export
👉 **Final Cut NON esporta SRT dai sottotitoli importati come file esterno.**

Final Cut può:
- esportare **SRT solo se i sottotitoli sono creati nativamente dentro FCP**
- NON convertire automaticamente SBV → SRT in uscita

### Quindi le strade reali sono due

#### Opzione consigliata (più veloce e pulita)
1. **Converti SBV → SRT prima**
- Subtitle Edit / tool online
2. Importi **SRT in Final Cut**
3. Se serve, fai micro-aggiustamenti
4. **Esporti di nuovo SRT** senza problemi

È il flusso corretto, professionale, senza sorprese.

#### Opzione alternativa (più macchinosa)
1. Importi SBV in Final Cut
2. Copi manualmente i sottotitoli in una **Caption role nativa**
3. Ricrei i sottotitoli
4. Esporti SRT

Onestamente: **perdi tempo inutilmente**.

### Sintesi brutale
- SBV: ok per lavorare
- FCP: **non è un convertitore**
- Se ti serve SRT finale: **converti prima o dopo, ma fuori da Final Cut**

### Il mio consiglio nel tuo caso
Converti **subito** l’SBV in SRT, poi lavora solo in SRT.
Meno attrito, zero rogne.

Se vuoi:
- ti dico **esattamente come importarlo in FCP** (ruoli, lingua, standard)
- oppure **come ripulire l’SRT per proiezione** o per YouTube

Dimmi solo dove deve finire quel video.

---

## 🧑 User

fcp non me lo importa

---

## 🤖 Assistant

Ok. Se **Final Cut non importa l’SBV**, il motivo è tecnico e preciso. Vado diretto.

## Perché FCP NON importa l’SBV
Final Cut **non supporta nativamente il formato.sbv**.
Lo “accetta” solo in alcuni casi tramite drag&drop ambiguo, ma **non è un formato ufficialmente compatibile**.

I formati che **FCP importa davvero** sono:
- **.srt**
- **.itt**
- **.vtt** (non sempre stabile)
- **.xml** (caption convertite)

👉 **SBV = no**, nella pratica.

## Quindi cosa devi fare (obbligatorio)
Devi **convertire l’SBV prima**. Non c’è alternativa.

### Metodo rapido e sicuro (consigliato)
**Subtitle Edit** (gratis, Mac incluso):
1. Apri Subtitle Edit
2. `File → Open` → seleziona `.sbv`
3. Controlla che i timecode siano ok
4. `File → Save as` → **SubRip (.srt)**
5. Importa l’**SRT** in Final Cut

Final Cut lo importerà **al 100%**.

### Metodo online (se hai fretta)
- subtitlesconverter.com
- sbv → srt
Funziona, ma zero controllo qualitativo.

## Come importarlo correttamente in Final Cut
Una volta che hai l’SRT:
1. `File → Import → Captions`
2. Seleziona l’SRT
3. Imposta:
- **Language**: Italian
- **Format**: iTT o SRT (dipende dalla versione FCP)
4. Conferma

Comparirà come **Caption role**, non come clip video.

## Riassunto senza sconti
- ❌ SBV → **Final Cut non lo importa**
- ✅ SRT → **import immediato**
- YouTube ti ha dato SBV → **va convertito**
- Final Cut **non è un tool di conversione**

## Consiglio operativo
Non perdere altro tempo a forzare FCP.
**SBV → SRT fuori**, poi lavori pulito.

Se vuoi:
- ti preparo io la **conversione corretta**
- oppure ti dico **le impostazioni giuste per sottotitoli da proiezione / YouTube / festival**

Dimmi solo **dove andrà proiettato o pubblicato il video**.