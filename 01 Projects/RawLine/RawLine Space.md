# RawLine Space: ricerca e proposta di prodotto

Data: 2026-11-11. Nuova app della famiglia RawLine, dopo [[RawLine Rename]] e [[RawLine Selects]]. Serve a **riordinare, catalogare e alleggerire** un archivio fotografico professionale. Non è un'app di backup. Come le altre, più avanti confluirà in [[RawLine]], e il motore va scritto in RawlineKit fin dal primo giorno.

Obiettivo: l'app di cui un professionista si fida per mettere le mani su 40–100 TB di lavoro dei clienti. Prima viene la sicurezza, poi la comodità. Funziona al 100% offline, come tutta la famiglia.

> Le cose dette da Andrea sono segnate **(Andrea)**. Le proposte mie, nate dalla ricerca, sono segnate **(proposta)** e vanno confermate.
> La ricerca completa, app per app, è nelle 14 note in `research_notes/RawLine Space/`. Ogni dato lì è segnato come verificato o dedotto.
> **Analisi di fondo (11 nov):** [[RawLine Space - Analisi]] rilegge tutto questo documento e propone scelte di architettura, correzioni e l'ordine delle uscite. Sono proposte: valgono solo dopo la conferma di Andrea.

---

## 0. Regola che non si tocca: sicurezza professionale (Andrea, 11 nov)

La paura di ogni professionista è un file corrotto, cancellato o modificato per sbaglio. Space deve essere iper solida:

- **Mai toccare il contenuto** di RAW, XMP, video ed export durante il riordino. Si spostano e si rinominano file e cartelle, punto.
- **Tutto è un piano, niente agisce da solo.** Prima si prepara, poi si guarda l'anteprima, poi si conferma (sezione 3).
- **Storico persistente:** ogni operazione resta in un registro su disco, che sopravvive a chiusura, crash e riavvio. Si torna indietro quando si vuole, anche giorni dopo.
- **Nessuna eliminazione immediata e nessuna eliminazione definitiva di default** (sezione 6).
- **Un crash o un disco scollegato a metà** lasciano l'archivio coerente, e l'operazione si riprende.

## 0bis. Ordine d'importanza (deciso da Andrea l'11 nov)

1. **Le fondamenta, sotto tutto:** registro, istantanee, ripristino, quarantena, le cinque porte (sezioni 3 e 6). Senza queste nessuna funzione esce.
2. **Le due funzioni principali, alla pari:**
   - **Riordino intelligente** (sezione 4): capire una cartella disordinata per giornate, luoghi e servizi; i clienti sparsi negli anni e il verso opposto; lo schema dell'archivio con le impostazioni per cliente.
   - **Libera spazio** (sezione 5): tenere export e RAW usati, con l'abbinamento a più punti d'attacco.
3. **Poi:** catalogo dei dischi (sezione 7), che serve anche alle due principali, e Consolida (sezione 7bis).

## 0ter. Cosa dice l'archivio vero (lettura del G-SPEED, 11 nov, solo nomi e dimensioni)

Lettura fatta in sola lettura, senza aprire le foto e senza scrivere niente sul disco. Il G-SPEED (38 TiB, HFS+) contiene **15,3 TiB in 671.646 file**.

- **Cosa occupa lo spazio.** I RAW sono circa 10,4 TB: ARW 7,3 TB, CR2 1,9, CR3 0,75, DNG 0,37, RAF 0,07. I video circa 3,9 TB: MP4 2,3, MXF 1,1, MOV 0,5. I PSD e PSB 480 GB, i JPEG 277 GB, i TIFF 170 GB. **Il video è un quarto dell'archivio**, quindi la domanda sui video non è secondaria.
- **Struttura.** Le cartelle sono per anno, ma gli anni non sono uniformi: `2020:2021`, `2022`, `2023:2024`, `2024`, `2025`, `2026`. A fianco ci sono cartelle per progetto o cliente fuori dagli anni (Forever, GRIVEL, Namibia, Patagonia, DRONE, SSDSandisk, Personale). Dentro gli anni ci sono i servizi, nominati in tanti modi diversi: `210325_LaSportiva_…`, `20260403 - Les Dames Anglaises`, `Noli Home - Calcara`, `2026Ottin`. Alcuni servizi sono già divisi per giorno (`Day1 Revelstoke`, `240304`).
- **Doppioni sullo stesso disco, già trovati.** Gli stessi servizi stanno sia in `2023:2024` sia in `2024`: Courmayeur Winter 23:24 (183 GB identici), AVF Toscana (69 GB) e tre lavori Noli Home (Calcara, Max Pila, Trossello). Nei Noli Home la versione in `2024` contiene tutta quella vecchia più altri file: è un caso da manuale per Consolida. Quattro cartelle sono doppie tra `SSDSandisk` e `GRIVEL` (circa 85 GB). In tutto ci sono **circa 350 GB di doppioni evidenti** solo confrontando nome e dimensione, da confermare con gli hash.
- **Export.** Ci sono almeno 30 modi diversi di chiamare la cartella export: `Export`, `export`, `JPG`, `Web`, `ExportDay1`, `Export_Cliente_Passerini`, `… - Export`, `per stampa`. Space deve riconoscerli tutti, e lo schema dell'archivio può uniformarli.
- **Libera spazio, ordine di grandezza.** In 85 servizi che hanno sia RAW sia export, circa **7 TB di RAW non trovano un export con lo stesso nome**. È una stima grezza, fatta solo per nome, senza leggere stelle ed elaborazioni. Il dato vero sarà più basso, perché vanno tenuti i RAW con stelle o sviluppi. Ci sono poi 11 servizi (circa 390 GB) in cui **nessun** export ha il nome del RAW, come un matrimonio con 784 export: lì gli export sono stati rinominati e serve l'abbinamento a più punti d'attacco.
- **XMP e cataloghi.** Ci sono 291.508 RAW, di cui 166.716 con l'XMP accanto: **circa 125.000 RAW non hanno XMP**, quindi le loro elaborazioni e stelle, se ci sono, stanno solo nel catalogo. Il catalogo attivo non è sul G-SPEED ma sul Mac (`~/Pictures/Lightroom/…v13-3.lrcat`); sul G-SPEED ci sono solo cataloghi vecchi, in `2020:2021/Lightroom`. Ci sono anche circa 12.000 file `.cop` di Capture One e 912 `.acr`: Space deve leggere anche quelli come segni di elaborazione.
- **Cartelle troppo grandi.** `2020:2021/2020` e `2020:2021/2021` contengono un anno intero ciascuna (27.000 e 18.000 RAW): sono le candidate ideali per il riordino in giornate e servizi.

---

## 0quater. Anche i video (deciso da Andrea l'11 nov)

Space tratta foto **e video** fin dall'inizio: sul G-SPEED il video è circa un quarto dell'archivio. Prima proposta, da approfondire:

- **Famiglie anche per i video.** Ogni clip si muove insieme ai suoi file d'accompagnamento: gli XML delle Sony (`C0001M01.XML`), le cartelle della scheda (`PRIVATE/M4ROOT`, `XDROOT`), i file del drone (SRT, LRF), i 360 (`.insv`), l'audio WAV separato. Una clip non si separa mai dal suo XML.
- **Riordino.** La data e l'ora si prendono dai metadati della clip e dall'XML, non dalla data del file. In più servono corpo e drone, e GPS dove c'è (droni, action cam). Si riusano le stesse giornate e sessioni delle foto, e anche il riconoscimento dello stesso servizio quando foto e video stanno in cartelle diverse.
- **Libera spazio sui video (proposta):**
  1. **file rigenerabili:** proxy, media ottimizzati, file di render e cache di Final Cut e DaVinci. Si possono togliere senza perdere niente, perché l'app li ricrea. Spesso è la vincita più facile;
  2. **girato non usato:** si tengono il master consegnato e le clip usate nei progetti, letti dalle librerie di Final Cut (`.fcpbundle`) e dai progetti di DaVinci, sempre in sola lettura. Il resto va in quarantena, con le stesse regole delle foto;
  3. **doppioni** di clip copiate più volte (scheda, SSD, disco).
- **Mai toccare le librerie di Final Cut e i progetti di DaVinci dall'interno.** Si leggono soltanto. Se si spostano le clip, la libreria va ricollegata: c'è lo stesso problema dei cataloghi di Lightroom, con un avviso e una guida al ricollegamento.

## 1. Cosa abbiamo imparato dalle altre app

### 1.1 Il mercato in una tabella

| App | Che cos'è | Il pezzo da prendere | Il difetto da evitare |
|---|---|---|---|
| **Diem** (Sam Kolder, Diem Data Management, Mac/Win, beta) | Catalogo locale dei dischi, sfogliabili da scollegati. Tre livelli di scansione (Metadata ~20 min, Light ~50 min, Deep ~2 h per 4 TB). | **Gather**: un album di file sparsi su più dischi; l'app dice quali dischi collegare e copia tutto in una destinazione. Ricerche salvate che si aggiornano, tag validi su tutti i dischi, mappa, volti. | Niente di documentato su verifica, annulla o registro. AI opzionale che può passare dal cloud, account obbligatorio, telemetria. Da 12 $/mese. |
| **Hazel** (Noodlesoft, 42 $) | Regole che sorvegliano cartelle e spostano o rinominano in automatico. | Le regole lette come **schema dell'archivio**. Il popover ✓/✗ che spiega perché un file corrisponde. **App Sweep**: elenco da spuntare, "Tieni tutto", "Rimetti a posto". | Azioni automatiche in sottofondo, sovrascrittura silenziosa, tentativi infiniti. Anteprima solo un file alla volta. Lenta e fragile su cartelle profonde (80.000 foto in più di una settimana). Usa le date del file, non dello scatto. |
| **Big Mean Folder Machine** (30 €) | Ricostruisce gerarchie fino a 4 livelli (per data EXIF, nome, tipo), divide in lotti, unisce. Copia di default. | Un criterio per livello; la cartella "Altri" per i file senza dato, dichiarata in anteprima con il motivo. | Una versione è stata **ritirata perché l'anteprima non corrispondeva a ciò che faceva**. Niente annulla, niente verifica, non tiene insieme RAW e XMP. Ferma dal 2018. |
| **NeoFinder** (9.3.1, 40 $) | Catalogo storico dei dischi: miniature, EXIF/XMP, GPS su mappa, ricerca a 16 criteri. | **Un catalogo per disco**; trova i **file senza copia** su nessun altro disco. QuickUpdate al ricollegamento. | Circa **54 KB per file** (su 100 TB sarebbero 100–270 GB di catalogo). Solo MD5, spento. Nomi dei luoghi presi da internet. Riconosce i dischi con un file nascosto che si copia nei cloni. Interfaccia densa. |
| **Offline Files, DriveShelf, DriveVault, DriveBuddy** (2025–26, 10–100 $) | Nuova ondata di cataloghi semplici per dischi scollegati. | DriveShelf riconosce il disco dalla sua identità, non dal nome; raggruppa i dischi per cliente, progetto e anno. **DriveVault segnala i "buchi di backup"**, cioè i file presenti su un disco solo. | Doppioni trovati solo con nome e dimensione (falsi positivi). Nessuno legge bene stelle ed etichette dagli XMP. |
| **Tusk** (79 $, luglio 2026) | Sa dove sta ogni copia (dischi e cloud) e libera spazio sul Mac. | **"Elimina" solo se ogni copia ha lo stesso hash (BLAKE3)**, e si blocca se un disco è scollegato. Tabella file × disco con stati chiari (Synced, Partial, Missing on X…). | Ricollegando un disco controlla solo dimensione e data, quindi non vede i file rovinati col tempo. Licenza che chiede la rete. Limite di 100.000 file per progetto. |
| **Hedge OffShoot, Pomfort, ShotPut Pro + ASC MHL** | Copia verificata del cinema: l'hash si calcola leggendo, poi si rilegge la destinazione e si confronta. | Lo standard **ASC MHL** (cartella `ascmhl/`, manifesti immutabili, catena di custodia). **Mai cancellare l'originale con la verifica "solo dimensione".** | Un MHL unico per disco scala male con milioni di file: meglio uno per servizio. |
| **Photo Mechanic Plus** | Catalogo con anteprime per i dischi scollegati. | Tre stati per foto (presente, non disponibile, fuori catalogo); RAW+JPEG trattati come un'unità. | **Camera Bits ha smesso di venderlo** perché il catalogo dipende da una tecnologia di terzi non più supportata, e non c'è un modo per esportarlo. Photo Mechanic normale continua. |
| **Lightroom Classic / Capture One** | Cataloghi SQLite con percorsi assoluti. | Se si sposta un albero intero **senza rinominare i file**, basta ricollegare la cartella più alta. | Nessun plugin sa ricollegare in massa; l'SDK di Lightroom non lo permette. |
| **Peakto** (Cyme) | Meta-catalogo: legge Lightroom, Capture One, Foto. | Doppioni con **slider di somiglianza e regole ordinate** su quale copia tenere (prima il RAW, poi il voto, la risoluzione…), mai eliminazione automatica. | Si blocca oltre 200.000 foto; licenza online. |
| **Excire Foto 2027** (249 $) | AI tutta locale: parole chiave, volti, OCR, doppioni. | Indice usabile a disco scollegato; riaggancio automatico del disco. | ~25 GB di anteprime ogni 100.000 foto; analisi lenta. |
| **Kyno, Archiware P5, CatDV** | Media management e archiviazione (anche su LTO). | P5: al posto del file archiviato resta un **segnaposto leggero** da cui vedere l'anteprima e farselo ridare. Ripristino che non sovrascrive mai. | Kyno perde i metadati se sposti un file nel Finder. P5 è costoso e pensato per tecnici IT. |
| **DaisyDisk, GrandPerspective** | Mappe visive dello spazio. | Il **Collector**: si parcheggia ciò che si vuole togliere, poi si decide. | DaisyDisk elimina **in modo definitivo, senza Cestino**. |
| **PhotoSweeper, Gemini, Czkawka, dupeGuru** | Cercatori di doppioni. | **Cartelle di riferimento** da non toccare mai; la spiegazione di ogni scelta automatica; cache degli hash valida a disco staccato. | Annulla valido solo nella sessione aperta; eliminazione definitiva dove non c'è Cestino. |
| **IMatch, Photo Supreme, ExifTool, Elodie, Phockup, CCC, ChronoSync** | Altre app (vedi `Altre app.md`). | IMatch riconosce i dischi dal seriale e ha il comando Relocate; Elodie ha schemi con ripiego (`%album\|%location`); Phockup ha la prova a secco; CCC ha la **SafetyNet**. | Geocodifica online (Advanced Renamer). |

### 1.2 Il vuoto che Space può occupare
1. **Nessuna app riordina sapendo cosa c'è dentro.** Le altre o riordinano a regole cieche (Hazel, BMFM) o catalogano senza riordinare (NeoFinder, Diem). Space conosce date, GPS, fotocamera, stelle e sviluppi dagli XMP, e presenza nei cataloghi.
2. **Nessuna libera spazio con criterio fotografico.** Tusk sa *dove* sono le copie, ma non *cosa* è inutile. Oggi chi vuole farlo usa script fragili.
3. **Nessuna porta la sicurezza del cinema in un archivio fotografico.** Checksum, MHL, registro, ripresa e ripristino esistono, ma sparsi tra app diverse.
4. **Il catalogo di Photo Mechanic Plus è sparito dal mercato.** Chi lo usava per l'archivio cerca un'alternativa.

---

## 2. Principi

1. **Niente si muove da solo.** Space suggerisce, Andrea decide.
2. **L'anteprima è il piano.** Quello che si vede è esattamente ciò che verrà eseguito, non una sua imitazione (lezione di BMFM).
3. **Ogni passo si annulla**, tutto insieme o file per file, anche dopo aver chiuso l'app.
4. **Si legge tutto, si scrive il minimo.** Il contenuto dei file non si tocca.
5. **Una foto è una famiglia:** RAW, XMP, JPEG gemello ed eventuale WAV si muovono sempre insieme.
6. **I dischi staccati sono normali**, non un errore.
7. **Offline**, anche la licenza: analisi con Vision/Core ML, luoghi da un database incluso nell'app.
8. **Stessa famiglia:** finestra, grafite, parole e gesti di Rename e Selects.

---

## 3. Il flusso di lavoro: cinque porte prima di toccare un file (Andrea, 11 nov)

1. **Scegli cosa fare e confermi l'intenzione.** Per esempio: "Riordina la cartella 2026", "Raggruppa i clienti", "Libera spazio su Noli Home 2024". Una prima conferma: "Vuoi preparare un riordino? Non verrà toccato niente finché non lo applichi."
2. **Laboratorio.** Space propone (giornate, luoghi, clienti simili, schema) e Andrea sposta, rinomina, unisce, divide e trascina. Si lavora su una **copia virtuale** dell'albero: su disco non succede niente.
3. **Genera anteprima.** Space mostra l'albero finale navigabile, **prima e dopo affiancati**, con miniature, conteggi e GB per cartella. Accanto a ogni proposta c'è il perché (✓/✗ come in Hazel). Un esempio: "in *Altri* perché senza data di scatto".
4. **Controllo finale.** Un riepilogo che contiene:
   - numero di file e cartelle spostati e rinominati, GB spostati;
   - spazio che si libera **davvero**: i cloni APFS e gli hard link non si contano;
   - conflitti (nomi doppi, permessi, disco quasi pieno);
   - cartelle presenti in un catalogo di Lightroom o Capture One;
   - modalità scelta (sezione 3.1);
   - tempo stimato.

   Se c'è un conflitto non risolto, il pulsante per applicare non compare.
5. **Conferma dosata sul rischio (deciso da Andrea l'11 nov, sostituisce il "tieni premuto 5 secondi" su tutto; dettagli e motivi nella sezione 8bis.5):**
   - **spostare e rinominare**, che si annullano sempre: un pulsante con verbo e numeri ("Sposta 2.340 file") e l'annulla sempre in vista;
   - **mettere in quarantena:** pressione prolungata di 1,5–2 s (regolabile) con l'anello che si riempie, più un'alternativa da tastiera e VoiceOver (⌘Invio con foglio di conferma);
   - **eliminare per sempre**, cioè svuotare la quarantena: si scrive il nome della cartella.
   - La conferma dell'intenzione (porta 1) e il controllo finale (porta 4) possono diventare un solo riepilogo.

Subito prima di applicare, Space ricontrolla che sul disco non sia cambiato niente dall'anteprima. Confronta identificativo del file, dimensione e data di modifica, file per file, appena prima di ogni passo. Se qualcosa è cambiato, si ferma e rigenera l'anteprima.

Durante l'esecuzione si può mettere in pausa. Alla fine c'è un rapporto, e l'operazione entra nello **Storico** col pulsante "Ripristina com'era". **(proposta)** Le proposte che Andrea rifiuta non si ripresentano.

### 3.1 Dove si applica: tre modalità a scelta (Andrea, 11 nov)

| Modalità | Come funziona | Spazio in più | Quando |
|---|---|---|---|
| **Copia su un altro disco** (consigliata) | La nuova struttura viene scritta su un altro disco. Ogni file viene riletto e confrontato con l'hash; l'originale resta intatto. | Quanto l'archivio | Quando c'è un disco libero. |
| **Clone sullo stesso disco** (proposta) | Solo su APFS: la nuova struttura nasce accanto alla vecchia senza occupare spazio. Si verifica, poi si toglie la vecchia. | Quasi zero | Archivi enormi su APFS. **Non funziona sul RAID G-SPEED**, che è HFS+ (verificato sul Mac). |
| **Direttamente sulla sorgente** | Spostamenti e rinomine sul posto, con registro e ripristino. Space lo sconsiglia e lo dice, ma lo permette: con 100 TB una copia non si fa. | Zero | Quando non c'è alternativa. |

Regole tecniche **(proposta, provate sul Mac dall'agente)**:
- **Sullo stesso disco** si usa una rinomina atomica che non sovrascrive mai (`RENAME_EXCL`, già usata da `SafeRenamer` in Rename). Funziona anche sull'HFS+ del G-SPEED.
- **Tra dischi diversi:**
  1. si copia calcolando l'hash XXH128 durante la lettura (circa 35 GB/s sul Mac: il limite è sempre il disco);
  2. si forza la scrittura su disco (`F_FULLFSYNC`, o `fsync` dove non c'è, annotandolo);
  3. si rilegge la destinazione e si confronta;
  4. solo se l'esito è "verificato", file per file, **Space chiede la conferma** per togliere l'originale, che va in quarantena (sezione 3.2).
- **I conflitti di nome si cercano ignorando maiuscole e forma Unicode**, perché HFS+ e APFS trattano gli accenti in modo diverso.
- **Per elencare milioni di file** si visita una cartella alla volta e l'EXIF si legge senza decodificare l'immagine.
- **Gli snapshot APFS non si possono usare**: Apple li concede solo alle app di backup. La sicurezza la fanno il registro e la quarantena.

### 3.2 Spostare: dentro lo stesso disco o da un disco all'altro (deciso da Andrea l'11 nov)

Per Andrea "spostare" vuol dire due cose diverse, e Space le tratta in modo diverso.

**Dentro lo stesso disco (riordinare le cartelle): consentito.** Il file fisicamente non lascia il disco. Cambia solo il percorso, con una rinomina atomica che non sovrascrive mai. È l'operazione meno rischiosa. Basta il pulsante con verbo e numeri. Ogni spostamento finisce nel registro e si annulla.

**Da un disco all'altro: si copia, si verifica, poi si chiede.** Non esiste uno spostamento "alla Lightroom", che prende il file e lo porta via in un colpo solo. È l'unica strada ammessa, senza scorciatoie e senza un'opzione per saltarla:

1. **Copia.** L'hash XXH128 si calcola mentre si legge l'originale.
2. **Verifica a più passaggi, sotto ogni aspetto:**
   - **contenuto:** si scrive davvero sul disco (`F_FULLFSYNC`), poi si rilegge la destinazione senza la cache del sistema e si confronta l'hash byte per byte;
   - **completezza:** stesso numero di file e cartelle e stessi byte totali, servizio per servizio. Nessuna famiglia si spezza: RAW, XMP, JPEG gemello e WAV ci sono tutti;
   - **nomi:** identici, anche negli accenti e nelle maiuscole;
   - **metadati del file:** date di creazione e modifica, etichette e colori del Finder, attributi estesi, permessi;
   - **leggibilità (proposta):** su un campione, o su tutti se Andrea lo chiede, i RAW e gli export si aprono e danno l'anteprima.
3. **Rapporto.** "2.340 file copiati e verificati, 186 GB, 0 differenze". Se c'è anche una sola differenza, quel file resta "non verificato". Il suo originale non si tocca, e Space propone di ricopiarlo.
4. **Conferma separata per togliere l'originale.** Solo ora Space chiede: "Completa lo spostamento: togli gli originali da *G-RAID 2*?". Non succede mai da solo e mai nello stesso clic della copia. Prima di togliere, Space ricontrolla rapidamente che la copia ci sia ancora e sia uguale, perché tra copia e conferma possono passare giorni. L'originale va in quarantena sul suo disco, come ogni eliminazione (sezione 6).
5. **Spostamento a metà.** Finché Andrea non conferma, lo spostamento resta nello Storico come "copiato e verificato, originali ancora presenti". Le due copie convivono senza problemi e lo spostamento si può completare o annullare quando si vuole. Annullarlo vuol dire togliere la copia, non toccare l'originale.

Se una copia nasce e si verifica sullo stesso disco, per esempio con un clone APFS, vale lo stesso schema: verifica, poi conferma per togliere la vecchia struttura.

---

## 4. Riordino e raggruppamento

### 4.0 Un'app per tutti, non solo per l'archivio di Andrea (Andrea, 11 nov)
Space deve adattarsi a chi organizza in modo diverso: professionisti di generi diversi, principianti, amatori con tanti scatti (per esempio avifauna). L'archivio di Andrea serve come **riferimento con dati veri** (sezione 0ter), non come modello imposto.

**Cosa dice la ricerca (11 nov):** non esiste uno standard. Ognuno organizza secondo il proprio lavoro, e conta più essere coerenti che lo schema esatto. Sono emerse sette famiglie:

| Modello | Forma tipica | Chi lo usa |
|---|---|---|
| **Per data** | `Anno / AAAA-MM-GG_Evento` (a volte `Anno / Mese / Evento`) | Principianti, amatori, reportage, sport, agenzie. È il consiglio più diffuso. |
| **Anno → cliente → servizio** | `Anno / Cliente / AAAAMMGG_Servizio` | Professionisti con tanti clienti diversi. È il modello di Andrea. |
| **Cliente → anno → progetto** | `Cliente / Anno / AAAAMMGG_Progetto` | Commerciale con clienti fissi che tornano ogni anno. |
| **Progetto o viaggio a giorni** | `Viaggio / Day1_Luogo, Day2_Luogo…` | Viaggi, spedizioni, tour (le cartelle Forever di Andrea). |
| **Matrimoni ed eventi** | `AAAAMMGG_Sposi / RAW, Export, Album`, a volte con i secondi fotografi separati | Matrimoni, eventi. |
| **Natura e avifauna** | Cartelle per data o uscita. **Specie e luogo stanno nelle parole chiave**, non nelle cartelle | Naturalisti e amatori. Molti esperti sconsigliano le cartelle per soggetto: se una foto esce dalla cartella, l'informazione si perde. |
| **Ibrido foto+video** | `Progetto / Foto (RAW, Export) · Video (Girato, Progetto, Render) · Consegne` | Creator e videomaker. |

C'è poi il modello **"a secchi"** di Peter Krogh (The DAM Book): l'archivio è diviso in blocchi numerati della dimensione di un disco. Serve a chi archivia su più dischi, ed è utile per Consolida.

**Errori comuni da segnalare (dalla ricerca):**
- tutto in una sola cartella;
- troppi livelli (oltre 3–4);
- mesi scritti in lettere, che si ordinano male (Aprile prima di Gennaio);
- orologio della fotocamera sbagliato;
- cartelle con la sola data, che obbligano a ricordare cosa c'era.

**Consigli da seguire (dalla ricerca):**
- partire dalle importazioni nuove invece di rifare tutto l'archivio in una volta;
- spostare il progetto in archivio solo dopo la consegna;
- per i RAW scartati, molti li tengono da qualche settimana a qualche mese dopo la consegna, poi li tolgono, oppure seguono quanto scritto nel contratto.

**Come lo traduce Space (proposta):**
1. **Scelta assistita (deciso da Andrea l'11 nov).** Al primo avvio Space legge l'archivio e **consiglia un modello**, segnato come "Consigliato", spiegando perché (es. "il 70% dei tuoi servizi è già così"). L'ultima parola però è sempre dell'utente: sceglie il consigliato o un altro dei sette, e lo personalizza (livelli, nomi, eccezioni).
2. Accanto a ogni modello c'è un esempio fatto con le cartelle vere dell'utente, così si vede subito come diventerebbe l'archivio.
3. **Le proposte di riordino restano coerenti col modello dell'utente.** Space non impone il proprio: sistema le incoerenze dentro quel modello (anni accoppiati, nomi diversi, doppioni, export con 30 nomi).
4. **Le eccezioni sono normali:** un cliente grande o un progetto lungo possono vivere fuori dagli anni (Forever e GRIVEL per Andrea).
5. **Per chi organizza per soggetto (avifauna) (proposta, da decidere):** Space propone ricerche salvate per specie e luogo invece di cartelle. Scrivere parole chiave negli XMP sarebbe una funzione nuova da valutare: oggi Space non tocca il contenuto dei file.
6. **"Libera spazio" con un'età minima:** Space propone solo i progetti consegnati da almeno N mesi, con N scelto dall'utente.

Fonti:
- [Renamer.ai, organizzazione dei professionisti](https://renamer.ai/insights/photographer-file-organization-professional-workflow)
- [Markus Hagner, convenzioni sui nomi (2026)](https://markus-hagner-photography.com/how-to-build-a-photography-file-naming-convention-that-keeps-your-images-findable/)
- [SLR Lounge, cancellare o tenere i RAW](https://www.slrlounge.com/delete-raw-photos-archive-forever)
- [Fstoppers, flusso dopo un matrimonio](https://fstoppers.com/education/my-post-wedding-workflow-image-backup-and-cataloging-87643)
- [Singapore Birds, foto di uccelli](https://singaporebirds.com/blog/a-quick-way-to-organize-bird-pictures)
- [PetaPixel, gerarchie di parole chiave](https://petapixel.com/2025/04/03/how-to-craft-a-lightroom-keyword-hierarchy/)
- [Lightroom Killer Tips, perché non per data](https://lightroomkillertips.com/two-reasons-why-i-dont-organize-my-photos-by-date-in-lightroom/)
- [Amateur Photographer, guida per principianti](https://amateurphotographer.com/technique/improve-your-photography/beginners-guide-to-file-and-photo-management)
- [Fiveable, archivi di reportage](https://library.dev.fiveable.me/news-photography/unit-15/organizing-archiving-news-photographs/study-guide/8CwXL9qxE1Q1QB6w)
- [The DAM Book, cap. 4](https://www.oreilly.com/library/view/the-dam-book/9780596803353/ch04.html)
- [Il sistema a secchi](https://digital-photography-school.com/file-archiving-strategy-the-bucket-system/)
- [OWC, archiviare i progetti video](https://owc.com/blog/how-to-organize-video-project-files-for-worry-free-archival)
- [PostFlow, media per creator](https://thepostflow.com/post-production/post-production-workflows/media-management-for-solo-creators/)

### 4.1 Capire una cartella disordinata (Andrea)
Si dà a Space una cartella con più servizi mescolati. Space legge data e ora di scatto (non quelle del file, l'errore di Hazel), GPS e fotocamera, e propone:
- **giornate**, con un taglio intelligente per le notti lunghe, come la "Long night" di Rename;
- **sessioni**, cioè le grosse pause tra uno scatto e l'altro;
- **luoghi**, se c'è il GPS: nomi dei posti da un database offline incluso nell'app;
- **fotocamere diverse**, per esempio due corpi o un secondo fotografo;
- **(proposta)** una correzione dell'orologio della fotocamera, riusando ClockSync di Selects.

I file senza un dato non vengono indovinati: vanno in una cartella di ripiego scelta da Andrea, dichiarata in anteprima con il conteggio.

### 4.2 Clienti sparsi negli anni, e il verso opposto (Andrea)
- **Unire:** "Ho trovato *Noli Home* in 2024, 2025 e 2026, più *NoliHome* e *Noli-Home*. Vuoi raggrupparli in `Noli Home/2024/…`?"
- **Dividere:** "Questo cliente contiene 2024 e 2025. Vuoi portarli in `2024/Noli Home/…` e `2025/Noli Home/…`?"
- Andrea conferma sempre quali nomi sono lo stesso cliente, e Space se lo ricorda.

### 4.3 Lo schema dell'archivio (proposta, dalle regole di Hazel ed Elodie)
Andrea definisce una volta la forma dell'archivio, con i token di Rename e un valore di ripiego, per esempio `Anno / Cliente / AAAAMMGG_Servizio|Senza servizio`. Poi:
- si possono dare **impostazioni diverse per cliente** (Andrea);
- c'è un **controllo di salute in sola lettura**: ogni cartella risulta "conforme" o "fuori posto → dovrebbe stare in…", e diventa una proposta, mai un'azione;
- c'è un **elenco dei sinonimi dei clienti**;
- l'esempio si vede dal vivo su una cartella campione.

### 4.4 Altri suggerimenti di ordine (proposta)
Space segnala anche:
- cartelle vuote o chiamate "Senza titolo";
- **XMP senza RAW** e RAW senza XMP;
- export sparsi fuori dal loro servizio;
- cartelle enormi da dividere;
- nomi con caratteri che danno problemi su altri sistemi.

### 4.5 Unificare i nomi delle cartelle export e dei servizi (Andrea, 11 nov)
Sul G-SPEED la cartella export ha almeno 30 nomi diversi: `Export`, `export`, `JPG`, `Web`, `ExportDay1`, `Export_Cliente_Passerini`, `… - Export`, `per stampa`… Space propone di **uniformarli**.

1. **Riconosce le cartelle export** in due modi:
   - dal nome, con tutte le varianti (export, jpg, web, social, insta, stampa, consegna…);
   - **dal contenuto:** solo JPEG, TIFF o PSD, con date di creazione successive allo scatto, nati da RAW dello stesso servizio. Così trova anche le export con nomi strani.
2. **Propone un nome unico con il modello di Andrea (approvato l'11 nov).** Di solito Andrea consegna una versione alta e una web; per le campagne solo l'alta; a volte ci sono giri di revisione prima della consegna finale.
   ```
   Servizio/
     Export/
       Alta/            ← consegna finale (per le campagne c'è solo questa)
       Web/
       Revisioni/       ← solo se ci sono stati giri di revisione
         R1_AAAA-MM-GG/
         R2_AAAA-MM-GG/
   ```
   - Space riconosce Alta e Web anche nelle cartelle di oggi guardando la dimensione dei file (es. lato lungo sopra 4000 px = Alta, sotto 2500 px = Web). Le soglie le decide Andrea.
   - I giorni restano come sottocartelle: `Export/Alta/Giorno 1` al posto di `ExportDay1`.
   - **TIFF e PSD (Andrea, 11 nov):** oggi stanno in una cartella loro. I TIFF possono essere tre cose diverse: export di consegna, file intermedi nati dal RAW per lavorarli, oppure file nati da un PSD. Proposta:
     ```
     Servizio/
       Lavorazione/     ← PSD, PSB e TIFF di lavoro
       Export/
         Alta/          ← qui anche i TIFF consegnati
     ```
     Space distingue i TIFF **(proposta)** in quattro modi: se c'è un PSD con lo stesso nome è nato dal PSD; i 16 bit e i profili ampi (ProPhoto) fanno pensare a un file di lavoro; un TIFF accanto ad altri export di consegna è una consegna; nel dubbio chiede ad Andrea. I PSD non vengono **mai** proposti per "Libera spazio" in automatico: contengono ore di ritocco. I **TIFF di lavoro nati da un PSD che esiste ancora** invece si possono proporre per "Libera spazio", perché si riesportano dal PSD. Anche qui si decide progetto per progetto (Andrea, 11 nov).
   - **Revisioni dopo la consegna (deciso l'11 nov):** Space può proporre di toglierle con "Libera spazio", tenendo solo il finale, ma **si decide progetto per progetto**. Non esiste una regola generale che le tolga in automatico.
3. **Fa lo stesso con i nomi dei servizi** (`210325_LaSportiva_…`, `20260403 - Les Dames Anglaises`, `2026Ottin`): propone un formato unico, per esempio `AAAAMMGG_Cliente_Servizio`, prendendo la data dal primo scatto. Lo stesso vale per le cartelle anno (`2020:2021`, `2023:2024` → un anno per cartella).
4. **Si vede tutto in anteprima prima/dopo** e si applica con le cinque porte. Andrea può tenere un'eccezione per cliente, per esempio "per questo cliente la cartella si chiama come vuole lui".
5. **Attenzione al catalogo:** se una cartella export è stata importata in Lightroom, rinominarla la rende mancante. Space lo segnala nel controllo finale, con la guida al ricollegamento (sezione 8).

---

## 5. Space: liberare spazio sui progetti vecchi (Andrea)

Si dà a Space un progetto (RAW, XMP, export, video). Space propone tre strade:
- **A.** tenere solo gli export;
- **B.** tenere solo gli export JPEG;
- **C.** tenere gli export e i RAW con XMP che li hanno generati, eliminando gli scatti non usati.

Per ognuna mostra lo spazio che si libera davvero, per esempio "C: tieni 214 RAW su 3.180, liberi 118 GB".

### 5.1 Abbinare export e RAW con più punti d'attacco (Andrea)
I nomi `DSC01234` si ripetono ogni 10.000 scatti e tra due corpi: un solo criterio non basta. Space prova le strade dalla più sicura alla meno sicura:

1. **Catalogo e servizi di pubblicazione di Lightroom**, quando ci sono.
2. **Nome del RAW scritto nell'export** (`xmpMM:PreservedFileName`, `crs:RawFileName`), più l'ora di scatto. Lightroom però lo scrive **solo esportando con "Tutti i metadati"**. Con "Solo copyright" sparisce perfino la data di scatto. Capture One di default esporta senza metadati.
3. **Impronta dello scatto:** numero di serie del corpo + data e ora al centesimo. È la chiave pratica, perché le note del produttore di solito non arrivano nei JPEG. Il contatore degli scatti non basta come chiave unica: sui Sony recenti conta solo l'otturatore meccanico, Fuji e Canon lo possono azzerare.
4. **Nome originale nel nome del file.** I nomi di RawLine Rename finiscono col nome originale, quindi l'abbinamento regge anche dopo la rinomina.
5. **Identificativi XMP del documento.** Va provato con i file di Andrea se puntano al RAW.
6. **Somiglianza dell'immagine in locale:** l'anteprima incorporata nel RAW confrontata con Vision. È l'unica strada per gli export "Solo copyright".
7. **Indizi di contesto:** stessa cartella di servizio, stessa giornata.

**Il primo che funziona vince (Andrea), con un controllo in più (proposta).** Si prende il primo criterio che trova la coppia, ma solo se gli altri criteri disponibili **non lo contraddicono**. Esempio: il nome coincide ma la fotocamera è diversa. Quella coppia va nel mucchio "da controllare", che Andrea guarda a mano. Gli abbinamenti deboli (strade 6 e 7) non liberano mai spazio senza una sua conferma.

### 5.2 Paracadute (proposta)
- **Non si eliminano mai i RAW con stelle, flag, etichetta colore o sviluppi** (XMP o catalogo), salvo richiesta esplicita.
- **Allarme sulle quantità:** "Stai per eliminare il 98% del progetto" chiede un'altra conferma.
- **(da Tusk) "Elimina solo se esiste una copia verificata altrove", come opzione:** l'hash deve coincidere su un altro disco collegato. Se il disco del backup è scollegato, Space si ferma. Non è attiva di serie: per gli scatti non usati dei lavori vecchi non serve (vedi 8bis.4, punto 2).
- **(da P5) Segnaposto leggero:** al posto dei RAW tolti resta un piccolo file con anteprima e metadati, che dice dove trovare la copia di sicurezza.
- **Video:** da decidere (vedi le domande).

---

## 6. Storico, ripristino ed eliminazione (Andrea)

- **Registro delle operazioni:** un database SQLite sul Mac, scritto in modo forzato sul disco. Ogni passo viene annotato *prima* di agire, con il suo stato (preparato, fatto, verificato). Alla riapertura Space ricontrolla ogni passo sul disco e propone di completare o di tornare indietro.
- **Una copia del registro su ogni disco** (proposta), in una cartella nascosta `.rawline-space/`. Così lo storico viaggia col disco.
- **Istantanea della struttura** prima di ogni operazione: cartelle, nomi, dimensioni, hash. "Ripristina com'era" la riapplica e **non sovrascrive mai** quello che nel frattempo è stato messo al suo posto.
- **Storico con le date: "Ripristina schema precedente" (deciso da Andrea l'11 nov).** Lo Storico è una linea del tempo, disco per disco e cartella per cartella. Ogni voce dice data e ora, cosa è stato fatto, quanti file, dove, ed è in uno di questi stati: fatto, verificato, in attesa di conferma, annullato. Ci si può tornare anche giorni o mesi dopo, con l'app chiusa e riaperta nel frattempo o il Mac riavviato. Si può annullare una sola voce, oppure scegliere una data e tornare allo schema di allora. Space annulla le operazioni una alla volta, dalla più recente all'indietro.
  - **Il ripristino passa dalle stesse porte:** anteprima prima e dopo, poi conferma. Non è un salto nel buio.
  - **Quello che è cambiato dopo resta:** foto aggiunte nel frattempo, XMP modificati da Lightroom o Camera Raw, cartelle nuove. Space le mostra nell'anteprima, porta gli XMP insieme al loro RAW e non cancella niente di nuovo. Se un nome è già occupato, lo segnala come conflitto da risolvere a mano.
  - **Annullare uno spostamento tra dischi** che è già stato completato vuol dire ricopiare all'indietro con la stessa verifica a più passaggi. Gli originali tornano dalla quarantena se ci sono ancora, altrimenti si ricopiano dalla destinazione. Per questo lo Storico avvisa prima che la quarantena di un'operazione scada.
  - **Il registro sopravvive ai problemi:** il database è sul Mac (SQLite, scritture forzate su disco), con una copia su ogni disco coinvolto, mai sul G-SPEED finché vale la regola di sola lettura. Si esporta anche come file leggibile (CSV o JSON), così lo schema originale si ricostruisce anche senza Space.
- **Quarantena su ogni disco (sul modello di CCC SafetyNet).** Eliminare vuol dire spostare il file in una cartella di quarantena sullo stesso disco. È uno spostamento istantaneo e reversibile, con un manifesto. Ha una scadenza scelta da Andrea (es. 30 giorni). Va detto chiaramente che lo spazio si libera davvero solo quando la quarantena si svuota, e lo svuotamento chiede un'altra conferma tenendo premuto. Il Cestino di sistema resta un ripiego.
- **Certificato ASC MHL** (confermato da Andrea l'11 nov sera: le copie sono sempre verificate, al livello del cinema) per ogni servizio copiato o alleggerito, scritto in Swift dentro l'app, tutto offline. Algoritmo xxh128 (SHA-256 lo standard non lo ammette). Si prova la compatibilità con lo strumento `ascmhl` e con MediaVerify di Pomfort.

---

## 6bis. Integrità dei file: tutti gli standard, senza ridondanza in più (deciso da Andrea il 13 nov)

**Obiettivo (Andrea):** usare il più possibile gli standard che esistono per prevenire, controllare ed essere sicuri che i file siano copiati bene e non si danneggino. Tutto questo senza creare altra ridondanza e senza occupare altro spazio, perché oggi lo spazio costa troppo. Le funzioni più pesanti si possono attivare o disattivare. Alcune sono spente di default.

**L'idea di fondo.** Senza spazio in più non si può riparare un file da solo. Si può però:
1. **accorgersi subito** di ogni danno;
2. **sapere sempre dove esiste un'altra copia buona**. Per Andrea sono i vecchi dischi e il BigDisk. Space li conosce dal catalogo, e da lì si ripara.

Il costo va pagato in tempo di lettura, non in spazio.

### Sempre attivi (spazio occupato: quasi zero)

| Controllo | Da quale standard o lezione | Costo |
|---|---|---|
| **Copia verificata**: impronta calcolata leggendo, scrittura forzata, rilettura dal disco senza cache, confronto di contenuto, date, permessi ed etichette | Copia verificata del cinema (Hedge, Pomfort, ShotPut) | Tempo: ogni file si legge due volte |
| **Registro scritto prima di agire**, impronta registrata prima della rinomina finale | Database (WAL), git | Pochi KB per operazione |
| **Certificato ASC MHL** per ogni servizio copiato | ASC MHL (cinema) | Un file XML di pochi KB per servizio |
| **Impronta di ogni file nel catalogo** sul Mac, presa al primo inventario | Livelli di conservazione digitale NDSA ("fixity") | Circa 100 byte per file: 70 MB per 671.000 file |
| **Corruzione silenziosa**: allarme se il contenuto cambia ma la data di modifica no | NDSA, lezioni Synology e Drobo | Niente in più |
| **Controllo al riattacco**: se un disco è stato staccato male, prima di scrivere si controllano il file system e si rileggono per intero i file dell'operazione interrotta | Nato dalle prove del 13 nov | Minuti |
| **Un disco assente non è un disco vuoto**: senza sorgente non si parte | Lezioni Dropbox e Resilio | Niente |
| **Stop al primo errore** di lettura o scrittura su un disco, che passa in sola lettura | Pratica DIT | Niente |
| **File incompleti riconosciuti**: dimensione zero, JPEG senza la fine, MP4 o MOV senza indice, RAW più corti del previsto. Non contano mai come copia valida né come doppione | Lezioni sulle copie "riuscite ma rovinate" | Lettura della testa e della coda del file |
| **Formato e rischio del disco**: avviso su exFAT, su un disco senza journal, su una scrittura forzata che il disco non accetta | Note tecniche (sezione 3.1) | Niente |
| **Contatore delle copie** per ogni lavoro: "questo servizio esiste su 1 disco" | Regola 3-2-1, DriveVault | Niente, è nel catalogo |
| **Rapporto leggibile** di ogni operazione: copiato, verificato, saltato e perché | Lezioni "me ne accorgo troppo tardi" | Pochi KB |

### Attivabili, spenti di default (costano tempo, non spazio)

| Funzione | Da quale standard | Quando serve |
|---|---|---|
| **Riverifica periodica**: ogni mese rilegge una parte dell'archivio, per esempio un dodicesimo, e la confronta con le impronte salvate. In un anno ha ricontrollato tutto | NDSA, "scrub" di ZFS e Btrfs | Archivi fermi da anni. Sul G-SPEED un giro completo richiede circa 30 ore di lettura |
| **Riparazione da un'altra copia**: un file risultato rovinato si ricopia da un disco del catalogo che ha la stessa impronta, con la solita copia verificata | Nessuno lo fa per le foto | Quando la riverifica trova un danno |
| **Prova di leggibilità completa**: ogni RAW, JPEG e video viene aperto e decodificato, non solo confrontato | Pratica di Lensrentals e dei DIT | Prima di eliminare una sorgente, o sui lavori importanti |
| **Doppia lettura della sorgente**: la sorgente si legge due volte e le due impronte devono coincidere | Scarico del girato sul set | Dischi vecchi o sospetti |
| **Impronta SHA-256** in aggiunta a XXH128 | Manifesti d'archivio e tribunali | Quando un cliente o un archivio la richiede |
| **Esportazione BagIt** di un servizio: cartella con l'elenco delle impronte, ricontrollabile con qualunque strumento | BagIt (RFC 8493, Library of Congress) | Consegne d'archivio, lavori da conservare decenni |
| **Registro in formato PREMIS**: la storia di ogni file (copiato, verificato, spostato) in un formato standard degli archivi | PREMIS (Library of Congress) | Per chi lavora con archivi o musei |
| **Impronta salvata anche negli attributi del file**, così viaggia con il file | Pratica di alcuni strumenti di archivio | Solo sui dischi sbloccati, mai sul G-SPEED; scrive negli attributi, non nel contenuto |

### Riparazione in parallelo (chiesta da Andrea e provata il 13 nov)

Quando un controllo trova dei file rovinati (riverifica, controllo al riattacco, verifica di una copia), Space li ripara tutti insieme, più file alla volta. Il prototipo è `ripara.swift` in `research_notes/RawLine Space/Prototipi 13 nov/`.

1. **Controllo in parallelo:** rilegge i file e confronta ognuno con l'impronta registrata quando è stato copiato. Il numero di letture in parallelo dipende dal disco: poche sui dischi meccanici, di più sugli SSD.
2. **Ricerca della copia buona:** tra i dischi del catalogo, compresi quelli bloccati come il G-SPEED, che si aprono **solo in lettura**. Una copia vale solo se ha **esattamente l'impronta registrata**. Non basta che sia "diversa da quella rotta", perché anche l'altra copia può essere rovinata.
3. **Copia verificata** della copia buona su un nome temporaneo accanto al file rovinato, con la solita rilettura dal disco.
4. **Il file rovinato va in quarantena**, mai cancellato: può servire a recuperare a mano una parte. Poi la copia buona prende il suo nome, con la rinomina che non sovrascrive mai.
5. **Ogni passo va nel registro** prima di essere fatto.
6. **Se nessuna copia ha l'impronta giusta, Space non sceglie.** Il file resta com'è, segnato "da decidere", con l'elenco delle copie provate e del perché non vanno.

Nel prodotto la riparazione è un'azione con anteprima ("15 file rovinati, 15 riparabili dal disco X"), e Andrea la conferma una volta per tutti.

### Recupero quando non c'è un'altra copia (provato il 13 nov, report §8)

Il prototipo è `recupera.swift`. Tutti e due i metodi sono **sempre attivi**, perché non costano spazio sul disco:

1. **Letture ripetute.** Se una lettura fallisce, Space riprova un settore alla volta, con pause crescenti. Se il file torna integro, lo riscrive in un punto nuovo del disco, via dal punto debole, e lo segnala: quel disco sta invecchiando.
2. **Controllo ogni MB (CRC-64).** Si calcola durante la copia e occupa 8 byte per MB, lo 0,0008%: circa 130 MB per tutto il G-SPEED, nel database di Space e non sui dischi.
   - Dice quale MB di un file è rovinato.
   - Corregge da solo 1 o 2 bit cambiati per MB. La correzione si accetta solo se l'impronta dell'intero file torna identica.
   - Per i danni più grandi indica il punto esatto, così si capisce che cosa si è perso.

Il file rovinato non viene mai cancellato: va in quarantena anche qui.

### Recupero approfondito (provato la sera del 13 nov, report `Space recupero approfondito.md`)

- **Sempre attivi, senza spazio sui dischi:**
  - controllo CRC-64 **ogni 64 KB** invece che ogni MB: circa 2 GB nel database di Space per tutto il G-SPEED, localizza meglio e corregge 1–2 bit ogni 64 KB;
  - letture ripetute e correzione dei bit;
  - **elenco delle copie nascoste** di ogni foto: anteprime e anteprime avanzate di Lightroom, export, regolazioni nel catalogo.
- **Azione "Recupera", con anteprima e conferma.** Il risultato è sempre un file nuovo e l'originale va in quarantena:
  - **intestazione dal gemello:** i dati RAW tornano identici byte per byte; data e dati di scatto veri si rimettono dal catalogo;
  - **riparazione dei pixel:**
    - nel RAW per gli ARW compressi Sony e non compressi;
    - con l'anteprima di Lightroom per le tessere degli ARW senza perdita;
    - nei JPEG con punti di ripartenza (quasi tutti gli export di Lightroom);
  - **indice dei video Sony troncati:** provato con indice e fotogrammi identici all'originale, ma **messo da parte da Andrea il 13 nov**: per ora i video restano fuori da questa parte;
  - **ritrovare file cancellati** o schede formattate, in sola lettura, salvando su un altro disco.
- **Opzione che costa spazio, spenta di default:** dati di riparazione nostri (Reed-Solomon, come PAR2 ma scritto da noi) allo 0,5–1%, solo sui file senza nessun'altra copia. Per tutti i RAW del G-SPEED: 55–110 GB.

Ogni file recuperato porta un'etichetta: "identico all'originale" (verificato con l'impronta), "intestazione ricostruita" o "ricostruito in parte".

### Da valutare in futuro (costano spazio)

- **Dati di riparazione PAR2:** un file in più, circa il 5–10% dello spazio, che permette di ricostruire le parti rovinate senza un'altra copia. Andrea l'ha messo da parte il 13 nov come opzione futura. Da verificare la licenza: il programma più diffuso non si può incorporare in un'app chiusa.
- **Copie in più:** restano una scelta dell'utente. Space le conta e avvisa, non le crea da solo.

---

## 7. Catalogo dei dischi (Andrea, dalle idee di Diem, NeoFinder, DriveShelf, Tusk)

- **Quando si collega un disco, Space propone di catalogarlo.** Un catalogo per disco. Il disco si riconosce dall'UUID del volume, non dal nome, con un avviso se due dischi si somigliano (i cloni).
- **Livelli di catalogazione a scelta**, come Diem, con una **stima di tempo e di spazio prima di partire**: solo struttura e metadati; poi miniature; poi hash completi. Si può mettere in pausa e riprendere.
- **Obiettivo di peso: molto sotto i 54 KB per file di NeoFinder.** Le miniature si ricavano dall'anteprima incorporata nei RAW, in una dimensione scelta.
- **A disco scollegato** si naviga, si cerca e si vedono le miniature: "è sul disco *Archivio 42TB*, collegalo per aprirlo".
- **Ricerca su tutti i dischi** per cliente, data, luogo, fotocamera, **stelle ed etichette dagli XMP**: nessuna delle app nuove lo fa bene, e Selects gli XMP li scrive già. Ricerche salvate che si aggiornano da sole.
- **Doppioni a tre livelli** (proposta):
  1. identici, per hash;
  2. lo stesso scatto in un'altra forma (RAW e JPEG, export);
  3. simili, con Vision.

  Regole ordinate su quale copia tenere, sul modello di Peakto e dupeGuru, sempre con il perché. **Dischi di riferimento** che non si toccano mai.
- **Buchi di backup e copie uniche** (da DriveVault e NeoFinder): l'elenco dei file che esistono su un disco solo. Su 40–100 TB è forse la funzione più preziosa.
- **Mappa dello spazio** per anno, cliente e tipo di file.
- **Gather** (da Diem): si sceglie un insieme di file sparsi su più dischi, Space dice quali dischi collegare e li copia in una destinazione, con verifica.
- **(proposta) Riordino preparato a disco scollegato**, sul catalogo, e applicato quando il disco torna, dopo aver ricontrollato che non sia cambiato.
- **(proposta) Riverifica periodica dell'integrità:** rilegge gli hash e li confronta con quelli registrati, per scoprire i file rovinati col tempo (Tusk e NeoFinder non lo fanno). Ogni riverifica allunga la catena del certificato MHL.

---

## 7bis. Consolida: da tanti supporti a uno solo (Andrea, 11 nov)

> È **una** delle funzioni, non la principale: le priorità sono nella sezione 0bis.

Una funzione unica per tanti scenari: qualunque insieme di sorgenti verso qualunque destinazione.
- **Sorgenti:** dischi esterni, SSD, schede, vecchi DAS, cartelle sparse su più volumi.
- **Destinazioni:** un NAS, un DAS, un disco unico più grande.

Il motivo è lo stesso: uniformare e mettere ordine.

Esempio: 6–7 dischi da 10 TB riempiti negli anni, con copie dello stesso lavoro sparse e diverse tra loro. Si vuole portare tutto su un supporto nuovo **una volta sola, in ordine, senza doppioni e senza perdere niente**. Il problema è che nessuno sa più cosa c'è dove:
- su un disco ci sono i RAW con l'ultima elaborazione;
- su un altro ci sono gli stessi RAW con un'elaborazione più vecchia, però anche gli export JPEG;
- i TIFF stanno su due dischi;
- i PSD esistono su uno solo.

### Cosa fa Space
1. **Catalogo di tutti i dischi** (sezione 7). Si collegano uno alla volta, anche in giorni diversi.
2. **Riconosce lo stesso progetto su più dischi** anche se le cartelle si chiamano in modo diverso. Usa il nome simile, ma soprattutto **gli scatti in comune**: stessi hash o stessa impronta (numero di serie + ora al centesimo). Esempio: "*Noli Home 2024* sul Disco 3 e *NoliHome_shooting* sul Disco 6 hanno 2.940 scatti in comune: è lo stesso servizio."
3. **Costruisce la famiglia di ogni scatto, su tutti i dischi.** Per ogni foto raccoglie RAW, XMP, JPEG, TIFF, PSD, PSB e versioni con `-Modifica`, `_edit` o `-2`, e dice dove sta ciascuno. Esempio: "DSC01234: RAW su Disco 2 e Disco 5; elaborazione più recente sul Disco 5 (XMP del 3 marzo 2025); JPEG sul Disco 2; TIFF su Disco 2 e Disco 5; **PSD solo sul Disco 2**."
4. **Mostra il confronto per progetto**, una tabella pezzo × disco sul modello di Tusk:
   - cosa è uguale ovunque;
   - cosa c'è solo su un disco (**le copie uniche, da non perdere**);
   - cosa è diverso tra i dischi.
5. **Propone il progetto unito**, cioè la versione completa da mettere sulla destinazione: un RAW per scatto, l'elaborazione scelta, tutti gli export, i TIFF e i PSD da ogni disco, nello schema dell'archivio (sezione 4.3).
6. **Si applica con le cinque porte** (sezione 3) **in modalità copia**: i dischi vecchi restano intatti. Ogni file arriva sulla destinazione letto, scritto e riletto con l'hash, e per ogni servizio si scrive un certificato MHL.
7. **Solo dopo, se Andrea vuole**, Space dice quali dischi vecchi hanno *tutto* il loro contenuto verificato sulla destinazione. A quel punto quei dischi si possono svuotare o riusare. Space non li formatta mai da solo.

### Le elaborazioni in conflitto (deciso da Andrea l'11 nov: sceglie lui ogni volta)
Lo stesso RAW con due XMP diversi è il caso delicato. **Space non sceglie mai da solo: sceglie Andrea, ogni volta.**
- Ogni conflitto finisce nel mucchio "da controllare". Per ognuno Space mostra le due anteprime affiancate, la data di ogni XMP e le differenze (ritaglio, bianco e nero, stelle, etichette).
- Finché un conflitto non è risolto, quello scatto non entra nel progetto unito. Il resto del progetto può andare avanti.
- **(proposta)** Per non fare migliaia di clic restano scelte di Andrea, ma fatte in blocco: "per tutto questo servizio tieni il Disco 5", oppure "applica la stessa scelta agli scatti con le stesse differenze". Il riepilogo finale mostra sempre cosa è stato scelto e come.
- **(proposta)** Tra le scelte c'è anche "tienile tutte e due": l'altra elaborazione si conserva come seconda versione.

Attenzione: se le elaborazioni stanno solo dentro cataloghi di Lightroom diversi, uno per disco, e non negli XMP, Space le vede solo leggendo quei cataloghi (sezione 8).

### Cose pratiche (proposta)
- **Tempo misurato, non ipotizzato.** Prima di partire Space fa una breve prova di lettura e scrittura reale su ogni sorgente e sulla destinazione, e stima il tempo con la velocità vera. Il collo di bottiglia può essere il disco, la porta (USB, Thunderbolt) o la rete (1, 2,5, 5 o 10 Gbit). La stima si aggiorna durante la copia.
- **Più sorgenti insieme** quando non condividono lo stesso collo di bottiglia; su dischi meccanici una alla volta.
- **Lotti per progetto**, pausa e ripresa dopo un'interruzione o un disco scollegato.
- **Destinazione NAS:** se ha gli snapshot (Btrfs, ZFS), Space consiglia di attivarli prima. Vanno provati la rinomina che non sovrascrive su SMB, l'elenco veloce dei file e i nomi con gli accenti, prima su un NAS di test.
- **Destinazione disco o DAS:** Space controlla in anticipo formato, spazio libero e compatibilità dei nomi.

---

## 8. Cataloghi di Lightroom e degli altri

Spostare cartelle fuori da Lightroom le rende "mancanti". La ricerca suggerisce un ibrido **(proposta)**:
1. **Sempre:** avviso in sola lettura sulle cartelle catalogate, più la **regola di non rinominare mai i file catalogati**. Se si spostano interi alberi, in Lightroom basta un ricollegamento della cartella più alta.
2. **Sempre:** una guida al ricollegamento, cioè l'elenco vecchio→nuovo percorso, nell'ordine in cui farlo in Lightroom.
3. **Solo come opzione avanzata:** aggiornare direttamente il catalogo di Lightroom, a Lightroom chiuso. Si tocca solo il percorso delle cartelle radice, dopo un backup del catalogo e con un controllo di integrità prima e dopo. Lo schema non è documentato da Adobe e cambia tra le versioni: è il punto più delicato, va deciso con Andrea.
4. **Capture One:** niente scrittura finché non ci sono prove sicure. **Photo Mechanic Plus:** non si scrive nel suo database; si può solo leggere, da verificare.

Oggi RawlineKit il catalogo di Lightroom lo **legge** soltanto.

---

## 8bis. Cosa insegnano i problemi delle persone (ricerca dell'11 nov)

Nove agenti, tre passaggi ciascuno, circa 400 fonti. Le note complete sono in `research_notes/RawLine Space/Criticità/`. I tre dati più sorprendenti li ho verificati di persona in un secondo passaggio.

### 8bis.1 Le criticità più gravi e diffuse
1. **Spostare tra dischi significa copiare e poi cancellare, e se si interrompe si perde.** Succede anche spostando da dentro Lightroom: in un caso sono arrivate 76 foto su 97, in un altro due sottocartelle su tre sono sparite da entrambi gli SSD (novembre 2025). È un problema noto da anni.
2. **Le sincronizzazioni scambiano un disco scollegato o rinominato per "tutto cancellato".** Dropbox ha rimosso oltre 160.000 file in un caso. Resilio dichiara che un rinomina vale "cancella + crea". Un rinomina di sole maiuscole ha cancellato file da entrambi i lati.
3. **Le app per i doppioni cancellano tutte le copie.** **Verificato:** in Lightroom Classic 15.4 (giugno 2026), "Elimina foto rifiutate" nella nuova vista Duplicati toglieva dal disco anche le copie non rifiutate. Adobe ha ritirato la versione e ha corretto il problema con la 15.4.1 due giorni dopo ([Lightroom Queen](https://www.lightroomqueen.com/whats-new-in-lightroom-2026-06/), [segnalazione Adobe](https://community.adobe.com/bug-reports-674/p-delete-rejected-photos-in-duplicates-view-deletes-all-copies-1628661)).
4. **I falsi doppioni.** Nome più dimensione, ora al secondo nelle raffiche, "simile" scambiato per "uguale", RAW e JPEG dello stesso scatto presi per doppioni.
5. **File rinominati = collegamenti persi.** Le cartelle spostate si ricollegano in blocco quasi ovunque. I **file rinominati** invece in Lightroom e InDesign si ricollegano a mano uno per uno: c'è il caso di 65.000 file da ricollegare. Reimportare o fare "rimuovi mancanti" fa perdere gli sviluppi.
6. **Video: si cancella l'unica copia del girato** credendo che "stia nella libreria". In Final Cut i media esterni sono solo collegamenti, e i backup automatici di Final Cut e Resolve contengono il database, non i media. Copiare solo gli MP4 Sony senza XML, o gli MXF Canon senza `CONTENTS`, rende il girato orfano.
7. **Copie "riuscite" ma rovinate.** Lensrentals riporta che 9 corruzioni su 10 nascono nel trasferimento. Il Finder si ferma a metà sulle copie grandi verso i NAS, e quasi nessuno verifica con un hash.
8. **XMP e catalogo non coincidono.** Un catalogo da 109.000 foto mostra 21.030 conflitti falsi per `arw` contro `ARW`. *Non confermato:* un solo utente (luglio 2026) dice che Bridge cancella l'XMP del RAW quando si elimina il JPEG con lo stesso nome, e un altro non riesce a ripeterlo ([thread](https://community.adobe.com/bug-reports-557/bridge-deletes-the-sidecar-xmp-file-associated-with-a-raw-file-when-a-another-file-with-similar-name-but-different-type-is-deleted-1632752)).
9. **Lentezza a grande scala**, la lamentela numero uno sulle app concorrenti (8 app). digiKam con 468.000 elementi ci mette più di 5 minuti ad aprirsi; Capture One con 900.000 foto 10 minuti.
10. **Paura dell'abbandono e prezzi.** Photo Mechanic Plus chiuso, Kyno fermo per anni, Daminion Standalone chiuso, abbonamenti e licenze a scaglioni per numero di dischi.

### 8bis.2 Perché "Libera spazio" conta più di prima
**Verificato:** i dischi rigidi sono rincarati di circa il 46% in quattro mesi, tra settembre 2025 e gennaio 2026, con aumenti dal 23% al 66% a seconda del modello. Western Digital e Seagate hanno la produzione 2026 venduta ai data center AI ([WinBuzzer](https://winbuzzer.com/2026/02/18/wd-seagate-2026-hard-drive-shortage-ai-data-centers-xcxwbn/), [PCWorld](https://www.pcworld.com/article/3063473/western-digital-is-out-of-hard-drives-because-ai-data-centers.html)). C'è chi ha ridotto l'archivio da 12 a 3 TB (Fstoppers, luglio 2026). Liberare spazio oggi vuol dire **soldi veri**. **(proposta)** Space mostra anche quanto vale in euro lo spazio liberato.

### 8bis.3 Cosa chiedono e nessuno dà
- Sapere **dove sta cosa** su 10–26 dischi, per cliente e lavoro, non solo per nome file.
- **Liberare spazio con criterio**: quali RAW sono stati usati, senza rischi. Oggi si usano strumenti generici o script.
- **Scegliere la copia buona** tra versioni divergenti dello stesso lavoro: nessuna fonte spiega come farlo.
- Per gli amatori: **scartare in fretta le raffiche**, specie e luogo proposti in automatico (offline), un linguaggio semplice.
- **Prezzo una tantum**, licenza che funziona senza rete, formati aperti per poter uscire dall'app, download diretto oltre allo store.

### 8bis.4 Nuovi requisiti per Space
Ai requisiti già scritti nelle sezioni 3–7 si aggiungono:
1. **Un volume assente non è mai un volume vuoto.** Un disco scollegato non genera eliminazioni, conflitti o "file mancanti" da sistemare.
2. **Le copie verificate non sono un obbligo (Andrea, 11 nov).** Per gli scatti non usati dei lavori vecchi (5, 6, 7 anni fa), dove non c'è nessun obbligo verso il cliente, si possono togliere senza tenerne copie altrove: è il caso più semplice. Il controllo "restano almeno N copie verificate" diventa un'**opzione**, scelta per progetto o per età del lavoro. Serve soprattutto quando si toglie qualcosa che va conservato, per esempio quando si svuota un disco vecchio dopo Consolida. La quarantena con scadenza resta sempre.
3. **Un doppione si può togliere solo se è identico byte per byte.** I "simili" e lo "stesso scatto in altra forma" si mostrano, non si tolgono mai in automatico. Ogni scelta ha la sua riga di spiegazione.
4. **Prima di togliere un doppione si verifica che resti almeno una copia vera e leggibile** (la lezione di Lightroom 15.4).
5. **"In uso" vince su tutto.** I file a cui punta un catalogo (Lightroom, Capture One, Apple Foto, Photo Mechanic Plus) o un progetto video (Final Cut, Resolve, Premiere) sono segnati e non vengono mai proposti per la pulizia senza un avviso esplicito.
6. **Spostare cartelle sì, rinominare file catalogati no** (di default). Se serve, si fa con la mappa vecchio→nuovo e le istruzioni di ricollegamento per ogni app.
7. **Rinomina di sole maiuscole in due passaggi** (nome temporaneo, poi nome finale), come fa già `SafeRenamer`.
8. **Avvisare per backup e sincronizzazioni.** Se la cartella è dentro Dropbox, Synology Drive, Resilio, iCloud o sotto Time Machine o Backblaze, Space lo dice e stima quanti GB ripartiranno dopo il riordino.
9. **Le schede video sono blocchi unici.** Ogni clip resta legata ai suoi file d'accompagnamento. I database e i backup dei progetti non vengono mai proposti per la pulizia. Un proxy si toglie solo se l'originale è verificato su un altro volume.
10. **Controllo dei nomi prima di migrare** su un NAS: caratteri vietati, Unicode, percorsi oltre i 255 caratteri. In più, non creare file `._` e `.DS_Store`.
11. **Scala:** test con 1 milione di file e 100 TB; catalogazione in due passaggi, interrompibile e ripresa; AI locale con limite di memoria e CPU.
12. **Formati aperti:** catalogo SQLite esportabile, registro leggibile anche fuori dall'app, licenza offline, nessun limite sul numero di dischi.
13. **Per gli amatori (proposta):** alleggerimento in tre livelli con nomi chiari (Prudente, Equilibrato, Deciso) e un linguaggio senza gergo ("raffica", "foto quasi uguali", "spazio liberato").

### 8bis.5 Le conferme (deciso da Andrea l'11 nov: dosate sul rischio)
La ricerca UX (Apple, Nielsen Norman Group, WCAG, studi sull'attenzione) mette in guardia dal flusso deciso nella sezione 3:
- **Troppe barriere uguali diventano un gesto automatico.** L'attenzione a un avviso cala già alla seconda ripetizione (Anderson 2015 e 2020): sei passaggi ogni volta rischiano di proteggere meno.
- **Tenere premuto 5 secondi non è accessibile.** VoiceOver, Switch Control e Controllo vocale fanno solo clic istantanei, e il WCAG chiede che da tastiera nulla dipenda da tempi stabiliti. Serve sempre un'alternativa, per esempio ⌘Invio con un foglio di conferma.

**Deciso: conferme dosate sul rischio**, tenendo sempre anteprima, registro e annulla. Questa scelta sostituisce il "tieni premuto 5 secondi su tutto" della sezione 3.
- **Spostare e rinominare** (si annulla sempre): un pulsante con verbo e numeri ("Sposta 2.340 file") e l'annulla in vista.
- **Mettere in quarantena:** pressione prolungata, più breve (1,5–2 s, regolabile) e con l'alternativa da tastiera.
- **Eliminare per sempre** (svuotare la quarantena): scrivere il nome.
- Conferma dell'intenzione e controllo finale si possono unire in un unico riepilogo.

Fonti principali delle note: Adobe Community, Lightroom Queen, Apple Discussions, Creative COW, DVinfo, Larry Jordan, Fstoppers, PetaPixel, Synology Community, Eclectic Light, Lensrentals, Nielsen Norman Group, Apple HIG, WCAG 2.2, e altre (link completi in ogni nota).

---

## 9. Cose da non fare (raccolte dalle altre app)

- Azioni automatiche in sottofondo (Hazel).
- Eliminazione definitiva come impostazione predefinita (DaisyDisk, Gemini sui dischi senza Cestino).
- Annulla che vale solo finché l'app è aperta (Gemini).
- Verifica "solo dimensione" prima di cancellare (Hedge e Pomfort lo vietano).
- Un'anteprima che non è il piano vero (BMFM).
- Una "salute del disco" che non dice cosa misura (Offline Files).
- Licenze o funzioni che chiedono la rete (Tusk, Peakto, Diem).
- Metadati chiusi in un formato proprietario o in cartelle nascoste che si perdono spostando i file (Kyno, Diem).
- Un catalogo che dipende da tecnologia di terzi e non si può esportare (Photo Mechanic Plus).
- Limiti rigidi sul numero di file (Tusk, Excire).
- Opzioni nascoste nel Terminale (NeoFinder).

---

## 10. Domande aperte per Andrea

**Risposte dell'11 novembre:**
- **Cataloghi + XMP.** Le foto stanno in cataloghi di Lightroom, ma ogni cartella ha anche i suoi XMP. Il flusso di Andrea:
  - selezione con rating in RawLine Selects (prima in Photo Mechanic);
  - i lavori rapidi si aprono in Photoshop/Camera Raw solo sulle foto selezionate, e quelle elaborazioni stanno negli XMP;
  - i lavori lunghi e gli eventi con tanti file passano da Lightroom.

  Quindi Space deve leggere **sia gli XMP sia i cataloghi**, e trattarli come due fonti che possono non coincidere.
- **Il disco è il G-SPEED Shuttle XL**, HFS+: niente clone a spazio zero.
- **Regola sul G-SPEED, da non toccare.** È il disco di lavoro, con i materiali di tutti i clienti e progetti in corso. Si può **solo leggere e copiare altrove** per le prove. Mai spostare, rinominare o cancellare niente, mai scriverci file, nemmeno nascosti o temporanei. Tutte le prove di Space si fanno su copie, su un altro disco.

**Ancora aperte:**
1. ~~In Lightroom è attivo "Scrivi automaticamente le modifiche nell'XMP"?~~ **Sì**, letto da una copia del catalogo l'11 nov sera. Il catalogo però punta quasi tutto a dischi vecchi non più collegati: vedi [[RawLine Space - Analisi]], sezione 10.2.
2. Su quale disco si possono fare le copie di prova, e quanto spazio c'è?
3. ~~Video?~~ Sì, anche i video (sezione 0quater).
4. Esporti da Lightroom con "Tutti i metadati" o con "Solo copyright"? Decide quanto è facile abbinare export e RAW.
5. ~~Per i cataloghi: basta avviso + guida al ricollegamento, o vuoi anche l'aggiornamento diretto?~~ **Andrea vuole l'aggiornamento automatico** (11 nov sera), fatto su una copia del catalogo, controllata prima di usarla. Fattibilità e passi in [[RawLine Space - Analisi]], sezione 10.3.
6. ~~Hai un secondo disco con il backup dell'archivio?~~ **No: l'archivio esiste solo sul G-SPEED** (Andrea, 11 nov sera). È il rischio più grande: la seconda copia va fatta prima di tutto il resto, con uno strumento che esiste già.
7. Distribuzione: beta gratuita fuori App Store come le altre?

## 11. Fonti

Le fonti app per app sono in fondo a ogni nota di `research_notes/RawLine Space/`. Le principali:
- [Diem](https://downloaddiem.com)
- [Hazel, manuale](https://www.noodlesoft.com/manual/hazel/hazel-overview)
- [NeoFinder](https://en.wikipedia.org/wiki/NeoFinder)
- [Offline Files](https://www.cined.com/offline-files-for-macos-search-any-drive-even-when-its-unplugged/)
- [DriveShelf](https://www.cined.com/es/driveshelf-for-mac-released-search-unplugged-drives-cross-drive-duplicate-finder-free-iphone-companion/)
- [Tusk](https://nofilmschool.com/tusk-mac-backup-app)
- [Hedge OffShoot 24.3](https://hedge.co/blog/offshoot-24-3)
- [ASC MHL](https://cdn.theasc.com/ASCMHL_One-Sheet_v1-1_210121_102845.pdf)
- [Photo Mechanic Plus non più in vendita](https://home.camerabits.com/photo-mechanic-plus-is-no-longer-available-for-purchase/)
- [Lightroom, foto mancanti](https://www.lightroomqueen.com/lightroom-photos-missing-fix/)
- [Peakto](https://fstoppers.com/reviews/peakto-review-hub-all-your-images-and-catalogs-628058)
- [Excire Foto](https://www.photoworkout.com/excire-foto-review)
- [Kyno](https://www.archiware.com/solutions/kyno)
- [GrandPerspective e DaisyDisk](https://appmus.com/vs/grandperspective-vs-daisydisk)
- [Big Mean Folder Machine](https://alternativeto.net/software/big-mean-folder-machine/about/)
