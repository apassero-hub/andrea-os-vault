# Diem (Sam Kolder): ricerca per RawLine Space

Ricerca dell'11 novembre 2026. Legenda: **[V]** = verificato su una fonte (vedi sezione 8) · **[D]** = mia deduzione, non confermata.

Nota sull'identità: esistono molte app chiamate "Diem": un social/search per donne (askdiem.com), un diario fotografico iOS (Gootra), una to-do list, un'app wellness e la criptovaluta Diem/Libra. Quella di Sam Kolder è **Diem di Diem Data Management Inc.** (Cheyenne, Wyoming), sito **downloaddiem.com** [V].

---

## 1. Cos'è

Diem è un'app desktop (macOS e Windows) per gestire i media: indicizza hard disk esterni e cloud e ne tiene un catalogo locale. Così si possono sfogliare e cercare foto e video anche a disco staccato [V]. Aggiunge una ricerca con AI (oggetti, atmosfere, volti, parlato, somiglianza visiva) e una funzione "Gather" che raccoglie i file scelti da più dischi e li copia in un'unica destinazione [V]. È in **beta gratuita**, con piani a pagamento già pubblicati [V].

Il team [V]: Sam Kolder (filmmaker, il problema nasce dal suo archivio e dal corso Kolder Creative); Kai (cofondatore di Kolder Creative, usabilità e design); Elliot Napier (prodotto e strategia); Adrian (architettura tecnica, fondatore di **Gyroflow**). Branding e UI sono dell'agenzia Jaro Design (caso studio di giugno 2023, "poised for launch") [V]. Termini e privacy sono aggiornati al 6 gennaio 2026 [V].

## 2. Funzioni e impostazioni nel dettaglio

### Indicizzazione ("Sync")
- Si collega ogni disco o account cloud **una volta**. Diem salva sul computer una copia locale dei metadati dei file, della struttura delle cartelle e, a scelta, delle anteprime [V].
- **Tre livelli di sync**, con tempi stimati da loro per un disco da 4 TB [V]:
  - **Metadata sync**, circa 20 min (solo nomi, percorsi, dati tecnici [D]);
  - **Light sync**, circa 50 min (probabilmente con miniature [D]);
  - **Deep sync**, circa 2 h (probabilmente analisi AI, trascrizioni e volti [D]).
- In roadmap ci sono la "index size estimation" (stima di quanto occuperà l'indice), "folders for drives" (raggruppare i dischi), "custom notes for drives" (note per disco) [V].
- Nel piano Free si sincronizzano **al massimo 3 dischi**, nei piani a pagamento senza limite [V]. Non sono indicati limiti in TB [V].

### Ricerca
- **AI search**: per oggetti, mood e concetti [V]. Nel Free è limitata a 10 risultati per ricerca [V].
- **Trascrizione**: il parlato di audio e video diventa testo ricercabile. Non è nel Free [V].
- **Visual search**: trova clip e foto visivamente simili, senza conoscere il nome del file [V].
- **Faces / People**: rileva e raggruppa i volti, e si possono dare nomi alle persone. Nel Free fino a 5 volti [V].
- **Places**: i file su una mappa del mondo tramite il GPS. È in roadmap la "manual file GPS location", cioè assegnare la posizione a mano [V].
- **Saved Searches / smart bins**: ricerche salvate che si aggiornano da sole quando arriva materiale nuovo che corrisponde [V].

### Organizzazione
- **Album**: raccolte di file per progetto, che possono stare su dischi diversi [V].
- **Tag personalizzati**: validi su tutti i dischi e i cloud [V]. È annunciato un "improved file tagging" [V].
- **Metadata viewer**: codec, pixel format, bitrate, frame rate, dati della camera, timecode, GPS [V].
- In roadmap: "custom metadata fields", "scene detection", **"find duplicate files"** [V].

### Media browser
- Riproduce subito molti formati, compresi RAW video (R3D, BRAW) e foto RAW, in tempo reale [V]. Nel Free i "RAW codecs" non ci sono [V].
- **Stabilizzazione con Gyroflow** dentro l'app [V].
- **LUT di anteprima** per il materiale log, che non modifica i file [V].
- I file sul cloud si vedono e si riproducono senza scaricarli [V].
- **Generazione di proxy** (nel piano Creator; altrove indicata come roadmap) [V].

### Gather (raccolta e trasferimento)
- Si crea un album, si "raccolgono" i media e si copiano in una destinazione qualsiasi. Diem **dice quali dischi collegare** e poi raccoglie i file [V].
- Non è documentato se la copia venga verificata (checksum), come gestisca i conflitti di nome o le interruzioni [V: non trattato].

### Collaborazione (piani alti, in gran parte roadmap)
- Trasferimenti P2P, condivisione di file Diem (anche con chi non usa Diem), accesso da più dispositivi, cloud storage come add-on, "smart storage" ("coming soon") [V].
- Plugin per Resolve e Premiere, versione Linux, app mobile, traduzioni: tutti in roadmap [V].

### Impostazioni
- Non ho trovato una documentazione pubblica delle impostazioni, né manuale o changelog [V: non trovati]. Le uniche scelte documentate sono il livello di sync per disco, l'attivazione delle funzioni AI (opzionali e da accendere a mano, secondo la privacy) e le anteprime opzionali [V].

## 3. Interfaccia e flusso

Flusso dichiarato in tre passi [V]:
1. **Sync once**: si collega il disco, si sceglie il livello di sync e si aspetta l'indicizzazione.
2. **Search**: una barra di ricerca unica su tutti i dischi, anche staccati.
3. **Gather & transfer**: si mettono i file in un album, Diem chiede di collegare i dischi giusti e copia tutto nella destinazione.

Elementi visibili dell'interfaccia (dalle immagini del sito, senza didascalie) [V]: barra di ricerca AI in alto, viste **People** e **Places** (mappa del mondo), un media browser con anteprime e lettore, e una lista dei dischi o delle sorgenti. Jaro Design ha prodotto design system, prototipi UX, UI ad alta fedeltà e un prototipo Figma, ma non descrive le singole schermate [V].

Di mia deduzione [D]: la struttura tipica è barra laterale con dischi, cloud, album e ricerche salvate; griglia centrale di miniature; pannello dei metadati. Ogni elemento mostrerà probabilmente lo stato del disco (collegato o no). Gesti e scorciatoie da tastiera non sono documentati.

## 4. Sicurezza dei file (anteprima, annulla, verifica)

È il punto più debole dal punto di vista documentale:
- Diem si presenta come un catalogo che **legge** i file e li **copia** (Gather). Non ho trovato funzioni documentate di spostamento, rinomina o eliminazione dei file originali [V: non trattato]. È quindi probabile che sia in gran parte di sola lettura [D].
- La LUT di anteprima è esplicitamente non distruttiva [V].
- **Non è documentato** niente su anteprima delle operazioni, annulla, registro, verifica delle copie con checksum o gestione degli errori di trasferimento [V: non trattato].
- Termini [V]: il servizio è fornito "as is"; la responsabilità è limitata a 100 USD o a quanto pagato negli ultimi 12 mesi; dichiarano "We do not host or back up your files"; le funzioni beta "may be unstable" e si usano a proprio rischio.
- Privacy [V]: i contenuti dei file sono elaborati in locale "by default" e i file non vengono caricati di default. Però le **funzioni AI opzionali possono mandare input e output a un fornitore AI, "which may include OpenAI"**. Inoltre raccolgono nomi file, percorsi, tipi, date, dimensioni ed "embeddings" come dati derivati, IP, dati del dispositivo, crash report e uso anonimo; serve un account (registrazione, social login); i pagamenti passano da Stripe.

## 5. Prezzo, piattaforme, limiti, critiche

**Piattaforme** [V]: macOS (DMG) e Windows 64 bit (ZIP). Linux e mobile sono in roadmap. Non ci sono requisiti di sistema pubblicati.

**Prezzi** (pagina Pricing) [V]:

| Piano | Mensile | Annuale | Contenuto principale |
|---|---|---|---|
| Free | 0 $ | — | 3 dischi, AI search con 10 risultati, Places, 5 volti, cloud. Senza trascrizione, codec RAW, Gather, plugin |
| Creator | 12 $ | 9 $/mese (108 $/anno) | dischi illimitati, AI illimitata, Faces, Places, Gather, proxy |
| Collaborator | 29 $ | 23 $/mese (276 $/anno) | in più P2P, condivisione, multi-dispositivo; cloud a pagamento a parte |
| Teams | 49 $ | 40 $/mese (480 $/anno) | 2 posti, +10 $/mese per utente (8 $/mese annuale) |

C'è una prova gratuita del Creator, di durata non indicata [V]. Download beta gratis previa email [V].

**Limiti** [V, salvo dove indicato]:
- È ancora beta: dichiarata potenzialmente instabile.
- Duplicati, note sui dischi, campi metadati personalizzati e plugin per gli editor non ci sono ancora (roadmap).
- Ci sono account, abbonamento e telemetria. L'AI può passare da un cloud esterno, quindi **non è garantito il 100% offline** per le funzioni AI. Se le funzioni base funzionino offline non è dichiarato [V: non trattato]. Secondo me richiede almeno login e verifica dell'abbonamento [D].
- Il Free blocca funzioni proprio sul RAW (codec RAW esclusi).
- Diem non scrive XMP né sidecar: tag, album e volti restano dentro Diem [D, nessuna menzione di XMP o esportazione dei tag].
- Le stime di sync sono per 4 TB. Per 40–100 TB si arriverebbe, in proporzione, a 3,5–8 h solo di metadata e 20–50 h di deep sync [D, calcolo lineare].

**Critiche degli utenti**: non ho trovato recensioni indipendenti, thread Reddit, articoli o video di prova. Tutte le informazioni vengono dal sito di Diem e dall'agenzia di design [V]. Il progetto sembra in sviluppo da almeno metà 2023 e ancora in beta nel 2026 [D, dalle date delle fonti].

## 6. Idee da prendere per RawLine Space (concrete)

1. **Catalogo dei dischi staccati**: ogni volume ha un'identità stabile (UUID del volume più un nome dato dall'utente). L'archivio si sfoglia e si cerca anche a disco scollegato, con lo stato "collegato / non collegato" sempre visibile.
2. **Livelli di scansione per disco**: Rapida (solo file system, dimensioni e date), Standard (più EXIF/XMP e miniature piccole), Profonda (più hash per i duplicati, anteprime più grandi, analisi locali). Prima di partire si mostra una **stima del tempo e dello spazio dell'indice**, visto che loro la mettono in roadmap: da noi dovrebbe esserci dal primo giorno.
3. **"Collega il disco X"**: quando un'operazione (raccolta, verifica, pulizia) tocca file su dischi staccati, l'app elenca i dischi da collegare, in quale ordine e quanti dati servono da ognuno, e riprende da sola quando il disco viene montato.
4. **Album trasversali e ricerche salvate dinamiche**: per esempio "RAW senza XMP", "export più vecchi di 2 anni", "video del cliente X". Si aggiornano a ogni nuova scansione e sono il punto di partenza per alleggerire l'archivio.
5. **Note e cartelle per i dischi**: dove sta fisicamente il disco, di che anno è, se è un backup di quale altro. Loro le hanno in roadmap; per un archivio di 40–100 TB su decine di dischi sono essenziali.
6. **Vista mappa e ricerca per luogo** dal GPS dei RAW, con assegnazione manuale della posizione a intere cartelle (servizio o viaggio). Va fatta con mappe offline o con un fondo semplice senza tile online.
7. **Metadata viewer completo** per foto e video (codec, bitrate, timecode, camera, GPS) e **LUT di anteprima non distruttiva** per i video log dei clienti.
8. **Ricerca visiva e per volti in locale** (Vision / Core ML sul Mac), come alternativa offline alle loro funzioni AI cloud.
9. **Proxy e miniature dentro il catalogo**, così il catalogo resta utile anche quando il disco originale è in un cassetto.

## 7. Cose da NON copiare

- **Nessuna AI in cloud e nessun invio di embeddings o percorsi a server**: Diem dichiara un possibile invio a OpenAI e la raccolta di nomi file e percorsi. RawLine Space deve fare tutto in locale, senza account obbligatorio.
- **Nessun limite che blocca il RAW** o il numero di dischi in una versione di prova: per un archivio professionale è proprio il caso d'uso principale.
- **Nessun dato chiuso nel database dell'app**: tag e classificazioni vanno scritti anche in XMP o esportati in formati aperti, così il catalogo non diventa una prigione.
- **Nessuna copia senza garanzie**: Diem non documenta né verifica né registro. RawLine Space deve fare copie con checksum, scrittura in temporaneo e poi rinomina, registro delle operazioni, ripresa dopo interruzione e nessuna sovrascrittura silenziosa.
- **Niente promesse in roadmap come argomento di vendita** (duplicati, plugin, sharing): meglio poche funzioni solide.
- **Niente funzioni social o di collaborazione** (P2P, condivisione, multi-dispositivo): sono fuori dallo scopo e richiedono la rete.
- **Niente tempi di sync tarati su 4 TB**: bisogna progettare e testare per 40–100 TB, con scansione incrementale, pausa e ripresa.

## 8. Fonti (link)

- Sito ufficiale, home con funzioni, FAQ e download: https://www.downloaddiem.com/
- Mirror o variante del sito: https://code.downloaddiem.com/
- About (team, storia): https://www.downloaddiem.com/about
- Pricing e roadmap: https://www.downloaddiem.com/pricing
- Termini (6 gennaio 2026): https://www.downloaddiem.com/terms
- Privacy (6 gennaio 2026): https://www.downloaddiem.com/privacy
- Caso studio di Jaro Design (giugno 2023): https://www.jaro.design/works/diem-app
- Profilo che cita Diem tra le attività di Sam Kolder: https://creatordb.app/creatorstats/samkolder/
- App omonime da non confondere: https://www.askdiem.com/ · https://apps.apple.com/us/app/-/id1511065007
