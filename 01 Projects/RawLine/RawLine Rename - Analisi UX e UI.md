---
progetto: RawLine Rename
tipo: analisi
data: 2026-11-04
versione analizzata: 1.0 beta 1.2
---

# RawLine Rename: analisi UX e UI del renaming

Complemento di [[RawLine Rename - Analisi competitor]]. Qui si guarda solo **come si usa** la rinomina: cosa si vede, quanti passi servono, dove ci si inceppa. Le funzioni del motore sono nell'altra nota.

## Verdetto in breve

Il motore e la sicurezza sono già al livello dei migliori: anteprima viva, gemelli automatici, ripristino dei nomi originali, passo per passo. Su questi punti RawLine è sopra NameChanger, Renamer 7 e Transnomino, e alla pari con A Better Finder Rename. **L'interfaccia invece non è ancora al top.** Ci sono tre problemi che un fotografo nota al primo uso:

1. **Troppo spazio prima dell'elenco.** Sopra i file ci sono sei fasce: intestazione, Nuovo nome, Correzioni, riga delle opzioni, barra delle spunte, intestazione delle colonne. Con 6 file di prova l'elenco comincia a metà finestra. Con un blueprint da 6 pezzi (6 righe più 5 separatori) l'elenco scende ancora (stima dal codice, da verificare a schermo).
2. **Gli errori non si risolvono da dove si vedono.** Un nome con la sola data dà "Stesso nome di un altro file del lotto" su ogni riga, ma nessun pulsante lo risolve. La soluzione ("Aggiungi -2, -3", oppure aggiungere il contatore) sta altrove.
3. **L'evidenziazione delle differenze fa rumore** quando il nome cambia del tutto (vedi sotto).

Tutti e tre si sistemano senza toccare il motore: sono da **beta 1.3**.

## Come l'ho analizzata

- Lettura di tutte le viste dell'app (finestra, Nuovo nome, Correzioni, elenco, pannello del file, barra in basso, menu, impostazioni).
- App aperta su una cartella di prova con 6 RAW dell'Alpha 1 (copie da "Aosta Valley Freeride"), con le regole dell'ultima sessione. Screenshot dello stato reale.
- Ricerca sul flusso di rinomina di A Better Finder Rename 12, Advanced Renamer 4, NameChanger, Renamer 7, Transnomino, Photo Mechanic (rinomina all'ingest), Lightroom Classic (Filename Template Editor), Finder di macOS.

## Cosa è già al top (da non toccare)

| Punto | Perché è forte | Chi fa peggio |
|---|---|---|
| **Pezzi del nome con il valore del primo file accanto** ("Data di scatto → 2026-10-22") | Si capisce cosa produce ogni pezzo senza leggere sintassi | Lightroom mostra un solo esempio in fondo al dialogo; Advanced Renamer e Bulk Rename mostrano solo `<tag>` |
| **Gemelli RAW+JPEG+XMP insieme, da soli** | Nessuna configurazione | ABFR lo fa ma va acceso nelle opzioni avanzate; NameChanger e Transnomino no |
| **Un solo pulsante d'azione che cambia significato** ("Rinomina 6 file" / "Mostra il primo errore" / "Spunta qualche file") | Non si può sbagliare | Advanced Renamer: "Start batch" sempre uguale, errori in un elenco a parte |
| **Ripristino dei nomi precedenti e originali, storia** | Ci si fida a rinominare | La maggior parte ha solo l'annulla dell'ultima operazione |
| **Passo per passo nel pannello del file** | Spiega perché un nome è venuto così | Nessun concorrente Mac lo ha così chiaro |
| **Corpi macchina con sigla e orologio** | Pensato per chi scatta con più corpi | Photo Mechanic ci arriva solo con le code replacement da file di testo |
| **Blueprint per settore** | Si parte da un caso reale | Nessuno |

## Problemi visti a schermo (beta 1.2)

**1. Differenze a caratteri quando il nome cambia tutto.** `_AP13929.ARW` → `2026-10-22.ARW`: nel vecchio nome alcune cifre sono barrate e altre no, nel nuovo le cifre sono a strisce alterne. È il confronto carattere per carattere che trova coincidenze casuali (2, 9, 0). NameChanger e ABFR evidenziano solo quando un pezzo resta uguale.
→ Se i due nomi hanno poco in comune (es. meno del 40% uguale), mostrare il vecchio tenue e il nuovo tutto colorato, senza strisce. Evidenziare solo i pezzi interi rimasti (es. `_AP13929` quando c'è `{original}`).

**2. Conflitti senza soluzione a portata.** Sei righe di "Stesso nome di un altro file del lotto", e in basso "6 errori". Nessun pulsante per risolverli.
→ Sopra l'elenco una barra sola: "6 file avrebbero lo stesso nome", con tre pulsanti: **Aggiungi il contatore** / **Aggiungi l'ora con i secondi** / **Aggiungi -2, -3**. ABFR aggiunge da solo "(a) (b)"; Advanced Renamer ha le "collision rule". Noi possiamo fare meglio proponendo la correzione giusta, invece di applicarne una nascosta.

**3. Due date diverse nella stessa riga.** Il menu del formato mostra "2026-10-23" (data campione fissa, 23 ottobre) e a destra il valore vero "2026-10-22". Sembra un errore.
→ Gli esempi nel menu del formato si calcolano dalla data del primo file. Se non ci sono file, si usa la data campione.

**4. Riga Data affollata.** Formato, Notte lunga, regolatore "Il giorno comincia alle 5:00" che va a capo su due righe, valore e ×. Nella build di prova "Long night from an hour" era in inglese: la build di prova era stata compilata prima delle traduzioni. Nella beta 1.2 pubblicata dovrebbe essere in italiano, da controllare.
→ Notte lunga e centesimi in un pulsante "Opzioni ora…" che apre un popover. Nella riga resta solo un'etichetta quando sono accesi ("notte lunga dalle 5:00").

**5. "Tutti i file / Solo spuntati" due volte.** È nell'intestazione e di nuovo, come badge, nella barra delle spunte.
→ Tenerlo solo nella barra delle spunte, dove si agisce sui file.

**6. Riga delle opzioni sparsa.** "Risultato", "Numera in ordine di", "Nomi uguali" e "Vista" stanno in una fascia a parte fra le Correzioni e l'elenco.
→ "Risultato" va dentro la card Nuovo nome, come riga finale grande: è la cosa più importante. "Numera in ordine di" va nelle opzioni del contatore. "Nomi uguali" va nella barra dei conflitti (punto 2). "Vista" va nella barra delle spunte, a destra.

**7. Separatore "_" invisibile quando è selezionato.** Nel controllo segmentato "Fra gli elementi" il trattino basso selezionato non si vede (testo chiaro su azzurro, in basso).
→ Usare etichette "_ trattino basso", come nelle Impostazioni, o un glifo più alto.

**8. Correzioni vuote occupano una card intera.** Titolo, sottotitolo e pulsante anche quando non ce ne sono.
→ Senza correzioni basta una riga "+ Aggiungi correzione" dentro la card del nome. La card si apre solo quando ce n'è almeno una.

## Cosa hanno gli altri che a noi manca

In ordine di valore per chi rinomina una volta all'import.

| # | Funzione | Chi ce l'ha | Valore per noi | Peso |
|---|---|---|---|---|
| 1 | **Nome modificato a mano per un singolo file** (doppio clic sul nuovo nome) | Advanced Renamer, ReNamer, Name Mangler | Alto: lo scatto che fa eccezione (la foto della firma, il ritratto del cliente) senza creare una regola | Medio: il nome a mano deve restare finché non si cambiano le regole, con un segno "modificato a mano" e la possibilità di toglierlo. ReNamer lo perde a ogni anteprima, ed è proprio quello da evitare |
| 2 | **Correzione dei conflitti con un clic** | ABFR (automatica), Advanced Renamer (regole) | Alto, vedi punto 2 sopra | Basso |
| 3 | **Ingest: copia dalla scheda e rinomina in un passo** | Photo Mechanic, Lightroom, Capture One | Altissimo per chi rinomina una volta all'import: oggi bisogna copiare nel Finder e poi aprire RawLine | Alto: è un pezzo di prodotto. Da decidere se va in RawLine Rename o in RawLine completa. Il primo passo può essere la modalità **Copia in…** di Advanced Renamer: rinomina copiando in un'altra cartella, la scheda resta intatta |
| 4 | **Quick Look con la barra spaziatrice** nell'elenco | Finder, Photo Mechanic | Medio: verificare la foto prima di rinominarla, soprattutto nella vista griglia | Basso |
| 5 | **Annulla (⌘Z) sulle modifiche alle regole** | Tutte le app Mac native | Medio: oggi un pezzo tolto per sbaglio va rimesso a mano | Medio |
| 6 | **Rinomina dal Finder** (Azione rapida "Rinomina con RawLine", trascinamento sull'icona nel Dock) | ABFR (estensione Finder e droplet), Transnomino (Automator) | Medio: l'ingresso più naturale su Mac | Basso per il Dock, medio per l'Azione rapida |
| 7 | **Campi da compilare nel preset** (Cliente, Evento) e **scorciatoie di testo** | Photo Mechanic (code replacement: `\gf` diventa "Giulia Ferri") | Alto per chi lavora a eventi: si scrive il cliente una volta, in un campo evidenziato | Medio, è già nell'altra nota come `{ask:…}` |
| 8 | **Riordino a mano dei file per il contatore** (trascinare una riga) | NameChanger | Basso: per noi conta l'ordine di scatto, ma serve per il backstage scattato col telefono senza orologio giusto | Medio |
| 9 | **Contatore che prosegue fra le sessioni** (ultimo numero usato, anche in cartelle diverse) | Photo Mechanic `{seqn}` | Medio per chi numera i lavori (studio): la numerazione Automatica copre la cartella, non lo storico | Basso |
| 10 | **Colonne di dati nell'elenco** (data di scatto, corpo, ISO) | Advanced Renamer | Basso: il pannello del file copre già il bisogno | Basso |

Cose dei concorrenti da **non** copiare:
- La catena di "rinominatori" tutti uguali (Renamer 7, Transnomino, Advanced Renamer). Il nostro "prima il nome, poi le correzioni" è più chiaro per un fotografo.
- I pannelli densi di Bulk Rename Utility.
- La risoluzione dei conflitti silenziosa di ABFR ("(a)", "(b)" aggiunti senza dirlo). Meglio proporla e far scegliere.

## Proposta di disposizione

Obiettivo: **l'elenco dei file occupa almeno il 60% dell'altezza**, e il nome si legge in una riga.

```
┌ Prova UX · 6 file, 22 ottobre 2026                          [Cerca]  ┐
├──────────────────────────────────────────────────────────────────────┤
│ 1 NUOVO NOME                                         [Preset ▾] [⏻]  │
│  [Data ▾] _ [Autore ▾] _ [Sposi] _ [Contatore ▾] _ [Originale] [+]   │  ← gettoni in una riga,
│  20261022_Ferri_Sposi_0001_DSC01234.ARW                              │    opzioni in popover
│  + Aggiungi correzione   (2 correzioni ▸)                            │
├──────────────────────────────────────────────────────────────────────┤
│ ⚠ 6 file avrebbero lo stesso nome  [Aggiungi contatore] [Ora con s]  │  ← solo se serve
├──────────────────────────────────────────────────────────────────────┤
│ ◉ Tutti i file · verranno rinominati 6        Ordine: scatto  ☰ ▦    │
│  ✓ ▣ _AP13929.ARW            → 20261022_Ferri_Sposi_0001_…           │
│  …                                                                   │
├──────────────────────────────────────────────────────────────────────┤
│ 6 da rinominare · 0 uguali              ☑ Mostra nel Finder [Rinomina]│
└──────────────────────────────────────────────────────────────────────┘
```

- **Gettoni in una riga** (come il Filename Template Editor di Lightroom e il TokenField che usiamo già nelle regole). Le opzioni di ogni gettone si aprono al clic in un popover, con il valore del primo file in cima. Le righe di oggi restano come vista "dettaglio" per chi vuole.
- **Risultato grande** sotto i gettoni: è la prova che il nome è giusto.
- **Barra dei conflitti** solo quando serve.
- **Le opzioni del lotto** (ordine, vista) stanno nella barra delle spunte.

## Piano

**Beta 1.3: rifinitura, senza funzioni nuove nel motore.** Fatta il 4 novembre 2026 (commit `45768e5`), tutti i punti 1–7. Il separatore ora si sceglie da un menu con le parole. Ordine e nomi uguali stanno nella barra sopra l'elenco, con le voci che si spiegano da sole ("Numeri per data di scatto", "Nomi uguali: errore"). Verificata a schermo su 6 RAW; Quick Look e il popover Opzioni ora non sono stati provati a mano.
1. Barra dei conflitti con le tre correzioni (punto 2).
2. Differenze: niente strisce quando il nome cambia tutto (punto 1).
3. Esempi dei formati dalla data del primo file (punto 3).
4. Notte lunga e centesimi in un popover "Opzioni ora" (punto 4).
5. Via il doppio selettore Tutti/Solo spuntati; riga delle opzioni dentro la card e nella barra delle spunte; Correzioni compatte quando sono vuote (punti 5, 6, 8).
6. Separatore leggibile (punto 7).
7. Quick Look con lo spazio.

**Beta 2: le funzioni che mancano**
1. Gettoni in una riga con popover (la nuova disposizione).
2. Nome modificato a mano per un file.
3. ⌘Z sulle regole.
4. Campi da compilare nel preset (`{ask:Cliente}`).
5. Azione rapida del Finder e trascinamento sull'icona nel Dock.

**Da decidere: prodotto**
- Ingest dalla scheda (copia + rinomina) in Rename o solo nella RawLine completa. Primo passo possibile: modalità "Copia in…".

## Da verificare a schermo

- Altezza reale della card Nuovo nome con un blueprint da 6 pezzi.
- Traduzione "Notte lunga da un'ora" nella build pubblicata 1.2.
- Vista griglia e pannello del file con molti file (non provati in questa sessione).

## Fonti

- A Better Finder Rename 12: [novità](https://www.publicspace.net/ABetterFinderRename/Version12.html), [risoluzione automatica dei conflitti](https://www.publicspace.net/ABetterFinderRename/v12/AutomaticFileNameResolution.html), [opzioni dei conflitti](https://publicspace.net/ABetterFinderRename/v12/FileNameConflictResolutionOptions.html), [opzioni avanzate](https://publicspace.net/ABetterFinderRename/v12/AdvancedOptions.html)
- Advanced Renamer: [modalità rinomina, copia, sposta](https://advancedrenamer.com/user_guide/batchmode), [uso](https://advancedrenamer.com/user_guide/using_aren), [recensione Softpedia](https://www.softpedia.com/reviews/windows/Advanced-Renamer-Review-457834.shtml)
- ReNamer: [modifica manuale](https://www.den4b.com/docs/books/renamer/page/manual-editing)
- NameChanger: [sito ufficiale](https://www.mrrsoftware.com/namechanger/), [tutorial Hongkiat](https://www.hongkiat.com/blog/rename-multiple-files-mac)
- Renamer 7: [renamer.com](https://renamer.com/), [Setapp](https://setapp.com/apps/renamer)
- Transnomino: [SourceForge](https://sourceforge.net/app/transnomino/mac/), [ifun.de](https://www.ifun.de/transnomino-9-grosses-update-fuer-den-freien-datei-umbenenner-248797/)
- Photo Mechanic: [variabile sequenza](https://docs.camerabits.com/support/solutions/articles/48001205803), [rinomina per numero di serie all'ingest](https://home.camerabits.com/rename-images-based-on-camera-serial-number-during-ingest/), [glossario](https://docs.camerabits.com/support/solutions/articles/48001206190-glossary-of-terms)
- Lightroom Classic: [Filename Template Editor](https://helpx.adobe.com/si/lightroom-classic/help/filename-template-editor-text-template.html), [consigli sulla rinomina](https://digital-photography-school.com/tips-for-file-renaming-success-in-lightroom/)

## Secondo check visivo (4 novembre 2026, prima di pubblicare la 1.3)

Screenshot con il blueprint Matrimoni (6 pezzi) in chiaro e in scuro.

- **Trovato:** con 6 pezzi la card Nuovo nome riempiva tutta la finestra e l'elenco dei file mostrava zero righe. → **Fatto:** i pezzi sono **tessere in fila** che vanno a capo, come i blocchi del sito. Ogni tessera mostra cosa è e il valore del primo file; le opzioni si aprono in un popover al clic, con Sposta a sinistra/destra e Rimuovi; si trascinano per spostarle. Fra due tessere c'è il separatore di quel punto, cliccabile. Con 6 pezzi il nome sta in una riga e si vedono tutti i file.
- **Trovato:** l'app usava un blu acciaio (#1F6F8B) che non c'entra con il logo (verde scuro #0F403B, verde acqua #12C6AA, bianco caldo #F8F7F1) né con il sito (teal #0E9E8A, #0B7A6B per il testo, inchiostro #0B3F38). → **Fatto:** palette del sito in tutta l'app, con contrasti controllati. Il colore d'accento di sistema (selezioni, interruttori, pulsante Rinomina) è teal: #0B7A6B su chiaro (5,2:1 sul bianco), #0E9E8A su scuro. Il verde acqua del logo va solo nei testi piccoli su fondo scuro. Nomi in inchiostro #0B3F38, tessere bianche su chiaro e verde notte su scuro, rosso mattone #A8371F per gli errori come sul sito.
- **Trovato:** il marchio in cima era "RAWLINE / RENAME" in corsivo maiuscolo, diverso dal sito. → **Fatto:** "rawline" minuscolo, largo e pieno, con "rename" in una tessera teal, come sul sito.
- Anche le righe delle Correzioni usano lo stile delle tessere.

Ancora da guardare: icona dell'app e pannello del file con la nuova palette; il font del sito (Unbounded) non è nell'app, il marchio lo imita con SF Pro largo.

## Terzo check: versione grafite (4 nov 2026)

Decisione: app sobria e funzionale, accento grafite; i colori del marchio solo per logo, icona e sito. Tolto anche l'ultimo blu (i link "Leggi la guida" e "Riprendi tutte" ora sono testo sottolineato). Analisi fatta su schermate reali in chiaro e scuro, con la lente di frontend-design ("una sola cosa forte, il resto quieto") e superpowers.

### Da sistemare prima di caricare
1. **Contrasto in scuro.** Con un accento grigio macOS applica il suo Grafite chiaro: testo bianco su grigio chiaro (Rinomina, "Tutti i file", selezione nella barra laterale, numeri delle sezioni) a circa 2:1, sotto il minimo di 4,5:1. Serve testo scuro sull'accento in modalità scura.
2. **Troppi blocchi pieni in chiaro.** Barra laterale con due selezioni nere (cartella e filtro), cerchi numerati neri, etichetta "Tutti i file" nera, interruttori neri, Rinomina nero: l'occhio non sa dove andare. Pieno solo Rinomina; selezioni in grigio leggero con testo normale, come il Finder; numeri a contorno.

### Importanti
3. **Nuovo nome tutto evidenziato.** Quando cambia tutto il nome, il fondo grigio copre tutto e sembra testo selezionato. Meglio: parti nuove in testo pieno, parti che restano in grigio, nessun riquadro.
4. **Due spunte per riga.** Il segno "verrà rinominato" e la spunta di scelta sono due cerchi uguali uno accanto all'altro. L'icona di stato serve solo per avvisi ed errori.
5. **Lo stesso numero ripetuto quattro volte.** "Verranno rinominati tutti i 6 file", "6 da rinominare", "Rinomina 6 file", "cambia 6 file". Ne basta uno vicino a Rinomina.
6. **Pannello file vuoto sempre aperto.** "Seleziona un file" occupa un quinto della finestra senza fare nulla. Chiuso di base, si apre quando scegli un file.
7. **"cambia 6 file" con la barra sotto** sembra un cursore da trascinare. Solo testo.
8. **Schermata iniziale:** le icone delle cartelle recenti sono blocchi neri; il percorso mostra un pezzo di codice ("…-b03f-…/scratchpad") invece della cartella madre.

### Minori
9. Estensione che cambia solo maiuscole (ARW → arw) segnata in rosso barrato: allarme per una modifica innocua. Grigio barrato.
10. Le righe di aiuto sotto i titoli (11 pt grigio chiaro) si leggono a fatica.
11. BETA arancione è l'unico colore dell'interfaccia oltre agli errori: va bene, segnala lo stato.

### Non verificato a schermo
Popover dei pezzi, pannello file con un file scelto, vista Griglia, Impostazioni e Guida: servono clic, e le autorizzazioni di Accessibilità non vanno date. Da provare a mano.

**Fatto in 1.3.1 (4 nov 2026):** punti 1–8 sistemati e verificati su schermate in chiaro e scuro. Restano per dopo: estensione che cambia solo maiuscole in rosso (9), righe di aiuto poco leggibili (10), e la prova a mano di popover, pannello file, Griglia, Impostazioni e Guida.
