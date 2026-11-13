# Cosa si rompe rinominando o spostando

Ricerca per RawLine Space, 11 novembre 2026. Domanda: quando si riordina un archivio foto/video (spostare cartelle, rinominare servizi ed export, unificare 30 varianti di "Export" in "Export/Alta" ed "Export/Web"), **cosa si rompe davvero** e come lo vivono le persone.

Legenda affidabilità: **[U]** = documentazione ufficiale del produttore · **[R]** = riportato dagli utenti (forum, blog) · **[D]** = dedotto da noi, da verificare con una prova.

Regola di fondo, detta da quasi tutti: le app che tengono un catalogo salvano **il percorso**. Se il percorso cambia fuori dall'app (Finder, script, o un'app come RawLine Space), l'app vede il file "mancante". I file non sono persi, ma il lavoro fatto nel catalogo (sviluppi, stelle, montaggi) resta appeso finché qualcuno non ricollega.

---

## 1. Tabella

| Oggetto | Cosa si rompe | Come si ricollega | Ricollegamento in massa? |
|---|---|---|---|
| **Lightroom Classic** (catalogo) | Spostare, rinominare o cancellare in Finder rompe il legame catalogo-file [U, Adobe]. Cartella con "?" e foto con "!". Con le anteprime avanzate (Smart Preview) il "!" può non comparire, quindi il problema si nasconde [R]. | Clic destro sulla cartella → *Trova cartella mancante*; per le foto *Trova foto mancanti* con l'opzione "trova foto mancanti vicine" [U]. | **Sì per cartelle spostate/rinominate**: ricollegando la cartella più alta si ricollega tutta la gerarchia [R, Adobe Community]. **No per file rinominati**: Lightroom cerca per nome, i file rinominati vanno ricollegati uno a uno [R, più fonti]. Bug segnalati: dopo il rinomina "già associata a un'altra foto", oppure serve riavviare [R]. |
| **Capture One** (catalogo) | Cartella spostata fuori dall'app resta nel catalogo come "offline" [U, blog Capture One]. | *Locate / Locate Folder…* sulla cartella e indicare la nuova posizione [U]. | **Parziale**: locate sulla cartella radice può ricollegare l'albero [R]; *Locate* è disattivato con più file selezionati [R]. Segnalato un bug del Locate che "può danneggiare il catalogo" e cartelle vecchie che "ritornano" al riavvio [R]. Le **sessioni** (cartelle Capture/Selects/Output relative) soffrono meno [D]. |
| **Photo Mechanic Plus** (catalogo) | File spostati, rinominati o cancellati fuori dall'app risultano "missing" [U, Camera Bits]. | Browse → albero Folder Path → *Update Folder Location…* [U]. Catalog Sync mette gli introvabili in una raccolta "Missing" [U]. | **Una cartella alla volta**: la documentazione non indica un modo in massa [U]. Le schede Browse già aperte col vecchio percorso "non si correggono da sole" [U]. Photo Mechanic senza Plus (solo navigazione) non si rompe: legge il disco [D]. |
| **Final Cut Pro** (media esterni, non copiati nella libreria) | Clip "Missing Media" se il file è stato spostato o rinominato nel Finder [U, Apple]. Anche **rinominare il volume** può far risultare mancanti i media [R, Creative COW]. | File → Ricollega file → Media originali; *Locate All* [U]. | **Sì**: dopo aver indicato un file, FCP trova gli altri, anche con schema di nome (File1_A → File2_A) [U]. Limiti: se nella cartella ci sono due file uguali non ricollega nessuno; il comando **non si può annullare** [U]. Nomi generici (Clip0001.mov) su più dischi confondono il ricollegamento [R]. Strumenti di terzi esistono (es. "Final Cut ReLinker", beta) [R]. |
| **DaVinci Resolve** (progetti nel database) | "Media Offline" per ogni clip spostata [R, molte guide]. | *Relink Selected Clips* (dal 20 sotto Clip Operations) oppure *Change Source Folder* se la struttura interna è rimasta uguale [U, manuale]. | **Sì**: *Relink Clips for Selected Bin*; il manuale dice che il percorso originale viene ignorato, quindi va bene per media riorganizzati [U]. Conviene scegliere la cartella più stretta e controllare durata e timecode [R]. |
| **Premiere Pro** (progetto) | Media offline se spostati [U, Adobe]. | *Collega media* (Link Media); "Ricollega gli altri automaticamente" [U]. | **Sì in teoria**: trovato il primo, ricollega gli altri nella stessa cartella o vicine [U]. **In pratica instabile**: bug segnalati nel 2025 (25.x) in cui non ricollega più gli altri, ricollegamenti che non restano dopo il salvataggio [R]. |
| **InDesign** (immagini collegate) | Collegamenti "mancanti" nel pannello Collegamenti [U]. All'apertura InDesign cerca da solo i mancanti [U, manuale]. | Pannello Collegamenti → Ricollega → "Cerca collegamenti mancanti in questa cartella" [U]. | **Sì per cartelle**: *Ricollega a cartella* risolve in un colpo i collegamenti rotti perché è cambiato il nome o il posto della cartella; **non aiuta se si sono rinominati i file** [R, CreativePro]. Utenti chiedono da anni un "ricollega tutto in un clic" [R]. |
| **Photoshop** (oggetti avanzati collegati) | Livello col collegamento mancante; può essere annidato e invisibile e bloccare *Pacchetto* [R]. | Photoshop prova da solo: percorso relativo, poi assoluto, poi **alias macOS**, poi cartella del documento [U, Adobe]. Altrimenti *Ricollega a file* [U]. | **Parziale**: dopo averne ricollegato uno cerca gli altri nella stessa cartella (non documentato) [R]. Se il PSD si sposta insieme alle immagini (percorso relativo) di solito regge [U]. |
| **Alias del Finder e segnalibri** (Open Recent, liste di sistema) | Uniscono percorso e numero di file (inode): **reggono a spostamenti e rinomine sullo stesso volume** [U Apple archivio, R Eclectic Light]. Si rompono se il file passa ad **altro volume** [R]. Se nasce un file con lo stesso nome nel vecchio posto, l'alias può puntare a quello [R]. | Automatico se stesso volume; altrimenti ricreare l'alias. | Non serve per lo stesso volume. Per volumi diversi: nessuno strumento standard [D]. |
| **Collegamenti simbolici (symlink)** | Tengono solo il percorso: rinominare qualunque cartella del percorso li rompe, "nessun ripiego" [R, Eclectic Light]. | Ricreare. | Script [D]. |
| **Preferiti della barra laterale del Finder** | Rinomina di solito ok; uno **spostamento** a volte fa sparire il preferito o dà "elemento originale non trovato" [R]. | Togliere e trascinare di nuovo la cartella [R]. | No. |
| **Link condivisi Dropbox** | Il link è legato all'ID del file, non al nome: **rinominare o spostare dentro Dropbox non rompe il link** [U, staff Dropbox]. Si rompe se si cancella o si ricarica come file nuovo [U]. Alcune segnalazioni contrarie [R]. | — | — Attenzione [D]: se RawLine Space sposta fuori e dentro Dropbox (copia+cancella invece di rinomina), il file diventa nuovo e **il link al cliente muore**. |
| **Hazel e automazioni** (Shortcuts, Automator, script) | Le regole sono legate alla cartella sorvegliata; non abbiamo trovato documentazione su cosa fa Hazel se la cartella viene rinominata. Segnalati problemi su iCloud, rete e permessi [R]. Script con percorsi scritti a mano si rompono di sicuro [D]. | Ripuntare la regola, ricontrollare Accesso completo al disco di Hazel Helper [R]. | No. |
| **Spotlight** | Dopo un cambio di struttura reindicizza; può segnare file come cambiati e far ripartire i backup [R, MacRumors]. Ricerche salvate per percorso si svuotano [D]. | Si aggiorna da solo; se serve `mdutil -E` [R]. | Automatico. |

---

## 2. Backup e sincronizzazioni dopo un riordino

Il rischio è doppio: **ricopiare terabyte** (tempo, banda, spazio) oppure, peggio, **cancellare** dall'altra parte perché il servizio vede "sparito il vecchio, comparso il nuovo".

| Servizio | Comportamento su rinomina/spostamento | Rischio |
|---|---|---|
| **Time Machine** | Niente pagina Apple ufficiale. Utenti e guide (Pondini) concordano quasi tutti: rinominare o spostare una cartella fa rifare il backup di **tutta la cartella e delle sottocartelle** [R]. Un utente con 150+ GB di cartelle foto/video rinominate segnala proprio questo [R]. | Disco di backup che si riempie, sfoltimento anticipato delle versioni vecchie [D]. |
| **Carbon Copy Cloner** | CCC fa combaciare destinazione e origine: quello che non c'è più nel vecchio percorso viene tolto dalla destinazione [U, Bombich]. Con SafetyNet attivo va temporaneamente nel SafetyNet o in un'istantanea; **con SafetyNet spento è cancellato subito** [U]. Non abbiamo trovato riconoscimento dei rinomina: la copia col nuovo nome riparte da capo [D, coerente con [R]]. | Destinazione piena (vecchio nel SafetyNet + nuovo), e copia vecchia persa alla potatura successiva [U]. Recuperare **prima** del backup successivo [U]. |
| **Backblaze Personal** | File spostato: il client lo considera nuovo, ma il server confronta l'impronta e "aggiorna solo la posizione" senza ricaricare [U]. La pagina sulla deduplica però chiede che coincidano **contenuto e nome**: un file **rinominato** potrebbe essere ricaricato [U, testo ambiguo; da provare]. I file rimossi dal vecchio percorso restano **30 giorni** di base (1 anno o per sempre a pagamento, solo da quando lo si attiva) [U]. | Upload di TB su connessioni lente; vecchie copie che scadono dopo 30 giorni [U]. Dischi esterni scollegati oltre 30 giorni: stessa sorte [U, noto]. |
| **Dropbox** | Rinomina vista come cancellazione + creazione: arriva la mail "hai eliminato molti file" [R]. Dropbox reindicizza; sembra caricare ma trasferisce solo i file cambiati [R]. Una minoranza dice di non aver più trovato i file [R]. | Panico da mail, sync lunghe; link condivisi salvi se è un vero rinomina (vedi tabella). |
| **Synology Drive** | Richiesta di funzione sul forum Synology: spostare 750 file già sincronizzati in una sottocartella li ha **cancellati sul server e ricaricati** [R]. Pausa + rinomina su entrambi i lati non ha evitato l'upload [R]. Hyper Backup: rinominare una cartella grande crea un backup nuovo [R]. Nessuna documentazione ufficiale trovata. | Ricarica completa; versioni che occupano spazio. |
| **Resilio Sync** | Ufficiale: un rinomina è visto come "cancellare il file col vecchio nome e crearne uno nuovo" [U]; serve l'Archivio attivo [U]. Utenti: dopo il rinomina tutti i file ricopiati in rete; spostamenti tra cartelle sincronizzate diverse = resync [R]. Versioni vecchie: **rinomina solo di maiuscole/minuscole ("TEst"→"Test") ha cancellato i file su entrambi i lati** [R]. | Cancellazioni che si propagano a tutti i dispositivi; recupero manuale dall'Archivio [U]. |
| **Syncthing / ownCloud / Nextcloud** (citati per confronto) | Syncthing su Synology: crea la cartella nuova, ricopia tutto, sposta la vecchia nelle versioni [R]. ownCloud: 20 minuti di upload poi cancella i vecchi [R]. Nextcloud su Samba: cancella invece di rinominare [R]. | Stesso schema. |

**In sintesi:** nessun servizio di sync/backup diffuso garantisce che un rinomina sia gratuito. Il caso peggiore realistico per un fotografo: rinominare 4 TB di servizi → Time Machine riparte, CCC duplica in SafetyNet e poi pota, Synology ricarica tutto, Dropbox manda mail di cancellazione. E un rinomina **solo di maiuscole** su dischi non sensibili alle maiuscole (default macOS) è un caso speciale e pericoloso.

---

## 3. Casi reali

- **"Ho riorganizzato in Finder"**: su Adobe Community un utente che aveva ristrutturato le cartelle fuori da Lightroom si è sentito dire che non c'è "nessun modo facile" di andare avanti; il consiglio è stato reimportare in un catalogo nuovo [R]. ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/how-do-i-find-missing-folders-and-restore-links-to-the-catalogue-on-a-mac/m-p/10468670))
- **Rinomina in blocco con strumento esterno**: un utente ha rinominato le foto con un programma di terzi e Lightroom non le ha più ricollegate, perché i nomi nel catalogo non coincidono [R]. **Questo è esattamente il caso di RawLine Rename + Space.** ([Adobe Community, bug](https://community.adobe.com/t5/lightroom-classic-bugs/p-loses-connection-with-files-after-folder-is-renamed/m-p/12826973))
- **Bug di Lightroom sul rinomina dopo l'importazione**: thread di bug lungo più pagine; ricollegare dà "già associata a un'altra foto", o le foto tornano solo riavviando [R]. ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-bugs/p-loses-connection-with-files-after-folder-is-renamed/m-p/12423379))
- **Ripetere più volte**: un altro utente ha ricollegato tutto solo "dopo ripetute esecuzioni di Trova foto mancanti" [R]. ([Lightroom Queen](https://www.lightroomqueen.com/community/threads/organize-images-in-finder-and-lightroom-folders.38027/))
- **Capture One "distrutto"**: thread intitolato "Moved my catalog on my PC and now its destroyed" e "Moved files to new hard disc, all files now offline" [R]. ([Capture One](https://support.captureone.com/hc/fr/community/posts/360012302898-Moved-files-to-new-hard-disc-all-files-now-offline))
- **Premiere 2025**: dopo il trasferimento su un altro disco i media non si ricollegano più in automatico; un utente ha dovuto ricollegare le clip una per una [R]. ([Adobe Community](https://community.adobe.com/t5/premiere-pro-discussions/quot-relink-other-automatically-quot-doesn-t-work-using-pr2025-version/td-p/14928279/highlight/true/page/2))
- **Time Machine e 150 GB di foto rinominate**: l'utente chiede come evitare il backup completo senza rimettere i vecchi nomi [R]. ([Apple Discussions](https://discussions.apple.com/thread/4815147))
- **Dropbox, 17.000 file**: dopo il rinomina, mail di cancellazione massiccia; i file erano nella cartella rinominata, ma "comparsi tra i file eliminati" per un quarto d'ora [R]. ([Dropbox Forum](https://www.dropboxforum.com/t5/Delete-edit-and-organize/I-got-an-email-telling-me-that-16-000-files-have-been-deleted/td-p/60741))
- **Resilio, maiuscole**: rinominare "TEst" in "Test" ha cancellato i file su tutti e due i lati [R]. ([Resilio Forum](https://forum.resilio.com/topic/19944-renaming-a-folder-to-the-same-name-with-different-case-causes-file-loss/))
- **Synology Drive**: 750 file spostati in una sottocartella → cancellati e ricaricati, con richiesta esplicita a Synology di gestire i rinomina senza cancellare [R]. ([Synology Community](https://community.synology.com/enu/forum/1/post/195501))

Il tono comune: non è la perdita di file a spaventare, è **il lavoro nel catalogo che sembra sparito** e le ore passate a ricollegare. Il consiglio che ritorna ovunque: "fai tutto dentro l'app del catalogo, mai nel Finder".

---

## 4. Requisiti concreti per RawLine Space

Tutto offline, sul Mac, coerente con la regola di sicurezza di Space (anteprima, conferma, giornale, annulla).

### A. Cosa rilevare prima di toccare qualcosa

1. **Cataloghi che puntano alla cartella**: cercare sui dischi `.lrcat` (Lightroom, SQLite), `.cocatalog` (Capture One), cataloghi Photo Mechanic Plus, `.fcpbundle` (Final Cut), progetti `.prproj` (gzip XML), `.indd`, PSD con collegamenti, e il database di Resolve. Leggerli **in sola lettura** (copia temporanea), estrarre i percorsi e dire: "312 foto del catalogo *Lavori 2024* sono in questa cartella".
2. **Media dentro o fuori**: per le librerie Final Cut distinguere media copiati dentro la libreria (non si rompono) da media esterni (si rompono).
3. **Cartelle sincronizzate o sotto backup**: riconoscere Dropbox, iCloud Drive, Google Drive, Synology Drive, Resilio (`.sync`), Syncthing (`.stfolder`), destinazioni CCC, esclusioni di Time Machine. Stimare **quanti GB ripartiranno**.
4. **Rinomina che cambiano solo maiuscole/minuscole** ("export" → "Export"): segnalarli a parte e farli in due passaggi sicuri (nome temporaneo, poi finale).
5. **File rinominati, non solo spostati**: per Lightroom e InDesign è il caso che non si ricollega in massa. Separare nell'anteprima "cartelle spostate" (ricollegabili con un clic dentro l'app) da "file rinominati" (molto più costosi).
6. **Alias, symlink, preferiti, regole Hazel, script**: elencare symlink e alias che puntano dentro l'area toccata; leggere se possibile le cartelle sorvegliate da Hazel.
7. **Volume di destinazione**: spostare su un altro volume = copia + cancella. Rompe alias, link Dropbox, deduplica dei backup. Avvisare esplicitamente.
8. **App aperte**: se Lightroom, Capture One, FCP o Resolve sono aperti sul catalogo coinvolto, fermarsi.

### B. Cosa avvisare (in parole semplici)

- "Questa cartella è nel catalogo Lightroom *X*: dopo lo spostamento le foto avranno il punto esclamativo. Ti diciamo esattamente cosa fare per ricollegarle."
- "Rinominare questi 4.200 file rompe il legame col catalogo e **Lightroom non li ricollega in automatico**." Proporre l'alternativa: rinominare dall'interno di Lightroom, oppure solo cartelle.
- "Questa cartella è in Synology Drive / Resilio: il rinomina potrebbe ricaricare 1,8 TB e propagare cancellazioni sugli altri dispositivi."
- "Time Machine / CCC rifaranno la copia di 2,3 TB: serve spazio sul disco di backup."
- "Backblaze tiene la versione col vecchio nome solo 30 giorni."
- "Questi file hanno link condivisi Dropbox: spostali **dentro** Dropbox, non fuori e dentro."

### C. Cosa offrire per ricollegare

1. **Giornale vecchio percorso → nuovo percorso** (CSV/JSON leggibile), per ogni file, salvato accanto all'archivio e nell'app. È la base per tutto il resto e per l'annullamento.
2. **Istruzioni per app** generate dal giornale: "In Lightroom: clic destro su *2023/Cliente_Export* → Trova cartella mancante → scegli *Export/Alta*". Ricollegare la cartella **più alta** possibile, così ne bastano pochi.
3. **Preferire spostamenti di cartelle a rinomina di file** quando c'è un catalogo: progettare le regole di Space perché il nome del file resti uguale e cambi solo la cartella. Così Lightroom, InDesign, FCP, Resolve e Photoshop ricollegano in massa.
4. **Mantenere la struttura interna** delle cartelle spostate: è la condizione per *Change Source Folder* di Resolve e *Ricollega a cartella* di InDesign.
5. **Alias di cortesia (facoltativo)** nel vecchio posto per un periodo, così chi apre un vecchio percorso dal Finder trova la strada. Mai symlink nelle cartelle sincronizzate.
6. **Annulla completo** basato sul giornale: rimettere i nomi vecchi è la soluzione più sicura se il cliente scopre il problema tardi.
7. **Modalità "solo cataloghi esclusi"**: opzione per non toccare nulla che sia referenziato da un catalogo finché l'utente non ha ricollegato o confermato.
8. **Fase 2 (da valutare)**: aggiornare direttamente i percorsi nel catalogo Lightroom (SQLite) o generare XML FCP/Resolve per il ricollegamento. È possibile tecnicamente ma rischioso: solo con catalogo chiuso, copia di sicurezza prima, e prove serie. Da non fare nella prima versione.
9. **Rinomina sul NAS, non dal Mac**: per Synology suggerire di fare il rinomina dal NAS (DSM) quando possibile, che secondo alcuni utenti evita la ricarica [R, da verificare].

### D. Prove da fare prima di promettere qualcosa

- Time Machine: rinominare una cartella da 5 GB e misurare il backup successivo.
- Backblaze: rinominare file e cartella e controllare se ricarica (la documentazione è ambigua).
- Synology Drive e Dropbox: rinomina dal Mac e dal NAS/web, misurare il traffico.
- Lightroom: spostare 3 cartelle con RawLine Space, ricollegare con *Trova cartella mancante* dalla cartella padre, verificare che stelle e sviluppi ci siano tutti.
- FCP e Resolve: spostare media esterni mantenendo la struttura e ricollegare.
- Tutte le prove su copie, mai sul disco di lavoro clienti.

---

## 5. Fonti

**Ufficiali**
- Adobe, Lightroom Classic, trovare le foto mancanti: https://helpx.adobe.com/lightroom-classic/help/locate-missing-photos.html
- Adobe, InDesign, aggiornare e ripristinare collegamenti: https://helpx.adobe.com/ca/indesign/desktop/add-graphics-and-media/manage-links/update-restore-replace-links.html
- Adobe, Photoshop, oggetti avanzati collegati: https://helpx.adobe.com/au/photoshop/desktop/create-manage-layers/smart-objects/package-linked-smart-objects.html
- Adobe, Premiere, ricollegare media offline: https://helpx.adobe.com/ro/premiere-pro/how-to/relink-offline-media.html
- Apple, Final Cut Pro, ricollegare clip ai file: https://support.apple.com/guide/final-cut-pro/relink-clips-to-media-files-ver26f5c8c9/mac
- Apple, Final Cut Pro, problemi di gestione media: https://support.apple.com/en-bh/guide/final-cut-pro/verd1f9666b/mac
- Apple (archivio), alias: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/Aliases.html
- Blackmagic, manuale Resolve (copia), relink: https://www.steakunderwater.com/VFXPedia/__man/Resolve18-6/DaVinciResolve18_Manual_files/part532.htm
- Capture One, ricollocare file offline: https://www.captureone.com/blog/relocating-catalog-images-in-capture-one-pro-7 · https://learn.captureone.com/relocating-offline-files-catalogs/
- Camera Bits, cartelle spostate fuori dall'app: https://docs.camerabits.com/support/solutions/articles/48001164434-updating-the-catalog-location-of-externally-moved-folders
- Camera Bits, media mancanti: https://docs.camerabits.com/en/support/solutions/articles/48001162818
- Bombich (CCC), file non più sull'origine: https://bombich.com/kb/ccc6/files-arent-on-source-may-be-removed-from-destination
- Bombich, SafetyNet: https://bombich.com/kb/ccc6/protecting-data-already-on-your-destination-volume-carbon-copy-cloner-safetynet
- Backblaze, deduplica e spostamenti: https://www.backblaze.com/computer-backup/docs/deduplication
- Backblaze, spostare o rinominare un file: https://help.backblaze.com/hc/en-us/articles/217666638-What-Happens-If-I-Move-or-Rename-a-File
- Backblaze, cronologia versioni: https://www.backblaze.com/computer-backup/docs/version-history
- Resilio, file cancellati dalla cartella sincronizzata: https://www.resilio.com/documentation/content/troubleshooting/general/how_can_it_happen_that_files_got_deleted_from_the_sync_folder_and_what_to_do_next/
- Synology, Cloud Sync e cartella rinominata: https://kb.synology.com/en-sg/DSM/tutorial/Cannot_sync_with_Dropbox_Team_Space_with_Cloud_Sync
- Dropbox (staff sul forum), link condivisi e spostamenti: https://www.dropboxforum.com/t5/Create-upload-and-share/Will-moving-the-file-that-a-shared-link-points-to-break-the/m-p/329913

**Forum e blog (riportato dagli utenti)**
- Lightroom, bug cartella rinominata: https://community.adobe.com/t5/lightroom-classic-bugs/p-loses-connection-with-files-after-folder-is-renamed/m-p/12423379
- Lightroom, riordino in Finder: https://community.adobe.com/t5/lightroom-classic-discussions/how-do-i-find-missing-folders-and-restore-links-to-the-catalogue-on-a-mac/m-p/10468670
- Lightroom, ricollegamento in massa: https://community.adobe.com/t5/lightroom-classic-discussions/batch-relink-missing-files/m-p/10501525
- Lightroom Queen, organizzare in Finder: https://www.lightroomqueen.com/community/threads/organize-images-in-finder-and-lightroom-folders.38027/
- Capture One, file offline dopo cambio disco: https://support.captureone.com/hc/fr/community/posts/360012302898-Moved-files-to-new-hard-disc-all-files-now-offline
- Capture One, bug del Locate: https://support.captureone.com/hc/fr/community/posts/360012253538-Serious-bug-in-the-Locate-feature-can-damage-a-catalog
- Premiere 2025, ricollegamento automatico: https://community.adobe.com/t5/premiere-pro-discussions/quot-relink-other-automatically-quot-doesn-t-work-using-pr2025-version/td-p/14928279/highlight/true/page/2
- Larry Jordan, perché i file FCP vanno offline: https://larryjordan.com/articles/fcp-x-why-files-go-offline/
- Creative COW, media FCP e nome del volume: https://creativecow.net/forums/thread/media-no-longer-linked-on-storage-drive/page/2/
- Final Cut ReLinker (terzi, beta): https://petezhang-com.pages.dev/final-cut-relinker
- CreativePro, ricollega a cartella in InDesign: https://creativepro.com/?p=109659
- InDesign, richiesta "ricollega tutto": https://community.adobe.com/t5/indesign-discussions/add-one-click-option-to-relink-all-missing-links-to-a-folder/m-p/15495825
- Eclectic Light, link, alias e declino dei percorsi: https://eclecticlight.co/2024/08/26/links-aliases-and-the-decline-of-paths/
- Eclectic Light, alias e segnalibri: https://eclecticlight.co/2019/01/11/aliases-and-bookmarks-are-smarter-than-you-think/
- Preferiti Finder e spostamenti (cocoa-dev): https://lists.apple.com/archives/cocoa-dev/2015/May/msg00259.html
- Time Machine, cartella rinominata: https://discussions.apple.com/thread/4815147
- Time Machine, stessa cartella spostata: https://forums.macrumors.com/threads/time-machine-re-backups-same-files-after-moved-to-different-folder-on-same-drive.1529718
- Dropbox, rinomina e mail di cancellazione: https://www.dropboxforum.com/discussions/101001014/does-renaming-a-folder-cause-all-files-in-folder-to-be-deleted-from-old-re-added/4083
- Dropbox, 16.000 file "cancellati": https://www.dropboxforum.com/t5/Delete-edit-and-organize/I-got-an-email-telling-me-that-16-000-files-have-been-deleted/td-p/60741
- Synology Drive, richiesta di gestire i rinomina: https://community.synology.com/enu/forum/1/post/195501
- Synology, rinominare una cartella grande: https://www.synoforum.com/threads/changing-a-large-folders-name.13357/
- Resilio, resync dopo rinomina: https://forum.resilio.com/topic/40799-resync-all-files-after-the-folder-after-i-renamed-the-folders-name/
- Resilio, rinomina solo maiuscole e perdita di file: https://forum.resilio.com/topic/19944-renaming-a-folder-to-the-same-name-with-different-case-causes-file-loss/
- Syncthing, rinominare una sottocartella grande: https://forum.syncthing.net/t/how-best-to-efficiently-change-the-name-of-a-large-subfolder/16514
- Hazel su Synology (permessi): https://talk.macpowerusers.com/t/hazel-issue-on-synology/17846

Note sul metodo: alcune pagine ufficiali (Adobe help, Backblaze help, forum Resilio) hanno rifiutato la lettura diretta; per quelle il contenuto viene dai riassunti dei risultati di ricerca. Il comportamento di Time Machine non ha documentazione Apple: è tutto [R].
