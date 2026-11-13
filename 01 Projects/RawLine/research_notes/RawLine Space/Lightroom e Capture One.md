# RawLine Space — Lightroom, Capture One e abbinamento export↔RAW

Ricerca dell'11 novembre 2026. Legenda: **[V]** verificato su una fonte (link nella sezione 8). **[D]** dedotto o esperienza comune, da confermare con una prova su file veri. **[P]** da provare a mano.

Due problemi:
- **(A)** se RawLine Space sposta le cartelle fuori dall'app, Lightroom Classic e Capture One perdono le foto;
- **(B)** per liberare spazio bisogna abbinare ogni export JPEG/TIFF al RAW (+XMP) da cui è nato, anche quando il nome è cambiato.

---

## 1. Come i cataloghi memorizzano i percorsi

### Lightroom Classic (.lrcat)
- Il file `.lrcat` è un database SQLite **[V]**. Accanto ci sono `.lrcat-wal` e `.lrcat-shm` mentre il catalogo è aperto (modalità WAL), `Previews.lrdata` e, dalle versioni recenti, `.lrcat-data` **[V]**.
- Il percorso completo di un file è diviso su tre tabelle **[V]** (formato documentato da lrcat-extractor e dalle query della comunità):
  - **`AgLibraryRootFolder`**: una riga per ogni cartella "radice" del pannello Cartelle. Colonne `id_local`, `id_global` (UUID), `absolutePath` (percorso assoluto con `/` finale, per es. `/Volumes/Archivio/Foto/`), `name`, `relativePathFromCatalog` (percorso relativo rispetto al catalogo, **NULL se è su un altro volume**).
  - **`AgLibraryFolder`**: una riga per cartella. `id_local`, `id_global`, `rootFolder` (→ `AgLibraryRootFolder.id_local`), `pathFromRoot` (per es. `2024/2024-06-12 Cervino/`, **vuoto per la radice**), `parentId`.
  - **`AgLibraryFile`**: una riga per file. `id_local`, `id_global`, `folder` (→ `AgLibraryFolder.id_local`), `baseName`, `extension`, `idx_filename`, `lc_idx_filename`, `originalFilename`, `sidecarExtensions` (per es. `XMP` o `JPG` per le coppie RAW+JPEG), `importHash`, `modTime`, `externalModTime`, `md5`.
  - **`Adobe_images`**: la foto vera e propria. `rootFile` → `AgLibraryFile.id_local`. Le copie virtuali sono altre righe di `Adobe_images` con lo stesso `rootFile` e `masterImage` valorizzato. Qui stanno `captureTime`, `fileFormat`, `pick`, `rating`, `colorLabels`.
  - Percorso = `absolutePath || pathFromRoot || baseName || '.' || extension` **[V]**.
- Conseguenza **[D]**: spostare l'intero albero sotto una radice cambia **una sola riga** (`absolutePath`). Spostare una sottocartella in un'altra radice tocca `AgLibraryFolder` (`rootFolder` + `pathFromRoot`) di quella cartella e di tutte le sue figlie.
- `AgLibraryFile.originalFilename` conserva il nome del file al momento dell'import **[D, da verificare sul catalogo di prova]**. È utile per l'abbinamento (§6).
- Lo schema cambia tra le versioni di Lightroom. La documentazione pubblica copre LR 4–6 più le query della comunità fino a Classic 13. Adobe non pubblica nessuno schema ufficiale **[V]**.

### Capture One: cataloghi
- `.cocatalog` è un pacchetto (cartella) che contiene `.cocatalogdb`, un database SQLite in stile Core Data (tabelle `Z…`) **[V]**.
- `ZIMAGE.ZIMAGELOCATION` → `ZPATHLOCATION.Z_PK`. In `ZPATHLOCATION`, `ZMACROOT` (oppure `ZWINROOT`) è il volume e `ZRELATIVEPATH` è il percorso dentro il volume. `ZIMAGE` ha il nome del file e `ZSIDECARPATH` **[V, forum + script di migrazione di darktable]**.
- Le immagini **referenziate** del catalogo hanno percorsi **assoluti che partono dall'etichetta del volume** **[V]**. Le immagini **gestite** stanno dentro il pacchetto del catalogo e non sono un problema per RawLine Space.
- Regolazioni e metadati vivono nel database. Capture One non scrive mai nell'originale **[V]**. Gli XMP accanto ai file esistono solo se la sincronizzazione dei metadati è impostata su "Full" **[V]**.

### Capture One: sessioni
- Una sessione è una cartella con `NomeSessione.cosessiondb` e le sottocartelle `Capture`, `Selects`, `Output`, `Trash` **[V]**.
- Le regolazioni stanno in `CaptureOne/Settings*/*.cos` **accanto alle immagini**, cioè nella sottocartella `CaptureOne` di ogni cartella di immagini **[V]**. Le anteprime stanno in `CaptureOne/Cache`.
- I riferimenti alle cartelle standard della sessione sono **relativi**: se si sposta tutta la sessione, funziona **[V]**. Alcuni utenti però hanno visto **sottocartelle aggiunte ed album di sessione salvati come percorsi assoluti** **[V, segnalazioni sul forum]**.

---

## 2. Spostamenti fuori dall'app e ricollegamento

### Lightroom Classic
- Lightroom conosce solo l'ultima posizione registrata. Se un file o una cartella viene spostato o rinominato nel Finder, o se il disco cambia nome di mount, compaiono il "?" sulla cartella e il "!" sulla miniatura **[V]**.
- Rimedi nativi **[V]**:
  - **Trova cartella mancante** (*Find Missing Folder*), col clic destro sulla cartella col "?": la si indica nella nuova posizione. **Se lo si fa sulla cartella più alta**, tutte le sottocartelle con nomi e struttura invariati si ricollegano da sole. Per questo la Lightroom Queen consiglia di tenere nel pannello Cartelle un'unica gerarchia sotto una radice (*Mostra cartella principale*).
  - **Aggiorna posizione cartella** (*Update Folder Location*): stessa funzione, disponibile anche quando la cartella non risulta mancante. **[D]**: in pratica riscrive `AgLibraryRootFolder` o `AgLibraryFolder`.
  - **Individua** (*Locate*) sulla singola foto, con l'opzione "Trova le foto mancanti vicine". Segnalazione di settembre 2025: l'opzione **è sparita in Classic 14.4**, anche se la guida Adobe la descrive ancora **[V, forum]**.
  - **Libreria › Trova tutte le foto mancanti** crea la collezione "Fotografie mancanti" **[V]**.
- Limiti **[V]**:
  - i **file rinominati fuori da Lightroom vanno ricollegati uno per uno**;
  - "Sincronizza cartella" o un nuovo import **possono far perdere le regolazioni**, perché creano foto nuove senza la storia;
  - le anteprime avanzate (Smart Previews) possono **nascondere il "!"** di un file mancante.
- Nell'SDK Lua dei plugin non c'è nessuna API per spostare o ricollegare file. Un plugin GitHub che riordina per data deve copiare e reimportare, e non può togliere le vecchie voci **[V]**.

### Capture One
- **Locate…** col clic destro su immagine, cartella o **volume**. Sulla cartella ricollega tutte le immagini al suo interno. Sul volume serve quando il disco ha cambiato nome **[V]**.
- Spostamenti e rinomine fatti **dentro** Capture One mantengono i collegamenti. Quelli fatti nel Finder li rompono. Le foto offline si possono regolare grazie alle anteprime, ma non esportare (tranne JPEG QuickProof) **[V]**.
- Non esiste un elenco dei percorsi mancanti, né un ricollegamento di massa per i file rinominati. Gli utenti lo chiedono da anni **[V]**.
- **Sessioni**: si sposta la cartella intera e la si riapre con File › Apri sessione **[V]**. Le `.cos` viaggiano con le immagini solo se si sposta anche la sottocartella `CaptureOne` **[D, conseguenza della struttura]**.

---

## 3. Strumenti di terzi e rischi di scrivere nel catalogo

### Strumenti trovati
- **Any Source** (John R. Ellis, johnrellis.com): ha il comando **Find Missing Folders**, che seleziona le cartelle che Lightroom crede mancanti e ne scrive i percorsi in `missing-folders.txt` sulla Scrivania **[V]**. **Non ricollega niente.** Non ho trovato nessun plugin di Ellis chiamato "Fix Missing".
- **Nessun plugin che ricolleghi in massa per ora di scatto o hash** dopo una rinomina **[V, ricerca senza risultati]**. Una funzione così sarebbe una nicchia libera.
- `lrcat-extractor` (Rust) e le query SQL della comunità servono solo a **leggere** i cataloghi.
- Per Capture One: lo script `migrate_capture_one_pro.sql` di darktable legge `.cocatalogdb` **[V]**.

### Rischi di scrivere direttamente nel catalogo
- **[V]** Esistono casi documentati in cui si è corretto `AgLibraryRootFolder.absolutePath` a mano (Dropbox spostato): backup, Lightroom chiuso, aggiornamento, riapertura. Tutte le fonti però lo presentano come un'operazione a rischio di corruzione, senza alcun supporto Adobe.
- Rischi concreti **[D]**:
  1. **catalogo aperto**: con la modalità WAL, scrivere mentre Lightroom gira produce stati incoerenti o perdite. Bisogna controllare il file `.lock` e i processi;
  2. **schema non documentato** che cambia tra le versioni, con trigger e indici (`idx_filename`, `lc_idx_filename`) da tenere allineati;
  3. **unicità**: due cartelle col nuovo percorso generano l'errore "UNIQUE constraint failed", già segnalato sul forum Adobe in casi simili;
  4. **sincronizzazione con Lightroom cloud** e cataloghi con Smart Previews;
  5. **perdita della garanzia d'integrità**: Adobe offre solo il controllo integrità e "Importa da un altro catalogo" per riparare;
  6. per Capture One, `ZRELATIVEPATH`/`ZMACROOT` sono campi Core Data con colonne di versione (`Z_OPT`) e una cache. Nessuna fonte conferma che basti modificarli.
- **Buona pratica** **[V/D]**:
  - lavorare su una **copia** del catalogo con l'app chiusa;
  - eseguire `PRAGMA integrity_check` prima e dopo (la guida di Capture One la consiglia per i suoi cataloghi);
  - toccare solo le righe delle cartelle, mai i file;
  - tenere un registro per tornare indietro;
  - far aprire il catalogo all'utente e verificare.

---

## 4. Metadati degli export che portano al RAW

### Lightroom Classic e Camera Raw
| Campo | Cosa contiene | Affidabilità per risalire al RAW |
|---|---|---|
| `XMP-xmpMM:PreservedFileName` | nome originale del file sorgente al momento dell'export **[V, forum, J. R. Ellis]** | alta se l'export usa "Tutti i metadati" |
| `XMP-crs:RawFileName` | nome del RAW (senza percorso) **[V]**. Lightroom lo **aggiorna se si rinomina il RAW in LR**, Bridge no **[V]** | media: segue il nome *attuale* del RAW in LR |
| `XMP-xmpMM:DocumentID` / `OriginalDocumentID` / `InstanceID` | `xmp.did:` / `xmp.iid:`, basati su UUID **[V, Adobe]**. OriginalDocumentID dovrebbe restare quello della prima versione | **[P]** non ho trovato nessuna fonte che dica se l'OriginalDocumentID di un export LR coincida con un valore del RAW o del suo XMP |
| `XMP-xmpMM:DerivedFrom` (stRef: DocumentID, InstanceID, OriginalDocumentID, FilePath) | collegamento al genitore, scritto **di sicuro da Photoshop** **[V]** | per i JPEG di Lightroom non è confermato **[P]** |
| `XMP-xmpMM:History` (action, when, softwareAgent, parameters) | storia dei salvataggi (Photoshop, ACR) **[V struttura]** | indicativo: dice quale software e quando |
| `XMP-crs:*` (tutte le regolazioni) | parametri di sviluppo | si possono confrontare con l'XMP del RAW, a conferma |
| EXIF `DateTimeOriginal`, `SubSecTimeOriginal`, `OffsetTimeOriginal`, `SerialNumber`/`BodySerialNumber`, `LensSerialNumber`, `Make`/`Model` | dati di scatto copiati dal RAW | **ottimi** come chiave, se non vengono tolti (vedi sotto) |
| `EXIF:DateTime` (ModifyDate) | **ora dell'export**, non dello scatto **[V]** | non usarlo |

**Impostazioni di metadati all'esportazione** (Lightroom Classic, JPEG/TIFF/PSD) **[V]**:

| Opzione | Data e ora di scatto | EXIF della fotocamera (corpo, matricola, obiettivo) | crs (sviluppo) | PreservedFileName / RawFileName |
|---|---|---|---|---|
| **Solo copyright** | **tolta**: nessun EXIF | no | no | **riportano il nome dell'export**, non quello del RAW **[V, forum]** |
| Copyright e contatti | tolta | no | no | come sopra **[D]** |
| Tutto tranne fotocamera e Camera Raw | **resta** | no (con qualche fuga segnalata come bug) | no | **[P]** |
| Tutto tranne Camera Raw | resta | sì | no | **[P]**: RawFileName è nel namespace crs e probabilmente se ne va **[D]** |
| **Tutti i metadati** | resta | sì | sì | **presenti, col nome originale** **[V]** |

- "Rimuovi info persone" e "Rimuovi info posizione" sono attive di default nelle due opzioni "copyright" **[V]**.
- Gli export **DNG e Originale** includono sempre tutti i metadati **[V]**.
- Conseguenza: con "Solo copyright", che è comune per i JPEG ai clienti, **non resta niente di utile tranne i pixel**. L'abbinamento deve funzionare anche per somiglianza d'immagine (§6).

### Capture One
- **Di default l'export non include metadati**: vanno attivati nella ricetta (scheda Metadati) **[V]**. Quando li si attiva, passano EXIF, IPTC e parole chiave.
- Ho trovato **nessuna prova** che Capture One scriva `PreservedFileName`, `RawFileName`, `DerivedFrom` o `DocumentID` legati al RAW **[V, ricerca senza risultati]**.
- C'è un campo e un token **"Original Filename"** che Capture One può conservare e usare in nome o metadati, ma va popolato **[V]**.
- L'EXIF di scatto (DateTimeOriginal, matricola) passa se i metadati sono attivi nella ricetta **[D, da provare]**.

### Photo Mechanic
- Namespace `XMP-photomech`: `ColorClass`, `Tagged`, `Prefs` ("Tagged:0, ColorClass:1, Rating:2, FrameNum:3"), `PMVersion`, `EditStatus`, `TimeCreated`, `CreatorIdentity`, `CountryCode`. Nel trailer IPTC ci sono `FrameNum`, `Rotation` e i ritagli **[V, ExifTool]**.
- **Nessun campo standard per il nome originale** **[V]**. Durante l'ingest le variabili possono scrivere `{filename}` in un campo IPTC, ma è una scelta dell'utente **[D]**.
- Photo Mechanic di solito **rinomina** già durante l'ingest. Quindi il nome del RAW sul disco spesso non è quello della fotocamera, mentre ImageNumber e ShutterCount nel RAW restano **[D]**.

---

## 5. Identificare uno scatto in modo univoco

Chiave generale **[D, convenzione diffusa e coerente con le note di ExifTool]**:

> `Make + Model + matricola del corpo + DateTimeOriginal + SubSecTimeOriginal (+ contatore scatti, quando c'è)`

- `SubSecDateTimeOriginal` è un tag composito di ExifTool che nasce da DateTimeOriginal + SubSecTimeOriginal/OffsetTimeOriginal **[V]**. È indispensabile per le raffiche: senza i decimi di secondo, due scatti nello stesso secondo collidono.
- Phil Harvey ricorda che **ExifTool non confronta i pixel**. I duplicati per metadati sono un'euristica: chi ha bisogno di certezza deve aggiungere un hash del contenuto **[V]**.
- ExifTool **non ha un "ID scatto" unico tra le marche**. Le stringhe in uso sono `-SerialNumber`, `-InternalSerialNumber`, `-ShutterCount`, `-ImageCount`, `-FileNumber` per marca. Con `-api` e `-if` si filtra **[V tags]**.

| Marca | Matricola | Contatore per scatto | Note **[V, pagine TagNames di ExifTool]** |
|---|---|---|---|
| **Sony** | `SerialNumber` (0x2031), `InternalSerialNumber` (Tag9050) | `ShutterCount` / `ShutterCount2` / `ShutterCount3` in **Tag9050a/b/c/d** (cifrati, ExifTool li decifra) | 9050a: "modulo 65536 su alcuni modelli". 9050b: valido da luglio 2015 su ILCE/ILCA. 9050c: ILCE-1/7SM3/FX3. **9050d** (A6700, A7CII, A7CR, ZV-E1, A1 II, A7 V, A7R VI): **conta solo l'otturatore meccanico**, quindi con quello elettronico **non è univoco**. Ci sono anche `SequenceImageNumber`/`SequenceFileNumber` (posizione nella raffica) in Tag2010 |
| **Canon** | `SerialNumber` (0x000c), `InternalSerialNumber` (0x0096) | `FileNumber` (0x0008, cartella-file, per es. 100-1234), `FileIndex` + `DirectoryIndex` in CameraInfo. `ShutterCount` solo 1D Mark III e inaffidabile | il contatore di file si **azzera** se si cambia la numerazione. `ImageUniqueID` (0x0028) esiste nelle maker notes |
| **Nikon** | `SerialNumber` (0x001d, usato come chiave di decifratura), altro `SerialNumber` 0x00a0 | **`ShutterCount` (0x00a7)**: conta l'otturatore meccanico **ed elettronico** | il più affidabile delle quattro marche. `ImageCount` (0x00a5) |
| **Fujifilm** | `InternalSerialNumber` (0x0010): "unico per la maggior parte dei modelli", contiene il modello e la data di fabbricazione | `ImageCount` (0x1438): "**può tornare a 0 con un nuovo firmware**". `SequenceNumber` (0x1101) per le raffiche | `ImageGeneration` (0x1436): 0 = originale, **1 = ri-sviluppato dal RAW in macchina**, utile per riconoscere i JPEG fatti in camera |

Valutazione **[D]**:
- Nikon ShutterCount + matricola è quasi un ID perfetto.
- Per Sony va bene la matricola + SubSecDateTimeOriginal. Lo ShutterCount è un rafforzativo, e sui modelli 9050d con otturatore elettronico non basta.
- Canon e Fuji: data e decimi + matricola, col contatore come indizio secondario.
- **Attenzione agli orologi sbagliati o non sincronizzati tra due corpi**: Selects ha già la logica "orologi" e si può riusare.

Nell'**export** di Lightroom il contatore delle maker notes **di solito non arriva**: Lightroom non copia le MakerNotes nei JPEG **[D, comportamento comune, da verificare con exiftool]**. Restano gli EXIF standard (data, decimi, `SerialNumber` → `BodySerialNumber`, obiettivo), quindi la chiave che vale anche per gli export è **matricola + SubSecDateTimeOriginal**.

---

## 6. Proposta di abbinamento export↔RAW a più punti d'attacco (dal più affidabile)

Ogni livello produce un punteggio. Un export si considera abbinato solo sopra una soglia, e i casi incerti vanno all'utente.

1. **Catalogo, se disponibile (lettura soltanto)**. Lightroom registra gli export *pubblicati* (servizi di pubblicazione: tabelle `AgRemotePhoto` e simili **[D]**). Un export pubblicato collega con certezza foto e file. Per gli export normali Lightroom **non** tiene traccia del file prodotto **[D]**.
2. **`PreservedFileName` / `RawFileName` + stessa data e decimi**. Il nome coincide con un RAW (o con `AgLibraryFile.originalFilename`) **e** l'ora di scatto coincide: affidabilità ~certa.
3. **Matricola corpo + `SubSecDateTimeOriginal`** (+ Make/Model, + `LensSerialNumber`), uguali tra export e RAW: affidabilità molto alta. È robusto alle rinomine.
4. **`DocumentID`/`OriginalDocumentID`/`DerivedFrom`** dell'export uguali agli ID nell'XMP del RAW o nel DNG: alta, **ma solo se la prova [P] conferma che Lightroom li propaga**. Per gli export Photoshop (TIFF/PSD) `DerivedFrom` è affidabile.
5. **DateTimeOriginal al secondo senza matricola** + modello + obiettivo + dimensioni coerenti col ritaglio, con `crs:` dell'export uguali a quelle dell'XMP del RAW: media.
6. **Somiglianza d'immagine** (locale, offline): hash percettivo (dHash/pHash) dell'anteprima JPEG incorporata nel RAW (`PreviewImage`/`JpgFromRaw` via ExifTool, senza decodifica completa), confrontato con l'export ridimensionato e, se serve, l'embedding Vision di Apple (`VNGenerateImageFeaturePrintRequest`, sul dispositivo). Serve per gli export "Solo copyright". Funziona solo nella **stessa sessione/cartella/giornata** per non esplodere sui 100 TB, e richiede conferma quando il ritaglio o il bianco e nero è forte.
7. **Indizi di contesto** (solo per ordinare i candidati, mai da soli): nome con numero fotocamera (`DSC05480`, `_A7R1234`), cartella vicina o con la stessa data, data del file.

Regole di sicurezza **[D]**:
- non liberare mai spazio con un abbinamento dei livelli 5–7 senza conferma;
- tenere un rapporto con la prova usata per ogni coppia;
- non cancellare mai il RAW sulla base dell'abbinamento: semmai si cancella l'export doppio, o si sposta il RAW in archivio freddo.

---

## 7. Opzioni per RawLine Space sui cataloghi

| Opzione | Come | Pro | Contro |
|---|---|---|---|
| **A. Solo avviso** | Prima di spostare, RawLine Space cerca i `.lrcat` / `.cocatalog` / `.cosessiondb` (Spotlight locale + percorsi recenti di LR nelle preferenze), li **legge in sola lettura** su una copia e segnala "queste 12 cartelle sono in un catalogo" | zero rischi, offline, rapido, nessuna dipendenza dallo schema in scrittura | l'utente deve comunque ricollegare a mano |
| **B. Guida al ricollegamento** | Si sposta mantenendo la **struttura relativa** sotto una radice unica e si genera una scheda passo-passo: "In Lightroom, clic destro su *Foto 2019* › Trova cartella mancante › scegli `/Volumes/Archivio2/Foto 2019`". Per Capture One: "Locate… sul volume o sulla cartella" | sfrutta il fatto che **un solo ricollegamento sulla radice ripara tutto l'albero** (LR e C1). Rischio nullo per il catalogo. Si può anche spostare **solo cartelle intere, senza rinominare file**, così il ricollegamento resta sempre possibile | qualche passaggio manuale. Le foto rinominate fuori si ricollegano una per una, quindi RawLine Space **non deve mai rinominare file catalogati** |
| **C. Aggiornamento diretto del catalogo** | A Lightroom/C1 chiusi: backup del `.lrcat`, `PRAGMA integrity_check`, `UPDATE AgLibraryRootFolder SET absolutePath=…` (o `ZPATHLOCATION`), di nuovo il controllo d'integrità, registro per annullare | esperienza "magica" su grandi archivi | schema non documentato che cambia tra le versioni, rischio di corruzione, nessun supporto Adobe o Capture One, test continui a ogni aggiornamento di LR/C1. Se va male, il danno è enorme (anni di regolazioni) |
| **D. Ibrido (consigliato)** | **A** sempre + **B** come flusso standard. **C** solo come funzione avanzata e facoltativa, limitata al caso più semplice e sicuro (cambio di `absolutePath` di una radice in Lightroom), con backup automatico e verifica, disattivata per Capture One finché non ci sono prove | massimo beneficio e rischio controllato. Tutto offline, come da regola RawLine | più lavoro di sviluppo e test (cataloghi di prova di più versioni) |

Altri suggerimenti **[D]**:
- un pulsante "**Prepara Lightroom**", che mostri la cartella principale (*Show Parent Folder*) per avere un'unica radice prima dello spostamento;
- un controllo d'integrità dopo lo spostamento: si rilegge il catalogo e si confermano i nuovi percorsi, mostrando quanti file risultano ancora mancanti;
- non toccare mai le sottocartelle `CaptureOne/` né gli `.xmp` accanto ai RAW: vanno sempre spostati insieme al file.

---

## 8. Fonti

**Lightroom Classic: catalogo e percorsi**
- lrcat-extractor, formato .lrcat: https://rust-digger.code-maven.com/src/lrcat-extractor-0.4.1/doc/lrcat_format.md e https://docs.rs/lrcat-extractor/0.6.0/src/lrcat/libraryfiles.rs.html
- PetaPixel, ricerca SQL in più cataloghi: https://petapixel.com/2019/05/08/how-to-search-multiple-lightroom-catalogs-at-once-with-sql-tools
- Query del percorso completo: https://www.uniquephoto.com/community/qa/how-can-i-find-which-lightroom-catalog-contains-a-specific-photo
- Correzione manuale di AgLibraryRootFolder (Dropbox): https://www.uniquephoto.com/community/qa/how-can-i-fix-lightroom-seeing-all-dropbox-photos-as-new-after-the-dropbox-folder-path-changed
- Jeffrey Friedl, accesso diretto al DB SQLite: https://regex.info/blog/2006-07-29/221
- Separatori dei percorsi (Lightroom Queen): https://www.lightroomqueen.com/community/threads/semi-ot-question-re-file-path-on-windows.43010/post-1284962
- Adobe, catalogo corrotto: https://helpx.adobe.com/ca/lightroom-classic/desktop/technical-support/workflow-issues/catalog-issues/troubleshoot-corrupt-catalog.html
- Adobe, file WAL/SHM: https://community.adobe.com/t5/lightroom-classic-discussions/lrcat-shm-and-lrcat-wal-are-for/td-p/9505585

**Lightroom Classic: ricollegamento**
- Adobe, Individuare le foto mancanti: https://helpx.adobe.com/ee/lightroom-classic/help/locate-missing-photos.html
- Lightroom Queen, foto mancanti: https://www.lightroomqueen.com/lightroom-photos-missing-fix/ e https://www.lightroomqueen.com/check-catalog-missing-files/
- Julieanne Kost, ricollegamento: https://jkost.com/blog/?p=22606
- "Trova foto mancanti vicine" rimossa in 14.4: https://community.adobe.com/questions-675/find-nearby-missing-photos-option-has-been-removed-from-locate-missing-photo-983431
- Ricollegamento in massa: https://community.adobe.com/t5/lightroom-classic-discussions/batch-relink-missing-files/td-p/10501525
- Rinomina fuori da LR: https://community.adobe.com/t5/lightroom-classic-discussions/relink-edited-photos-after-name-change-outside-lightroom/m-p/14051364
- Limiti dell'SDK (fixfolders): https://github.com/jiaxuan/fixfolders.lrdevplugin
- John R. Ellis, Any Source: https://johnrellis.com/lightroom/anysource.htm

**Capture One**
- Ricollegare i file offline nei cataloghi: https://www.captureone.com/blog/relocating-offline-files-catalogs/
- Percorsi assoluti nei cataloghi: https://support.captureone.com/hc/de/community/posts/360012140517-Referenced-images-in-catalogs-use-absolute-paths-to-images
- Catalogo in un visualizzatore SQLite (ZIMAGE/ZPATHLOCATION): https://support.captureone.com/hc/es/community/posts/4404071937937-Viewing-catalogue-in-SQLite-viewer-editor
- Script di migrazione di darktable: https://sources.debian.org/src/darktable/5.2.1-1/tools/migrate_capture_one_pro.sql
- Relocate multiplo e percorsi mancanti: https://support.captureone.com/hc/fr/community/posts/9977547298717-Relocate-multiple-images-show-file-paths-for-missing-images?page=2
- Spostare le sessioni: https://support.captureone.com/hc/en-us/community/posts/360012182297-Move-or-rename-sessions , https://support.captureone.com/hc/fr/community/posts/360012191597-Troubleshooting-Moving-A-Session , https://support.captureone.com/hc/es/community/posts/360009392217-moving-a-session-problems-relative-vs-absolute
- Errore di connessione al database su dischi esterni/NAS: https://support.captureone.com/hc/en-us/articles/30493722534941-Fix-the-Database-connection-failed-error-when-using-external-or-NAS-drives
- Panoramica dell'esportazione: https://support.captureone.com/hc/en-us/articles/360002639458-Overview-of-exporting-images
- Metadati negli export: https://support.captureone.com/hc/es/community/posts/4414707628433-Metadata-when-exporting-files-JPEG-or-any-other

**Metadati XMP/EXIF**
- ExifTool, tag XMP (xmpMM, crs, aux): https://exiftool.org/TagNames/XMP.html
- ExifTool, Photo Mechanic: https://exiftool.org/TagNames/PhotoMechanic.html
- ExifTool, Sony / Canon / Nikon / Fujifilm: https://exiftool.org/TagNames/Sony.html , https://exiftool.org/TagNames/Canon.html , https://exiftool.org/TagNames/Nikon.html , https://exiftool.org/TagNames/FujiFilm.html
- Adobe, namespace xmpMM: https://developer.adobe.com/xmp/docs/XMPNamespaces/xmpMM
- Exiv2, xmpMM e crs: https://exiv2.org/tags-xmp-xmpMM.html , https://exiv2.org/tags-xmp-crs.html
- InQuest, gli ID XMP: https://inquest.net/?p=6381
- PreservedFileName negli export LR (J. R. Ellis): https://community.adobe.com/t5/lightroom-classic-ideas/p-embed-original-file-name-in-metadata-on-export/idc-p/15073335
- RawFileName nei sidecar dopo la rinomina: https://community.adobe.com/feature-requests-676/p-add-preserve-current-filename-in-xmp-metadata-as-a-checkbox-to-export-664989/index1.html
- Opzioni di metadati all'export: https://lightroomkillertips.com/controlling-metadata-export/
- Fughe con "Tutto tranne fotocamera e Camera Raw": https://community.adobe.com/t5/lightroom-classic-bugs/p-tag-xmp-photoshop-cameraprofiles-needs-to-be-removed-from-metadata-options-in-export-options/idi-p/14815152
- "Solo copyright" toglie la data di scatto: https://community.adobe.com/t5/lightroom-classic-discussions/capture-date-is-not-included-with-exif-data-during-export/m-p/12583341
- ExifTool forum, duplicati e confronto pixel: https://exiftool.org/forum/index.php?msg=39257 , SubSecDateTimeOriginal: https://exiftool.org/forum/index.php?msg=72475

---

## Prove a mano da fare [P]
1. Esportare un ARW, un CR3, un NEF e un RAF da Lightroom con ognuna delle 5 opzioni di metadati, poi `exiftool -a -G1 -s -xmp-xmpMM:all -xmp-crs:RawFileName -SerialNumber -SubSecDateTimeOriginal -MakerNotes:all` e confrontare con il RAW e il suo XMP. Serve a confermare DocumentID/DerivedFrom e la sorte delle maker notes.
2. Fare lo stesso con una ricetta di Capture One, con e senza metadati.
3. Su un catalogo di prova (Classic 13/14/15): spostare un albero nel Finder, eseguire "Trova cartella mancante" e confrontare `AgLibraryRootFolder`/`AgLibraryFolder` prima e dopo. Serve a capire esattamente cosa scrive Lightroom e a decidere l'opzione C.
4. Verificare `AgLibraryFile.originalFilename` dopo una rinomina dentro Lightroom.
