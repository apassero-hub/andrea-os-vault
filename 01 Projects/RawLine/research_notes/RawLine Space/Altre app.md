# RawLine Space: le altre app

Ricerca dell'11 novembre 2026. Questa nota copre le app che non sono già analizzate a parte (Diem, Hazel, NeoFinder, Photo Mechanic, Peakto, Kyno e le altre).

Legenda:
- **[V]** verificato su una fonte (sito ufficiale, documentazione, note di rilascio).
- **[D]** dedotto da fonti di terzi o da conoscenza generale, non riscontrato in questa ricerca.
- **[?]** non trovato.

---

## 1. Cataloghi DAM desktop (catalogano anche dischi scollegati)

### IMatch (photools, solo Windows)
- **Cos'è:** il DAM desktop più "da archivista": database locale e metadati molto approfonditi.
- **Funzioni utili per noi:**
  - Dischi scollegati: riconosce i dischi rimovibili dal numero di serie. Quando un disco viene espulso lo segna tutto come *off-line* e lo rimette online da solo quando torna [V].
  - Comando *Relocate*: aggiorna il database quando cartelle o file sono stati spostati fuori dall'app. Un disco nuovo ha un seriale diverso, quindi i file risultano offline finché non si fa il relocate [V].
  - *File Relations*: RAW e JPEG della fotocamera sono "buddy", i derivati (DNG, TIFF, JPEG d'esportazione) sono "versioni". Le regole si configurano e i metadati passano dal master alle versioni [V].
- **Limiti:** solo Windows; curva d'apprendimento alta; il prezzo non è stato verificato in questa ricerca.
- **Per noi:** il modello buddy/versioni è esattamente quello che serve per "tenere solo export e RAW usati".

### IDimager Photo Supreme (Mac, Windows, Linux)
- **Cos'è:** DAM a catalogo, con funzioni identiche su Windows e macOS, nativo Apple Silicon e compatibile con macOS Tahoe [V].
- **Funzioni utili per noi:**
  - Catalogo SQLite (PostgreSQL o SQL Server nella Server Edition). Il catalogo tiene riferimenti a file che possono anche non essere presenti sul disco [V].
  - Si possono rivedere le anteprime "senza la libreria completa né internet" [V]. Che i volumi offline siano gestiti come in IMatch è [D].
  - All'importazione: nomi personalizzati, cartelle strutturate, regole di stack e versioni [V].
  - *Folder Verification and Syncing* rileva i cambiamenti, anche a orari programmati [V].
  - Trova i doppioni e li toglie [V].
  - Backup integrato (v2025) [V].
- **AI:** il riconoscimento volti è locale. L'analisi immagini e la ricerca in linguaggio naturale (v2026) possono girare su Ollama locale oppure su OpenAI e Gemini in cloud [V].
- **Prezzo:** licenza Single User o Server; prova di 30 giorni. I prezzi non erano leggibili sulla pagina [?].
- **Limiti:** interfaccia datata; le funzioni AI migliori dipendono da un modello locale da installare a parte.

### Mylio Photos (Mac, Windows, iOS, Android)
- **Cos'è:** libreria unica che unisce dischi, computer e telefoni, con sincronizzazione tra dispositivi senza passare dal cloud.
- **Funzioni utili per noi:**
  - Tiene la struttura di cartelle esistente, senza migrazione [V].
  - Gli album non spostano i file; tag e modifiche vengono scritti nei file [V].
  - Navigazione e ricerca funzionano offline; l'AI gira in locale [V].
  - I *Vault* conservano gli originali a piena risoluzione [V].
  - *SpaceSaver* tiene copie ottimizzate sui dispositivi piccoli [V].
  - Rimozione doppioni e Quick Review delle raffiche [V].
  - Dichiara di reggere più di 500.000 elementi [V].
- **Prezzo:** abbonamento. Le fonti sono discordanti: da circa 120 a 240 USD l'anno per l'individuale, e piani Business da 950 USD l'anno per 5 utenti (pagina Mylio non datata) [D].
- **Limiti:** pensato per famiglie e piccoli studi, non per 100 TB di RAW. Abbonamento.
- **Per noi:** il concetto "ogni disco sa cosa contiene, la libreria è una sola" e le copie leggere dove manca spazio.

### digiKam (open source, Mac, Windows, Linux)
- **Cos'è:** DAM gratuito KDE con database SQLite o MySQL. SQLite è consigliato sotto le 100.000 foto [V]; per archivi grandi serve MySQL o MariaDB [D].
- **Funzioni utili per noi:**
  - Le collezioni possono stare su cartelle locali, remote o rimovibili [V]. Che i dischi rimovibili scollegati restino nel database come "non disponibili" è [D].
  - Le miniature stanno in un database dedicato in formato PGF [V].
  - Gli spostamenti vanno fatti dentro digiKam per tenere il database allineato. Se un album sparisce fuori dall'app, al riavvio chiede se cancellarlo dal database [V].
  - All'importazione crea cartelle per data, con la data presa dall'immagine dalla 8.0 [V]. Rinomina con F2 [V].
- **Limiti:**
  - Ci sono bug aperti su date e rinomina all'importazione [V].
  - Il dialogo "Aggiungi cartelle" non rinomina [V].
  - È lento su archivi enormi [D].

### Daminion (Windows; server e cloud)
- **Cos'è:** DAM per team con un livello di metadati sopra i file lasciati dove sono [D].
- **Prezzo:** su preventivo, abbonamento per utenti e spazio; terzi indicano da 249 USD per utente all'anno [D].
- **Limiti:** orientato al server e al team. Non è chiaro se esista ancora un'edizione desktop standalone [?].
- **Per noi:** poco rilevante, se non come esempio di "catalogo sopra i file senza spostarli".

### ACDSee Photo Studio 2026 (Windows; versione Mac separata)
- **Cos'è:** visualizzatore e DAM con editor e AI "locale" dichiarata [V].
- **Limiti:** non ho trovato nulla su cataloghi di dischi offline [?]; esistono più edizioni (Home, Professional, Ultimate).
- **Per noi:** marginale.

### ImageRanger (Mac, Windows)
- **Cos'è:** gestore di foto e video con riconoscimento volti locale, che scrive i tag nei metadati dei file. Licenza una tantum [D, schede di terzi].
- **Funzioni utili per noi:** gestione di NAS e dischi USB anche offline (recensione 2023) [D].
- **Limiti:** dettagli e prezzo non verificati sul sito ufficiale [?].

---

## 2. Visualizzatori con import e riordino

### Adobe Bridge (Mac, Windows, con Creative Cloud)
- **Photo Downloader:** sottocartelle "Data scatto" in vari formati, oppure nome personalizzato; rinomina all'importazione con data, ora e metadati [V].
- **Batch Rename:**
  - Anteprima prima di applicare, preset salvabili [V].
  - Rinomina sul posto, oppure copia o sposta in un'altra cartella [V].
  - La numerazione segue l'ordinamento corrente [V].
- **Limiti:** niente catalogo dei dischi offline e niente annulla dichiarato per la rinomina in serie [?]. Advanced Rename all'importazione esiste solo su macOS [V].
- **Per noi:** l'anteprima "vecchio → nuovo" e i preset sono lo standard che gli utenti si aspettano.

### XnView MP (Mac, Windows, Linux; gratis per uso privato)
- **Import and Sort:** copia o sposta in sottocartelle per data EXIF, anche nel formato aaaa-MM [V].
- **Batch rename:** si possono mettere percorsi nel nome, ma secondo gli utenti è fragile: la conversione in serie modifica i file e la barra rovescia viene sostituita [V, forum].
- **Limiti:** nessuna rete di sicurezza; nel forum lo sviluppatore raccomanda di fare un backup prima [V].
- **Per noi:** esempio da non seguire. Il riordino va sempre separato dalla conversione dei file.

---

## 3. Riordinatori per data e GPS (EXIF)

### ExifTool (riga di comando, tutte le piattaforme, gratis)
- **Cos'è:** il motore sotto quasi tutti questi strumenti.
- **Funzioni utili per noi:**
  - `-Directory<DateTimeOriginal -d %Y/%m/%d` sposta i file in cartelle per data [V].
  - `-testname` è la prova a secco: mostra vecchio e nuovo nome senza toccare niente [V].
  - Con `-FileName` che contiene una barra cambia anche la cartella [D].
  - Non sovrascrive file già esistenti; `%-c` aggiunge un contatore [D].
  - Geolocalizzazione inversa da ExifTool 13.x (le coordinate diventano città) con un database interno offline [D]. Elodie lo usa proprio per questo.
- **Limiti:** nessuna interfaccia. Le GUI (ExifToolGUI per Windows, "Chronos" non trovato) sono sottili [?].
- **Per noi:** è il riferimento per la logica "prova a secco → applica" e per il fallback sui campi data.

### Elodie (open source, Python)
- **Cos'è:** riordinatore da riga di comando basato su EXIF.
- **Funzioni utili per noi:**
  - Cartelle predefinite anno-mese/luogo, per esempio `2015-07-Jul/Mountain View` [V].
  - Schema in `config.ini` con segnaposto (`%year`, `%location`, `%camera_make`, album) e **catene di ripiego con `|`**: album, poi luogo, poi un'etichetta predefinita [V].
  - Senza GPS il file finisce in "Unknown Location" [V].
  - `generate-db` crea un database di hash SHA-256 e `verify` controlla il "bit rot" [V].
  - `update` corregge luogo, data o album nell'EXIF e risposta il file di conseguenza [V].
  - Geocodifica: MapQuest è deprecato, ora usa ExifTool [V].
- **Limiti:** 83 issue aperte e 33 PR aperte; manutenzione incerta [V]. Solo riga di comando.

### Ordigi (fork di Elodie)
- **Funzioni utili per noi:** schema `{%Y}/{%m-%b}-{city}-{folder}` con ripiego a barra verticale e database SQLite dei metadati [V, solo dall'estratto del README; il sito blocca i bot].
- **Limiti:** progetto piccolo [D].

### Phockup (open source, Python e Docker)
- **Funzioni utili per noi:**
  - Struttura anno/mese/giorno personalizzabile [V].
  - Copia di default; `--move` per spostare, `--link` per creare hard link [V].
  - `--dry-run` [V].
  - I file senza data vanno in `unknown`, così la cartella d'origine si può svuotare in sicurezza [V].
  - Doppioni confrontati per checksum: un file identico viene saltato, uno diverso con lo stesso nome prende il suffisso `-1` [V].
  - Date estratte con regex dal nome del file, scelta del campo EXIF, ripiego sulla data di modifica [V].
- **Limiti:** non gestisce in modo esplicito le coppie RAW+XMP o RAW+JPEG [V, il README non ne parla].
- **Per noi:** gli **hard link** sono un'idea forte per "vedere" un riordino senza duplicare i dati.

### PhotoStructure (Mac, Windows, Linux, Docker)
- **Cos'è:** libreria che ordina in automatico.
- **Funzioni utili per noi:**
  - **Copia, non sposta mai** gli originali, in cartelle `2019/2019-05-01` con il nome originale [V].
  - Lo schema di cartelle è modificabile: se lo si cambia, riorganizza tutto [V].
  - I doppioni sono "visivi": varianti dello stesso scatto raggruppate [V].
  - Deduce le date mancanti da file vicini, nomi di cartelle e timbri [V].
- **Limiti:** non libera spazio, perché copia [V, forum]; con l'orologio della fotocamera sbagliato mette foto nella cartella 2000-01-01 [V, forum].

### PhotoMove (solo Windows)
- **Funzioni utili per noi:** sposta o copia in cartelle anno/mese/giorno dalla data di scatto, con il modello di fotocamera facoltativo; la versione Pro offre più schemi [D, terzi].
- **Limiti:** solo Windows; schemi rigidi [D].

### Advanced Renamer (Windows, Mac)
- **Funzioni utili per noi:**
  - Anteprima prima di rinominare e **annulla dell'intero lotto** [V].
  - Crea cartelle da EXIF [V].
  - Nome della città dal GPS [V].
- **Limite importante:** la geocodifica usa un **database online**, quindi serve internet [V]. È un esempio di cosa noi **non** dobbiamo fare.

### A Better Finder Rename 12 (Mac)
- **Funzioni utili per noi:**
  - Tratta insieme i **file collegati** (RAW+JPEG+XMP) e usa i metadati dell'uno per rinominare gli altri [V].
  - Controllo fine su quale data usare [V].
  - Preset con trascinamento [V].
  - Richiede macOS 15 o successivo (v12.36) [V].
- **Limiti:** niente geocodifica e annulla non documentato [?].
- **Per noi:** più vicino a RawLine Rename che a Space.

---

## 4. Server self-hosted (solo idee)

### Immich
- Storage template con default `Year/Year-Month-Day/Filename.Extension` [V].
- Segnaposti condizionali, per esempio `{{#if album}}{{album}}{{else}}Other{{/if}}` [V].
- Il nuovo schema vale per i caricamenti nuovi; i file esistenti si spostano solo lanciando a mano il job "Storage Template Migration" [V].
- **Idea:** cambiare lo schema non deve mai spostare tutto in automatico. Serve un passo esplicito.

### PhotoPrism
- Due modi distinti [V]:
  - *Index*: indicizza sul posto, nomi invariati, originali anche in sola lettura.
  - *Import*: toglie i doppioni, rinomina e ordina per anno e mese.
- `.ppignore` per escludere cartelle [V]; i sidecar vanno in una cartella separata [V].
- **Idea:** si cataloga prima in sola lettura, e il riordino è un'azione a parte.

---

## 5. Copia, sincronizzazione e verifica (sicurezza)

### Carbon Copy Cloner 7 (Mac)
- **SafetyNet:** i file sostituiti o cancellati sulla destinazione finiscono in `_CCC SafetyNet` invece di sparire [V].
- **Backup Health Check** (ex "Find and replace corrupted files"):
  - Calcola il checksum di sorgente e destinazione e sostituisce i file illeggibili [V].
  - Rende i backup molto più lenti [V, forum].
  - "Corrotto" significa illeggibile fisicamente, non "alterato" [V].
- **Per noi:** il cestino interno con data, separato dal Cestino di macOS.

### ChronoSync (Mac)
- **Verify Copied Data** ricontrolla solo i file appena copiati e raddoppia i tempi [V].
- **Validate** è un'azione separata che confronta bit per bit tutto il contenuto [V].
- **Validate then Synchronize** (v12) [V].
- *Archive Replaced/Deleted Files* sposta in una cartella d'archivio [V].
- **Idea:** separare "verifica di ciò che ho appena copiato" dalla "verifica completa dell'archivio".

### FreeFileSync (open source, Mac, Windows, Linux)
- Anteprima del confronto con frecce e colori prima di sincronizzare [V].
- Versioning in una cartella con data e ora [V].
- Cestino per le rimozioni locali, con un avviso se il cestino non è disponibile su macOS [V].
- La verifica dopo la copia è un'opzione nascosta [V, forum 2010; da verificare oggi].

### IntegrityChecker (diglloydTools, Java)
- SHA1 per ogni file in un `.ic` nascosto nella cartella, oppure un unico `.icjh` per l'intero albero [V].
- Comandi `update`, `verify` e `status` [V].
- L'autore consiglia di verificare i dischi di backup ogni 4-6 mesi [V].
- Ultima release vista: 3.0 fc9, gennaio 2023 [V].
- **Idea:** il manifesto di hash **viaggia con il disco**, così si verifica anche su un altro Mac.

### ForkLift 4 e Path Finder (Mac)
- ForkLift 4 ha una finestra Sync con anteprima dei file da sincronizzare [V]. La 4.7.5 (settembre 2026) evita trasferimenti in conflitto [V].
- Path Finder non è stato verificato in questa ricerca [?].
- **Per noi:** utili come file manager, non come riordinatori.

### Fileside (Mac, Windows)
- File manager a riquadri con area di lavoro salvabile per progetto [V].
- **"Full undo for everything"** [V].
- Unione avanzata di cartelle [V].
- Ultima versione vista: 2.0.5, luglio 2026 [V].
- **Idea:** l'annulla universale come promessa di prodotto.

---

## 6. Organizzatori a regole e AI (2025-2026)

### organize (tfeldmann, open source)
- Regole in YAML: `locations` più filtri e azioni, controllate dall'alto in basso [V].
- `organize sim` è la prova a secco, `organize run` applica [V].
- Tag per eseguire o saltare gruppi di regole [V].
- **Idea:** regole leggibili e simulabili, con una prova obbligatoria prima di applicarle.

### Floxtop (Mac)
- AI sul dispositivo; richiede Apple Intelligence per la classificazione [V].
- Mostra le 5 destinazioni più probabili per ogni file [V].
- Annulla per le azioni in blocco (1.9.0, aprile 2026) [V].
- Pro a 19,99 USD una tantum [V, sito del produttore].
- **Limiti:** pensato per documenti e Download, non per archivi fotografici [D].

### OCDify, SweepDisk, FilesMagicAI, VaultSort 3, RenameClick (Mac, 2025-2026)
- Organizzatori AI che dichiarano di essere offline: LLM locale con llama.cpp (OCDify), Apple Intelligence (FilesMagicAI), Apple Silicon (VaultSort, maggio 2026) [D, schede e Product Hunt].
- **Limiti:** tutti generici, nessuno specifico per la fotografia.

### Sparkle (Every)
- Abbonamento, citato a 30 USD al mese [D].
- Organizza **solo dai nomi dei file** senza aprirli [D].
- Usa la rete [D]. Non è compatibile con la regola offline.

### Sorted (macOS)
- Non trovato in modo affidabile [?].

---

## Scartate
- **Photo Date Organizer, EXIF ReName, Namexif e Chrono Namer:** vecchie, solo Windows o abbandonate.
- **Daminion e ACDSee:** poco pertinenti, come detto sopra.
- **Sparkle:** usa il cloud.
- **Immich e PhotoPrism:** sono server, quindi tenute solo come fonte di idee.

---

## Le 10 idee migliori per RawLine Space

1. **Sempre prima la prova a secco, poi il piano.** Riprende `-testname` di ExifTool, `--dry-run` di Phockup, `organize sim` e l'anteprima di FreeFileSync e Bridge. Ogni riordino produce un piano leggibile (vecchio → nuovo, conteggi, conflitti) che si salva e si applica in un secondo momento.
2. **Annulla dell'intero lotto, anche dopo giorni.** Riprende Advanced Renamer e Fileside. Il diario delle operazioni resta su disco e permette di annullare tutto anche dopo aver riavviato l'app.
3. **Il cestino di RawLine al posto della cancellazione.** Riprende SafetyNet e il versioning di FreeFileSync. Ciò che "alleggeriamo" va in una cartella datata sullo **stesso volume**, quindi lo spostamento è istantaneo e non occupa spazio in più. Si svuota solo dopo una conferma esplicita e un periodo di attesa.
4. **Manifesto di hash che vive sul disco.** Riprende IntegrityChecker e `verify` di Elodie. Un file nascosto per volume con gli hash (xxHash o SHA-256) permette di verificare un disco su qualunque Mac e di ripetere la verifica ogni 4-6 mesi. Va distinto il "verifica ciò che ho copiato" dalla "verifica completa", come in ChronoSync.
5. **Dischi riconosciuti per identità, non per nome.** Riprende IMatch. Il disco si riconosce dall'UUID del volume e dal seriale; quando è scollegato resta catalogato con miniature e metadati, e torna online da solo. Serve un comando "Ritrova" per quando un disco viene clonato o cambiato.
6. **Famiglie di file: RAW, JPEG, XMP ed export.** Riprende le relazioni buddy/versioni di IMatch e i file collegati di A Better Finder Rename. Tutto si sposta e si rinomina insieme. "Tieni solo il RAW usato" significa tenere i RAW che hanno una **versione** esportata, una stella o un colore.
7. **Schemi di cartelle con catene di ripiego.** Riprende Elodie (`%album|%location|"Senza luogo"`) e Immich (`{{#if}}`). Per esempio `{Anno}/{Data}-{Cliente|Luogo|"Da smistare"}`. Quello che non si riesce a classificare va in una cartella "Da smistare", mai in un posto a caso.
8. **Geocodifica 100% offline.** Al contrario di Advanced Renamer, che va online, si usa un database di città incluso nell'app, come quello di ExifTool 13. Si aggiunge il ripiego "data e ora vicine a una foto con GPS", sul modello delle date dedotte di PhotoStructure.
9. **Catalogare in sola lettura, riordinare come azione separata.** Riprende *Index* contro *Import* di PhotoPrism e la migrazione manuale di Immich. Cambiare lo schema non sposta mai niente da solo; si aggiunge l'opzione "copia, non spostare" come PhotoStructure, per chi vuole provare.
10. **Viste senza spostare i file.** Riprende `--link` di Phockup e gli album di Mylio. Si può creare un albero "per cliente" o "per luogo" con hard link o alias, senza duplicare i dati e senza toccare l'archivio originale. Serve per provare uno schema prima di applicarlo davvero.

Idea in più: la **copia leggera** di Mylio (SpaceSaver). Per i dischi scollegati si tengono in catalogo anteprime da circa 2560 px, così si possono sfogliare e scegliere cosa alleggerire anche senza il disco collegato.

---

## Fonti (link)

- IMatch, file offline: https://photools.com/help/imatch/content/en/topics/offline-files.htm
- IMatch, relazioni e versioni: https://www.photools.com/help/imatch/content/en/topics/rel_versions.htm , https://photools.com/help/imatch/content/en/topics/rel_buddy.htm
- Photo Supreme, funzioni: https://www.idimager.com/features-overview
- Photo Supreme, novità 2025 e 2026: https://www.idimager.com/what-s-new-in-photo-supreme-2025 , https://www.idimager.com/photo-supreme-v2026-released
- Photo Supreme, prezzi: https://www.idimager.com/pricing
- Mylio: https://mylio.com/
- Mylio, recensione Fstoppers: https://fstoppers.com/lightroom/mylio-adds-securecloud-its-offerings-photographers-678583
- digiKam, quick start: https://docs.digikam.org/en/getting_started/quick_start.html
- digiKam, importazione per data: https://mail.kde.org/pipermail/digikam-users/2025-January/036943.html
- digiKam, bug sulla rinomina: https://bugs.kde.org/show_bug.cgi?id=478002
- Daminion, prezzi: https://daminion.net/pricing/
- ACDSee, novità: https://www.acdsee.com/en/photo-studio/whats-new
- ImageRanger: https://alternativeto.net/software/imageranger/about
- Adobe Bridge, Photo Downloader: https://helpx.adobe.com/bridge/desktop/organize-and-find-files/organize-files-and-folders/import-photos.html
- Adobe Bridge, Batch Rename: https://helpx.adobe.com/vn_en/bridge/desktop/organize-and-find-files/tag-and-find-files/batch-rename-files.html
- XnView MP, forum: https://newsgroup.xnview.com/viewtopic.php?p=175978 , https://newsgroup.xnview.com/viewtopic.php?p=203475
- ExifTool, FileName e Directory: https://exiftool.org/filename.html
- ExifTool, geolocalizzazione: https://exiftool.org/geolocation.html
- Elodie: https://github.com/jmathai/elodie
- Ordigi: https://git.hadoly.fr/takino/ordigi
- Phockup: https://github.com/ivandokov/phockup
- PhotoStructure, organizzazione automatica: https://photostructure.com/getting-started/automatic-library-organization/
- PhotoStructure, doppioni: https://photostructure.com/guide/what-do-you-mean-by-deduplicate/
- PhotoMove: https://alternativeto.net/software/photomove/about
- Advanced Renamer: https://advancedrenamer.com/
- Advanced Renamer, GPS: https://advancedrenamer.com/user_guide/howto_gps
- A Better Finder Rename 12: https://www.publicspace.net/ABetterFinderRename/version12.html
- Immich, storage template: https://docs.immich.app/administration/storage-template/
- PhotoPrism, originali: https://docs.photoprism.app/user-guide/library/originals
- Carbon Copy Cloner 7: https://bombich.com/
- CCC, forum MacRumors: https://forums.macrumors.com/threads/carbon-copy-cloner-7-users-thread.2302964/page-33
- ChronoSync, Verify e Validate: https://www.econtechnologies.com/the-difference-between-verify-and-validate/
- ChronoSync, novità v12: https://downloads.econtechnologies.com/manuals/Whats_New_in_v12.pdf
- FreeFileSync: https://freefilesync.org/
- FreeFileSync, forum sulla verifica: https://freefilesync.org/forum/viewtopic.php?p=4266
- IntegrityChecker: https://macperformanceguide.com/Software-IntegrityChecker.html
- IntegrityChecker 3.0: https://MacPerformanceGuide.com/blog/2023/20230122_1200-IntegrityCheckerJava-3_0fc9.html
- ForkLift 4.7.5: https://alternativeto.net/news/2026/9/forklift-4-7-5-improves-sync-and-prevents-conflicting-file-transfers/
- Fileside: https://www.fileside.app/
- Fileside 2.0.5: https://www.fileside.app/blog/2026-07-18_release-notes-2.0.5/
- organize: https://organize.readthedocs.io/en/latest/rules/
- Floxtop 1.9.0: https://alternativeto.net/news/2026/4/floxtop-1-9-0-adds-multi-file-workflows-bulk-actions-and-search/
- Floxtop: https://alternativeto.net/software/floxtop/about
- Organizzatori AI 2026: https://fast.io/resources/best-ai-file-organizers-2026/
- Sparkle, alternative: https://alternativeto.net/software/sparkle-ai/
- OCDify: https://www.hunted.space/product/ocdify
- VaultSort 3: https://buttondown.com/vaultsort/archive/vaultsort-3-is-here-smart-categorize-has-shipped/
