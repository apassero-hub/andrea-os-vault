# Criticità: cercatori di doppioni e app di pulizia

Ricerca dell'11 novembre 2026 per RawLine Space. Tema: incidenti, lamentele e paure reali di chi usa cercatori di doppioni (PhotoSweeper, Gemini 2, Czkawka, dupeGuru, Teekesselchen, Duplicate Finder, CleanMyMac, DaisyDisk, Apple Foto, Mylio, Lightroom Classic 15.4, Excire, Peakto) e di chi libera spazio cancellando RAW.

Come leggere: ogni criticità ha **casi**, **causa**, **come evitarla** e una riga di **conferma** (quante fonti indipendenti, quanto recenti). Le citazioni sono brevi e tradotte o riportate tali e quali.

Limiti: il budget di ricerca web si è esaurito prima di coprire Reddit in modo diretto (nessun thread r/DataHoarder o r/photography emerso dai risultati) e prima di cercare lamentele specifiche su Easy Duplicate Finder e Nektony (si trovano solo recensioni del produttore o di affiliati). Excire e Peakto qui hanno solo limiti generici: per il dettaglio c'è già `../Peakto ed Excire.md`.

---

## 1. Criticità in ordine di gravità

### 1.1 Cancellare "il doppione" cancella tutte le copie (strumento sbagliato o bug)

- **Lightroom Classic 15.4, giugno 2026.** Nella nuova vista Duplicati, "Delete Rejected Photos" ha cancellato dal disco e dal catalogo *tutte* le foto del gruppo, non solo quelle scartate: circa 60 foto perse. Adobe ha consigliato di non usare la funzione e tre giorni dopo è uscita la 15.4.1 con "critical bug fixes", senza dire se il bug fosse tra quelli ([Adobe, bug report](https://community.adobe.com/bug-reports-674/p-delete-rejected-photos-in-duplicates-view-deletes-all-copies-1628661)). Chi ha segnalato il bug nota che la finestra di conferma mostrava il numero totale, che forse non era quello visto all'inizio.
- **Lightroom, 2020.** Un utente cancella una delle due copie e spariscono entrambe: la seconda era una copia virtuale, che non esiste sul disco ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/deleted-one-photo-two-were-gone/td-p/11040289)). Lo stesso succede con due importazioni dello stesso file: cancellarne una toglie il file e le lascia entrambe "mancanti" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/lr-folder-contains-duplicate-raw-files/m-p/10210296/highlight/true)).
- **Esempio da un altro campo (musica, SongKong, 2020).** Il confronto fatto solo sui metadati ha fatto cancellare originale *e* doppione in metà dei casi controllati. Lo sviluppatore ha riconosciuto il bug, l'ha corretto e ha aggiunto al rapporto anche i file tenuti ([jthink](https://community.jthink.net/t/delete-duplicates-deletes-original/8617)).
- **Causa.** Nessuno controlla che resti almeno una copia vera e leggibile del gruppo. Si scambia una "voce di catalogo" per un file, e la conferma non dice con precisione cosa sparisce.
- **Come evitarla.** Prima di ogni azione va verificato che, per ogni gruppo, almeno una copia resti fuori dall'azione, esista sul disco e corrisponda per hash. Se manca, l'azione si blocca. La conferma deve elencare per nome cosa sparisce e cosa resta. Copie virtuali e voci di catalogo vanno distinte dai file.
- **Conferma.** Quattro fonti indipendenti; il caso più grave è di giugno 2026. **Alta.**

### 1.2 Cancellazione definitiva o "il Cestino non c'è"

- **DaisyDisk** cancella per scelta definitivamente, senza passare dal Cestino, con 5 secondi per annullare. Il suo manuale vecchio dice che l'unica speranza è un software di recupero ([DaisyDisk](https://daisydiskapp.com/guide/deleting-files)).
- **Czkawka (CLI), 2020.** `dup -d` cancellava senza chiedere né scrivere nulla. Segnalato come "EXTREMELY DANGEROUS"; nel 2021 è arrivato un dry-run, nel 2023 non cancellare era diventato il comportamento normale, chiusa nel 2024 ([GitHub #46](https://github.com/qarmin/czkawka/issues/46)).
- **Mylio**: "Delete Marked" cancella da tutti i dispositivi e "cannot be undone"; l'alternativa "Move Marked" sposta fuori dalla libreria ([manuale Mylio](https://manual.mylio.com/topic/removing-vs-deleting-duplicate-images)).
- **Dischi esterni exFAT**: macOS può saltare il Cestino ([risultato di ricerca, forum](https://yomotherboard.com/question/how-can-i-get-deleted-files-on-my-external-drive-to-go-to-trash-instead-of-being-permanently-deleted/)). Su Windows anche i file più grandi del Cestino lo saltano ([MiniTool](https://www.minitool.com/data-recovery/files-deleted-from-external-hard-drive-are-not-in-recycle-bin.html)).
- **Lightroom, 2026.** 12.000 file su 47.000 sono finiti nel Cestino per sbaglio (catalogo sbagliato aperto). "Rimetti a posto" del Finder non funziona perché a spostare i file è stata l'app, non il Finder, quindi vanno rimessi a mano nelle cartelle datate ([Adobe](https://community.adobe.com/questions-675/accidentally-deleted-the-whole-library-stopped-before-completion-12k-of-47k-photos-in-trash-folder-1628969)).
- **Causa.** "Liberare spazio subito" è in conflitto con "poter tornare indietro". Il Cestino da solo non basta: non sa ricostruire le cartelle, non regge 40–100 TB e su exFAT o in rete può mancare del tutto.
- **Come evitarla.** Usare una quarantena di RawLine Space sullo stesso volume che mantiene percorsi e giornale (la regola di Space: mai cancellare subito). Il ripristino deve rimettere ogni file al suo percorso. Lo spazio si recupera davvero solo con un secondo passo esplicito, dopo giorni. I volumi exFAT e di rete vanno riconosciuti e trattati a parte.
- **Conferma.** Cinque fonti, dal 2020 al 2026. **Alta.**

### 1.3 Falsi doppioni: file diversi giudicati uguali

- **Stesso nome e stessa dimensione.** In Shotwell, tre Sony A55 producevano file con nomi e dimensioni identici, e foto mai importate venivano saltate come doppioni. Bug "major": formattando la scheda si perdevano. Corretto aggiungendo l'ora di scatto ([GNOME](https://gitlab.gnome.org/GNOME/shotwell/-/issues/4791)). Il contatore delle fotocamere torna a 0001 quando cambia la scheda o la cartella ([Photography Life](https://photographylife.com/avoiding-duplicate-file-names)).
- **Ora di scatto al secondo.** Teekesselchen confronta l'ora di scatto EXIF, precisa solo al secondo, quindi le raffiche diventano "doppioni". Rimedio: l'opzione ExifTool ([Lightroom Queen](https://www.lightroomqueen.com/clean-duplicate-photos/), [Have Camera Will Travel](https://havecamerawilltravel.com/lightroom/find-duplicate-photos/)). Su circa 50.000 foto un utente ha trovato "decine" di falsi doppioni e decine di doppioni mancati ([Lightroom Queen forum](https://www.lightroomqueen.com/community/goto/post?id=1214638)).
- **Somiglianza visiva.** La modalità foto di dupeGuru divide l'immagine in una griglia 15×15 di colori medi. Un utente ha avuto falsi abbinamenti anche al 96–99% ([AlternativeTo](https://alternativeto.net/software/dupeguru/about)). La cartella "Duplicati" di Apple Foto mostra anche foto solo simili ([Apple Community](https://discussions.apple.com/docs/DOC-250001956)). Per togliere una coppia senza unirla bisogna modificare leggermente una delle due ([Apple Community](https://discussions.apple.com/thread/254985972)).
- **Causa.** Si confondono "uguale" e "simile", o si usano criteri deboli (nome, dimensione, ora al secondo).
- **Come evitarla.** Un file si considera doppione da liberare **solo se è identico byte per byte** (hash completo dopo un primo filtro per dimensione). I "simili" vanno in un'altra sezione: si possono solo guardare e non hanno mai un'azione automatica. Il nome del file non è mai una prova.
- **Conferma.** Sei fonti, dal 2016 al 2023 e ancora valide. **Alta.**

### 1.4 La regola automatica tiene la copia sbagliata

- **PhotoSweeper (recensione App Store, 2018).** Ha marcato da cancellare la copia integra e tenuto l'originale parzialmente corrotto. Ha tenuto "filename (1)" e "(2)" invece dell'originale. Le regole sono "buried in the Preferences" e ogni modifica richiede una nuova scansione ([App Store](https://apps.apple.com/au/app/photosweeper/id463362050?mt=12)).
- **Teekesselchen (2021).** Ha scartato i JPG invece degli HEIC che l'utente voleva tenere; l'impostazione "preferisci il file più grande" non cambiava nulla ([Lightroom Queen](https://www.lightroomqueen.com/community/threads/teekesselchen-duplicate-reject-flag-jpg-not-heic.42104/)).
- **Apple Foto.** Utenti segnalano che la copia tenuta ha il nome o lo stato di modifica sbagliato e che i titoli delle copie tolte vanno persi ([Apple Community](https://discussions.apple.com/thread/256021424)). Apple tiene "la foto con più metadati" ma non unisce metadati diversi ([Apple Community](https://discussions.apple.com/thread/254424603)).
- **Gemini 2 (2020).** Proponeva di tenere la copia "in un album" senza spiegare perché ([Apple Community](https://discussions.apple.com/thread/251952346)).
- **Lightroom.** Una copia può avere le modifiche di sviluppo e l'altra i metadati ([Lightroom Queen](https://www.lightroomqueen.com/clean-duplicate-photos/)). Gli strumenti esterni al catalogo non sanno quale copia è stata modificata.
- **Causa.** Le regole sono opache e il "migliore" si sceglie con criteri estetici o arbitrari (nome più corto, dimensione, ordine di scansione: dupeGuru considera originale il primo file trovato ([Cisdem](https://www.cisdem.com/resource/dupeguru-for-mac-review-and-alternative.html))). Nessuno controlla l'integrità del file né i legami con cataloghi e progetti.
- **Come evitarla.** Ogni scelta "tieni questa" va motivata in una riga leggibile (per esempio "è nella cartella cliente, è collegata al catalogo X, si apre senza errori"). L'ordine delle priorità deve essere visibile nella stessa schermata, non nelle Preferenze. Le copie con nome tipo "(1)", "copia" o "-2" vanno trattate per quello che sono. Prima di scegliere si controlla che il file da tenere si decodifichi. Se le copie differiscono per modifiche o metadati, non si sceglie in automatico.
- **Conferma.** Cinque fonti indipendenti, dal 2018 al 2025. **Alta.**

### 1.5 Il catalogo o il progetto puntavano proprio al file cancellato

- I consigli sono costanti: i cercatori di doppioni esterni al catalogo "can damage catalogs", e cancellare dal sistema lascia le foto "missing" in Lightroom ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/deleted-one-photo-two-were-gone/td-p/11040289), [Lightroom Queen](https://www.lightroomqueen.com/clean-duplicate-photos/)).
- Il caso tipico: doppia importazione, la copia modificata risulta mancante, quella senza modifiche è presente. Il rimedio è togliere dal catalogo (non dal disco) quella senza modifiche e ricollegare l'altra ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/file-associated-with-another-photo-in-catalog-error/td-p/13665737)).
- Una volta cancellate dal catalogo le voci, le modifiche si perdono anche se i file si recuperano ([Wondershare, riassunto di thread](https://recoverit.wondershare.com/faq/lightroom-delete-from-disk-raw-photos.html)).
- **Mylio** chiama "Lost Originals" i file cancellati fuori dall'app prima della sincronizzazione ([manuale Mylio](https://manual.mylio.com/topic/handling-lost-originals)).
- **CleanMyMac 2–3 (2018).** Secondo un'esperta della community le prime versioni avevano rimosso i master originali delle foto modificate nella libreria Foto, rompendo le coppie master–versione. Il problema si è risolto facendo ricostruire le anteprime ([Apple Community](https://discussions.apple.com/thread/8411740)).
- **Video.** I proxy non sostituiscono gli originali in esportazione ([Blitzcut](https://blitzcutai.com/blog/video-proxies)): cancellare "il doppione grande" di un progetto con proxy significa non poter più finire il lavoro.
- **Causa.** Il file system non sa chi usa un file. Cataloghi (Lightroom, Capture One, Foto, Mylio) e progetti (Final Cut, Premiere, Resolve) tengono legami che l'app di pulizia non vede.
- **Come evitarla.** Prima di proporre qualcosa, leggere in sola lettura cataloghi e progetti trovati sul volume e marcare "in uso" ogni file referenziato. Un file in uso non si propone mai in automatico; se l'utente lo vuole, deve sapere da quale catalogo è usato. Se si trova un catalogo che non si riesce a leggere, la cartella si blocca.
- **Conferma.** Sei fonti dal 2018 al 2026 (per il video una sola fonte sui proxy). **Alta.**

### 1.6 Sidecar XMP, coppie RAW+JPEG e file di contorno

- **Bridge 16.0.5, luglio 2026.** Cancellare `myFile.jpg` cancellava anche `myFile.xmp` del RAW, con tutte le modifiche. Riprodotto "100%" su due Mac, sparito con un aggiornamento automatico ([Adobe](https://community.adobe.com/bug-reports-557/bridge-deletes-the-sidecar-xmp-file-associated-with-a-raw-file-when-a-another-file-with-similar-name-but-different-type-is-deleted-1632752)).
- Recuperare i RAW dal Cestino senza i loro XMP ha fatto perdere "hours of lost work" ([Adobe](https://community.adobe.com/questions-675/sidecar-file-not-being-read-after-restoring-accidentally-deleted-files-981656)).
- Un cercatore di doppioni non può abbinare i sidecar perché hanno un'altra estensione ([photo-sidecar-cleaner](https://github.imc.re/sisyphosloughs/photo-sidecar-cleaner)).
- **Apple Foto** tratta RAW+JPEG come un'unica foto: "Delete the image, and both files are thrown away". Non c'è un comando "cancella solo il RAW", richiesto da anni ([Six Colors, 2026](https://sixcolors.com/post/2026/02/photos-wont-let-you-remove-the-raw-photo-from-a-rawjpeg-pair/)). **Shotwell** ha avuto il bug opposto: cancellava il JPEG della coppia quando non doveva ([GNOME](https://gitlab.gnome.org/GNOME/shotwell/-/issues/2871)).
- Camera Raw salva le maschere AI in file `.acr` separati, che restano orfani dopo una rinomina ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/p-information-on-acr-files/m-p/15191219)).
- **Causa.** I file si trattano uno per uno invece che come gruppi (RAW + XMP + .acr + JPEG gemello + .THM/.LRV del video).
- **Come evitarla.** L'unità di lavoro è il **gruppo di file dello stesso scatto**: si sposta, si mette in quarantena e si ripristina tutto insieme. RAW e JPEG gemelli non sono mai doppioni tra loro (contenuto diverso), sono una coppia. Se va tolto solo uno dei due, lo decide l'utente, e il gruppo dice sempre cosa resta.
- **Conferma.** Sei fonti, quattro del 2026. **Alta.**

### 1.7 "Cancellato" ma lo spazio non torna (o i file non spariscono)

- **Gemini 2.** Ha detto di aver messo i doppioni nel Cestino, ma il Cestino era vuoto ([MacRumors](https://forums.macrumors.com/threads/please-can-you-help-with-a-gemini2-problem.2434334), pagina non apribile, visto solo nel riassunto della ricerca). Un altro utente: "the photos never really go away" ([Apple Community](https://discussions.apple.com/thread/251952346)). Dentro Foto i file finiscono in "Eliminati di recente" ([MacSources](https://macsources.com/gemini-2-for-mac-review-a-smart-solution-for-cleaning-up-your-mac/)). Il supporto MacPaw ammette risultati "All neat!" con doppioni presenti, perché vede solo la libreria di sistema e i file locali ([MacPaw](https://macpaw.com/support/gemini/knowledgebase/gemini-2-troubleshooting)).
- **Causa.** Lo stato dichiarato dall'app non corrisponde a quello vero del disco. A questo si aggiungono librerie gestite, istantanee APFS e Time Machine locale che tengono occupato lo spazio.
- **Come evitarla.** Dopo ogni operazione rileggere il disco e mostrare lo spazio libero misurato, non quello stimato. Spiegare quando lo spazio non torna (istantanee, quarantena, file ancora aperti).
- **Conferma.** Quattro fonti, dal 2020 al 2021 più la pagina di supporto. **Media.**

### 1.8 Lentezza e blocchi su archivi grandi

- L'hash di un disco da 5 TB "will take days, maybe weeks" ([Digital Volcano](https://forum.digitalvolcano.co.uk/viewtopic.php?p=9953)). Su un NAS con 200.000 file la scansione rallenta fino a bloccarsi ([Digital Volcano](https://forum.digitalvolcano.co.uk/viewtopic.php?p=9257)).
- PhotoSweeper usava il 2% della CPU durante la scansione ([App Store](https://apps.apple.com/au/app/photosweeper/id463362050?mt=12)). Il plugin Excire per Lightroom è definito "resource hog", e sia Peakto sia Excire occupano molto spazio ([risultati di ricerca](https://scottwyden.com/peakto-search/)).
- Le soluzioni note: prima filtrare per dimensione e poi calcolare l'hash; usare strumenti pensati per dischi lenti e milioni di file, come fclones ([docs.rs](https://docs.rs/crate/fclones/0.28.0/source/README.md)); dividere la scansione per cartelle.
- **Causa.** Ogni file viene letto per intero anche quando non serve. Non c'è una cache tra una sessione e l'altra e i dischi meccanici non si leggono a pieno ritmo.
- **Come evitarla.** Filtrare per dimensione, poi hash parziale (inizio e fine), poi hash completo solo tra i candidati. Una cache persistente riconosce i file per volume, inode, dimensione e data, così una nuova scansione rilegge solo ciò che è cambiato. La scansione si può interrompere e riprendere, va per disco e segue l'ordine fisico. Bisogna stimare la durata, poter mettere in pausa e lasciare il Mac utilizzabile (vedi la regola sulla decodifica leggera di Selects).
- **Conferma.** Quattro fonti; quelle su NAS e HDD non sono datate. **Media-alta.**

### 1.9 Errore umano amplificato dall'app

- Catalogo sbagliato aperto, tutto marcato "scartato", cancellato: 12.000 file in pochi secondi ([Adobe, 2026](https://community.adobe.com/questions-675/accidentally-deleted-the-whole-library-stopped-before-completion-12k-of-47k-photos-in-trash-folder-1628969)).
- In Lightroom la scorciatoia di cancellazione nella raccolta Duplicati "doesn't ask for confirmation" (commento in [Lightroom Queen](https://www.lightroomqueen.com/clean-duplicate-photos/)).
- In dupeGuru la vista "Dupes Only" nasconde gli originali, così è facile marcare il file sbagliato ([Cisdem](https://www.cisdem.com/resource/dupeguru-for-mac-review-and-alternative.html)).
- Un'intera cartella di 1.200 foto è sparita dopo aver cancellato poche foto, senza traccia nel Cestino e senza una causa trovata ([Adobe, 2023](https://community.adobe.com/questions-675/lost-entire-images-in-folder-after-a-single-photo-deletion-972441)).
- **Causa.** Le azioni di massa sono troppo facili e il contesto (quale disco, quale archivio, quanti file, quanti GB) non si vede.
- **Come evitarla.** Prima di un'azione grande mostrare un riepilogo con volume, numero di file, GB e progetti cliente coinvolti. Oltre una soglia l'utente deve scrivere un numero o il nome del volume. Mai scorciatoie da tastiera senza conferma. Rendere visibile ogni copia del gruppo e mai solo "i doppioni".
- **Conferma.** Quattro fonti, dal 2017 al 2026. **Alta.**

### 1.10 Pulitori "di sistema" che toccano le librerie

- **CleanMyMac.** Oltre al caso della libreria Foto (1.5), un utente racconta che dopo una pulizia sono finiti nel Cestino "well over 100 files" di mp3, pdf e documenti (citazione dal riassunto di una ricerca sui thread Apple Community di CleanMyMac; il thread preciso non è stato aperto, il candidato più probabile è [questo](https://discussions.apple.com/thread/254123674)). MacPaw dice che l'app non cancella file personali in automatico ([MacPaw](https://macpaw.com/is-cleanmymac-safe)).
- **Causa.** Il pulitore considera "cache" o "spazzatura" cose che per un professionista sono dati (anteprime, cache di render, librerie).
- **Come evitarla.** RawLine Space non tocca mai pacchetti di libreria (`.photoslibrary`, `.fcpbundle`, `.lrdata`, `.cocatalog`) né cache delle app. Al massimo segnala quanto pesano e spiega come ripulirle dall'app che le ha create.
- **Conferma.** Tre fonti, aneddotiche, dal 2018 al 2022. **Media.**

---

## 2. Rimpianti e paure di chi libera spazio

**Rimpianti emersi**
- **Aver cancellato RAW che oggi saprebbe sviluppare meglio.** Il caso più citato: si cancellano i RAW dopo un viaggio e anni dopo si vorrebbero di nuovo con le capacità di oggi ([risultati di ricerca su Digital Camera World e Fstoppers](https://www.digitalcameraworld.com/news/i-hoarded-hundreds-of-gigabytes-of-raw-photos-until-i-saw-sense-and-hit-delete)). L'autore di Fstoppers tiene quasi tutto, eppure ammette di rimpiangere alcune cancellazioni ([Fstoppers, 2021](https://fstoppers.com/opinion/deleting-photos-when-it-too-much-and-should-stop-568561)).
- **Il valore futuro non si prevede.** "we actually don't know the utility or value of images" (Fstoppers). Matrimoni: i clienti tornano anni dopo a chiedere altre foto.
- **Tenere solo i JPEG consegnati** è un'abitudine dichiarata: c'è chi cancella i DNG appena consegnato il lavoro. La replica della community è che il RAW "is your original negative" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/what-to-do-with-jpg-amp-raw-files/td-p/13210634)).
- **Le modifiche perse fanno più male dei file.** Chi recupera i file ma non catalogo o XMP deve "start editing again" ([riassunto thread Adobe](https://recoverit.wondershare.com/faq/lightroom-delete-from-disk-raw-photos.html)).
- **Pile HDR e panorami.** Ci si chiede se tenere i RAW sorgente dopo l'unione ([Adobe, 2025](https://community.adobe.com/questions-680/re-storage-dilemma-keeping-or-deleting-hdr-pano-raws-907531)): nessuna risposta chiara.

**La posizione opposta (da tenere presente)**
- Secondo alcuni il rimpianto è raro: "how often does one regret deleting photos" (commento su Fstoppers). Il consenso è che "there is no consensus" ([Fstoppers](https://fstoppers.com/originals/case-keeping-every-raw-photo-you-shoot-or-not-366568)). Una pratica molto diffusa: tenere i RAW dei selezionati e buttare il resto.

**Paure ricorrenti**
- "Can I trust it to not delete the original?", titolo di un thread di un'altra app ([Tonfotos](https://community.tonfotos.com/d/324-can-i-trust-it-to-not-delete-the-original)). Cancellare doppioni è "always a little terrifying" ([MacNZ Mark](https://macnzmark.wordpress.com/2016/07/18/r-14/)).
- Paura che lo strumento "rompa il catalogo" (avvisi ricorrenti degli esperti Lightroom).
- Paura delle scelte di massa: gli esperti consigliano di rivedere ogni gruppo invece di cancellare in blocco ([Apple Community](https://discussions.apple.com/thread/251952346)). Chi ha 20.000 doppioni però non può rivederli uno per uno: è la tensione centrale.
- Paura di non poter tornare indietro dopo molto tempo (Cestino svuotato, scheda formattata).

**Cosa chiedono esplicitamente**
- Mostrare i doppioni senza cancellarli ("print duplicates by default", Czkawka #46). Marcare invece di cancellare (PhotoSweeper marca "Rejected"; Teekesselchen usa una parola chiave).
- Spostare in una cartella invece di cancellare (dupeGuru e Mylio "Move Marked"), mantenendo la struttura delle cartelle (richiesta SongKong).
- Unire i metadati delle copie tolte nella copia tenuta (Mylio lo promette; per Apple Foto gli utenti dicono che non succede).
- Poter dire "questi non sono doppioni" una volta per tutte (Apple Foto, [Apple Community](https://discussions.apple.com/thread/254985972)).
- Cancellare solo il RAW di una coppia RAW+JPEG (Six Colors).
- Un rapporto che elenchi anche cosa è stato tenuto, non solo cosa è stato tolto (correzione SongKong).

---

## 3. Requisiti concreti per RawLine Space

**Identità dei doppioni**
1. Si propone di liberare un "doppione" solo se è **identico byte per byte** (hash completo). Per arrivarci: filtro per dimensione, hash parziale, hash completo. Nome, dimensione e ora di scatto servono solo a scegliere i candidati.
2. "Simili" (raffiche, versioni ritagliate, export) è una sezione separata, solo da guardare, senza azioni automatiche.
3. Un RAW e il suo JPEG gemello, il RAW e il suo XMP, un export e il suo RAW **non sono mai doppioni**: sono legami di un gruppo.
4. Si ricorda tra una sessione e l'altra quello che l'utente ha detto "non è un doppione" e "tieni sempre".

**Cosa tenere**
5. Per ogni gruppo si controlla prima dell'azione che **almeno una copia resti**, esista sul disco, abbia lo stesso hash e si apra senza errori. Se una di queste cose manca, l'azione si blocca.
6. La scelta della copia da tenere è motivata in una riga e segue priorità visibili: copia referenziata da un catalogo o progetto, poi cartella cliente o archivio principale, poi nome originale (non "(1)", "copia", "-2"), poi disco di archivio invece di disco di passaggio. L'utente può riordinarle nella stessa schermata.
7. Se le copie hanno metadati o modifiche diversi (XMP diversi, voci di catalogo diverse), non si sceglie in automatico. Si mostra la differenza e si propone di unire i metadati prima.

**Cataloghi e progetti**
8. Lettura in sola lettura di cataloghi Lightroom e Capture One, librerie Foto, progetti Final Cut, Premiere e Resolve trovati sul volume. I file referenziati diventano "in uso" e non si propongono mai in automatico.
9. Se c'è un catalogo che non si sa leggere, la cartella resta bloccata e si avvisa.
10. Pacchetti di libreria e cache delle app non si toccano mai: solo il loro peso, con l'indicazione di dove pulirli.

**Azioni e ritorno indietro**
11. Nessuna cancellazione immediata. Si sposta in una **quarantena sullo stesso volume** (spostamento istantaneo, nessuna copia) con un giornale persistente. Il ripristino rimette ogni file al percorso esatto, anche dopo settimane o un riavvio. Lo spazio si libera solo con un secondo passo esplicito, dopo un periodo che l'utente sceglie.
12. Il gruppo di file di uno scatto (RAW, XMP, .acr, JPEG gemello, .THM/.LRV, proxy) si muove insieme.
13. Volumi exFAT, di rete o senza Cestino vanno riconosciuti e segnalati. La quarantena resta, il "cancella dopo" chiede doppia conferma.
14. I volumi di sola lettura dichiarati dall'utente (dischi di lavoro dei clienti) sono bloccati a livello di app, non solo nell'interfaccia.

**Conferme e rapporto**
15. Prima di ogni azione un riepilogo con volume, numero di file, GB, cartelle cliente, file in uso, cosa resta. Oltre una soglia l'utente scrive il numero o il nome del volume. Nessuna scorciatoia da tastiera che agisca senza conferma.
16. La vista mostra sempre **tutte le copie del gruppo**, mai solo "i doppioni".
17. Dopo l'azione si rilegge il disco e si mostra lo spazio libero misurato. Se lo spazio non torna, si spiega perché (istantanee APFS, quarantena).
18. Rapporto esportabile (CSV o testo) con cosa è stato spostato, cosa tenuto e perché, e hash: serve anche come prova verso il cliente.

**Prestazioni su 40–100 TB**
19. Cache persistente delle impronte, riconosciute per volume, inode, dimensione e data. Si riparte senza rileggere, la scansione si può interrompere e riprendere e va per volume, ordinata per percorso fisico.
20. Si stima la durata, si può mettere in pausa, si usa poca energia: il Mac deve restare utilizzabile durante una scansione di giorni.
21. Tutto in locale, senza rete (regola RawLine offline).

**Liberare spazio sui RAW (non doppioni)**
22. "Tieni solo i selezionati" non è mai il comportamento normale. Va proposto per progetto, mostrando cosa resta (RAW dei selezionati, export consegnati, sorgenti di pile HDR e panorami usate) e con quarantena lunga.
23. Le sorgenti di pile HDR e panorami e i RAW con un export collegato contano come "usati".

---

## 4. Fonti

Lightroom Classic e Adobe
- Bug 15.4 Duplicati, giugno 2026: https://community.adobe.com/bug-reports-674/p-delete-rejected-photos-in-duplicates-view-deletes-all-copies-1628661
- 12.000 file nel Cestino, catalogo sbagliato, giugno 2026: https://community.adobe.com/questions-675/accidentally-deleted-the-whole-library-stopped-before-completion-12k-of-47k-photos-in-trash-folder-1628969
- Bridge cancella l'XMP, luglio 2026: https://community.adobe.com/bug-reports-557/bridge-deletes-the-sidecar-xmp-file-associated-with-a-raw-file-when-a-another-file-with-similar-name-but-different-type-is-deleted-1632752
- Cartella sparita dopo poche cancellazioni, ottobre 2023: https://community.adobe.com/questions-675/lost-entire-images-in-folder-after-a-single-photo-deletion-972441
- Cancellata una, sparite due (copia virtuale), 2020: https://community.adobe.com/t5/lightroom-classic-discussions/deleted-one-photo-two-were-gone/td-p/11040289
- Doppi RAW nella stessa cartella: https://community.adobe.com/t5/lightroom-classic-discussions/lr-folder-contains-duplicate-raw-files/m-p/10210296/highlight/true
- "File associated with another photo": https://community.adobe.com/t5/lightroom-classic-discussions/file-associated-with-another-photo-in-catalog-error/td-p/13665737
- XMP non letti dopo il ripristino: https://community.adobe.com/questions-675/sidecar-file-not-being-read-after-restoring-accidentally-deleted-files-981656
- File .acr orfani: https://community.adobe.com/t5/lightroom-classic-discussions/p-information-on-acr-files/m-p/15191219
- RAW come negativo: https://community.adobe.com/t5/lightroom-classic-discussions/what-to-do-with-jpg-amp-raw-files/td-p/13210634
- Pile HDR e panorami, 2025: https://community.adobe.com/questions-680/re-storage-dilemma-keeping-or-deleting-hdr-pano-raws-907531
- Lightroom Queen, pulire i doppioni: https://www.lightroomqueen.com/clean-duplicate-photos/
- Teekesselchen e JPG/HEIC, 2021: https://www.lightroomqueen.com/community/threads/teekesselchen-duplicate-reject-flag-jpg-not-heic.42104/
- Duplicate Finder e Teekesselchen a confronto: https://www.lightroomqueen.com/community/goto/post?id=1214638
- Plugin per i doppioni: https://havecamerawilltravel.com/lightroom/find-duplicate-photos/
- Recupero dopo "Delete from Disk" (riassunto): https://recoverit.wondershare.com/faq/lightroom-delete-from-disk-raw-photos.html

Apple Foto, Gemini 2, CleanMyMac, PhotoSweeper
- Six Colors, RAW+JPEG inseparabili, febbraio 2026: https://sixcolors.com/post/2026/02/photos-wont-let-you-remove-the-raw-photo-from-a-rawjpeg-pair/
- Unione dei doppioni in Foto: https://discussions.apple.com/thread/256021424
- Metadati diversi non uniti: https://discussions.apple.com/thread/254424603
- Rilevamento doppioni in Foto 5: https://discussions.apple.com/docs/DOC-250001956
- "Segna come non doppione": https://discussions.apple.com/thread/254985972
- Gemini 2 e Foto, 2020: https://discussions.apple.com/thread/251952346
- Gemini 2, Cestino vuoto (MacRumors, pagina non apribile): https://forums.macrumors.com/threads/please-can-you-help-with-a-gemini2-problem.2434334
- Supporto MacPaw Gemini 2: https://macpaw.com/support/gemini/knowledgebase/gemini-2-troubleshooting
- MacSources su Gemini 2: https://macsources.com/gemini-2-for-mac-review-a-smart-solution-for-cleaning-up-your-mac/
- MacNZ Mark su Gemini 2: https://macnzmark.wordpress.com/2016/07/18/r-14/
- CleanMyMac e la libreria Foto, 2018: https://discussions.apple.com/thread/8411740
- CleanMyMac "Buyer Beware": https://discussions.apple.com/thread/254123674
- MacPaw "is CleanMyMac safe": https://macpaw.com/is-cleanmymac-safe
- Recensioni PhotoSweeper sull'App Store: https://apps.apple.com/au/app/photosweeper/id463362050?mt=12

Strumenti open source e altri
- Czkawka #46: https://github.com/qarmin/czkawka/issues/46
- dupeGuru (recensione Cisdem): https://www.cisdem.com/resource/dupeguru-for-mac-review-and-alternative.html
- dupeGuru su AlternativeTo: https://alternativeto.net/software/dupeguru/about
- Shotwell, falsi doppioni RAW: https://gitlab.gnome.org/GNOME/shotwell/-/issues/4791
- Shotwell, JPEG della coppia cancellato: https://gitlab.gnome.org/GNOME/shotwell/-/issues/2871
- SongKong, cancellati anche gli originali (musica), 2020: https://community.jthink.net/t/delete-duplicates-deletes-original/8617
- Tonfotos, "Can I trust it": https://community.tonfotos.com/d/324-can-i-trust-it-to-not-delete-the-original
- photo-sidecar-cleaner: https://github.imc.re/sisyphosloughs/photo-sidecar-cleaner
- fclones: https://docs.rs/crate/fclones/0.28.0/source/README.md
- Digital Volcano, hash lenti su HDD: https://forum.digitalvolcano.co.uk/viewtopic.php?p=9953
- Digital Volcano, NAS che si blocca: https://forum.digitalvolcano.co.uk/viewtopic.php?p=9257
- DaisyDisk, cancellazione: https://daisydiskapp.com/guide/deleting-files
- Mylio, rimuovere o cancellare: https://manual.mylio.com/topic/removing-vs-deleting-duplicate-images
- Mylio, originali persi: https://manual.mylio.com/topic/handling-lost-originals
- Cestino saltato su exFAT: https://yomotherboard.com/question/how-can-i-get-deleted-files-on-my-external-drive-to-go-to-trash-instead-of-being-permanently-deleted/
- MiniTool, Cestino saltato: https://www.minitool.com/data-recovery/files-deleted-from-external-hard-drive-are-not-in-recycle-bin.html
- Peakto ed Excire (limiti): https://scottwyden.com/peakto-search/
- Proxy e originali: https://blitzcutai.com/blog/video-proxies
- Nomi di file uguali: https://photographylife.com/avoiding-duplicate-file-names

Cancellare RAW
- Fstoppers, cancellare le foto, 2021: https://fstoppers.com/opinion/deleting-photos-when-it-too-much-and-should-stop-568561
- Fstoppers, tenere tutti i RAW: https://fstoppers.com/originals/case-keeping-every-raw-photo-you-shoot-or-not-366568
- Digital Camera World, centinaia di GB cancellati: https://www.digitalcameraworld.com/news/i-hoarded-hundreds-of-gigabytes-of-raw-photos-until-i-saw-sense-and-hit-delete
