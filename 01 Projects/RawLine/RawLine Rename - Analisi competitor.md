# RawLine Rename: priorità di naming dai competitor

Data: 2026-11-03. Le funzioni di rinomina da aggiungere a [[RawLine Rename]], ricavate dal confronto con Advanced Renamer 4, A Better Finder Rename 12, Renamer 7, Name Mangler 3, Transnomino, NameChanger e Photo Mechanic, e dalle convenzioni usate dai professionisti. Ordinate per priorità, con la user experience al primo posto.

## Priorità 1: prima della versione 1.0

| # | Funzione | Chi ce l'ha | Perché conta | Come farla "alla RawLine" |
|---|---|---|---|---|
| 1.1 | **Blueprint di naming per settore** | Nessuno in questa forma (Lightroom ha solo modelli strutturali) | Chi apre l'app per la prima volta non vuole costruire regole da zero: vuole partire dalla convenzione del suo settore e adattarla. | Una grammatica a caselle e sette blueprint: vedi sotto, "Blueprint di naming". |
| 1.2 | **Notte lunga: data dello scatto che segue la sessione** (fatto, beta 1.2) | ABFR (solo orario fisso) | Matrimoni, eventi e astrofotografia passano la mezzanotte: il contatore riparte a metà festa e le foto delle 00:30 finiscono nel giorno dopo. | **Spenta per impostazione predefinita**, attivabile per regola. Vedi sotto, "Notte lunga". |
| 1.3 | **Scatti nello stesso secondo** (fatto in parte, beta 1.2: opzione Centesimi; il suggerimento automatico dall'avviso conflitti resta da fare) | ABFR | Con la raffica dell'Alpha 1 decine di file hanno lo stesso `{date:HHmmss}`. Oggi interviene l'avviso conflitti, ma è la regola a dover dare un risultato pulito. | Variabile `{subsec}` (millisecondi, già letti da ImageMetadataReader) e suffisso automatico per lo stesso secondo: `_143022`, `_143022-2`. Proporlo quando l'avviso conflitti trova questo caso ("23 file scattati nello stesso secondo: aggiungo i centesimi?"). |
| 1.4 | **Profilo "Compatibile ovunque"** | ABFR (Windows/SMB) | Consegne su NAS, WeTransfer, Google Drive e siti: caratteri come `:` `?` `"` e i nomi lunghi rompono i file su Windows. | Nella regola Pulisci: opzione "Sicuro per Windows, NAS e web". Aggiungere all'avviso conflitti il limite Windows (260 caratteri di percorso). |

## Notte lunga

L'orario fisso di A Better Finder Rename ("il giorno inizia alle 4") rovina proprio gli scatti outdoor: una salita in vetta che parte alle 03:30 o un'alba alle 04:45 d'inverno finirebbero nel giorno prima. Per questo la funzione non è mai attiva da sola e ha tre stati:

| Stato | Come funziona | Quando serve |
|---|---|---|
| **Spenta** (predefinita) | La data è quella del calendario. | Sempre, salvo i casi sotto. Nessuna sorpresa. |
| **Automatica, a sessioni** | Il giorno cambia solo dopo una pausa negli scatti di almeno [3] ore. Una sequenza continua resta tutta nel giorno in cui è cominciata. | Matrimoni ed eventi (21:00 → 02:00 senza pause = un solo giorno); astrofotografia (22:00 → 04:00 = la notte di partenza). Un'alba alle 03:30 dopo una notte di sonno arriva dopo una pausa lunga: giorno nuovo, data giusta. |
| **Orario fisso** | Il giorno inizia all'ora scelta, es. [05:00]. | Per chi preferisce una regola semplice e prevedibile. |

Regole di interfaccia:
- Si sceglie nelle opzioni secondarie della regola Formato nome e del Contatore ("Ripartenza ogni giorno"), non nelle impostazioni generali: vale per quel preset, non per tutta l'app.
- Nell'anteprima ogni file la cui data è stata spostata mostra un segno discreto ("data del 14 giugno, scattata alle 00:42 del 15"), e il riepilogo in basso dice quanti sono. Mai una modifica invisibile.
- È già accesa, in modalità Automatica, solo nel blueprint *Matrimoni ed eventi privati*.

## Blueprint di naming

### Cosa dice la ricerca

Ho cercato le convenzioni di fotografi e organizzazioni di alto profilo in più settori. Non esiste uno standard unico, ma le fonti convergono su pochi punti:

1. **Data + chi + cosa + numero è lo scheletro di quasi tutti.**
   - Peter Krogh (*The DAM Book*, il riferimento sul digital asset management per fotografi): nome o iniziali del fotografo, data, numero.
   - ProStorage: `20140101_Scorsese_Martin_MGP_0456` (data, soggetto, sigla dello studio, numero).
   - Prism Photo Workshop, per i fotogiornalisti freelance: data, cognome del fotografo, slug della storia, numero.
   - La convenzione che usi tu (`data_NomeCognome_soggetto_numero_originale`) è in linea con questi.
2. **Si rinomina una volta sola, all'importazione.** dpBestflow, la guida al flusso digitale dell'ASMP (l'associazione americana dei fotografi professionisti), raccomanda nomi permanenti e unici assegnati all'ingest: riduce la confusione tra copie, software e cliente.
3. **Il numero si assegna in ordine di scatto tra tutte le fotocamere.** ProStorage e le guide per matrimoni lo dicono esplicitamente per evitare collisioni con due corpi.
4. **Chi scatta va dichiarato quando i file escono dallo studio.** Le riviste chiedono il nome del fotografo nel file (Black+White Photography lo vuole all'inizio). Gli studi di matrimonio mettono una lettera per il secondo fotografo, **in fondo**, dopo il numero, perché al cliente non interessa.
5. **Il committente può imporre il suo formato.** dpBestflow: il fotografo usa i propri nomi, chi riceve le immagini fornisce eventuali istruzioni. Nella pubblicità alcuni studi usano un **codice lavoro** al posto del nome del cliente nei file condivisi, per riservatezza.
6. **Le voci contrarie, da tenere a mente.**
   - dpBestflow sconsiglia di mettere nomi di lavori e descrizioni nel nome del file.
   - Archivi e musei preferiscono identificatori non descrittivi e lasciano il contenuto ai metadati.

   Il compromesso: nel nome solo ciò che serve a riconoscere il lavoro (data, chi, cliente o soggetto in breve), tutto il resto nei metadati IPTC.
7. **Il video è un caso a parte.** Le cineprese professionali (RED, ARRI, Canon) usano già lettera della camera, rullo e clip (`A001C001`). Le guide di produzione sconsigliano di rinominare gli originali, perché sidecar, timecode e ricollegamento dei proxy dipendono dal nome.
8. **Agenzie e pool: Getty Images, Reuters, AP.** Sono il riferimento per sport e grandi eventi: ai Giochi di Sochi l'AP trasmetteva circa 2.000 foto al giorno, e i fotografi di Getty e Reuters insieme hanno scattato circa un milione di fotogrammi (Gizmodo). Cosa si sa e cosa no:
   - Le agenzie **non pubblicano** una convenzione di nomi per i fotografi: non l'ho trovata né per Getty, né per Reuters, né per AP.
   - Una volta in archivio, Getty rinomina i file con un proprio codice numerico (le immagini si scaricano come `GettyImages-` seguito dal numero). Il nome del fotografo conta quindi **prima della trasmissione**, sul banco del photo editor e nel pool.
   - L'attribuzione vera passa dai metadati IPTC (autore, credito, fonte). Lo standard è dell'IPTC, di cui AP, Getty e Reuters sono membri.
   - Nei pool l'attribuzione automatica si fa con le Hot Codes di Photo Mechanic, che diverse grandi testate usano al Super Bowl per assegnare i crediti a ogni fotografo.

   Per questo il blueprint Sport, agenzie e pool usa le iniziali e l'evento: nome corto, chi ha scattato si legge subito, il resto sta nei metadati.

### La grammatica: sei caselle, sempre nello stesso ordine

Ogni blueprint è la stessa fila di caselle, alcune accese e altre spente. Chi impara la grammatica capisce tutti i blueprint.

`DATA` `_` `CHI` `_` `CLIENTE` `_` `SOGGETTO` `_` `NUMERO` `_` `ORIGINALE`

| Casella | Valore | Da dove viene | Note |
|---|---|---|---|
| **DATA** | `20260614` | Data di scatto, formato unico in tutti i blueprint | Tutta attaccata: ordina per data e non riempie il nome di trattini. |
| **CHI** | `GiuliaFerri`, `Ferri` o `GF` | Dal campo Autore/Copyright impostato in fotocamera, oppure scritto una volta nelle impostazioni | Tre forme a scelta: nome e cognome, cognome, iniziali. Nessuna domanda a ogni lavoro. |
| **CLIENTE** | `Salewa` o `J2614` | Domanda al primo uso, ricorda l'ultimo valore | Nome del cliente oppure codice lavoro, per i lavori riservati. |
| **SOGGETTO** | `FW26-Campaign`, `Rossi-Bianchi`, `JUV-INT` | Domanda, nome della cartella o città dai metadati | Shooting, evento, partita, luogo. |
| **NUMERO** | `0001` | Progressivo in ordine di scatto tra tutti i corpi, dopo l'allineamento degli orologi | Ordinando per nome è lui a mettere in fila le foto di più macchine. RAW, JPEG e XMP gemelli prendono lo stesso numero. |
| **ORIGINALE** | `DSC01234` | Nome della fotocamera, identico | Per risalire sempre al file della scheda. |

Regole fisse:
- **Il corpo, se serve, va tra NUMERO e ORIGINALE** (`…_0001_GF2_DSC01234`): prima del numero romperebbe l'ordine cronologico.
- Le caselle spente spariscono con il loro separatore: mai `__`.
- `_` separa le caselle, `-` sta dentro una casella (`Rossi-Bianchi`, `JUV-INT`).
- **Lunghezza**: con tutte le caselle accese e il nome completo si arriva a circa 60 caratteri. L'anteprima avvisa sopra i 50 e suggerisce di passare CHI a cognome o iniziali.

### I sette blueprint

Esempi su: Giulia Ferri, Sony Alpha 1 con tag GF1, `DSC01234.ARW`, scattato il 14 giugno 2026. Tra parentesi quadre le domande.

| Blueprint | Caselle accese | Esempio | Perché, secondo le fonti |
|---|---|---|---|
| **Personale e portfolio** (predefinito) | DATA, CHI, SOGGETTO, NUMERO, ORIGINALE | `20260614_GiuliaFerri_Cervino_0001_DSC01234` | Lo schema di Krogh e di ProStorage: chi, quando e cosa, sempre riconoscibile anche fuori dal tuo disco. Il soggetto può venire dalla città, senza domande. |
| **Commerciale e ADV** | DATA, CHI, [CLIENTE], [SOGGETTO], NUMERO, ORIGINALE | `20260614_GiuliaFerri_Salewa_FW26-Campaign_0001_DSC01234` | Cliente e shooting sono il modo in cui l'agenzia e il brand cercano i file. Opzione **Codice lavoro** al posto del cliente per i lavori riservati prima del lancio: `20260614_GiuliaFerri_J2614_FW26_0001_DSC01234`. |
| **Editoriale** | DATA, CHI, [SOGGETTO = testata o storia], NUMERO, ORIGINALE | `20260614_GiuliaFerri_Montagna-Ghiacciai_0001_DSC01234` | Le redazioni vogliono il nome del fotografo nel file e lo slug della storia (Prism, Black+White). Se una testata impone il nome all'inizio assoluto, si rinominano le copie consegnate, non gli originali. |
| **Matrimoni ed eventi privati** | DATA, CHI, [SOGGETTO = coppia o evento], NUMERO, corpo, ORIGINALE + Notte lunga automatica | `20260614_Ferri_Rossi-Bianchi_0001_GF1_DSC01234` | Date-first, coppia, numero a 4 cifre, codice del fotografo dopo il numero: è la convenzione più diffusa tra gli studi di matrimonio. CHI col solo cognome per stare sotto i 50 caratteri. |
| **Sport, agenzie e pool** | DATA, CHI, [SOGGETTO = partita o gara], NUMERO, ORIGINALE | `20260614_GF_JUV-INT_0001_DSC01234` | Il nome dell'evento e la data, più il nome della fotocamera, sono la scelta dei fotografi sportivi. Iniziali per CHI: in un pool ogni fotografo ha la sua sigla e l'attribuzione è automatica. **Preset e tabella dei corpi si esportano e si danno a tutta la squadra.** Per una cartella per gara, SOGGETTO = nome della cartella. |
| **Studio con numero di lavoro** | [CLIENTE = numero lavoro], SOGGETTO, NUMERO, ORIGINALE | `26-1042_Salewa_0001_DSC01234` | Il sistema dei grandi uffici fotografici (Boston University): anno a due cifre e numero d'incarico, che coincide con preventivi e fatture. **Niente data all'inizio**: comanda il numero di lavoro. Vale anche per prodotto ed e-commerce, con il codice prodotto al posto del numero (`SKU-48213_01_DSC01234`). |
| **Video** | Nessuna rinomina degli originali (consigliato), oppure DATA, [SOGGETTO], ORIGINALE | `20260614_DOC-Cervino_C0012` | Sidecar, timecode e proxy dipendono dal nome della clip. Il blueprint avvisa e propone di lasciare gli originali come sono. Se si rinomina, il nome della clip resta intero in fondo. |

### Come appaiono nell'app

**Fatto e pubblicato nella beta 1.1 (3 novembre 2026), in italiano e in inglese:**
- Nel menu Preset (barra in alto e menu File › Preset), sotto i preset salvati, la sezione **Blueprint** con i sette nomi, un'icona e una riga di descrizione ciascuno.
- Scegliere un blueprint carica una regola Formato nome e il menu mostra "Senza nome, da “Matrimoni ed eventi privati”". Il blueprint originale non cambia mai. Salva preset propone il nome del blueprint.
- Le parole segnaposto (Soggetto, Cliente, Shooting, Storia, Sposi, Evento, Progetto, NNNN) sono nella lingua dell'app e si sostituiscono nel campo del formato.
- CHI viene da `{author:joined}`, `{author:surname}` o `{author:initials}` (anche `unito`, `cognome`, `iniziali`), letti dall'autore impostato in fotocamera. Il © e l'anno del copyright si ignorano.
- La Guida (Aiuto › Guida › Preset) spiega i blueprint.

| Blueprint nell'app | Modello caricato |
|---|---|
| Personale e portfolio | `{date:yyyyMMdd}_{author:joined}_Soggetto_{counter}_{original}` |
| Commerciale e ADV | `{date:yyyyMMdd}_{author:joined}_Cliente_Shooting_{counter}_{original}` |
| Editoriale | `{date:yyyyMMdd}_{author:joined}_Storia_{counter}_{original}` |
| Matrimoni ed eventi privati | `{date:yyyyMMdd}_{author:surname}_Sposi_{counter}_{body}_{original}` |
| Sport, agenzie e pool | `{date:yyyyMMdd}_{author:initials}_Evento_{counter}_{original}` |
| Studio con numero di lavoro | `{date:yy}-NNNN_Cliente_{counter}_{original}` |
| Video (solo video) | `{date:yyyyMMdd}_Progetto_{original}` |

Numero a 4 cifre, in ordine di scatto, mai azzerato, con numerazione Automatica (dalla beta 1.2).

**Fatto e pubblicato nella beta 1.2 (3 novembre 2026), in italiano e in inglese:**
- **Numerazione Automatica o Manuale** sul pezzo Contatore (e nella regola Formato nome). Automatica: il contatore continua dopo il numero più alto già presente nella cartella per i nomi che cominciano allo stesso modo (stessa data, autore, soggetto); i file del lotto non contano, così rilanciare l'anteprima non fa salire i numeri. Se non trova nulla parte da Inizio. Manuale: parte sempre da Inizio. I nomi nuovi e i blueprint nascono in Automatica; i preset vecchi si aprono in Manuale.
- **Notte lunga** sul pezzo Data: Senza notte lunga / Per sessioni (pausa regolabile, 3 h di base) / Da un'ora (5:00 di base). Sposta il giorno di `{date}` (l'ora resta quella vera) e la ripartenza ogni giorno. Spenta di base; accesa per sessioni solo nel blueprint Matrimoni.
- **Centesimi di secondo**: casella sul pezzo Data quando il formato ha i secondi; `HHmmss` diventa `HHmmssSS`.
- **Aggiornamenti a ogni apertura**: l'app cerca subito una nuova versione invece di aspettare un giorno dall'ultimo controllo.

**Da fare:**
- Le sei caselle come gettoni da accendere e spegnere nella riga del Formato nome, ognuna con la sua fonte.
- Le domande al posto delle parole segnaposto (vedi `{ask:…}` sotto).
- Alla prima apertura: "Che lavoro fai più spesso?", con i sette blueprint.

### Cosa serve nel motore

- ~~`{author}` con tre forme~~ (fatto). Resta da fare: un valore di riserva nelle impostazioni per chi non imposta l'autore in fotocamera.
- **Campo da compilare nel preset**: una variabile tipo `{ask:Cliente}` che l'interfaccia mostra come campo evidenziato, chiede al primo uso e ricorda l'ultimo valore.
- ~~Separatore che sparisce con la variabile vuota~~ (fatto, beta 1.1): un dato mancante resta vuoto e porta via un separatore accanto; i separatori doppi scritti a mano restano.
- ~~Continua la numerazione~~ (fatto, beta 1.2, come numerazione Automatica).
- **Blueprint in sola lettura** nel menu Preset, distinti da I miei preset.
- **Esportazione e importazione di preset e tabella dei corpi** come file unico, per i pool.
- **Avviso sui video**: quando una regola tocca clip video, ricordare che la rinomina può rompere sidecar e proxy.
- **Avviso di lunghezza** sopra i 50 caratteri.
- ~~Notte lunga~~ (fatto, beta 1.2): i tre stati, applicata sia a `{date}` sia alla ripartenza per giorno.
- **Pulisci: spazi e parentesi diventano trattini**, da verificare su quello che fanno oggi `collapseWhitespace` e `removeInvalidCharacters`.

Avvertenza da mostrare nei blueprint: rinominare **prima** di importare in Lightroom o Capture One, perché i cataloghi perdono il collegamento ai file rinominati da fuori.

### Strumenti a parte

| Strumento | Cosa fa | Esempio |
|---|---|---|
| **Sistema nomi ricevuti** | Solo Pulisci (spazi, accenti, caratteri non ammessi, emoji) + estensione minuscola. Non cambia il senso del nome. | `Foto Matrimonio (1)  copia.JPG` → `Foto-Matrimonio-1-copia.jpg` |
| **Torna al nome della fotocamera** | `{original}`: annulla qualsiasi rinomina, anche di settimane fa. | `DSC01234` |

## Priorità 2: versione 1.x

| # | Funzione | Chi ce l'ha | Perché conta | Come farla |
|---|---|---|---|---|
| 2.1 | **Descrivi cosa vuoi, RawLine crea le regole** | Renamer 7 (AI Assist locale) | Il modo più semplice di usare un rinominatore: niente da imparare. | Framework Foundation Models di Apple (on-device, offline, compatibile con la sandbox): un campo "Descrivi il nome che vuoi" sopra Aggiungi regola, che produce regole normali e modificabili. Solo su macOS 26. |
| 2.2 | **Rinomina con preset da Comandi rapidi e dal Finder** | ABFR (preset applicati trascinando sull'icona) | Rinominare senza aprire l'app: tasto destro › "Rinomina con preset". | Un App Intent "Rinomina con preset" che usa il motore così com'è, con anteprima e conferma. Il servizio Finder c'è già: va esteso ai preset. Se non si sceglie un preset, si apre la finestra con i file caricati. |
| 2.3 | **Nomi da elenco o da CSV** | Advanced Renamer, ABFR, Renamer 7 | Elenchi di prodotti, atleti, alunni, ospiti per i ritratti. | Regola "Da un elenco": incolla testo o scegli un CSV; abbinamento per ordine oppure per colonna (nome attuale → nome nuovo). Avviso se il numero di righe non corrisponde. |
| 2.4 | **Tabelle di sostituzione (alla Hot Codes)** | Photo Mechanic | La tabella dei corpi è già una tabella seriale → tag: generalizzarla copre codici cliente, numeri di maglia, sigle località. | Variabile `{lookup:NomeTabella:variabile}` con tabelle modificabili nelle impostazioni, importabili da CSV. |
| 2.5 | **Scegliere quale data usare** e **fuso orario** | ABFR 12 | File con più date in conflitto (EXIF, creazione, XMP); viaggi con fuso diverso. | Nel formato data: "Usa [Data di scatto ▾]" con priorità; opzione "ora locale del luogo di scatto / mia ora". `OffsetTime` è già letto. |
| 2.6 | **Ordine manuale per il contatore** | ABFR (drag and drop) | `BatchOrder` ha data di scatto, nome, ordine dato: manca il trascinamento delle righe per decidere a mano la sequenza. | Trascinamento nell'elenco quando l'ordinamento è "Manuale". |
| 2.7 | **Esposizione e bracketing** | ABFR 12.29 | Per paesaggi HDR: riconoscere i gruppi dal nome. | Variabili `{ev}` (compensazione) e numero nella serie di bracketing. |
| 2.8 | **Maiuscole solo su una parte** | ABFR 12 | Es. città in maiuscolo dentro un nome più lungo. | Ambito "solo il blocco N" o "solo tra … e …" nella regola Maiuscole e minuscole. |

## Sintesi

1. **Una grammatica a sei caselle e sette blueprint per settore**, costruiti sulle convenzioni reali dei professionisti e sull'idea che si rinomina una volta sola.
2. **Casi reali da evento**: notte lunga (spenta di default, automatica a sessioni) e scatti nello stesso secondo.
3. **Rinominare senza aprire l'app**: Comandi rapidi e preset nel Finder.
4. **"Descrivi cosa vuoi"** con l'AI on-device di Apple.

## Fonti

**Convenzioni dei professionisti**
- [dpBestflow (ASMP): File Delivery Checklist](https://www.dpbestflow.org/file-delivery/file-delivery-checklist) · [File Naming](https://www.dpbestflow.org/file-management/file-naming) · [ASMP su dpBestflow](https://www.asmp.org/strictly-business-blog/be-a-professional-with-dpbestflow/)
- [The DAM Book di Peter Krogh](http://thedambook.com/the-dam-book/) · [discussione sulla sua convenzione (NikonCafe)](https://www.nikoncafe.com/threads/what-is-your-file-naming-convention.110980/)
- [ProStorage: The World's Best File Naming System](https://getprostorage.com/blog/worlds-best-file-naming-system/)
- [Prism Photo Workshop: onboarding fotogiornalisti freelance](https://www.prismphotoworkshop.org/onboarding-freelance-photojournalists-template) · [Black+White Photography: invii](https://www.blackandwhitephotographymag.co.uk/submissions/)
- [PhotoMint: nomi dei file nei matrimoni](https://www.photomint.com/shooting-a-wedding/how-to-name-your-image-files/) · [VSCO: consegna ai clienti](https://www.vsco.co/learn/how-to-share-photos-with-clients)
- [TTL Sports: dati per fotografi sportivi](https://www.ttlsports.com/data-management-best-practices-for-sports-photographers) · [Photo Mechanic: ingest e rinomina (JM Peltier)](https://www.jmpeltier.com/importing-editing-metadata-photo-mechanic/)
- [Boston University Marcom: convenzione YY-NNNN-SLUG](https://sites.bu.edu/marcom-team/departments/photography/server-organization-naming-conventions) · [Roslund: numero di lavoro](https://www.roslundmackenzie.com/news/file-naming-conventions) · [SendPhoto: codice lavoro per i lavori riservati](https://sendphoto.io/blog/photo-organization-tips)
- [RED: convenzione nomi delle clip](https://docs.red.com/955-0047/MediaOperationGuide/Content/5_Eject_And_Format_Media/Clip_Naming_Convention.htm) · [Clapper: nomi delle clip e perché non rinominarle](https://clapper.in/articles/camera-clip-naming-conventions/)
- [UT Austin: nomi dei file nella digitalizzazione](https://cloud.wikis.utexas.edu/wiki/display/utldigitalstewardship/Digitization%3A+File+naming) · [Queen's University Belfast: scegliere un nome](https://www.qub.ac.uk/research-centres/CentreforDataDigitisationandAnalysis/ServicesandOutputs/ToolkitsandGuides/ChoosingaFileName)

**Agenzie**
- [Gizmodo: come lavorano i fotografi alle Olimpiadi](https://gizmodo.com/the-inside-story-of-how-olympic-photographers-capture-s-1521746623)
- [Getty Images: documentazione per sviluppatori (nomi dei file scaricati)](https://developer.gettyimages.com/docs/gettingstarted/)
- [IPTC](https://en.wikipedia.org/wiki/International_Press_Telecommunications_Council)
- [Photo Mechanic: Hot Codes, webinar](https://home.camerabits.com/wp-content/uploads/2023/02/Photo-Mechanic-Hot-Codes-Webinar-Notes.pdf)

**Competitor**
- [Advanced Renamer per macOS](https://www.advancedrenamer.com/mac)
- [A Better Finder Rename](https://www.publicspace.net/ABetterFinderRename/) · [novità versione 12](https://www.publicspace.net/ABetterFinderRename/version12.html) · [preset applicati trascinando](https://www.publicspace.net/ABetterFinderRename/v12/PresetsPopUp.html)
- [Renamer 7](https://renamer.com/)
- [Name Mangler](https://manytricks.com/namemangler)
- [Photo Mechanic: Hot Codes](https://docs.camerabits.com/support/solutions/articles/48001252633-hot-codes)
- [Lightroom Classic: modelli di nome](https://jkost.com/blog/2021/03/renaming-files-in-lightroom-classic.html)
