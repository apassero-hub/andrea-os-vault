# Hazel (Noodlesoft): ricerca per RawLine Space

Ricerca dell'11 novembre 2026. Legenda: **[V]** = verificato su una fonte (vedi sezione 8) · **[D]** = mia deduzione, non confermata.

Versione di riferimento: **Hazel 6.1.x** (6.0 uscito nel 2024, 6.1 con l'aspetto "Liquid Glass" per macOS 26 Tahoe, 6.1.2 l'ultima trovata nelle note di rilascio) [V].

---

## 1. Cos'è

Hazel è un'utility per macOS che **sorveglia cartelle** e applica in automatico **regole** ai file che ci arrivano dentro: sposta, ordina in sottocartelle, rinomina, mette tag, archivia, lancia script [V]. Il caso d'uso tipico sono le cartelle "di passaggio" (Scrivania, Download), non gli archivi enormi [V]. Ha due parti:

- **Cartelle e regole**: ogni cartella sorvegliata ha la sua lista di regole; ogni regola è "condizioni → azioni" [V].
- **Gestione del Cestino**: svuotamento automatico per età o dimensione, più **App Sweep**, che trova i file di supporto lasciati dalle app cestinate [V].

Lavora in background, sempre acceso, con un'icona nella barra dei menu e un'estensione del Finder (serve per il comando "Revert") [V]. È di uno sviluppatore piccolo (Paul Kim, Noodlesoft), su mercato da quasi vent'anni [V: articolo TidBITS del 2007; nome del fondatore D].

Funziona in locale: le regole girano sul Mac. Usa la rete solo per le azioni che la chiedono (Upload FTP/SFTP/WebDAV), per gli aggiornamenti e, se si vuole, per sincronizzare le regole tramite un file su Dropbox/iCloud [V]. Quindi come modello è compatibile con la regola "100% offline" di RawLine.

## 2. Funzioni e impostazioni nel dettaglio

### 2.1 Logica delle regole [V]
- Hazel prende **un elemento alla volta** e lo prova contro le regole **in ordine di lista**. **Vince solo la prima regola che corrisponde**; le successive vengono saltate.
- Eccezioni: l'azione **"Continue matching rules"** fa proseguire l'elemento alla regola seguente (non usabile insieme a Move o Sort into subfolder); l'azione **"Ignore"** blocca l'elemento per tutte le regole successive.
- Le azioni della regola girano **in sequenza**; se una fallisce, le successive per quell'elemento saltano e Hazel **ritenta ai passaggi successivi** finché la regola corrisponde ancora.
- Hazel **ricorda quali elementi hanno già corrisposto a quale regola**: dopo un'esecuzione riuscita non li ritocca (evita i loop). Se l'utente annulla a mano una modifica, la regola non la riapplica.
- Se si **modificano le condizioni** di una regola, Hazel rivaluta gli elementi con le nuove condizioni e agisce su quelli che ora corrispondono.
- Un elemento resta "sotto osservazione" finché non esce dalla cartella: una regola a data (es. "aggiunto più di 30 giorni fa") può scattare giorni dopo.
- Regola finale tipica: condizione **"Any File"** come raccogli-tutto.

### 2.2 Condizioni e attributi [V]
- Combinazione **All / Any / None** delle condizioni (in versioni recenti si passa da "All" ad "Any" anche tenendo premuto Opzione [V: forum MPU]).
- **Condizioni annidate**, profonde a piacere, ognuna col suo All/Any/None. Ogni gruppo annidato ha un **bersaglio**:
  - il file corrente (predefinito);
  - **la cartella che lo contiene**;
  - **un qualsiasi / tutti gli elementi nella stessa cartella** (fratelli);
  - **un qualsiasi / tutti i sotto-elementi** (solo per cartelle).
  Le azioni si applicano sempre all'elemento in esame, anche se la condizione guarda i vicini.
- Attributi di base: Name, Extension, Full Name, Kind; **Date Added** (ingresso nella cartella sorvegliata), Date Created, Date Last Modified, Date Last Opened, **Date Last Matched**, Current Time; Tags, Color Label, Comment; Size, Locked; **Contents** (testo, con OCR al volo su immagini e PDF senza testo da Hazel 6; non scrive l'OCR nel file); Source URL; **Subfolder Depth**; **Sub-file/folder Count**.
- **"Other"**: qualsiasi attributo Spotlight installato sul Mac (qui stanno i metadati foto).
- Per le foto: dalla 4.1 esiste un attributo **"Capture date"** (tra gli attributi Spotlight) e dalla 5.1 **"Date Taken (Hazel)"**, che funziona anche coi video [V: note di rilascio]. Gli utenti lo descrivono come "nascosto in fondo alle opzioni" [V: forum MPU]. Che legga in modo affidabile ogni formato RAW (ARW, CR3, NEF, RAF…) **non l'ho trovato confermato** [D: dipende probabilmente dagli importer Spotlight/ImageIO di macOS].
- **Script come condizione**: "Passes AppleScript / JavaScript / shell script". Per lo shell: il percorso arriva in `$1`, **exit 0 = corrisponde**. Gli script di condizione vanno tenuti veloci (vengono rivalutati spesso) e **non devono modificare nulla nella cartella**, se no si creano loop.

### 2.3 Attributi personalizzati (token) [V]
- Si creano dentro i **match pattern** delle condizioni e si danno nomi propri. Tipi: **testo**, **data**, **lista** (nuovo in Hazel 6, es. lista di tag), **elemento di lista**, **tabella** (si cerca un valore in una colonna e si usa il valore di un'altra colonna dopo: es. numero fattura → nome cliente).
- Si possono riusare nelle condizioni successive e nelle azioni (rinomina, sottocartelle, tag dinamici).
- AppleScript/JavaScript possono **restituire attributi personalizzati** (`hazelOutputAttributes`); lo shell script **no**. Esempio reale: uno script JXA che legge la data di scatto con `sips` e la restituisce come attributo data, perché le date predefinite di Hazel sono quelle del file system e non quelle di scatto [V: gist redoPop]. L'autore poi è passato a uno script con **exiftool** che rinomina e sposta usando `DateTimeOriginal`.
- Critica nota: nelle tabelle di corrispondenza non ci sono jolly né regex [V: forum MPU].

### 2.4 Azioni [V]
- **Move**, **Copy**, **Rename**, **Sort into subfolder**, **Sync** (copia monodirezionale dei soli elementi nuovi; in certe condizioni propaga anche le cancellazioni), **Upload** (FTP/SFTP/WebDAV).
- **Add / Remove tags** (anche "Dynamic Tags" da metadati o attributi personalizzati), **Set color label**, **Add comment** (Spotlight), **Toggle extension**, **Toggle lock**.
- **Archive** (zip; l'originale va nel Cestino), **Unarchive** (l'archivio va nel Cestino).
- **Open**, **Show in Finder**, **Make alias**, **Import into Music / Photos / TV** (l'originale resta dov'è).
- **Run Shortcut / AppleScript / JavaScript / Automator / shell script**. Per lo shell, exit ≠ 0 = errore, e **Hazel rilancia la regola finché non riesce**.
- **Pause** (attesa di secondi/minuti tra due azioni, nuovo in Hazel 6), **Display notification**, **Run rules on folder contents**, **Continue matching rules**, **Ignore**.
- **Non esiste un'azione "Elimina definitivamente"**: tutto ciò che viene "buttato" va nel Cestino. La cancellazione definitiva avviene solo nella gestione del Cestino.

### 2.5 Pattern di rinomina e sottocartelle [V]
- Il pattern mischia **testo libero e token** (le "bolle" blu), con un campo **Example** che mostra subito il risultato.
- Per ogni token: Replace Text (coppie trova/sostituisci), **Set Default** (valore di riserva se vuoto), Set Maximum Length; maiuscole/minuscole; per i numeri cifre minime e correzione (+/-); per le liste primo/ultimo/n-esimo/tutti; per le date **Edit Date Pattern** e **Adjust Date** (± anni, mesi, giorni, ore, minuti). Da 6.1 gli anni hanno 4 cifre di default.
- **Counter**: contatore configurabile per numerare i file.
- **Sort into subfolder**: crea le cartelle che mancano; il token **▸** aggiunge un livello (es. `Anno ▸ Anno-Mese`); **"Treat as File Path"** trasforma un testo con separatore in cartelle annidate; il token **"Anything" (…)** fa corrispondere nomi parziali di cartelle esistenti ma non può crearle.
- Ricetta tipica dei fotografi: Sort into subfolder con data (di scatto o di creazione) → `Anno ▸ Mese` (o `Anno ▸ Mese ▸ Giorno`), più una Rename `aaaa-mm-gg_hh.mm.ss` [V: blog e forum MPU].

### 2.6 Sottocartelle e rielaborazione [V]
- Di default Hazel guarda **solo il primo livello** della cartella sorvegliata.
- Per scendere serve una regola apposita: condizione **"Kind is Folder"** + azione **"Run rules on folder contents"**. È ricorsiva, profondità 0 = cartella sorvegliata, 1 = primo livello; si limita con la condizione **Subfolder Depth**. L'ordine conta: le regole specifiche (es. "cancella cartelle vuote") vanno prima della regola-sottocartelle.
- Il manuale stesso avverte: gerarchie profonde, rielaborate di continuo, **rallentano molto**; consigliato solo su strutture poco profonde.
- **Run Rules Now** (menu, menu contestuale, icona) forza l'esecuzione e **rilancia le azioni anche su file che avevano già corrisposto**. Utile dopo una modifica, ma pericoloso.
- Regole: **attiva/disattiva** singola (⌘-clic = tutte); **pausa** a livello di cartella (si può comunque lanciare una volta a mano).

### 2.7 Cartelle sorvegliate [V]
- Cartelle normali (trascinandole), **App Folder** (download di Safari, Mail, Chrome…), **Smart Folder** del Finder (ma lì niente sottocartelle).
- Opzioni cartella: elimina i **duplicati numerati** identici ("file-1"), manda nel Cestino i **download incompleti** dopo X tempo. Da 6.1: opzioni per i **file solo-cloud** (dettagli non documentati nelle note).
- **Togliere una cartella cancella anche le sue regole, senza annullamento.**
- Gruppi di cartelle annidabili.
- Dischi di rete: funzionano se montati, ma se il NAS non è raggiungibile le regole generano **raffiche di errori**; gli utenti mettono in pausa a mano o aggiungono uno script che controlla la rete [V: blog Podfeet / forum Automators]. Dalla 5.3.4 è corretto il cestinamento su volumi esterni senza Cestino proprio [V].

### 2.8 Cestino e App Sweep [V]
- **Svuotamento automatico** (Preferenze > Trash): per **età** (ore … anni) e/o per **dimensione massima** (MB, GB o % del disco), eliminando nell'ordine in cui i file sono entrati. File singolo più grande del limite: o resta (ignorato nel conteggio) o si cancella subito.
- Opzione **cancellazione sicura** (sovrascrittura 7 volte; inutile su SSD, lenta).
- Il manuale dice esplicitamente che è **definitiva** e consiglia di mettere limiti "più lunghi e più alti di quanto pensi".
- **App Sweep**: quando si cestina un'app, Hazel cerca i file di supporto e mostra una **finestra con l'elenco spuntabile**: si tolgono le spunte a ciò che si vuole tenere, oppure "Keep All", oppure "Move to Trash". I file vanno **nel Cestino**, non cancellati. Se si fa "Rimetti a posto" sull'app, Hazel **propone di rimettere anche i file di supporto**. Sconsigliato per app con disinstallatore proprio.

### 2.9 Sync delle regole [V]
- Si esporta il set di regole di **una cartella** in un **file di sync** (su Dropbox, iCloud, server). Gli altri Mac lo adottano.
- Sincronizza l'intero set, non le singole regole; **non fonde**: adottare un file sovrascrive le regole locali di quella cartella.
- Lo stato attivo/disattivo **non** si sincronizza; **le regole nuove arrivano disattivate** sugli altri Mac.
- Cache locale: se il file non è raggiungibile Hazel continua a lavorare; un'icona d'errore segnala problemi.
- Ci sono anche **Import / Export** di regole e **regole d'esempio**.

## 3. Interfaccia e flusso

- Finestra a **tre colonne** (cartelle · regole · editor della regola), oppure due colonne / due righe [V].
- Editor della regola in stile Smart Folder del Finder: righe "If [all] of the following conditions are met" e "Do the following", con pop-up attributo/operatore/valore e pulsanti +/- [V].
- **Rule Preview** (⌘⌥P): si sceglie **un file** della cartella e ogni condizione si segna con **✓ verde o ✗ rossa**; sopra compare "Rule matches / does not match". Cliccando il segno si apre un popover col **valore reale dell'attributo** e degli attributi personalizzati catturati; il popover si può staccare e tenere aperto mentre si modifica. Si aggiorna in tempo reale, funziona anche con regole disattivate, e si possono cliccare le altre regole per vedere se corrispondono. **Non esegue né simula le azioni** [V]. Da 6.1 gira in background per non bloccare l'interfaccia, e corregge un caso raro in cui l'anteprima differiva dal risultato reale [V].
- **Rule Status** (⌘⌥R): tabella di **tutti gli elementi** della cartella con la data in cui hanno corrisposto (vuoto = non ancora elaborato; **messaggio d'errore** al posto della data se è fallito). Pannello Info per file: attributi che corrispondono in **blu**, quelli che fanno fallire in **rosso**. Spazio = Quick Look, pulsante Refresh [V].
- Menu nella barra: esegui regole, Revert, View Log [V].
- Notifiche di sistema configurabili [V].
- Ricerca tra le regole, undo delle **modifiche alle regole** (da Hazel 5; non dei file) [V].
- Flusso tipico: aggiungi cartella → crea regola → preview su qualche file → attiva → controlla Rule Status/log → aggiusta.

## 4. Sicurezza dei file (anteprima, annulla, log, conflitti)

### Anteprima [V]
- Solo **sulle condizioni**, **un file alla volta**. Non c'è un **dry-run** che mostri "cosa farebbe la regola su tutta la cartella" (nuovo nome, nuova posizione). Il campo **Example** del pattern mostra il risultato della rinomina, ma su un file d'esempio.
- La vista d'insieme è Rule Status, ma mostra il passato (cosa ha corrisposto), non il futuro.

### Annullare (Revert, nuovo in Hazel 6) [V]
- Clic destro sul file nel Finder → **Revert**, oppure dal menu di Hazel. Riporta il file a **posizione e nome originali** e ripristina proprietà come tag e commenti.
- Vale per: Move, Rename, Sort into subfolder, Add/Remove tags, Set color label, Add comment, Toggle extension/lock, Archive/Unarchive.
- **Non vale** per: Copy, Sync, Upload, Make alias, Import in Music/Photos/TV, script e automazioni. Le note di rilascio precisano che il ripristino tocca solo gli attributi del file, non gli effetti su altre app o percorsi.
- È **per file** (dal Finder). Non ho trovato un "annulla l'ultima esecuzione su 3.000 file" né una cronologia a più passi [D: non documentato].
- Avvertenza ufficiale: **correggi prima la regola**, sennò Hazel rimette subito il file dove l'aveva messo.
- Prima di Hazel 6 non esisteva alcun annullamento sui file: la difesa era solo backup e preview [V: ricerche e forum].

### Registro (log) [V]
- File di testo `~/Library/Logs/Hazel/Hazel.log`, aperto in Console (Help > View Logs o menu barra). Riporta cosa è successo e gli errori; con **debug mode** (Info > tenendo Opzione → "Debug…") si ottiene più dettaglio, e l'output degli script compare nel log solo in debug. Rotazione automatica del log.
- È un log tecnico da sviluppatore: si cerca con il campo di ricerca di Console, **non è una cronologia leggibile** né un "registro operazioni" da cui annullare [D].

### Conflitti di nome e duplicati [V]
- Move: se a destinazione esiste già un file con lo stesso nome → **rinomina** (aggiunge un numero), **sostituisci**, o **butta via** il file in arrivo (nel Cestino). Opzione "Throw away if a duplicate" se è identico.
- Copy / Sort / Upload: rinomina, sostituisci o non copiare; "Do not copy if a duplicate".
- Non c'è un'opzione "fermati e chiedi" [V: non presente nell'elenco]. **Sostituisci** sovrascrive in silenzio [D: il manuale non dice se l'esistente va nel Cestino].
- Errori: Hazel **ritenta** all'infinito finché l'azione riesce (script con exit ≠ 0 compresi), l'errore appare in Rule Status e nel log. Con un NAS staccato questo diventa una raffica di errori [V].

### Altre trappole documentate [V]
- Svuotamento del Cestino **definitivo**.
- Rimuovere una cartella dalla lista **cancella le sue regole senza annullamento**.
- **Run Rules Now** rifà le azioni anche su file già elaborati.
- Script di condizione che toccano la cartella → **loop**.
- Un utente col caso "100.000 foto in sottocartelle su disco esterno" si è visto **rinominare sottocartelle in modo inatteso**; il consiglio degli altri è stato **"lavora su una copia"** [V: forum MPU].

## 5. Prezzo, piattaforme, limiti, critiche

### Prezzo e piattaforme [V]
- **42 $** licenza singola, **65 $** family pack; **aggiornamento 20 $** da qualsiasi versione precedente. **Non è un abbonamento**: aggiornamenti gratuiti dentro la versione maggiore, la licenza continua a funzionare. Prova gratuita (modalità valutazione/demo descritte nel manuale).
- Solo **macOS**: Hazel 6.1 richiede **macOS 13 Ventura** o successivi; Apple Silicon supportato. Niente iOS/Windows.

### Limiti [V salvo dove indicato]
- Pensato per **cartelle di ingresso**, non per riorganizzare archivi esistenti di decine di TB: di default vede solo il primo livello, la ricorsione è sconsigliata su gerarchie profonde.
- Nessuna nozione di **"progetto", "servizio", "cliente"**: ragiona file per file. Le condizioni sui "fratelli" aiutano (es. "esiste un .xmp con lo stesso nome nella cartella" [D: fattibile con match pattern, non visto come esempio]), ma non c'è un concetto di **gruppo RAW+XMP+JPG** che si muove insieme.
- Date di scatto: le date predefinite sono quelle del file system; per l'EXIF servono "Date Taken"/"Capture date" (via Spotlight) o script exiftool. Video "a caso" con Date Taken [V: forum MPU]. Nessuna lettura documentata dei sidecar XMP (domanda rimasta senza risposta sul forum) [V].
- Prestazioni su grandi volumi: un utente ha elaborato **~80.000 foto in più di una settimana** su un NAS Synology [V]. Non ci sono dati ufficiali sulle prestazioni con milioni di file [V]. Si basa su FSEvents e Spotlight [D].
- Nessun **report d'insieme** (quanto spazio, quanti duplicati, cosa è fuori posto): è un esecutore, non un analizzatore.
- Nessuna IA per riconoscere i contenuti (richiesta da utenti, non aggiunta in Hazel 6) [V].

### Critiche raccolte [V]
- **Affidabilità con le sottocartelle**: Dr. Drang (leancrew) l'ha disinstallato perché le uniche regole che fallivano erano quelle basate sulla regola-sottocartelle.
- **Regole che smettono di scattare** (si risolve spegnendo e riaccendendo), lentezza su compiti prima istantanei, specie su Tahoe.
- **Regole fragili**: chi estrae date da documenti con formati che cambiano passa più tempo a correggere che a fare a mano.
- **Curva d'apprendimento**: Opzione per "Any", "Date Taken" nascosto, logica "prima regola che vince" e ricorsione poco intuitive.
- Sviluppo lento e forum poco attivo (sviluppatore singolo); ma molti utenti lo usano da 10+ anni con decine di regole e lo considerano maturo.
- Alternative citate: Rulebook, Forel (open source), File Juggler (Windows), Keyboard Maestro/Alfred per parte dei casi; per le foto **exiftool** in una riga (`-d "%Y/%Y-%m" "-directory<DateTimeOriginal"`), A Better Finder Rename, Lightroom.

## 6. Idee da prendere per RawLine Space

1. **Lo "schema dell'archivio" come lista di regole ordinate, ma in sola lettura.** Stesso modello mentale di Hazel (condizioni → destinazione/nome), però l'esito non è un'azione ma uno **stato**: per ogni file/servizio, "conforme", "fuori posto → dovrebbe stare in `2025/2025-06_Cliente_Lavoro/RAW`", "nome non conforme", "nessuna regola". Lo schema si applica a tutto l'archivio e produce una **lista di proposte**. Niente gira in background.
2. **Rule Preview portato su tutto l'archivio.** Prendere il ✓/✗ per condizione con il **valore reale nel popover** (bellissimo per capire *perché*), ma aggiungere quello che Hazel non ha: una tabella **"prima → dopo"** (percorso e nome attuali → proposti) per tutti gli elementi interessati, con conteggi e GB spostati. È il dry-run che manca a Hazel.
3. **Rule Status come "stato dell'archivio".** Una vista con colonne *regola che corrisponde · stato · ultimo controllo · errore*, attributi in blu/rosso. In Space diventa la dashboard di salute: % conforme per disco/anno/cliente.
4. **Pattern a token con campo Example dal vivo**, e i modificatori per token: **valore di riserva** (es. "SenzaData"), lunghezza massima, trova/sostituisci, **Adjust Date** (utilissimo per i fusi orari e gli orologi della fotocamera sbagliati, in linea con le funzioni "orologi" di Selects), token **▸** per i livelli di cartella. Riusare i token già in RawLine Rename, così Rename e Space parlano la stessa lingua.
5. **Condizioni sui vicini (enclosing folder / fratelli / sotto-elementi)**. Base per regole del tipo "cartella servizio = contiene RAW **e** esiste `Export/`", "RAW con XMP accanto", "cartella che contiene solo JPG di export → alleggeribile". In Space andrebbero promosse a **unità di lavoro "servizio" e "gruppo file"** (RAW+XMP+JPG+sidecar video), che si spostano sempre insieme.
6. **Date di scatto prima di tutto.** Hazel insegna che la data del file system mente: Space deve usare EXIF `DateTimeOriginal` (e i metadati dei video, che sono il punto debole), mostrare **da dove viene ogni data** e avvisare quando le fonti non sono d'accordo.
7. **Attributi personalizzati e tabella.** L'"attributo tabella" di Hazel (valore → altro valore) si traduce bene in una **rubrica clienti/lavori locale**: codice lavoro nel nome cartella → cliente, anno, tipo di consegna, scadenza di conservazione.
8. **Revert per elemento + per operazione.** Prendere l'idea di "annulla dal clic destro nel Finder" (estensione Finder o Quick Action), ma basarla su un **registro di operazioni** di Space: ogni conferma dell'utente = un'operazione con ID, annullabile tutta insieme o file per file, con controllo che il file sia ancora dove l'abbiamo lasciato.
9. **Regole "imparate" che non si ripetono.** Il meccanismo "Hazel ricorda cosa ha già corrisposto" → in Space: proposte **rifiutate** dall'utente restano rifiutate (con motivo), così la volta dopo non si ripresentano.
10. **App Sweep come modello d'interazione per l'alleggerimento.** Elenco spuntabile, "Tieni tutto", "Sposta nel Cestino/Quarantena", e **"Rimetti a posto" che riporta anche i file collegati**. È esattamente il tono giusto per "questi 1,2 TB di export doppi/anteprime/cache si possono togliere".
11. **Ritenzione per età e dimensione, ma su una quarantena di Space** (non sul Cestino di sistema): "tieni le cose tolte almeno 90 giorni / finché la quarantena non supera 2 TB", con promemoria e conferma finale esplicita, mai automatica.
12. **Gestione dischi staccati fatta bene.** Hazel su NAS sommerge di errori: Space deve riconoscere un volume non montato come stato normale ("disco offline, ultimo indice del…"), mettere in pausa le proposte che lo riguardano e riprendere quando torna.
13. **Esporta/importa lo schema** come file leggibile (es. JSON/plist con versioni), per condividerlo tra due Mac o tenerlo come documentazione dell'archivio. Ma **niente sync che sovrascrive** (vedi sotto).
14. **Script come estensione avanzata**, opzionale: condizioni con exit code 0/1 e possibilità di restituire attributi (exiftool, ecc.), sempre in sola lettura nella fase di analisi.

## 7. Cose da NON copiare

- **Azione immediata in background.** In Hazel la regola scatta da sola appena il file arriva. In Space niente si muove senza conferma.
- **"Run Rules Now" che rifà tutto anche su file già elaborati**, senza anteprima di cosa succederà.
- **Anteprima solo sulle condizioni e su un file alla volta.** Insufficiente per archivi da decine di TB.
- **Conflitto "Sostituisci" silenzioso** e "butta via il file in arrivo". In Space: mai sovrascrivere; in caso di conflitto fermarsi e mostrare i due file (dimensione, hash, data) con la scelta all'utente.
- **Ritentare all'infinito** un'azione fallita. Meglio: un errore = una voce chiara nel registro, la proposta resta in sospeso, nessun nuovo tentativo senza l'utente.
- **Svuotamento del Cestino automatico e definitivo**, e la cancellazione "sicura" a 7 passaggi (inutile su SSD, lenta).
- **Log tecnico in Console** come unico registro. Serve un registro umano, filtrabile per data, disco, cliente, operazione, con annulla.
- **Revert limitato a certe azioni e a un file per volta**; e il rischio che la regola rimetta subito a posto il file annullato.
- **Rimuovere una cartella = cancellare le sue regole senza annullamento.**
- **Sync regole che sovrascrive senza unire** e porta le regole nuove disattivate in modo implicito.
- **Prima regola che vince + ricorsione tramite una regola speciale "Kind is Folder"**: potente ma opaca, ed è la prima fonte di errori secondo gli utenti. In Space: priorità visibile e spiegata ("questo file corrisponde a 3 regole, vince la n. 1 perché…"), scansione ricorsiva come comportamento normale dell'indice, non come trucco.
- **Funzioni nascoste** (Opzione per "Any", "Date Taken" sepolto tra gli attributi Spotlight).
- **Script che possono modificare la cartella durante la valutazione** (loop).
- **Azioni che dipendono dalla rete** (Upload) nello stesso motore delle regole: in Space non servono e andrebbero contro la regola offline.

## 8. Fonti (link)

Manuale ufficiale e Noodlesoft
- Manuale, indice: https://www.noodlesoft.com/manual/hazel/hazel-overview/
- Logica delle regole: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/create-edit-rules/understand-the-logic-of-rules/
- Preview a Rule: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/create-edit-rules/preview-a-rule/
- Show Rule Status: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-rules/show-rule-status/
- Revert a File: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-rules/revert-a-file/
- Run Rules Manually: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-rules/run-rules-manually/
- Enable, Disable, or Pause Rules: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-rules/enable-disable-or-pause-rules/
- Sync Rules: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-rules/sync-rules/
- Troubleshoot Rules: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-rules/troubleshoot-rules/
- Manage Folders: https://www.noodlesoft.com/manual/hazel/work-with-folders-rules/manage-folders/
- Attribute Reference: https://www.noodlesoft.com/manual/hazel/attributes-actions/attribute-reference/
- Custom Attributes: https://www.noodlesoft.com/manual/hazel/attributes-actions/attribute-reference/using-custom-attributes/
- Action Reference: https://www.noodlesoft.com/manual/hazel/attributes-actions/action-reference/
- Using Patterns in Actions: https://www.noodlesoft.com/manual/hazel/attributes-actions/action-reference/using-patterns-in-actions/
- Using Shell Scripts: https://www.noodlesoft.com/manual/hazel/attributes-actions/using-shell-scripts/
- Processing Subfolders: https://www.noodlesoft.com/manual/hazel/advanced-topics/processing-subfolders/
- Using Nested Conditions: https://www.noodlesoft.com/manual/hazel/advanced-topics/using-nested-conditions/
- Viewing Logs: https://www.noodlesoft.com/manual/hazel/viewing-logs/
- Hazel Preferences: https://www.noodlesoft.com/manual/hazel/hazel-basics/hazel-preferences/
- Automatic Deletion (Cestino): https://www.noodlesoft.com/manual/hazel/hazel-basics/manage-your-trash/use-automatic-deletion/
- App Sweep: https://www.noodlesoft.com/manual/hazel/hazel-basics/manage-your-trash/use-app-sweep/
- What's New in Hazel 6: https://www.noodlesoft.com/?p=1857
- Hazel 6 FAQ (prezzi, requisiti): https://www.noodlesoft.com/kb/hazel-6-faq/
- Note di rilascio complete: https://www.noodlesoft.com/release_notes
- Note 6.0: https://www.noodlesoft.com/?p=1871 · 6.1: https://www.noodlesoft.com/?p=2008 · 6.1.2: https://www.noodlesoft.com/?p=2018

Forum, blog, esempi
- MPU, Hazel per foto (100.000 immagini, "lavora su una copia"): https://talk.macpowerusers.com/t/hazel-for-photos-image-organization/33747
- MPU, ordinare foto per Anno/Mese: https://talk.macpowerusers.com/t/how-to-get-hazel-to-sort-pictures-to-year-month-folder-structure/10901
- MPU, organizzazione cronologica con Hazel e Synology (~80.000 foto in oltre una settimana): https://talk.macpowerusers.com/t/ground-zero-chronological-photo-organization-with-hazel-and-synology/17186
- MPU, "Is Hazel dying?": https://talk.macpowerusers.com/t/is-hazel-dying/44699
- MPU, "Hazel Alternative?": https://talk.macpowerusers.com/t/hazel-alternative/37165
- MPU, Hazel su condivisioni di rete: https://talk.macpowerusers.com/t/hazel-on-network-shares/8902
- Gist JXA per data di scatto: https://gist.github.com/redoPop/0667cab8afd6c1fb94bb
- Macdrifter, Hazel Tip for Organizing Photos: https://www.macdrifter.com/2014/02/hazel-tip-for-organizing-photos.html
- Dr. Drang, "My trouble with Hazel": https://leancrew.com/all-this/2020/02/my-trouble-with-hazel/
- Podfeet, Hazel + NAS e script di controllo rete: https://www.podfeet.com/blog/2022/03/shortcut-nas-volume/
- TidBITS 2007, "Clean up messy folders with Hazel": https://tidbits.com/2007/11/14/clean-up-messy-folders-with-hazel/
- TidBITS, Hazel 6.1: https://talk.tidbits.com/t/hazel-6-1/32328
- MacStories, Hazel 4 (introduzione preview e sync): https://www.macstories.net/?p=43083
- Articolo Medium su Hazel + exiftool (non leggibile, 403): https://iaindunn.medium.com/automated-photo-workflow-using-hazel-rules-and-exiftool-fa15be79d624
