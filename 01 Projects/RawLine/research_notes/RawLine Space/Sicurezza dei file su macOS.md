# Sicurezza dei file su macOS — ricerca tecnica per RawLine Space

Data: 11 novembre 2026. Contesto: app Swift fuori App Store (Developer ID), archivi da 40–100 TB su dischi esterni (RAID/DAS), file system APFS, HFS+, exFAT, forse SMB. Regola: mai perdere o corrompere un file, ogni operazione registrata e annullabile anche dopo un crash, niente eliminazioni immediate. Tutto deve funzionare offline: nessuna delle tecniche qui sotto usa la rete.

**Legenda**
- **[Provato]**: verificato su questo Mac (M1 Max, macOS 26.7.3) con piccoli programmi di prova, sul disco interno APFS e, in sola lettura, sul RAID esterno *G-SPEED Shuttle XL TB3* (HFS+ con journal, montato `noowners`).
- **[Fonte]**: scritto in documentazione Apple, man page, header dell'SDK o articoli tecnici affidabili.
- **[Dedotto]**: ragionamento mio, da verificare con prove.

---

## 1. Rinomina e spostamento atomico sullo stesso volume

**Tecnica consigliata**
- Per ogni rinomina o spostamento sullo stesso volume usare `renamex_np(src, dst, RENAME_EXCL)`, oppure `renameatx_np` con descrittori di cartella. Se la destinazione esiste, la chiamata fallisce con `EEXIST` e non sovrascrive niente. **[Fonte: rename(2)] [Provato su APFS: `File exists`]**
- Prima di tutto chiedere al volume cosa supporta: `getattrlist` con `ATTR_VOL_CAPABILITIES` e i bit `VOL_CAP_INT_RENAME_EXCL` e `VOL_CAP_INT_RENAME_SWAP` (header `sys/attr.h`). Se il flag non è supportato, la chiamata restituisce `ENOTSUP`. **[Fonte: rename(2)]**
- `RENAME_SWAP` scambia due oggetti in un passo atomico, anche un file con una cartella, e richiede che la destinazione esista. Non si combina con `RENAME_EXCL` (dà `EINVAL`). Serve per "sostituisci e tieni il vecchio": si scambia e poi il vecchio va in quarantena. **[Fonte] [Provato su APFS]**
- Conviene aggiungere `RENAME_NOFOLLOW_ANY`, che rifiuta qualunque link simbolico lungo il percorso (`ELOOP`). Per restare dentro la radice dell'archivio c'è `RENAME_RESOLVE_BENEATH` (`ENOTCAPABLE` se si esce); la disponibilità dipende dalla versione di macOS. **[Fonte: man page recente]**
- Spostare tra volumi diversi con `rename` non si può: dà `EXDEV`. Lo spostamento tra volumi va trattato sempre come copia verificata seguita da quarantena dell'originale (sezioni 3 e 4). **[Fonte]**

**Capacità misurate [Provato]**

| Capacità | APFS (interno) | HFS+ (RAID G-SPEED) |
|---|---|---|
| `RENAME_EXCL` | sì | sì |
| `RENAME_SWAP` | sì | **no** |
| `exchangedata` (vecchia API) | no | sì |
| Cloni (`VOL_CAP_INT_CLONE`) | sì | no |
| Snapshot | sì | no |
| Maiuscole/minuscole distinte | no | no |
| Journal | sì | sì |

- **exFAT**: non ha journal. Il codice di Blender lo tratta come file system senza rinomina atomica e ripiega su "controlla, poi rinomina". **[Fonte: Blender, OWC] [Dedotto: interrogare i bit su un volume exFAT reale prima di fidarsi]**
- **SMB/NAS**: il protocollo prevede un flag "sostituisci se esiste" inviato dal client. Samba, lato server, usa `rename()` semplice con una possibile corsa critica (bug Samba 13648). Non ho trovato documentazione su come `smbfs` di macOS tratti `RENAME_EXCL`. **[Fonte parziale] [Dedotto: su SMB leggere i bit e, se mancano, fare controllo più rinomina, accettando il rischio residuo]**

**Rischi**
- `rename()` garantisce l'**atomicità** (dopo un crash esiste il vecchio nome o il nuovo, mai metà), non la **durabilità**. Un ingegnere Apple (DTS) lo conferma e consiglia `F_FULLFSYNC` per essere sicuri che la modifica sia scritta. Non è documentato se `fsync` sulla cartella basti. **[Fonte: forum Apple 849633]**
- Su volumi senza `RENAME_EXCL` (exFAT, forse SMB) tra il controllo e la rinomina un altro processo può creare lo stesso nome. **[Dedotto]**
- Cambiare solo maiuscole o minuscole (`IMG.ARW` → `img.ARW`) su un volume che non le distingue: `RENAME_EXCL` potrebbe vedere "esiste già" sul file stesso. **[Dedotto, da provare]** Si risolve passando da un nome temporaneo univoco, con due rinomine registrate nel journal.

---

## 2. Cloni APFS (clonefile, copyfile con COPYFILE_CLONE)

**Tecnica consigliata**
- Sullo stesso volume APFS, per "duplica" o "copia di sicurezza prima di modificare", usare `copyfile(src, dst, state, COPYFILE_CLONE | COPYFILE_ALL)` e poi leggere `COPYFILE_STATE_WAS_CLONED`. Così si sa se è stato davvero un clone o una copia normale (ripiego automatico). **[Fonte: copyfile(3)] [Provato: `was_cloned=1`]**
- Se si vuole **solo** il clone e mai una copia lenta, usare `COPYFILE_CLONE_FORCE` o `clonefile()`: falliscono con `ENOTSUP` invece di copiare. **[Fonte]**
- `COPYFILE_CLONE` implica già `EXCL`, `STAT`, `XATTR`, `DATA` e `NOFOLLOW_SRC`. Le ACL vanno chieste a parte con `COPYFILE_ACL`. Se il clone riesce, le callback di avanzamento non vengono chiamate. **[Fonte]**
- Per verificare quanto spazio occupa davvero un file: `getattrlist` con `ATTR_CMNEXT_PRIVATESIZE` (opzione `FSOPT_ATTR_CMN_EXTENDED`) dà i byte non condivisi con cloni o snapshot, cioè quanti se ne liberano eliminandolo. **[Fonte: getattrlist(2)] [Provato: subito dopo il clone sia l'originale sia il clone segnano 0]** L'SDK definisce anche `ATTR_CMNEXT_CLONEID` e `ATTR_CMNEXT_CLONE_REFCNT`, ma solo sui volumi con `VOL_CAP_FMT_CLONE_MAPPING`, che sul mio APFS risulta **assente**. **[Provato]**

**Limiti e rischi**
- Un clone non è un backup: condivide i blocchi, quindi un errore del disco li danneggia entrambi. **[Fonte: Eclectic Light] [Dedotto]**
- Finder e `ls` mostrano i cloni a grandezza piena (in un esempio, 70 GB "visibili" con 10 GB reali). Il flag "clonato" resta anche dopo che i contenuti si sono separati. **[Fonte: Eclectic Light 2025]**
- Eliminare un clone, o l'originale, libera poco o niente: lo spazio "liberato" che si mostra all'utente va calcolato con `PRIVATESIZE`, non con la dimensione del file. **[Provato e dedotto]**
- Su HFS+, exFAT e SMB non ci sono cloni (`VOL_CAP_INT_CLONE` = 0 sul RAID HFS+). `COPYFILE_CLONE` lì fa una copia completa, che su file grandi richiede tempo e spazio. Va sempre controllato prima. **[Provato e fonte]**
- Tra volumi diversi un clone non è mai possibile. **[Fonte]**
- `COPYFILE_RECURSIVE` con il clone non è atomico e non segue i link a cartelle. **[Fonte: copyfile(3)]**

---

## 3. Copia verificata tra volumi

**Tecnica consigliata**
1. Copiare in un **file temporaneo** nella cartella di destinazione (per esempio `.rawline-tmp-<uuid>`), mai direttamente con il nome finale.
2. Per i dati si può usare `copyfile` con `COPYFILE_DATA` e la callback di avanzamento, che permette anche di annullare. In alternativa un ciclo proprio `read`/`write` con `F_NOCACHE` su entrambi i file, che evita di riempire la cache con decine di TB letti una sola volta, e con buffer grandi (1–8 MB). **[Fonte: fcntl(2)] [Dedotto: il ciclo proprio permette di calcolare l'hash mentre si legge la sorgente]**
3. Calcolare l'hash della sorgente **durante** la lettura.
4. Copiare i metadati con `copyfile(..., COPYFILE_METADATA)`, cioè attributi estesi (compresi tag Finder, `com.apple.metadata:_kMDItemUserTags`, resource fork, FinderInfo) più permessi, date e ACL. Poi reimpostare data di creazione e di modifica con `setattrlist`, perché scrivere gli xattr può cambiare la data di modifica. **[Fonte: copyfile(3)] [Dedotto]**
5. `fcntl(fd, F_FULLFSYNC)` sul file di destinazione. Se fallisce (succede su alcuni dischi esterni ed exFAT), ripiegare su `fsync` **e annotarlo nel journal** come "durabilità debole". **[Fonte: Bitcoin Core #26455/#26534] [Provato: su APFS interno restituisce 0]**
6. **Rileggere** la destinazione da disco con `F_NOCACHE`, così si legge davvero il disco e non la RAM, ricalcolare l'hash e confrontarlo. Confrontare anche dimensione e numero e contenuto degli xattr.
7. Dare il nome finale con `renamex_np(tmp, finale, RENAME_EXCL)`, poi `F_FULLFSYNC` sulla cartella di destinazione. Come detto, l'effetto sulla cartella non è documentato: è comunque la pratica di SQLite e dei database. **[Fonte parziale]**
8. Solo a questo punto l'originale può andare in quarantena (sezione 4).

**Hash: xxHash3 o SHA-256**

| Algoritmo | Velocità misurata su M1 Max | Note |
|---|---|---|
| XXH3-64 / XXH128 (`xxhsum -b`, dati in cache) | **~35 GB/s** | non crittografico, ottimo contro errori di disco e di trasferimento |
| SHA-256 CryptoKit (1 GB in RAM) | **~2,35 GB/s** | crittografico, usa le istruzioni SHA di Apple Silicon |

**[Provato]** Eclectic Light misura circa 2,6–3 GB/s con SHA-256 su M3 e M4 Pro in condizioni reali, disco compreso; sui Mac Intel è circa 6 volte più lento. **[Fonte]**

- Consiglio **XXH128** come hash di verifica (non rallenta mai, nemmeno su RAID Thunderbolt 5), salvato nel journal. SHA-256 solo come opzione, per esempio per un manifesto d'archivio leggibile da altri strumenti. Con una sola CPU SHA-256 può diventare il collo di bottiglia su SSD oltre i 2,5 GB/s. **[Dedotto]**
- xxHash è una libreria C (licenza BSD) da includere nell'app: niente rete, coerente con la regola offline.

**Cosa conservare e i rischi relativi**
- Permessi, proprietario e flag: il RAID HFS+ è montato `noowners`, quindi i proprietari vengono ignorati. Non va segnalato come errore. **[Provato: mount]**
- Su **exFAT** non ci sono xattr nativi: macOS li salva in file AppleDouble `._nome` accanto. Tag Finder e resource fork sopravvivono solo finché quei file restano con l'originale. **[Fonte: comportamento noto di macOS] [Dedotto: verificare con prove]** Avvisare l'utente prima di copiare su exFAT.
- **SMB**: `copyfile` non fa la copia lato server, che invece Finder fa, quindi su file grandi è molto più lento. **[Fonte: Apple DTS, forum 766035]**
- Durabilità: certi dischi accettano `F_FULLFSYNC` ma non svuotano davvero la loro cache. Nessuna API può accorgersene. **[Fonte: Bitcoin Core, Apple DTS]** Per questo l'originale non si cancella mai subito: resta in quarantena (sezione 4).
- `fsync` da solo non basta su macOS: porta i dati al disco ma non oltre la cache del disco. `O_DSYNC` non garantisce di più. **[Fonte: transactionalblog, Eclectic Light]**

---

## 4. Cestino, quarantena e snapshot

**Cestino sui dischi esterni**
- Ogni volume non di avvio ha `/.Trashes/<uid>/`. `FileManager.trashItem(at:resultingItemURL:)` restituisce il nuovo URL, che va **scritto nel journal**. Apple (DTS) consiglia di non indovinare se un volume ha il cestino: si chiama `trashItem` e si gestisce il fallimento. **[Fonte: forum Apple]**
- Sulle condivisioni SMB Finder avvisa che gli elementi vengono eliminati subito, cioè spesso non c'è cestino. **[Fonte]**
- Il cestino è fuori dal nostro controllo: l'utente lo svuota, Finder può rinominare i file in caso di nomi uguali. Non ci si può contare per l'annullamento. **[Dedotto]**

**Quarantena propria (consigliata)**
- Cartella nascosta alla radice di **ogni volume**, per esempio `/.RawLineSpace/Quarantena/<data>_<id-operazione>/`, sullo stesso volume del file. Così entrare in quarantena è una **rinomina atomica**, istantanea e senza copia. È lo stesso schema di CCC SafetyNet, che sposta le vecchie versioni e i file eliminati in `_CCC SafetyNet` alla radice della destinazione e lo sfoltisce quando lo spazio libero scende sotto 25 GB (valore predefinito). **[Fonte: Bombich KB]**
- Dentro ogni cartella di quarantena va un piccolo manifesto con percorso originale, file ID, dimensione, data di modifica e hash. Così l'annullamento funziona anche senza il database dell'app, per esempio se il Mac cambia. **[Dedotto]**
- Si svuota solo su conferma esplicita, oppure con una regola (età o spazio) scelta dall'utente e mostrata con chiarezza. Lo spazio liberato reale va calcolato con `PRIVATESIZE` su APFS.
- Escluderla da Spotlight (file `.metadata_never_index` nella cartella) e chiedersi se escluderla anche da Time Machine. **[Dedotto]**

**Snapshot APFS sui dischi esterni**
- `tmutil localsnapshot` fa snapshot solo dei volumi inclusi in Time Machine (o del volume dati di avvio), non di un volume esterno qualsiasi. **[Fonte: Eclectic Light 2026]**
- `fs_snapshot_create` richiede root **più** l'entitlement ristretto `com.apple.developer.vfs.snapshot`, che Apple concede caso per caso tramite DTS, di solito solo ad app di backup "di volume intero" che cancellano da sole i propri snapshot. Per tornare a uno snapshot serve un entitlement privato riservato ad Apple. **[Fonte: forum Apple 89635, 786595, 855505]**
- HFS+ ed exFAT non hanno snapshot. **[Provato: `INT_SNAPSHOT` = 0 sul RAID]**
- **Conclusione**: per RawLine Space gli snapshot non sono una base affidabile. Al più si possono proporre come extra ("crea uno snapshot con CCC o Time Machine prima di un grande riordino"). La sicurezza deve venire da journal più quarantena. **[Dedotto]**

---

## 5. Registro delle operazioni (journal / write-ahead log)

**Modelli in altri software [Fonte]**
- **SQLite WAL e rollback journal**: prima si scrive nel log l'intenzione, poi si sincronizza (`fullfsync` su macOS con `PRAGMA fullfsync`), poi si applica. Al riavvio si riprende o si annulla quello che è a metà. Nota: il SQLite incluso in macOS è modificato da Apple per una sincronizzazione meno forte, quindi va attivato `PRAGMA fullfsync=ON` (e `checkpoint_fullfsync`). **[Fonte: transactionalblog, forum SQLite]**
- **CCC SafetyNet**: non cancella, sposta in una cartella sullo stesso volume. **[Fonte]**
- **rsync `--backup --backup-dir`**: i file sostituiti o eliminati finiscono in una cartella separata invece di sparire (comportamento noto dal manuale di rsync).
- **git**: scrive gli oggetti con un nome temporaneo, poi li rinomina; i riferimenti si aggiornano con un file `.lock` più una rinomina atomica. Uno stato a metà non viene mai considerato valido.

**Progetto consigliato [Dedotto]**
- Database SQLite **sul disco interno del Mac** (Application Support), in modalità WAL, con `synchronous=FULL` e `fullfsync=ON`. Più una **copia del registro sul volume stesso** (`/.RawLineSpace/journal/`, file JSON Lines solo in aggiunta, con `F_FULLFSYNC` a ogni passo), così un disco scollegato e collegato a un altro Mac porta con sé la propria storia.
- Ogni operazione è una macchina a stati scritta **prima** di agire:
  `PIANIFICATA → INIZIATA → (COPIATA → VERIFICATA) → APPLICATA → ORIGINALE_IN_QUARANTENA → CHIUSA`, con `FALLITA` / `ANNULLATA`.
- Ogni riga contiene: id operazione e lotto, tipo, percorso e **file ID** di sorgente e destinazione, UUID del volume (`URLResourceKey.volumeUUIDStringKey`), dimensione, data di modifica, hash, nome temporaneo.
- Ogni passo deve essere **idempotente** e verificabile sul disco. Esempio: "la destinazione esiste con questo hash? Allora la copia è fatta".
- **Ripresa all'avvio o al ricollegamento del disco** (si riconosce dall'UUID del volume): per ogni operazione non chiusa si guarda lo stato reale. Se l'originale c'è ancora, si ripulisce il temporaneo e si riparte. Se c'è la destinazione verificata ma l'originale non è ancora in quarantena, si completa. Nel dubbio non si elimina niente e si chiede all'utente.
- L'**annullamento** è l'operazione inversa registrata come una nuova operazione: niente si cancella dalla storia.
- Per lotti da milioni di file: una transazione SQLite ogni N file (per esempio 500), non una per file, altrimenti `fullfsync` diventa il collo di bottiglia. Però una copia verificata non si conferma mai prima del suo `F_FULLFSYNC`.

---

## 6. Rilevare cambiamenti tra anteprima ed esecuzione

**Identità del file**
- Salvare nell'anteprima file ID (`ino`), `dev` e UUID del volume, dimensione, data di modifica (e di creazione) e, per i file piccoli o a campione, un hash. Il file ID resta uguale dopo una rinomina sullo stesso volume. HFS+ e APFS hanno ID persistenti (`VOL_CAP_FMT_PERSISTENTOBJECTIDS` = 1 su entrambi). **[Provato]** Su exFAT e SMB gli ID **non** sono affidabili tra un montaggio e l'altro. **[Dedotto, da verificare]**
- Subito prima di ogni passo, `open(O_NOFOLLOW)` più `fstat`, e confronto. Se qualcosa non torna si salta il file e lo si segnala, senza mai indovinare.
- **FSEvents** con `kFSEventStreamCreateFlagFileEvents | kFSEventStreamCreateFlagUseExtendedData` dà per ogni evento il percorso e l'inode (`kFSEventStreamEventExtendedFileIDKey`, chiave `"fileID"`, presente nell'SDK). **[Provato: header FSEvents.h]** Serve ad accorgersi durante l'anteprima che qualcosa è cambiato. Gli eventi possono però essere raggruppati o persi (flag `MustScanSubDirs`), quindi vale solo come avviso: la verifica finale si fa sempre con `fstat`. **[Fonte parziale] [Dedotto]** Su SMB FSEvents non vede le modifiche fatte da altri computer.

**File aperti da altre app**
- Non esiste una notifica di sistema. L'unico modo è `proc_listpidspath` (o `lsof`), che vede descrittori aperti, file mappati e cartelle correnti, ma non i file che un'app ha già letto in memoria e chiuso. **[Fonte: forum Apple 750123, sorgente libproc]** Va usato a campione, prima di spostare, come avviso ("Lightroom o Photo Mechanic usano questo file").
- Sul volume può esserci `VOL_CAP_INT_RENAME_OPENFAIL`, cioè una rinomina che fallisce sui file aperti: assente sui miei due volumi. **[Provato]** Gestire comunque `EBUSY`.
- Rischio specifico: cataloghi Lightroom o Capture One che puntano ai percorsi. Spostare rompe i collegamenti; meglio offrire un'esportazione della mappa vecchio→nuovo. **[Dedotto]**

**Disco quasi pieno**
- Prima del lotto: `URLResourceKey.volumeAvailableCapacityKey` (sui volumi esterni quella "ForImportantUsage" ha senso soprattutto sul disco di avvio) contro la somma delle copie più un margine (per esempio max(5%, 50 GB)). Durante: gestire `ENOSPC` e `EDQUOT` cancellando **solo il proprio temporaneo**. **[Dedotto]**
- Su APFS con snapshot lo spazio liberato dalla quarantena può non tornare (blocchi trattenuti dagli snapshot). **[Fonte: Eclectic Light, CCC]**

**Unicode (NFC/NFD) e maiuscole/minuscole**
- HFS+ salva i nomi in forma **NFD** (decomposta). APFS conserva i byte così come arrivano; la variante che non distingue maiuscole e minuscole è anche **insensibile alla normalizzazione**, quella che le distingue no. **[Fonte: Eclectic Light 2017/2021/2024]** Per exFAT non ho trovato una fonte autorevole. **[Non verificato]**
- Regole [Dedotto]:
  - confrontare i nomi sempre con una chiave `NFD + case folding` (`String.decomposedStringWithCanonicalMapping` più `folding(options: [.caseInsensitive], …)`) per trovare i **conflitti nell'anteprima**, anche tra file system diversi;
  - non riscrivere mai i byte del nome di un file che non si rinomina;
  - nei nomi generati da RawLine scegliere una forma (NFC, quella di Linux e dei NAS) e applicarla sempre;
  - controllare il volume di destinazione (`VOL_CAP_FMT_CASE_SENSITIVE`): due file che differiscono solo per maiuscole su un volume che le distingue diventano un conflitto su HFS+ o APFS che non le distinguono;
  - lunghezza: 255 unità UTF-16 su HFS+ e APFS. Caratteri vietati su exFAT e SMB: `: * ? " < > | \`.

---

## 7. Prestazioni: milioni di file ed EXIF

**Elencare i file**
- Secondo un ingegnere Apple (DTS) `FileManager` con le API **basate su URL** (`enumerator(at:includingPropertiesForKeys:…)`, chiedendo subito le chiavi che servono: `fileResourceIdentifierKey`, `fileSizeKey`, `contentModificationDateKey`, `isDirectoryKey`…) è veloce quasi quanto `getattrlistbulk` scritto a mano. `fts` guadagna poco (circa 0,2 s su 350.000 file) con molto più lavoro. Leggere i valori dall'URL, non da `fileAttributes`, che può costare un `stat()` in più. **[Fonte: forum Apple 766035]**
- `getattrlistbulk` riduce le chiamate di sistema (circa 10 invece di 20.000 per una cartella da 10.000 file). Va usato con buffer grandi (almeno 32 KB, come `fts`). **[Fonte]** Vale la pena solo se le misure lo giustificano. **[Dedotto]**
- Su **SMB** c'è un caso noto (macOS 15) di elenco che ricomincia all'infinito con cartelle annidate. Rimedio: visitare **una cartella alla volta** con una coda, senza enumerazioni annidate aperte. **[Fonte: forum Apple 766035]** Consiglio questa struttura ovunque: si divide anche bene su più thread, una cartella per compito. **[Dedotto]**
- **Dischi meccanici**: APFS su HDD è da 3 a 15–20 volte più lento di HFS+ nell'elencare un milione di file, perché sparge i metadati sul disco. **[Fonte: Bombich 2019]** Per RAID di HDD da 40–100 TB HFS+ resta una scelta sensata, e l'indice di RawLine Space (SQLite con file ID e data di modifica) evita di rielencare tutto ogni volta. **[Dedotto]**
- Misurare a cache fredda: macOS tiene in cache le cartelle lette da poco. **[Fonte]**

**Leggere l'EXIF**
- `CGImageSourceCreateWithURL` più `CGImageSourceCopyPropertiesAtIndex` con `kCGImageSourceShouldCache: false` legge i metadati senza decodificare i pixel. **[Fonte: Ole Begemann, documentazione Apple ImageIO]** Non ho trovato misure per i RAW (ARW, CR3, NEF). **[Non verificato]**
- [Dedotto] Per la velocità: leggere in parallelo con concorrenza limitata (su HDD poca, 2–4; su SSD di più), e riusare il parser leggero già presente in RawLine Selects e Rename se ce n'è uno per marca (vedi codice in `~/Developer/Rawline`). La data di scatto serve spesso solo per ordinare: si salva nell'indice e non si rilegge.

---

## Ricetta proposta per RawLine Space

**0. Prima di ogni lotto**
1. Per ogni volume coinvolto: UUID, tipo di file system, capacità (`RENAME_EXCL`, `RENAME_SWAP`, `CLONE`, `CASE_SENSITIVE`, `PERSISTENTOBJECTIDS`), spazio libero. Se il volume è exFAT o SMB, l'anteprima avvisa: "operazioni meno protette".
2. Anteprima: per ogni file file ID, dimensione e data di modifica; conflitti di nome (chiave NFD più case folding, considerando il volume di destinazione); spazio necessario; file aperti (a campione).
3. Scrittura del piano nel journal (`PIANIFICATA`) con `fullfsync`. L'utente conferma.

**A. Rinominare o spostare sullo stesso volume**
1. Journal: `INIZIATA` (con sorgente, destinazione, file ID).
2. Ricontrollo con `lstat`: stesso file ID, dimensione e data di modifica? Se no, si salta e si segnala.
3. `renameatx_np(src, dst, RENAME_EXCL | RENAME_NOFOLLOW_ANY)`. Se dà `ENOTSUP` (exFAT o SMB): controllo `lstat(dst)` e poi `rename`, annotato come "non atomico".
4. Cambio di sole maiuscole o normalizzazione: due passi, passando da un nome temporaneo univoco.
5. `F_FULLFSYNC` sulla cartella (o sulle due cartelle) a fine gruppo. Journal: `CHIUSA`, con l'operazione inversa già pronta.

**B. Copiare (o spostare tra volumi)**
1. Journal: `INIZIATA` con il nome temporaneo.
2. Stesso volume APFS: `copyfile(COPYFILE_CLONE | COPYFILE_ALL)` e controllo di `WAS_CLONED`. Fine, nessun hash necessario.
3. Altrimenti: lettura della sorgente con `F_NOCACHE` e XXH128 in corso di lettura, scrittura sul temporaneo, `copyfile(COPYFILE_METADATA)`, ripristino delle date con `setattrlist`, `F_FULLFSYNC` (o ripiego su `fsync` annotato).
4. Rilettura della destinazione con `F_NOCACHE`, confronto di hash, dimensione e xattr. Se non coincidono, il temporaneo si elimina (è nostro, mai un file dell'utente) e si riprova una volta, poi `FALLITA`.
5. `renamex_np(tmp, finale, RENAME_EXCL)` e `F_FULLFSYNC` della cartella. Journal: `VERIFICATA` e `APPLICATA`.
6. Solo se è uno spostamento: l'originale va in quarantena sul **suo** volume (passo C). Mai `unlink`.

**C. "Eliminare"**
1. Journal: `INIZIATA`.
2. Ricontrollo dell'identità (file ID, dimensione, data di modifica).
3. `renamex_np(file, /.RawLineSpace/Quarantena/<lotto>/<percorso-relativo>, RENAME_EXCL)`, creando le cartelle intermedie. Sullo stesso volume è istantaneo e atomico.
4. Se non si può creare la quarantena (volume in sola lettura, SMB senza permessi): niente eliminazione. Si propone `trashItem` o si annulla quel file.
5. Manifesto della quarantena aggiornato. Journal: `ORIGINALE_IN_QUARANTENA`.
6. Svuotare la quarantena è un'azione separata, confermata, con lo spazio reale (`PRIVATESIZE`), registrata anche lei. Su SMB e exFAT l'eliminazione definitiva va avvisata come irreversibile.

**D. Dopo un crash o un disco scollegato**
- All'avvio e al montaggio di un volume noto (per UUID): si rileggono le operazioni non chiuse e si confronta lo stato reale con il journal. Si completa quando è certo (destinazione verificata presente), si torna indietro quando è certo (solo il temporaneo presente). Altrimenti tutto si ferma su quel file e si chiede all'utente. Il temporaneo `.rawline-tmp-*` è l'unica cosa che l'app può cancellare da sola.

**E. Prove da fare prima di scrivere codice**
- Rifare la sonda delle capacità e le prove di rinomina e clone su un volume **exFAT** e su una condivisione **SMB** del NAS (le stesse prove di qui, in una cartella di prova).
- Uscita forzata (`kill -9`) a ogni stato della macchina, più disco scollegato a metà copia su un disco di prova, mai sull'archivio vero.
- Copia di prova su exFAT con tag Finder: i tag ritornano copiando di nuovo su APFS?
- Misura di FileManager e di `getattrlistbulk` su 1 milione di file sul RAID HFS+, a cache fredda.
- Lettura EXIF (ARW, CR3, NEF, RAF) con ImageIO contro il parser di RawLine: file al secondo su HDD e su SSD.

---

## Fonti (link)

**Apple: man page, header, documentazione**
- rename(2) / renamex_np: https://keith.github.io/xcode-man-pages/rename.2.html
- copyfile(3): https://keith.github.io/xcode-man-pages/copyfile.3.html
- exchangedata(2): https://keith.github.io/xcode-man-pages/exchangedata.2.html
- fs_snapshot_create(2): https://keith.github.io/xcode-man-pages/fs_snapshot_create.2.html
- getattrlist(2) (ATTR_CMNEXT_PRIVATESIZE): https://leancrew.com/all-this/man/man2/getattrlist.html
- Header dell'SDK su questo Mac: `MacOSX.sdk/usr/include/sys/attr.h` (VOL_CAP_INT_RENAME_*, ATTR_CMNEXT_CLONEID, CLONE_REFCNT) e `FSEvents.framework/Headers/FSEvents.h` (`kFSEventStreamEventExtendedFileIDKey`)
- ImageIO, kCGImageSourceShouldCache: https://developer.apple.com/documentation/imageio/kcgimagesourceshouldcache
- proc_listpidspath (sorgente): https://cs.iossec.tech/Libc/Libc-583/source/darwin/proc_listpidspath.c

**Apple Developer Forums (risposte DTS)**
- Durabilità di rename su APFS: https://developer.apple.com/forums/thread/849633
- getattrlistbulk su SMB in Sequoia, FileManager contro fts: https://developer.apple.com/forums/thread/766035
- Entitlement per gli snapshot: https://developer.apple.com/forums/thread/89635 · https://developer.apple.com/forums/thread/786595 · https://developer.apple.com/forums/thread/855505
- Cestino sui volumi: https://developer.apple.com/forums/thread/831369
- File aperti da altri processi: https://developer.apple.com/forums/thread/750123 · https://developer.apple.com/forums/thread/779747

**Eclectic Light Company (Howard Oakley)**
- Copie, cloni e hard link: https://eclecticlight.co/2025/05/13/how-to-tell-the-difference-between-copies-clone-files-and-hard-links/
- Come capire se un file è un clone: https://eclecticlight.co/2021/04/02/how-can-you-tell-whether-a-file-has-been-cloned-in-apfs/
- Copiare, spostare e clonare in APFS: https://eclecticlight.co/2020/04/14/copy-move-and-clone-files-in-apfs-a-primer/
- Ci si può fidare che un disco scriva i dati?: https://eclecticlight.co/2022/02/18/how-can-you-trust-a-disk-to-write-data/
- Unicode e normalizzazione in APFS: https://eclecticlight.co/2021/05/08/explainer-unicode-normalization-and-apfs/ · https://eclecticlight.co/2024/03/25/apfs-directories-and-names/
- Snapshot: https://eclecticlight.co/2026/05/10/last-week-on-my-mac-snapshots-the-elephant-in-apfs/ · https://eclecticlight.co/2026/09/09/take-control-of-snapshots/ · https://eclecticlight.co/2024/04/08/apfs-snapshots/
- Velocità di SHA-256: https://eclecticlight.co/2025/04/28/how-checking-hashes-can-slow-your-mac/ · https://eclecticlight.co/2025/07/17/encryption-and-checking-hashes-slows-faster-ssds/ · https://eclecticlight.co/2025/07/23/intel-macs-can-be-much-slower-computing-sha-256-hashes/

**Bombich / Carbon Copy Cloner**
- SafetyNet (CCC 6): https://bombich.com/kb/ccc6/protecting-data-already-on-your-destination-volume-carbon-copy-cloner-safetynet
- Manutenzione della SafetyNet: https://bombich.com/kb/ccc5/automated-maintenance-ccc-safetynet-folder
- APFS su dischi meccanici: https://bombich.com/blog/2019/09/12/analysis-apfs-enumeration-performance-on-rotational-hard-drives

**Altro**
- mjtsai, fsync e F_FULLFSYNC: https://mjtsai.com/blog/?p=35060 · lettura delle cartelle: https://mjtsai.com/blog/?p=25067
- Darwin's Deceptive Durability: https://transactionalblog.pages.dev/blog/2022-darwins-deceptive-durability.html
- SQLite e F_FULLFSYNC: https://sqlite.org/forum/info/b94afa45dda82aae8cbf49f9d511a00b332870fc926cba18954acd889bbfb7cd
- Bitcoin Core, F_FULLFSYNC che fallisce su dischi esterni ed exFAT: https://mirror.b10c.me/bitcoin-bitcoin/26455/ · https://mirror.b10c.me/bitcoin-bitcoin/26534/
- xxHash: https://github.com/Cyan4973/xxHash · https://xxhash.com/
- Rinomina non atomica su exFAT, SMB e NFS (Blender): https://projects.blender.org/blender/blender/pulls/115096
- Samba, corsa critica nella rinomina: https://bugzilla.samba.org/show_bug.cgi?id=13648
- exFAT non è un formato professionale (OWC): https://www.owc.com/blog/exfat-is-not-a-professional-drive-format-heres-what-cross-platform-mac-to-pc-content-creators-should-use-instead
- getattrlistbulk (crate Rust, cifre indicative): https://docs.rs/crate/getattrlistbulk/0.1.0
- Metadati immagine senza decodifica (Ole Begemann): https://oleb.net/blog/2011/09/accessing-image-properties-without-loading-the-image-into-memory/
