# NeoFinder (wfs-apps.de): ricerca per RawLine Space

Ricerca dell'11 novembre 2026, sulla versione 9.3.1 (29 settembre 2026). Fonti: manuale ufficiale (cdfinder.de/guide), storico versioni, negozio, forum ufficiale, MacUpdate, blog di Michael Tsai.

Legenda: **[V]** = verificato su fonte ufficiale o diretta · **[D]** = dedotto o non confermato (il manuale non lo dice).

---

## 1. Cos'è

- Catalogatore di dischi e DAM per macOS, di Norbert M. Doerner (Germania). Esiste dal 1995, prima si chiamava CDFinder. **[V]**
- Indicizza dischi interni ed esterni, NAS/SMB, schede, dischi ottici, LTO, Dropbox, Backblaze B2 e altri cloud. Si cerca e si sfoglia anche a disco scollegato. **[V]**
- Ha un'app iOS compagna che sfoglia e cerca nei cataloghi. Su Windows c'è abeMeda, di un altro sviluppatore, che usa lo stesso formato di catalogo. **[V]**
- Versioni recenti: 9.0 (14 ottobre 2025: nuovo motore di catalogazione, interfaccia rifatta, RED/NEV nativi), 9.1 (dicembre 2025), 9.2 (marzo 2026), 9.2.1 (marzo 2026), 9.3 (31 agosto 2026: foto simili, ingest, catalogazione foto più veloce del 25% circa) e 9.3.1 (settembre 2026: macOS 27, ultima versione per Catalina). **[V]**
- Le note della 9.3.1 dichiarano che il codice è scritto senza "AI". **[V]**

## 2. Funzioni e impostazioni nel dettaglio

### 2.1 Cosa salva nel catalogo
- **Un file per ogni volume o cartella catalogata** (`.neofinder` o `.neofinder7`), nella cartella "NeoFinder Database" in `~/Library/Application Support/NeoFinder/`. La cartella si può spostare dove si vuole. Ogni catalogo porta il nome del volume. **[V]**
- Salva nomi, date di creazione e modifica, dimensioni e struttura delle cartelle, più i metadati di foto, video e audio e le miniature. **[V]**
- **Le impostazioni di catalogazione si salvano dentro ogni catalogo.** Gli aggiornamenti le riusano anche se le preferenze globali cambiano. **[V]**
- Limiti dichiarati: fino a 4 miliardi di file per catalogo. C'è chi lavora con 23.000 o anche 57.000 file di catalogo. **[V]**

### 2.2 Impostazioni di catalogazione (Preferenze > Catalogazione) **[V]**
- **Preset:** "All Data" (raccoglie tutto, molto lento) e "Super Fast" (solo file e cartelle, niente metadati).
- **Miniature di foto e video:** la dimensione si sceglie, ma il manuale non indica i valori in pixel **[D: non trovati]**. La qualità JPEG è un'impostazione esperta, `ThumbnailQuality` (1–100, **predefinita 20**, quindi bassa per tenere piccoli i cataloghi). Per le foto usa prima la miniatura EXIF/XMP incorporata, se è grande abbastanza. Se la dimensione richiesta è maggiore, decodifica tutto il file, ed è molto più lento.
- **RAW:** usa il motore RAW di macOS. In opzione c'è LibRAW per tutti i formati (`catAlwaysUseLibRAW`), aggiornato nella 9.1.
- **Livelli di inclusione:** "All" è il valore predefinito. Con meno livelli le dimensioni delle cartelle non tornano.
- **Discover image sequences:** comprime in una voce sola le sequenze (DPX, EXR, TIF). Il manuale avverte i fotografi di tenerla spenta, perché si rischia di perdere foto.
- **Commenti del Finder, tag del Finder e OpenMeta:** si possono attivare o spegnere. Sono molto lenti su SMB, ExFAT e NTFS.
- **Generate FileCheck (slow):** checksum MD5 per ogni file. È spento per impostazione predefinita (vedi §4).
- **Archivi:** cataloga dentro DMG, ISO, sparseimage, ZIP, TAR/TGZ, RAR e sitx.
- **Ignora:** file invisibili, alias e symlink, contenuto dei pacchetti. Ci sono esclusioni per nome o suffisso (§3.10 del manuale).
- **Testo:** di default legge 256 caratteri (`numBytesForTextFiles`). Il testo PDF completo si legge solo su richiesta.
- **Numero di serie automatico** per i nuovi cataloghi, con prefisso e suffisso.
- **"Always confirm settings":** mostra le impostazioni a ogni nuovo catalogo.
- **Impostazioni esperte** da Terminale (`defaults write de.wfs-apps.neofinder …`), tra cui:
  - `verifyThumbnailsForUpdate`
  - `MovieStillFrame` (fotogramma al 20% della durata)
  - `crashGuardTimeout` (60 s per il processo che decodifica)
  - `tmpFolder`
  - `NoChangePlease` (vieta ogni modifica su disco)
  - `deleteFilesImmediately` (NO di default)
  - `alwaysWriteSidecarXMP` (NO di default)
  - `writeXMPintoRAW` (NO di default)
  - `copySidecarFiles` (SÌ di default)

### 2.3 Video **[V]**
- La miniatura viene dal fotogramma al 20% della durata, non dal primo (spesso nero).
- In opzione fa un "mini foglio provini" di 2×2 fotogrammi con il tempo. Dalla 9.0 c'è anche il foglio provini video per MKV, AVI, NEV e R3D.
- Metadati: risoluzione, durata, codec, audio (codec, canali, frequenza, lingua), sottotitoli, capitoli, timecode SMPTE, metadati ARRI e FPS di ripresa negli MXF, GPS dei MOV (e degli MP4 se si legge l'XMP interno).
- Formati nativi: MOV, MP4, Canon CRM, BRAW, R3D, NEV. Per MPEG, VOB, MXF e simili serve ffmpeg installato a parte.
- Si cerca per altezza (HD), codec, FPS e timecode.
- XAVC non è citato per nome. **[D: probabilmente va come MP4/MXF]**

### 2.4 Velocità e dimensione dei cataloghi
- Lo sviluppatore non pubblica cifre di velocità. Dice solo che la 9.0 ha un motore "più veloce e affidabile" e che la 9.3 cataloga le foto circa il 25% più in fretta. **[V]**
- Un utente su MacUpdate racconta di aver catalogato 16 milioni di file su un disco da 8 TB senza problemi. **[V, aneddoto]**
- Esempio del manuale: 21 cataloghi, 185.000 elementi, 16 TB di volumi → **circa 10 GB di catalogo, quasi tutto miniature**, e 33 MB di RAM per tenerli caricati. Sono circa 54 KB per elemento. **[V]**
- Proiezione per 40–100 TB di RAW (diciamo 2–5 milioni di file): con impostazioni simili verrebbero cataloghi da 100–270 GB. **[D: stima lineare]** È il punto da battere.
- Lentezze segnalate nel forum: volumi NTFS (pause lunghe, la CPU quasi ferma), aggiornamenti via SMB e commenti e tag del Finder via SMB, colpa del client SMB di Apple. **[V]**
- Consigli ufficiali:
  - catalogare per cartelle di primo livello (per esempio un catalogo per anno) invece di un catalogo per disco intero;
  - spegnere le opzioni che non servono e l'antivirus;
  - fare miniature piccole;
  - usare `LogMediaPaths` per scoprire quali file rallentano. **[V]**
- Con 7.000 cataloghi nella stessa cartella l'app rallentava, perché controlla periodicamente la cartella. Dividerli in 15 sottocartelle ha risolto. **[V]**

### 2.5 Aggiornamento quando si ricollega un disco
- **Riconoscimento del volume:** nome, dimensione e data di creazione, più un file nascosto `.neofinder.abemeda.volinfo.xml` scritto nella radice del disco con un ID univoco. **[V]**
  - Il problema: i cloni fatti con CCC o SuperDuper copiano anche quel file e confondono l'app. Bisogna cancellarlo o escluderlo dal clone.
  - Il file si può disattivare con `noDeviceIDFile`. **[V]**
- **Update Catalog:** manuale, anche su più cataloghi in parallelo. Se il disco è offline chiede di collegarlo. **[V]**
- **QuickUpdate** (attivo di default): tiene metadati e miniature dei file non modificati. Il criterio di "modificato" non è documentato. **[D: con ogni probabilità data di modifica e dimensione]**
- Un aggiornamento conserva nome e commento del catalogo, commenti ed etichette sugli elementi e le miniature già fatte. Rilegge icona, spazio libero e statistiche. **[V]**
- **AutoUpdater** (solo con licenza Business): aggiorna all'avvio, "On mount" (quando si collega il volume, se l'app è aperta), a orario o ogni 1–12 ore, nei giorni scelti. Può smontare il volume a fine aggiornamento, eseguire gli aggiornamenti in parallelo o in coda e tiene un registro. Non sveglia il Mac. **[V]**
- La catalogazione automatica quando si monta un disco nuovo non esiste più, per i limiti di sicurezza di macOS. Al suo posto c'è un'app di appoggio, "Update and Eject": ci si trascina sopra il disco e lei cataloga o aggiorna, poi espelle. **[V]**
- **Reconnect Catalog:** se i dati sono stati spostati, si indica il nuovo percorso. **[V]**
- 9.2: se un volume sparisce durante la catalogazione, l'aggiornamento si annulla e l'app lo segnala, invece di fallire senza dire niente. **[V]** È un buon segnale, ma vuol dire che prima falliva in silenzio.
- 9.3: corretto un errore per cui la catalogazione ExFAT poteva fallire in silenzio su alcune versioni di macOS. **[V]**

### 2.6 Ricerca e filtri **[V]**
- **QuickFind:** campo di ricerca veloce, anche dalla barra dei menu.
- **Find Editor:** fino a 16 criteri, in modalità E oppure O. L'ambito può essere tutti i cataloghi, alcuni scelti o quelli con una certa etichetta.
  - Campi: nome, commento, dimensione, durata, percorso, date, risoluzione, parole chiave, "Any Text" (comprende EXIF e IPTC).
  - Su EXIF, IPTC, ID3 e XMP ci sono "vuoto/non vuoto", `==`, `!=` e `!!`.
  - Le espressioni regolari funzionano su alcuni campi.
- Le **Smart Folder** sono ricerche salvate, anche con date relative ("ultimi 21 giorni").
- **Display Filter:** filtra la vista corrente per campo, anche per campi vuoti o non vuoti.
- Altre integrazioni: URL di ricerca, Spotlight, menu Servizi, FileMaker e Alfred.
- La ricerca funziona sui cataloghi offline: è lo scopo dell'app. Il manuale non dà cifre di velocità.

### 2.7 Mappa GPS **[V]**
- La mappa è quella di Apple (MapKit), con vista satellite e punti d'interesse. Le versioni 7.x usavano OpenStreetMap.
- Selezionando i file compaiono i loro pin. Dalla 9.2.1 i pin mostrano la miniatura e si possono vedere più pin insieme.
- Si trascina un pin per correggere la posizione (l'app scrive il file e il catalogo) e si possono geotaggare i file che non hanno coordinate.
- **GeoFinder** cerca nei cataloghi gli elementi geotaggati dentro il rettangolo visibile della mappa.
- Legge anche altitudine, direzione e inclinazione.
- Esporta in KMZ.
- Il nome del luogo si ottiene online da OpenStreetMap (e dal server GeoNames per la ricerca dei luoghi). Poi si può applicare a tutte le foto entro un raggio in metri.
- Offline: le tessere di MapKit già in cache si vedono, ma senza rete la mappa è limitata, e la ricerca dei luoghi e la geocodifica non funzionano. **[D]**

### 2.8 Duplicati **[V]**
- Criteri: nome (anche senza estensione, così `.NEF` e `.JPG` con lo stesso nome risultano uguali), checksum FileCheck MD5 o ISRC per l'audio.
- Si può chiedere che coincidano anche dimensione, data di creazione e data di modifica. Si filtra per tipo (foto, video, tutto) e per dimensione minima.
- Ambito: tutti i cataloghi, alcuni scelti o quelli con un'etichetta. Si confrontano dischi diversi, anche offline.
- Opzione "file unici": trova i file che esistono una volta sola, cioè senza copia di sicurezza.
- I duplicati di cartella si confrontano solo per nome più le opzioni scelte.
- Dalla 9.0 mostra quante copie ha ogni risultato.
- **Non c'è un comando "elimina duplicati".** Si possono selezionare e farne un Album. Per cancellarli si usa il cancella normale (§4).

### 2.9 Tag, etichette, metadati **[V]**
- 15 etichette colorate rinominabili: le prime 7 corrispondono a quelle del Finder. Si mettono su cataloghi ed elementi.
- Stelle, parole chiave e parole chiave gerarchiche, persone, Album, annotazioni personalizzate e cinque campi extra per ogni catalogo.
- **QuickTags e QuickPerson** (9.0): pannelli per aggiungere parole chiave o persone con un clic.
- **Editor XMP** con preset (dalla 9.2 importa anche i preset Adobe) e sostituzioni di testo.
- Scrittura XMP: il default per formato non è documentato. Esistono `alwaysWriteSidecarXMP` e `writeXMPintoRAW` (entrambi NO di default). La 9.0 scrive l'XMP dentro gli ARW, ORF e RW2. **[V]**
- La 9.3 ha corretto un errore per cui i sidecar XMP non seguivano i file spostati nei cataloghi. **[V]**
- **AutoTags:** parole chiave automatiche generate da "engine" da scaricare.
- **Image Analysis:** analisi in background con il risultato salvato nel catalogo.
- **Find Similar Photos** (9.3): su macOS 14 e successivi usa una rete neurale (Vision) sul soggetto della foto, gira sul Mac e tiene i risultati in cache.
- **Find Faces** c'è, ma non ho approfondito come funziona.
- Gli engine AutoTags si scaricano. Non ho verificato se poi girano tutti in locale. **[D]**

### 2.10 Condivisione dei cataloghi **[V]**
- La cartella del database si mette su un NAS o un server, ma per condividerla serve la licenza Business su ogni Mac.
- **Non c'è un sistema di lock documentato.** Il manuale consiglia uno o pochi amministratori che scrivono e gli altri in sola lettura, impostata dai permessi del server. Avverte che due istanze che modificano lo stesso catalogo insieme danno "risultati inattesi".
- "Keep looking for changes" ricarica i cataloghi modificati da altri.
- Gli alias di cataloghi e cartelle permettono di unire cataloghi privati e condivisi.
- Su iOS i cataloghi si sfogliano.
- Si esportano i segnalibri (9.3) e i cataloghi (§10 del manuale), e c'è AppleScript.
- Etichette con codice a barre 2D da stampare per i dischi fisici: si scansionano con l'app iOS e si apre il catalogo del disco.

### 2.11 Altro **[V]**
- Light Table, presentazione, conversione video e audio, rotazione JPEG senza perdita, modifica della data EXIF, watermark, esportazione foto.
- Image Capture (import da fotocamera in cartelle per data, con ID unico e rinomina) e, dalla 9.3, "Ingest Media Folders" (copia, rinomina, metadati, catalogazione).
- Importa i cataloghi di circa 25 altri programmi (iView, WinCatalog, ProMax LTO, …).

## 3. Interfaccia e flusso

- Finestra unica stile Finder **[V]**:
  - a sinistra LIBRARY, con cataloghi, cartelle di cataloghi, Album e Smart Folder;
  - al centro la vista (lista, icone, colonne);
  - a destra l'Inspector, con metadati, editor XMP e mappa.
- **Fill bar:** barra di riempimento per catalogo, per vedere cosa c'è dentro. **[V]**
- Gli elementi offline restano consultabili: QuickLook mostra la miniatura salvata nel catalogo (9.0). **[V]**
- Flusso tipico **[V]**:
  1. collegare il disco e catalogarlo una volta;
  2. ricollegarlo e fare "Update" (o lasciarlo all'AutoUpdater);
  3. cercare con QuickFind o il Find Editor;
  4. "Reveal in Finder" o AutoMount, che monta il volume di rete se serve;
  5. se il disco è offline, l'app chiede di collegarlo.
- Impressione generale: interfaccia densa, molto "anni 2000 aggiornata", con centinaia di opzioni sparse tra preferenze, menu Special, menu contestuali e impostazioni da Terminale. **[D, dalle schermate e dalla struttura del manuale]** Su MacUpdate compaiono le voci "Design", "Stability" e "Value" tra i punti da migliorare. **[V]**

## 4. Sicurezza dei file

- **Checksum FileCheck:** MD5, spento di default. Rilegge ogni file per intero, quindi è lento. Si verifica dal menu contestuale (un catalogo, un file o una selezione) e una finestra elenca i file che non tornano. **[V]**
  - Non c'è SHA-256 né xxHash.
  - Non risulta un rapporto esportabile né una verifica programmata. **[D]**
  - Non è chiaro come aggiorna il checksum quando un file cambia legittimamente. **[D]**
- **Spostare:** si trascina un file su una cartella dello stesso catalogo. Sposta l'originale su disco e aggiorna il catalogo. Funziona **solo con i file, non con le cartelle**, e solo dentro lo stesso catalogo. **[V]**
- **Rinominare:** c'è la casella "Also rename on volume", che compare solo se il disco è online e ci sono i permessi. **[V]**
  - Il Multi Renamer ha variabili, anteprima del primo file, avviso giallo se due nomi coincidono e annulla.
  - Rinomina prima il file su disco e poi aggiorna il database.
- **Cancellare:** chiede conferma e manda nel Cestino. Sui NAS senza `.Trash` macOS chiede conferma file per file. `deleteFilesImmediately` (NO di default) salta il Cestino. **[V]**
- **Sidecar:** `copySidecarFiles` (SÌ di default). Fino alla 9.3 c'era un errore per cui i sidecar non seguivano i file spostati. **[V]**
- **Blocco totale:** `NoChangePlease` impedisce qualunque modifica su disco. **[V]**
- Annulla documentato per Multi Renamer, rimozione di parole chiave e Album. Per lo spostamento non risulta. **[V/D]**
- Rimuovere un elemento dal catalogo è diverso dal cancellare il file. Un Update lo fa ricomparire. **[V]**
- Il file nascosto di ID scritto su ogni disco è una modifica al disco, anche se piccola, e crea problemi con i cloni. **[V]**
- **Rete:** l'app contatta Sparkle per gli aggiornamenti, Apple Maps, GeoNames, OpenStreetMap, MusicBrainz, Cover Art Archive, Dropbox e B2. Ogni connessione dichiara il motivo a Little Snitch. Il manuale non dice se l'attivazione della licenza richiede la rete. **[V/D]**

## 5. Prezzo, piattaforme, limiti, critiche

- **Prezzo:**
  - licenza Private 39,99 $ una tantum, per un massimo di 3 Mac personali **[V]**;
  - aggiornamento dalla 6.x–8.x a 25,99 $ **[V]**;
  - cross-grade da prodotti concorrenti (Excire, PhotoSweeper, DiskTracker, Media Pro, …) a 25 $ **[V]**;
  - licenze Business da 2 a 50 utenti e Site: prezzi non trovati **[D]**.
  - Non è un abbonamento. La 9.x vale fino alla 10.0, attesa "forse a fine 2029". Niente rimborsi. **[V]**
- **Versione gratuita:** demo completa ma con **massimo 10 cataloghi** e nessun limite di tempo. Wikipedia, ferma alla 7.7, parlava di 25. **[V]**
- **Licenza Business obbligatoria** per AutoUpdater, database condiviso e alias di cataloghi e cartelle. **[V]**
- **Piattaforme:** macOS 10.15 o successivo (la 9.3.1 è l'ultima per Catalina), Apple Silicon e Intel. App iOS per sfogliare. Windows tramite abeMeda. **[V]**
- **Limiti e critiche:**
  - Niente catalogazione automatica quando si collega un disco nuovo. L'"On mount" funziona solo per i cataloghi già esistenti, solo con licenza Business e solo ad app aperta. **[V]**
  - Molto lento su ExFAT, NTFS e SMB (commenti e tag del Finder, NTFS con pause lunghe). **[V]**
  - Cataloghi pesanti per via delle miniature (circa 54 KB per elemento nell'esempio ufficiale). **[V]**
  - Il checksum è solo MD5 ed è lento. Nessuna catena di verifica tra copie. **[V]**
  - Spostamento solo per file, solo dentro lo stesso catalogo. **[V]**
  - Errori in silenzio corretti di recente (volume che sparisce, ExFAT, sidecar che non seguivano gli spostamenti, "elementi fantasma" nelle Smart Folder). Segno di un'app potente ma dove i casi limite sui dati veri sono capitati. **[V]**
  - L'updater integrato era rotto su macOS 15 e 26 (nella 9.2 bisognava aggiornare a mano). **[V]**
  - Le impostazioni importanti stanno nascoste in `defaults write`. **[V]**
  - Critiche pubbliche scritte: poche. MacUpdate dà 4,2/5 (78 voti) e lodi a stabilità, supporto e documentazione da utenti di lunga data. **[V]**

## 6. Idee da prendere per RawLine Space (concrete)

1. **Un catalogo per volume, in un file a sé**, con le impostazioni di catalogazione dentro il catalogo. Si fa il backup e si sposta un disco alla volta, e gli aggiornamenti restano coerenti. In RawLine Space: un pacchetto per disco (SQLite più cartella di miniature) e un indice globale ricostruibile.
2. **Riconoscere il volume con più segnali** (UUID del volume, dimensione, data di creazione, nome), ma **senza scrivere file sul disco**. Per i cloni: avvisare quando due dischi hanno la stessa impronta e chiedere quale è quale.
3. **QuickUpdate:** al ricollegamento rileggere solo i file con dimensione o data di modifica cambiata (più l'inode o il file ID di APFS per riconoscere i file spostati). Le miniature e i metadati dei file invariati restano.
4. **Usare prima l'anteprima JPEG incorporata nel RAW**, e decodificare solo se è troppo piccola. È già la logica di "decodifica leggera" di Selects. Miniature in HEIC o JPEG a qualità controllata, con due tagli (piccola per la griglia, grande per l'anteprima offline).
5. **Preset di catalogazione chiari** ("Veloce: solo file", "Foto: miniature + EXIF/XMP/GPS", "Completo + checksum"), con la stima del tempo e dello spazio del catalogo prima di partire.
6. **"File unici" (senza copia)** come funzione di primo piano: per chi ha 40–100 TB è la domanda vera ("cosa ho in una sola copia?"). Il confronto tra dischi usa il checksum, con nome più dimensione più data come prima scrematura.
7. **Duplicati RAW+JPEG con lo stesso nome base** (ignorare l'estensione) e raggruppamento RAW+XMP+JPEG come un'unica "foto".
8. **Mini foglio provini 2×2 per i video**, con il fotogramma al 20% invece del primo. Timecode, codec e FPS ricercabili.
9. **Ricerca con criteri E/O, "vuoto/non vuoto", Smart Folder con date relative** e ambito per etichetta o per gruppo di dischi. Più un filtro rapido sulla vista.
10. **Ricerca per area visibile della mappa** e applicazione del luogo a tutte le foto in un raggio. In RawLine Space va fatta tutta offline: niente geocodifica online, ma un database di località locale (per esempio GeoNames scaricato una volta dentro l'app) e tessere locali o una mappa vettoriale semplice.
11. **Fill bar** per disco (quanto c'è di RAW, video, export, XMP) e **stato del catalogo** (data dell'ultimo aggiornamento, presenza dei checksum, spazio libero del disco).
12. **Etichetta stampabile con QR o codice per ogni disco** che apre il catalogo. Utilissima con 20–40 dischi su uno scaffale.
13. **Segnalare se un disco sparisce a metà** e non salvare mai un catalogo parziale come se fosse completo (lezione della 9.2).
14. **Interruttore globale "sola lettura"** (come `NoChangePlease`), ma visibile nell'interfaccia e attivo di default all'inizio.
15. **Similarità per soggetto con Vision in locale e risultati in cache**, calcolati in background. È compatibile con la regola offline.
16. **Importare i cataloghi NeoFinder o le loro esportazioni** come via d'ingresso per chi passa a RawLine Space (da valutare: il formato non è documentato).

## 7. Cose da NON copiare

- **File nascosto di ID scritto su ogni disco:** modifica i dischi d'archivio e confonde i cloni.
- **MD5 opzionale e lento come unica integrità.** Meglio xxHash3 o BLAKE3 per la velocità e SHA-256 per l'interoperabilità, calcolati durante la copia o la prima catalogazione. Servono anche la verifica programmata, il rapporto esportabile e lo storico "verificato il…".
- **Spostamento senza annulla, solo di file, solo dentro lo stesso catalogo.** RawLine Space deve avere un piano mostrato prima, copia → verifica → cancellazione dell'originale, cartelle comprese, sidecar sempre insieme e un registro per annullare.
- **Impostazioni critiche nascoste in `defaults write`** (qualità delle miniature, cancellazione immediata, scrittura XMP nei RAW). Niente opzioni pericolose nascoste.
- **Funzioni base dietro la licenza Business** (aggiornamento al collegamento, alias): per un fotografo da solo sono indispensabili.
- **Catalogazione automatica assente per i dischi nuovi.** RawLine Space deve proporre "Catalogare questo disco?" quando si collega, con un clic e senza app di appoggio.
- **Geocodifica e ricerca dei luoghi online:** non rispettano la regola offline.
- **Un'interfaccia con centinaia di opzioni** tra menu Special, preferenze e Terminale. Meglio pochi preset più un pannello avanzato.
- **Cataloghi enormi per miniature non ottimizzate.** Va misurato e mostrato quanto pesa un catalogo per TB.
- **Errori in silenzio** (ExFAT, volume scollegato, sidecar): ogni scansione deve finire con un riepilogo (file letti, saltati, errori).
- **Mancanza di lock sul database condiviso.** Se si condivide, serve un lock o almeno la sola lettura esplicita.

## 8. Fonti (link)

- Sito e panoramica: https://www.cdfinder.de/
- Storico versioni: https://www.cdfinder.de/versions.html
- Negozio e licenze: https://www.cdfinder.de/store.html
- Manuale: https://www.cdfinder.de/guide/
- Catalogazione: https://www.cdfinder.de/guide/3/cataloging.html
- Impostazioni di catalogazione: https://www.cdfinder.de/guide/3/3.3/cataloging_settings.html
- Catalogazione all'espulsione (Update and Eject): https://www.cdfinder.de/guide/3/3.4/catalog_and_eject.html
- Aggiornamento dei cataloghi: https://www.cdfinder.de/guide/3/3.5/updating.html
- AutoMount: https://www.cdfinder.de/guide/3/3.8/automount.html
- AutoUpdater: https://www.cdfinder.de/guide/3/3.9/auto-updater.html
- Dischi clonati e ID del volume: https://www.cdfinder.de/guide/3/3.11/catalog-cloned-disks.html
- Etichette con codice a barre: https://www.cdfinder.de/guide/3/3.18/Securely_store_media.html
- Organizzazione: https://www.cdfinder.de/guide/4/organizing.html
- Backup del database: https://www.cdfinder.de/guide/4/4.5/neofinder_backup.html
- Rimuovere elementi dal catalogo: https://www.cdfinder.de/guide/4/4.12/delete_catalog_items.html
- Reconnect Catalog: https://www.cdfinder.de/guide/4/4.14/reconnect.html
- Ricerca: https://www.cdfinder.de/guide/5/find.html
- Find Editor: https://www.cdfinder.de/guide/5/5.2/findeditor.html
- Duplicati: https://www.cdfinder.de/guide/5/5.3/find_duplicates.html
- Foto simili: https://www.cdfinder.de/guide/5/5.8/find_similar_photos.html
- Spostare, rinominare e cancellare: https://www.cdfinder.de/guide/8/8.6/file_workflow.html
- Multi Renamer: https://www.cdfinder.de/guide/8/8.14/multi_rename.html
- Prestazioni: https://www.cdfinder.de/guide/11/performance.html
- Catalogazione più veloce: https://www.cdfinder.de/guide/11/11.1/faster-cataloging.html
- Foto: https://www.cdfinder.de/guide/17/neofinder_and_photos.html
- XMP, EXIF, IPTC: https://www.cdfinder.de/guide/17/17.2/neofinder_xmp.html
- FileCheck: https://www.cdfinder.de/guide/19/filecheck.html
- Geotagging: https://www.cdfinder.de/guide/20/neofinder_geotagging.html
- Mappa e GeoFinder: https://www.cdfinder.de/guide/20/20.1/neofinder_map_geofinder.html
- Nome del luogo dal GPS: https://www.cdfinder.de/guide/20/20.5/gps_place_name.html
- Video: https://www.cdfinder.de/guide/22/neofinder_and_videos.html
- Impostazioni esperte: https://www.cdfinder.de/guide/24/neofinder_hidden_prefs.html
- FAQ: https://cdfinder.de/guide/25/faq.html
- Sicurezza e rete: https://www.cdfinder.de/guide/26/security.html
- AutoTags: https://www.cdfinder.de/guide/30/auto_keywords.html
- Più utenti con server o NAS: https://www.cdfinder.de/guide/2/2.2/neofinder_server.html
- Forum, NTFS lento: https://neofinder.de/forum/phpBB3/viewtopic.php?p=185
- Forum, aggiornamenti via rete: https://www.neofinder.de/forum/phpBB3/viewtopic.php?p=787
- Forum, cataloghi privati e condivisi: https://www.neofinder.de/forum/phpBB3/viewtopic.php?p=645
- Michael Tsai su NeoFinder 9.0 (prezzi): https://mjtsai.com/blog/2025/10/30/neofinder-9-0/
- MacUpdate (voti e recensioni): https://neofinder.macupdate.com/
- Wikipedia (storia): https://en.wikipedia.org/wiki/NeoFinder
- Concorrente economico citato da PetaPixel (Offline Files, 7,99 $): https://petapixel.com/2026/02/27/this-mac-app-lets-you-find-photos-no-matter-which-drive-theyre-on
