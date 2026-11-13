# Archivi video: criticità reali di videomaker e creator ibridi

Ricerca dell'11 novembre 2026 per RawLine Space. Tre passaggi: ricerca larga, lettura dei thread più ricchi, controllo sui manuali ufficiali. Le citazioni sono brevi e tradotte o riportate in originale; i link sono nella sezione 5.

**Limiti della ricerca.** Il budget di ricerche web si è esaurito prima del controllo finale: non ho potuto aprire il manuale ufficiale di DaVinci Resolve (le pagine di Blackmagic Forum rispondevano 403) né la pagina Apple sui backup delle librerie. Dove una cosa viene da forum o blog e non da un manuale è segnato **[non ufficiale]**. Reddit non è emerso nei risultati: le lamentele vengono da Apple Community, Adobe Community, Creative COW, DVinfo, Blackmagic Forum (dai riassunti dei risultati), Larry Jordan, ProVideo Coalition.

---

## 1. Criticità in ordine di gravità

### 1.1 Cancellare l'unica copia credendo che "stia nella libreria" (gravissima, perdita definitiva)
- In Final Cut, con "Lascia i file nella posizione corrente", la libreria contiene solo **link simbolici** ai file esterni: chi cancella o sposta gli originali dal Finder perde il girato. Apple elenca come cause dei clip mancanti file "spostati o rinominati nel Finder" ([Apple, icone di avviso](https://support.apple.com/en-za/guide/final-cut-pro/verd1f977a7/mac)).
- Caso tipico su Apple Community: originali cancellati, restano solo i proxy; si vedono con Vista > Solo proxy, ma "you can't create a proxy if FCP cannot find the media" ([thread 254866395](https://discussions.apple.com/thread/254866395)). Se in quel momento uno "strumento di pulizia" cancella anche i proxy, non resta niente.
- I **backup automatici** delle librerie (Final Cut) e dei progetti (Resolve) contengono **solo il database**, non i media ([riassunto Apple Community](https://discussions.apple.com/thread/254866395); [Larry Jordan su Resolve](https://larryjordan.com/articles/how-i-lost-all-my-davinci-resolve-projects-and-how-you-can-save-yours/)). Molti lo scoprono dopo.
- Su Adobe Community un thread aperto nel 2019 e ancora attivo nel 2024 raccoglie perdite di girato dopo crash, ricollegamenti e "offline media" ([Adobe Community](https://community.adobe.com/t5/premiere-pro-discussions/premiere-pro-deleted-all-of-my-original-video-files-for-good-over-18-hours-of-editing-and-priceless/m-p/11777302)): nessuna causa unica, ma il pattern è "file spariti, nemmeno nel cestino".

**Diffusione:** molto alta e costante negli anni (thread dal 2019 al 2025).

### 1.2 Cancellare la "cartella cache" che in realtà è il database di Resolve (gravissima)
- Larry Jordan (dic. 2024) ha perso tutti i progetti cancellando una cartella creata da Resolve al primo avvio: era la Project Library. Resolve "doesn't store files by project" ([Larry Jordan](https://larryjordan.com/articles/how-i-lost-all-my-davinci-resolve-projects-and-how-you-can-save-yours/)).
- I progetti di Resolve vivono in un **database** (cartella "Resolve Disk Database" / "Resolve Project Library" secondo la versione, o PostgreSQL), non in file di progetto sparsi. Un `.drp` esportato pesa poche centinaia di KB senza media ([Larry Jordan, backup e archivi](https://larryjordan.com/articles/managing-projects-in-davinci-resolve-backups-exports-and-archives/)). Sul Blackmagic Forum c'è il thread "Databases went missing...Again....project lost" ([forum](https://forum.blackmagicdesign.com/viewtopic.php?p=918735)) **[solo titolo e riassunto]**.

**Per RawLine Space:** una cartella con nome generico e file `.db` non è cache: va riconosciuta come database e non va mai proposta per la pulizia.

### 1.3 Struttura delle schede rotta: copiati solo gli MP4/MXF (grave, spesso recuperabile ma costosa)
- Sony: chi copia solo le cartelle dei clip "orphaned" il girato; Clip Browser, XDCAM Transfer e il plugin di FCP non lo riconoscono più. Si rimedia ricreando la struttura e rigenerando gli XML con il software Sony ([DVinfo, EX1 orphaned MP4](https://www.dvinfo.net/forum/sony-xdcam-ex-pro-handhelds/124349-ex1-orphaned-mp4-files-solved.html); [DVinfo, solo MP4](https://dvinfo.net/forum/sony-xdcam-ex-pro-handhelds/486257-missing-support-files-help-only-mp4s.html)). Thread vecchi (2008–2018), ma il problema si ripresenta con XAVC.
- Canon XF / Cinema EOS: va copiata **tutta** la cartella `CONTENTS`; senza la struttura "you are effectively locked out" dal girato ([DVinfo, rescue C300](https://www.dvinfo.net/forum/canon-cinema-eos-camera-systems/517294-how-rescue-c300-files.html); [DVinfo, copia HDD](https://www.dvinfo.net/forum/canon-xf-series-4k-hd-camcorders/489175-cant-open-files-hdd-copy.html)).
- Si perdono: timecode e metadati dell'XML (Sony), relazioni tra clip spezzati, proxy di camera, profili, e la possibilità di usare gli strumenti del produttore.
- Sony stesso nel manuale FS5: non modificare file e cartelle della scheda dal computer, i file di gestione sono nascosti e cancellarli impedisce la riproduzione ([manuale PXW-FS5 p.158](https://www.manualslib.com/manual/1037099/Sony-Pxw-Fs5.html?page=158)).

### 1.4 Media offline dopo spostamenti e riorganizzazioni (grave per tempo perso, raramente per dati)
- Final Cut: "la maggior parte dei problemi" nasce dallo spostare file col Finder invece che con Final Cut ([Larry Jordan, perché i file vanno offline](https://larryjordan.com/articles/fcp-x-why-files-go-offline/)). Casi reali: libreria spostata su NAS, tutto offline e niente sotto "Mancanti" nel ricollegamento ([Apple Community 254726346](https://discussions.apple.com/thread/254726346)).
- Resolve: ricollegamento con "Relink Selected Clips" e Deep Search; su Windows le lettere di unità che cambiano mandano tutto offline ([riassunti Blackmagic Forum](https://forum.blackmagicdesign.com/viewtopic.php?p=1144196)).
- **Conseguenza per noi:** ogni spostamento che RawLine Space fa (riordino archivio) può mandare offline progetti di FCP, Resolve e Premiere che puntano ai vecchi percorsi. È il rischio numero uno di una funzione di "riordino".

### 1.5 Librerie Final Cut enormi senza capire perché (media, molto diffusa)
- "5 GB che diventano 264 GB": libreria su disco interno pieno, Mac che non si avvia più (marzo 2025, [Apple Community 256008995](https://discussions.apple.com/thread/256008995)). Cause: render in background, transcodifica ottimizzata all'importazione, ProRes molto più pesante dell'H.264.
- Altri casi: "libreria 10 volte più grande degli originali" ([254262438](https://discussions.apple.com/thread/254262438)), "350 GB" ([251360205](https://discussions-cn-prz.apple.com/thread/251360205)), "spazio occupato anche dopo aver cancellato i render" ([253106233](https://discussions.apple.com/thread/253106233)).
- Rimedio standard: File > Elimina file generati della libreria; ma se si cancellano le preferenze il render in background si riattiva da solo.
- **Insidia:** importando le MP4 Sony da una struttura `M4ROOT` con "Copia nella libreria", Final Cut le **re-incapsula in .mov** e talvolta le rinomina con suffissi `(fcp1)`, `(fcp2)`: "been this way for over 10 years" (set. 2025, [Apple Community 256136664](https://discussions.apple.com/thread/256136664)). Risultato: doppioni **non identici byte per byte** dell'originale sulla scheda.

### 1.6 Doppioni sparsi su più dischi senza sapere qual è il master (media, molto diffusa)
- Il girato viene copiato su disco di lavoro, backup, libreria (gestita), cartella del cliente, NAS: nessuno sa più quale copia è quella a cui puntano i progetti. Avvertenza ricorrente: verificare a quale copia punta il progetto prima di cancellare "il doppione" **[non ufficiale, blog e forum]**.
- Premiere crea duplicati nel progetto se lo stesso file viene importato due volte e "Consolidate Duplicates" spesso non li unisce se un solo metadato differisce ([Adobe Community](https://community.adobe.com/t5/premiere-pro-discussions/consolidate-duplicates-does-not-work/m-p/15124334/highlight/true)).
- Doppioni "semantici" non trovati dall'hash: re-wrap .mov di FCP (1.5), clip uniti dei GoPro, transcodifiche ProRes, export intermedi.

### 1.7 Gestori di progetto che non fanno quello che promettono (media)
- **Premiere Project Manager**: "Consolida e transcodifica" con rifilatura copia spesso i **clip interi**; un utente si aspettava 56 GB e ne ha ottenuti 189 su 207 ([Adobe bug report](https://community.adobe.com/t5/premiere-pro-bugs/project-manager-consolidate-and-transcode-problems/idi-p/9260441)). Peachpit conferma che con certi media crea "copies of the full original clips" ([Peachpit](https://www.peachpit.com/articles/article.aspx?p=3113584&seqNum=3)).
- **Resolve Media Management**: la rifilatura con codec a compressione temporale (H.264, XAVC) è supportata dal manuale 18, ma utenti segnalano che in 16–17 copiava interi i clip XAVC e che in 19–20, se la rifilatura fallisce, copia il clip intero senza errore; un thread si intitola "Media Management turns timeline into a mess" ([Blackmagic Forum](https://forum.blackmagicdesign.com/viewtopic.php?p=1150366)) **[da riassunto, pagina non leggibile]**.
- **Final Cut Consolida**: casi in cui FCP dice che "i file esistono già in quella posizione" o in cui consolidare lascia la libreria in stato strano ([Apple Community 255826031](https://discussions-kr-prz.apple.com/thread/255826031)).

### 1.8 Cosa tenere dopo la consegna: nessuna regola condivisa (media, decisionale)
- Linee guida ricorrenti: tenere sempre consegne finali, file di progetto (libreria FCP, database Resolve, progetto Premiere) e asset personalizzati, che pesano poco; cancellare render e proxy dopo l'archiviazione; politiche di conservazione del girato a tempo ([Video Project Archiving Best Practices](https://impactstudiostv.com/blog/video-production-archive-best-practices); [Adobe Community, girato dopo il progetto](https://community.adobe.com/t5/premiere-pro-discussions/what-to-do-with-raw-footage-after-completion-of-project/m-p/15127377)) **[non ufficiale]**.
- Il nodo: decidere quale girato "non usato" si può buttare richiede sapere quali clip sono in quali timeline, e i progetti sono in tre formati chiusi diversi.

### 1.9 File d'accompagnamento delle action cam e dei droni (media-bassa, ma subdola)
- GoPro `.LRV`/`.THM` e DJI `.LRF` sono anteprime rigenerabili; ma DJI `.SRT` contiene dati di volo (coordinate, quota) e non si rigenera ([MavicPilots](https://mavicpilots.com/threads/lrf-and-srt-files.118171/post-1333525)) **[non ufficiale]**.
- GoPro spezza le registrazioni lunghe in capitoli da ~4 GB; nessun software GoPro li unisce e un concat ffmpeg può perdere la telemetria GPMF ([Trek View](https://www.trekview.org/blog/join-gopro-chaptered-split-video-files-preserve-telemetry/)).
- Insta360 vecchi (X3, X2, ONE X a 5.7K): due file `_00_` e `_10_` per ogni clip; cancellarne uno rende impossibile la cucitura ([manuale Insta360](https://onlinemanual.insta360.com/x4air/en-us/operating-tutorials/storage/file-format)).

### 1.10 Strumenti frammentati o in bilico (bassa, ma è lo spazio di mercato)
- **Final Cut Library Manager** è passato a Hedge e si chiama **Arctic** (49 $, il vecchio non è più aggiornato) ([Hedge blog](https://hedge.co/blog/a-new-home-for-final-cut-library-manager)); un recensore avverte di non cancellare gli ottimizzati alla leggera ([Larry Jordan](https://larryjordan.com/articles/product-review-final-cut-library-manager/)).
- **Hedge** è diventato **OffShoot** nel 2023 (copia verificata, ASC MHL) ([Newsshooter](https://www.newsshooter.com/2023/10/04/hedge-becomes-offshoot/)).
- **Kyno**: acquistato da Signiant nel 2021, ultimo aggiornamento noto 1.8.5 fine 2021, "in limbo" ([ProVideo Coalition](https://www.provideocoalition.com/adobe-prelude-is-end-of-life-bridge-still-there-kyno-in-limbo/)); Adobe Prelude chiuso.
- **PostLab** (Hedge) gestisce collaborazione FCP e documenta come spostare media e cache fuori dalla libreria ([PostLab docs](https://docs.hedge.video/postlab/faq/how-do-i-move-my-media-and-or-cache-outside-my-fcp-library)).
- Nessuno di questi fa insieme: catalogo di 40–100 TB su dischi offline + lettura di FCP/Resolve/Premiere per sapere cosa è usato + pulizia sicura.

---

## 2. Cosa è rigenerabile e cosa no

Regola generale: **è rigenerabile solo se l'originale esiste ed è raggiungibile**. Prima di proporre la cancellazione di un proxy o di un file ottimizzato, RawLine Space deve verificare che l'originale corrispondente sia presente (e possibilmente su un altro disco di backup).

### Final Cut Pro (pacchetto `.fcpbundle`)

| Contenuto | Rigenerabile? | Fonte |
|---|---|---|
| Render Files | **Sì**, "can always regenerate render files from original media" | [Apple 119914](https://support.apple.com/en-qa/119914) |
| Ottimizzati (Transcoded Media / High Quality Media) | **Sì**, se l'originale esiste | [Apple, ottimizzati e proxy](https://support.apple.com/en-qa/guide/final-cut-pro/verb8e5f6fd/mac) |
| Proxy (Transcoded Media / Proxy Media) | **Sì**, se l'originale esiste; **No** in librerie "solo proxy" o con originali mancanti | come sopra; [Apple Community 254866395](https://discussions.apple.com/thread/254866395) |
| Analysis Files, miniature, forme d'onda | Sì, Final Cut li ricrea **[non ufficiale]** | [Creative COW / forum] |
| Original Media **gestiti** (copiati nella libreria) | **No**: sono il girato | — |
| Original Media **esterni** (link simbolici) | Il link no, il file sta fuori: non toccare il file di destinazione | [Larry Jordan 10.1.2](https://larryjordan.com/articles/fcp-x-10-1-2-whats-new-in-media-management/) |
| `.mov` re-incapsulati da MP4 Sony (`(fcp1)`) | No dentro FCP (sono gli originali per la libreria), anche se la MP4 sulla scheda esiste | [Apple Community 256136664](https://discussions.apple.com/thread/256136664) |
| Database (`CurrentVersion.fcpevent`, `Settings.plist`, ecc.) | **No** | — |
| Motion Templates e LUT personalizzati nella libreria | **No** | — |
| Final Cut Backups (`~/Movies/Final Cut Backups`) | No, ma contengono **solo il database**, non i media | [Apple Community 254866395](https://discussions.apple.com/thread/254866395) |

Avvertenza ufficiale: "Elimina file generati" agisce **anche sui media esterni** (proxy e ottimizzati salvati fuori dalla libreria) ([Apple](https://support.apple.com/en-qa/guide/final-cut-pro/verb8e5f6fd/mac)).

### DaVinci Resolve

| Contenuto | Rigenerabile? | Fonte |
|---|---|---|
| CacheClip (render cache, `.dvcc`) | **Sì**; svuotarla fa rigenerare anche le forme d'onda | [Blackmagic Forum p=749669](https://forum.blackmagicdesign.com/viewtopic.php?p=749669) **[da riassunto]** |
| OptimizedMedia | **Sì**, se l'originale esiste; Resolve torna al sorgente | [Beginners Approach](https://beginnersapproach.com/davinci-resolve-delete-optimized-media/) **[non ufficiale]** |
| ProxyMedia generati da Resolve | **Sì**, se l'originale esiste | [Frame.io workflow](https://workflow.frame.io/guide/resolve-proxies) **[non ufficiale]** |
| Project Library / Disk Database | **No**: contiene tutti i progetti | [Larry Jordan](https://larryjordan.com/articles/how-i-lost-all-my-davinci-resolve-projects-and-how-you-can-save-yours/) |
| Resolve Project Backups (`~/Movies/Resolve Project Backups`) | No (ma senza media) | come sopra |
| Gallery (fermi immagine di riferimento, PowerGrade) | **No** | — (da verificare sul manuale) |
| `.drp` esportati | No (piccoli, solo progetto) | [Larry Jordan](https://larryjordan.com/articles/managing-projects-in-davinci-resolve-backups-exports-and-archives/) |
| `.dra` archivi | No (contengono media e progetto: sono un archivio) | come sopra |

**Da verificare sul manuale ufficiale Blackmagic** (non raggiunto in questa ricerca): nomi esatti delle cartelle in Resolve 20/21 e cosa contiene la cache di Fusion.

### Premiere Pro

| Contenuto | Rigenerabile? | Fonte |
|---|---|---|
| Media Cache (`.cfa`, `.pek`, `.ims`), anche se salvati accanto agli originali | **Sì**, "recreated automatically whenever source media requires them" | [Adobe helpx, media cache](https://helpx.adobe.com/au/premiere/desktop/troubleshooting/media-issues/automatically-manage-your-media-cache-files.html) |
| Preview Files (render) | **Sì** | [Adobe Community](https://community.adobe.com/t5/premiere-pro-discussions/is-it-safe-to-delete-preview-files-folders/m-p/5339900) |
| Proxy generati da Premiere | Sì, se l'originale esiste | — |
| `.prproj` e Auto-Save | **No** | — |
| Media copiati da Project Manager | No (sono copie di originali: possibili doppioni) | [Adobe helpx Project Manager](https://helpx.adobe.com/hk_en/premiere-pro/using/trim-or-copy-project.html) |

Adobe: non cancellare la cache a mano con Premiere aperto.

### File di camera

| File | Rigenerabile? |
|---|---|
| GoPro `.LRV`, `.THM` | Sì (anteprime per l'app Quik) |
| DJI `.LRF` | Sì (proxy) |
| DJI `.SRT` | **No**: telemetria del volo |
| Insta360 `LRV_` | Sì su desktop, serve all'app mobile |
| Insta360 `.insv` `_00_` e `_10_` | **No**, servono entrambi |
| Sony proxy in `Sub` / Canon proxy | Rigenerabili come contenuto ma non come file di camera con stesso nome e timecode: trattare come "da tenere" se la struttura della scheda è integra |
| XML Sony, `MEDIAPRO.XML`, `INDEX.MIF`, `.CIF`, `.SIF` Canon | **No** (si possono a volte ricostruire con software del produttore, ma con perdita) |

---

## 3. Struttura delle schede che non va rotta

Nota: alcuni dettagli qui sotto (sottocartelle `SUB`, `THMBNL`, `STATUS.BIN` Sony; contenuto di `XDROOT`; prefissi GoPro `GX`/`GH`; percorsi DJI e Canon EOS R) vengono da conoscenza pregressa e non sono stati ricontrollati in questa ricerca: vanno verificati su schede vere prima di scrivere il codice.

Regola: **la scheda si tratta come un'unità indivisibile**. Copiare, spostare o rinominare solo l'interno rompe il riconoscimento negli strumenti del produttore e nei browser dei montaggi.

- **Sony XAVC S / XAVC HS (Alpha, FX)**: `PRIVATE/M4ROOT/` con `CLIP/` (MP4 + **XML per ogni clip** con timecode e metadati), `SUB/` (proxy), `THMBNL/`, `MEDIAPRO.XML`, `STATUS.BIN`; impostazioni in `PRIVATE/SONY/SETTING/`. Le registrazioni AVCHD stanno in `PRIVATE/AVCHD/`. ([wolfcrow](https://wolfcrow.com/file-organization-and-metadata/); [CatDV](https://catdv-docs.services.quantum.com/player-technologies/Camera-formats,-containers,-and-codecs.html))
- **Sony XDCAM / XAVC professionale**: `XDROOT/` (Clip, Sub, Edit, General, `MEDIAPRO.XML`, `DISCMETA.XML`) o la vecchia `BPAV/` (XDCAM EX). Premiere non riconosce cartelle unite senza `DISCMETA` ([Adobe Community](https://community.adobe.com/questions-729/merge-sony-folder-structure-from-two-cards-so-that-premiere-media-browser-recognizes-them-1372171)).
- **Canon XF / Cinema EOS (XF-AVC, MXF)**: `CONTENTS/CLIPS001/<clip>/` con `.MXF`, `.XML`, `.SIF`, `.CIF` e `INDEX.MIF`. Copiare tutta `CONTENTS` intatta. Cinema RAW Light (`.CRM`): **struttura non verificata** in questa ricerca.
- **Canon foto-ibride (EOS R)**: `DCIM/100CANON/` con `.MP4`/`.MOV` e `.CR3`; per i video XF-AVC su R5 C/R5 usare la logica `CONTENTS`.
- **DJI**: `DCIM/100MEDIA/` (o `DJI_001`), `DJI_xxxx.MP4` + `.SRT` (telemetria, da tenere) + `.LRF` (proxy); il nome base lega i tre file.
- **GoPro**: `DCIM/100GOPRO/`, `GX010001.MP4` (H.265) o `GH010001.MP4` (H.264): le prime due cifre sono il **capitolo**, le ultime quattro il clip; `.LRV` e `.THM` d'accompagnamento; telemetria GPMF **dentro** l'MP4.
- **Insta360**: `DCIM/Camera01/`, `VID_AAAAMMGG_HHMMSS_<lente><master/proxy>_<seq>.insv`, `LRV_...`, `IMG_...insp`/`.dng`. Le cifre dopo l'ora indicano lente (0 posteriore, 1 frontale) e master/proxy (0/1) ([manuale Insta360](https://onlinemanual.insta360.com/x4air/en-us/operating-tutorials/storage/file-format)).

---

## 4. Requisiti concreti per RawLine Space

### Sicurezza (in linea con la regola "anteprima, conferma, giornale, annulla")
1. **Mai cancellare un proxy, un ottimizzato o una cache senza aver trovato l'originale corrispondente**, verificato per dimensione e durata (meglio: hash o confronto del contenuto) e presente su almeno un altro volume. Se l'originale manca, il proxy diventa "unica copia" e va messo tra i file da proteggere, con un avviso esplicito.
2. **Non toccare mai l'interno di un `.fcpbundle`** se non con lo stesso effetto di "Elimina file generati": solo `Render Files`, `Transcoded Media` (con la verifica del punto 1), `Analysis Files`. Mai `Original Media`, database, Motion Templates. Proporre in alternativa di farlo da Final Cut.
3. **Riconoscere il database di Resolve** (cartella con `Project.db`/struttura della Project Library, o connessione PostgreSQL) e le cartelle `Resolve Project Backups`, `Final Cut Backups`, Auto-Save di Premiere: etichetta "progetti, non cache", mai proposte per la pulizia.
4. **Riordinare senza mandare offline**: prima di spostare un file, sapere quali progetti lo usano; dopo lo spostamento, offrire un rapporto "progetti che puntano ai vecchi percorsi" con istruzioni di ricollegamento, oppure lasciare i file dove sono e riordinare solo il catalogo. Valutare la creazione di una mappa vecchio→nuovo percorso esportabile.
5. **Unità indivisibili**: riconoscere le strutture delle schede (sezione 3) e trattarle come blocchi: si spostano, copiano, archiviano intere. Mai proporre di "prendere solo gli MP4". Segnalare le schede **già rotte** (MP4 Sony senza XML, MXF Canon senza `CONTENTS`) come problema da conoscere.
6. **Gruppi di file d'accompagnamento**: legare per nome base DJI `.MP4/.SRT/.LRF`, GoPro capitoli + `.LRV/.THM`, Insta360 `_00_/_10_` + `LRV_`. Lo `.SRT` DJI e la coppia `.insv` sono "da tenere".

### Lettura dei progetti (sola lettura, offline)
7. **Final Cut**: leggere la libreria in sola lettura (database SQLite interno e/o FCPXML esportato) per sapere quali clip sono usati nei progetti e con quali intervalli. Non aprire la libreria con permessi di scrittura, e avvisare se Final Cut ha la libreria aperta.
8. **DaVinci Resolve**: il progetto non è un file; opzioni: leggere `.drp` esportati, leggere il database su disco in sola lettura, o importare FCPXML/EDL esportati dall'utente. Lo scripting API richiede Resolve aperto: utile come opzione, non come base.
9. **Premiere**: il `.prproj` è XML compresso con gzip: leggibile in sola lettura senza Premiere.
10. Con questi dati: classificare il girato in **usato in una consegna / usato solo in bozze / mai usato**, e solo per l'ultima categoria proporre l'alleggerimento, sempre con conferma.

### Doppioni
11. Tre livelli: **identici** (hash), **stesso contenuto, contenitore diverso** (re-wrap .mov di FCP con `(fcp1)`, MP4 della scheda: confrontare durata, timecode, numero di fotogrammi e hash del flusso video), **derivati** (proxy, ottimizzati, transcodifiche ProRes, capitoli GoPro uniti).
12. Per ogni gruppo di doppioni mostrare **a quale copia puntano i progetti** e quale sta dentro una struttura di scheda integra; la copia "master" proposta è quella completa di XML e file d'accompagnamento.
13. Funzionare su dischi **scollegati**: il catalogo deve ricordare cosa c'era su ogni disco (40–100 TB non sono mai tutti collegati insieme).

### Dopo la consegna
14. Profilo "archivia progetto consegnato": tenere consegne, progetti, asset personalizzati, girato usato con le sue strutture intere, telemetria; proporre come rimovibili render, cache, ottimizzati e proxy con originale verificato; il girato mai usato solo come proposta separata e reversibile (spostamento in un'area di quarantena, non cancellazione).
15. Rapporto stampabile prima/dopo con lo spazio liberabile per categoria e il rischio di ciascuna.

### Copia verificata
16. Quando RawLine Space copia o sposta girato tra dischi: verifica con checksum (xxHash64) e possibilmente MHL compatibile ASC MHL, come fa OffShoot, per non introdurre corruzioni silenziose.

---

## 5. Fonti

**Ufficiali**
- Apple, Se ti serve più spazio per una libreria Final Cut Pro: https://support.apple.com/en-qa/119914
- Apple, Creare file ottimizzati e proxy: https://support.apple.com/en-qa/guide/final-cut-pro/verb8e5f6fd/mac
- Apple, Icone di avviso in Final Cut Pro: https://support.apple.com/en-za/guide/final-cut-pro/verd1f977a7/mac
- Adobe, Gestione automatica della media cache: https://helpx.adobe.com/au/premiere/desktop/troubleshooting/media-issues/automatically-manage-your-media-cache-files.html
- Adobe, Consolidare, transcodificare, archiviare: https://helpx.adobe.com/hk_en/premiere-pro/using/trim-or-copy-project.html
- Sony, manuale PXW-FS5 p.158: https://www.manualslib.com/manual/1037099/Sony-Pxw-Fs5.html?page=158
- Insta360, formati dei file: https://onlinemanual.insta360.com/x4air/en-us/operating-tutorials/storage/file-format
- Hedge/OffShoot, verifica: https://docs.hedge.video/offshoot/features/verification
- Hedge, Final Cut Library Manager diventa Arctic: https://hedge.co/blog/a-new-home-for-final-cut-library-manager
- PostLab, media e cache fuori dalla libreria: https://docs.hedge.video/postlab/faq/how-do-i-move-my-media-and-or-cache-outside-my-fcp-library

**Forum e articoli**
- Apple Community, 5 GB → 264 GB (2025): https://discussions.apple.com/thread/256008995
- Apple Community, libreria 10× gli originali: https://discussions.apple.com/thread/254262438
- Apple Community, spazio dopo i render: https://discussions.apple.com/thread/253106233
- Apple Community, proxy senza originali: https://discussions.apple.com/thread/254866395
- Apple Community, re-wrap MP4 Sony in .mov (2025): https://discussions.apple.com/thread/256136664
- Apple Community, libreria spostata, media offline: https://discussions.apple.com/thread/254726346
- Larry Jordan, perché i file vanno offline: https://larryjordan.com/articles/fcp-x-why-files-go-offline/
- Larry Jordan, Consolidate: https://larryjordan.com/articles/fcp-x-consolidate-media-and-libraries/
- Larry Jordan, FCP 10.1.2 media management: https://larryjordan.com/articles/fcp-x-10-1-2-whats-new-in-media-management/
- Larry Jordan, progetti Resolve persi (2024): https://larryjordan.com/articles/how-i-lost-all-my-davinci-resolve-projects-and-how-you-can-save-yours/
- Larry Jordan, backup ed export Resolve: https://larryjordan.com/articles/managing-projects-in-davinci-resolve-backups-exports-and-archives/
- Larry Jordan, recensione Final Cut Library Manager: https://larryjordan.com/articles/product-review-final-cut-library-manager/
- Blackmagic Forum, CacheClip: https://forum.blackmagicdesign.com/viewtopic.php?p=749669
- Blackmagic Forum, database spariti: https://forum.blackmagicdesign.com/viewtopic.php?p=918735
- Blackmagic Forum, Media Management e timeline: https://forum.blackmagicdesign.com/viewtopic.php?p=1150366
- Adobe Community, Project Manager consolida e transcodifica: https://community.adobe.com/t5/premiere-pro-bugs/project-manager-consolidate-and-transcode-problems/idi-p/9260441
- Adobe Community, originali spariti: https://community.adobe.com/t5/premiere-pro-discussions/premiere-pro-deleted-all-of-my-original-video-files-for-good-over-18-hours-of-editing-and-priceless/m-p/11777302
- Adobe Community, cartelle Sony unite: https://community.adobe.com/questions-729/merge-sony-folder-structure-from-two-cards-so-that-premiere-media-browser-recognizes-them-1372171
- Peachpit, Project Manager: https://www.peachpit.com/articles/article.aspx?p=3113584&seqNum=3
- DVinfo, EX1 MP4 orfani: https://www.dvinfo.net/forum/sony-xdcam-ex-pro-handhelds/124349-ex1-orphaned-mp4-files-solved.html
- DVinfo, solo MP4: https://dvinfo.net/forum/sony-xdcam-ex-pro-handhelds/486257-missing-support-files-help-only-mp4s.html
- DVinfo, C300: https://www.dvinfo.net/forum/canon-cinema-eos-camera-systems/517294-how-rescue-c300-files.html
- DVinfo, copia Canon XF: https://www.dvinfo.net/forum/canon-xf-series-4k-hd-camcorders/489175-cant-open-files-hdd-copy.html
- wolfcrow, organizzazione file Sony: https://wolfcrow.com/file-organization-and-metadata/
- CatDV, formati di camera: https://catdv-docs.services.quantum.com/player-technologies/Camera-formats,-containers,-and-codecs.html
- Trek View, capitoli GoPro e telemetria: https://www.trekview.org/blog/join-gopro-chaptered-split-video-files-preserve-telemetry/
- MavicPilots, LRF e SRT: https://mavicpilots.com/threads/lrf-and-srt-files.118171/post-1333525
- ProVideo Coalition, Kyno in limbo: https://www.provideocoalition.com/adobe-prelude-is-end-of-life-bridge-still-there-kyno-in-limbo/
- Newsshooter, Hedge diventa OffShoot: https://www.newsshooter.com/2023/10/04/hedge-becomes-offshoot/
- Beginners Approach, ottimizzati Resolve: https://beginnersapproach.com/davinci-resolve-delete-optimized-media/
- Frame.io, proxy Resolve: https://workflow.frame.io/guide/resolve-proxies
