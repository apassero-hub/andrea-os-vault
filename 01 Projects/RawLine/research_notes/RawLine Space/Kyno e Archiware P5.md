# Kyno e Archiware P5 — ricerca per RawLine Space

Data: 11 novembre 2026. Legenda: **[V]** verificato su fonte (link in fondo), **[D]** dedotto o non confermato.

> Nota sulla premessa "Kyno, ora Archiware": **non risulta**. Kyno (Lesspain Software, Germania) è stato comprato da **Signiant** nel marzo 2021 [V]. Con Archiware c'era solo una *partnership*: integrazione P5 Archive in Kyno Premium dalla 1.7.1 (2019), **tolta nella 1.9.0** (settembre 2025) [V]. La pagina integrazioni di Archiware cita ancora Kyno, ma è un residuo [D].

---

## 1. Kyno (Lesspain / Signiant)

**Cos'è.** Un browser di media per macOS e Windows: si apre una cartella o un disco e si vede, si riproduce, si tagga, si rinomina, si converte. Non c'è nessuna importazione in un catalogo. Nasce per il video (MXF, P2, HEVC, BRAW, R3D) [V]. Per i RAW fotografici non c'è nulla di documentato [D: non è il suo campo].

### Media senza database proprietario
- Non tiene un database centrale dei contenuti e lavora direttamente sul file system di qualsiasi disco collegato [V, CineD].
- I **metadati descrittivi** (stelle, tag, titolo, descrizione, scena, ripresa, marker, sottoclip) stanno in **file XML in cartelle nascoste accanto ai media** [V, supporto Lesspain]. Secondo NeoFinder è la cartella `.LP_Store`, con un file `<nomefile completo>.lpmd` per ogni clip, in un formato non documentato [V].
- I **metadati tecnici e le miniature** sono una cache in `~/Library/Caches/Kyno`, l'**indice di ricerca** sta in `~/Library/Kyno`. Si possono cancellare senza perdere nulla: si ricostruiscono da soli [V].
- Pregio: copiando la cartella i metadati la seguono [V]. Difetto: **se si sposta o rinomina un file nel Finder si perde il collegamento** ai metadati, a meno di spostare a mano anche il file nascosto [V]. Il sidecar è legato al nome del file, non a un identificativo del contenuto [V/D].
- Premium: si può scegliere dove salvare i metadati descrittivi (per i dischi in sola lettura) e usare una cache condivisa (dalla 1.5) [V]. La 1.9 aggiunge impostazioni per volume, con metadati tecnici e miniature su storage condiviso [V].
- Esportazione, importazione e **fusione** dei metadati tra copie dello stesso girato, per lavorare in più sedi (dalla 1.6) [V].
- Scrittura XMP per Premiere (dalla 1.7.1) [V]. Altrimenti il formato resta chiuso: NeoFinder offre un comando per convertirlo in XMP [V].

### Rinomina, sposta, organizza in blocco
- Motore di rinomina in blocco con **27 variabili**. Si può rinominare anche incollando clip in una cartella o durante la conversione [V, OWC/PremiereBro].
- La rinomina fatta in Kyno è definitiva, cambia il file su disco [V, OWC]. Che porti con sé il sidecar è [D] probabile, ma non è documentato.
- **Drilldown**: mostra in un'unica vista tutti i media delle sottocartelle, a qualsiasi profondità. Larry Jordan: "I LOVE this feature" [V].
- Sicurezze documentate per la rinomina (anteprima, annulla, registro): **non trovate** [D: niente nelle fonti].

### Copia verificata (offload e backup)
- "Copy & verify" dalla 1.6 (2019): checksum bit per bit, standard **MHL**, modalità completa o incrementale [V].
- Premium: due destinazioni insieme e scelta della verifica fra MD5, SHA1 o solo dimensione (dalla 1.8) [V].
- 1.7.3: i file nascosti si ignorano tranne i metadati Kyno. Avvisa se la cartella di destinazione esiste già o se lo spazio non basta. Il lavoro fallisce se gli errori sono troppi [V].
- 1.7.4: la copia **riprende dopo un distacco temporaneo del disco** [V].
- 1.8: dopo una copia verificata indicizza automaticamente [V].

### Sottoclip, marker, ricerca
- Marker usati come sottoclip, fotogrammi da esportare o commenti. Sottoclip da punti in/out ed esportazione in blocco [V].
- Ricerca e filtri, per esempio "file incompatibili con FCP X" per recuperare formati vecchi [V, Larry Jordan]. In una prima recensione la ricerca copriva solo la cartella scelta, salvo usare il drilldown [V].
- Ricerche salvate: non documentate [D].

### Dischi scollegati
- **Non è un catalogo di dischi offline.** Per cercare, lo storage dev'essere collegato [V, OWC]. Dalla 1.7.5 si può spegnere il monitoraggio del file system sui dischi esterni e di rete, per evitare blocchi [V]. La 1.9 corregge cartelle segnate per errore come offline dopo un aggiornamento di macOS [V].

### Interfaccia, prezzo, stato
- Interfaccia a pannelli (volumi a sinistra, griglia o lista, player, metadati). La 1.9 porta un tema più scuro e un font più grande [V].
- Prezzo: da **159 €** (sito ufficiale) [V]. Su Capterra Standard 159 $ e Premium 349 $ per utente, licenza a pagamento unico [V, terze parti].
- Stato: tra la 1.8.5 (dicembre 2021) e la **1.9.0 (settembre 2025)** non è uscito nulla. La 1.9 è la prima versione nativa per Apple Silicon, ma l'aggiornamento automatico scarica ancora la versione Intel [V]. Digital Production la definisce "ancora viva", un aggiornamento di manutenzione, e invita a provarla prima di usarla in produzione [V].

### Critiche
- Formato dei sidecar chiuso e non documentato. Rinominare o spostare fuori da Kyno rompe i metadati [V].
- Sviluppo quasi fermo per 4 anni, NeoFinder la considerava "abbandonata" [V]. Le integrazioni Frame.io e P5 sono state tolte [V].
- Un lettore di Larry Jordan la trova cara e complessa se serve solo a convertire [V, opinione].

---

## 2. Archiware P5 (Archive, Backup, Synchronize)

**Cos'è.** Una suite server con interfaccia **web** (si usa dal browser) per macOS, Windows, Linux, FreeBSD e diversi NAS [V]. I moduli sono **Archive** (archivio permanente che cresce), **Backup** (copie cicliche che si sovrascrivono), **Synchronize** (replica, con versioni e istantanee) e **Archive DLM** (spostamento automatico fra livelli di storage) [V]. Versione attuale **8.0** (febbraio 2026) [V].

### Archiviazione su LTO, dischi, cloud
- Destinazioni: disco, nastro **LTO/LTFS**, cloud (S3, Azure, Wasabi, Backblaze B2) [V].
- Formato nativo P5, che conserva ACL, attributi estesi e del Finder e caratteri speciali, oppure LTFS [V]. Critica: i dati in formato P5 si **ripristinano solo con P5** [V].
- Archiviazione incrementale. **INC+** riconosce anche i file spostati [V]. Cartelle sorvegliate per archiviare in automatico, filtri per nome, dimensione e data [V].
- Etichetta i nastri da solo e tiene traccia di cosa c'è su ciascuno. Un nastro non mescola backup e archivio [V, Larry Jordan].
- Duplicare i nastri è macchinoso: serve un secondo piano e un secondo pool [V, Larry Jordan 2019].

### Indice con anteprime, consultabile offline
- Ogni file archiviato finisce nell'**indice dell'archivio**, che viene salvato in automatico a intervalli regolari [V].
- Miniature e **proxy video** generati con FFmpeg e ImageMagick. Archiware lo chiama "mini-MAM": l'archivio offline si sfoglia per immagini [V]. Nella 8.0 le anteprime si possono generare in parallelo su più client [V].
- Campi metadati personalizzabili, con menu e lettura dall'intestazione del file. Ricerca combinata e salvata, le ultime 10 ricerche in un menu [V].
- Si sfoglia e si cerca **senza i nastri montati**: l'indice e le anteprime stanno sul server e il nastro viene chiesto solo per il ripristino [D: è la logica del mini-MAM, ma non ho trovato una frase esplicita].
- Lettura e catalogazione di nastri LTFS creati da altri programmi [V].

### "Archivia e libera spazio"
- **Archive App** (vecchia, solo Mac, P5 5.3 e successivi): dal menu contestuale del Finder si sceglie "Archive to P5". **Dopo l'archiviazione riuscita gli originali vengono cancellati** e sostituiti da un file collegamento con lo stesso nome più `.p5a`. Con un doppio clic sul `.p5a` si vedono anteprima e metadati e si ripristina. Se il `.p5a` viene spostato, il file torna nella nuova posizione [V, datasheet].
- **P5 Companion** (attuale, Mac/Win/Linux, gratuito con la licenza Archive): si archivia trascinando. Secondo come è impostato il piano, l'originale **può** essere cancellato e sostituito da stub `.p5c`. Per ripristinare si trascinano gli stub, dopo aver visto anteprima e metadati. Gli stub restano dopo il ripristino e si possono riusare [V].
- Nei piani di archiviazione la **cancellazione della sorgente è spenta di default** [V, Larry Jordan].
- Se la cancellazione aspetti una **verifica di rilettura** o solo la scrittura riuscita **non è chiaro** dalle fonti pubbliche [D]. La verifica esiste: checksum xxHash a 64 e 128 bit, confronto dei checksum nel formato nativo, rilettura nel formato LTFS, manifest MHL opzionale [V]. Le note della 7.1.4 citano un bug corretto sulla "cancellazione dopo archiviazione" [V]: è una funzione delicata anche per loro.
- 8.0: "cancellazione controllata" dei dati archiviati, cancellazione selettiva, riuso dei volumi, cancellazione sicura [V].

### Ripristino e report
- Il ripristino parte dall'indice e cerca su tutti i volumi [V]. **Project Restore** (8.0) legge EDL, OTIO, FCPXML e ALE e ripristina i media usati da un progetto anche se i percorsi sono cambiati, con anteprima delle versioni [V].
- Di default il ripristino va nella posizione originale e può **sovrascrivere**: Larry Jordan consiglia "Relocate to directory" [V]. Con la Desktop Edition si ripristina solo su dischi collegati al computer che fa da host [V, 2019].
- Report: Job Monitor con avanzamento e tempo stimato [V]. Una dashboard 8.0 mostra lo spazio per progetto e l'andamento nel tempo [V]. Report per email o esportabili: non documentati nelle fonti lette [D: ci sono quasi certamente notifiche, ma non le ho verificate].

### Interfaccia, prezzo
- Interfaccia web con procedura guidata iniziale [V]. Larry Jordan: pensata per chi fa IT, documentazione da riscrivere per i creativi, voci per moduli non inclusi nella licenza che confondono [V].
- Licenza **perpetua**, manutenzione facoltativa al 15% l'anno (gratis il primo anno). Desktop LTO Edition (Backup + Archive, 1 drive): **1.200 € / 1.680 $** (G2, dato del 2021). Nel 2019 costava 1.400 $, la suite completa circa 3.920 $ [V]. Si compra tramite rivenditori, prezzo con configuratore [V]. Prova di 30 giorni [V].

### Critiche
- Cara per un singolo drive, complessa e pensata per chi fa IT [V, Larry Jordan 2019].
- Il formato proprietario preoccupa per l'accesso a lungo termine [V].
- Backup e archivio si cercano in due posti diversi. Larry: l'utente dovrebbe solo trovare il file [V].
- Un lettore racconta di una libreria diventata inaccessibile per problemi di IP e licenza scaduta [V, commento].

---

## 3. Confronto rapido: CatDV (Quantum)
- Catalogo con database. Un clip risulta **offline** se il file è stato spostato o cancellato, se il volume è staccato o se è stato **archiviato ed eliminato** dal disco [V].
- Le miniature stanno nel catalogo e restano visibili anche offline. I proxy possono stare in una cartella condivisa o **dentro il catalogo** come archivio autonomo [V].
- Con il plugin di archiviazione (Cache-A, Archiware e altri): "purge" cancella l'originale e lascia proxy e miniature, il ripristino si fa dal menu Strumenti. Nel plugin Archiware è P5 a garantire l'integrità e si consiglia di non verificare due volte [V].
- I file si ritrovano tramite il percorso ("Media Path" e volumi mappati). Con un catalogo spostato su un'altra macchina tutto risulta offline finché non si ricollega [V, forum].
- Axle AI: non approfondito, nessuna fonte utile sull'uso offline. È basato su server [D].

---

## Idee da prendere per RawLine Space

1. **Sidecar accanto ai file, più indice locale ricostruibile** (come Kyno), ma con due correzioni:
   - formato **aperto e documentato** (XMP per le foto, JSON leggibile per il resto);
   - aggancio per **contenuto** (hash veloce più dimensione) e non per nome. Se l'utente sposta o rinomina nel Finder, RawLine Space ricollega da sola invece di perdere i metadati.
2. La cache di miniature e indice va considerata **sacrificabile**: si cancella e si ricostruisce, e lo diciamo chiaramente nell'interfaccia ("puoi cancellarla, non perdi nulla").
3. **Catalogo dei dischi scollegati** con miniature e anteprime piccole (quello che manca a Kyno e che P5 fa bene): cerco "Gran Sasso 2019 drone" e mi dice "disco *Archivio 07*, collegalo". La richiesta del nastro in P5 diventa "collega il disco X".
4. **Copia verificata in stile Kyno 1.7.x**: MHL o checksum xxHash, più destinazioni, **ripresa dopo il distacco**, avvisi su spazio e cartella già esistente, stop se gli errori sono troppi, indicizzazione automatica a copia finita.
5. **"Archivia e libera spazio" in due tempi distinti**:
   - archivia, poi **rileggi e verifica** su ogni copia;
   - solo dopo propone di liberare spazio, mostrando l'elenco e i GB recuperati;
   - la cancellazione è **spenta di default** (come P5), va nel Cestino e non è definitiva;
   - è consentita solo se esistono almeno N copie verificate.
6. **Segnaposto leggero** al posto del file liberato (come `.p5a`/`.p5c`): stesso nome più un'estensione RawLine, che contiene miniatura, metadati, hash e dove sta l'originale. Con un doppio clic si apre l'anteprima e si ripristina. Se il segnaposto viene spostato, il ripristino va lì.
7. **Ripristino mai in sovrascrittura**: di default in una cartella nuova o affiancato, con conferma esplicita per sovrascrivere.
8. **Ripristino da progetto** (P5 8.0): dato un FCPXML, un progetto Resolve o un catalogo Lightroom, trova e riporta indietro solo i file usati, anche se i percorsi sono cambiati, grazie all'hash.
9. **Riconoscimento dei file spostati** (come INC+): un file con hash già archiviato non viene archiviato di nuovo, si aggiorna solo il percorso.
10. **Drilldown** come vista standard: tutti i media di un albero in un'unica griglia.
11. **Rinomina in blocco con variabili**, ma con anteprima affiancata vecchio/nuovo, annulla e registro: le sicurezze che Kyno non documenta.
12. **Una sola ricerca** su tutto (online, offline, archiviato, copie) e non "cerca nel backup oppure nell'archivio" (critica di Larry Jordan a P5).
13. **Cruscotto dello spazio** per progetto o cartella e andamento nel tempo (dashboard 8.0): dove sono i TB, cosa è archiviato in modo sicuro e quindi liberabile.
14. Fusione dei metadati tra copie dello stesso archivio (come Kyno 1.6), utile con due dischi gemelli.

## Cose da NON copiare

- Formato dei sidecar chiuso e non documentato, legato al nome del file (Kyno): rinominare nel Finder fa perdere il lavoro.
- Formato di archivio proprietario che si legge solo con l'app (formato nativo P5): RawLine Space deve lasciare **file normali su dischi normali**, leggibili senza l'app.
- Cancellazione dell'originale come effetto automatico dell'archiviazione (vecchia Archive App: "dopo l'archiviazione riuscita, gli originali vengono cancellati") senza un passaggio di verifica e conferma visibile.
- Ripristino che va di default al percorso originale e può sovrascrivere.
- Architettura server e web, rivenditori, configurazione da tecnico IT, voci di moduli non inclusi in licenza: per un fotografo sul campo serve un'app Mac nativa e autonoma.
- Licenza o accesso che può bloccare la consultazione del proprio archivio (caso del lettore con licenza e IP): l'archivio deve restare leggibile anche se l'app non è aggiornata o la licenza è scaduta.
- Sviluppo fermo per anni e aggiornamento automatico che scarica la versione sbagliata (Kyno 1.9).
- Integrazioni o funzioni cloud: tutto offline, come da regola RawLine. Il modulo cloud Synchronize di P5 non ci riguarda.

## Fonti (link)

Kyno
- Note di versione ufficiali: https://support.lesspain.software/support/solutions/articles/12000016005-release-notes-for-kyno
- Dove Kyno salva i dati (supporto Lesspain): https://lesspain.freshdesk.com/solution/articles/12000007801-where-content-is-stored-by-kyno
- Pagina prodotto: https://lesspain.software/kyno/
- NeoFinder, metadati Kyno (.LP_Store/.lpmd): https://www.cdfinder.de/guide/22/22.10/catalog_KYNO.html
- Digital Production, Kyno 1.9 (set. 2025): https://digitalproduction.com/2025/09/19/kyno-update-still-alive-still-useful/
- CineD, Kyno 1.6: https://www.cined.com/kyno-1-6/
- Larry Jordan, recupero media legacy: https://larryjordan.com/articles/recover-legacy-media-using-kyno/
- Larry Jordan, first look: https://larryjordan.com/articles/first-look-kyno-media-management-software/
- OWC Jellyfish, batch rename e Kyno: https://www.owc.com/support/jellyfish/batch-rename , https://www.owc.com/support/jellyfish/kyno-for-jellyfish
- PremiereBro, 10 modi di usare Kyno: https://premierebro.squarespace.com/blog/10-ways-kyno-can-speed-up-your-pre-editing-premiere-pro-workflow
- ProVideoCoalition, acquisizione Signiant: https://www.provideocoalition.com/signiant-acquires-kyno-developer-lesspain-software/
- Partnership Archiware (2019): https://lesspain.software/kyno/pages/news/partnership-with-archiware-and-integration-with-archiware-p5-archive/
- Capterra (prezzi): https://www.capterra.com/p/203547/Kyno/

Archiware P5
- P5 Archive: https://www.archiware.com/products/p5-archive
- Mini-MAM: https://www.archiware.com/solutions/mini-mam
- P5 Companion (blog): https://www.archiware.com/blog/p5-companion-app/
- Datasheet P5 Archive App (.p5a): https://stjernholmco.dk/upload_dir/shop/Datasheet_P5_Archive_App_EN.pdf
- P5 8.0 (StorageNewsletter, feb. 2026): https://www.storagenewsletter.com/2026/02/17/archiware-releases-p5-version-8-0-with-cloud-synchronize-support/
- Larry Jordan, recensione P5 Desktop Edition: https://larryjordan.com/articles/product-review-archiware-p5-desktop-edition/
- G2, prezzi: https://g2.com/products/archiware-p5-archive/pricing
- P5 Archive DLM: https://www.archiware.com/products/p5-archive-dlm
- P5 Synchronize: https://archiware.com/products/p5-synchronize
- Integrazioni P5: https://www.archiware.com/p5-integrations/

CatDV
- Guida all'archiviazione: https://catdv-docs.services.quantum.com/tutorials/archiving/Getting-Started-with-Archiving.html
- Plugin Archiware: https://catdv-docs.services.quantum.com/archiving-plugins/archiware-v2.x/index.html
- Cache-A, archiviazione e ripristino: https://catdv-docs.services.quantum.com/tutorials/archiving/Cache-A-Archive-and-Restore.html
- Media e metadati offline: https://catdv-docs.services.quantum.com/catdv-client/14/Viewing-media-and-media-metadata.html
