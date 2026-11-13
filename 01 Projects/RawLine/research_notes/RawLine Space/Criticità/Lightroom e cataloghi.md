# Criticità: gestione dei file nei cataloghi (Lightroom Classic, Capture One, Bridge/ACR, Photo Mechanic Plus, Apple Foto)

Ricerca dell'11 novembre 2026 per RawLine Space. Fonti: forum Adobe Community, supporto Capture One, Camera Bits, Apple Discussions, Lightroom Queen, Fred Miranda, blog. Reddit, DPReview, MacRumors e il forum Leica hanno risposto 403 alla lettura diretta: per quelle fonti ci sono solo i titoli e gli estratti dei risultati di ricerca.

Legenda per ogni criticità: **Fonti** = quante fonti indipendenti la confermano (thread o autori diversi); **Recente** = se ci sono casi del 2023–2026.

---

## 1. Criticità in ordine di gravità

### 1.1 Spostare o rinominare fuori dal catalogo rompe i collegamenti, e il "rimedio" sbagliato cancella gli sviluppi
**Descrizione.** In Lightroom Classic, Capture One e Apple Foto (librerie referenziate) il catalogo conserva il percorso del file. Se si sposta, rinomina o copia nel Finder, o se cambia il nome o l'ID del volume, le foto risultano "mancanti" o "offline". Gli sviluppi stanno nel catalogo e non sono persi. Lo diventano quando la persona, spaventata, fa "Rimuovi foto mancanti", reimporta o sincronizza la cartella: così perde sviluppi, raccolte e copie virtuali.
**Casi reali.**
- Ricollegamento di 65.000 file dopo un guasto RAID: un esperto consiglia di lasciarlo andare tutta la notte ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/lrcc-recovery-from-raid-failure/m-p/11848168)).
- 14.000 foto mancanti dopo il passaggio a un nuovo disco esterno: thread del 2022 riaperto a dicembre 2024 e ancora senza soluzione ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/missing-photos-after-moving-to-new-external-drive/m-p/15047037)).
- Un utente dice di aver "desincronizzato" le cartelle e perso tutti gli sviluppi in corso, nel 2025–2026 ([Adobe](https://community.adobe.com/questions-675/i-managed-to-desync-my-folders-from-lightroom-classic-and-have-lost-all-my-edits-in-progress-and-edits-made-ready-for-export-is-there-a-way-to-restore-this-1625929)).
- Il consiglio ricorrente degli esperti: "Do NOT import photos. Do NOT do a Folder synchronize" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/move-folder-from-1-ssd-to-another-within-lrc-2-of-3-subfolders-disappeared/td-p/15591057)). Reimportare è "almost never the answer" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/frustration-and-secondhand-embarrassment-recreating-catalog-on-macos-sonoma/td-p/14639895)).
- Apple Foto con file referenziati: il collegamento dipende dall'ID del volume e non dal nome, quindi si rompe quando il disco passa su un altro Mac ([Apple](https://discussions-cn-prz.apple.com/thread/252741972)).
- Capture One: dopo il trasferimento su un nuovo disco tutte le immagini risultano "offline". Il comando Locate a volte è grigio o ricollega solo una parte, e il percorso salvato nel database cambia formato tra Mac e Windows ([C1](https://support.captureone.com/hc/de/community/posts/360013471098-All-images-appear-offline-after-copying-the-whole-catalog-to-an-external-drive), [C1](https://support.captureone.com/hc/fr/community/posts/360012387438-Offline-Images)). Esiste una richiesta utenti di un "batch locate" ([C1](https://support.captureone.com/hc/fr/community/posts/15871871424669-Relinking-missing-lost-images-in-the-catalog-to-the-new-location-on-a-hard-drive-create-a-batch-locate-option)).

**Diffusione.** È il problema più frequente in assoluto: decine di thread ogni anno, al punto che Adobe ha una pagina di aiuto dedicata ([Adobe help](https://helpx.adobe.com/lightroom-classic/desktop/manage-catalogs-and-files/locate-missing-photos.html)).
**Fonti:** oltre 10 indipendenti. **Recente:** sì, dal 2024 al 2026.

### 1.2 Lo spostamento fatto dentro Lightroom perde file per davvero
**Descrizione.** Il consiglio ufficiale è spostare le cartelle da dentro Lightroom, ma ci sono casi in cui lo spostamento tra dischi si interrompe a metà e alcune sottocartelle spariscono da entrambi i dischi.
**Casi reali.**
- 14 novembre 2025, LrC 15.0.1: trascinata una cartella con 3 sottocartelle da un SSD a un altro. Solo la prima sottocartella è arrivata, le altre due non sono più su nessuno dei due dischi. L'utente ha dovuto recuperarle dal backup. Un esperto scrive che il problema "è segnalato da un decennio" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/move-folder-from-1-ssd-to-another-within-lrc-2-of-3-subfolders-disappeared/td-p/15591057)).
- Altri thread: "Lightroom has lost files while moving to another folder" ([Adobe](https://community.adobe.com/questions-675/lightroom-has-lost-files-while-moving-to-another-folder-982938)), "Lost files on trying to move between LrC folders" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/lost-files-on-trying-to-move-between-lrc-folders/td-p/13057201)), "RAW images being deleted without correctly migrating" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/raw-images-being-deleted-without-correctly-migrating-files-to-new-location/td-p/12761805)).

**Diffusione.** È raro, ma è il caso peggiore: perdita fisica dei file causata da uno spostamento non verificato, cioè cancellare l'origine prima di aver controllato la copia.
**Fonti:** 4 thread. **Recente:** sì (2025).

### 1.3 Cataloghi corrotti e sviluppi spariti dopo un aggiornamento
**Descrizione.** Cataloghi segnalati come corrotti, anche più volte al giorno, dopo un aggiornamento di LrC o di macOS. Sviluppi che spariscono con la cronologia ancora intatta. Errori dell'archivio delle modifiche AI (`.lrcat-data`). La riparazione toglie la cronologia degli sviluppi e il backup può essere troppo vecchio o corrotto anche lui.
**Casi reali.**
- LrC 14.0.1 su macOS 15: cinque cataloghi su cinque SSD esterni si corrompono ogni giorno, da ottobre 2024 a febbraio 2025. La soluzione accettata è creare un catalogo nuovo e importare il vecchio. Per un altro utente non ha funzionato. Dopo la riparazione "edits remained but the history was gone" ([Adobe](https://community.adobe.com/questions-675/catalogs-keep-getting-corrupted-every-single-day-v14-0-1-macos-15-979218)).
- Corruzione con la versione 15 e corruzioni ripetute ([Adobe](https://community.adobe.com/questions-675/lightroom-classic-v15-corrupted-catalog-983855), [Adobe](https://community.adobe.com/questions-675/repeated-corrupt-catalogs-983153)).
- LrC 14.4: gli sviluppi sui JPEG scompaiono, i cursori tornano a zero ma la cronologia è presente. Un backup della 14.3.1 li mostra correttamente ([Adobe](https://community.adobe.com/questions-675/jpeg-edits-disappear-after-update-history-intact-sliders-reset-982657)).
- "Failed to initialize AI edits storage": maschere AI a rischio. Su un catalogo da 359.000 foto, il controllo di integrità e l'ottimizzazione non segnalano nulla ([Adobe](https://community.adobe.com/questions-675/p-failed-to-initialize-ai-edits-storage-983966)).
- Capture One: un utente ha corrotto il catalogo due volte a metà di 60.000 immagini. Le corruzioni avvengono soprattutto alla chiusura forzata ([C1](https://support.captureone.com/hc/fr/community/posts/17779116673181-Catalogue-performance-issues)).
- Apple Foto: una libreria da circa 1 TB su disco esterno non si apre più, e "a backup of a corrupted library is also corrupted" ([Apple](https://discussions-cn-prz.apple.com/thread/256132130), [Apple](https://discussions.apple.com/thread/256112660)).

**Diffusione.** Alta e ciclica: ogni versione maggiore di LrC (14, 15) porta una nuova ondata di segnalazioni.
**Fonti:** oltre 8. **Recente:** sì (2024–2026).

### 1.4 XMP e catalogo non sincronizzati: conflitti a migliaia e sidecar persi
**Descrizione.** Il catalogo e i sidecar XMP divergono. LrC segnala "conflitto" o "modificato su disco" anche senza alcuna modifica. Bridge e ACR possono staccare o cancellare l'XMP quando si rinomina o si elimina un file. Le differenze di maiuscole/minuscole (`.xmp` contro `.XMP`, `arw` contro `ARW`) bastano a rompere l'associazione.
**Casi reali.**
- Agosto–novembre 2026, LrC 15.6: catalogo da 109.000 foto con 21.030 "Conflict Detected" e 22.480 "Not Up to Date". Ogni uscita dal programma riscrive gli XMP per minuti. Causa individuata da un utente: `SidecarForExtension` scritto in minuscolo contro maiuscolo. Un altro utente ha un catalogo da oltre 200.000 foto con lo stesso problema. Stato del bug: "Investigating" ([Adobe](https://community.adobe.com/bug-reports-674/p-lightroom-classic-repeatedly-detects-metadata-conflicts-and-writes-xmp-changes-when-no-edits-were-made-1635848)).
- Luglio 2026, Bridge 16.0.5 su macOS 26: eliminando un JPEG con lo stesso nome di un RAW, Bridge cancella anche l'XMP del RAW e gli sviluppi ACR vanno persi ([Adobe](https://community.adobe.com/bug-reports-557/bridge-deletes-the-sidecar-xmp-file-associated-with-a-raw-file-when-a-another-file-with-similar-name-but-different-type-is-deleted-1632752)).
- La rinomina in blocco di Bridge stacca o cancella gli XMP dei RAW ([Adobe](https://community.adobe.com/t5/bridge-discussions/bridge-s-batch-rename-is-causing-loss-of-connection-to-xmp-data/m-p/15382537), [Adobe](https://community.adobe.com/questions-558/batch-rename-deleted-xmp-files-for-raw-photos-178108)).
- LrC 14.1 non scrive più l'XMP in automatico ([Adobe](https://community.adobe.com/questions-675/lr-classic-14-1-doesn-t-automatically-save-xmp-metadata-980682)). Con "scrivi automaticamente XMP" attivo, invece, la versione 15 diventa lenta, e Adobe suggerisce di disattivarlo ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-v15-0-amp-later-slow-in-develop-and-library-module-operations/m-p/15575633)).
- Su NAS la marca temporale del catalogo non coincide con quella dell'XMP, e i conflitti diventano permanenti ([Adobe](https://community.adobe.com/t5/lightroom-classic-bugs/p-wrong-timestamp-stored-in-catalog-causing-wrong-metadata-status-all-windows-versions/m-p/12262366)).

**Diffusione.** Alta per chi usa più programmi (Photo Mechanic, Bridge e LrC), cioè proprio i professionisti.
**Fonti:** 7 o più. **Recente:** sì (2025–2026).

### 1.5 Photo Mechanic Plus chiuso: archivi catalogati senza via d'uscita
**Descrizione.** Il 27 febbraio 2026 (aggiornato il 2 marzo) Camera Bits ha tolto dalla vendita Photo Mechanic Plus. Motivo: la tecnologia di terze parti su cui si basa il catalogo "is actively breaking Photo Mechanic Plus for most users". Non esiste uno strumento di migrazione, solo "continue to investigate possible migration plans". Il supporto dura "for as long as it remains stable" sul sistema operativo in uso. Secondo una fonte di terze parti, Plus non funzionerà più su Apple Silicon quando finirà Rosetta ([Camera Bits](https://home.camerabits.com/photo-mechanic-plus-is-no-longer-available-for-purchase/), [imagic](https://imagic.ink/blog/is-photo-mechanic-worth-buying-2026)).
**Casi reali.**
- Un fotogiornalista con un archivio su NAS di circa 700.000 immagini: il primo import in Excire ha caricato quasi 2 milioni di file, compresi RAW doppi ed export JPEG di Lightroom. Ha dovuto fermarsi e ripartire. Excire per lui non è un sostituto ("a search-and-cull tool"), quindi resta su PM+ finché funziona ([Storyteller, set. 2026](https://picturestoryteller.com/2026/09/08/photo-mechanic-plus-is-gone-heres-what-im-using-instead/)).
- Sul forum Camera Bits un utente scrive che non c'è alternativa a Plus che soddisfi le sue aspettative ([Camera Bits forum](https://forums.camerabits.com/index.php?topic=15937.120)). Sul forum Leica si discute del "demise" di PM+ e si valutano digiKam, NeoFinder e Capture One ([Leica forum](https://www.l-camera-forum.com/topic/428024-photo-catalogues-dam-the-potential-demise-of-photo-mechanic-plus/), solo estratto).
- La strategia di uscita consigliata è "Save Metadata to Files" negli XMP ([DPReview](https://www.dpreview.com/forums/threads/photo-catalog-software-options.4835355/), solo estratto).

**Diffusione.** Riguarda una nicchia (fotogiornalisti e sport) con archivi molto grandi. Non ho trovato proteste di massa, ma tanta incertezza.
**Fonti:** 5 (1 ufficiale, 4 di utenti). **Recente:** sì (2026).
**Lezione.** Un catalogo proprietario è un rischio di blocco: quando il software muore, le informazioni devono vivere fuori.

### 1.6 Lentezza con centinaia di migliaia di foto
**Descrizione.** Oltre 200.000–500.000 foto, LrC e Capture One rallentano molto: aperture lunghe, import di ore che usano 1–2 core, anteprime che richiedono settimane.
**Casi reali.**
- Catalogo da 540.000 immagini (6 GB) su una macchina con 192 GB di RAM e RAID NVMe: rigenerare le anteprime richiederebbe "3-4 weeks". Un import da 1 TB è fallito dopo 4 notti ([Adobe, 2024–2025](https://community.adobe.com/t5/lightroom-classic-discussions/performance-slow-on-large-catalog-540k-images/td-p/14868732)).
- Circa 500.000 foto con NAS a 10GbE: un import durava 16 ore, in un catalogo nuovo meno di 30 minuti (giugno 2025, stesso thread).
- 207.000 immagini: 49 minuti per caricare la Libreria (novembre 2024, stesso thread).
- Capture One con 900.000 foto: 10 minuti per aprire e circa un minuto per ogni clic. 500 file nel cestino in 15 minuti ([C1](https://support.captureone.com/hc/fr/community/posts/17779116673181-Catalogue-performance-issues)).
- Apple Foto: le librerie grandi aprono e chiudono lentamente, e la ricerca dei doppioni impiega oltre un giorno su 7.500 foto ([Apple](https://discussions.apple.com/thread/255909786), [Apple](https://discussions.apple.com/thread/256063315)).

**Diffusione.** È proprio la scala di RawLine Space (40–100 TB), dove la risposta comune è "dividi in più cataloghi", che però produce la criticità 1.7.
**Fonti:** 6 o più. **Recente:** sì (2024–2025).

### 1.7 Più cataloghi, doppioni e cartelle duplicate
**Descrizione.** Per lentezza o per abitudine si creano più cataloghi: uno per anno, uno per portatile, uno per lavoro. Unirli genera copie virtuali e doppioni. LrC riconosce i doppioni solo dentro lo stesso catalogo e solo se identici byte per byte. Lo stesso NAS compare due volte nel pannello Cartelle (lettera di unità contro percorso UNC, oppure NAS sostituito con lo stesso nome).
**Casi reali.**
- Unendo cataloghi che contengono le stesse foto, l'import crea copie virtuali: "one master file but multiple develop histories" ([Lightroom Queen](https://www.lightroomqueen.com/community/threads/resolving-differences-between-two-catalogs.52272/), [Lightroom Queen](https://www.lightroomqueen.com/merging-catalogs-overview/)).
- La vista Doppioni di LrC trova solo dati immagine identici. I file rinominati o con metadati cambiati sfuggono all'import ([Adobe help](https://helpx.adobe.com/lightroom-classic/desktop/organize-photos-in-lightroom-classic/find-and-manage-duplicate-photos.html), [Adobe](https://community.adobe.com/questions-675/is-there-a-way-for-lr-to-recognize-duplicates-in-import-when-just-the-file-name-differs-974902)).
- Lo stesso disco appare due volte in LrC ([Adobe](https://community.adobe.com/questions-675/same-drive-shown-twice-in-lightroom-classic-967325)). Con una Synology, ogni import crea due cartelle simili ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/problem-with-import-new-photos-from-synology-nas-get-two-similar-folders-in-lightroom/m-p/12048399)).
- Il caso dei 2 milioni di file in Excire con RAW doppi ed export (vedi 1.5).
- Apple Foto: unire due librerie fa perdere video (72 diventano 57) e la funzione Doppioni ne trova solo una parte ([Apple](https://discussions.apple.com/thread/256063315)).

**Fonti:** 7 o più. **Recente:** in parte (2024–2026; i casi Synology sono più vecchi).

### 1.8 NAS e migrazioni tra dischi o sistemi
**Descrizione.** Adobe "ufficialmente" non supporta il catalogo su NAS. Le foto sul NAS funzionano, ma quando il NAS va in sospensione a ogni avvio tutte le cartelle risultano mancanti. Il passaggio da Windows a Mac rompe i percorsi (lettere di unità).
**Casi reali.**
- 130.000 foto su NAS QNAP, passaggio da Windows a macOS Sonoma: il ricollegamento fallisce sia con SMB sia con AFP, e la ricostruzione del catalogo resta ferma 2 giorni. Nessuna soluzione (maggio–giugno 2024) ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/frustration-and-secondhand-embarrassment-recreating-catalog-on-macos-sonoma/td-p/14639895)).
- Synology: centinaia di cartelle da ricollegare a ogni avvio, probabilmente per la sospensione del NAS ([Adobe, 2021](https://community.adobe.com/questions-675/synology-nas-i-have-to-relink-all-folders-every-time-i-start-lightroom-classic-why-956840)).
- Errore "Locate folder" su NAS segnalato come bug nel 2025 ([Adobe](https://community.adobe.com/t5/lightroom-classic-bugs/p-locate-folder-gt-error-is-displayed-when-tried-to-relink-the-folder-present-on-nas/idc-p/15336874)), oltre a "Find folders on NAS now failing" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/p-moved-back-to-mac-find-folders-on-nas-now-failing/m-p/15195860)).
- Con un NAS da oltre 700.000 file scollegato, LrC si apre e tutte le foto risultano "missing", ma le anteprime restano navigabili: è una cosa utile ([Adobe](https://community.adobe.com/questions-675/lightroom-classic-images-stored-on-nas-official-yes-or-no-975545)).

**Fonti:** 5 o più. **Recente:** sì (2024–2025).

### 1.9 File solo in cloud scambiati per corrotti
**Descrizione.** Le cartelle in Dropbox o iCloud impostate "solo online" fanno apparire le foto illeggibili o corrotte.
**Caso.** Catalogo da 49.705 foto di cui circa 40.000 non leggibili e 8.663 "DNG non validi". Erano segnaposto Dropbox (settembre 2024) ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-catalog-missing-40-000-photos-including-previews/m-p/14856468)).
**Fonti:** 1 caso grande più consigli ricorrenti. **Recente:** sì (2024).

### 1.10 Il malinteso sul backup: "ho il backup del catalogo"
**Descrizione.** Il backup di LrC salva solo `.lrcat` e `.lrcat-data`, non le foto. Molti lo scoprono quando ormai è tardi. Anche il `.lrcat-data` (maschere AI) è stato a lungo ignorato dai backup ([Adobe help](https://helpx.adobe.com/hu/lightroom-classic/help/back-catalog.html), [Scott Kelby](https://scottkelby.com/warning-backing-up-your-lightroom-catalog-does-not-backup-your-photos/), [Lightroom Queen](https://www.lightroomqueen.com/lightroom-catalogs-top-10-misunderstandings/), [Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/11-0-upgrade-new-catalog-lrcat-data-file-not-backed-up/td-p/12480468)).
**Fonti:** 4 o più. **Recente:** il malinteso è stabile nel tempo.

**Scartato perché vecchio o superato:** problemi di LR 6/CC 2015, iPhoto, Capture One 7–20 senza conferme recenti (citati solo come contesto), Apple Foto su dischi non APFS (problema noto e risolto formattando).

---

## 2. Cosa chiedono le persone e non trovano

1. **Ricollegamento in blocco intelligente.** Le persone vogliono indicare la nuova radice e veder ricollegati tutti i file, anche quando la struttura è cambiata, cercandoli per nome, data di scatto e dimensione. Oggi LrC ricollega solo se la gerarchia è identica, e la ricerca delle foto mancanti "only searches the catalog itself" e non i dischi. Capture One non ha un "batch locate" (richiesta aperta dagli utenti).
2. **Uno spostamento tra dischi che non possa perdere file.** Una copia verificata, e l'origine tolta solo dopo il controllo, con un registro di cosa è andato dove.
3. **Doppioni tra cataloghi, dischi e NAS diversi**, anche con nomi cambiati, metadati modificati o export JPEG del RAW, senza dover unire prima i cataloghi.
4. **Un modo per uscire da un catalogo morto** (PM+), o da uno che non si vuole più usare, senza perdere stelle, etichette, didascalie e parole chiave: un'esportazione verso XMP standard o un formato aperto.
5. **Sapere cosa c'è in un archivio prima di importarlo.** Il caso Excire con 2 milioni di file invece di 700.000 mostra che serve un'analisi preliminare: RAW, export, doppioni, sidecar.
6. **Risolvere i conflitti XMP/catalogo con un confronto chiaro**, per esempio una richiesta di confronto prima/dopo dei conflitti di metadati ([Adobe idea](https://community.adobe.com/t5/lightroom-classic-ideas/p-before-after-comparison-of-metadata-conflicts/idi-p/12249522)), invece di scegliere alla cieca tra "leggi dal file" e "sovrascrivi".
7. **Avere il catalogo "disponibile" anche con i dischi scollegati**: sfogliare e cercare sapendo su quale disco sta ogni file.
8. **Capire se un backup è davvero completo** (foto, sidecar, catalogo e dati AI), non solo il catalogo.

---

## 3. Cosa significa per RawLine Space (requisiti concreti)

**Sicurezza delle operazioni**
- R1. **Mai spostare con un "move" diretto tra volumi.** Si copia, si verifica il checksum (xxHash o SHA), si scrive il registro, e solo dopo l'origine va nel cestino o nell'area di quarantena di RawLine, mai eliminata subito. La criticità 1.2 dimostra che uno spostamento interrotto a metà fa perdere sottocartelle intere.
- R2. **Operazioni atomiche e riprendibili.** Se il disco si stacca o l'app si chiude a metà, al riavvio Space sa esattamente quali file sono già copiati e verificati e quali no, e propone di riprendere o annullare.
- R3. **Un sidecar viaggia sempre con il suo file.** RAW, `.xmp`/`.XMP`, `.acr`, `.pp3`, `.cos`/`.cot` di Capture One, `.dop`, THM e LRF dei video si spostano e si rinominano come un blocco unico, senza differenze di maiuscole. Eliminare o spostare un JPEG non deve mai toccare l'XMP del RAW con lo stesso nome (criticità 1.4, bug di Bridge del 2026).
- R4. **Non scrivere dentro cataloghi altrui** (`.lrcat`, `.cocatalog`, `.photoslibrary`, `.pmdb`). Space li legge in sola lettura, su una copia, per sapere dove sono i file e cosa contengono.

**Ricollegamento: il nostro vantaggio**
- R5. **Ogni spostamento fatto da Space produce una "mappa dei percorsi"** (vecchio → nuovo) esportabile. Da questa si genera un aiuto al ricollegamento: per LrC, l'elenco delle cartelle radice da indicare con "Trova cartella mancante" nell'ordine giusto; per Capture One, le cartelle da indicare con Locate. Così la persona non deve cercare.
- R6. **Prima di spostare, avvisare** se la cartella è referenziata da un catalogo Lightroom, Capture One, Apple Foto o PM+ trovato sul Mac: "Questa cartella è in 'Catalogo 2023.lrcat'. Dopo lo spostamento dovrai ricollegarla: ecco come". Funziona in sola lettura: il `.lrcat` è un database SQLite, con i percorsi in `AgLibraryRootFolder` e `AgLibraryFolder`.
- R7. **Ritrovare i file "mancanti" sui dischi**, non solo nel catalogo: data una lista di percorsi persi (letta dal catalogo), cercare per nome, dimensione, data di scatto e hash nell'indice di Space, che copre anche i dischi scollegati.

**Doppioni e analisi**
- R8. **Doppioni tra volumi e tra cataloghi**, su tre livelli: identico (hash), stesso scatto (data EXIF, numero di serie e contatore, dimensione) con nome diverso, derivato (export JPEG o TIFF di un RAW). Ogni doppione mostra quale copia è "usata" da un catalogo e quale no, e la copia referenziata non va mai proposta per la rimozione.
- R9. **Censimento prima di agire**: un riepilogo per cartella e per volume con RAW, export, video, sidecar, cataloghi, doppioni e file solo in cloud o segnaposto (Dropbox o iCloud "solo online": riconoscerli e non trattarli mai come corrotti).
- R10. **Riconoscere percorsi alternativi dello stesso volume** (stesso NAS montato come `smb://nome` e come IP, stesso disco con nome cambiato) usando l'UUID del volume e non il nome. Così non nascono cartelle duplicate.

**Metadati e uscita dai cataloghi**
- R11. **Leggere ed esportare i metadati da un catalogo verso XMP standard** (stelle, etichette, scelta/scarto, parole chiave, didascalie IPTC): una "via d'uscita" da PM+ e da LrC. Sempre con anteprima e scrivendo l'XMP accanto al file solo dopo conferma, con un backup dell'XMP esistente.
- R12. **Segnalare i conflitti XMP/catalogo** e quale è più recente, mostrando la differenza campo per campo, senza risolverli in automatico.

**Prestazioni e scala**
- R13. L'indice di Space deve restare reattivo con milioni di file (40–100 TB): scansione incrementale, import e analisi su più core, apertura immediata anche con i dischi scollegati (si sfoglia l'indice e le anteprime salvate).
- R14. **NAS: tollerare la sospensione e i distacchi.** Un volume assente è "non montato" e non "file eliminati". Non proporre mai pulizie basate sull'assenza di un volume.

**Backup e chiarezza**
- R15. **Verificare la "completezza" di un archivio**: per ogni lavoro, controllare se esistono RAW, sidecar, catalogo e `.lrcat-data`, e se c'è una seconda copia verificata su un altro volume. Prima di qualunque alleggerimento, dire chiaramente se il backup del catalogo da solo non contiene le foto.
- R16. **Registro persistente leggibile anche fuori dall'app** (CSV o JSON), con un annulla per ogni operazione, perché la persona deve poter ricostruire cosa è successo anche se Space non c'è più: è la lezione di PM+.

---

## 4. Fonti

**Ufficiali**
- Camera Bits, PM+ non più in vendita (27 feb 2026, agg. 2 mar 2026): https://home.camerabits.com/photo-mechanic-plus-is-no-longer-available-for-purchase/
- Adobe, Trovare le foto mancanti: https://helpx.adobe.com/lightroom-classic/desktop/manage-catalogs-and-files/locate-missing-photos.html
- Adobe, Doppioni: https://helpx.adobe.com/lightroom-classic/desktop/organize-photos-in-lightroom-classic/find-and-manage-duplicate-photos.html
- Adobe, Backup del catalogo: https://helpx.adobe.com/hu/lightroom-classic/help/back-catalog.html
- Capture One, immagini offline: https://support.captureone.com/hc/en-us/articles/360002400597
- Camera Bits, spostare un catalogo: https://docs.camerabits.com/support/solutions/articles/48001168255-moving-a-catalog

**Adobe Community (Lightroom Classic / Bridge)**
- 540.000 immagini, lentezza: https://community.adobe.com/t5/lightroom-classic-discussions/performance-slow-on-large-catalog-540k-images/td-p/14868732
- Cataloghi corrotti ogni giorno (14.0.1): https://community.adobe.com/questions-675/catalogs-keep-getting-corrupted-every-single-day-v14-0-1-macos-15-979218
- Catalogo v15 corrotto: https://community.adobe.com/questions-675/lightroom-classic-v15-corrupted-catalog-983855
- Corruzioni ripetute: https://community.adobe.com/questions-675/repeated-corrupt-catalogs-983153
- Sviluppi JPEG spariti (14.4): https://community.adobe.com/questions-675/jpeg-edits-disappear-after-update-history-intact-sliders-reset-982657
- AI edits storage: https://community.adobe.com/questions-675/p-failed-to-initialize-ai-edits-storage-983966
- Conflitti XMP senza modifiche (2026): https://community.adobe.com/bug-reports-674/p-lightroom-classic-repeatedly-detects-metadata-conflicts-and-writes-xmp-changes-when-no-edits-were-made-1635848
- Marca temporale sbagliata, conflitti: https://community.adobe.com/t5/lightroom-classic-bugs/p-wrong-timestamp-stored-in-catalog-causing-wrong-metadata-status-all-windows-versions/m-p/12262366
- LrC 14.1 non scrive XMP: https://community.adobe.com/questions-675/lr-classic-14-1-doesn-t-automatically-save-xmp-metadata-980682
- v15 lenta, XMP automatico: https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-v15-0-amp-later-slow-in-develop-and-library-module-operations/m-p/15575633
- Bridge cancella l'XMP del RAW (2026): https://community.adobe.com/bug-reports-557/bridge-deletes-the-sidecar-xmp-file-associated-with-a-raw-file-when-a-another-file-with-similar-name-but-different-type-is-deleted-1632752
- La rinomina in blocco di Bridge stacca gli XMP: https://community.adobe.com/t5/bridge-discussions/bridge-s-batch-rename-is-causing-loss-of-connection-to-xmp-data/m-p/15382537
- Lo spostamento in LrC perde sottocartelle (nov 2025): https://community.adobe.com/t5/lightroom-classic-discussions/move-folder-from-1-ssd-to-another-within-lrc-2-of-3-subfolders-disappeared/td-p/15591057
- File persi spostando in LrC: https://community.adobe.com/questions-675/lightroom-has-lost-files-while-moving-to-another-folder-982938
- RAW eliminati senza migrazione: https://community.adobe.com/t5/lightroom-classic-discussions/raw-images-being-deleted-without-correctly-migrating-files-to-new-location/td-p/12761805
- 14.000 foto mancanti dopo il cambio disco: https://community.adobe.com/t5/lightroom-classic-discussions/missing-photos-after-moving-to-new-external-drive/m-p/15047037
- Sviluppi persi dopo la desincronizzazione: https://community.adobe.com/questions-675/i-managed-to-desync-my-folders-from-lightroom-classic-and-have-lost-all-my-edits-in-progress-and-edits-made-ready-for-export-is-there-a-way-to-restore-this-1625929
- 40.000 foto Dropbox "corrotte": https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-catalog-missing-40-000-photos-including-previews/m-p/14856468
- Guasto RAID, 65.000 file da ricollegare: https://community.adobe.com/t5/lightroom-classic-discussions/lrcc-recovery-from-raid-failure/m-p/11848168
- NAS QNAP, migrazione da Windows a Mac: https://community.adobe.com/t5/lightroom-classic-discussions/frustration-and-secondhand-embarrassment-recreating-catalog-on-macos-sonoma/td-p/14639895
- Synology, ricollegare a ogni avvio: https://community.adobe.com/questions-675/synology-nas-i-have-to-relink-all-folders-every-time-i-start-lightroom-classic-why-956840
- Immagini su NAS, ufficialmente sì o no: https://community.adobe.com/questions-675/lightroom-classic-images-stored-on-nas-official-yes-or-no-975545
- Bug Locate folder su NAS: https://community.adobe.com/t5/lightroom-classic-bugs/p-locate-folder-gt-error-is-displayed-when-tried-to-relink-the-folder-present-on-nas/idc-p/15336874
- Stesso disco mostrato due volte: https://community.adobe.com/questions-675/same-drive-shown-twice-in-lightroom-classic-967325
- Synology, cartelle doppie all'import: https://community.adobe.com/t5/lightroom-classic-discussions/problem-with-import-new-photos-from-synology-nas-get-two-similar-folders-in-lightroom/m-p/12048399
- Doppioni con nome diverso: https://community.adobe.com/questions-675/is-there-a-way-for-lr-to-recognize-duplicates-in-import-when-just-the-file-name-differs-974902
- Idea: confronto prima/dopo dei conflitti: https://community.adobe.com/t5/lightroom-classic-ideas/p-before-after-comparison-of-metadata-conflicts/idi-p/12249522
- `.lrcat-data` non incluso nel backup: https://community.adobe.com/t5/lightroom-classic-discussions/11-0-upgrade-new-catalog-lrcat-data-file-not-backed-up/td-p/12480468

**Capture One (community)**
- Prestazioni del catalogo (900.000 foto, corruzioni): https://support.captureone.com/hc/fr/community/posts/17779116673181-Catalogue-performance-issues
- Tutto offline dopo la copia su un disco esterno: https://support.captureone.com/hc/de/community/posts/360013471098-All-images-appear-offline-after-copying-the-whole-catalog-to-an-external-drive
- Immagini offline, Locate grigio: https://support.captureone.com/hc/fr/community/posts/360012387438-Offline-Images
- Richiesta batch locate: https://support.captureone.com/hc/fr/community/posts/15871871424669-Relinking-missing-lost-images-in-the-catalog-to-the-new-location-on-a-hard-drive-create-a-batch-locate-option
- Ricollegare i file offline (Learn): https://learn.captureone.com/relocating-offline-files-catalogs/

**Photo Mechanic Plus**
- Storyteller, "PM+ is gone" (set. 2026): https://picturestoryteller.com/2026/09/08/photo-mechanic-plus-is-gone-heres-what-im-using-instead/
- imagic, PM nel 2026: https://imagic.ink/blog/is-photo-mechanic-worth-buying-2026
- Forum Camera Bits, modello in abbonamento: https://forums.camerabits.com/index.php?topic=15937.120
- Forum Leica, "demise" di PM+ (solo estratto, 403): https://www.l-camera-forum.com/topic/428024-photo-catalogues-dam-the-potential-demise-of-photo-mechanic-plus/
- DPReview, opzioni per il catalogo (solo estratto, 403): https://www.dpreview.com/forums/threads/photo-catalog-software-options.4835355/

**Apple Foto**
- File referenziati "mancanti" su un altro Mac: https://discussions-cn-prz.apple.com/thread/252741972
- Libreria da 1 TB corrotta: https://discussions-cn-prz.apple.com/thread/256132130
- Libreria su disco esterno corrotta: https://discussions.apple.com/thread/256112660
- Unire librerie grandi, video persi: https://discussions.apple.com/thread/256063315
- Una libreria gigante o più librerie: https://discussions.apple.com/thread/255909786

**Guide e blog**
- Lightroom Queen, unire cataloghi: https://www.lightroomqueen.com/merging-catalogs-overview/
- Lightroom Queen, differenze tra cataloghi: https://www.lightroomqueen.com/community/threads/resolving-differences-between-two-catalogs.52272/
- Lightroom Queen, i 10 malintesi sui cataloghi: https://www.lightroomqueen.com/lightroom-catalogs-top-10-misunderstandings/
- Scott Kelby, il backup del catalogo non salva le foto: https://scottkelby.com/warning-backing-up-your-lightroom-catalog-does-not-backup-your-photos/
