# RawLine Space — Criticità: professionisti e migrazioni

Ricerca dell'11 novembre 2026 su forum, riviste e blog di fotografi e videomaker (matrimoni, eventi, sport, documentario, viaggio). Metodo: ricerca ampia, poi lettura delle pagine più ricche, poi controllo di quante fonti ne parlano e di quanto sono recenti.

**Come leggere i dati.** Sono quasi tutti racconti di singoli professionisti (forum Adobe, TrueNAS, Apple, MacRumors, Fstoppers, blog), non statistiche. "Diffusione" vuol dire quante fonti indipendenti riportano lo stesso problema. Reddit non si apre direttamente e i mirror restituiscono poco, quindi è poco rappresentato. Le pagine di dpBestflow (503) e di FredMiranda (403) erano irraggiungibili: le cito solo tramite i risultati di ricerca.

---

## 1. Problemi in ordine di frequenza e gravità

| # | Problema | Diffusione | Recenza | Gravità |
|---|---|---|---|---|
| 1 | Archivio sparso su tanti dischi, non si sa più cosa c'è dove | molto alta (8+ fonti) | 2019–2026 | alta: ore perse, lavori irrecuperabili |
| 2 | Spazio che cresce senza fine, costi in salita (dischi +46–100% tra 2025 e 2026) | alta (6+) | 2025–2026 | alta, ed è peggiorata quest'anno |
| 3 | Copie che falliscono in silenzio durante consolidamenti e migrazioni | alta (6+) | 2019–2026 | molto alta: perdita di dati scoperta tardi |
| 4 | Lightroom: file "mancanti" dopo uno spostamento, ricollegamento manuale | molto alta (10+ discussioni Adobe) | 2019–2026 | media-alta |
| 5 | Duplicati e copie divergenti dello stesso lavoro (più cataloghi, più dischi) | alta (6+) | 2019–2026 | media: spazio sprecato, modifiche perse |
| 6 | Clienti che chiedono le foto anni dopo | media (4–5) | 2014–2026 | media: mezza giornata per ritrovarle |
| 7 | Quanto tenere i RAW: nessuna regola, ansia del "e se servono?" | alta (6+) | 2018–2026 | media, mentale più che tecnica |
| 8 | Dischi che si guastano, bit rot, RAID che non basta | media-alta (5+) | 2024–2026 | alta |
| 9 | Abbandono di programmi (Aperture, cataloghi chiusi): regolazioni e metadati persi | media (5) | 2014–2019, eredità ancora presente | media |

### 1.1 Archivio sparso, non si sa cosa c'è dove
- **Casi.** Un documentarista ha un archivio "runs to 26 hard drives, and counting" e avverte di non contare sulla memoria un anno dopo ([Alan Fentiman, 2024/2026](https://alanfentiman.co.uk/documentary-filmmaker-footage-archive/)). Su Lightroom un fotografo raduna circa 89.000 foto da molti dischi esterni con "a lot of trash and duplicates" ([Adobe Community](https://community.adobe.com/t5/lightroom-classic/how-many-drives-used-to-store-photos/m-p/9550273)). Una matrimonialista etichetta un disco per anno per ritrovare il cliente di tre anni prima ([Fundy Designer](https://fundydesigner.com/tip-week-3/)).
- **Causa.** I dischi si comprano uno alla volta quando quello vecchio è pieno. Non c'è un indice che resti consultabile a disco staccato. Ogni anno cambiano nomi e struttura delle cartelle. Chi usa un catalogo offline (NeoFinder, Offline Files) lo fa perché il Finder non vede i dischi staccati ([CineD](https://www.cined.com/offline-files-for-macos-search-any-drive-even-when-its-unplugged/), [Cameraman Adelaide](https://cameramanadelaide.com.au/catalogue-external-raw-video-footage/)). Ma un catalogo mostra solo i dischi già scansionati, e scansionare dischi da 8 TB e oltre richiede molto tempo.

### 1.2 Spazio e costi
- **Casi.** Fstoppers (marzo 2026): un archivio disordinato "is not an asset. It's a liability", e i costi nascosti (backup, abbonamenti, migrazioni, tempo) sono sottovalutati ([Fstoppers, "The Anxiety of the Archive"](https://fstoppers.com/opinion/anxiety-archive-heavy-burden-digital-hoarding-722296)). Un fotografo sportivo, dopo due dischi morti nel NAS, porta l'archivio da circa 12 TB a 3 TB tenendo solo il meglio. Racconta HDD rincarati del 46–50% da settembre 2025, e nei commenti si legge che un 20 TB costa ormai 720 $, il doppio di prima ([Fstoppers, luglio 2026](https://fstoppers.com/business/what-two-dead-drives-taught-me-about-cost-keeping-my-photos-902496)). La scarsità di dischi nel 2026, legata ai data center per l'AI, è confermata dalla stampa tecnica ([PCWorld](https://www.pcworld.com/article/3063473/western-digital-is-out-of-hard-drives-because-ai-data-centers.html), [Tech4Gamers](https://tech4gamers.com/hard-drive-supply-shortages-get-even-worse-with-prices-rising-10-in-q2-2026/)).
- **Causa.** Il digitale ha tolto la selezione forzata che imponeva la pellicola: non si cancella niente. I RAW da 50–100 MB e i video 4K/6K fanno crescere tutto in fretta.
- **Novità 2026.** Liberare spazio, prima comodo, adesso fa risparmiare davvero. È l'argomento più forte per RawLine Space.

### 1.3 Copie che falliscono in silenzio
- **Casi.** Con il Finder verso un Synology in SMB, le copie grandi "will usually fail at some point" mentre rsync riesce sempre ([MacRumors, "Finder + NAS + copy = broken?"](https://forums.macrumors.com/threads/finder-nas-copy-broken.2479662/)). Errore −8062 copiando verso NAS Synology e QNAP dopo macOS Tahoe, causato dai `.DS_Store` e dai file `._` ([Apple Community, gennaio 2026](https://discussions.apple.com/thread/256234396)). Il numero di file copiati non corrisponde e Lightroom non aiuta a capire quali mancano ([Lightroom Queen, commenti](https://www.lightroomqueen.com/consolidate-photos-from-multiple-drives/)). Su un altro forum: "copies of large numbers of files can and do fail" ([OpenPhotographyForums](https://openphotographyforums.com/forums/threads/moving-files-from-pc-to-a-mac.1361/post-12872)). Un errore `filecopy` errno 34 copiando da NAS ([Apple Developer Forums](https://developer.apple.com/forums/thread/814076)).
- **Causa.** Il motore di copia del Finder non riprende da dove si è fermato e i suoi errori sono poco chiari. Lo strato SMB di macOS crea metadati Apple in file a parte. Nessuno verifica con un hash alla fine della copia.

### 1.4 Lightroom: file mancanti e ricollegamento
- **Casi.** Un fotografo copia sul NAS in 18 ore e poi il ricollegamento del catalogo "everything just hung" ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/batch-relink-missing-files/m-p/10501525)). Cambia il nome o il percorso del NAS e intere gerarchie finiscono col punto interrogativo ([UniquePhoto Q&A](https://www.uniquephoto.com/community/qa/how-can-i-relink-a-top-level-lightroom-folder-after-a-nas-path-or-server-name-changes)). Lightroom fa perdere a macOS la connessione SMB col Synology, con almeno 6–7 utenti dal 2021 al 2025 ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-causes-macos-to-lose-smb-connection-to-synology-nas/m-p/14334025)). Il catalogo sul NAS non è supportato da Adobe e chi ce lo mette prima o poi lo trova corrotto ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/using-nas-drive-for-your-images/m-p/13764234)).
- **Causa.** Il catalogo salva percorsi assoluti. Ogni spostamento fatto fuori da Lightroom rompe il collegamento. Gli spostamenti fatti dentro Lightroom su grandi volumi sono lenti e a volte "spariscono" file (Victoria Bampton, Lightroom Queen).

### 1.5 Duplicati e copie divergenti
- **Casi.** Più cataloghi Lightroom con lo stesso RAW modificato in modo diverso: unendoli escono copie virtuali o modifiche perse, e "You can NOT Sync 2 different catalogs" ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/how-to-properly-sync-multiple-lr-catalogs-main-one-and-on-the-road/td-p/11114869), [Lightroom Queen](https://www.lightroomqueen.com/merging-catalogs-overview/)). Un programma per i duplicati controllava solo 12.000 foto su 41.000 per colpa delle pile ([Lightroom Queen](https://www.lightroomqueen.com/consolidate-photos-from-multiple-drives/)). Nessuna fonte trovata spiega come scegliere "la copia più recente" tra due dischi.
- **Causa.** Disco da viaggio, disco di lavoro, backup e consegna al cliente sono copie dello stesso lavoro che poi prendono strade diverse (export rifatti, XMP aggiornati su una sola copia).

### 1.6 Clienti che tornano anni dopo
- **Casi.** Una cliente chiede le foto nove anni dopo e cercarle costa mezza giornata ([Photrio](https://www.photrio.com/forum/threads/fee-for-providing-lost-images.176687/)). Spose che tornano dopo tre anni ([DVinfo](https://www.dvinfo.net/forum/wedding-event-videography-techniques/509759-saving-raw-wedding-footage-how-long.html)). SLR Lounge consiglia di tenere i RAW buoni perché lo spazio costa meno di un file perso che il cliente richiede ([SLR Lounge](https://www.slrlounge.com/data-management-tips-for-multi-shooter-photo-studios/)).
- **Causa.** Non c'è un indice per cliente e data. Il nome del cliente spesso è solo nel nome della cartella.

### 1.7 Quanto tenere i RAW
- Non esiste uno standard. Le posizioni vanno da "cancellare dopo la consegna" o dopo 3 mesi, a "tenere per sempre", a cancellare i RAW non toccati e non valutati da 24 mesi se non c'è un obbligo col cliente ([Fstoppers 2026](https://fstoppers.com/opinion/anxiety-archive-heavy-burden-digital-hoarding-722296), [Fstoppers](https://fstoppers.com/originals/case-keeping-every-raw-photo-you-shoot-or-not-366568), [SLR Lounge](https://www.slrlounge.com/delete-raw-photos-archive-forever), [DVinfo](https://www.dvinfo.net/forum/wedding-event-videography-techniques/487559-how-long-do-you-keep-footage.html)). SLR Lounge per gli studi propone di tenere i progetti sul NAS per 12–24 mesi e poi passare a JPEG su dischi esterni.
- **Causa.** La paura di cancellare qualcosa che serve. Manca uno strumento che mostri quali RAW sono stati usati (valutati, modificati, esportati) e quali no.

### 1.8 Guasti e integrità
- Tre dischi persi in carriera e due in un colpo solo nel RAID 6. Un altro professionista trova il bit rot nonostante il RAID e ora fa lo scrubbing programmato sul Synology ([Fstoppers 2026](https://fstoppers.com/business/what-two-dead-drives-taught-me-about-cost-keeping-my-photos-902496)). Un blackout durante un'operazione RAID corrompe l'array su un DAS ([Bryan Hansel, 2025](https://bryanhansel.substack.com/p/swimming-in-gigabytes-of-images)). Circa 2.000 $ spesi in recupero dati dopo un guasto (risultato di ricerca su blog di matrimonialisti).

### 1.9 Abbandono di sistemi
- Con la chiusura di Aperture, "your edits will not convert", e le bandierine non passano a Lightroom ([PhotoJoseph](https://photojoseph.com/node/14105), [MacRumors](https://forums.macrumors.com/threads/aperture-to-photos-migration.2123017/)). Chi aveva scritto i metadati nei file se l'è cavata meglio. Lezione: le informazioni chiuse in un database proprietario scadono, quelle nei file e nei sidecar XMP restano.

---

## 2. Migrazioni verso NAS e DAS: cosa va storto

1. **Il Finder non regge le copie lunghe.** Copie di decine di TB falliscono a metà, restano ferme su "preparazione" e non riprendono. Chi ce la fa passa a rsync o Carbon Copy Cloner ([MacRumors](https://forums.macrumors.com/threads/finder-nas-copy-broken.2479662/), [Apple Community](https://discussions.apple.com/thread/5512219?page=3)). La Smithsonian ha impiegato "over six weeks" per copiare decine di TB in rete ([Smithsonian Libraries](https://blog.library.si.edu/?p=9563)). Un clone durato 56 ore dopo che il Finder era fallito.
2. **Nomi dei file.** I caratteri `? * / \ : | " < >`, gli spazi in fondo e la Unicode decomposta (NFD) di macOS vengono storpiati o bloccano la copia. TrueNAS con l'Apple encoding dà l'errore −43 su file come "test 2/2" ([TrueNAS Forums, gennaio 2026](https://forums.truenas.com/t/name-mangling-problems-with-mac-os-client/61656), [TrueNAS](https://www.truenas.com/community/threads/strange-copy-failure-over-smb-folder-name-mangled-files-missing.80403)). Percorsi oltre i 255–300 caratteri rifiutati ([SynoForum](https://www.synoforum.com/threads/migrating-source-has-filenames-paths-that-are-too-long.16244/)). La documentazione TrueNAS avverte che attivare la codifica Apple su una share esistente può cambiare i file già presenti ([TrueNAS docs](https://www.truenas.com/docs/scale/27/shares/smb/fcpshare/)).
3. **File fantasma `._` e `.DS_Store`.** Ne compare uno per ogni file copiato, raddoppiano il numero di file e causano l'errore −8062 su Tahoe ([Apple Community 2026](https://discussions.apple.com/thread/256234396)).
4. **SMB lento nello sfogliare.** Cartelle RAW che il Finder apre in circa 30 s, mentre su Windows o da Terminale si aprono subito. Le cause sono le miniature e i metadati. Il consiglio è avere meno file per cartella ([TrueNAS](https://forums.truenas.com/t/smb-and-macos-finder-speed-again/35792), [SynoForum](https://www.synoforum.com/threads/super-slow-nas-transfer-speeds-macos.6849/latest), [MacRumors](https://forums.macrumors.com/threads/why-macos-is-so-slow-when-browsing-network-drives.2449306)).
5. **Cataloghi e librerie da applicazione sul NAS.** Lightroom non è supportato in rete. Final Cut va bene solo con la libreria in locale e i media sul NAS, oppure su share configurate apposta ([Apple](https://support.apple.com/en-us/HT207128), [FCP.co](https://fcp.co/hardware-and-software/pro/1914-using-a-synology-nas-with-final-cut-pro-x)).
6. **Ricollegamento dopo la migrazione.** I percorsi cambiano (`/Volumes/Disco3/...` diventa `/Volumes/Archivio/...`) e tutti i cataloghi (Lightroom, Capture One, Photo Mechanic, Final Cut, Resolve) puntano al vuoto. Il consiglio ricorrente è tenere un "rename manifest" origine→destinazione ([ZimaSpace](https://shop.zimaspace.com/blogs/support-tips/filenames-change-between-macos-linux)).
7. **Manutenzione del NAS e ritorno al DAS.** Aggiornamenti firmware continui e "odd quirks" portano un fotografo di viaggio da un QNAP a un OWC Thunderbay 8 da 112 TB con mirror notturno ([Shutter Muse, 2025/2026](https://shuttermuse.com/my-professional-photo-backup-routine-2025/)). Un altro rinuncia al NAS perché richiedeva switch a 10 GbE, cavi e software nuovi: "I really don't like managing computer systems" ([Bryan Hansel, 2025](https://bryanhansel.substack.com/p/swimming-in-gigabytes-of-images)). Un NAS rallentato fino al riavvio dopo un anno acceso ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/catalog-backup-to-nas-slooow/m-p/14694222)).
8. **Verifica assente.** Le guide serie (dpBestflow, Lightroom Queen) dicono di non cancellare i dischi vecchi finché il nuovo non è verificato. In pratica pochi verificano con un hash: si fidano di "copia completata". Strumenti come rsync `-c` esistono ma sono da riga di comando ([dekoning.work](https://dekoning.work/blog/backup-and-verifying-file-copies-with-rsync)).
9. **Funzioni dei pacchetti NAS che non si portano dietro tutto.** Migrando Synology Photos tra NAS passa "everything except albums" ([Synology Community](https://community.synology.com/enu/forum/1/post/163701)).

---

## 3. Cosa vorrebbero e non trovano

- **Un indice unico di tutti i dischi, anche quelli staccati**, con miniature e ricerca per cliente, data, luogo e fotocamera. Oggi si mettono insieme NeoFinder o Offline Files e Lightroom, ma nessuno strumento fa tutto ([CineD](https://www.cined.com/offline-files-for-macos-search-any-drive-even-when-its-unplugged/)).
- **Capire quale copia è quella buona** tra due o più versioni dello stesso lavoro (più recente, più completa, con gli XMP aggiornati). Non è emerso nessuno strumento che lo faccia.
- **Una copia che riprende e verifica**, con un resoconto leggibile di cosa è fallito e perché (nome non valido, percorso troppo lungo), senza dover usare il Terminale.
- **Duplicati per contenuto**, non solo per nome o data, che tengano conto di pile, export e sidecar ([Habr](https://habr.com/en/articles/990286)).
- **Una regola di conservazione dei RAW basata su dati**: quali RAW non sono mai stati valutati, modificati o esportati. Fstoppers propone la soglia dei 24 mesi ma nessuno strumento la applica.
- **Una migrazione che non rompa i cataloghi**: una mappa dei percorsi vecchi→nuovi da usare per ricollegare.
- **Nessuna manutenzione da sistemista**: i professionisti vogliono fotografare, non gestire server.

---

## 4. Requisiti concreti per RawLine Space

**Inventario e ricerca**
1. **Indice persistente di ogni volume**, anche staccato: percorso, dimensione, date, EXIF essenziali (fotocamera, data di scatto, GPS), miniatura piccola e hash. Mostra "su quale disco è", con nome ed etichetta del disco, numero di serie e UUID.
2. **Ricerca per cliente e lavoro**: deduce cliente e lavoro dai nomi delle cartelle con regole modificabili, poi cerca per data di scatto e luogo. Tutto offline.
3. **Scansione riprendibile e incrementale**: dischi da 8–20 TB richiedono ore, quindi la scansione deve poter riprendere dopo una disconnessione, e le scansioni successive devono rileggere solo ciò che è cambiato.

**Duplicati e copie divergenti**
4. **Duplicati per hash** (veloce: dimensione, poi hash parziale, poi hash completo) e, a parte, **quasi-duplicati** (stesso scatto, export diversi).
5. **Confronto tra cartelle-lavoro** su più dischi: cosa c'è solo in A, solo in B, cosa è diverso (XMP più recente, export in più). Proposta della "copia migliore" con il motivo, sempre da confermare.
6. **Sidecar e pile insieme al loro RAW**: XMP, JPG gemelli, file `.cos` di Capture One, `.lrdata` e simili non vanno mai separati dal file a cui appartengono.

**Liberare spazio (con la regola di sicurezza professionale di Space)**
7. **Rapporto RAW usati e non usati**: valutati, con etichetta o modificati (XMP, catalogo Lightroom in sola lettura), esportati (corrispondenza con i JPEG di consegna). Soglia modificabile (es. 24 mesi) e mai sui lavori segnati "contratto/cliente".
8. **Stima dello spazio recuperabile in TB e in euro** ai prezzi del 2026: è l'argomento che convince adesso.
9. **Anteprima → conferma → giornale persistente → annullamento** su ogni operazione. Si sposta in quarantena, non si cancella subito.

**Consolidamento e migrazione verso NAS o DAS**
10. **Controllo preventivo dei nomi** per la destinazione (SMB, exFAT, ZFS): caratteri vietati, spazi in fondo, NFD/NFC, percorsi lunghi, nomi che coincidono ignorando le maiuscole. Proposta di rinomina con manifest.
11. **Copia robusta**: riprende dopo un'interruzione, non dipende dal Finder, va avanti con più copie in parallelo regolabili, gestisce le disconnessioni SMB e il risveglio dallo stop.
12. **Verifica con hash a fine copia** (xxHash o SHA-256) e rapporto finale: quanti file, quanti byte, quali sono falliti e perché. Il disco vecchio diventa "liberabile" solo dopo la verifica.
13. **Niente file `._` e `.DS_Store`** scritti sulla destinazione, oppure pulizia guidata.
14. **Manifest percorsi vecchi→nuovi** (CSV/JSON) e, in seguito, aiuto al ricollegamento di Lightroom (Find Missing Folder alla cartella più alta) e degli altri cataloghi, senza mai scrivere nei cataloghi senza conferma.
15. **Stime realistiche dei tempi** in base alla velocità misurata (USB, Thunderbolt, 1/2,5/10 GbE): "questa migrazione richiede circa 3 giorni".
16. **Struttura di destinazione proposta** (Anno/AAAA-MM-GG_Cliente_Lavoro, con RAW, Export e Video in cartelle separate), con un numero di file per cartella che non rallenti il Finder via SMB.
17. **Sorgenti in sola lettura**: nessuna scrittura sui dischi d'origine, nemmeno file nascosti o di indice (in linea con la regola sul G-SPEED).

**Salute**
18. **Avvisi su dischi vecchi o malati** (SMART dove si può leggere, età del disco, ultimo controllo) e **ricontrollo periodico degli hash** sull'archivio per scoprire il bit rot.
19. **Tutto offline**: niente cloud, niente account, coerente con la regola di RawLine.

---

## 5. Fonti

**Riviste e blog di fotografi**
- [Fstoppers — The Anxiety of the Archive (mar 2026)](https://fstoppers.com/opinion/anxiety-archive-heavy-burden-digital-hoarding-722296)
- [Fstoppers — What Two Dead Drives Taught Me (lug 2026)](https://fstoppers.com/business/what-two-dead-drives-taught-me-about-cost-keeping-my-photos-902496)
- [Fstoppers — The Case for Keeping Every Raw Photo](https://fstoppers.com/originals/case-keeping-every-raw-photo-you-shoot-or-not-366568)
- [Fstoppers — From NAS to Cloud](https://fstoppers.com/business/nas-cloud-how-photographers-should-rethink-storage-717747)
- [SLR Lounge — Data Management for Multi-Shooter Studios](https://www.slrlounge.com/data-management-tips-for-multi-shooter-photo-studios/)
- [SLR Lounge — Delete RAW or Archive Forever?](https://www.slrlounge.com/delete-raw-photos-archive-forever)
- [PetaPixel — How to Back Up Photos as a Wedding Photographer](https://petapixel.com/2019/06/20/how-to-back-up-photos-as-a-wedding-photographer/)
- [Shutter Muse — Professional Photo Backup Routine 2025](https://shuttermuse.com/my-professional-photo-backup-routine-2025/)
- [Bryan Hansel — Swimming in Gigabytes of Images (2025)](https://bryanhansel.substack.com/p/swimming-in-gigabytes-of-images)
- [Alan Fentiman — Documentary Footage Archive: 26 Hard Drives](https://alanfentiman.co.uk/documentary-filmmaker-footage-archive/)
- [Fundy Designer — Tip of the week (dischi per anno)](https://fundydesigner.com/tip-week-3/)
- [Lightroom Queen — Consolidate photos from multiple drives](https://www.lightroomqueen.com/consolidate-photos-from-multiple-drives/)
- [Lightroom Queen — Merging catalogs overview](https://www.lightroomqueen.com/merging-catalogs-overview/)
- [dpBestflow — Storage Migration](https://dpbestflow.org/migration/storage-migration) (non raggiungibile, 503)

**Forum: Adobe, Apple, NAS**
- [Adobe — Lightroom fa perdere la connessione SMB col Synology](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-causes-macos-to-lose-smb-connection-to-synology-nas/m-p/14334025)
- [Adobe — Synology NAS disconnecting with Lightroom](https://community.adobe.com/t5/lightroom-classic-discussions/synology-nas-disconnecting-repeatedly-when-using-lightroom/td-p/15315073)
- [Adobe — Catalog backup to NAS slooow](https://community.adobe.com/t5/lightroom-classic-discussions/catalog-backup-to-nas-slooow/m-p/14694222)
- [Adobe — Using NAS drive for your images](https://community.adobe.com/t5/lightroom-classic-discussions/using-nas-drive-for-your-images/m-p/13764234)
- [Adobe — Batch relink missing files](https://community.adobe.com/t5/lightroom-classic-discussions/batch-relink-missing-files/m-p/10501525)
- [Adobe — Sync multiple catalogs](https://community.adobe.com/t5/lightroom-classic-discussions/how-to-properly-sync-multiple-lr-catalogs-main-one-and-on-the-road/td-p/11114869)
- [Adobe — How many drives used to store photos](https://community.adobe.com/t5/lightroom-classic/how-many-drives-used-to-store-photos/m-p/9550273)
- [UniquePhoto — Relink after NAS path change](https://www.uniquephoto.com/community/qa/how-can-i-relink-a-top-level-lightroom-folder-after-a-nas-path-or-server-name-changes)
- [Apple Community — errore −8062 copiando verso NAS su Tahoe (gen 2026)](https://discussions.apple.com/thread/256234396)
- [Apple Community — Strange problem copying to NAS](https://discussions.apple.com/thread/5512219?page=3)
- [Apple Developer — filecopy errno 34 da NAS](https://developer.apple.com/forums/thread/814076)
- [Apple — Use shared storage with Final Cut Pro](https://support.apple.com/en-us/HT207128)
- [MacRumors — Finder + NAS + copy = broken?](https://forums.macrumors.com/threads/finder-nas-copy-broken.2479662/)
- [MacRumors — Why macOS is so slow browsing network drives](https://forums.macrumors.com/threads/why-macos-is-so-slow-when-browsing-network-drives.2449306)
- [TrueNAS — Name mangling con client macOS (gen 2026)](https://forums.truenas.com/t/name-mangling-problems-with-mac-os-client/61656)
- [TrueNAS — Copy failure over SMB, files missing](https://www.truenas.com/community/threads/strange-copy-failure-over-smb-folder-name-mangled-files-missing.80403)
- [TrueNAS — SMB and macOS Finder speed](https://forums.truenas.com/t/smb-and-macos-finder-speed-again/35792)
- [TrueNAS docs — Final Cut Pro share](https://www.truenas.com/docs/scale/27/shares/smb/fcpshare/)
- [SynoForum — Path troppo lunghi in migrazione](https://www.synoforum.com/threads/migrating-source-has-filenames-paths-that-are-too-long.16244/)
- [SynoForum — Super slow NAS transfer macOS](https://www.synoforum.com/threads/super-slow-nas-transfer-speeds-macos.6849/latest)
- [Synology Community — Photos library da NAS vecchio a nuovo](https://community.synology.com/enu/forum/1/post/163701)
- [FCP.co — Synology NAS con Final Cut Pro](https://fcp.co/hardware-and-software/pro/1914-using-a-synology-nas-with-final-cut-pro-x)

**Matrimoni, eventi, video**
- [Photrio — Fee for providing lost images](https://www.photrio.com/forum/threads/fee-for-providing-lost-images.176687/)
- [DVinfo — Saving raw wedding footage for how long?](https://www.dvinfo.net/forum/wedding-event-videography-techniques/509759-saving-raw-wedding-footage-how-long.html)
- [DVinfo — How long do you keep footage](https://www.dvinfo.net/forum/wedding-event-videography-techniques/487559-how-long-do-you-keep-footage.html)
- [Cameraman Adelaide — Catalogare il girato per la consultazione offline](https://cameramanadelaide.com.au/catalogue-external-raw-video-footage/)
- [CineD — Offline Files per macOS](https://www.cined.com/offline-files-for-macos-search-any-drive-even-when-its-unplugged/)

**Strumenti, prezzi, abbandono di sistemi**
- [OpenPhotographyForums — Moving files, verificare le copie](https://openphotographyforums.com/forums/threads/moving-files-from-pc-to-a-mac.1361/post-12872)
- [dekoning.work — Verificare le copie con rsync](https://dekoning.work/blog/backup-and-verifying-file-copies-with-rsync)
- [Habr — Confronto tra strumenti per i duplicati](https://habr.com/en/articles/990286)
- [ZimaSpace — Nomi che cambiano tra macOS e Linux](https://shop.zimaspace.com/blogs/support-tips/filenames-change-between-macos-linux)
- [ZimaSpace — DAS Thunderbolt o NAS per il fotografo solo](https://shop.zimaspace.com/blogs/nas-server-setup/solo-photographer-thunderbolt-das-vs-creator-nas) (venditore)
- [Smithsonian Libraries — sei settimane per copiare i dati](https://blog.library.si.edu/?p=9563)
- [PCWorld — Western Digital senza dischi per l'AI (2026)](https://www.pcworld.com/article/3063473/western-digital-is-out-of-hard-drives-because-ai-data-centers.html)
- [Tech4Gamers — Prezzi HDD +10% nel secondo trimestre 2026](https://tech4gamers.com/hard-drive-supply-shortages-get-even-worse-with-prices-rising-10-in-q2-2026/)
- [PhotoJoseph — Migrazione da Aperture](https://photojoseph.com/node/14105)
- [MacRumors — Aperture to Photos migration](https://forums.macrumors.com/threads/aperture-to-photos-migration.2123017/)
