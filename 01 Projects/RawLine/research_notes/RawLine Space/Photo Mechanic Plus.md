# Photo Mechanic Plus (Camera Bits) — catalogo e gestione file

Ricerca per RawLine Space, 11 novembre 2026. Solo catalogo e gestione dei file.
Legenda: **[V]** = verificato su fonte (di solito docs.camerabits.com o blog ufficiale) · **[D]** = dedotto da me o da fonti di terzi/forum, da controllare.

> **Notizia principale:** Photo Mechanic Plus **non è più in vendita dal 27 febbraio 2026** [V]. Camera Bits spiega che il catalogo si basa su una tecnologia di terze parti non più supportata, che i cambiamenti del sistema operativo la rendono instabile e che il prodotto "si rompe per la maggior parte degli utenti". Dopo la perdita di chi aveva ideato la funzione, il team non è riuscito a risolvere i problemi. Il catalogo non avrà altri sviluppi. Gli abbonamenti attivi non vengono annullati in automatico e l'assistenza continua finché il software resta stabile. La migrazione dei database verso altri sistemi è "allo studio", senza conferme [V]. Photo Mechanic standard (senza catalogo) continua a essere sviluppato [V].
> Inoltre: la build 7285 e le precedenti hanno l'interfaccia del catalogo che non scala bene su macOS Tahoe, e Camera Bits non lo correggerà ("fuori supporto") [V]. Già macOS Sonoma 14.3 aveva rotto funzioni critiche del catalogo [V]. Un post ufficiale del 2026 dice che, finito Rosetta (macOS 28), "nessuna versione di Photo Mechanic Plus" girerà su Apple silicon [V]. Questo contrasta in parte con l'annuncio del 2023 di build universali per standard e Plus. Ne deduco che le build Plus ancora usabili da chi ha licenze vecchie siano Intel [D].
>
> Per RawLine Space questo è il dato più utile: **il primo catalogo "veloce" per professionisti è morto per una dipendenza esterna non controllata e per un sapere concentrato in una persona.** Gli utenti Plus si ritrovano con un database che nessuno sa più esportare. È anche un'opportunità di mercato.

---

## 1. Cos'è

- Photo Mechanic è il browser/ingest/metadati di riferimento per i fotogiornalisti e lo sport. **Plus** aggiungeva il **catalogo** (lanciato nel 2020) [V]: un database delle foto che non sposta i file e contiene solo indice, metadati e anteprime ("proxy") [V].
- Non è un editor e non salva sviluppi come Lightroom [V, Fstoppers].
- Licenze (pagina prezzi Camera Bits, senza data) [V]:
  - Standard: 14,99 $/mese, 149 $/anno, 299 $ perpetua.
  - Plus: 24,99 $/mese, 249 $/anno, 399 $ perpetua.
  - Black Friday 2025: Plus a 149 $ il primo anno [V].
  - Da marzo 2024 si va verso l'abbonamento, e le licenze perpetue di PM6/Plus non ricevono più aggiornamenti importanti [V]. Oggi Plus non è più acquistabile [V].

## 2. Catalogo e gestione file nel dettaglio

**Cosa salva il catalogo** [V]
- Il database è `catalog.pmdb`, dentro una cartella del catalogo che contiene anche la sottocartella **Proxies**.
- Ogni elemento ha di default un'anteprima proxy, di dimensione impostabile. Se la dimensione cambia, la Sync completa rigenera i proxy.
- I proxy possono stare "con il catalogo" o su "External Storage", in una posizione globale (Catalog Preferences → Location for External Proxies). Se si cambia la posizione, la cartella Proxies va spostata **a mano** con l'app chiusa.
- "Calculate Catalog Folder Size" mostra quanto spazio occupano il database e i proxy.
- Indicizza i metadati IPTC/XMP/EXIF, ma **non tutti i campi IPTC** sono cercabili: l'elenco è in Catalog → Searchable fields. Per esempio l'ISO non è indicizzato. Il trucco ufficiale è copiare `ISO={ISO}` nelle parole chiave con un template [V].

**Cataloghi multipli** [V]
- Si possono avere più cataloghi (Catalog Management → New Catalog), ciascuno con due caselle:
  - **Search**: il catalogo entra in ricerca, filtri, Browse e Collections.
  - **Add/Modify**: Scan e Include/Remove agiscono su quel catalogo.
- Una scansione aggiunge gli elementi a **tutti** i cataloghi con Add attivo.
- **Forget** nasconde un catalogo senza cancellarlo. **Reintegrate** lo fa tornare. **Locate Existing Catalog** lo ritrova dopo uno spostamento.
- **Delete** elimina database e proxy in modo definitivo, senza annulla, ma non tocca gli originali.
- **Rename** dall'app rinomina anche la cartella. Rinominarla dal Finder causa errori.
- L'unico tipo di posizione supportato è "Local".

**Dischi esterni e scollegati** [V]
- Un catalogo può coprire più dischi e cartelle, anche offline. Gli elementi di dischi non montati restano visibili grazie ai proxy, con i loro metadati.
- **Limite:** i media offline non possono sincronizzare le modifiche ai metadati ("can't yet sync").
- Stato per miniatura:
  - **verde**: catalogato e presente.
  - **giallo**: catalogato ma non disponibile. Può essere *Offline* (disco non montato) o *Missing* (non più nel percorso noto).
  - **trasparente**: non catalogato.
- Edit → Select Catalog Status → Source File Unavailable seleziona tutti i gialli.

**Dove tenere il catalogo** [V]
- Sul disco più veloce, di solito quello interno. Le foto possono stare su dischi esterni.
- Il NAS è sconsigliato. Dropbox e servizi cloud non sono supportati.
- Si può tenere un catalogo su un disco rimovibile e usarlo da più Mac, ritrovandolo con Locate. Un solo utente alla volta, nessuna condivisione [V].

**Aggiunta al catalogo** [V]
- **Scan to Catalog**: cartelle annidate, con cartelle escluse e filtri per estensione. Durante la scansione si può navigare, ma la ricerca vede solo ciò che è già indicizzato.
- **Include items in Catalog** dal contact sheet.
- **Auto Catalog** durante l'ingest.

**Catalog Sync** [V]
- Impostazioni per catalogo: cartelle incluse (ricorsive, con "Include Existing Paths From Catalog"), cartelle escluse (anche per pattern di nome), estensioni.
- **Quick**: cerca solo i file nuovi.
- **Full**: file nuovi, proxy mancanti e metadati cambiati da altri programmi o su un altro computer.
- Crea in automatico le collezioni `-sync-` → data e ora → **New / Missing / Offline**.
- Pulsanti Start / Pause (riprende da dove si è fermata) / Stop (tiene quanto fatto) / Close (continua in background).
- Le collezioni Missing/Offline sono una **fotografia** del momento: dopo il ricollegamento gli elementi restano nella collezione, solo con l'indicatore verde.
- La documentazione **non** dice che Sync riconosca i file rinominati. Un file rinominato fuori dall'app viene aggiunto come nuovo e quello vecchio resta "missing" da rimuovere a mano [V, "Offline or Missing Media"].

**Spostare, rinominare, copiare dentro l'app**
- Copy/Move (Cmd-Y o trascinamento) [V]:
  - Copia o sposta. Lo spostamento cancella l'originale. La casella "Move" torna su "copia" ogni volta che si apre la finestra.
  - Rinomina con variabili e cartelle con variabili. Destinazioni: cartella originale, sottocartella, cartella corrente, "chiedi sempre".
  - RAW+JPEG come coppia, solo JPEG o solo RAW. Copia dei WAV associati.
  - Applica il template IPTC.
  - **Overwrite**: i file sovrascritti "non si possono recuperare".
- Camera Bits scrive che spostare le cartelle **con Photo Mechanic Plus** aiuta a tenere giusti i percorsi del catalogo [V]. La formula è prudente: "helps ensure". Non ho trovato documentazione che garantisca l'aggiornamento automatico per ogni operazione (move dal Navigator, rinomina di file) [D].
- Remove Folder in Browse toglie dal catalogo la cartella **con tutte le sottocartelle**. La documentazione non parla di conferma né di annulla [V/D].

**Ingest con cartelle a variabili** [V]
- Destinazione primaria più una secondaria facoltativa (doppia copia). Di default viene creata una cartella `YYYYMMDD`.
- "into folder with name": testo più variabili, con `/` per le sottocartelle. Esempio ufficiale: `/Pictures/{year4}/{datesortdash} - Nome evento/`.
- `{ingestsequence}` per le sequenze di cartelle. La rinomina usa variabili e contatore.
- Variabili utili: `{year4}`, `{datesortdash}`, `{date}`, `{iseq}`, `{serial}`, più "Variable Substring Extraction" per tagliare parti di nomi. Non ho trovato `{year}` e `{month}` con questi nomi esatti nelle pagine lette [D].
- Opzioni:
  - **Incremental Ingest**: copia solo i file nuovi. Cambiare l'orologio di sistema lo può confondere (known issue).
  - **Unmount** a fine ingest.
  - **Erase Source after ingest**: la stessa documentazione la sconsiglia.
- Nelle pagine lette non c'è una verifica di integrità della copia (checksum) [D: assente o non documentata].

**RAW + JPEG + XMP** [V salvo dove indicato]
- Il filtro d'ingest "Copy RAW and non-RAW" tratta la coppia come un'unità: stessa destinazione, stesso nome, stesso template [D, guida del forum].
- C'è la modalità di visualizzazione "Combined" per le coppie RAW+JPEG [D, forum].
- Per i RAW non TIFF scrive **sempre** un sidecar XMP. Per i RAW basati su TIFF (NEF, CR2…) il sidecar è facoltativo, perché può scrivere dentro il file.
- Con un'opzione si aggiorna solo il sidecar senza toccare l'embedded.
- Fonti di terzi: PM scrive `.XMP` in maiuscolo, mentre Lightroom usa `.xmp` [D]. Esiste un'impostazione per decidere se l'XMP appartiene al RAW o al JPEG [D].

**Ricerca** [V]
- Quattro strumenti: **Search** (booleana AND/OR), **Filter** (per campo, con grafici a barre dei conteggi e scala log10 facoltativa), **Browse** (albero per metadati e per Folder Path), **Collections** (anche annidate, senza spostare i file).
- Le ricerche salvate ("snapshot") si aggiornano da sole [V, Fstoppers].

**Prestazioni**
- La recensione Fstoppers del 2021 lo definisce "very fast" [V].
- Un utente nel 2020 ha catalogato circa 180.000 foto senza crash, ma è un sostenitore del prodotto [D].
- Nei commenti si parla di settimane per la scansione iniziale di archivi enormi [D].
- Problema noto: il "Pre-loading Metadata" si blocca su molti file [V].
- Non ho trovato dati affidabili sopra il milione di file [D].

## 3. Interfaccia e flusso

- Il pannello **Organizer** affianca la navigazione classica di Photo Mechanic (Navigator, contact sheet) [V].
  - Ha le schede Search/Filter/Browse/Collections.
  - Mostra il selettore dei cataloghi attivi, che si può nascondere se c'è un solo catalogo.
  - Facoltativamente, aprendo una scheda contact sheet di risultati passa all'interfaccia che l'ha prodotta [V].
- Flusso tipico [V/D]: Ingest (con Auto Catalog) → culling e metadati nel contact sheet → l'archivio resta su dischi esterni → ricerca nel catalogo anche a dischi staccati → Sync periodica per allineare.
- In Browse, il sottoalbero **Folder Path** è il luogo dove si gestiscono le cartelle catalogate: rimozione, aggiornamento della posizione.
- Critiche all'interfaccia: su Windows sembra datata, ed è complessa da capire all'inizio [V, Fstoppers]. L'interfaccia del catalogo non scala su Tahoe [V].

## 4. Sicurezza dei file

- Il catalogo non tocca mai gli originali. Delete Catalog elimina solo database e proxy [V].
- Lo spostamento "Move" non resta attivo: torna sempre su copia, una buona difesa contro gli errori [V].
- **Overwrite** cancella in modo irrecuperabile [V]. **Erase source after ingest** è disponibile ma sconsigliato [V].
- Remove Folder rimuove anche tutte le sottocartelle dal catalogo, e le pagine lette non dicono nulla su conferma o annulla [V/D].
- Non esiste un backup integrato del catalogo: bisogna chiudere l'app e copiare almeno `catalog.pmdb`, meglio tutta la cartella [V].
- Non esiste un registro delle operazioni sui file né un annulla documentato per copy/move [D: non trovato].
- Non ho trovato documentata una verifica della copia con checksum all'ingest [D].

## 5. Cosa succede se un'altra app (come RawLine Space) sposta cartelle catalogate, e come si ricollegano

**Verificato** [V]:
1. Photo Mechanic Plus **non segue** gli spostamenti fatti fuori dall'app (Finder, Explorer, quindi anche RawLine Space). Gli elementi diventano **gialli/Missing**. I proxy restano e si vedono ancora anteprima e metadati.
2. **Come si ricollega:** Browse → Folder Path → clic destro sulla cartella → **Update Folder Location…** (prima della build 6375 si chiamava "Choose new location…") → si indica la nuova posizione. Camera Bits ha ripubblicato questo tutorial il 3 settembre 2025 e l'11 febbraio 2026.
3. Il catalogo corregge i percorsi e l'albero Browse si aggiorna, ma **le schede Browse già aperte col vecchio percorso non si aggiornano**: bisogna cliccare di nuovo la cartella.
4. **File rinominati fuori dall'app:** la Sync li aggiunge come nuovi e i vecchi restano Missing, da rimuovere a mano. **Si perdono quindi i dati che stanno solo nel catalogo**, come l'appartenenza alle collezioni, se non sono scritti nell'XMP [V per il comportamento, D per la perdita delle collezioni].
5. **Metadati cambiati da altre app** (per esempio stelle in XMP scritte da Lightroom o RawLine Selects): li rilegge solo **Catalog Sync Full** [V].
6. Il catalogo stesso, se spostato senza Forget, risulta tutto offline. Va fatto Forget → spostamento → Locate → Reintegrate [V].

**Dedotto, implicazioni per RawLine Space** [D]:
- L'aggiornamento è **una cartella alla volta e manuale**. Se RawLine Space riordina centinaia di cartelle, l'utente di PM Plus deve fare centinaia di "Update Folder Location". È un forte motivo per cui RawLine Space dovrebbe **produrre un elenco "vecchio percorso → nuovo percorso"** (CSV o testo) ed eventualmente una guida passo per passo.
- Il formato `catalog.pmdb` non è documentato. Scriverci direttamente sarebbe rischioso, ed è sconsigliato anche perché Camera Bits stessa sta abbandonando il prodotto. Meglio non toccarlo.
- Il modo più semplice per tenere allineato PM Plus: spostare **cartelle intere** mantenendo i nomi dei file, così basta un Update Folder Location sulla cartella madre. Non ho verificato se l'aggiornamento della cartella madre si propaga alle sottocartelle: va provato a mano.
- Rinominare i file in RawLine Space rompe il collegamento in PM Plus più di uno spostamento di cartella.
- Visto lo stato del prodotto, è realistico che molti utenti PM Plus cerchino un'alternativa. Un **importatore di sola lettura del catalogo PM Plus** (collezioni, percorsi) potrebbe essere un argomento forte, ma va valutato se `catalog.pmdb` è leggibile. Dal nome sembra SQLite: la documentazione parla di "SQL Query Planning". Non l'ho verificato.

## 6. Idee da prendere per RawLine Space

1. **Proxy salvati nel catalogo**, con dimensione scelta dall'utente, per **sfogliare e cercare archivi su dischi scollegati**. È la funzione più amata di PM Plus.
2. **Tre stati chiari per ogni file:** presente / disco offline / mancante. Aggiungere un comando "seleziona tutti i non disponibili".
3. **Offline ≠ Missing:** distinguere "disco non montato" da "file sparito". Con l'UUID del volume si può fare meglio di PM [D].
4. **Sync con modalità rapida e completa, che si può mettere in pausa e riprendere**, e che produce **collezioni datate New/Missing/Offline** come rapporto. In RawLine Space queste collezioni dovrebbero aggiornarsi da sole al ricollegamento, a differenza di PM.
5. **Più cataloghi con flag separati "cerca" e "modifica"**: per esempio archivio storico in sola lettura e lavori correnti modificabili.
6. **Forget / Locate / Reintegrate**: chiudere un catalogo senza cancellarlo e ritrovarlo dopo averlo spostato su un altro disco o Mac.
7. **Percorsi a variabili** per ingest e riordino (`{year4}/{datesortdash} - evento`), con **anteprima del percorso risultante** in fondo alla finestra.
8. **Copy/Move che torna sempre su "copia"** a ogni apertura.
9. **Gestione delle coppie RAW+JPEG(+XMP+WAV) come un'unica unità** in copia, spostamento e rinomina.
10. **Exclude per pattern di nome cartella** nelle scansioni, per saltare `Export`, `_tmp`, cache di Lightroom e simili.
11. **Grafici a barre dei conteggi** nei filtri, con scala logaritmica: utili per vedere dove sta il volume dell'archivio.
12. **Il catalogo sul disco veloce interno, gli archivi sui dischi esterni**: è la stessa architettura di PM, sensata per 40–100 TB.

## 7. Cose da NON copiare

1. **Una dipendenza critica da tecnologia di terze parti** per il cuore del catalogo. È la causa diretta della morte di Plus. Per RawLine Space serve SQLite/GRDB o Core Data, sotto il nostro controllo, con formato documentato ed esportabile.
2. **Nessuna via d'uscita dai dati:** gli utenti Plus restano con un `.pmdb` senza esportazione. RawLine Space deve avere export completo (CSV/JSON/XMP) fin dalla prima versione.
3. **Gli spostamenti esterni non vengono riconosciuti in automatico** e si correggono una cartella alla volta. Meglio riconoscere le cartelle spostate da firma o hash, nome e dimensione dei file, e proporre il ricollegamento in blocco.
4. **I file rinominati diventano "nuovo + mancante"** e si perdono collezioni e dati presenti solo nel catalogo. Serve un abbinamento per contenuto o metadati.
5. **Collezioni Missing/Offline che non si aggiornano.**
6. **Schede aperte che restano col percorso vecchio** dopo l'aggiornamento.
7. **Remove Folder che porta via tutte le sottocartelle senza conferma o annulla documentati.**
8. **Proxy esterni da spostare a mano** con l'app chiusa quando si cambia posizione.
9. **Nessun backup integrato del catalogo**, e la richiesta di chiudere l'app per copiarlo. RawLine Space dovrebbe fare backup automatici e coerenti del database.
10. **Overwrite irrecuperabile ed "Erase source after ingest"**: se proprio ci sono, solo con il Cestino e una doppia conferma.
11. **Campi IPTC non indicizzati**, con trucchi come "ISO nelle parole chiave". Bisogna indicizzare tutto ciò che si legge.
12. **Il catalogo vincolato a un sistema operativo e a un'architettura** (Intel/Rosetta, scalatura su Tahoe): serve un'app nativa Apple silicon e test a ogni nuovo macOS.

## 8. Fonti

Ufficiali Camera Bits:
- Photo Mechanic Plus is No Longer Available for Purchase (27 feb 2026, agg. 2 mar 2026): https://home.camerabits.com/photo-mechanic-plus-is-no-longer-available-for-purchase/
- Photo Mechanic 6 on Mac: It's Time to Plan Ahead (2026): https://home.camerabits.com/photo-mechanic-6-on-mac-its-time-to-plan-ahead/
- Photo Mechanic: Now Apple Silicon Native: https://home.camerabits.com/photo-mechanic-now-apple-silicon-native/
- #WorkflowWednesday (elenco tutorial 2025–2026): https://home.camerabits.com/workflowwednesday/
- Updating the Catalog Location of Externally Moved Folders: https://docs.camerabits.com/support/solutions/articles/48001164434-updating-the-catalog-location-of-externally-moved-folders
- [Legacy] stessa guida: https://docs.camerabits.com/support/solutions/articles/48001252551-updating-the-catalog-location-of-externally-moved-folders
- Introduction to Catalogs: https://docs.camerabits.com/support/solutions/articles/48001078324
- Catalog Management: https://docs.camerabits.com/en/support/solutions/articles/48001179060
- Moving a Catalog: https://docs.camerabits.com/support/solutions/articles/48001168255-moving-a-catalog
- Where to Store Your Catalog: https://docs.camerabits.com/support/solutions/articles/48001159651-where-to-store-your-catalog
- Offline or Missing Media: https://docs.camerabits.com/en/support/solutions/articles/48001162818
- Catalog Sync: https://docs.camerabits.com/en/support/solutions/articles/48001161171
- Catalog Preferences: https://docs.camerabits.com/en/support/solutions/articles/48001156772
- Searchable Fields in a Catalog: https://docs.camerabits.com/support/solutions/articles/48001170214-searchable-fields-in-a-catalog
- Removing a Folder from a Catalog: https://docs.camerabits.com/support/solutions/articles/48001166164-removing-a-folder-from-a-catalog/
- Copy/Move Photos Tool: https://docs.camerabits.com/en/support/solutions/articles/48000223598
- Ingesting Photos: https://docs.camerabits.com/support/solutions/articles/48000207409
- Live Ingest: https://docs.camerabits.com/support/solutions/articles/48000341503
- Introduction to Variables: https://docs.camerabits.com/support/solutions/articles/48000207639
- [Legacy] IPTC/XMP Preferences: https://docs.camerabits.com/support/solutions/articles/48001252595--legacy-iptc-xmp-preferences
- Known Issues: https://docs.camerabits.com/support/solutions/articles/48001248753
- Pricing and Information: https://docs.camerabits.com/support/solutions/articles/48001252734-photo-mechanic-pricing-and-information
- Changes to Photo Mechanic Licensing: https://home.camerabits.com/changes-coming-to-photo-mechanic/

Terze parti:
- Fstoppers, recensione parte 2, il catalogo (3 ott 2021): https://fstoppers.com/software/photo-mechanic-plus-lightroom-killer-depth-review-part-2-image-catalog-544151
- Dan Bailey, primo uso del catalogo (2020): https://danbaileyphoto.com/blog/new-photo-mechanic-plus-offers-full-catalog-functionality/
- J.M. Peltier, Cataloging Photo Mechanic Plus: https://www.jmpeltier.com/cataloging-photo-mechanic-plus/
- J.M. Peltier, RAW+JPEG workflow: https://www.jmpeltier.com/raw-jpeg-workflow-solutions/
- PetaPixel, passaggio all'abbonamento (nov 2023): https://petapixel.com/2023/11/15/photo-mechanic-caves-to-industry-trends-shifts-to-subscription-model
