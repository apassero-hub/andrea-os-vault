# Peakto ed Excire: ricerca per RawLine Space

Ricerca dell'11 novembre 2026. Legenda: **[V]** = verificato su una fonte (sito ufficiale, help center, recensione), **[D]** = dedotto o non confermato. Non ho installato né provato nessuna delle due app: tutto viene da fonti scritte.

---

## 1. Peakto (Cyme)

### Cos'è
- [V] Meta-catalogo **solo per Mac** (macOS 12+, ottimizzato per Apple Silicon; su Intel serve una GPU robusta). Non sostituisce i cataloghi: li indicizza dove sono e "non sposta i file".
- [V] Sorgenti dichiarate (45+ app e formati): Lightroom Classic, Lightroom CC, Capture One, Apple Foto, Luminar Neo, DxO PhotoLab, Pixelmator Pro, Photoshop, ON1, Affinity, Nitro, Final Cut Pro, iMovie, Premiere Pro, DaVinci Resolve, cartelle del Finder. Un utente dice di aver letto anche vecchie librerie Aperture.
- [V] Versioni: la 2.0 nel 2024, la 2.3 con anteprime HD per Capture One, la 2.5.5 con culling e doppioni, la **2.7 a marzo 2026** (CP+): Nikon ZR/N-RAW, RED RAW, Blackmagic RAW, Affinity, Nitro e approvazioni di squadra. Il post Cyme di giugno 2026 aggiunge un plugin per Premiere, collaborazione via web e un'interfaccia rifatta.

### Funzioni e impostazioni
- **Ricerca** [V]: ricerca "conversazionale" in linguaggio naturale, con `@persona` e `#luogo` combinabili ("@Lisa che mangia un gelato a #Barcellona"), più "trova simili" e suggerimenti. Si può regolare la tolleranza della ricerca. Funziona anche sul singolo fotogramma di un video.
- **AI** [V]: analisi estetica (un punteggio), parole chiave suggerite, riconoscimento volti in batch con aggiunta manuale dei volti non trovati. Importa i nomi delle persone già messi in Apple Foto e Lightroom.
- **Raggruppamenti** [V]: album automatici per contenuto, timeline, persone, luoghi (tag `#luogo`). [D] Non ho trovato raggruppamenti per "evento" basati sul tempo, come quelli di Apple Foto.
- **Culling e doppioni** [V] (dalla 2.5.5, help center Cyme):
  - si sceglie l'ambito (libreria intera, collezioni, una o più sorgenti) e Peakto dice quante immagini analizzerà;
  - due modelli: *Deduplication* (quasi identiche) e *Culling* (raffiche, varianti, rifacimenti). Uno **slider di somiglianza** va da "stretto" (doppioni) a "largo" (culling);
  - i gruppi diventano cluster. Le foto senza simili spariscono dalla vista;
  - **regole ordinabili e disattivabili** per scegliere la migliore: tipo di file (RAW prima del JPEG), dimensione o risoluzione, voto, qualità del volto, punteggio estetico. Si applicano a mano o in automatico su tutti i cluster;
  - riepilogo per cluster e riepilogo globale, confronto A/B con zoom;
  - azioni di massa su tutte le "tenute" o tutte le "scartate": bandierine, etichette colore, cestino, album;
  - funziona anche con le sorgenti scollegate, ma lo zoom profondo richiede gli originali online.
  - [V] Nella 2.5.5 la funzione andava attivata con un comando da Terminale: segno di una funzione ancora acerba.
- **Sincronizzazione** [V]: le sorgenti si aggiornano in tempo reale o a orari fissi. All'import Peakto analizza prima e mostra il numero di file e il tempo stimato. Si può mettere in pausa e riprendere.
- **Collaborazione** [V]: Peakto Web dal browser, accesso remoto "senza cloud" (server proprio), link per ospiti, progetti, commenti, stati di approvazione (In attesa, Accettato, Rifiutato, Da rivedere). È nel piano Pro.
- **MCP** [V]: c'è un server MCP per comandare Peakto da Claude e strumenti simili (beta).

### Come legge i cataloghi altrui e cosa salva
- [V] Per i cataloghi (Lightroom, Capture One, Foto, Luminar) **usa le anteprime già generate dall'app ospite**, così si vedono le modifiche fatte lì. Se il catalogo non ha generato le anteprime, la miniatura resta vuota. C'è una voce nel menu Sviluppatore, "Analyse Available Previews", per controllarle.
- [V] Per le cartelle sorvegliate genera le anteprime da solo.
- [V] Capture One non salva anteprime su disco. Fino alla 2.3 le foto modificate comparivano come miniature minuscole, poi è arrivato un workaround.
- [V] Recensioni e forum: voti ed etichette messi in Peakto **non tornano a Lightroom**. Gli utenti segnalano anche foto eliminate in Lightroom che restano visibili in Peakto dopo la sincronizzazione.
- [D] Legge i cataloghi in sola lettura (il database SQLite `.lrcat`, le librerie di Foto e così via). Nessuna fonte lo garantisce per iscritto, ma il fatto che i voti non tornino indietro lo fa pensare.
- [D] Salva un database suo e le anteprime per le cartelle. Non ho trovato dati sullo spazio occupato.

### Offline
- [V] Il sito ufficiale (FAQ) dice: "l'AI funziona sul tuo Mac". Fstoppers conferma che la ricerca è locale.
- [V] Una recensione Fstoppers (2023–24) dice che la ricerca **in lingue diverse dall'inglese richiedeva internet**, probabilmente per tradurre. [D] Non so se valga ancora nel 2026.
- [V] Peakto controlla la licenza online. Sul forum Cyme c'è chi deve riattivarla a ogni avvio.
- [V] Si può consultare e cercare su **dischi scollegati** (funzione "Offline Access" dalla 2.2) e scorrere i video da dischi scollegati.

### Gestione file e sicurezza
- [V] "Peakto non elimina mai automaticamente". C'è un **cestino centralizzato** che pulisce i file ovunque si trovino, ma ci finisce solo ciò che l'utente manda esplicitamente. Prima dell'azione si conferma ogni scelta (tenuta o scartata).
- [D] Non ho trovato una funzione per spostare o riorganizzare i file su disco: Peakto guarda e pulisce, non riordina le cartelle.

### Interfaccia
- [V] Griglia principale con album auto-generati, vista singola con metadati, pannelli staccabili (anteprima, EXIF), modalità barra dei menu, "apri in..." verso l'editor preferito.
- [V] Critiche: la GUI confonde chi la usa le prime volte, la ricerca conversazionale è un controllo separato (un clic in più), alcuni pulsanti non hanno tooltip, le ricerche complesse rallentano l'interfaccia. Le foto HDR o RAW non sviluppate compaiono scure.

### Prezzo
- [V] Standard circa $10 al mese, $89 per 12 mesi, $129 per 24 mesi; licenza "a vita" circa $189 con **un solo anno di aggiornamenti**. Pro da circa $25 al mese per utente. Prova di 7 giorni (non per la licenza a vita). Nel Mac App Store compare anche un abbonamento annuo da $59,99. La pagina prezzi ufficiale non mostrava le cifre (caricate via script).

### Limiti e critiche
- [V] Indicizzazione iniziale lenta su librerie grandi: 2,5 GB di cataloghi Lightroom in circa 90 minuti nel 2023, migliorata dalla 1.10. Sul forum ci sono blocchi a 215.965 foto su oltre 400.000, crash al 58% e analisi dei volti congelata dopo la 2.0.1.
- [V] Foto mancanti dopo l'acquisizione da NAS, avvisi ricorrenti di "analisi AI incompleta", librerie di Foto su SSD viste sempre offline (dischi "fantasma").
- [V] La somiglianza non funzionava su un iMac Intel.
- [V] Il prezzo è considerato alto, e la licenza "a vita" include un solo anno di aggiornamenti.
- [D] Dipendere dalle anteprime dell'app ospite è il suo punto debole: se il catalogo non le ha, Peakto non vede.

---

## 2. Excire Foto / Excire Search (Pattern Recognition Company, Lubecca)

### Cos'è
- [V] **Excire Foto**: gestore di foto autonomo per Mac (Apple Silicon e Intel recenti) e Windows. La versione attuale è **Excire Foto 2027** (uscita il 16 giugno 2026, versione 5.0.2 a fine ottobre 2026).
- [V] **Excire Search 2026**: plugin per Lightroom Classic (settembre 2025) con le stesse funzioni AI dentro il catalogo Lightroom: ricerca, culling, doppioni, volti, messa a fuoco.
- [V] Ha vinto il premio TIPA 2026 come "Best Photo Management Software". L'annuncio è del produttore.

### Funzioni e impostazioni
- **AI locale** [V]: parole chiave automatiche in una gerarchia di categorie (animale, cibo, texture...), con la possibilità di **nasconderle**. Dalla 2027 genera parole chiave anche dai **nomi delle cartelle**.
- **Ricerca** [V]: testo libero (oggetti, scene, stati d'animo, attività), filtro per colore dominante (12 colori) con slider per il numero di risultati, ricerca per somiglianza da una foto. Con la 2027 arriva l'**OCR**: cartelli, insegne, numeri di pettorale, menu. L'ambito si sceglie con un ingranaggio: "Vista corrente" o "Catalogo intero".
- **Persone** [V]: "Find People" parte da un volto e trova le altre foto della stessa persona. "Find Faces" filtra per 5 fasce d'età, uno slider maschio/femmina e uno sorriso/non sorriso. La precisione migliora confermando alcune identità.
- **Raggruppamenti** [V]: per persone, scena, sequenza, contenuto e data di scatto. Mappa (2027), timeline e grafico temporale, "Analytics" su attrezzatura e abitudini di scatto.
- **Selezione** [V]: analisi estetica (punteggio da 0 a 100) e di nitidezza, occhi aperti o chiusi, sorriso, focus peaking, griglia dei terzi, Survey/Light Table per confrontare. **I progetti di culling hanno un tetto di 10.000 immagini** (fonte Aiarty).
- **Doppioni** [V]:
  - trova doppioni veri, **versioni diverse dello stesso originale** e foto molto simili o raffiche;
  - **preset** comuni più "Impostazioni avanzate" per decidere quanto deve essere stretta la corrispondenza;
  - ambito: tutto il database oppure il filmstrip corrente;
  - **la ricerca esatta richiede gli originali collegati**, quelle meno precise lavorano sulle anteprime;
  - i risultati si salvano come **collezioni** (una per gruppo, con il numero di doppioni accanto);
  - dalla 2024 c'è una finestra con le statistiche dei doppioni e le bandierine, e si possono **escludere le sequenze** di scatto dalla ricerca;
  - Excire **propone, non decide**: l'utente rivede e mette le bandierine. [D] Non ho trovato regole automatiche per "tenere la migliore" come quelle di Peakto.
- **Metadati** [V]: parole chiave, stelle, colori, bandierine, IPTC, GPS. Restano nel database finché non si lancia **"Store Metadata"**, che scrive i sidecar XMP per i RAW e incorpora i metadati in JPEG e TIFF. Gli XMP vengono letti da Lightroom, Capture One, Luminar e ON1.
- **Condivisione** [V]: Dropbox, Google Drive, OneDrive, Nextcloud ed esportazione video. Sono funzioni di rete, ma facoltative.

### Come legge i cataloghi altrui e cosa salva
- [V] Excire Foto **non legge i cataloghi altrui**: lavora per cartelle e XMP. Non legge le librerie di Apple Foto (bisogna prima esportare in cartelle). Per Lightroom c'è il plugin Excire Search, che lavora dentro il catalogo.
- [V] Salva un **database locale suo, in una cartella separata**, con le anteprime. Le anteprime sono **sempre 1280×720** (Quickstart 2027). Una pagina Excire stima circa **25 GB per 100.000 foto** con le anteprime di massima qualità.
- [V] Il database vive su un solo computer: niente database condiviso, ogni Mac ha il suo. Disinstallando si cancellano database e anteprime, mai gli originali.
- [V] Non riscansiona di continuo: resta fermo finché non si sincronizza esplicitamente.

### Offline
- [V] "Tutto gira in locale", nessuna foto viene caricata. Lo dicono il sito ufficiale e più recensioni. Licenza perpetua.
- [V] **Dischi scollegati**: dopo l'analisi si naviga e si cerca sulle anteprime anche con il disco staccato. Ricollegandolo, tutto si riaggancia da solo (recensione Aiarty e forum FredMiranda). [D] Il manuale non descrive come avviene il riaggancio (UUID del volume? percorso?).
- [D] L'attivazione della licenza richiede la rete almeno una volta (su Trustpilot c'è chi segnala problemi di attivazione).

### Gestione file e sicurezza
- [V] Non sposta, non copia e non rinomina gli originali: crea riferimenti e anteprime. Togliere una foto dal database non tocca il disco. **Eliminare dal disco è un'azione separata con conferma esplicita.**
- [D] Non ho trovato funzioni per spostare o riorganizzare le cartelle, né un cestino interno con annullamento.

### Interfaccia
- [V] Albero delle parole chiave a destra, menu di ordinamento in alto, stelle, colori e bandierine in basso, punteggio estetico nel pannello destro. Schermata di benvenuto. Dalla 2027 ci sono la barra dei filtri AI, il timeline graph, i pannelli regolabili e la ricerca rapida di cartelle e collezioni.
- [V] Critiche: interfaccia "non bella" (2022), menu più lenti delle scorciatoie, l'ambito della ricerca va impostato a mano, gerarchie di parole chiave scomode da gestire (forum DxO), alcuni bug (Macwelt: "buono ma non senza errori").

### Prezzo
- [V] Excire Foto 2027: **$249 / €229** di listino ($219 / €199 al lancio). Aggiornamento a $79 dalla 2025 e $99 dalla 2024. Prova di 14 giorni. Licenza perpetua, senza abbonamento. Excire Search costa a parte ed è considerato caro per un plugin (Digital Camera World).

### Limiti e critiche
- [V] **Analisi lenta**: 3.541 foto in 1 h 9 min (Expert Photography), circa 30 min per 1.900 foto (recensione 2025), circa 1 h ogni 10.000 foto con il plugin (SLR Lounge). Le librerie a sei cifre vanno lasciate girare di notte. Un utente con 1,3 milioni di foto dice: "lento, ma funziona". In compenso, con oltre 650.000 foto la navigazione resta rapida (DIYPhotography).
- [V] Qualche parola chiave sbagliata, risultati non sempre precisi, la ricerca a volte perde foto.
- [V] Niente modifica delle foto, niente database condiviso, il culling ha un tetto di 10.000 foto. I progetti di culling richiedono un doppio import (2025).
- [D] Le anteprime fisse a 1280×720 non bastano per giudicare la nitidezza a schermo pieno su un display 5K quando il disco è scollegato.

---

## 3. Idee da prendere per RawLine Space (tutte offline)

1. **Indice che sopravvive al disco scollegato** (Excire e Peakto): miniature e anteprime nel database, ricerca e navigazione con il disco staccato e riaggancio automatico al ricollegamento. In più, legare i volumi all'**UUID del volume** (e non al nome o al punto di montaggio) ed evitare i "dischi fantasma" che affliggono Peakto.
2. **Anteprime a due livelli con budget dichiarato**: una miniatura piccola sempre presente e un'anteprima media (circa 1280–2048 px) opzionale per ogni volume. All'utente si mostra la stima dello spazio prima di iniziare (Excire: ~25 GB ogni 100.000 foto). Per 40–100 TB serve un'impostazione "solo miniature" per i dischi d'archivio.
3. **Prima analizzare, poi importare** (Peakto): mostrare numero di file, dimensione e tempo stimato prima di partire, con **pausa e ripresa** e la possibilità di farlo girare di notte. Dopo un crash o un riavvio il lavoro riprende dal punto esatto, senza ripartire da zero (i blocchi a 215.000 su 400.000 sono il problema numero uno di Peakto).
4. **Doppioni a livelli separati**: (a) identici, cioè stessa impronta del contenuto, con un hash veloce e poi uno completo; (b) "stesso scatto in altra forma" (RAW+JPEG, export, TIFF dal RAW, ritagli), riconosciuto da EXIF, data di scatto, numero di serie e contatore scatti; (c) quasi doppioni visivi con Vision (`VNGenerateImageFeaturePrintRequest`) e uno **slider di somiglianza**. Come Excire, si possono escludere le raffiche dai doppioni.
5. **Regole ordinabili per "quale tenere"** (Peakto): RAW prima del JPEG, risoluzione più alta, voto più alto, file con XMP o modifiche, il file sul disco "principale" rispetto alla copia di backup, il percorso più vecchio o più nuovo. Le regole si possono attivare, disattivare e trascinare in ordine, e vanno in automatico su tutti i gruppi ma restano modificabili gruppo per gruppo.
6. **Riepilogo dello spazio recuperabile**, per gruppo e globale ("liberi 3,2 TB"), con confronto A/B e zoom. Lo zoom profondo c'è solo con il disco collegato, e va detto chiaramente.
7. **Risultati come collezioni salvate** (Excire): ogni ricerca di doppioni diventa una collezione rivedibile più tardi, anche a disco scollegato. Le azioni distruttive si eseguono solo a disco collegato.
8. **Metadati prima nel database, poi su disco con un comando esplicito** (lo "Store Metadata" di Excire): scrittura degli XMP compatibili con Lightroom e Capture One, in un lotto e con anteprima delle modifiche.
9. **Lettura dei cataloghi Lightroom in sola lettura**: aprire `.lrcat` in SQLite in modalità read-only, su una copia se Lightroom è aperto, per importare voti, parole chiave, collezioni e volti senza mai scriverci. Si recupera anche l'anteprima dal `Previews.lrdata`. [D] È fattibile, ma va verificato sui formati 2025–2026.
10. **Ricerca per testo nelle foto** (OCR di Excire 2027) con `VNRecognizeTextRequest`, utile per pettorali, cartelli e insegne. **Volti** con Vision in locale e conferma umana, **mappa** e **timeline** da EXIF GPS e data, senza geocodifica online. Per i nomi dei luoghi serve un database di località offline incluso nell'app.
11. **Parole chiave dai nomi delle cartelle** (Excire 2027): idea economica e utilissima per archivi già ordinati per cliente o località.
12. **Ricerca in italiano senza rete**: evitare il difetto di Peakto (le lingue non inglesi richiedevano internet). Usare un modello di embedding testo-immagine multilingue in Core ML, oppure un dizionario locale dei sinonimi italiano→inglese.
13. **Statistiche dell'archivio** (le Analytics di Excire): spazio per anno, fotocamera, obiettivo e disco. È ciò che serve per decidere cosa alleggerire.

## 4. Cose da NON copiare

- **Dipendere dalle anteprime dell'app ospite** (Peakto): se Lightroom o Capture One non le ha generate, la foto resta vuota. RawLine Space deve saper decodificare i RAW da sé (ImageIO e Core Image), restando leggera come Selects.
- **Licenza che chiede la rete a ogni avvio** (forum Peakto) o attivazione fragile (Excire). Serve un'attivazione una tantum con un lungo periodo di grazia offline.
- **Ricerca non inglese che richiede internet** (Peakto), cloud sharing e server MCP che spingono verso servizi esterni. Sono fuori dalla regola del 100% offline.
- **Sincronizzazione a senso unico ambigua** (Peakto): voti che non tornano a Lightroom e foto eliminate che restano visibili. Bisogna dire chiaramente cosa viene scritto dove, e mostrare quando i dati sono "vecchi".
- **Funzioni importanti nascoste** (il culling di Peakto 2.5.5 si attivava dal Terminale, la ricerca conversazionale era in un controllo separato). Serve una sola barra di ricerca.
- **Tetti rigidi** come i 10.000 foto per progetto di culling di Excire: su 40–100 TB non hanno senso.
- **Analisi lunghissime senza priorità**: meglio indicizzare prima i metadati e le miniature di tutto l'archivio (pochi minuti per disco) e lasciare l'AI dopo, in background, a bassa priorità.
- **Anteprime di dimensione fissa** non configurabili (1280×720 per Excire).
- **Licenza "a vita" con un solo anno di aggiornamenti** (Peakto), percepita come poco onesta.
- **Eliminare senza un cestino interno ripristinabile**: RawLine Space deve spostare nel Cestino di macOS (o in una cartella "Da eliminare" sullo stesso volume), tenere un registro delle operazioni con annullamento e non cancellare mai l'ultima copia rimasta di un file.

## 5. Fonti (link)

**Peakto**
- https://cyme.io/en/peakto/ (FAQ: AI sul Mac, dischi scollegati, cestino centralizzato)
- https://cyme.io/en/pricing/
- https://cyme.io/en/products/peakto/features/find-duplicate-photos/
- https://desk.cyme.io/portal/en/kb/articles/culling-deduplication
- https://desk.cyme.io/portal/en/kb/articles/how-to-enable-culling-deduplication-in-peakto-2-5-5
- https://desk.cyme.io/portal/en/kb/articles/troubleshooting-blank-thumbnails
- https://cyme.io/en/blog/twelve-months-of-turning-ideas-into-a-better-peakto/ (giugno 2026)
- https://cyme.io/en/blog/smarter-search-bar-in-peakto-2-3/
- https://www.provideocoalition.com/peakto-2-7-adds-support-for-nikon-zr-and-red-raw-formats/ (marzo 2026)
- https://fstoppers.com/software/peakto-version-20-gets-smarter-more-useful-and-searches-video-671464
- https://fstoppers.com/reviews/peakto-mac-adds-incredibly-powerful-conversational-search-its-photo-cataloger-637402
- https://fstoppers.com/reviews/peakto-review-hub-all-your-images-and-catalogs-628058
- https://petapixel.com/2025/03/18/ai-powered-peakto-app-lets-you-find-the-perfect-image-from-anywhere
- https://shotkit.com/peakto-review/
- https://www.thephoblographer.com/2023/04/16/still-a-long-way-from-being-great-peakto-review/ (citata da altri, non letta per intero)
- https://desk.cyme.io/portal/en/community/all-about-peakto-and-avalanche (forum: problemi degli utenti)
- https://apps.apple.com/us/app/peakto/id1633496874

**Excire**
- https://excire.com/en/excire-foto/
- https://excire.com/en/excire-foto-2027-is-here/
- https://excire.com/manuals/Excire-Foto-2027-Quickstart-(EN).pdf (anteprime 1280×720, citato nei risultati di ricerca)
- https://www.photoworkout.com/?p=222334 (lancio 2027, prezzi)
- https://petapixel.com/2026/06/19/excire-foto-2027-promises-a-feature-rich-and-powerful-photo-management-experience/
- https://www.photographynews.co.uk/news/prc-launch-excire-foto-2027/
- https://amateurphotographer.com/review/excire-foto-2027-review-get-on-top-of-even-the-most-disorganised-photo-collection/
- https://www.diyphotography.net/my-photo-library-was-chaos-a-hands-on-review-of-excire-search-2026-and-excire-foto-2025/ (testo non leggibile per intero, uso solo il dato delle 650.000 foto)
- https://expertphotography.com/excire-foto-review
- https://www.aiarty.com/knowledge-base/excire-foto-review-dam.htm (dischi scollegati, eliminazione, XMP, tetto di 10.000; sito di parte)
- https://digitalcameraworld.com/photography/photo-editing/excire-search-2026-review-ai-powered-image-searching-in-lightroom-classic
- https://petapixel.com/2025/09/17/ai-powered-excire-search-2026-aims-to-redefine-lightroom-workflows
- https://www.sonyalpharumors.com/major-excire-foto-2024-update/ (statistiche dei doppioni, esclusione delle sequenze)
- https://www.fredmiranda.com/forum/topic/1934194/ e https://www.fredmiranda.com/forum/topic/1937544/ (utenti con librerie grandi)
- https://forum.dxo.com/t/dam-take-a-look-at-excire-foto/13356/9
- https://www.macwelt.de/article/2244256/excire-foto-test.html
- https://trustpilot.com/review/www.excire.com
