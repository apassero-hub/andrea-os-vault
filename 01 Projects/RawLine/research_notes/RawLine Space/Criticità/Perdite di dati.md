# Perdite di dati e file rovinati: storie vere

Ricerca dell'11 novembre 2026 per RawLine Space. Obiettivo: capire come le persone perdono davvero foto e video quando riordinano, spostano, copiano, puliscono o migrano un archivio, per costruire un'app che quegli errori non li possa ripetere.

**Metodo.** Ricerca larga su forum Adobe (Lightroom Classic), Apple Discussions, MacRumors, Synology/SynoForum, forum Dropbox e Resilio, Fred Miranda, Eclectic Light Company, PetaPixel, blog di noleggio e DIT (Lensrentals, Hedge, PremiumBeat), blog di fotografi. Poi lettura diretta dei casi più istruttivi. Alcune pagine (MacRumors, Fred Miranda, PetaPixel, Capture One, forum Resilio) rispondono 403 al download diretto: per quelle uso solo quanto riportato dai risultati di ricerca e lo segnalo come "non letto direttamente". Le pagine dei venditori di software di recupero (iBoysoft, EaseUS, Recoverit, Stellar) sono state usate solo come conferma secondaria, mai come unica fonte, perché hanno interesse a drammatizzare.

**Legenda affidabilità** (colonna "Conferme"): numero di fonti indipendenti che descrivono lo stesso meccanismo · **R** = almeno un caso dal 2024 in poi · **S** = solo casi vecchi ma meccanismo ancora valido.

---

## 1. Tipi di incidente, in ordine di frequenza e gravità

L'ordine combina quanto spesso compare nei forum e quanto danno fa (irreversibile > recuperabile).

### 1.1 Spostamento tra dischi interrotto (copia + cancella finito male)
**Conferme:** 5+ fonti indipendenti · S/R

**Cosa succede.** Tra due volumi diversi uno "sposta" è sempre copia seguita da cancellazione dell'originale. Se il disco si scollega, l'app si blocca, va via la corrente o l'utente preme "Stop", la cancellazione può partire su file non copiati, o restano due metà incomplete.

**Casi.**
- Lightroom Classic, thread "Moving files, resulted in deleting the files" (2015–2017, 63 risposte): spostando 97 foto tra cartelle ne arrivano 76, le altre spariscono; un altro utente ne perde ~600. Adobe dichiara risolto nella 6.12 ma altri segnalano ancora errori. "This is a HUGE problem." ([Adobe](https://community.adobe.com/t5/lightroom-classic-bugs/p-moving-files-resulted-in-deleting-the-files/idc-p/12675540))
- Lightroom: cartella di 2.000+ immagini che si interrompe a metà spostamento e resta "con 0 immagini" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/moving-large-folder-to-another-drive-error-and-missing-images/m-p/14247291)).
- Utente che preme Stop durante uno spostamento: "clicked stop when moving files and now they are gone" ([Adobe](https://community.adobe.com/questions-558/clicked-stop-when-moving-files-and-now-they-are-gone-174664)).
- Finder di Leopard (2007): con disco scollegato a metà, il Finder credeva lo spostamento concluso e cancellava la sorgente; il `mv` del Terminale no ([The Register](https://www.theregister.co.uk/2007/11/06/leopard_dataloss_bug_uncovered/), [eWeek](https://www.eweek.com/apple/leopard-s-disappearing-data-spots/)). Bug vecchio, ma il consiglio che ne è nato è ancora quello di tutti: copiare, verificare, poi cancellare.
- Apple Discussions: se lo spostamento si interrompe "many times both the source & destination files are lost" (citato nei risultati, [Apple](https://discussions.apple.com/thread/255014778)).

**Causa vera.** L'operazione non è atomica e la cancellazione non dipende da una verifica del contenuto copiato. Spesso l'app si fida dell'esito "senza errori" dell'API di copia.

**Come evitarlo.** Mai spostare tra volumi: copiare, verificare con checksum la copia, scrivere a giornale, poi mettere l'originale nel Cestino (non cancellare) e solo a fine lotto. Riprendere un'operazione interrotta dal giornale.

### 1.2 Sincronizzazione che propaga una cancellazione (Dropbox, Synology Drive/Cloud Sync, Resilio, rsync --delete)
**Conferme:** 6+ fonti indipendenti · R

**Cosa succede.** Un disco esterno si scollega o una cartella viene svuotata/rinominata, il programma di sincronizzazione lo interpreta come "l'utente ha cancellato tutto" e cancella anche sul server e sugli altri computer.

**Casi.**
- Dropbox: fotografo con i file locali su un disco esterno che si scollega; oltre 160.000 file rimossi dal server e dagli altri Mac ([forum Dropbox](https://community.dropbox.com/discussions/101001013/deleted-files-due-to-external-drive-getting-disconnected/665220), non letto direttamente, riassunto dai risultati).
- Dropbox 2014: bug di Selective Sync, 8.343 file cancellati per sempre ([ITPro](https://www.itpro.com/cloud/cloud-storage/363163/dropbox-bug-deletes-8000-photos-belonging-to-one-user), [PetaPixel](https://petapixel.com/2014/07/31/cautionary-tale-bug-dropbox-permanently-deleted-8000-photos)).
- Resilio Sync: disco esterno staccato, i file risultano cancellati anche sugli altri nodi; in altri casi l'archivio `.sync/Archive` era vuoto o veniva cancellato insieme alla cartella ([Resilio forum](https://forum.resilio.com/topic/70835-external-hdd-accidentally-removed-files-deleted-on-other-peers/), [Resilio forum 2](https://forum.resilio.com/topic/71794-hundreds-of-files-deleted-by-sync-and-not-available-in-archive), [guida Resilio](https://helpdesk.resilio.com/hc/en-us/articles/4415660046739-How-can-it-happen-that-files-got-deleted-from-the-sync-folder-and-what-to-do-next)).
- Synology Cloud Sync con OneDrive (2022): "thousands of messed up files", PDF illeggibili, file con suffissi `$sshnew$`/`$sshold$`, causa mai chiarita ([SynoForum](https://www.synoforum.com/threads/catastrophe-support-needed-corrupt-files-across-the-board.9064/)). Synology stessa ammette che le sue sincronizzazioni possono cambiare file e rimanda a snapshot e Hyper Backup ([Synology KB](https://kb.synology.com/en-uk/DSM/tutorial/What_are_reasons_for_file_changes)).
- Synology Drive: con l'impostazione "i file cancellati in locale vengono rimossi dal NAS" valida per tutti i client ([SynoForum](https://www.synoforum.com/threads/unreliable-two-way-sync-using-synology-drive-client-deleted-files-reappear.9356/)).
- rsync `--delete` con sorgente e destinazione invertite: archivio iPhoto cancellato, recuperato solo da Flickr ([D'Arcy Norman](https://darcynorman.net/2006/10/03/be-careful-with-rsync--delete/)); un utente salvato dal `-n` (prova a vuoto) su un disco da 4 TB ([Ubuntu Discourse](https://discourse.ubuntu.com/t/rsync-tries-to-delete-everything/53259)).
- MacRumors 2024: "Synology NAS erased my external hard drive" ([MacRumors](https://forums.macrumors.com/threads/synology-nas-erased-my-external-hard-drive.2427465), non letto, 403).

**Causa vera.** L'assenza di un volume viene confusa con l'assenza dei file; i programmi a specchio non distinguono "non c'è più" da "non riesco a vederlo"; la cancellazione di massa non chiede conferma.

**Come evitarlo.** Considerare un volume scollegato come "sconosciuto", mai come "vuoto". Bloccare qualsiasi operazione che cancelli più di una soglia di file senza conferma esplicita. Mostrare il conto delle cancellazioni prima, come fa `rsync -n`.

### 1.3 Copia che "riesce" ma il file è rovinato o incompleto (scheda, trasferimento, ingest)
**Conferme:** 5 fonti indipendenti · R

**Cosa succede.** La copia si conclude, la scheda viene formattata, settimane dopo in montaggio una clip o un RAW è rotto o manca.

**Casi.**
- Lensrentals: clip mancanti scoperte dopo che le schede erano già state formattate; "nove volte su dieci" il file si rovina nel trasferimento. "Once the footage is gone, the footage is really and truly gone." ([Lensrentals](https://www.lensrentals.com/blog/2018/04/how-videographers-can-avoid-data-catastrophes/))
- Hedge: una scheda può restituire dati sbagliati senza errori visibili, l'unico modo di saperlo è il checksum o riguardare ogni clip ([Hedge](https://hedge.co/blog/it-s-all-about-the-source)).
- PremiumBeat e OWC: copia verificata con checksum come prova documentata ([PremiumBeat](https://www.premiumbeat.com/blog/how-to-properly-dump-camera-footage-to-protect-your-assets/), [OWC](https://www.owc.com/blog/copy-that-1-0-is-live-why-you-need-to-checksum-your-media)).
- Data Clinic (recupero dati UK): lo scenario più comune nei matrimoni è il disco che muore prima della seconda copia ([Data Clinic](https://www.dataclinic.co.uk/data-recovery/wedding-photo-data-recovery/)).
- JPEG "mezzi grigi": spesso file incompleti più che corrotti, cioè copie interrotte ([Disktuna](https://www.disktuna.com/?p=3916)).

**Causa vera.** Si verifica la presenza e la dimensione, non il contenuto. Si formatta la fonte prima di avere due copie verificate.

**Come evitarlo.** Checksum di sorgente e destinazione (meglio rileggendo dalla destinazione), anche file per file; mai dichiarare "spostabile/cancellabile" una fonte finché non esistono almeno due copie verificate (o la regola scelta dall'utente).

### 1.4 Dischi singoli, RAID e NAS che muoiono (e rebuild falliti)
**Conferme:** 4 fonti indipendenti · S/R

**Casi.**
- Raoul Pop: due Drobo morti in una settimana (2012), uno per un blackout senza UPS, uno durante la sostituzione di un disco; "well over 30,000" foto e video, l'80% delle foto 2000–2007; i dati recuperati erano poi corrotti a livello di singolo file, scoperto solo riaprendoli ([raoulpop.com](https://raoulpop.com/2019/01/11/the-time-drobo-lost-over-30000-of-my-photos-and-videos/)).
- Fred Miranda: DroboS con ~5 TB, circa il 90% perso ([Fred Miranda](https://www.fredmiranda.com/forum/topic/1024047/0), non letto, 403).
- Jim Kasson: la fine della strada con Drobo ([kasson.com](https://kasson.com/bleeding_edge/the-bleeding-edge/drobo-the-end-of-the-road)).
- Venditori di recupero: un secondo disco che cede durante il rebuild rende il volume illeggibile ([Rossmann](https://rossmanngroup.com/services/drobo-data-recovery)).
- Adorama: 20 GB di lavori cliente su un disco che smette di funzionare e chiede di essere inizializzato ([Adorama](https://www.adorama.com/alc/data-crash-lost-and-found/)).

**Causa vera.** Il RAID è stato preso per un backup; nessuna copia indipendente; corrente senza UPS; rebuild lunghi (circa 1 TB al giorno sui Drobo) che stressano gli altri dischi.

**Come evitarlo (per l'app).** RawLine Space non può impedire un guasto, ma può: sapere quante copie indipendenti esistono di ogni lavoro, avvisare quando un lavoro vive su un solo disco, non fare mai operazioni pesanti su un volume degradato o in rebuild, e non proporre di "liberare spazio" cancellando l'unica copia.

### 1.5 exFAT (e dischi senza journaling) corrotti
**Conferme:** 5 fonti indipendenti · R (Sonoma 2023–2024, Tahoe 2026)

**Casi.**
- macOS Sonoma: exFAT passato in user space, dischi exFAT che non montano o perdono file, nessuna correzione per quattro aggiornamenti; un utente con schede dashcam: "Literally all files vanished" ([Blocks and Files](https://blocksandfiles.com/2024/05/23/apples-sonoma-screwed-exfat-external-drive-access/), [Apple](https://discussions.apple.com/thread/255173291), [Apple 2](https://discussions.apple.com/thread/255488280)).
- Capture One community: "Beware of ex fat external drives on Mac" ([Capture One](https://support.captureone.com/hc/fr/community/posts/5715613733789-Beware-of-ex-fat-external-drives-on-Mac), non letto, 403).
- Premiere: exFAT senza journaling, qualsiasi blackout può rovinare i file ([Adobe](https://community.adobe.com/t5/premiere-pro-discussions/dv-captured-footage-from-premiere-randomly-disappearing-from-new-hard-drive/m-p/12820788/highlight/true)); OWC: exFAT "non è un formato professionale" ([OWC](https://www.owc.com/ca/blog/exfat-is-not-a-professional-drive-format-heres-what-cross-platform-mac-to-pc-content-creators-should-use-instead)).
- macOS Tahoe 26.3 (febbraio 2026): dischi esterni che non montano o spariscono dopo poco; un utente deve copiare 40+ TB altrove e riformattare ([AppleWorld.Today](https://appleworld.today/2026/02/macos-tahoe-26-3-reportedly-breaking-external-storage-for-some-users/), [AppleInsider](https://forums.appleinsider.com/discussion/243469/help-us-figure-out-macos-tahoe-external-drive-mounting-issues)). Perdita di dati non confermata, ma è il contesto in cui l'app lavorerà.

**Causa vera.** exFAT non ha journaling: una scrittura interrotta (estrazione senza espulsione, blackout) lascia la tabella dei file incoerente. Il driver di macOS cambia tra versioni.

**Come evitarlo.** Riconoscere il formato di ogni volume; su exFAT/FAT fare scritture più prudenti (lotti piccoli, `fsync`, verifica immediata), avvisare chiaramente che è il formato più fragile, mai usare un exFAT come unica destinazione di un archivio.

### 1.6 Sovrascritture per nomi in conflitto (Finder "Sostituisci" sulle cartelle)
**Conferme:** 5 fonti indipendenti · S (comportamento invariato)

**Casi.**
- Trascinando una cartella su un'altra con lo stesso nome, "Sostituisci" cancella la vecchia cartella intera, non unisce; chi viene da Windows si aspetta l'unione ([Daring Fireball](https://daringfireball.net/2005/04/replace), [Low End Mac](https://lowendmac.com/misc/05/1031.html), [MacRumors](https://forums.macrumors.com/threads/replace-folders-sucks.1665590)).
- Il pulsante "Unisci" compare solo con Opzione e solo in certi casi; con versioni diverse di file omonimi restano solo Stop o Sostituisci ([Fileside](https://www.fileside.app/blog/2021-07-31_merge-folders-mac), [MacMost](https://macmost.com/how-to-merge-two-folders-on-a-mac.html)).
- Utente che sovrascrive un catalogo: i programmi di recupero trovano i file cancellati ma non quelli sovrascritti ([Apple](https://discussions.apple.com/thread/253775052)).

**Causa vera.** Le collisioni di nome sono risolte con una scelta binaria e distruttiva; i file sovrascritti non vanno nel Cestino.

**Come evitarlo.** Nessuna sovrascrittura mai: in caso di conflitto confrontare il contenuto (checksum); se identico, è un doppione da gestire; se diverso, rinominare con suffisso e segnalarlo. Le cartelle si uniscono sempre file per file.

### 1.7 Cancellazioni sbagliate: doppioni, "elimina dal disco", copie virtuali, NAS senza Cestino
**Conferme:** 5 fonti indipendenti · R

**Casi.**
- App di ricerca doppioni che non indica quale sia l'originale: l'utente cancella originali e copie ([Adobe Bridge](https://community.adobe.com/t5/bridge-discussions/how-can-i-deal-with-duplicate-files/m-p/10728846)); cancellando fuori da Lightroom si rischia di eliminare proprio il file usato dal catalogo ([Adobe](https://community.adobe.com/questions-675/finding-duplicates-without-risking-original-images-974078), [Adobe, PhotoSweeper](https://community.adobe.com/questions-675/problems-with-lr-classic-and-photosweeper-980534)).
- Lightroom 2020: "cancello un doppione e spariscono tutti e due" perché il secondo era una copia virtuale; "I may have deleted a lot of original files" ([Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/deleted-one-photo-two-were-gone/td-p/11040289)).
- Confusione "Rimuovi" contro "Elimina dal disco" in Lightroom ([Julieanne Kost](https://jkost.com/blog/2019/05/removing-vs-deleting-images-in-lightroom-classic.html), [Adobe](https://community.adobe.com/questions-675/is-there-a-way-to-recover-a-photo-after-delete-from-disk-983968)).
- Su condivisioni SMB (NAS) il Finder cancella subito, senza Cestino; anche "Elimina dal disco" di Lightroom salta il Cestino su questi volumi ([Eclectic Light](https://eclecticlight.co/2015/07/19/qa-deleting-without-trash/), [Apple](https://discussions.apple.com/thread/254034923), [Adobe](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-cc-quot-files-on-a-volume-that-does-not-support-trash-quot/m-p/14179878/highlight/true)).

**Causa vera.** "Doppione" deciso solo su nome/data/dimensione o su somiglianza visiva; nessuna conoscenza di quale copia è usata da cataloghi e progetti; la cancellazione su rete è definitiva e l'utente non lo sa.

**Come evitarlo.** Doppione = contenuto identico byte per byte (hash completo). Indicare sempre la copia "da tenere" e perché (usata da catalogo Lightroom/Capture One/FCP, più vecchia, su disco con più copie). Su volumi senza Cestino, RawLine Space deve creare un proprio cestino di quarantena sullo stesso volume.

### 1.8 Bit rot e corruzione silenziosa scoperta anni dopo
**Conferme:** 4 fonti indipendenti · R

**Casi.**
- JPEG con la metà inferiore grigia o rumore: un solo byte rovinato compromette tutto quello che segue ([ctrl.blog](https://www.ctrl.blog/entry/bitrot-avif-jxl-comparison/), [Eclectic Light](https://eclecticlight.co/2020/04/30/file-integrity-10-effects-of-length-of-corruption-on-images-and-ecc-recovery/)).
- Synology Btrfs: lo scrubbing trova "checksum mismatch", ma senza ridondanza il file resta illeggibile; Synology avverte che gli snapshot locali possono contenere gli stessi dati rovinati; tra le cause RAM difettosa ([Synology KB](https://kb.synology.com/en-au/DSM/tutorial/Btrfs_checksum_mismatch)); utente a cui un video viene restituito corrotto nonostante lo scrub l'abbia segnalato ([SynoForum](https://www.synoforum.com/threads/btrfs-returns-corrupted-data-despite-checksum-mismatches-detected-during-scrub.16082/latest)).
- Drobo: corruzione a livello di file scoperta solo aprendo le foto recuperate (vedi 1.4).

**Causa vera.** Nessuno confronta periodicamente il contenuto; i backup a specchio copiano fedelmente il file già rovinato e, con la rotazione, perdono la versione buona.

**Come evitarlo.** Registrare un hash per ogni file al primo inventario; ricontrollare a richiesta o a rotazione; quando un file cambia contenuto senza che la data di modifica cambi, è corruzione: avvisare e indicare dove esiste una copia sana.

### 1.9 Accenti e Unicode nei nomi (NFC/NFD) tra Mac, NAS e Linux
**Conferme:** 4 fonti indipendenti · S/R

**Casi.**
- macOS usa la forma decomposta (NFD) su HFS+, APFS non normalizza ma macOS normalizza in quasi tutti i punti; su SMB/NFS un file creato con l'altra forma può risultare irraggiungibile ([Eclectic Light](https://eclecticlight.co/2021/05/08/explainer-unicode-normalization-and-apfs/), [Eclectic Light 2017](https://eclecticlight.co/2017/04/06/apfs-is-currently-unusable-with-most-non-english-languages/)).
- TrueNAS/Samba: il Finder dice "file non trovato" su nomi NFD in una condivisione ([TrueNAS](https://www.truenas.com/community/threads/normalization-to-nfc.64529), [lista Samba](https://lists.samba.org/archive/samba/2019-December/227427.html)).
- Script per convertire i nomi su Synology perché i client Mac non li vedevano ([gist](https://gist.github.com/xthezealot/9a65fac2c7b916c4d84e66188bf06bec)); FreeFileSync: entrambe le forme falliscono anche nel Finder ([FreeFileSync](https://freefilesync.org/forum/viewtopic.php?p=38613)).

**Causa vera.** Due nomi identici a vista sono byte diversi: un programma li vede come due file (falsi doppioni), un altro non trova l'originale, una sincronizzazione lo ricopia o lo cancella. Rilevante per l'italiano ("Valle d'Aosta - Courmayeur", "Città", "Perù").

**Come evitarlo.** Confrontare i nomi sempre normalizzati (NFC) ma conservare i byte originali; rilevare e segnalare cartelle con lo stesso nome in due forme; mai rinominare per normalizzare senza anteprima.

### 1.10 Errore umano: formattare o inizializzare il disco sbagliato
**Conferme:** 3 fonti (di cui 2 commerciali) · S

**Casi.**
- Fotografo che perde tutte le immagini di un evento per aver formattato il disco su cui credeva di aver già scaricato ([Joseph Kilgus](https://joseph-kilgus.squarespace.com/blog/archiving)).
- 900 GB di RAW di matrimoni copiati su WD Elements, poi formattato l'SSD, poi scoperte cartelle mancanti ([Recoverit](https://recoverit.wondershare.com/faq/wd-elements-raw-folders-missing-after-ssd-formatted.html), venditore).
- Disco che chiede di essere inizializzato e l'utente lo fa (Adorama, sopra).

**Causa vera.** Dischi con nomi simili o generici ("Untitled", "Samsung T7"), nessuna prova che la copia sia completa prima di cancellare la fonte.

**Come evitarlo.** Identificare i dischi per UUID e per nome dato dall'utente, mostrare sempre il nome umano e il colore del disco; prima di dire "questo disco può essere liberato" mostrare quante copie verificate esistono altrove.

### 1.11 File "spariti" che in realtà sono scollegati dal catalogo
**Conferme:** 4 fonti · R (febbraio 2026)

**Casi.**
- Lightroom Classic 15.1.1 su Tahoe 26.2: 1.285 RAF "spariti" con punto esclamativo, lavori cliente; causa sconosciuta, recupero affidato a un vecchio clone Carbon Copy Cloner ([Adobe](https://community.adobe.com/questions-675/lr-15-1-1-mac-running-tahoe-26-2-lr-has-lost-1285-photos-1548393)).
- Spostare o rinominare fuori da Lightroom rompe i collegamenti ([Lightroom Queen](https://www.lightroomqueen.com/lightroom-photos-missing-fix/), [Lightroom Killer Tips](https://lightroomkillertips.com/when-photos-go-missing/)).

**Causa vera.** Spesso nessuna perdita reale, ma il panico porta a gesti distruttivi (reimportare, cancellare, riformattare). È esattamente il rischio che RawLine Space introduce riordinando le cartelle.

**Come evitarlo.** Prima di spostare, sapere quali cataloghi e progetti (Lightroom, Capture One, Final Cut, Resolve) puntano a quei file; dopo lo spostamento, aiutare a ricollegarli o almeno lasciare una mappa vecchio percorso → nuovo percorso.

### Riassunto della verifica

| Tipo | Fonti indipendenti | Recente | Gravità |
|---|---|---|---|
| Spostamento interrotto | 5+ | sì (Adobe 2023) | Alta, spesso irreversibile |
| Sincronizzazione che cancella | 6+ | sì | Molto alta, si propaga |
| Copia "riuscita" ma rovinata | 5 | sì | Alta, scoperta tardi |
| Guasto disco/RAID | 4 | in parte | Molto alta |
| exFAT corrotto | 5 | sì (2024, 2026) | Alta |
| Sovrascrittura per nome | 5 | comportamento attuale | Alta, non recuperabile |
| Cancellazioni sbagliate | 5 | sì | Media-alta |
| Bit rot | 4 | sì | Media, scoperta anni dopo |
| Unicode nei nomi | 4 | comportamento attuale | Media (falsi doppioni, file irraggiungibili) |
| Disco sbagliato formattato | 3 (2 commerciali) | no | Molto alta, rara |
| Catalogo scollegato | 4 | sì (2026) | Bassa in sé, alta per le reazioni |

Scartati perché non verificabili: storie solo da siti di software di recupero senza dettagli (es. "Alex Mitchell, 500 GB" di Recoverit), post Reddit visti solo come titolo.

---

## 2. Le paure ricorrenti dei fotografi

1. **"L'app ha cancellato file che non le avevo detto di toccare."** È la paura numero uno contro ogni strumento automatico (doppioni, sincronizzazioni, spostamenti in Lightroom). Si traduce in diffidenza: molti consigliano di spostare solo dal Finder e ricollegare a mano.
2. **"Me ne accorgo troppo tardi."** Clip rotte trovate in montaggio, JPEG grigi trovati anni dopo, cartelle a 0 immagini scoperte dal cliente. La paura non è solo perdere, è non saperlo.
3. **"Ho cancellato l'unica copia."** Formattare la scheda, svuotare il disco "tanto è sul NAS", e il NAS non ce l'aveva.
4. **"Il RAID/NAS mi dava sicurezza e invece."** Chi ha perso un Drobo o un NAS non si fida più di un unico contenitore.
5. **"La sincronizzazione mi ha tradito."** Dropbox, Resilio, Synology Drive: la cancellazione che si propaga è vissuta come un tradimento perché arriva da uno strumento pensato per proteggere.
6. **"Ho rotto il catalogo."** Spostando cartelle si perdono anni di regolazioni, stelle, collezioni. Molti non spostano mai nulla per paura.
7. **"Il Mac nuovo o l'aggiornamento di macOS non vede più i miei dischi."** Sonoma ed exFAT, Tahoe e i dischi esterni: aggiornare il sistema è percepito come rischio.
8. **"Clienti e soldi."** Le storie più dolorose sono lavori cliente (matrimoni, eventi): c'è un danno economico e di reputazione, a volte legale ([terms.law](https://terms.law/forum/thread/wedding-photographer-lost-all-photos.html)).

---

## 3. Requisiti concreti per RawLine Space

Ogni requisito nasce da uno o più incidenti sopra (tra parentesi).

**Operazioni sui file**
1. **Niente spostamenti veri tra volumi.** Sempre: copia → verifica checksum rileggendo la destinazione → registrazione nel giornale → originale in quarantena. Mai cancellazione diretta. (1.1, 1.3)
2. **Giornale persistente prima di ogni scrittura.** Ogni operazione scritta su disco prima di eseguirla, con stato per file; all'avvio dopo un crash o un disco staccato, RawLine Space riprende o annulla dal giornale. (1.1)
3. **Annulla sempre possibile**, anche giorni dopo, fino allo svuotamento esplicito della quarantena. (1.1, 1.7)
4. **Quarantena propria su ogni volume**, perché NAS via SMB ed exFAT non hanno un Cestino affidabile. Mai `removeItem` immediato. (1.7)
5. **Nessuna sovrascrittura, mai.** Conflitto di nome: stesso hash = doppione; hash diverso = suffisso e segnalazione. Le cartelle si uniscono file per file. (1.6)
6. **Anteprima obbligatoria con i numeri**: quanti file, quanti GB, da dove a dove, quante cancellazioni. Soglia oltre la quale serve una conferma rafforzata (es. scrivere il nome del disco). (1.2, 1.10)
7. **Operazioni a lotti piccoli e verificati**, specie su exFAT/FAT e dischi USB: `fsync` dopo ogni file, verifica subito. (1.5)

**Dischi e volumi**
8. **Un disco scollegato è "assente", non "vuoto".** Nessuna conclusione o azione su file di volumi offline; se un volume sparisce a metà, pausa immediata e stato salvato. (1.2, 1.1)
9. **Identità dei dischi per UUID** più nome umano e colore; avviso se due dischi si chiamano allo stesso modo. (1.10)
10. **Riconoscere il formato** (APFS, HFS+, exFAT, SMB) e mostrare il livello di rischio; avvisare se un archivio vive solo su exFAT. (1.5)
11. **Non lavorare su volumi in difficoltà**: errori di I/O ripetuti, SMART in allarme, NAS in rebuild o degradato quando rilevabile → solo lettura. (1.4)
12. **RawLine Space non sincronizza.** Niente specchi bidirezionali né `--delete`: solo copie unidirezionali verificate. Rilevare cartelle dentro Dropbox/Synology Drive/Resilio/iCloud e avvisare che cancellare lì significa cancellare ovunque. (1.2)

**Integrità e copie**
13. **Inventario con hash per file** al primo passaggio (veloce + completo per i doppioni), salvato localmente e offline. (1.3, 1.8)
14. **Contatore delle copie indipendenti** per ogni lavoro/cartella: "questo matrimonio esiste su 1 disco" è un allarme, non un dettaglio. Liberare spazio è permesso solo se restano almeno N copie verificate (N scelto dall'utente, default 2). (1.4, 1.10)
15. **Controllo periodico di integrità** a richiesta: ricalcolo hash su un campione o su tutto, segnalazione di file cambiati senza data di modifica nuova (corruzione silenziosa) e indicazione della copia sana. (1.8)
16. **Riconoscere file incompleti**: dimensione zero, JPEG senza marcatore di fine, MP4/MOV senza indice (`moov`), RAW troncati. Mai considerarli "doppioni" né copie valide. (1.3, 1.8)

**Doppioni, cataloghi, nomi**
17. **Doppione solo se identico byte per byte**; la somiglianza visiva è un suggerimento, mai un'azione automatica. Indicare sempre quale copia tenere e perché. (1.7)
18. **Sapere chi usa i file**: leggere (solo lettura) cataloghi Lightroom Classic, Capture One, librerie Final Cut, progetti Resolve/Premiere per non spostare o cancellare file referenziati, e generare la mappa vecchio → nuovo percorso. Rispettare RAW+JPEG, sidecar XMP, copie virtuali. (1.7, 1.11)
19. **Nomi Unicode**: confronto normalizzato NFC, conservazione dei byte originali, segnalazione di nomi in due forme nella stessa cartella; nessuna normalizzazione silenziosa. (1.9)

**Comunicazione**
20. **Rapporto finale leggibile** (e salvato) di ogni operazione: cosa è stato copiato, verificato, messo in quarantena, saltato e perché. La paura numero due è "me ne accorgo troppo tardi": l'app deve dirlo subito. (2)
21. **Linguaggio che non confonde** "Rimuovi dall'elenco" con "Elimina dal disco": una sola parola per l'azione distruttiva, sempre la stessa, con colore e conferma propri. (1.7)

Tutto quanto sopra è locale e funziona senza rete, come richiesto dalla regola RawLine.

---

## 4. Fonti

**Spostamenti e copie interrotti**
- https://community.adobe.com/t5/lightroom-classic-bugs/p-moving-files-resulted-in-deleting-the-files/idc-p/12675540
- https://community.adobe.com/t5/lightroom-classic-discussions/moving-large-folder-to-another-drive-error-and-missing-images/m-p/14247291
- https://community.adobe.com/questions-558/clicked-stop-when-moving-files-and-now-they-are-gone-174664
- https://www.theregister.co.uk/2007/11/06/leopard_dataloss_bug_uncovered/
- https://www.eweek.com/apple/leopard-s-disappearing-data-spots/
- https://discussions.apple.com/thread/255014778

**Sincronizzazioni**
- https://community.dropbox.com/discussions/101001013/deleted-files-due-to-external-drive-getting-disconnected/665220
- https://www.itpro.com/cloud/cloud-storage/363163/dropbox-bug-deletes-8000-photos-belonging-to-one-user
- https://petapixel.com/2014/07/31/cautionary-tale-bug-dropbox-permanently-deleted-8000-photos
- https://forum.resilio.com/topic/70835-external-hdd-accidentally-removed-files-deleted-on-other-peers/
- https://forum.resilio.com/topic/71794-hundreds-of-files-deleted-by-sync-and-not-available-in-archive
- https://helpdesk.resilio.com/hc/en-us/articles/4415660046739-How-can-it-happen-that-files-got-deleted-from-the-sync-folder-and-what-to-do-next
- https://www.synoforum.com/threads/catastrophe-support-needed-corrupt-files-across-the-board.9064/
- https://www.synoforum.com/threads/unreliable-two-way-sync-using-synology-drive-client-deleted-files-reappear.9356/
- https://kb.synology.com/en-uk/DSM/tutorial/What_are_reasons_for_file_changes
- https://forums.macrumors.com/threads/synology-nas-erased-my-external-hard-drive.2427465
- https://darcynorman.net/2006/10/03/be-careful-with-rsync--delete/
- https://discourse.ubuntu.com/t/rsync-tries-to-delete-everything/53259

**Copie verificate e ingest**
- https://www.lensrentals.com/blog/2018/04/how-videographers-can-avoid-data-catastrophes/
- https://hedge.co/blog/it-s-all-about-the-source
- https://www.premiumbeat.com/blog/how-to-properly-dump-camera-footage-to-protect-your-assets/
- https://www.owc.com/blog/copy-that-1-0-is-live-why-you-need-to-checksum-your-media
- https://www.dataclinic.co.uk/data-recovery/wedding-photo-data-recovery/
- https://www.disktuna.com/?p=3916

**Dischi, RAID, NAS**
- https://raoulpop.com/2019/01/11/the-time-drobo-lost-over-30000-of-my-photos-and-videos/
- https://www.fredmiranda.com/forum/topic/1024047/0
- https://kasson.com/bleeding_edge/the-bleeding-edge/drobo-the-end-of-the-road
- https://rossmanngroup.com/services/drobo-data-recovery
- https://www.adorama.com/alc/data-crash-lost-and-found/

**exFAT e macOS**
- https://blocksandfiles.com/2024/05/23/apples-sonoma-screwed-exfat-external-drive-access/
- https://discussions.apple.com/thread/255173291
- https://discussions.apple.com/thread/255488280
- https://support.captureone.com/hc/fr/community/posts/5715613733789-Beware-of-ex-fat-external-drives-on-Mac
- https://community.adobe.com/t5/premiere-pro-discussions/dv-captured-footage-from-premiere-randomly-disappearing-from-new-hard-drive/m-p/12820788/highlight/true
- https://www.owc.com/ca/blog/exfat-is-not-a-professional-drive-format-heres-what-cross-platform-mac-to-pc-content-creators-should-use-instead
- https://appleworld.today/2026/02/macos-tahoe-26-3-reportedly-breaking-external-storage-for-some-users/
- https://forums.appleinsider.com/discussion/243469/help-us-figure-out-macos-tahoe-external-drive-mounting-issues

**Sovrascritture e Finder**
- https://daringfireball.net/2005/04/replace
- https://lowendmac.com/misc/05/1031.html
- https://forums.macrumors.com/threads/replace-folders-sucks.1665590
- https://www.fileside.app/blog/2021-07-31_merge-folders-mac
- https://macmost.com/how-to-merge-two-folders-on-a-mac.html
- https://discussions.apple.com/thread/253775052

**Cancellazioni, doppioni, cataloghi**
- https://community.adobe.com/t5/bridge-discussions/how-can-i-deal-with-duplicate-files/m-p/10728846
- https://community.adobe.com/questions-675/finding-duplicates-without-risking-original-images-974078
- https://community.adobe.com/questions-675/problems-with-lr-classic-and-photosweeper-980534
- https://community.adobe.com/t5/lightroom-classic-discussions/deleted-one-photo-two-were-gone/td-p/11040289
- https://jkost.com/blog/2019/05/removing-vs-deleting-images-in-lightroom-classic.html
- https://community.adobe.com/questions-675/is-there-a-way-to-recover-a-photo-after-delete-from-disk-983968
- https://eclecticlight.co/2015/07/19/qa-deleting-without-trash/
- https://discussions.apple.com/thread/254034923
- https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-cc-quot-files-on-a-volume-that-does-not-support-trash-quot/m-p/14179878/highlight/true
- https://community.adobe.com/questions-675/lr-15-1-1-mac-running-tahoe-26-2-lr-has-lost-1285-photos-1548393
- https://www.lightroomqueen.com/lightroom-photos-missing-fix/
- https://lightroomkillertips.com/when-photos-go-missing/

**Bit rot e integrità**
- https://www.ctrl.blog/entry/bitrot-avif-jxl-comparison/
- https://eclecticlight.co/2020/04/30/file-integrity-10-effects-of-length-of-corruption-on-images-and-ecc-recovery/
- https://kb.synology.com/en-au/DSM/tutorial/Btrfs_checksum_mismatch
- https://www.synoforum.com/threads/btrfs-returns-corrupted-data-despite-checksum-mismatches-detected-during-scrub.16082/latest

**Unicode nei nomi**
- https://eclecticlight.co/2021/05/08/explainer-unicode-normalization-and-apfs/
- https://eclecticlight.co/2017/04/06/apfs-is-currently-unusable-with-most-non-english-languages/
- https://www.truenas.com/community/threads/normalization-to-nfc.64529
- https://lists.samba.org/archive/samba/2019-December/227427.html
- https://gist.github.com/xthezealot/9a65fac2c7b916c4d84e66188bf06bec
- https://freefilesync.org/forum/viewtopic.php?p=38613

**Errore umano**
- https://joseph-kilgus.squarespace.com/blog/archiving
- https://recoverit.wondershare.com/faq/wd-elements-raw-folders-missing-after-ssd-formatted.html (venditore)
- https://terms.law/forum/thread/wedding-photographer-lost-all-photos.html
