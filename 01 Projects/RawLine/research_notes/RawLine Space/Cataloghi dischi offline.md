# Cataloghi di dischi offline: la nuova ondata 2025–2026

Ricerca di prodotto per RawLine Space. Data: 11 novembre 2026.

Legenda: **[V]** verificato su una fonte (sito ufficiale, App Store o articolo citato); **[D]** dedotto da me, non scritto da nessuna fonte; **[?]** fonti in disaccordo o dato mancante.

Nota sul metodo: quasi tutte le recensioni (CineD, Newsshooter, Creative COW, appleworld.today) sono articoli promozionali basati su comunicati e citazioni degli sviluppatori, senza prove indipendenti. Le critiche vere vengono quasi solo dai commenti degli utenti (App Store, Reddit r/DataHoarder, Product Hunt), e sono poche. PetaPixel ha risposto 403: ne ho letto solo titoli ed estratti.

---

## 1. Offline Files (Paul Kothe, Berlino)

**Cos'è.** App Mac di un montatore e direttore della fotografia di Berlino. Cataloga i dischi esterni e li rende cercabili da scollegati. È la più ricca della nuova ondata e quella aggiornata più spesso (circa una versione ogni 1–3 settimane nel 2026). Uscita a gennaio 2026 [V].

**Funzioni.**
- Scansione di ogni volume collegato; nel catalogo salva nome, percorso completo, dimensione, date di creazione e modifica, estensione e spazio libero del disco. Mai il contenuto dei file [V].
- **Miniature offline** messe in cache (dalla 1.26, aprile 2026): foto e video si vedono anche con il disco scollegato [V].
- **Metadati media**: riconosce .braw, .r3d, .mxf, ProRes e i RAW foto (.arw, .cr3, .dng); dalla 1.32 legge anche IPTC/XMP [V]. Quali campi XMP indicizzi (stelle, etichette, parole chiave?) non è scritto [?].
- **Checksum**: non citati da nessuna fonte [?]. [D] Probabilmente non ci sono, dato che parla di "metadata only".
- **Ricollegamento**: riconosce da solo un disco già noto e aggiorna l'indice in background [V]. Il criterio usato (UUID del volume o altro) non è dichiarato [?].
- **Ricerca**: un'unica ricerca su tutti i volumi, online e offline; il risultato indica volume e percorso. Ci sono filtri avanzati per tipo di media, ricerca solo per nome (1.27), completamento automatico mentre si scrive e ricerca dalla barra dei menu (1.31). Si integra con **Spotlight**: i file dei dischi scollegati compaiono nella ricerca di macOS [V].
- **Smart Analyze** (opzionale, solo Apple Silicon): riconoscimento sul Mac di persone, animali, oggetti e scene in foto e video, cercabili in 14 lingue (per esempio "cane") [V].
- **Cleanup**: doppioni tra tutti i volumi e "related versions" (versioni collegate dello stesso file). Dalla 1.32 si può mandare nel Cestino con annullamento ⌘Z [V]. Il criterio dei doppioni non è dichiarato [?].
- **Gruppi di dischi**, note per volume, preferiti e segnalibri [V].
- **Drive Health Beacon** (1.27) [V]: il nome fa pensare a un indicatore di salute del disco, ma non ho trovato cosa misuri [?].
- **Storage Analytics** (1.26): confronto dell'uso tra volumi e per tipo di file [V].
- **Shared Catalogs** (beta, 1.26.1): cataloghi condivisi fra più Mac, salvati per disco [V]. Il modo in cui si condividono non è documentato [?]. [D] Forse tramite un file o una cartella in comune.
- Cartelle cloud (Dropbox, iCloud Drive, Google Drive, OneDrive) aggiungibili come volumi solo su richiesta (1.29) [V].
- **Esportazione CSV** con opzioni, vista ad albero, pannello Get Info e Azioni (1.32), anteprima rapida dei video con LUT ed esportazione di fotogrammi, widget [V].
- App iPhone: nessuna [V, per assenza nell'App Store].

**Interfaccia.** Finestra principale con barra laterale comprimibile, panoramica dei volumi ridisegnata nella 1.29, barra di selezione comune, voce nella barra dei menu e un tour guidato del prodotto (1.30) [V]. L'app è in 14 lingue, italiano compreso [V].

**Prezzo.** Acquisto unico, nessun abbonamento. Il prezzo è salito nel tempo: $7.99 a febbraio (Newsshooter), $8.99/€8.99 (CineD), €9.99 sul sito, $9.99 ad agosto (appleworld) e **$12.99 oggi sull'App Store** [V]. Richiede macOS 15 (il sito dice 15.2) e gira su Apple Silicon e Intel; supporta In famiglia [V].

**Limiti.** Per aprire un file o vederne l'anteprima completa serve il disco collegato. Non è un DAM: niente proxy, niente integrazione con i bin dei programmi di montaggio, non sostituisce un MAM aziendale. Il dettaglio dei metadati cambia col formato [V]. Smart Analyze funziona solo su Apple Silicon [V].

**Critiche.** Non ne ho trovate di concrete. appleworld gli dà 4/5 e la dice "veloce e fluida"; sull'App Store le valutazioni sono troppo poche per una media [V]. [D] Il rischio è che, aggiungendo funzioni così in fretta, l'app finisca per somigliare a un DAM senza esserlo.

---

## 2. DriveShelf (Sergiy Pudich / EasyFilm, Bangkok)

**Cos'è.** App Mac di un regista che lavora nel cinema dal 2012. Nata per gestire il suo archivio, è la sua prima app ed è entrata nella linea di strumenti EasyFilm. Uscita a fine settembre 2026 [V].

**Funzioni.**
- Salva nome, percorso, dimensione, date e **tag del Finder**. Le librerie di Final Cut Pro, iMovie, Foto e Logic sono mostrate come un unico elemento [V]. Chiede l'accesso in sola lettura e solo ai dischi scelti; non copia, sposta o modifica nulla, tag compresi [V].
- Miniature e checksum: nessuno dei due è citato [V, per assenza].
- **Identità del disco**: rinominare un disco nel Finder non rompe il collegamento al catalogo, mentre riformattarlo crea un disco nuovo [V]. [D] Il comportamento corrisponde all'UUID del volume.
- **Riscansione**: quando si collega un disco nuovo compare il popup "New Drive Detected" [V]. Le condivisioni di rete vengono riscansionate da sole se il catalogo ha più di 12 ore e la condivisione è collegata; la cartella Inizio resta aggiornata mentre l'app è aperta [V]. Una riscansione automatica dei dischi esterni quando si ricollegano non è documentata [?].
- **Ricerca**: per nome o per parte del percorso su tutti i dischi, con filtri per tipo, dimensione, disco e tag del Finder [V]. Si sfoglia in stile Finder, cartella per cartella, anche a disco scollegato [V].
- **Doppioni**: file con **stesso nome e stessa dimensione** su più dischi; le cartelle sono confrontate file per file. C'è una dimensione minima per saltare i file piccoli (sidecar, cache). Non cancella mai niente: mostra dove si trova ogni copia, apre le cartelle affiancate per confrontarle ed esporta in CSV [V]. [D] Con questo criterio due file diversi con stesso nome e stessa dimensione risultano doppioni, mentre una copia rinominata sfugge.
- **Gruppi** di dischi per cliente, progetto o anno [V].
- **Spazio libero e velocità di lettura** nella barra laterale, con un test di velocità integrato. Un **report PDF** elenca le cartelle più grandi di ogni disco [V]. Salute del disco: non citata [V, per assenza].
- **App iPhone gratuita** inclusa nell'acquisto: mostra lo stesso catalogo in sola lettura, sincronizzato tramite l'iCloud dell'utente e non i server dello sviluppatore. "Sync Now" manuale o sincronizzazione automatica. Serve iOS 26.5 [V].
- **Esporta e importa il catalogo** (File → Export/Import Catalog), comodo per passare a un nuovo Mac [V].

**Interfaccia.** In stile Finder: barra laterale con dischi, spazio libero e gruppi; viste per ricerca e doppioni; una schermata per scegliere i dischi [V].

**Prezzo.** Gratis fino a 3 dischi (una condivisione NAS conta come uno). Dischi illimitati con **$14.99 / €17.99** una tantum, valido su tutti i Mac e iPhone dello stesso ID Apple [V]. Richiede macOS 14 e gira su Apple Silicon e Intel [V].

**Limiti.** Non è un backup. Le condivisioni di rete sono solo SMB e il NAS non è ancora supportato ufficialmente; i dischi interni aggiuntivi non sono supportati; non condivide librerie fra ID Apple diversi; nell'iPhone non si cataloga [V].

**Critiche.** Nessuna recensione indipendente; gli articoli si basano sulle dichiarazioni dello sviluppatore [V].

---

## 3. DriveVault – Offline Catalog (Full Access Media Limited)

**Cos'è.** App Mac lanciata sul Mac App Store dopo una beta che, secondo lo sviluppatore, ha avuto più di 300 tester [V].

**Funzioni.**
- Si scansiona ogni disco una volta sola. Il catalogo contiene nomi, struttura delle cartelle, metadati, **EXIF** e **anteprime visive** opzionali per immagini e video, consultabili offline [V].
- Viste a colonne e a icone con anteprime [V].
- **Confronto tra dischi con report dei "backup gap"**, cioè cosa manca su un disco rispetto a un altro [V]. Il criterio di confronto non è dichiarato [?].
- Statistiche dello spazio della libreria [V].
- **Modelli di struttura cartelle per i progetti** [V].
- **Esportazione del catalogo per i team**; il catalogo si può condividere con altri utenti DriveVault [V].
- Context Scan (beta): ricerca nel testo dei PDF. Scansione più veloce dei file video RAW [V].
- Versione 1.2.11: Diagnostic Center e riscansione rivista [V]. Come si aggiorna un disco ricollegato non è documentato [?].
- Ricerca dalla barra dei menu [V, da un post dello sviluppatore].
- Checksum, doppioni, salute dei dischi e app iPhone: non citati [V, per assenza].

**Prezzo.** Gratis per 1 disco fino a 4 TB. I livelli a pagamento sono acquisti unici per 5, 10, 20 dischi o illimitati, da $9.99 a $99.99 (un articolo dice da $14.99) [V/?]. Richiede macOS 14 [V].

**Limiti e critiche.** La scansione completa di dischi molto grandi richiede tempo e il supporto per NAS e RAID è ancora in sviluppo, come ammette lo sviluppatore [V]. Su Reddit: "$100 per il livello più alto è caro"; non legge CD e Blu-ray; la distribuzione solo dall'App Store è un ostacolo per chi tiene un Mac vecchio scollegato da internet [V]. Le poche recensioni sull'App Store sono positive e citano il confronto tra dischi [V].

---

## 4. DriveBuddy (CODEC, LLC, Atlanta)

**Cos'è.** App Mac per indicizzare i dischi e cercarli da scollegati. Uscita a gennaio 2026 (Newsshooter) [V].

**Funzioni.**
- Indicizza solo nomi, percorsi e dimensioni, sul Mac [V].
- Ricerca per nome e percorso su tutta la libreria, con filtro per tipo. Il risultato porta al disco e alla cartella giusti: si collega quel disco e si mostra il file nel Finder [V].
- Mostra spazio totale, usato e libero per disco, con ordinamento per spazio libero; ripartizione visiva per tipo di file; albero completo delle cartelle [V].
- Raggruppa per **progetto**, con tag per **cliente** e un registro sfogliabile dei dischi [V].
- **Esporta e importa** la libreria fra Mac; **CSV** con capienza, uso e contenuto di primo livello di ogni disco [V].
- Si può lavorare mentre scansiona: gli SSD sono veloci, i dischi meccanici grandi più lenti [V].
- Doppioni, miniature, salute dei dischi e iPhone: non citati [V, per assenza].

**Prezzo.** $19.99 una tantum per 2 Mac, rimborso entro 14 giorni, venduto dal sito (non dall'App Store, a quanto risulta) [V/D]. Richiede macOS 13.5; una versione per Windows è in sviluppo [V].

**Limiti.** Niente NAS: solo dischi collegati direttamente; per aprire i file serve il disco collegato [V]. È la più semplice del gruppo [D].

---

## 5. Strada (accesso remoto ai dischi, non un catalogo)

**Cos'è.** Una piattaforma per lavorare da remoto sui propri dischi senza passare dal cloud. Sul computer che ospita i media gira un agente desktop (Strada Agents, peer-to-peer, presentato al NAB 2025). Strada 2.0 è uscita ad agosto 2026 [V].

**Funzioni.**
- **Strada Connect**: una cartella o un disco condiviso compare nel Finder come un volume collegato in locale; si apre direttamente in Premiere, Resolve, Photoshop o Pro Tools. Viaggiano solo i dati che servono alla riproduzione, con una cache locale [V].
- Supporta dischi interni ed esterni, RAID, NAS e schede delle fotocamere [V].
- App iOS e Android per sfogliare, riprodurre ed esportare; permessi su chi vede o copia cosa; inviti e link di caricamento [V].

**Prezzo.** Gratis per sfogliare e vedere; Basic $8 per utente al mese (montaggio remoto, trasferimenti, cache); Pro $24 per utente al mese; Enterprise a parte [V]. Gira su macOS 13, Windows 11, iOS 17 e Android 12 [V].

**Limiti e critiche.** Il computer di origine deve restare acceso, online e con l'utente collegato; la banda in upload di chi ospita limita tutti. Mancano autenticazione a due fattori, SSO e passkey; le certificazioni di sicurezza sono in corso. CineD considera non verificate le prestazioni dichiarate e nota che la workstation diventa "infrastruttura" [V].

**Per RawLine Space:** è l'opposto del nostro modello, perché richiede la rete e un account. Interessa solo come riferimento per cosa vuole l'utente: trovare e vedere un file che non ha fisicamente davanti [D].

---

## 6. Altre app simili

### Offline Disks File Searcher (sviluppatore cinese, 是 刘)
- $8.99, ultimo aggiornamento aprile 2023 (1.8.5); richiede macOS 10.14.6 [V].
- Salva solo nomi e tipi di file. Scansiona più dischi in parallelo e si può cercare mentre scansiona (circa 1–2 minuti per 1 TB su USB, secondo lo sviluppatore). Esclude cartelle nascoste o scelte dall'utente (per esempio node_modules), mostra la data dell'ultimo aggiornamento di ogni posizione e capienza e spazio libero [V].
- Richieste degli utenti: date dei file, indici condivisibili, etichette o descrizioni dei dischi, indicatore di avanzamento della ricerca [V]. È utile come elenco di cosa manca a un catalogo minimo.

### DiskCatalogMaker (Fujiwara Software, storico)
- 9.3.1 del settembre 2026; macOS 12–27; $38.99 utente, $79.99 famiglia, prova di 30 giorni; versione LE sull'App Store senza miniature [V].
- Miniature opzionali, doppioni tra i dischi selezionati, ricerca booleana AND/OR, Spotlight, cataloga anche il contenuto degli archivi (zip, rar, 7z...), catalogo compresso pensato per "dati enormi", condivisione su server AFP [V].

### NeoFinder (Wfs-apps, storico, riferimento pro)
- Miniature di foto e video, metadati XMP/IPTC/EXIF cercabili, scrittura nei file di alcune informazioni XMP, app iPhone/iPad che porta con sé i cataloghi, rete multipiattaforma con abeMeda per Windows [V].
- Critica su Reddit: l'aggiornamento automatico delle condivisioni di rete richiede una licenza business che costa tre volte tanto [V].

### Tusk (Niklas Fischer, 2026)
- Non è un catalogo puro ma un'app di **backup** per fotografi e videomaker (PetaPixel, agosto 2026). Traccia ogni file con **checksum BLAKE3** su tutte le destinazioni; collegando un disco vecchio si vede cosa contiene. **Prima di liberare spazio sul Mac verifica tutte le copie e si rifiuta se ne manca una.** Ripristina dalla copia migliore e mette in coda le operazioni quando i dischi sono scollegati [V].
- $49 a vita al lancio, poi $79, prova di 14 giorni. Il cloud è opzionale e usa gli account dell'utente (Dropbox, Google Drive, S3) [V].
- Limiti: mancano le sincronizzazioni programmate; l'osservazione continua delle cartelle non regge i progetti grandi (lo ammette lo sviluppatore) [V].

### Chrova (Makoto Tsuyuki) e Peakto (CYME)
- Gestori di foto locali con **miniature in cache visibili a originali scollegati**. Chrova ha anche importazione con **doppioni riconosciuti per hash**, ricerca per data, stelle, bandierina, fotocamera, obiettivo, tag e luogo, mappe e GPX [V]. Sono un'altra categoria (DAM leggeri), utili come riferimento [D].

---

## Tabella di confronto

| | Offline Files | DriveShelf | DriveVault | DriveBuddy | Offline Disks FS | DiskCatalogMaker | NeoFinder | Tusk |
|---|---|---|---|---|---|---|---|---|
| Miniature offline | Sì | No | Sì (opz.) | No | No | Sì (opz., non in LE) | Sì | ? |
| EXIF/XMP | Sì (XMP/IPTC da 1.32) | No (tag Finder) | EXIF | No | No | ? | Sì, anche scrittura | No |
| Checksum | ? | No | ? | No | No | ? | ? | **BLAKE3** |
| Criterio doppioni | ? (+ "versioni collegate") | Nome + dimensione, soglia minima | — (confronto dischi) | — | — | Sì, criterio ? | ? | Checksum |
| Riconosce il disco ricollegato | Auto + sync in background | UUID [D]; rinomina ok, riformatta = nuovo | Riscansione (rivista nella 1.2.11) | ? | Data ultimo aggiornamento | ? | ? | Sì |
| Gruppi di dischi | Sì + note | Cliente/progetto/anno | ? | Progetto + tag cliente | Ordine nella barra laterale | ? | Sì | — |
| Spazio libero / salute | Analytics + "Health Beacon" | Spazio + velocità lettura + PDF | Statistiche | Spazio, tipo di file | Spazio | ? | ? | — |
| Confronto dischi / backup gap | No | Cartelle affiancate | **Sì** | No | No | No | ? | **Sì (copie verificate)** |
| AI locale | Smart Analyze | No | No | No | No | No | No | No |
| App iPhone | No | Gratis, sola lettura, iCloud | No | No | No | No | Sì | No |
| Esportazione | CSV, cataloghi condivisi (beta) | Catalogo + CSV doppioni + PDF | Catalogo per i team | Libreria + CSV | No | Catalogo su AFP | Cataloghi in rete | — |
| NAS | ? | Solo SMB, non ufficiale | In sviluppo | No | Sì (volumi remoti) | Cartelle di rete | Sì (licenza costosa) | — |
| Prezzo | $12.99 una tantum | Gratis 3 dischi / $14.99 | Gratis 1 disco 4 TB / $9.99–99.99 | $19.99 | $8.99 | $38.99 | a pagamento | $49–79 |
| macOS minimo | 15 | 14 | 14 | 13.5 | 10.14.6 | 12 | — | — |

---

## Idee da prendere per RawLine Space

1. **Il risultato dice quale disco collegare, e il disco ha un nome fisico.** Tutte le app lo fanno; DriveBuddy ci aggiunge "collega e mostra nel Finder". Per noi: un'etichetta stampabile o un colore per ogni disco, così "collega CLIENTI-2023-B" si trova sullo scaffale.
2. **Identità del disco legata all'UUID, non al nome** (DriveShelf: rinomina ok, riformatta = disco nuovo). Va mostrato esplicitamente all'utente.
3. **Miniature offline commisurate allo schermo** (Offline Files, DriveVault, NeoFinder, Chrova). Per i RAW conviene estrarre l'anteprima JPEG incorporata invece di decodificare il file: è coerente con la regola di Selects sulla decodifica leggera.
4. **Indicizzare i sidecar XMP** (stelle, etichette, scelte e scarti) e collegarli ai RAW: è il nostro vantaggio, dato che Selects scrive già gli XMP. Nessuna delle app nuove lo fa bene; NeoFinder sì, ma è vecchio e complicato.
5. **Doppioni in due livelli**: un controllo rapido su nome, dimensione e data (come DriveShelf, con soglia minima per saltare cache e sidecar), poi una **conferma con checksum** solo sui candidati prima di proporre una cancellazione. Il modello è Tusk: niente si libera finché non risultano N copie verificate.
6. **Report dei "backup gap"** (DriveVault): "questi 3.200 RAW del 2022 esistono su un solo disco". Per un archivio da 40–100 TB è forse la funzione più preziosa: il rischio vero non sono i doppioni ma le copie singole.
7. **Raggruppare per cliente, progetto o anno** (DriveShelf, DriveBuddy) e permettere **note per disco** (Offline Files).
8. **Spazio libero, tempo dall'ultima scansione e velocità di lettura** nella barra laterale (DriveShelf, Offline Disks FS). Per i dischi meccanici vecchi va aggiunto un avviso ("non scansionato da 14 mesi, disco del 2018").
9. **Librerie come elemento unico** (DriveShelf con Final Cut e Foto): lo stesso varrebbe per i cataloghi di Lightroom e le librerie di Capture One.
10. **Esportazione e importazione del catalogo** per cambiare Mac, **CSV** per il commercialista o il cliente, **report PDF** delle cartelle più grandi.
11. **Integrazione con Spotlight** (Offline Files): i file dei dischi scollegati si trovano anche da ⌘Spazio.
12. **Ricerca per contenuto con AI locale** (Smart Analyze di Offline Files), con Vision di Apple sul Mac: 100% offline, coerente con la regola di RawLine.
13. **Esclusione di cartelle** (cache, anteprime di Lightroom, .Trashes) e **ricerca mentre scansiona** (Offline Disks FS).
14. **App iPhone in sola lettura** tramite l'iCloud dell'utente (DriveShelf): utile, ma da valutare con la regola dell'offline. Il catalogo locale deve funzionare comunque; la sincronizzazione è un di più, mai necessaria. Prima va chiesto ad Andrea.

## Cose da NON copiare

- **Doppioni basati solo su nome e dimensione** usati per cancellare: troppi falsi positivi (DSC00001.ARW con la stessa dimensione su schede diverse) e i doppioni rinominati sfuggono. Va bene come primo filtro, non come verdetto.
- **Prezzo per numero di dischi o per capienza** (DriveVault, fino a $99.99): con 40–100 TB l'utente pro paga sempre il massimo e lo vive come una punizione. Su Reddit è la critica principale.
- **Funzionalità chiave legate alla licenza "business"** (NeoFinder e le condivisioni di rete).
- **Cancellare dal catalogo con un Cestino veloce** (Offline Files 1.32, ⌘Z) senza verificare che esista un'altra copia: su un archivio di clienti serve la regola di Tusk ("rifiuto se manca una copia").
- **Accumulare funzioni a ogni versione** (Offline Files: 8 versioni in 5 mesi, con LUT, widget e cloud) fino a diventare un DAM confuso: meglio poche funzioni solide.
- **Dipendere dalla rete o da un account** (Strada): incompatibile con RawLine.
- **Distribuire solo dall'App Store** (critica a DriveVault): chi tiene un Mac d'archivio offline vuole uno scaricamento diretto. RawLine è già fuori dallo store.
- **"Health" senza spiegare cosa misura** (il "Drive Health Beacon" di Offline Files): se mostriamo la salute, deve essere chiaro da dove viene il dato (SMART dove disponibile, età del disco, errori di lettura durante la scansione).
- **Scansioni complete lente e bloccanti sui dischi grandi** (critica a DriveVault): servono scansioni incrementali, interrompibili e che riprendono da dove si erano fermate.

---

## Fonti (link)

Offline Files
- https://apps.apple.com/app/offline-files/id6757367718
- https://paulkothe.de/offline-files
- https://www.cined.com/offline-files-for-macos-search-any-drive-even-when-its-unplugged/
- https://www.newsshooter.com/2026/02/24/offline-files-macos-app-that-indexes-external-drives/
- https://appleworld.today/2026/08/offline-files-is-a-great-mac-tool-for-searching-large-archives-across-multiple-disconnected-external-drives/
- https://petapixel.com/2026/02/27/this-mac-app-lets-you-find-photos-no-matter-which-drive-theyre-on (solo estratto, 403)

DriveShelf
- https://easyfilm.io/driveshelf/
- https://apps.apple.com/us/app/driveshelf/id6772950141
- https://www.cined.com/driveshelf-for-mac-released-search-unplugged-drives-cross-drive-duplicate-finder-free-iphone-companion/
- https://creativecow.net/driveshelf-a-filmmakers-mac-app-for-finding-footage-on-unplugged-drives/

DriveVault
- https://apps.apple.com/app/id6751731655
- https://www.producthunt.com/products/drivevault
- https://reddit.sentinel-team.org/posts/1rr4tfc/snapshots/2026-03-12T03%3A20%3A27.252886Z (copia del thread r/DataHoarder)

DriveBuddy
- https://drive-buddy.io
- https://www.newsshooter.com/2026/01/07/drivebuddy-search-across-all-your-drives-even-when-theyre-unplugged/

Strada
- https://www.cined.com/strada-2-0-now-available-mounts-remote-storage-as-a-virtual-drive-and-more/
- https://www.cined.com/strada-for-mobile-introduced-browse-play-and-export-on-ios-and-android/
- https://nofilmschool.com/strada-mobile-app

Altre
- https://apps.apple.com/us/app/offline-disks-file-searcher/id1200309146?mt=12
- https://diskcatalogmaker.com
- https://www.cdfinder.de/press-kit.html (NeoFinder)
- https://www.wfs-apps.de/PR/PR.NeoFinder.8.9.en.pdf
- https://www.producthunt.com/p/tusk-5/tusk-8149b5ad-8b7e-4c47-abef-179abfc223c7
- https://petapixel.com/2026/08/07/this-new-mac-app-keeps-track-of-your-photo-and-video-backups/ (Tusk, solo estratto, 403)
- https://apps.apple.com/app/id6759487336 (Chrova)
