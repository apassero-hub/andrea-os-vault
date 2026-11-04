# RawLine: specifiche

Documento di specifiche da fornire a Claude Code. Obiettivo: una piattaforma completa per fotografi, sul modello di Photo Mechanic ma più completa, semplice ed esteticamente curata. Quattro modalità: Importa, Seleziona, Metadati, Rinomina. Distribuita fuori dall'App Store, Mac per primo.

La modalità Rinomina riusa il motore di [[RawLine Rename]], l'app gratuita per l'App Store. Le sezioni sul nome, le regole, le variabili e la memoria valgono per entrambe le app.

## Principi

- Semplicità prima di tutto: ogni operazione comune deve richiedere pochi clic.
- Anteprima live sempre visibile, con confronto prima/dopo.
- Nessuna perdita di dati: il nome originale non si perde mai.
- Interfaccia nativa Mac, pulita e moderna.
- Gestione completa anche da tastiera.

## Editor del nome: due modalità

### Modalità blocchi

Il nome viene diviso in blocchi usando i separatori (underscore, trattino, spazio, punto, separatori personalizzati). Ogni blocco è una tessera cliccabile su cui si può:

- inserire testo prima o dopo il blocco
- eliminare il blocco senza toccare il resto
- sostituire il blocco
- spostare il blocco (trascinamento)
- bloccare il blocco (lucchetto) per proteggerlo da ogni modifica

Esempio: in un nome con il blocco "yellow" si può inserire il codice colore subito dopo "yellow", mantenendo intatto tutto ciò che segue.

### Modalità caratteri

Il nome viene mostrato come fila di singoli caratteri. Si può selezionare col mouse una zona precisa, anche a metà parola, e:

- modificare un singolo carattere
- cancellare la selezione
- inserire testo in un punto preciso
- sostituire la selezione

## Operazioni di rinomina

### Aggiungere testo

- all'inizio, alla fine
- prima o dopo una parola indicata
- in una posizione numerica precisa

### Eliminare

- un blocco o una parola
- N caratteri da una posizione
- tutto ciò che sta tra due parole indicate
- tutto ciò che sta prima o dopo una parte indicata

### Sostituire

- una parola, una singola lettera
- prima occorrenza, ultima, oppure tutte
- opzione maiuscole/minuscole sensibile o no
- modalità avanzata con espressioni regolari e gruppi di cattura

### Modificare solo una parte

- cambiare tutto ciò che sta prima o dopo una parte protetta, lasciando quella parte invariata

### Contatori

- valore di partenza, passo, numero di zeri iniziali
- contatore che riparte per cartella o per data

### Pulizia

- maiuscole, minuscole, iniziali maiuscole
- rimozione di spazi doppi, accenti, caratteri non validi
- modifica dell'estensione

## Variabili

Un unico sistema di variabili valido sia per i nomi dei file sia per i metadati:

- nome originale, nome attuale, nome cartella
- data e ora di scatto (formati personalizzabili)
- modello fotocamera, obiettivo, numero di serie corpo
- ISO, tempo, diaframma, focale
- campi IPTC (città, località, autore, cliente, evento)
- località ricavata dal GPS
- contatore

## Regole

- Le regole si impilano una sotto l'altra e si applicano in ordine.
- Ogni regola si può attivare o disattivare con un interruttore.
- Regole condizionali: "se la fotocamera è X", "solo per i video", "solo per i RAW" e simili.
- Le combinazioni di regole si salvano come preset riutilizzabili.

## Memoria e cronologia

- Alla prima rinomina il nome originale della fotocamera viene salvato:
  - come attributo esteso nascosto del file (xattr macOS)
  - nel campo IPTC dedicato al riferimento originale (Original Transmission Reference)
  - in un database locale dell'app
- Cronologia completa di tutte le rinomine.
- Annullare l'ultima operazione o tornare a qualsiasi versione precedente.
- Ripristino del nome originale in qualsiasi momento, anche dopo settimane e anche se il file è passato da Lightroom.
- Si può ricostruire il nome partendo sempre dall'originale, senza dover "rinominare il rinominato".

## Metadati e copyright

Ispirato al modello di metadati di Photo Mechanic, ma più semplice e bello.

### Profilo fisso (globale)

- nome, cognome, contatti, sito
- copyright con anno aggiornato automaticamente
- si imposta una volta e vale sempre

### Modelli di lavoro (temporanei)

- uno per cliente o per shooting
- evento, luogo, cliente, didascalia, parole chiave
- si sovrappongono al profilo fisso solo per quella sessione

### Applicazione

- su selezione di file
- automaticamente durante importazione o tramite cartella sorvegliata

## Funzioni da fotografo

- File gemelli: RAW, JPEG e XMP rinominati sempre insieme.
- Più fotocamere: correzione dello scarto orario tra corpi diversi e ordinamento cronologico reale prima della numerazione.
- Località dal GPS: ricavare città o località dalle coordinate.

### Riconoscimento automatico dei corpi macchina

Caso reale: due Sony Alpha 1 identiche, con lo stesso copyright, oggi distinte a mano con i prefissi AP1 e AP2.

- L'app legge il numero di serie del corpo dai metadati EXIF di ogni file.
- Nelle impostazioni si associa una volta sola ogni numero di serie a un tag (es. seriale del primo corpo = AP1, del secondo = AP2).
- Il tag diventa una variabile utilizzabile nei nomi e nei metadati, inserita in automatico in importazione e in rinomina.
- Due file con la stessa numerazione della fotocamera ricevono così nomi diversi.
- Corpo sconosciuto: l'app chiede di assegnargli un tag la prima volta che lo incontra.
- Se due file finiscono comunque con lo stesso nome, interviene l'avviso conflitti prima di applicare.

## Sicurezza

- Avviso conflitti: nomi duplicati, caratteri non validi, nomi troppo lunghi.
- Nessuna modifica applicata senza anteprima.

## Integrazione e automazione

- Azione rapida nel Finder: tasto destro, scelta di un preset, rinomina immediata.
- Cartelle sorvegliate: i file che entrano vengono rinominati e taggati in automatico.
- Scorciatoie da tastiera per tutte le operazioni principali.

## Importazione schede

Modulo di importazione ispirato a Photo Mechanic (Ingest), Lightroom, Capture One, Hedge e ShotPut Pro, ma integrato con rinomina e metadati.

### Avvio e selezione

- Inserendo la scheda si apre la finestra di importazione con le miniature.
- Selezione di tutto, di alcune foto, delle sole stellate in macchina o di un intervallo di date.
- Importazione di più schede insieme, anche da entrambi i corpi.
- Importazione incrementale: l'app ricorda i file già scaricati e copia solo quelli nuovi.
- I RAW restano nel formato originale (nessuna conversione DNG).

### Copie multiple (da 1 a 4)

- Si sceglie quante copie effettuare: 1, 2, 3 o massimo 4.
- Ogni destinazione è una riga con casella di spunta e pulsante per scegliere il disco o la cartella; il tasto "aggiungi copia" aggiunge una destinazione fino a quattro.
- Esempio: copia di lavoro, backup, disco esterno, NAS.
- Tutte le copie vengono scritte in parallelo dalla stessa lettura della scheda.
- Ogni copia è verificata con checksum rispetto all'originale.
- Ogni destinazione può avere una propria struttura di cartelle oppure ereditare quella principale.

### Struttura delle cartelle

- Lo schema delle cartelle si costruisce con le stesse variabili usate per i nomi, componibile a blocchi.
- Variabili per le cartelle: anno, mese (numero o nome), giorno, data completa in vari formati, cliente, evento, tipo di lavoro, luogo, tag corpo macchina (AP1, AP2), tipo di file (foto, video, anteprime), testo libero.
- Separazione opzionale automatica: RAW, video, JPEG di anteprima in sottocartelle diverse.
- Formato consigliato di default: `AAAA/AAAA-MM-GG_Cliente_Evento`, con data in formato internazionale (anno-mese-giorno) perché le cartelle si ordinano da sole in ordine cronologico.
- Schemi pronti selezionabili (per data, per cliente, per anno e cliente) e schemi personalizzati salvabili.
- Anteprima dell'albero di cartelle prima di avviare l'importazione.

### Schema di riferimento e procedura guidata

Schema predefinito scelto: `Anno / AAAA-MM-GG_Cliente_Progetto / [giorno] / Foto | Video / AP1 | AP2 | Audio | Drone`.

Procedura in fase di importazione:

1. L'app legge le date di scatto dalla scheda e propone anno e giorni dello shooting; l'utente conferma o corregge.
2. L'utente inserisce cliente e progetto, con suggerimenti dai clienti già usati per mantenere i nomi sempre identici.
3. Shooting di un giorno: nessuna sottocartella giorno.
4. Shooting di più giorni: la cartella lavoro usa solo la data del primo giorno (es. `2026-10-23_Cliente_Progetto`); dentro, una sottocartella per ogni giorno (es. `2026-10-24`), e ogni file va nel giorno in cui è stato scattato.
5. Dentro ogni giorno: Foto e Video, con AP1, AP2, Audio, Drone.
6. La cartella anno viene creata se non esiste.
7. Importando un'altra scheda dello stesso lavoro, l'app riconosce la cartella esistente e aggiunge solo i giorni o i file nuovi.

### Correzione date

- Avviso automatico se le date sembrano sbagliate: data di default della fotocamera (es. 2000 o anno di fabbrica), date nel futuro, date fuori dall'intervallo dello shooting, scarto tra i due corpi.
- Sovrascrittura manuale: si imposta la data e ora corretta di uno scatto di riferimento e l'app calcola lo scarto da applicare a tutti i file di quel corpo.
- In alternativa: spostamento di ore, minuti o giorni, oppure assegnazione manuale di un giorno a una selezione di file.
- Opzione per scrivere la data corretta anche nei metadati del file, oltre che usarla per cartelle e nomi; la data originale viene conservata nella cronologia.

### Durante la copia

- Applicazione automatica di rinomina, tag corpo macchina, profilo copyright e modello di lavoro.
- Barra di avanzamento generale e per ogni destinazione: file copiati, velocità, tempo stimato, fase in corso (copia, verifica).

### Anteprime JPEG (opzionali)

- Interruttore attivabile o disattivabile.
- Qualità e dimensione selezionabili, con preset (es. anteprima veloce, web, alta).
- Cartella dedicata, pronta da inviare al cliente.

### Fine importazione

- Riepilogo: file copiati, verificati con checksum, eventuali errori.
- Espulsione automatica della scheda solo dopo che tutte le copie sono state verificate, per evitare rimozioni non sicure.
- Notifica di completamento.
- Apertura opzionale della cartella o invio a Lightroom.

### Preset di importazione

- Un preset per tipo di lavoro (es. gara sportiva, prodotto in studio) che salva destinazioni, numero di copie, schema cartelle, rinomina, metadati e anteprime.

## Distribuzione e architettura

- Uso attuale: solo personale.
- Distribuzione sempre fuori dall'App Store, anche in caso di vendita futura.
- Nessuna sandbox App Store: accesso libero a dischi, schede, cartelle ed espulsione dei volumi.
- Firma con Developer ID e notarizzazione Apple predisposte fin dall'inizio, così l'app può essere installata su altri Mac senza blocchi di sicurezza se un giorno verrà venduta.
- Codice organizzato in moduli separati (importazione, selezione, metadati, rinomina, motore metadati) per poter aggiungere in futuro licenze e aggiornamenti automatici senza riscrivere nulla.
- Funzionamento offline per tutto tranne la località da GPS.
- Si sviluppa prima per Mac. In futuro potrebbe arrivare una versione per Windows: la logica (motore di rinomina, regole, variabili, schema cartelle, preset) va tenuta separata dall'interfaccia e dalle funzioni specifiche di macOS, così un domani si può portare senza riscriverla da zero.

## Struttura dell'app: quattro modalità

L'app è divisa in quattro modalità, nell'ordine naturale del lavoro: **Importa, Seleziona, Metadati, Rinomina**.

- All'apertura: schermata semplice con le quattro modalità come grandi pulsanti.
- Avvio intelligente: inserendo una scheda si apre direttamente Importa; trascinando file o cartelle sull'icona si apre Rinomina (o Seleziona, se sono immagini e l'utente lo imposta come preferenza).
- Una volta dentro, un selettore in alto permette di passare da una modalità all'altra senza tornare alla schermata iniziale, mantenendo la stessa selezione di file.
- Le modalità si possono concatenare: a fine importazione si passa direttamente alla selezione delle foto appena scaricate.

## Modalità selezione (culling)

Obiettivo: essere veloce almeno quanto Photo Mechanic e molto più di Lightroom, con un'interfaccia più pulita.

### Velocità

- Nessuno sviluppo del RAW: l'app mostra l'anteprima JPEG incorporata nel file dalla fotocamera (gli ARW della Sony Alpha 1 la contengono a piena risoluzione).
- Precaricamento delle foto successive e precedenti in memoria, per scorrere senza attese.
- Miniature generate in background e conservate in cache.
- Opzione per sviluppare il RAW vero solo su richiesta, per i casi in cui serve un controllo preciso.

### Valutazione

- Stelle da 1 a 5, etichette colore e scarto, assegnabili con tasti numerici e lettere.
- Avanzamento automatico alla foto successiva dopo la valutazione (attivabile o disattivabile).
- Valutazioni applicabili a più foto selezionate insieme.
- Annullamento di ogni valutazione.

### Controllo dettaglio

- Zoom al 100% istantaneo con un tasto o un clic.
- Zoom sincronizzato: lo stesso punto e livello di zoom restano mentre si passa da una foto all'altra, utile per controllare il fuoco nelle raffiche.
- Visualizzazione del punto di messa a fuoco registrato dalla Sony, sovrapposto alla foto.
- Istogramma e dati di scatto essenziali visibili a richiesta.

### Confronto e raffiche

- Confronto di due o più foto affiancate, con zoom sincronizzato.
- Raggruppamento automatico delle raffiche (per intervallo di tempo tra gli scatti), per scegliere la migliore di ogni sequenza.
- Vista per corpo macchina (AP1, AP2) o mista in ordine cronologico reale.

### Filtri

- Mostra solo stelle minime, solo un colore, solo non valutate, solo scartate.
- Filtri per corpo macchina, obiettivo, data.

### Compatibilità

- Valutazioni ed etichette scritte nei file XMP affiancati ai RAW, leggibili subito da Lightroom e Bridge.
- Lettura delle valutazioni già presenti (anche quelle date in macchina).
- Azioni rapide sulla selezione: spostare o copiare le scartate in una cartella, esportare le stellate, passarle alla modalità Metadati o Rinomina.

## Fonti di ispirazione

Finder di macOS, Photo Mechanic, Adobe Bridge, A Better Finder Rename, Transnomino, NameChanger.
