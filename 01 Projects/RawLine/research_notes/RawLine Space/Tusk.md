# Tusk (tuskbackup.com)

Ricerca dell'11 novembre 2026 per RawLine Space. Legenda: **[V]** = verificato su una fonte (sito, documentazione, articolo); **[D]** = dedotto da indizi, non dichiarato.

## 1. Cos'è

- App macOS di backup "a progetti" per videomaker e fotografi: guarda una cartella di progetto, copia i file nuovi o modificati su più destinazioni (dischi esterni, SD, Google Drive, Dropbox, S3 compatibile) e tiene un catalogo di **dove sta ogni copia di ogni file**, anche con i dischi scollegati. **[V]**
- Lo slogan del sito: mostra dove vive ogni file anche quando i dischi non sono collegati. Su Product Hunt: "the backup app that never forgets where your files went". **[V]**
- La promessa che conta per noi: **liberare spazio sul Mac** ("Delete Local") solo quando ogni file ha una copia verificata su ogni destinazione, e **ripristinare con un clic** dalla copia migliore disponibile. **[V]**
- Sviluppatore: **Niklas Fischer**, ingegnere software (founding engineer di cleverklagen, ex data scientist DAZN e FC Barcelona, titolare dell'agenzia kizo.agency, autore di corsi Udemy/Packt). L'ha fatta perché copiava a mano i video dei suoi corsi sui dischi e non sapeva più cosa fosse salvato dove. Non c'è una società con sede dichiarata: il piè di pagina dice solo "© 2026 Tusk". **[V]**
- Storia: prime versioni 0.2 a fine maggio 2026, beta di circa due mesi, 1.0 il 21 luglio 2026, lancio pubblico a inizio agosto (Newsshooter 3 ago, PetaPixel 7 ago, No Film School). Al 4 novembre è alla 1.12.8: 61 versioni in sei mesi, quindi uno sviluppatore solo che rilascia di continuo. **[V]**
- Funziona tutto in locale: nessun server Tusk, nessun account, nessuna telemetria. Il catalogo resta sul Mac; i file escono solo verso i cloud che l'utente collega. **[V]** (Unica chiamata di rete propria: il server licenze, vedi sez. 5.)

## 2. Funzioni e impostazioni nel dettaglio

**Progetti**
- Un progetto è una cartella "primaria" sul Mac più fino a **5 destinazioni**. La documentazione consiglia 2–3 (regola 3-2-1: l'originale conta come una copia, quindi minimo un disco locale + uno fuori sede). **[V]**
- Limite di **100.000 file per progetto** ("il massimo testato"); nessun limite al numero di progetti. Lavora per cartelle: non tratta un disco intero come un unico indice piatto. Per dischi pieni di file sparsi senza struttura rimanda a NeoFinder o DiskCatalogMaker. **[V]**
- Se rinomini la cartella nel Finder, il progetto va in "Folder missing" e compare un banner **Relink**: indice, destinazioni e storia restano. **[V]**
- Guarda la cartella e sincronizza in background (anche riesportazioni, salvataggi automatici di progetto, clip rinominate). Rallenta quando il Mac è sotto carico, si mette in pausa durante gli scarichi da SD, e c'è la sincronizzazione manuale. **[V]**
- Pianificazione per destinazione (es. ogni ora sull'SSD, ogni settimana fuori sede) e limiti di banda: **non ci sono**. Richiesti su Product Hunt; il creatore li ha promessi "nelle prossime settimane" per i progetti grandi. **[V]**

**Traccia un disco esistente ("Track an existing drive" / "Scan drive")**
- Aggiunge un disco che contiene già materiale: calcola l'hash dei file e costruisce i progetti **senza spostare né riscrivere nulla**. I dischi più grandi di 100.000 file vanno divisi in più progetti. **[V]**
- Trova i duplicati solo durante l'importazione, quando cerca copie locali. **[V]**

**Offload da SD (scarico schede)**
- Legge la scheda **una volta sola** e scrive in parallelo su tutte le destinazioni, calcolando BLAKE3 durante la copia; non serve spazio libero sul Mac. **[V]**
- Due modalità con lo stesso motore: **Standalone Offload** (copie verificate + rapporto, nessun tracciamento dopo) e **Project Offload** (i file entrano in un progetto con sync, ripristino e Delete Local). **[V]**
- Interruttore "copia di lavoro locale" (solo project offload): spento di solito, e allora i file risultano "Remote only"; acceso, vengono scritti anche nella cartella primaria. **[V]**
- Rapporto esportabile in **PDF o CSV** con nome, dimensione e checksum BLAKE3 per ogni destinazione. **[V]**
- Le sessioni sono salvate su disco: un crash, una chiusura o un riavvio riprendono dopo l'ultimo file completato. Per i file falliti c'è **Retry** con il motivo (errore di lettura, checksum diverso, timeout di rete). **[V]**
- Avviso esplicito: non formattare la scheda finché ogni file non è verificato su ogni destinazione. **[V]**

**Destinazioni**
- Dischi esterni: scegli una sottocartella (non la radice). Struttura e nomi originali mantenuti, **nessun contenitore proprietario**: i file si aprono con qualsiasi app anche senza Tusk. **[V]**
- Google Drive (permesso `drive.file`, più account, controllo quota prima dell'offload ma non a ogni sync), Dropbox (confinato in `Apps/Tusk`), S3 compatibile (B2, Wasabi, R2, AWS, MinIO; la cartella di destinazione deve essere vuota). **[V]**
- Una destinazione rimossa smette di ricevere file ma non perde quelli già scritti. **[V]**

**Impostazioni (Preferences, ⌘,)**
- Quelle documentate sono poche: **Accounts** (ricollegare i cloud), **License**, e un `settings.json` con preferenze d'interfaccia (ultima pagina, barra laterale, notifiche on/off). Non ho trovato una pagina che elenchi tutte le impostazioni. **[V]** per quelle citate; il resto non è documentato.
- Esiste una funzione di **repair** (dalla 1.12.8 mostra in GB/MB lo spazio che serve per completarla) e una di **Redistribute** (rispedisce le copie verificate da altre destinazioni a quella dove mancano). **[V]**

**Scelta automatica del disco più veloce**
- No Film School scrive che Tusk sceglie da solo il disco collegato più veloce per backup e ripristini. **[V, ma solo da articolo]**
- Nella documentazione c'è solo un punto: se durante un ripristino il disco sorgente si scollega, Tusk passa da solo **alla sorgente successiva più veloce** se esiste; altrimenti il ripristino va in pausa finché non ricolleghi il disco. **[V]**
- Come misura la velocità (test di lettura, tipo di collegamento, locale prima del cloud) non è scritto. **[D]** Probabilmente un ordine fisso tipo SSD/disco locale prima del cloud.

## 3. Interfaccia e flusso

- **App da barra dei menu** senza finestra fissa: chiudendo la finestra (⌘W) Tusk resta nella barra e continua a sincronizzare e scaricare; si chiude davvero con ⌘Q o col tasto destro sull'icona → Quit. **[V]**
- Finestra principale con barra laterale: **Projects, Drives, Offload, Search** (sul sito anche "Scan drive"). Ricerca globale in alto con ⌘K. Pagine **Jobs** e pannello **Notifiche**. **[V]**
- Vista progetto: **tabella dei file con lo stato di ogni file su ogni destinazione**, con un menu per riga (Restore, Retry, Redistribute). Pannello delle posizioni con l'indicatore offline. **[V]**
- Pagina Drives: ogni disco con stato e "Last seen" (ultima volta visto). **[V]**
- Stati usati (glossario ufficiale), utili come riferimento per il nostro vocabolario: **[V]**
  - File: Synced, In progress, Partial, Not local, Remote only, Missing on (destinazione), Error, Queued.
  - Progetto: Synced, In progress, Partial, Disconnected destination, Folder missing.
  - Disco: Connected, Disconnected, Reconnecting (di solito meno di un secondo).
  - Lavori: Active, Queued, Paused, Success, Partial, Cancelled, Failed. Ogni lavoro in coda dice **perché** aspetta.
- Primo avvio: prova di 14 giorni automatica, schermata di benvenuto che chiede l'accesso a Documenti, Scrivania, Immagini, Filmati, ecc.; per i dischi rimovibili macOS chiede il permesso la prima volta. **[V]**
- Scorciatoie poche e standard (⌘N nuovo progetto, ⌘, preferenze, ⌘⇧L log, ⌘R ricarica finestra). Non ci sono ⌘1–⌘4 per la barra laterale. **[V]**
- Tecnologia: download da ~239 MB, scorciatoia "Reload window", credenziali "encrypted with macOS safeStorage". Tutti indizi tipici di un'app **Electron**, non nativa. **[D]**
- Flusso tipico (demo No Film School): crei il progetto → aggiungi SSD + Google Drive → backup in parallelo → **Delete Local** → ripristino di tutto con un clic. **[V]**

## 4. Sicurezza dei file (verifica, ripristino)

**Verifica**
- Hash **BLAKE3** su ogni trasferimento. Nell'offload l'hash dei byte sorgente si calcola una volta e si confronta con quanto scritto su ogni destinazione; l'hash viene salvato per ricontrolli futuri. **[V]**
- Se rilegga davvero dal disco di destinazione dopo la scrittura (rilettura vera, non dalla cache) **non è scritto**. **[D]** La formula "computed during the copy" fa pensare a un hash calcolato in streaming, non a una rilettura separata.
- Sui cloud (Google Drive, S3) la documentazione **non dice** come verifica: niente su MD5 di Drive, ETag o checksum di S3. **[V che manca]**
- "Synced" vuol dire che c'è una copia verificata su ogni destinazione e che la copia locale corrisponde all'hash registrato. **[V]**
- Quando un disco si ricollega fa un **controllo rapido (stat)** di ogni file atteso, non un nuovo hash completo. I file mancanti o cambiati diventano "Missing on…". **[V]** Quindi il bit rot sul disco di backup non lo vede finché non si rifà un controllo completo. **[D]** (Il loro blog parla di bit rot, ma non ho trovato una funzione di "scrub" periodico documentata.)

**Eliminazione locale ("Delete Local")**
- Prima di togliere un file dal Mac controlla che **ogni destinazione collegata** abbia il file con checksum uguale. Se manca qualcosa **o un disco è scollegato, blocca** e dice cosa manca. **[V]**
- I file eliminati vanno nel **Cestino di macOS**, non vengono cancellati per sempre; dopo che il Cestino è vuoto si usa Restore. **[V]**
- I backup sono **additivi**: cancellare in locale non tocca mai le destinazioni. **[V]**
- Una procedura passo passo di Delete Local nella documentazione pubblica non c'è (la pagina dedicata non esiste). **[V che manca]**

**Ripristino**
- Un clic su un file o su tutto il progetto, dalla "best available copy": per i dischi va collegato il disco, per il cloud scarica dal provider. Stessa verifica a checksum. **[V]**
- Se la sorgente si scollega a metà passa alla sorgente successiva più veloce, oppure mette in pausa. **[V]**

**Dischi scollegati e interruzioni**
- Si accorge di un'espulsione in pochi secondi (eventi di montaggio/smontaggio di macOS). Annulla il trasferimento in corso verso quel disco, così **non lascia file a metà**. Le altre destinazioni continuano. **[V]**
- Un cavo strappato può lasciare scritture parziali, che vengono pulite al ricollegamento. **[V]**
- Riconoscimento dei dischi: la documentazione **si contraddice**. Una pagina dice "per nome del volume", un'altra "per UUID del volume". Rinominare nel Finder mantiene l'UUID; riformattare crea un disco nuovo (il vecchio si toglie con **Forget**). Consiglia di scrivere lo stesso nome su un'etichetta fisica. **[V]**

**Dati dell'app**
- Catalogo in **SQLite** (`~/Library/Application Support/Tusk/tusk.db`), che la documentazione indica come il file più importante da salvare. Log giornalieri tenuti 30 giorni, senza contenuti né password ma con i percorsi. Credenziali nel Portachiavi (`so.tusk.*`). **[V]**
- Non risulta che scriva un manifest o un indice **sui dischi di backup**: se perdi `tusk.db`, il catalogo non si può ricostruire dai dischi. **[D, dall'assenza nella documentazione]**

## 5. Prezzo, piattaforme, limiti, critiche

- **Prezzo**: acquisto unico da **79 $**, con i primi 100 a 49 $. Include un anno di aggiornamenti; dopo continua a funzionare. Prova di 14 giorni senza carta né account. Ogni chiave vale per **2 attivazioni**. **[V]**
- **Piattaforme**: solo macOS 12+, Apple Silicon e Intel (alcune versioni sono uscite solo per Apple Silicon). Download firmato e notarizzato. **[V]**
- **Licenza online**: il server licenze va raggiunto; c'è un "grace token" firmato che dura qualche giorno, poi serve la rete o un token manuale dal supporto. **[V]** Per noi questo è un punto debole: sul campo senza rete per settimane l'app si bloccherebbe. **[D]**
- **Limiti dichiarati**: 100.000 file per progetto; lavora per cartelle; niente cloni avviabili, niente backup continuo di tutto il Mac, **niente snapshot né storico delle versioni**; Dropbox limitato alla cartella dell'app; i token OAuth non passano da un Mac all'altro; i file cancellati si recuperano dal Cestino solo finché non lo svuoti. **[V]**
- **Cosa non fa come catalogo**: niente miniature né anteprime, niente metadati EXIF/IPTC e niente ricerca avanzata, almeno nel loro stesso confronto con NeoFinder e DiskCatalogMaker ("non è nato come catalogatore"). **[V]**
- **Critiche**: non ho trovato recensioni indipendenti né prove sul campo. Product Hunt: zero recensioni, 17 voti; i commenti chiedono la pianificazione per destinazione e i limiti di banda. Un commento di lode è stato liquidato dal creatore come scritto da un'AI. No Film School dice solo che "non è per tutti", specie per chi gestisce già bene i propri file. Su Reddit non ho trovato niente. **[V]**
- Altri rischi che vedo: è un prodotto giovane di uno sviluppatore solo, con rilasci quasi quotidiani (in agosto ha corretto blocchi dell'app con progetti grandi e falsi avvisi "dirty drive"); documentazione incompleta proprio sui punti critici (verifica sui cloud, procedura di Delete Local, criterio del disco più veloce); dentro c'è una contraddizione UUID/nome. **[D]**
- Il blog (51 articoli in sei mesi) è soprattutto materiale SEO e comparativo, scritto dal creatore. **[V]**

## 6. Idee da prendere per RawLine Space (concrete, senza cloud)

1. **Stato per file × per disco**: una tabella dove ogni riga è un file (o un progetto) e ogni colonna un disco, con stati chiari: Sincronizzato, Parziale, Non in locale, Mancante su X, Errore, In coda. Prendere il loro vocabolario come base e tradurlo in italiano.
2. **Catalogo che vale anche a disco scollegato**: ogni disco ha "visto l'ultima volta il…", il suo indice consultabile e la ricerca su tutti i dischi, anche quelli in un cassetto. È il cuore per archivi da 40–100 TB.
3. **"Libera spazio" bloccato finché non è sicuro**: si cancella solo se ogni file ha almeno N copie verificate (N lo scegli tu, minimo 2), con hash uguale, **su dischi collegati in quel momento**. Se un disco manca, si blocca e si spiega cosa manca e su quale disco.
4. **Cestino, mai cancellazione diretta**, più un nostro "cestino di progetto" con data, così si può annullare anche dopo che il Cestino di macOS è stato svuotato a metà.
5. **BLAKE3** (o xxHash3 per la velocità + BLAKE3 per la sicurezza) calcolato **in streaming durante la copia**, con l'hash salvato. Lettura unica della sorgente e scrittura in parallelo su più dischi.
6. **Traccia un disco esistente senza toccarlo**: scansione di sola lettura che crea il catalogo dagli archivi già pieni. È il primo passo obbligato per chi ha 100 TB.
7. **Sessioni che riprendono dopo un crash**, dall'ultimo file completato; annullare il file in corso se il disco si scollega, così non restano file a metà; **Retry** per i singoli file col motivo leggibile.
8. **Rapporto PDF/CSV** con nomi, dimensioni, hash e dischi, da dare al cliente o da tenere come prova di archiviazione.
9. **Redistribuisci**: se a un disco mancano file, ricopiarli da un altro disco verificato. **Ripristina**: dalla sorgente collegata più veloce, passando da sola alla successiva se una si scollega.
10. **Nomi dei dischi + etichetta fisica**: riconoscere i dischi per UUID, mostrare un nome scelto dall'utente e suggerire di stamparlo come etichetta (perfino un PDF di etichette da RawLine Space). "Dimentica disco" quando un disco viene riformattato.
11. **Ogni lavoro in coda dice perché aspetta** (disco scollegato, in pausa, dipende da un altro lavoro).
12. **Relink** quando una cartella viene rinominata o spostata, senza perdere storia e hash.
13. **Nessun formato proprietario**: i file restano con nome e struttura originali; RawLine Space è solo lo strato di catalogo e sicurezza. Se si disinstalla l'app, non si perde niente.
14. Indicatore nella **barra dei menu** solo per i lavori lunghi (scansioni, copie, verifiche) e per i dischi che si collegano. L'app vera resta una finestra completa.

## 7. Cose da NON copiare

- **Licenza da verificare online** con grace di pochi giorni: contraria alla regola 100% offline. Da noi la licenza va attivata una volta e poi deve funzionare per sempre senza rete.
- **Cloud come destinazione** (Drive, Dropbox, S3): fuori dalla filosofia RawLine Space. Al loro posto: più dischi locali, un disco "fuori sede" che si porta via e un NAS in rete locale, se mai.
- **Catalogo solo in un database sul Mac**: se si perde `tusk.db`, si perde la mappa. Noi dobbiamo scrivere anche un **manifest su ogni disco** (es. un file nascosto con gli hash) e un backup automatico del catalogo, così l'archivio si ricostruisce dai dischi stessi.
- **Controllo al ricollegamento solo con stat** (dimensione e data): non basta per dire "sicuro da cancellare" sui progetti vecchi. Prima di liberare spazio serve una **rilettura vera con hash** dal disco di destinazione, più un controllo periodico (scrub) contro il bit rot.
- **Dichiarare "verificato" senza dire come**: noi dobbiamo dire chiaramente cosa è stato controllato (hash rilletto dal disco, data, quale disco).
- **Limite di 100.000 file per progetto** e nessun indice di tutto il disco: per archivi fotografici (un matrimonio fa già 5–10.000 RAW + XMP + export) serve un catalogo che regga milioni di file.
- **Nessuna anteprima né metadato**: per i fotografi riordinare senza miniature, data di scatto, fotocamera, stelle e colori XMP serve a poco. RawLine Space deve leggere gli XMP (li sappiamo già gestire in Selects) per decidere cosa è "non usato".
- **Electron da 240 MB** e rilasci quasi quotidiani: per un'app che cancella file servono un'app nativa e rilasci prudenti, con prove sulle dimensioni reali.
- **Documentazione contraddittoria** (riconoscimento per nome o per UUID): su una funzione di sicurezza va scritta una regola sola e va spiegata.
- **Cancellare in base alla sola esistenza delle copie**: Tusk non distingue file "usati" da file "non usati", sa solo dove stanno le copie. Il nostro vero valore è decidere **cosa** si può togliere (scarti XMP, doppioni, anteprime e cache rigenerabili, proxy) e mostrare quanto spazio si libera prima di farlo.

## 8. Fonti (link)

- Sito ufficiale e FAQ: https://tuskbackup.com
- Fondatore: https://tuskbackup.com/about
- Documentazione: https://tuskbackup.com/docs
  - Primo avvio: https://tuskbackup.com/docs/getting-started
  - Dischi esterni e SD: https://tuskbackup.com/docs/integrations/external-drives
  - Google Drive: https://tuskbackup.com/docs/integrations/google-drive
  - S3: https://tuskbackup.com/docs/integrations/s3
  - Scelta delle destinazioni: https://tuskbackup.com/docs/integrations/choosing-destinations
  - Flussi di lavoro: https://tuskbackup.com/docs/workflows
  - Problemi comuni: https://tuskbackup.com/docs/troubleshooting
  - Glossario degli stati: https://tuskbackup.com/docs/reference/status-glossary
  - Scorciatoie: https://tuskbackup.com/docs/reference/keyboard-shortcuts
  - Dove salva i dati: https://tuskbackup.com/docs/reference/data-locations
  - Scollegare e ricollegare: https://tuskbackup.com/docs/drives/disconnect-reconnect
  - Nomi dei dischi: https://tuskbackup.com/docs/drives/labels-and-rename
  - Offload: https://tuskbackup.com/docs/offload/concept
  - Versioni: https://tuskbackup.com/docs/releases (note: /docs/releases/1.10.0, /1.12.0, /1.12.8)
- Blog (confronto cataloghi): https://tuskbackup.com/blog/best-disk-cataloging-apps-mac
- No Film School: https://nofilmschool.com/tusk-mac-backup-app
- Newsshooter: https://www.newsshooter.com/2026/08/03/tusk-a-mac-app-that-backs-up-project-files-across-drives-the-cloud/
- PetaPixel (non leggibile, 403): https://petapixel.com/2026/08/07/this-new-mac-app-keeps-track-of-your-photo-and-video-backups/
- Product Hunt: https://www.producthunt.com/p/tusk-5/tusk-8149b5ad-8b7e-4c47-abef-179abfc223c7 e https://www.producthunt.com/products/tusk-5/reviews
- AlternativeTo: https://alternativeto.net/software/tusk-backup/about/
