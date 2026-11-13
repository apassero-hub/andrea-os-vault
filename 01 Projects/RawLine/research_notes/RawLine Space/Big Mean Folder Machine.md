# Big Mean Folder Machine (Publicspace)

Ricerca di prodotto per RawLine Space, 11 novembre 2026.
Legenda: **[V]** verificato su fonte (sito ufficiale, manuale, note di rilascio, App Store, recensioni); **[D]** dedotto da me, non scritto da nessuna parte; **[?]** non documentato, da provare con la versione di prova.

---

## 1. Cos'è

- Utility per Mac di Frank Reiff / publicspace.net, lo stesso autore di A Better Finder Rename (ABFR). **[V]**
- Fa tre cose: **dividere** una raccolta in una gerarchia di cartelle (per data, tipo, nome, metadati), **dividere in lotti** (per numero di file o per dimensione), **unire** tante cartelle in una sola. **[V]**
- Pensata per fotografi, chi fa post-produzione, amministratori di sistema: archivi foto Anno/Mese/Giorno da data EXIF, librerie musicali Artista/Album, lotti per DVD/Blu-ray, raccolta di asset sparsi su più dischi. **[V]**
- Nata nel 2007 (beta 1.0 a giugno, 1.0 a ottobre), 2.0 nel 2009. Versione attuale **2.43**. **[V]**
- Lavora tutto in locale, nessun account né cloud. Etichetta privacy sull'App Store: "Data Not Collected". **[V]** L'unica funzione di rete è il controllo aggiornamenti Sparkle (sito). **[V]**
- Prodotto di fatto **fermo**: l'ultima novità funzionale sono HEIC/HEIF (2.37, 2018). Dopo ci sono solo compatibilità (Catalina, Big Sur, Apple Silicon 2.42 nel 2020), dialogo di sblocco (2.43, set 2021) e un aggiornamento App Store per le ricevute (nov 2024). **[V]**

## 2. Funzioni e impostazioni nel dettaglio

### 2.1 Dividere in una gerarchia ("Splitting into folder hierarchies")
- Si sceglie una o più cartelle sorgente, poi **un criterio per ogni livello** da un menu a comparsa, uno schema per i conflitti di nome e la cartella di destinazione. **[V]**
- **Fino a 4 livelli** (il quarto livello è arrivato con la 2.06 nel 2010; alcune pagine vecchie ne dicono 3). **[V]**
- Criteri disponibili per livello (somma di sito, manuale, Macworld 2008, note di rilascio): **[V]**
  - prima, seconda o terza lettera del nome;
  - tipo di file / estensione; codici creator e type del vecchio Mac OS (2.09);
  - data di creazione, data di modifica, **data di scatto EXIF** (JPEG e RAW, HEIC dalla 2.37);
  - tag musicali MP3/AAC, poi FLAC, OGG, AIFF (2.20);
  - **criteri personalizzati**: porzioni del nome (posizioni di carattere o parti separate da delimitatori), date con formato a piacere, tag musicali con segnaposto.
  - livelli basati sul numero di file (1.5): sotto-livelli che si riempiono a quote.
- **Formato delle date nei nomi delle cartelle**: segnaposto tra parentesi angolari mescolati a testo libero. Ci sono `<day>`/`<day0>`, `<month>`/`<month0>`, `<4DigitYear>`/`<2DigitYear>`, `<24hour>`/`<12hour>` (anche con zero davanti), `<amPm>`/`<AMPM>`, `<second0>`, `<dayOfWeek>`, `<dayOfYear>` (con 0 o 00), nome del mese e del giorno, interi o abbreviati da 1 a 5 lettere, nella lingua del sistema. **[V]** La documentazione è incoerente: l'esempio usa `<hour0>` e `<minute0>`, che non compaiono nella tabella. **[V]**
- **Segnaposto musicali**: `<Song>`, `<Artist>`, `<Album>`, `<TrackNum>`/`<0TrackNum>`, `<NumTracks>`, `<CDNum>`, `<NumCDs>`. **[V]**
- **Cartella "Others"**: se manca un dato che il criterio richiede (niente data di scatto, tag assente, file non compatibile), il programma **non indovina** e mette il file in "Others". **[V]** La gestione dei file senza EXIF è stata sistemata più volte (2.07, 2.08, 2.38). **[V]**
- Opzioni di maiuscole/minuscole per i nomi delle cartelle ("sentence case", "proper case", 1.4.5). **[V]**

### 2.2 Dividere in lotti ("Splitting into batches")
- Lotti per **numero di file** (es. 100) o per **dimensione su disco** (es. 100 MB, 4 GB per DVD). **[V]**
- Ordinamento prima della divisione: nome, data di modifica, data di creazione, dimensione, data EXIF, "nome e numero progressivo", con un **criterio secondario**. **[V]** (Macworld 2008)
- Nomi delle cartelle di lotto a intervalli ("0-99", "100-199") o numerati in fila, con formato a scelta. **[V]**
- Dalla 2.17 i lotti si possono fare **mantenendo la gerarchia** esistente. **[V]**

### 2.3 Unire ("Merging into one folder")
- Prende cartelle e sottocartelle e porta tutti i file in una destinazione unica, per "srotolare" una struttura esistente. **[V]**
- In pratica è la loro funzione di **appiattimento**: una modalità "Flatten" a parte non esiste. **[V]**
- Il manuale fa notare che il Finder si blocca quando due nomi coincidono, mentre BMFM risolve il conflitto da solo. **[V]**

### 2.4 Copia o sposta
- **Copia per impostazione predefinita**, gli originali restano dove sono. **[V]**
- Lo **spostamento** c'è dalla 1.3 (2008). L'App Store lo descrive come più veloce e meno pesante sul disco, **ma "less safe"**. **[V]**
- Non può cancellare le cartelle sorgente dopo l'unione o la divisione (critica di Macworld 2008). **[V]** Se sia stato aggiunto dopo **[?]**: le note di rilascio non ne parlano.

### 2.5 Conflitti di nome
- Quando due file finirebbero con lo stesso nome nella stessa cartella, se ne rinomina uno aggiungendo un **numero o una lettera**. **[V]**
- Dalla 2.0 si può configurare l'**ordine dei "distinguisher"** (chi prende (1), chi (2)…). **[V]** Le note di rilascio citano correzioni e accelerazioni del motore dei conflitti (1.6.5, 1.6.9, 2.21) e la conservazione di maiuscole e minuscole (1.6.6). **[V]**
- In ABFR la stessa logica ha questi parametri: tipo di distinguisher ((1),(2)… oppure (a),(b)…), "lascia invariato il primo file", **tre livelli di ordinamento** (data di scatto, poi data di modifica, poi nome con numero progressivo). **[V per ABFR]** È probabile che BMFM usi lo stesso motore. **[D]**
- Un'opzione "salta", "sovrascrivi" o "chiedi" **non risulta** da nessuna parte: si rinomina e basta. **[D]**
- Non risulta un controllo che due file con lo stesso nome siano proprio lo stesso file (hash): cioè nessuna deduplicazione. **[D]**

### 2.6 File collegati (RAW + XMP + JPEG)
- **BMFM non ha un'associazione dei file collegati.** Nessuna pagina, nota di rilascio o recensione ne parla. **[V, per assenza]**
- Rischio concreto **[D]**: con la divisione per data EXIF, un `.xmp` (o un `.THM` o un `.LRV`) senza EXIF leggibile finisce probabilmente in "Others" o in un'altra cartella, cioè **lontano dal suo RAW**. Lo stesso vale per i JPEG con EXIF diversi o tolti, e per l'ordine nei lotti per dimensione, che può dividere una coppia tra due lotti. Da provare.
- Il "fratello" ABFR invece, dalla v12, ha la **File Extension Pairing** **[V]**:
  - spunta "Use File Extension Pairings" nell'azione Advanced Options;
  - "Take names from:" (estensioni principali, es. `cr3, nef, arw`) e "Apply to:" (estensioni collegate, es. `xmp, jpg, gps`);
  - abbinamento per **nome base** uguale; se ci sono più estensioni sorgente vince la prima in lista; un file principale può avere più collegati; un collegato senza principale non viene toccato;
  - l'abbinamento si applica **prima** della risoluzione automatica dei conflitti, quindi in rari casi i nomi finali possono divergere. Lo dice la documentazione stessa: "controllare prima di rinominare".

### 2.7 Impostazioni salvate e automazione
- Le impostazioni vengono ricordate tra una sessione e l'altra (1.6). **[V]**
- C'erano le **droplet** (impostazioni salvate in una mini-app su cui trascinare le cartelle), poi **tolte nella 2.24 (2012)** per Developer ID. **[V]**
- Nel 2008 Macworld lamentava l'assenza di preset con nome. Oggi non risultano preset multipli in BMFM **[?]**, mentre ABFR ha preset e droplet.

## 3. Interfaccia e flusso

- **Assistente a passi** ("assistant-style"): ogni scelta viene spiegata lungo la strada. Il "pannello di controllo" per utenti esperti, promesso nel 2007, non risulta mai arrivato. **[V]/[D]**
- Il flusso tipico **[V]**:
  1. si trascinano una o più cartelle sorgente nella finestra;
  2. si sceglie l'operazione: gerarchia, lotti o unione;
  3. si impostano i criteri per livello, il formato dei nomi e lo schema dei conflitti;
  4. si sceglie la destinazione, poi copia o sposta;
  5. **anteprima** della struttura risultante;
  6. si conferma, si annulla o si torna a correggere;
  7. "Execute".
- **Anteprima** **[V]**:
  - mostra la **gerarchia di cartelle prevista** come albero da **espandere** cartella per cartella, fino ai file;
  - la guida ufficiale la usa come strumento di diagnosi: se manca un file, si espande l'albero per vedere dove finisce, si controlla "Others", e se non compare per niente si segnala un bug;
  - nel 2008 **non mostrava la dimensione delle cartelle** (critica di Macworld), e non risultano correzioni **[?]**;
  - si fa su dati calcolati dal motore con database interno, prima di toccare qualunque file ("Full preview before anything is done", annuncio 2.0).
- Avanzamento: un utente App Store (2018) chiede una schermata di stato più dettagliata e "una barra di avanzamento che funzioni". **[V]**
- Il programma resta aperto dopo un'operazione (dalla 1.1). **[V]**
- Non c'è un filtro per tipo (es. "solo i .avi"), né una divisione o unione selettiva (Macworld 2008). **[V]** Se sia stato aggiunto dopo **[?]**.

## 4. Sicurezza dei file

| Aspetto | Big Mean Folder Machine | A Better Finder Rename 12 |
|---|---|---|
| Anteprima | albero della struttura finale, espandibile **[V]** | tabella "nome attuale / Change to", evidenziazione delle modifiche, colonna dei risultati intermedi, percorso **[V]** |
| Predefinito sicuro | **copia** di default **[V]** | rinomina sul posto |
| Conferma | conferma dopo l'anteprima **[V]**; altro non è documentato | dialogo opzionale per ogni file: Quick Look, From/To, percorso, bottoni **Stop / Rename / Rename All** **[V]** |
| Errori | non documentato; la guida rimanda alla Console per i casi difficili **[V]** | dialogo con Problem / File / **Stop, Ignore This Problem, Ignore All Problems**, poi un riepilogo di tutti gli errori **[V]** |
| Annulla | **non esiste** (mai citato) **[D, quasi certo]** | **non esiste** per le rinomine eseguite: Edit › Undo annulla solo le modifiche alle impostazioni **[V]** |
| Registro | nessun log delle operazioni; solo un output di debug in Console, disattivabile (2.13) **[V]** | "Save File List…" esporta in TSV i nomi vecchi e nuovi, **ma solo se lo fai prima**; per tornare indietro si scambiano le colonne in un foglio di calcolo e si usa "Rename from file list" **[V]** |
| Interruzione a metà | non documentato: se il disco si riempie "la copia si ferma" e basta **[V]** | non documentato cosa resti a metà **[V]** |
| Controllo dello spazio | nessuno preventivo: la guida dice di verificarlo tu **[V]** | — |
| File system | consiglia APFS o HFS+ journaled; problemi con NAS (Synology va montato in AFP), Drobo (limiti di percorso), dischi non Mac, caratteri speciali, lunghezza dei nomi **[V]** | 3 meccanismi di rinomina (Standard, Unicode File Manager, Low-level) con ripiego automatico; opzione per ignorare i controlli sui volumi di sola lettura **[V]** |
| Consiglio ufficiale | "lavora su una copia" (per le correzioni ai nomi) **[V]** | "backup due volte più importante" sui lavori grandi **[V]** |

- In sostanza la sicurezza di BMFM sta in **copia predefinita + anteprima**, e basta. Una volta eseguito non c'è un registro di cosa è andato dove, non c'è ripristino, e non c'è una verifica della copia (checksum). **[D, coerente con tutto il documentato]**
- Storia: la **1.6.6 è stata ritirata** perché un bug di Leopard mostrava **anteprime sbagliate** ed errori fuorvianti. **[V]** È la prova che un'anteprima che non corrisponde all'esecuzione è il guasto peggiore possibile.
- La 1.2.1 ha corretto due casi in cui file invisibili, o con "/" nel nome, **non venivano copiati**. **[V]** Le perdite silenziose ci sono state.

## 5. Prezzo, piattaforme, limiti, critiche

- **Prezzo**: **€29,95** dal sito, una tantum; su App Store **$29,99**, con Family Sharing. **[V]** Storico: $19,95 (2009), $14,95 (2010). Licenze famiglia, piccola impresa, business ed enterprise (AlternativeTo dà una fascia di $30–60). **[V]**
- **Prova**: copia **solo i primi 10 file**. **[V]**
- **Piattaforme**: solo Mac. Universal (Intel + Apple Silicon). Il sito dice macOS 10.7 → 27; l'App Store chiede macOS 12.4 o successivo. **[V]** Solo in inglese. **[V]** Nessuna dichiarazione di accessibilità. **[V]**
- **Prestazioni**: motore a 64 bit con database interno, "centinaia di migliaia di file e terabyte" (dichiarato). **[V]** Su ABFR, dello stesso autore, i numeri sono espliciti **[V]**:
  - 20–50 mila file sono comodi con 16 GB di RAM;
  - consigliati lotti da 10–20 mila;
  - provato fino a 300 mila e oltre;
  - 100 mila file ci mettono "almeno 100 volte" più di 1.000;
  - leggere l'EXIF significa caricare **file interi**, ed è "molto lento" sulle librerie grandi;
  - conviene fare le prove su un sottoinsieme.

  Su 40–100 TB di RAW (milioni di file) BMFM è quindi con ogni probabilità **fuori scala** **[D]**.
- **Limiti e critiche raccolte**:
  - niente preset con nome per i lavori ricorrenti (Macworld 2008) e droplet rimosse nel 2012; **[V]**
  - niente filtro per tipo, niente unione o divisione selettiva; **[V 2008]**
  - l'anteprima non mostra le dimensioni; **[V 2008]**
  - manca un criterio per l'orientamento EXIF (verticale/orizzontale); **[V 2008]**
  - non cancella le sorgenti dopo uno spostamento o un'unione; **[V 2008]**
  - barra di avanzamento e stato poco chiari; **[V 2018]**
  - la versione App Store andava in crash su Monterey (sandbox), quella del sito no; **[V 2022]**
  - "è potente, studia le istruzioni prima: è facile sbagliare le strutture" (utente 2017); **[V]**
  - non legge i sidecar e non tiene insieme i file collegati; **[D]**
  - nessun annulla e nessun registro; **[D]**
  - manuale online scarno e in parte incoerente (segnaposto); **[V]**
  - sviluppo fermo dal 2018. **[V]**
- Recensioni: Macworld 2008 4/5 (Dan Frakes, "huge time-saver"); sull'App Store poche recensioni, tutte positive sulla potenza. Recensioni indipendenti recenti non ne ho trovate. **[V]**

## 6. Idee da prendere per RawLine Space (concrete)

1. **Gerarchia per livelli con un criterio per livello** (fino a 4 o più): un elenco ordinato di livelli, ciascuno con criterio + formato. È lo schema mentale più semplice per "Anno / Mese / Cliente / Tipo".
2. **Formati di data a segnaposto** (`<4DigitYear>-<month0>`), ma con **anteprima live del nome cartella** accanto al campo e un catalogo dei segnaposto cliccabile, così non si ripete l'incoerenza `<hour0>`. Aggiungere anche la "notte che conta per il giorno prima" (il night mode di ABFR) per i servizi serali.
3. **Una cartella esplicita per i file senza dato** ("Others") invece di indovinare, ma **dichiarata in anteprima con un conteggio e un motivo** ("312 file senza data di scatto"), con la possibilità di scegliere un ripiego (data del file, data dello XMP, data della cartella padre).
4. **Copia come predefinito** e lo spostamento etichettato come meno sicuro, così l'utente sceglie consapevolmente. Per RawLine Space la scelta copia/sorgente va presentata con le conseguenze (spazio necessario, ripristino).
5. **Lotti per dimensione o per numero, preservando la gerarchia** (per dischi d'archivio o LTO), con ordinamento primario e secondario.
6. **Risoluzione dei conflitti configurabile e deterministica**: tipo di suffisso, "lascia invariato il primo", ordine di priorità (data di scatto, poi modifica, poi nome). In più, prima di rinominare, **confronto per hash**: se è lo stesso file è un duplicato, non un conflitto.
7. **File collegati alla maniera di ABFR, ma come gruppo indivisibile**: abbinamento per nome base con estensioni "principali" e "collegate"; la data e la destinazione del gruppo si prendono dal file principale; il gruppo non si divide mai tra cartelle o lotti; i conflitti si risolvono **dopo** a livello di gruppo (correggendo il difetto che ABFR stesso documenta).
8. **Dialogo di conferma e di errore alla ABFR**: From/To con Quick Look e percorso cliccabile; per gli errori Stop / Ignora questo / Ignora tutti, più un **riepilogo finale** degli errori.
9. **Avvisi sul file system prima di partire**: volume non APFS o HFS+, NAS in SMB, caratteri o lunghezze di percorso a rischio, spazio libero insufficiente. BMFM li mette in una pagina di troubleshooting: noi li controlliamo **prima**, nell'anteprima.
10. **Lavorare su un sottoinsieme** come funzione vera e propria ("prova su 500 file a campione"), visto che lo stesso autore lo consiglia per i lavori grandi.
11. **Motore con database locale** per centinaia di migliaia di elementi (BMFM lo dichiara), ma con lettura dei metadati **parziale** (solo l'intestazione EXIF, mai il file intero) e un indice che riprende da dove si è fermato.

## 7. Cose da NON copiare

- **Nessun annulla, nessun registro.** In BMFM e in ABFR, una volta eseguito, il ripristino è "usa il backup", oppure in ABFR un TSV da salvare **prima** a mano e invertire in Excel. Per RawLine Space il registro dev'essere **automatico, sempre attivo, scritto prima di ogni mossa** (journal), e il ripristino un pulsante.
- **Anteprima che può divergere dall'esecuzione** (il caso della 1.6.6 ritirata). L'anteprima deve essere lo **stesso piano** che poi viene eseguito, non un calcolo parallelo, e va ricontrollata al momento di eseguire (file cambiati nel frattempo).
- **Anteprima senza numeri**: niente dimensioni, niente conteggi per cartella, niente spazio necessario. Va mostrato tutto, per cartella e in totale.
- **Copiare senza verificare**: nessun checksum, nessun controllo dello spazio prima di partire, "se il disco si riempie si ferma". Inaccettabile su archivi da decine di TB.
- **Interruzione a metà non documentata**: deve essere chiaro e riprendibile cosa è stato fatto e cosa no.
- **Spostamento "meno sicuro" senza rete di protezione**: se si lavora sulla sorgente, ogni spostamento sullo stesso volume va registrato e reso reversibile; tra volumi diversi si fa copia + verifica + rimozione solo dopo la verifica.
- **Trattare ogni file da solo**: dividere RAW e XMP o JPEG per data o per lotti è il rischio n. 1 per un fotografo.
- **Assistente rigido senza preset con nome**: i lavori ricorrenti vanno salvati come ricette.
- **Barra di avanzamento vaga**: servono file e byte fatti / totali, velocità, tempo stimato, file corrente.
- **Leggere i file interi per l'EXIF** (la lentezza dichiarata di ABFR).
- **Diagnosi rimandata alla Console di sistema**: gli errori devono stare nell'app, leggibili, esportabili.
- **Manuale scarno**: la guida deve coprire anteprima, conflitti e ripristino in modo completo.
- **Prova "solo 10 file"**: limita la valutazione su un archivio vero. Meglio una prova a tempo, o una solo in anteprima ma completa.

## 8. Fonti

- Sito ufficiale BMFM: https://www.publicspace.net/BigMeanFolderMachine/
- Manuale: https://www.publicspace.net/BigMeanFolderMachine/Manual.html
- Formati data: https://www.publicspace.net/BigMeanFolderMachine/Manual_Date_Format.html
- Formati tag musicali: https://www.publicspace.net/BigMeanFolderMachine/Manual_Music_Tags_Format.html
- Risoluzione problemi: https://www.publicspace.net/BigMeanFolderMachine/troubleshooting.html
- Note di rilascio: https://www.publicspace.net/BigMeanFolderMachine/version.html
- App Store: https://apps.apple.com/app/id402440280
- Macworld, recensione 1.5.1 (2008): https://www.macworld.com/article/1136598/bmfm.html
- MacTech, 2.0 (2009): https://www.mactech.com/2009/07/22/the-big-mean-folder-machine-2-0-gets-tweaked-user-interface
- MacTech, 2.0.8 (2010): https://www.mactech.com/2010/10/19/big-mean-folder-machine-update-allows-folder-hierarchies-to-be-split/
- Blog Publicspace, prima beta (2007): https://www.publicspace.net/blog/mac/2007/06/20/bigmeanfoldermachine/
- AlternativeTo: https://alternativeto.net/software/big-mean-folder-machine/about/
- SourceForge (scheda): https://sourceforge.net/app/the-big-mean-folder-machine/mac/
- Softpedia, changelog: https://mac.softpedia.com/progChangelog/The-Big-Mean-Folder-Machine-Changelog-26558.html
- ABFR, sito: https://www.publicspace.net/ABetterFinderRename/
- ABFR, indice della guida v12: https://www.publicspace.net/ABetterFinderRename/v12/index.html
- ABFR, annullare una rinomina: https://www.publicspace.net/ABetterFinderRename/v12/UndoingARename.html
- ABFR, dialogo di conferma: https://www.publicspace.net/ABetterFinderRename/v12/ConfirmationDialog.html
- ABFR, dialoghi di errore: https://www.publicspace.net/ABetterFinderRename/v12/ErrorDialogs.html
- ABFR, finestra principale e anteprima: https://www.publicspace.net/ABetterFinderRename/v12/MainWindow.html
- ABFR, file collegati: https://www.publicspace.net/ABetterFinderRename/v12/FilePairing.html
- ABFR, Advanced Options: https://publicspace.net/ABetterFinderRename/v12/AdvancedOptions.html
- ABFR, opzioni dei conflitti: https://publicspace.net/ABetterFinderRename/v12/FileNameConflictResolutionOptions.html
- ABFR, risoluzione automatica: https://www.publicspace.net/ABetterFinderRename/v12/AutomaticFileNameResolution.html
- ABFR, meccanismi di rinomina: https://www.publicspace.net/ABetterFinderRename/v12/RenameMechanisms.html
- ABFR, lavori molto grandi: https://www.publicspace.net/ABetterFinderRename/v12/DealingWithLargeRenamingTasks.html
- ABFR, novità v12: https://www.publicspace.net/ABetterFinderRename/version12.html
