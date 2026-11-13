# RawLine Space: recupero dei file rovinati, approfondimento

Data: 2026-11-13, sera. Andrea ha chiesto di approfondire tutti i modi di riparare un file rovinato oltre a "ricopiarlo da un'altra copia". Ho provato sei strade su file veri.

**Come ho lavorato.**
- **G-SPEED:** solo letto. Le prove sono state fatte su copie nella cartella di lavoro.
- **Catalogo Lightroom:** letto da una copia. Quello vero non è stato aperto, perché Lightroom era in uso.
- **Codice:** prototipi, non codice dell'app. Sono in `research_notes/RawLine Space/Prototipi 13 nov/recupero/`.

## In breve

| Strada | Prova | Risultato | Spazio |
|---|---|---|---|
| 1. Copie nascoste (Lightroom) | catalogo e anteprime veri | 78.220 anteprime, quasi tutte da 1000–2500 px. Le regolazioni di tutte le 170.818 foto sono nel catalogo | zero |
| 2. Intestazione da un "gemello" | 4 fotocamere e compressioni | Dati RAW **identici byte per byte**, immagine identica o quasi | zero |
| 3a. Pixel nel RAW (compresso Sony, non compresso) | 64 KB rovinati | La fascia rovinata sparisce, il file resta un RAW | zero |
| 3b. Tessera di un ARW senza perdita | 64 KB rovinati | Colmata con l'anteprima di Lightroom: contenuto giusto, un po' più morbido | zero |
| 3c. JPEG con punti di ripartenza | 64 byte rovinati | Ricostruiti esattamente i 413 blocchi colpiti | zero |
| 4. Video Sony troncato (messo da parte) | clip tagliata al 60% | Indice ricostruito **identico** all'originale, fotogrammi identici | zero |
| 5. File cancellati e scheda formattata | scheda exFAT finta | Cancellati: 8 su 8. Dopo la formattazione: 17 su 17 (uno con l'aiuto del punto 2) | zero |
| 6. Dati di riparazione nostri | ARW da 41 MB | Con l'1% in più ripara pezzi grandi, blocchi sparsi e intestazione, sempre **identico** all'originale | 0,5–1% |

## 1. Le copie nascoste che hai già

**Catalogo attivo** (`Lightroom Catalog-2-2-v13-3`, 170.424 foto senza contare le copie virtuali):

| Anteprima di Lightroom presente | Foto | di cui RAW |
|---|---|---|
| quasi a piena risoluzione (≥ 2500 px) | 178 | 177 |
| 1000–2499 px (l'anteprima "standard") | 66.699 | 63.928 |
| sotto i 1000 px | 11.325 | 11.248 |
| nessuna | 92.222 | 86.070 |

- **Le anteprime occupano 32 GB.** Ho controllato a campione 3.000 file d'anteprima veri: le dimensioni coincidono con quelle scritte nel catalogo.
- **Il catalogo vecchio sul G-SPEED** (`2020:2021/Lightroom`) ha altre 84.785 anteprime (37 GB) e **12.829 anteprime avanzate**. Queste sono DNG da 2560 px ancora modificabili, 13 GB in tutto. Non ho ancora collegato queste anteprime alle singole foto.
- **Le regolazioni stanno tutte nel catalogo.** Per 170.818 foto su 170.837 c'è la scheda completa delle regolazioni. In un DNG HDR di prova l'XMP dentro il file ha 156 campi di regolazione, e il catalogo ha la scheda completa della stessa foto. Quindi:
  - **XMP rovinato o perso:** si rifà dal catalogo. La via più sicura è il comando di Lightroom "Salva metadati nel file"; più avanti Space potrebbe farlo da solo.
  - **Export rovinato:** si rifà dal RAW con le regolazioni del catalogo. Lightroom non si comanda da fuori senza rete, quindi Space prepara l'elenco "da riesportare".
- **Limite:** le anteprime da circa 2000 px vanno bene per il web e per rivedere la foto, non per la stampa grande. Sono però un'ottima base per i punti 3b e 5.

## 2. Intestazione ricostruita da uno scatto gemello

Se l'inizio del file è rovinato (intestazione, dati di scatto), il file non si apre più, ma i dati dell'immagine possono essere intatti. Space prende l'intestazione di uno scatto sano della stessa fotocamera, poi ricollega i dati dell'immagine del file rovinato, che ritrova cercandone l'inizio.

**Cosa ho scoperto sugli ARW del tuo archivio** (campione di 400 RAW sul G-SPEED):
- **tre tipi di ARW:**
  - "senza perdita" a tessere da 512×512 px: A7 IV, A1, A1 II;
  - "compresso Sony" con perdita: A9 II, A1, A7 IV, ZV-1;
  - "non compresso": A7 IV, A9 II;
- **altri RAW:** ci sono anche Canon CR2 e DNG.
- **Ordine delle tessere:** la A7 IV scrive le tessere sempre nello stesso ordine, per colonne. Il gemello lo rivela.

| File di prova (primi 64 KB distrutti) | Esito |
|---|---|
| A7 IV, senza perdita | dati RAW identici, immagine **identica** pixel per pixel |
| A9 II, compresso Sony | dati RAW **identici byte per byte**, immagine quasi identica (43 dB) |
| A1, compresso Sony | come sopra (51 dB) |
| A7 IV, non compresso | come sopra (47 dB) |

- **Da dove vengono le piccole differenze:** solo dai dati di scatto del gemello (bilanciamento del bianco, esposizione, data), non dall'immagine. Nel prodotto Space rimette data e dati veri presi dal catalogo Lightroom, se ci sono, e segna il file "intestazione ricostruita".
- **Due regole emerse dagli errori delle prove:**
  - non scrivere mai la parte presa dal gemello sopra i dati dell'immagine;
  - leggere la posizione esatta di ogni puntatore, non cercarla per valore.

## 3. Riparare i pixel quando il danno è dentro l'immagine

**Il controllo ogni MB è troppo grossolano per questo lavoro.** Per i pixel serve sapere *dove* è il danno con più precisione. Propongo di passare al controllo CRC-64 **ogni 64 KB**:
- **spazio:** circa 2 GB nel database di Space per tutto il G-SPEED, sempre lo 0,012% e non sui dischi;
- **in cambio:** localizza 16 volte meglio e corregge 1–2 bit ogni 64 KB invece che ogni MB.

Nelle prove la zona da 64 KB l'ho indicata io, come farebbe questo controllo.

**3a. ARW compressi Sony e non compressi: riparazione dentro il RAW.**
- **Cosa succede:** un danno colpisce solo una fascia di righe, circa 5–12 righe per 64 KB.
- **La riparazione:** ogni riga rovinata si rifà dalla riga sana più vicina con lo stesso colore del sensore. Il file resta un RAW modificabile.

| File | Nella fascia rovinata |
|---|---|
| A9 II compresso | da 8,5 dB (rovinato) a **43 dB** (riparato): non si vede più |
| A7 IV non compresso | da 8,8 dB a **35 dB**: non si vede più |

**3b. ARW senza perdita: tessera colmata con l'anteprima.**
- **Cosa succede:** un danno rovina la tessera da 512×512 px dal punto del danno in poi.
- **Come la trova Space:** dal controllo ogni 64 KB sa quale tessera è, e dai dati di ritaglio e di orientamento sa dove cade nell'immagine.
- **Come la colma:** con l'anteprima di Lightroom, girata, allineata e adattata nei colori sulla zona sana attorno.
- **Risultato:** da 18,7 dB a **31,4 dB** nella tessera, con un errore medio di 4,5 su 255. Il contenuto è quello giusto, solo meno dettagliato, perché l'anteprima di prova era di 1440 px.
- **Due cose da sapere:**
  - questo produce un'immagine nuova (TIFF), non un RAW;
  - Lightroom salva le anteprime senza rotazione, quindi vanno girate (scoperto durante la prova).

**3c. JPEG.**
- **Punti di ripartenza:** su 300 JPEG del G-SPEED, **80 export di Lightroom su 87** li hanno. Gli export di Photoshop li hanno meno spesso: 76 su 181.
- **Con i punti di ripartenza** un danno resta chiuso in un pezzo. Nella prova, 64 byte rovinati hanno colpito lo 0,009% dei pixel. Il prototipo ha trovato i blocchi rovinati confrontando i bordi con i pixel vicini e ne ha ricostruiti **413, esattamente quelli colpiti**. Nella zona: da 9 dB a **30 dB**, a occhio non si vede.
- **Senza punti di ripartenza** il danno arriva fino in fondo all'immagine. Lì serve rifare l'export, o l'anteprima.

## 4. Video troncati

> **Messo da parte (Andrea, 13 nov):** per ora i video restano fuori da questa parte di Space. La prova resta scritta qui sotto, per quando se ne riparlerà.

**Il tuo archivio video:**
- 3.439 MP4 (2,5 TB);
- 2.072 MOV (0,6 TB);
- 579 MXF (1,2 TB).

**Come sono fatti i file Sony XAVC S.** Sono molto regolari: si ripete "blocco metadati, 24 fotogrammi, blocco audio". Ogni blocco metadati comincia con la stessa firma. Se la registrazione si interrompe (batteria, scheda tolta), l'indice finale non c'è e il video non si apre.

**La prova.**
- Ho tagliato al 60% una copia di `C0057.MP4` (4K a 50 fotogrammi al secondo). macOS dice "Cannot Open".
- Il prototipo ha ricostruito l'indice prendendo come modello `C0056.MP4`, della stessa fotocamera:
  - **l'indice è identico a quello originale** per tutta la parte recuperata: dimensioni e posizioni di ogni fotogramma, campione audio e blocco metadati;
  - il video si apre, dura 6,72 s, e i fotogrammi controllati a 0,5 s, 3,3 s e 6,6 s sono **identici** all'originale.
- **Cosa si perde:** oltre a quello che manca fisicamente, l'ultimo gruppo di fotogrammi incompleto (circa 1 s). I fotogrammi B in fondo si appoggiano a un fotogramma che non c'è più.
- **Limite:** vale per i Sony MP4. MXF e MOV di altre macchine (DJI, iPhone) hanno strutture diverse: serve un modulo per ciascuno.

## 5. Ritrovare file cancellati e schede formattate

Space legge un disco byte per byte, in sola lettura, e cerca l'inizio tipico di ARW, JPEG e MP4. La fine di ogni file la calcola dalla sua struttura interna.

**La prova.** Su una scheda exFAT finta (un'immagine disco nella cartella di lavoro) ho copiato 12 ARW, 4 JPEG e una clip Sony.

| Caso | Ritrovati identici all'originale |
|---|---|
| 8 file cancellati | **8 su 8** (e anche gli altri 9) |
| Scheda formattata dopo | **16 su 17** subito |
| Il diciassettesimo | il suo inizio era stato sovrascritto dalla formattazione, ma le sue 140 tessere RAW c'erano ancora: ricostruito con l'intestazione del gemello (punto 2), **immagine identica** |

**Limiti:**
- funziona quando i file sono scritti in un pezzo solo, cioè quasi sempre su una scheda formattata nella fotocamera;
- non funziona sui dischi pieni e frammentati da anni, né su file già sovrascritti;
- i file ritrovati si salvano sempre su un **altro** disco, mai su quello da cui si recupera.

## 6. Dati di riparazione nostri (alla PAR2, ma scritti da noi)

È lo stesso principio di PAR2, un codice di Reed-Solomon, scritto da zero: niente licenze da rispettare, e decidiamo noi su quali file e con quanto spazio.
- **Come funziona:** il file si divide in 200 blocchi e si calcolano m blocchi di riparazione. Si ricostruiscono fino a m blocchi rovinati, ovunque siano. Quali sono rovinati lo dice un controllo per blocco.
- **La prova:** su un ARW da 41,5 MB.

| Spazio in più | Danno | Esito |
|---|---|---|
| 1% (420 KB) | pezzo di circa 200 KB azzerato | **identico all'originale** |
| 1% | blocchi sparsi rovinati | **identico** |
| 1% | intestazione distrutta | **identico** |
| 1% | un blocco rovinato in più di quanti ne copre | rifiutato, file non toccato |
| 0,5% (210 KB) | come sopra, un blocco | **identico**; con due, rifiutato |

**Velocità:** 0,4 s per 41 MB nel prototipo. Nell'app, con codice nativo, sarà molto più veloce.

**Quanto costerebbe su tutto il G-SPEED** (16,8 TB):

| | 1% | 0,5% |
|---|---|---|
| RAW (11,0 TB) | 110 GB | 55 GB |
| Video (4,2 TB) | 42 GB | 21 GB |
| JPEG (0,3 TB) | 3 GB | 1,5 GB |

La proposta resta quella di prima: **spenta di default**, e da attivare solo sui file che non hanno nessun'altra copia (Space lo sa dal catalogo), magari solo sui RAW consegnati.

## Dove metterei ogni cosa in Space

- **Sempre attivi, senza spazio sui dischi:**
  - controllo CRC-64 ogni 64 KB (nel database di Space);
  - letture ripetute;
  - correzione di 1–2 bit;
  - elenco delle copie nascoste (anteprime, anteprime avanzate, export, catalogo) per ogni foto.
- **Azione "Recupera", con anteprima e conferma.** Il risultato è sempre un file nuovo e l'originale rovinato va in quarantena:
  - intestazione dal gemello;
  - riparazione dei pixel (RAW, tessera, JPEG);
  - ritrovare file cancellati da una scheda o da un disco, in sola lettura, salvando su un altro disco.
- **Opzione che costa spazio:** dati di riparazione allo 0,5–1%, solo dove non c'è nessun'altra copia.

**Etichette dei risultati.** Ogni file recuperato porta un'etichetta che dice com'è stato recuperato:
- "identico all'originale" (verificato con l'impronta);
- "intestazione ricostruita";
- "ricostruito in parte".

## Dati di prova

La copia del catalogo, la scheda finta e i file di prova erano tutti nella cartella di lavoro e li ho tolti. Sul BigDisk e sul G-SPEED non ho scritto niente in questa parte.
