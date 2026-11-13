# Copia verificata e ASC MHL — ricerca per RawLine Space

*Ricerca dell'11 novembre 2026. Legenda: **[V]** = verificato su fonte ufficiale o misurato qui; **[D]** = dedotto o non confermato.*

---

## 1. Panoramica

Nel cinema la "copia sicura" ha tre ingredienti, e tutti i programmi seri li hanno:

1. **Hash calcolato mentre si legge la sorgente** (nessuna lettura in più), di solito **xxHash64 big-endian (XXH64BE)**, che è lo standard di fatto (Hedge, Pomfort e Frame.io lo usano tutti). [V]
2. **Rilettura della destinazione** dopo la scrittura, nuovo hash, confronto con quello della sorgente. [V]
3. **Verifica della sorgente** (facoltativa ma consigliata): la sorgente viene riletta una seconda volta, così tre hash devono coincidere. Serve a scoprire schede o lettori che restituiscono dati diversi a ogni lettura. Altrimenti la destinazione "verifica" un dato già corrotto in lettura (falso positivo). [V, Pomfort]

A tutto questo si aggiunge un **manifesto** (MHL) scritto nella cartella copiata. Contiene percorsi relativi, dimensioni, date e hash, e permette di **riverificare la copia mesi dopo, su un altro Mac e con un altro programma**. ASC MHL (spec v1.0, 15 marzo 2022, formato XML "2.0") aggiunge la **cronologia**: ogni copia o verifica produce una nuova "generazione" immutabile, legata alle precedenti da un file catena. Ne risulta una **catena di custodia** che dice quando e dove un file si è rovinato. [V]

Le modalità che si trovano ovunque sono quattro, dalla più veloce alla più sicura:

| Modalità | Cosa controlla | Letture | Sicura per cancellare l'originale? |
|---|---|---|---|
| Solo dimensione | dimensione sorgente = dimensione destinazione | 1 sorgente | **No** (lo dicono Hedge e Pomfort) |
| Sorgente→destinazione | hash in lettura + rilettura destinazione | 1 sorgente + 1 destinazione | Sì, nella pratica |
| + verifica sorgente | come sopra + seconda lettura della sorgente | 2 sorgente + 1 destinazione | Sì, la più robusta |
| Solo verifica (in-place) | ricalcolo hash contro un MHL esistente | 1 | serve per controllare archivi già fatti |

Per RawLine Space (spostare, non solo copiare, su 40–100 TB) il minimo accettabile è **sorgente→destinazione con rilettura**. La cancellazione dell'originale va fatta solo per i file con esito "verified".

---

## 2. Le app una per una

### Hedge OffShoot (Mac/Windows)

- **Modalità di verifica** (da 24.3, in Impostazioni › Transfers › Verification) [V, docs.hedge.video]:
  - **Transfer** (predefinita): confronta *solo le dimensioni* di sorgente e destinazioni. È la più veloce, e Hedge stessa dice di non usarla se si cancellano le sorgenti. A copia finita, quando il disco è libero, riverifica in automatico l'ASC MHL appena scritto sulla destinazione. Se trova un problema riprova a copiare il file dalla sorgente o da un'altra destinazione.
  - **Source**: legge la sorgente prima della copia ("pre-read") per escludere errori di lettura. Controlla l'hash della sorgente e la dimensione della destinazione. È consigliata come predefinita da attivare.
  - **Source & Destination** (l'ex "Archive"): rilegge tutto e produce un terzo hash. "Tipicamente il doppio del tempo" di Transfer. È **obbligatoria per scrivere ASC MHL**.
  - Nomi vecchi delle stesse modalità: Checkpoint OFF / ON (Backup) / ON (Archive). L'app separata Checkpoint è stata assorbita in OffShoot. [V]
- **Hash**: XXH64BE sempre, calcolato dalla sorgente. MD5, SHA1 e C4 sono "legacy", attivabili singolarmente o tutti insieme, e "possono rallentare". [V]
- **MHL awareness**: se la sorgente ha già un (ASC) MHL, OffShoot usa quegli hash invece di rileggere. Lo fa solo se **dimensione e data di modifica coincidono**. [V]
- **Verifica successiva**: doppio clic su un .mhl, poi Verify. Controlla file mancanti e hash e verifica ogni MHL della catena. Su Windows (25.2+) si può verificare in blocco tutti gli MHL di un disco. Dalla 25.1 i risultati della verifica finiscono anche nella catena ASC MHL. [V]
- **Altri controlli**: a fine copia controlla che tutti i file esistano sulla destinazione. Avvisa se trova **file da 0 byte** sulla sorgente (tipico di schede exFAT estratte male). [V]
- **Stop & Resume** (24.1+): si possono riprendere anche i trasferimenti falliti o "completati con avvisi". La ripresa *riparte da capo saltando i file già presenti* (regole di Duplicate Detect). **I file copiati o verificati a metà non riprendono**: si ricopiano. Se cade il disco di destinazione, il log viene scritto in locale. La ripresa produce un log nuovo e MHL nuovi che coprono **solo i file appena copiati**. [V]
- **Log e report**: un Transfer Log per ogni trasferimento, sempre in locale (`~/Library/Application Support/Hedge/Transfer Logs`) e facoltativamente sulla destinazione. I report uniscono più log e accettano logo, titolo, note e una sezione clip con miniature e metadati. [V]
- **Prezzi** [V, hedge.co]: OffShoot **$169** perpetua, OffShoot Pro **$249** perpetua, oppure Pro in abbonamento ($49, la pagina è ambigua su mese o anno). Prova di 10 giorni. ASC MHL, preset avanzati e copie a cascata sono solo nel Pro.
- **Critiche di Hedge allo standard** [V, blog]: ASC MHL "scala male con milioni di file", non ha S3 nativo, e la spec non tiene conto dell'hash "eroe" della sorgente (si verifica solo l'ultimo riferito). MD5 è lento e sconsigliato.

### Hedge Canister

App per archiviare su **LTO/LTFS**, una o più cassette. Produce log di trasferimento, MHL e manifesti, e verifica tutto quello che scrive su nastro (Checkpoint integrato). I cataloghi si montano come disco di rete cercabile dal Finder. Prezzo ~**$399** da rivenditore (storico $349–399), in bundle con OWC Archive Pro. [V da recensioni e rivenditori; prezzo ufficiale non trovato]. È rilevante solo se un giorno RawLine Space vorrà parlare di nastro.

### Hedge Postlab

Serve alla condivisione di progetti NLE (FCP/Premiere/Resolve) in team via cloud. **Non riguarda la copia verificata**, ed essendo in cloud è comunque fuori dalla regola offline di RawLine. [D, noto, non riverificato oggi]

### Pomfort Silverstack XT / Offload Manager / MediaVerify

- **Processo di copia** [V, pomfort.com]: l'hash si calcola leggendo la sorgente e si salva nella libreria. Poi la destinazione si rilegge e si confronta. Con la **verifica della sorgente** (attiva di default) la sorgente si rilegge dopo la copia e tre hash devono coincidere. Gira *in parallelo* alla verifica della destinazione, quindi "di solito non aggiunge tempo". Aggiunge tempo solo se la sorgente è più lenta delle destinazioni. È nata dai casi RED One con schede consumate che davano letture diverse. Pomfort: "fortemente consigliato copiare sempre con verifica della sorgente".
- **Solo dimensione** ("File Size Verification Only"): esiste, ma Pomfort dice che non dà sicurezza reale. Anche in questo caso Silverstack calcola comunque xxHash durante la copia e lo salva. [V]
- **Hash** (Offload Manager): XXH64, MD5, SHA1, C4ID, XXH3, XXH128. Per le copie a cascata si scelgono copertura e algoritmi per ogni passaggio. [V]
- **Stati di verifica** per file (Silverstack 6.4+): **Verified** (verde), **Defect** (rosso), **Not Verified** (grigio). Si propagano verso l'alto (file › clip › bin › cartella) con priorità Defect > Not Verified > Verified. [V]
- **ASC MHL**: crea e **continua** cronologie ASC MHL (Offload Manager dalla 1.5, impostazione in "Copy & Job"). Può scrivere MHL anche per job falliti o annullati. [V da changelog e ricerca]
- **Ripresa**: i job di copia e di verifica si annullano e si riprendono più tardi dal pulsante "…" accanto alla barra. [V, manuale]
- **Report**: PDF, CSV, HTML e stampa diretta. [V]
- **Completezza** [V, articolo Pomfort]: la completezza va definita *dalla sorgente*, perché una lista fatta da ciò che è stato copiato non può mostrare cosa manca. Il manifesto va scritto **solo a copie finite**, così una copia fallita non lascia un manifesto parziale che sembra buono. Per controllare un insieme di cartelle serve una "lista di liste" (seal di Silverstack o MHL annidati).
- **MediaVerify**: **gratuito**, Mac/Windows. Verifica cronologie ASC MHL, fa una scansione di completezza (file mancanti e nuovi, basata su `diff`) prima di calcolare gli hash, mostra la cronologia per file (generazioni, algoritmi, date, autore) e produce report e log di testo. Non legge il "classic MHL" (per quello c'è SealVerify, ormai a fine vita). [V]
- **Prezzi** [V, store Pomfort]: Silverstack XT **849 USD/anno** (Silverstack base non si vende più). Offload Manager in licenze a tempo da 14 giorni, 1 mese o 1 anno, pagamento singolo, cifre non visibili nella pagina [prezzo non confermato]. Silverstack Lab ~€1.199/anno da rivenditore [V da rivenditore]. Allo scadere i progetti diventano di sola lettura.

### ShotPut Pro (Imagine Products, Mac/Windows)

- **Opzioni di verifica** [V, knowledge base del produttore tramite ricerca]: XXHash-64, XXHash3-64, XXHash-128, MD5, SHA-1, SHA-256, SHA-512, C4, CRC-32, **File Size Comparison** (la più veloce).
- **MHL**: report MHL dalla versione Mac 2019.2. Il supporto **ASC MHL** non risulta confermato nelle fonti trovate. [D]
- **Pausa e ripresa** dei trasferimenti, annullamento parziale e notifiche desktop. [V da stampa di settore]
- **Report PDF** "orientati ai media". [V, sito]
- **Prezzo**: perpetua **$149–169** (G2: $169), 12 mesi di aggiornamenti inclusi, poi $39–49/anno. Noleggi da 15 o 45 giorni ($19/$49 nel 2019). Attivazione online, un computer per licenza. [V da terze parti; prezzo attuale da confermare sul sito]

### Altri citati nelle fonti

TeraCopy (gratis, molti algoritmi, niente MHL), DaVinci Resolve Clone (gratis, solo MD5, lento), OWC Copy That, WrangleBot (open source), Limecraft Edge (MD5, xxHash64, XXH3 e ASC MHL dalla 2026.3). [V da articoli]

---

## 3. Lo standard ASC MHL nel dettaglio

**Fonti primarie**: specifica ASC MHL v1.0 del 15 marzo 2022 (ASC Advanced Data Management Subcommittee) e implementazione di riferimento `ascmhl` su GitHub. Tutto quanto segue è **[V]** dalla specifica, salvo dove indicato.

### Concetti

- **Manifesto** (`.mhl`, XML UTF-8): un'istantanea immutabile ("una volta creato non si modifica") degli hash di un insieme di file. I percorsi sono relativi alla cartella radice (lo "scope").
- **Cronologia (History)**: la cartella `ascmhl/` nella **radice** della cartella gestita, con tutti i manifesti più il file catena. Siccome sta dentro la cartella, **viaggia con i dati** quando li copi. Può contenere un `README.txt` facoltativo.
- **Catena**: `ascmhl/ascmhl_chain.xml`, l'indice della cronologia. Per ogni manifesto riporta `sequencenr` (1, 2, 3… continui), il percorso e il **hash C4 del manifesto stesso**, così si accorge se qualcuno ha alterato un manifesto.
- **Collezione**: `ascmhl_collection.xml`, stesso schema della catena ma con manifesti di scope diversi. Fa da "bolla di consegna" (per esempio più schede mandate per mail).
- **Cronologie annidate**: una sottocartella può avere il proprio `ascmhl/`. Ogni file va registrato nella cronologia **più vicina**, e quella superiore contiene solo riferimenti (`hashlistreference` con percorso e C4). Una verifica dall'alto crea nuove generazioni in tutte le cronologie annidate. Le modifiche in basso non risalgono.

### Nome dei manifesti

`<numero>_<nomecartella>_<YYYY-MM-DD>_<HHMMSS>Z.mhl`, ad esempio `0001_A002R2EC_2019-01-07_080228Z.mhl`. Il numero è progressivo a 4 cifre (o più) e parte da 1. Data e ora sono **UTC**, prese all'inizio dell'operazione e uguali in tutti i manifesti creati da quella stessa operazione.

### Struttura XML (namespace `urn:ASC:MHL:v2.0`, `version="2.0"`)

```xml
<hashlist version="2.0" xmlns="urn:ASC:MHL:v2.0">
  <creatorinfo>
    <creationdate>…</creationdate>   <!-- obbligatorio -->
    <hostname>…</hostname>           <!-- obbligatorio -->
    <tool version="1.0">RawLine Space</tool> <!-- obbligatorio -->
    <author email="" role="">…</author>   <!-- facoltativi: author, location, comment -->
  </creatorinfo>
  <processinfo>
    <process>transfer</process>      <!-- in-place | transfer | flatten -->
    <roothash>…content/structure…</roothash>   <!-- facoltativo -->
    <ignore><pattern>.DS_Store</pattern></ignore>
  </processinfo>
  <hashes>
    <hash>
      <path size="…" creationdate="…" lastmodificationdate="…">Cartella/file.ARW</path>
      <xxh64 action="original" hashdate="…">7680e5f98f4a80fd</xxh64>
      <previousPath>…</previousPath>  <!-- solo dopo una rinomina -->
      <metadata>…</metadata>          <!-- libero -->
    </hash>
    <directoryhash> … <content>…</content><structure>…</structure> </directoryhash>
  </hashes>
  <metadata>…</metadata>
  <references><hashlistreference><path>…</path><c4>…</c4></hashlistreference></references>
</hashlist>
```

- **action** su ogni hash di file: `original` (primo hash nella cronologia), `verified` (ricalcolato e uguale a un hash precedente), `failed` (ricalcolato e diverso, quindi il file è cambiato). Gli hash `failed` non si usano mai per verificare.
- **process**:
  - `in-place` crea il manifesto senza copiare (per esempio dopo una copia fatta col Finder).
  - `transfer` copia e scrive il manifesto insieme. Lo strumento **garantisce** che sorgente e destinazione siano identiche, confrontando gli hash o "altri mezzi in buona fede".
  - `flatten` copia gli hash da altri manifesti senza ricalcolarli.
- **Percorsi**: maiuscole e spazi preservati, separatore `/`, niente `/` iniziale, niente `..`.
- **Ignore**: sintassi `.gitignore`. Di default si ignorano `.DS_Store` e le cartelle `ascmhl`.
- **Hash di cartella**: `content` (hash degli hash dei figli) e `structure` (hash di nome più hash). La procedura "hash di hash" (Appendice G) ordina gli hash dei figli lessicograficamente, li codifica in byte e li passa in sequenza allo stesso algoritmo.

### Algoritmi (Appendice D)

| Elemento | Algoritmo | Codifica |
|---|---|---|
| `xxh64` | XXH64, seed 0, big-endian | 16 caratteri esadecimali |
| `xxh3` | XXH3 64 bit, seed 0, big-endian | 16 caratteri esadecimali |
| `xxh128` | XXH3 128 bit, seed 0, big-endian | 32 caratteri esadecimali |
| `md5` | MD5 | 32 caratteri esadecimali |
| `sha1` | SHA-1 | 40 caratteri esadecimali |
| `c4` | SHA-512 in Base58 con prefisso "c4" (SMPTE ST 2114) | 90 caratteri |

**SHA-256 non c'è nello schema XSD v2.0.** Il README di ascmhl lo citava, ma l'XSD elenca solo i sei qui sopra [V]. Nello stesso manifesto possono convivere più algoritmi, e si può cambiare algoritmo tra una generazione e l'altra. Però la verifica deve usare un algoritmo **già presente** nella cronologia.

### Operazioni che uno strumento conforme deve supportare

- **Create**: con hash di tutti i file non ignorati e non già coperti da cronologie annidate. Se è la prima, crea `ascmhl/` e la catena.
- **Diff**: **senza calcolare hash**, elenca i file *sconosciuti* (presenti ma non registrati) e quelli *mancanti*. È velocissimo.
- **Verify**: ricalcola gli hash e li confronta. Un file mancante conta come fallito. Su una cronologia **aggiunge sempre una nuova generazione** con l'esito.
- **History Append**: dopo una verifica, oppure quando si aggiungono file (il nuovo manifesto contiene solo quelli nuovi).
- **Rename**: nuova generazione con `previousPath`. Gli strumenti devono saper seguire le rinomine.
- **Flatten**: unisce la cronologia in un manifesto autonomo, senza i `failed` e con un solo hash per algoritmo (il più vecchio).
- **Limite dichiarato**: una modifica *voluta* a un file (tranne la rinomina) lo fa risultare `failed` per sempre, perché la v1.0 non prevede come "riabilitarlo". Un danno involontario si ripara rimettendo una copia buona.

### Lo strumento `ascmhl` (github.com/ascmitc/mhl)

- **Licenza MIT** [V], Python ≥ 3.11, ultima versione **1.2 del 4 luglio 2025** (PyPI) [V].
- Dipendenze: click, lxml, pathspec, xxhash, python-dateutil, packaging, requests. [V, setup.py]
- Comandi:
  - `ascmhl create`: hash, confronto con la cronologia, nuova generazione. Con `-sf` aggiunge un singolo file.
  - `ascmhl diff`: senza hash.
  - `ascmhl info`: generazioni. Con `-sf` mostra la cronologia di un file.
  - `ascmhl flatten`: implementato solo in parte.
  - `ascmhl-debug verify`, `xsd-schema-check`, `hash`.
- **Limiti dichiarati nel README** [V]: rilevamento e gestione delle rinomine **non implementati**, il file catena **non viene verificato**, alcune opzioni di info e flatten sono incomplete.
- Nel repo c'è anche l'**XSD** ufficiale (`xsd/ASCMHL.xsd`, `ASCMHLDirectory.xsd`). Ci sono anche implementazioni di terzi (per esempio `batikstudio/MhlFileVerify`), non valutate.

### Si può fare in RawLine Space, in locale?

**Sì, ed è la strada consigliata.** [D, ragionamento]

- Il formato è XML pubblico con XSD pubblico. È fattibile scrivere e leggere manifesti in Swift (XMLDocument o XMLParser di Foundation) senza alcuna dipendenza esterna.
- xxHash è BSD-2. Si può incorporare la libreria C (`xxhash.h`, header-only) nel target Swift, oppure usare un pacchetto Swift. MD5, SHA1 e SHA-512 per C4 sono già in **CryptoKit/CommonCrypto**. Il Base58 per C4 sono poche righe.
- **Non conviene** includere lo strumento Python nell'app: serve Python 3.11 più lxml compilato, e su un'app Mac firmata è complicato. Inoltre non verifica la catena e non gestisce le rinomine. Va però usato **come riferimento nei test**: generare MHL con RawLine Space, controllarli con `ascmhl-debug xsd-schema-check` e `ascmhl verify`, e viceversa. La licenza MIT permette anche di **leggerne e portarne la logica** (con la nota di copyright).
- La verifica incrociata con **MediaVerify di Pomfort** (gratis) e con OffShoot dà la prova di compatibilità reale.
- Tutto gira offline, nel rispetto della regola RawLine. Il pacchetto ascmhl dipende da `requests`, ma il formato in sé non richiede rete. [V/D]

### Velocità degli hash, misurata su questo Mac (Apple M1 Max) [V]

Dati in memoria, quindi il limite della CPU, non del disco:

| Algoritmo | Velocità (1 core) |
|---|---|
| XXH3-64 / XXH128 | ~35 GB/s (`xxhsum -b`, 0.8.3, NEON) |
| XXH64 | ~13,5 GB/s |
| SHA-1 / SHA-256 | ~2,4 GB/s (`openssl speed`, accelerazione hardware ARM) |
| MD5 | ~0,68 GB/s |

**Cosa significa sui dischi grandi** [D, calcolo]:

- Qualsiasi xxHash è più veloce di ogni disco (HDD ~150–280 MB/s, RAID ~1–2 GB/s, SSD Thunderbolt ~2–3 GB/s). **Il collo di bottiglia è sempre l'I/O.**
- MD5 invece può frenare un RAID o un SSD veloce. SHA-256 su Apple Silicon è sorprendentemente decente, ma non serve.
- 100 TB letti una volta a 250 MB/s richiedono **circa 4,6 giorni**. Un trasferimento con rilettura della destinazione richiede circa 9 giorni di soli dischi, a meno che la rilettura non si sovrapponga alla copia del file successivo.

**Scelta consigliata**: XXH64BE come predefinito (massima compatibilità con OffShoot, Silverstack e Frame.io). Hash aggiuntivo XXH128 come opzione. MD5 e SHA1 solo se un cliente li chiede.

---

## 4. Gestione errori e ripresa

| Situazione | Come la trattano | Fonte |
|---|---|---|
| Hash della destinazione diverso | OffShoot (Transfer) riprova a copiare il file dalla sorgente o da un'altra destinazione. In Source & Destination completa "con avvisi". Silverstack marca il file Defect (rosso) | [V] |
| Errore di lettura della sorgente | OffShoot (Source) **ferma** il trasferimento. Silverstack segnala la sorgente in modo distinto dalla destinazione | [V] |
| File mancanti a fine copia | OffShoot avvisa e scrive un warning nel log. ASC MHL Verify conta un file mancante come fallito | [V] |
| File da 0 byte sulla sorgente | OffShoot avvisa (schede exFAT estratte male) | [V] |
| Interruzione (stop, disco staccato, crash) | OffShoot riparte saltando i file già presenti e **ricopia da zero i file a metà**. Pomfort riprende copia e verifica dal job | [V] |
| Destinazione scollegata | OffShoot scrive il log in locale perché non può scrivere log o MHL sul disco perso | [V] |
| MHL dopo una ripresa | OffShoot crea un MHL nuovo **solo per i file nuovi**. Con ASC MHL diventa una nuova generazione | [V]/[D] |
| Manifesto parziale | Pomfort scrive il manifesto solo a copie finite e può anche creare MHL per job falliti o annullati | [V] |
| Riverifica a distanza di tempo | OffShoot (doppio clic sull'MHL), MediaVerify (gratis), `ascmhl verify`. Ogni verifica aggiunge una generazione | [V] |

Punti tecnici dedotti, da tenere a mente [D]:

- **"Skip se già presente" è pericoloso se si basa solo su nome e dimensione**: un file troncato o di uguale dimensione ma corrotto passerebbe. La ripresa va basata su un **giornale locale** dello stato dei singoli file, non sul solo contenuto della destinazione.
- La **cache del sistema operativo** può far sembrare riuscita una rilettura che in realtà legge la RAM. Per una vera rilettura dal disco su macOS serve `F_NOCACHE` (fcntl) sul file in lettura, oppure lo svuotamento della cache. I produttori non lo documentano, ma "readback" ha senso solo così.
- La scrittura va fatta su un file temporaneo nella destinazione (`.nome.rawline-part`), con `fsync` e `F_FULLFSYNC` prima di rinominarlo col nome definitivo. Un file col nome finale deve essere sempre un file completo.

---

## 5. Idee da prendere per RawLine Space (concrete)

1. **Tre modalità con nomi chiari**, con la prudente come predefinita per lo **spostamento**:
   - "Rapida" (solo dimensione): consentita **solo per copiare**, mai per spostare. Il pulsante "togli originale" resta disattivato.
   - "Sicura" (hash in lettura + rilettura della destinazione): predefinita.
   - "Massima" (+ seconda lettura della sorgente, in parallelo alla rilettura della destinazione, come Pomfort): consigliata per dischi vecchi o sospetti.
2. **Cancellare l'originale solo file per file e solo con esito `verified`**. Meglio ancora: spostare nel Cestino del disco sorgente, non cancellare in modo definitivo, e svuotare il cestino solo dopo un secondo controllo, a scelta dell'utente.
3. **ASC MHL nativo in Swift**:
   - `ascmhl/` nella radice di ogni cartella spostata, un manifesto `process=transfer` per ogni spostamento e la catena con il C4 dei manifesti.
   - Se la sorgente ha già una cronologia, **continuarla** (nuova generazione con `verified`) invece di crearne una nuova.
   - In `creatorinfo/tool` "RawLine Space" con la versione, `hostname`, autore facoltativo.
4. **MHL awareness alla OffShoot**: se la sorgente ha già un MHL e dimensione e data coincidono, si confronta con quegli hash. È anche la verifica gratuita della *sorgente* rispetto al passato: ci dice se l'archivio si era già rovinato prima dello spostamento.
5. **Diff prima di tutto (senza hash)**: una scansione rapida di file mancanti e nuovi rispetto all'MHL, come MediaVerify. Su 100 TB fa vedere in pochi minuti cosa manca, prima di giorni di hash.
6. **"Riverifica archivio" come funzione a sé**, programmabile (per esempio un disco al mese). Ogni passaggio aggiunge una generazione, e dà al fotografo la "catena di custodia" del proprio archivio negli anni. È qualcosa che nel mondo foto nessuno offre. [D]
7. **Giornale di lavoro locale** (SQLite nell'app): stato per file (da copiare, copiato, verificato, originale tolto), hash e tempi. La ripresa dopo crash o distacco usa il giornale: i file "a metà" si ricopiano, quelli "verificati" si saltano senza rileggerli. Il rapporto finale spiega cosa è stato fatto.
8. **Stati a semaforo con propagazione** (come Silverstack): verde verificato, rosso difetto, grigio non verificato, propagati a cartella, progetto e disco, con priorità rosso > grigio > verde.
9. **Controlli d'avvio della copia**: spazio libero sulla destinazione e file system. Avvisare su exFAT/FAT per file > 4 GB e su nomi non portabili. Segnalare **file da 0 byte**, e i **nomi uguali che differiscono solo per maiuscole/minuscole** (APFS di solito non distingue).
10. **Report**: un PDF leggibile (riassunto, disco sorgente e destinazione, numero di file, TB, durata, velocità media, eventuali avvisi) più un log di testo dettagliato, salvati in locale e sulla destinazione. Il fotografo lo può allegare alla consegna al cliente.
11. **Hash predefinito XXH64BE**. In più, XXH128 opzionale. MD5 e SHA1 solo su richiesta, con l'avviso che rallentano.
12. **Test di compatibilità automatici**: MHL scritti da RawLine Space validati con l'XSD ufficiale e verificati con `ascmhl`, e MHL di riferimento (dal repo ascmhl, con licenza MIT) letti da RawLine Space. Una prova a mano con MediaVerify e OffShoot.
13. **Scalabilità**: Hedge critica ASC MHL per i milioni di file, e un archivio foto ne ha tantissimi. La cronologia va quindi **annidata per cartella significativa** (servizio o giornata), non un solo manifesto gigante alla radice del disco. In radice basta un manifesto con soli `references`. Il parser XML va usato in streaming (XMLParser), non caricando un DOM da centinaia di MB. [D]

---

## 6. Cose da NON copiare

- **La predefinita "Transfer" di OffShoot (solo dimensione)**: va bene per una copia, ma è pericolosa per un'app che *sposta*. Hedge stessa dice di non cancellare le sorgenti con quella modalità.
- **Funzioni ASC MHL a pagamento a parte** (in Hedge sono solo nel Pro): per RawLine Space la sicurezza è il cuore del prodotto, non un'opzione premium.
- **Abbonamenti con progetti in sola lettura alla scadenza** (Pomfort): un archivio di decine di TB non deve diventare illeggibile se la licenza scade. Gli MHL sono comunque aperti, ma l'app deve sempre permettere almeno di leggere e verificare.
- **Attivazione online obbligatoria** (ShotPut Pro, attivazioni di rete): è contro la regola offline di RawLine.
- **MD5 come predefinito** (Resolve Clone): è lento senza motivo.
- **Ripresa basata solo su "il file c'è già"**: OffShoot salta i file già presenti in base alle regole di duplicato. Per spostare serve il giornale locale con lo stato di verifica.
- **MHL parziali che sembrano completi**: il manifesto va chiuso solo a fine lavoro, oppure marcato chiaramente come lavoro interrotto (con `comment` o `metadata`).
- **Dipendere dallo strumento Python ascmhl dentro l'app**: è incompleto su rinomine e catena, e porta Python e lxml in un'app firmata.
- **Gergo da DIT nell'interfaccia** ("Checkpoint ON (Archive)", "Cascading", "Hero checksum"): per i fotografi servono parole semplici. Hedge stessa ha rinominato le modalità nella 24.3 per questo.
- **Cloud e S3** (OffShoot Pro, Postlab): è fuori dal perimetro RawLine.

---

## 7. Fonti

**ASC MHL**
- Specifica ASC MHL v1.0 (15/03/2022): https://cdn.theasc.com/ASCMHL_Specification_v1.0.pdf
- One-sheet ASC MHL: https://cdn.theasc.com/ASCMHL_One-Sheet_v1-1_210121_102845.pdf
- Repo strumento e XSD: https://github.com/ascmitc/mhl
- Repo specifica: https://github.com/ascmitc/mhl-specification
- PyPI ascmhl (1.2, 4/7/2025, MIT): https://pypi.org/project/ascmhl/
- setup.py (dipendenze): https://raw.githubusercontent.com/ascmitc/mhl/master/setup.py
- Frame.io, "Media Hash Lists 101": https://blog.frame.io/2022/08/22/mhl-media-hash-lists-workflow/
- PRONOM (formato registrato): https://www.nationalarchives.gov.uk/PRONOM/fmt/1765

**Hedge**
- OffShoot prodotto e prezzi: https://hedge.co/products/offshoot
- Verifica: https://docs.hedge.video/offshoot/features/verification
- Stop & Resume: https://docs.hedge.video/offshoot/features/stop-and-resume
- Logging: https://docs.hedge.video/offshoot/features/logging
- Release notes: https://docs.hedge.video/offshoot/releases
- Blog OffShoot 24.3: https://hedge.co/blog/offshoot-24-3
- Blog ASC MHL: https://hedge.co/blog/asc-mhl
- Canister (recensione): https://www.provideocoalition.com/canister-for-macos-the-lingua-franca-of-lto-tape-drive-data-storage/
- Canister (rivenditore, prezzo): https://reach.dog/shop/mlogic/products/hedge-canister-ltfs-archiving-software-for-macos

**Pomfort**
- Offload Manager, funzioni: https://pomfort.com/offloadmanager/features/
- Offload Manager, licenze: https://pomfort.com/store/offloadmanager/licenses/
- Manuale Offload Manager: https://kb.pomfort.com/manuals/Offload-Manager-Manual.pdf?v=1.5
- Changelog Offload Manager: https://updates.pomfort.com/offloadmanager/changelog.php
- Silverstack store: https://pomfort.com/store/silverstack
- Verifica della sorgente: https://pomfort.com/article/how-source-verification-helps-identify-underlying-problems-in-your-copy-process/
- Completezza e manifesti: https://pomfort.com/article/managing-data-part-two-completeness-of-data-with-manifest-files/
- Stati di verifica: https://kb.pomfort.com/silverstack/reference/library/verification-states/
- MediaVerify: https://pomfort.com/mediaverify/

**ShotPut Pro**
- Opzioni di verifica (KB): https://imagineproducts.freshdesk.com/support/solutions/articles/35000203787-what-are-the-differences-between-the-verification-options-available-on-shotput-pro-
- Prezzi (G2): https://www.g2.com/products/shotput-pro/pricing
- Noleggi e prezzo 2019: https://studiodaily.com/2019/03/imagine-products-adds-rental-options
- Pausa e ripresa: https://www.tvtechnology.com/the-wire-blog/imagine-products-transforms-media-offloading-with-updates-to-shotput-pro-and-new-imagine-hq-ios-app

**Confronti e hash**
- Confronto programmi di copia: https://alexanderzhodge.substack.com/p/exploring-checksum-verification-and
- xxHash (BSD-2): https://github.com/Cyan4973/xxHash
- Misure locali: `xxhsum -b` 0.8.3 e `openssl speed` 3.6.2 su Apple M1 Max, 11/11/2026.

*Nota: i prezzi di Offload Manager, di ShotPut Pro attuale e di Canister non sono confermati dai siti ufficiali (pagine senza cifre o non raggiungibili).*
