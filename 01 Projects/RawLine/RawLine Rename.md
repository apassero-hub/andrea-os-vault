# RawLine Rename: specifiche

App gratuita per macOS, distribuita sull'App Store. È un rinominatore di file: nome, regole, variabili, memoria del nome originale. È anche il banco di prova del motore di rinomina che RawLine (l'app completa, vedi [[RawLine]]) riuserà così com'è.

Codice e documento di progetto: `~/Developer/Rawline` (`docs/2026-10-23-rawline-rename-design.md`).

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

## Fuori ambito per RawLine Rename

Queste funzioni appartengono solo a [[RawLine]]:

- importazione schede
- selezione (culling)
- profilo copyright e modelli di lavoro dei metadati
- cartelle sorvegliate

Rimandate a dopo la prima versione: correzione dello scarto orario tra corpi, località dal GPS, azione rapida nel Finder.

## Distribuzione

- Mac App Store, gratuita, nessun acquisto interno.
- Sandbox attiva: l'app tocca solo i file e le cartelle scelti dall'utente, e ricorda i permessi tra un avvio e l'altro.
- Tutto offline, nessun programma esterno: i metadati si leggono con i framework Apple.
- Il motore resta indipendente dalla sandbox e dall'interfaccia, così RawLine lo può riusare.

## Fonti di ispirazione

Finder di macOS, Photo Mechanic, A Better Finder Rename, Transnomino, NameChanger.
