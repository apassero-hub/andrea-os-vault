---
title: "Consigli su cataloghi Lightroom"
created: 2026-01-07
updated: 2026-01-07
model: gpt-5-2
messages: 6
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Consigli su cataloghi Lightroom

> Importato da ChatGPT export · 6 messaggi · gpt-5-2 · 2026-01-07

## 🧑 User

Ho bisogno di un consiglio. Io ho un catalogo di Adobe Lightroom, praticamente da quando ho iniziato a fare foto. Non so quante foto ci siano in quel catalogo, saranno centinaia di migliaia. È un modo corretto di utilizzare il catalogo? Ci sono dei modi migliori, più efficienti, più efficaci, magari che rendono il workflow più snello, più rapido?

---

## 🤖 Assistant

Sì: **usare un unico catalogo Lightroom è corretto**.
Ma **non è sempre la scelta più efficiente**, soprattutto con **centinaia di migliaia di file**.

Vado dritto al punto.

---

## 1. Un solo catalogo: pro e limiti reali

### Pro
- Ricerca globale immediata (keyword, date, location, rating).
- Continuità storica del lavoro.
- Nessuna frammentazione del database.

### Limiti concreti (quelli che senti davvero)
- Catalogo pesante → **backup lenti**, **aperture più lunghe**, **ottimizzazioni frequenti**.
- Preview gigantesche che crescono senza controllo.
- Ogni operazione globale (filtri complessi, smart collections, sync) è più lenta.
- Maggiore rischio: se il catalogo si corrompe, **perdi tutto in un colpo**.

Con il tuo volume di scatti, **sei oltre la soglia “comoda”** per un catalogo unico usato in modo indistinto.

---

## 2. L’errore più comune (probabile che lo stia facendo)

Tenere **tutto nello stesso catalogo** per:
- lavoro commerciale
- reportage personali
- test, scarti, prove, duplicati
- vecchi lavori mai più toccati

Questo **non è workflow**, è **archivio passivo**.

---

## 3. La soluzione migliore per il tuo caso (professionale, scalabile)

### Struttura a **cataloghi separati per funzione**, non per anno

#### A. Catalogo MASTER (archivio)
- Tutti i lavori **consegnati e chiusi**
- Solo RAW selezionati + finali
- Niente editing attivo
- Usato per ricerca, portfolio, recupero immagini

👉 Aperto raramente
👉 Ottimizzato e stabile

---

#### B. Catalogo WORKING (attivo)
- Ultimi 6–12 mesi di lavori
- Dove fai:
- selezione
- editing
- export
- Piccolo, veloce, reattivo

👉 Questo è il catalogo che apri ogni giorno

---

#### C. Catalogo TEMP / PROGETTO (opzionale)
- Lavori grossi (spedizioni, doc, campagne)
- Un catalogo per progetto, **chiuso a fine lavoro**
- Poi:
- esporti come catalogo
- lo importi nel MASTER

---

## 4. “Ma così perdo la visione globale?”
No.

Lightroom permette:
- **Import Catalog** mantenendo:
- rating
- keyword
- editing
- Ricostruisci tutto nel MASTER **senza duplicare file**

È un flusso professionale standard, non una pezza.

---

## 5. Ottimizzazioni obbligatorie (indipendenti dai cataloghi)

Se non le fai, qualunque struttura è inutile.

### Preview
- Standard Preview: **2048 px**, non Auto
- 1:1 Preview: **eliminale dopo 30 giorni**
- Ogni tanto: `Library > Previews > Discard 1:1`

### Catalog
- Ottimizza catalogo **ogni 1–2 settimane**
- Catalogo e preview **su SSD NVMe**
- Foto su SSD o RAID veloce (non USB lento)

### Import
- Usa **Smart Preview** per lavorare veloce
- Disattiva Face Recognition se non la usi
- Usa preset di import minimali (niente sharpening aggressivo)

---

## 6. Se vuoi essere ancora più veloce (livello alto)

### Photo Mechanic + Lightroom
- Selezione in Photo Mechanic
- Importi in Lightroom **solo i selezionati**
- Il catalogo cresce molto meno
- Meno preview, meno peso, più velocità

Per il tuo tipo di lavoro è **quasi obbligatorio**.

---

## 7. In sintesi, senza giri di parole

- **Un catalogo unico non è sbagliato**, ma nel tuo caso è **inefficiente**.
- Continuare così ti farà solo peggiorare prestazioni e rischio.
- La soluzione migliore è:
- **WORKING piccolo e veloce**
- **MASTER ordinato e stabile**
- Lightroom regge centinaia di migliaia di foto,
ma **non regge un workflow disordinato**.

Se vuoi, nel prossimo messaggio ti:
- propongo **una struttura di cartelle concreta**
- oppure ti do **un piano step-by-step per migrare senza fermarti di lavorare**

---

## 🧑 User

uso già photo mechanic per fare selezione e import lavori coi metadata ecc. ma per come mi dici tu come faccio a passare i lavori da un catalogo all'altro?

---

## 🤖 Assistant

Perfetto. Allora sei già a metà del lavoro.
Ti spiego **come si passa correttamente un lavoro da un catalogo Lightroom a un altro**, **senza perdere nulla** e **senza duplicare file**.

Vado diretto, procedura operativa.

---

## Metodo corretto: **Esporta come catalogo**

È **l’unico metodo pulito**. Tutto il resto è bricolage.

---

## 1. Nel catalogo WORKING (lavoro attivo)

### A. Seleziona il lavoro
- Puoi selezionare:
- una cartella intera
- una collezione
- un insieme di immagini filtrate

Consiglio: **una collezione per lavoro**. È più controllabile.

---

### B. Esporta come catalogo
Menu:
**File → Export as Catalog…**

Impostazioni consigliate:

- **Nome catalogo**:
`2025_Cliente_Progetto.lrcat`
- **Include available previews**: ✅ Sì
- **Include negative files**:
- ❌ NO se i file sono già nell’archivio definitivo
- ✅ Sì solo se stai spostando fisicamente i file

> Se i RAW restano dove sono, **NON includere i file**.
> Lightroom non li duplica, crea solo i riferimenti.

---

## 2. Apri il catalogo MASTER

Ora sei nel tuo catalogo archivio.

---

## 3. Importa il catalogo esportato

Menu:
**File → Import from Another Catalog…**

Seleziona il `.lrcat` che hai appena esportato.

### Opzioni corrette:
- **File handling**:
- “Add new photos to catalog without moving”
- **Existing photos**:
- “Replace metadata and develop settings only” (se richiesto)

Risultato:
- rating
- keyword
- colori
- crop
- editing
- history (se inclusa)

Tutto identico.

---

## 4. Verifica (fallo sempre)
Controlla:
- 2–3 immagini a caso
- keyword
- crop
- colore
- export test

Se è tutto ok, il lavoro è archiviato.

---

## 5. Pulisci il catalogo WORKING

Ora puoi:
- **rimuovere** il lavoro dal catalogo WORKING
(`Remove from catalog`, NON delete from disk)

Risultato:
- catalogo leggero
- nessun duplicato
- archivio pulito

---

## 6. Workflow consigliato (riassunto operativo)

1. Photo Mechanic
- ingest
- selezione
- metadata
2. Lightroom WORKING
- editing
- export cliente
3. Fine lavoro
- Export as catalog
- Import in MASTER
- Remove dal WORKING

Questo è **workflow professionale standard** su volumi grossi.

---

## 7. Errori da evitare (importante)

- ❌ Copiare cartelle a mano nel Finder
- ❌ Importare RAW due volte
- ❌ Usare “Import” invece di “Import from catalog”
- ❌ Eliminare file dal disco invece che dal catalogo

Uno solo di questi e ti trovi duplicati o link rotti.

---

## 8. Extra: naming e ordine (fa la differenza)

### Naming cataloghi
```
LR_MASTER.lrcat
LR_WORKING_2025.lrcat
```

### Collezioni nel MASTER
- `Anno`
- `Cliente`
- `Progetto`

Non cartelle. **Collezioni**.

---

Se vuoi, al prossimo messaggio posso:
- disegnarti **uno schema preciso di cartelle su disco**
- oppure aiutarti a **decidere cosa resta nel WORKING e cosa va nel MASTER**
- oppure ottimizzare il tuo setup specifico (Mac, dischi, RAID, NVMe)

Dimmi tu.

---

## 🧑 User

mi sembra macchinoso fare questo passaggio di dati da un catalogo all'altro. non mi conviene semplicemente farli anno per anno?

---

## 🤖 Assistant

Risposta secca: **sì, può convenirti**.
Ma **solo se accetti cosa perdi e cosa guadagni**. Non è una scorciatoia neutra.

Vado per punti, senza retorica.

---

## Cataloghi **anno per anno**
### Quando ha senso davvero

Nel tuo caso ha senso se:
- lavori molto “a commesse”
- **raramente riapri lavori vecchi**
- cerchi **semplicità mentale** prima che massima flessibilità
- vuoi **zero procedure di trasferimento**

Apri → lavori → chiudi → fine.

---

## Vantaggi reali (non teorici)

- Nessun export/import di cataloghi
- Cataloghi **più piccoli e veloci**
- Backup più leggeri
- Rischio distribuito (se si rompe un catalogo, perdi solo un anno)
- Struttura intuitiva:
- `LR_2023`
- `LR_2024`
- `LR_2025`

Dal punto di vista operativo è **molto più lineare**.

---

## Svantaggi reali (quelli che contano)

### 1. Ricerca globale spezzata
Non puoi:
- cercare una keyword su 10 anni
- confrontare velocemente lavori simili
- fare collezioni trasversali

Devi **aprire più cataloghi**.

---

### 2. Portfolio meno immediato
Se devi:
- costruire un progetto
- cercare immagini per un pitch
- recuperare materiali storici

Serve più tempo.

---

### 3. Editing storico frammentato
Preset, look, riferimenti visivi:
- li ritrovi, ma non in un unico spazio
- perdi “memoria visiva continua”

---

## Confronto diretto (chiaro)

| Approccio | Velocità | Semplicità | Controllo | Ricerca |
|---------|--------|-----------|----------|---------|
| Catalogo unico | Media | Alta | Basso | Ottima |
| Working + Master | Media | Bassa | Altissimo | Ottima |
| **Anno per anno** | **Alta** | **Altissima** | Media | Limitata |

---

## La verità operativa

> Se **ti pesa già ora** l’idea di esportare/importare cataloghi,
> **non lo farai mai con costanza**.

E un workflow che non segui è peggio di uno imperfetto.

---

## La mia raccomandazione per te

### Soluzione ibrida, concreta

1. **Da ora in avanti**: catalogo **anno per anno**
- `LR_2026.lrcat` (inizia pulito)
2. **Catalogo storico unico**:
- tieni il tuo attuale come `LR_ARCHIVE_PRE_2026`
- non lo tocchi più
3. Niente migrazioni retroattive.
4. Se un giorno serve:
- importi **solo quel lavoro** in un catalogo nuovo

Questo riduce:
- lavoro inutile
- stress
- rischio di casino

---

## Cartelle su disco (semplice e coerente)

```
/FOTO
├── 2023
├── 2024
├── 2025
└── 2026
```

Il catalogo **non decide l’archivio**.
Decide solo come lo navighi.

---

## Conclusione onesta

- Sì, **anno per anno è più pratico**
- No, **non è “meno professionale”**
- È solo meno potente sul lungo periodo

Se il tuo obiettivo è:
- lavorare veloce
- non perdere tempo
- non odiare Lightroom

**Fallo anno per anno.**

Se vuoi, posso:
- aiutarti a decidere **da che anno partire**
- oppure dirti **come spezzare il catalogo attuale senza traumi**
- oppure ottimizzare il catalogo annuale (preset, preview, backup)

Dimmi.