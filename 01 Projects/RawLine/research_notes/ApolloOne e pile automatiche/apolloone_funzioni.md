# ApolloOne: inventario completo delle funzioni (stato al 10 novembre 2026)

Nota sulle fonti. Il dominio apolloone.com oggi è parcheggiato e risulta in vendita su GoDaddy (redirect 307 verificato il 10/11/2026). Il sito ufficiale attuale è anogeissus.com. Lo sviluppatore è **Anogeissus Limited**: è il "seller" sul Mac App Store, e non "Zhao". La fonte primaria più ricca è il manuale ufficiale in PDF, versione 5.0.1, di 4.968 righe di testo estratto: https://anogeissus.com/downloads/ApolloOne-Help-en.pdf?v=501 (qui sotto: [Guida]). Altre fonti:
- [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- [Pagina prodotto](https://anogeissus.com/apolloone.html)
- [FAQ](https://anogeissus.com/apolloone-faq.html)
- [Blog](https://anogeissus.com/blog.html)
- [Supporto](https://anogeissus.com/support.html)

Gli anni delle date del blog sono 2026, salvo dove indicato. Quasi tutto il materiale è dichiarazione ufficiale dello sviluppatore. Recensioni indipendenti ne ho trovate pochissime: vedi la sezione Gaps.

## 1. Identità, versioni ed edizioni (gratis o a pagamento, prezzi)

### Takeaway
È un'app gratuita con acquisti in-app su quattro livelli: Free, Standard, Pro e Max. Ogni livello si può avere in abbonamento annuale o con licenza perpetua. La versione 5.0 (30 settembre 2026) ha introdotto l'edizione Max, che contiene tutte le funzioni di culling "intelligenti": Stacks, Focus Score, AI Rating e AI Keywords. Le funzioni AI e ML richiedono macOS 27.

### Cited Findings
- Versione corrente 5.1.0 (22 ottobre 2026), 38,2 MB, richiede macOS 14 o successivo, venditore Anogeissus Limited, 11 lingue. — [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- Prezzi degli acquisti in-app (USD):
  - Standard perpetua 35,99; Standard 1 anno 14,99
  - Pro 1 anno 23,99; Pro perpetua 59,99; aggiornamento perpetuo Pro 23,99
  - Max perpetua 99,99; Max trial 14 giorni 0,00
  - Da Pro a Max 40,00; da Standard a Max 64,00

  [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12). L'App Store non elenca un abbonamento Max annuale con prezzo, ma la FAQ parla di un unico gruppo di abbonamenti Standard/Pro/Max. — [FAQ](https://anogeissus.com/apolloone-faq.html)
- Ogni installazione parte con 14 giorni di trial Max. Alla scadenza nulla viene addebitato e l'app torna all'edizione Free, che resta usabile a tempo indeterminato con "unlimited image and video browsing" e alcune funzioni di editing. Dopo 14 giorni l'app ricorda di abbonarsi. — [Guida], [FAQ](https://anogeissus.com/apolloone-faq.html)
- Chi aveva pagato le versioni 1.x o 2.x riceve automaticamente la licenza perpetua Standard. Le licenze sono legate all'Apple ID. — [Guida], [FAQ](https://anogeissus.com/apolloone-faq.html)
- **Standard** (secondo la tabella della Guida):
  - visualizzazione dei punti AF e dei volti rilevati dalla fotocamera
  - Batch Rename, operazioni batch (GPS, rotazione, date EXIF, rimozione metadati), ritaglio
  - modifica di EXIF, MakerNotes e campi XMP/IPTC comuni nell'Inspector
  - alias, ordinamento "User Defined Sequence", ordinamento per cartella, ordinamento casuale
  - avvisi di sovraesposizione e sottoesposizione per i RAW
  - decodifica RAW al 100% invece che al 50%
  - Sharpen Displayed Image, rilevamento dei metadati AI (ComfyUI, A1111/Forge, Midjourney, NovelAI), export WebP
  - List View, tab e finestre multiple

  [Guida]
- **Pro** (in aggiunta a Standard):
  - Split View con zoom e scroll sincronizzati
  - batch resize e conversione, batch export
  - import da scheda con ripresa automatica
  - filtro sul contenuto dei metadati con regex, filtro per keyword, filtri GPS di distanza e altitudine
  - aggiunta di nuovi tag IPTC/XMP e "Synchronize XMP sidecar file to image"
  - export TIFF, PNG e HEIC; registrazione dello slideshow in video; template di metadati
  - scorciatoie personalizzabili
  - RawBridge per RAF compressi Fujifilm e NEF HE/HE* Nikon, InstaBake
  - HDR Mode RAW, SDR Proof Mode, HDR slideshow, export JPEG XL e AVIF, gain map JPEG/HEIC, istogramma HDR
  - Automatic Lens Correction
  - nascondere voci di menu, "Backup to:" all'import, import fino a 2 volte più veloce

  [Guida], [FAQ](https://anogeissus.com/apolloone-faq.html)
- **Max** (in aggiunta a Pro):
  - ML Processing (macOS 27)
  - Focus Score, Stacks, AI Rating e AI Keywords (macOS 27)
  - keyword gerarchiche scritte nel campo letto da Lightroom e Photo Mechanic
  - Code Replacements, AppleScript, status bar personalizzabile
  - Liquid Glass Mode (macOS 26)

  [Guida], [Pagina prodotto](https://anogeissus.com/apolloone.html)
- Note a piè di pagina della Guida: "Requires macOS 27 Golden Gate or later" per ML e AI, macOS 26 Tahoe per Liquid Glass, macOS 15 Sequoia per alcune funzioni. — [Guida]
- Il Keywords Manager (albero, vocabolari, import, unione, export) è incluso in ogni edizione. — [Pagina prodotto](https://anogeissus.com/apolloone.html)
- **Conflitto** sui requisiti minimi: le note della 4.7.0 dicono "minimum requirement of macOS 12", mentre la scheda attuale richiede macOS 14. Probabilmente il requisito è stato alzato tra la 4.7 e la 5.x, ma non ho trovato la nota che lo dica. — [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- **Prezzi vecchi**, da fonte terza e datata, quindi superati: trial di un mese a 0,99 $, Pro annuale a 19,99 $, Standard annuale a 11,99 $. — [Aftershoot](https://aftershoot.com/blog/best-9-photo-mechanic-culling-alternatives/)
- **Prodotti collegati**:
  - ApolloOne GO per iPhone e iPad: 1.0.0 il 30 luglio 2026, 2.0.2 il 28 ottobre 2026
  - Camera RawX: plugin Quick Look che mostra le modifiche fatte in ApolloOne

  [Blog](https://anogeissus.com/blog.html)

### Inferences
- La strategia commerciale è "visualizzatore gratuito più funzioni pro a livelli". Il culling avanzato (stack, nitidezza, AI) è stato messo nel livello più alto a 99,99 $, il che indica che lo sviluppatore lo considera il valore principale.

### Gaps
- Non ho trovato il prezzo dell'abbonamento annuale Max: la scheda dell'App Store recuperata non lo elencava.
- Non ho trovato la data della prima uscita (v1.0, ID App Store 1044484672, quindi intorno al 2015). Una recensione sull'App Store datata 2017 conferma che l'app esisteva almeno da allora.

## 2. Viewer: RAW, anteprima incorporata o decodifica, zoom, schermo intero, colore, istogramma, punti AF, clipping

### Takeaway
ApolloOne è un viewer a piena risoluzione. Per i RAW si può scegliere tra due strade:
- il JPEG incorporato, la via veloce
- una decodifica completa: Apple RAW come base, poi RawBridge per i formati che Apple non legge, LibRaw come ripiego, più ML Processing opzionale

Ha una cache con lettura in anticipo, uno zoom a scatti con tasti dedicati, la sovrapposizione dei punti AF e dei volti, un istogramma SDR e HDR, avvisi di sovra e sottoesposizione e una pipeline HDR molto sviluppata. Non ho trovato supporto esplicito per più monitor.

### Cited Findings
- **Pipeline RAW**:
  - Con "RAW > Use Embedded JPEG Preview Image" attivo, l'app usa il JPEG incorporato. Se l'anteprima manca o ha risoluzione insufficiente, entra in gioco il decoder.
  - Il decoder predefinito è Apple RAW con RawBridge. Il ripiego automatico è LibRaw.
  - La barra del titolo mostra [AppleRaw], [RawBridge] o [LibRaw], con "+ALC" quando è attiva la correzione automatica delle lenti.
  - Le simulazioni Fujifilm e i Picture Control Nikon non vengono applicati.

  [Guida]
- RawBridge, sviluppato con Gentlemen Coders LLC, pre-elabora i RAF compressi Fujifilm, i NEF HE/HE* Nikon, gli ORF di OM Digital Solutions e gli ARW Sony per farli passare nella pipeline Apple. È riservato all'edizione Pro. — [Guida]
- ML Processing (Max, macOS 27, ⌃⌘M) usa il decoder RAW Apple basato su machine learning: riduzione del rumore e demosaicizzazione migliore, con i guadagni maggiori su X-Trans. Copre 156 modelli di fotocamera. — [Guida], [Pagina prodotto](https://anogeissus.com/apolloone.html)
- La 4.8.0 (12 agosto 2026) ha aggiunto l'export del JPEG incorporato dal RAW. La 4.0.0 ha aggiunto "Instant JPEG Comparison", per confrontare il RAW con la sua anteprima incorporata. — [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12), [Guida]
- **Cache dei file**:
  - Pre-caricamento con lettura in anticipo e all'indietro, I/O concorrente e politica "adaptive LRU".
  - La dimensione predefinita dipende dalla RAM (8 con 8 GB). Si regola a mano da 4 a 32 immagini.
  - In modalità Auto la cache si adatta al supporto (per esempio riduce i thread su un NAS via Wi-Fi) e cresce con i RAW in base ai core e al tipo di disco (SSD o no).

  [Guida]. Una nota vecchia dice "File cache is now configurable from 2 to 16", quindi l'intervallo è stato ampliato in seguito. — [Guida, revision history]
- Visualizzazione veloce durante zoom e interazione, poi un secondo passaggio di qualità con filtro Lanczos quando l'utente si ferma. Il Lanczos non è disponibile in Fluid Swipe. — [Guida]
- **Dichiarazioni sulla velocità**: piena risoluzione, non anteprime scalate, "up to 55 fps on M1 Ultra"; "Arguably the fastest image viewer ever created for the macOS"; l'app usa multithreading, GCD e Core Image. — [Pagina prodotto](https://anogeissus.com/apolloone.html), [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- **Zoom**:
  - F adatta, T adatta in larghezza, Y adatta in altezza, = e - zoom avanti e indietro, S scala per riempire
  - ⌃1–⌃9 per zoom dal 10% al 90%; con ⌥ lo zoom è "by resolution", cioè per megapixel
  - D attiva/disattiva il 50%, Z il 100%, G il 200%
  - pan con ⌥+frecce
  - Navigator panel dalla 3.7.1

  [Guida]
- **Loupe**: un loupe circolare è stato migliorato nella 4.0.0. Dalla 5.0.0 "Click to zoom replaces the loupe": un clic o la pressione prolungata ingrandisce, con livelli configurabili al 100, 150, 200, 300 e 400%. Dalla 5.0.1 il click-to-zoom si può disattivare. — [Guida]
- Lo zoom al 100% (Z) centra automaticamente il primo punto AF o il primo volto. I tasti [ e ] ciclano tra i punti AF o i volti al 100%. Il punto AF primario è verde, gli altri bianchi; il volto primario è giallo. — [Guida]
- **Punti AF**: Canon, Nikon, Fujifilm, Olympus e Sony. Volti rilevati dalla fotocamera: Canon, Fujifilm, Nikon, Panasonic, Pentax, Olympus e Sony. Se il file non contiene volti, un rilevamento su GPU si può attivare con un default nascosto da Terminale. — [Guida]
- **Schermo intero**: due modalità. Invio dà lo schermo intero senza pannelli; ⌃⌘F dà "App Full Screen" con le barre laterali. A queste si aggiungono Liquid Glass Mode (⌃⌘G), in cui la toolbar è trasparente sopra la foto, e Fluid Swipe (⌘S), uno scorrimento in stile iPhone disponibile solo con trackpad o Magic Mouse. — [Guida]
- **Istogramma**: Colori e Luminosità, con un riquadro dei valori RGB sotto il puntatore. Nell'edizione Pro c'è un istogramma HDR con regione log2 di 4 EV e un visualizzatore di sovraesposizione a 4 bande in falsi colori, una per EV. Gli avvisi di sovra e sottoesposizione si attivano dal menu Tools, per qualsiasi immagine dalla 3.7.1. — [Guida]
- **Gestione del colore**:
  - L'Inspector mostra il profilo colore (4.6.1).
  - Export SDR in sRGB, Display P3 o Adobe RGB (4.9.0).
  - Elaborazione in virgola mobile a 64 bit e supporto ai display a 10 bit (4.0.0).
  - HDR su schermi EDR/XDR; SDR Proof Mode (⌃⌘S); opzione "Apple Colors".

  [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- **Sharpen Displayed Image** (⇧⌘S, 4.1.0) e **Preview Actual Print Size** (4.1.0). — [Guida]

### Inferences
- L'architettura RAW è "anteprima incorporata o decodifica Apple su richiesta", molto vicina a quella di RawLine Selects. Il badge del decoder nel titolo è un'idea economica e utile per la diagnosi.
- I tasti [ e ] per ciclare i punti AF al 100% sono una funzione di culling forte e facile da copiare.

### Gaps
- Non ho trovato menzioni di più monitor o di un secondo schermo nella Guida (cercati "second screen", "dual", "external display").
- Non esiste una modalità "survival" o di eliminazione progressiva, né un confronto a griglia con più di due immagini: lo Split View è limitato a due.

## 3. Culling: valutazioni, etichette, Pick/Reject, scorciatoie, avanzamento automatico, confronto

### Takeaway
Il culling è classico e veloce, guidato dalla tastiera:
- da 1 a 5 stelle, 0 per togliere la valutazione, X per lo scarto (rating -1)
- \ per il Pick, dalla 4.1.0 di dicembre 2025
- da ⌥1 a ⌥7 per sette etichette colore che sono i tag del Finder
- avanzamento automatico con il tasto A o Caps Lock

Il confronto è uno Split View a due immagini con zoom sincronizzato. Il culling automatico vero e proprio arriva con Stacks, Focus Score e AI Rating nella 5.0.

### Cited Findings
- Scorciatoie di valutazione:
  - da 1 a 5 per le stelle, 0 per togliere la valutazione, X per lo scarto
  - \ per il Pick
  - da ⌥1 a ⌥7 per accendere e spegnere le etichette Red, Orange, Yellow, Green, Blue, Purple, Gray; ⌥0 le toglie tutte
  - la combinazione di più etichette è ammessa

  [Guida]
- Pick toggle "compatible with Lightroom CC" e filtro Pick introdotti nella 4.1.0 (12 dicembre 2025). Il pulsante Pick nella toolbar è arrivato con la 4.8.0. Le miniature scartate vengono attenuate dalla 4.3.1 (1 aprile 2026). — [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- **Auto Advance** (A o Caps Lock): passa al file successivo dopo una modifica del tag del Finder, delle stelle, "Move only RAW File to Trash" o dei dati GPS. La stessa modalità funziona per il tethering: mostra i nuovi scatti in una cartella osservata, per esempio con Fujifilm X-Acquire. — [Guida]
- Scorciatoie personalizzabili: per le etichette e le valutazioni dalla 3.7.3, poi per tutte le voci di menu (edizione Pro). — [Guida]
- **Split View** (⌥V, scambio ⌥W, sincronizzazione ⌥S):
  - due immagini o video affiancati, Tab per cambiare vista attiva
  - scroll e zoom sincronizzati quando entrambe le immagini sono ingrandite; ⌃Z e ⌃G zoomano entrambe al 100 e al 200%
  - si può valutare, taggare, cancellare e ritagliare in ognuna delle due viste

  [Guida]
- Le operazioni sui file filtrati (copia, sposta, cestino) si fanno dopo il filtro. "Move only RAW File to Trash" esiste come operazione a sé. — [Guida]
- **Valutazione su coppia RAW+JPEG**: in Display Mode "Combine JPEG+RAW", che è la modalità predefinita, il tag viene applicato anche al RAW. Per le stelle la Guida, in una sezione forse datata, dice che il RAW corrispondente non viene valutato. Le note su AI Rating della 5.0 dicono invece che la valutazione va "into both halves of a Combine JPEG+RAW pair". **Conflitto interno alla Guida**: probabilmente la sezione sulle stelle è vecchia. — [Guida]
- Le miniature della Contact Sheet mostrano i badge della coppia RAW+JPEG e gli indicatori GPS. — [Pagina prodotto](https://anogeissus.com/apolloone.html)
- Filtro "Selections on Contact Sheet" (N): restringe la vista alle foto selezionate, un modo rudimentale per isolare un sottoinsieme. C'è anche "Invert Current Filters". — [Guida]
- Nella prima recensione utente (App Store, 2021) la velocità e il culling sono lodati; un'altra recensione 2021 segnala lentezza con gli HEIC su condivisioni AFP. — [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12) (riportato dal fetch, recensioni utente)

### Inferences
- Il modello dati usa tre assi separati, cosa che RawLine può imitare: stelle con scarto a -1, Pick booleano, etichette colore multiple.

### Gaps
- La Guida non documenta un'opzione per avanzare dopo il Pick. Nella lista delle operazioni che fanno avanzare il Pick non compare.
- Nessuna modalità survival, confronto N-up o "loupe compare" su più di due immagini.

## 4. Stacks e raggruppamento (bursts, bracketing, coppie RAW+JPEG)

### Takeaway
Gli Stacks (Max, dalla 5.0.0 del 30 settembre 2026) raggruppano solo per **intervallo di tempo** di scatto, regolabile da 1 a 60 secondi, oppure a mano. Non ci sono criteri EXIF di bracketing, né somiglianza visiva, né AI. Il salvataggio avviene in un extended attribute su ogni file, senza catalogo. Le coppie RAW+JPEG sono un meccanismo separato (Display Mode). C'è poi "AI Key Photo", che sceglie la foto rappresentativa unendo Focus Score e AI Rating.

### Cited Findings
- Auto-Stack (⌥⌘U): "group images by the time they were taken". Lo slider fissa lo stacco massimo tra due fotogrammi dello stesso stack, da 1 a 60 secondi; "Two seconds suits most continuous shooting". — [Guida]
- Ambito: la selezione oppure l'intera cartella. Un'etichetta mostra l'esito in diretta ("212 images → 14 stacks") e la Contact Sheet si ri-raggruppa mentre si trascina lo slider. Nulla viene scritto prima di "Apply". — [Guida]
- Considera solo le immagini con data di scatto che non sono già in uno stack. Gli stack manuali non vengono mai toccati e una seconda esecuzione raggruppa solo ciò che è rimasto sciolto. La key photo è il primo fotogramma. — [Guida]
- Stack manuale con "Stack Selection" (⌘U): la key photo è la prima immagine nell'ordinamento corrente. Tutte le immagini devono stare nella stessa cartella. Si possono aggiungere immagini trascinandole su una pila e unire due pile trascinandone una sull'altra. — [Guida]
- Aspetto della pila chiusa: la key photo su una cornice bianca, i fotogrammi successivi inclinati dietro e un contatore "×12". Uno stack con nome mostra il nome prima del contatore ("Kingfisher ×41"). La valutazione, l'etichetta e i badge della pila sono quelli della key photo. — [Guida]
- Comandi:
  - Open Stack (⌘↓) e Close Stack (⌘↑ o Esc)
  - Set Key Photo (⌘\), Promote (⇧⌘\) e Demote (⌥⌘\)
  - Split Stack, Extract Item, Unstack (⇧⌘U), Unstack All, Rename Stack
  - riordino trascinando le miniature
  - "Show Stacks Expanded" per tab, con il pulsante della toolbar che diventa giallo

  [Guida]
- Dentro uno stack aperto il titolo della finestra mostra "· Stack ×12" e l'ordine è quello proprio dello stack, a meno di scegliere un ordinamento (per esempio per Focus Score, il più nitido per primo). Chiudendo l'app con uno stack aperto, al riavvio si torna allo stesso punto. — [Guida]
- Le azioni su una pila chiusa agiscono solo sulla key photo. Fa eccezione la cancellazione: una finestra di dialogo propone "Delete Key Photo Only", "Delete All 12" o "Cancel", anche quando la conferma del cestino è disattivata. — [Guida]
- I filtri agiscono sulle singole immagini. Una pila filtrata in parte mostra quante immagini sono sopravvissute e, se la key photo è esclusa, la rappresenta la prima rimasta. — [Guida]
- Salvataggio: un extended attribute su ogni file, quindi rinomina, spostamento e copia nel Finder conservano lo stack; la sincronizzazione tra Mac passa da iCloud Drive. Sui volumi non macOS (schede) finisce nei file nascosti AppleDouble (._). Senza Max le immagini compaiono singole e gli stack restano intatti. — [Guida]
- Un export nella stessa cartella entra nello stack del file sorgente, subito dopo, senza mai diventare la key photo. — [Guida]
- **AI Key Photo**: sugli stack chiusi, calcola prima il Focus Score se manca, poi manda a Private Cloud Compute fino a 10 foto, le più nitide sopra una soglia scelta. La migliore diventa la key photo: più stelle, e a parità il Focus Score più alto. Non scrive valutazioni ed è reversibile con "Revert AI Ratings". — [Guida]
- ApolloOne GO 1.3.0 (1 ottobre 2026) ha portato gli Stacks su iOS, il Pick/Reject sulle coppie RAW+JPEG e il filtro "Picked + Unmarked". — [Blog](https://anogeissus.com/blog.html)
- Coppie RAW+JPEG: Display Mode "Combine JPEG+RAW" (⌘J, predefinita), "RAW Only" (⌘L), "Files other than RAW" (⌘K), "All Files" (⌘;). C'è anche un'opzione per cercare i RAW in una sottocartella separata (per esempio "Evento/RAW"). — [Guida]
- Live Photo: l'immagine e il MOV con lo stesso nome sono trattati come un solo file con badge LIVE. — [Guida]

### Inferences
- Il raggruppamento è volutamente semplice: solo il tempo. Bracketing, HDR e panorami vengono "presi" solo se scattati entro N secondi. Per RawLine c'è spazio per distinguersi con criteri EXIF (per esempio la sequenza di esposizione o il bracket) o con la somiglianza visiva (Vision feature print).
- L'anteprima dal vivo durante il trascinamento dello slider e la conferma speciale "delete all N" sono dettagli di interfaccia da copiare.

### Gaps
- Non ci sono criteri basati su bracketing EXIF, somiglianza visiva o AI per formare gli stack: non sono documentati e la Guida parla solo del tempo.
- Non si sa se Auto-Stack usi i sottosecondi EXIF (SubSecTimeOriginal).

## 5. Funzioni AI: Focus Score, AI Rating, AI Keywords, volti

### Takeaway
- **Focus Score** gira in locale e misura la nitidezza da 1 a 100 *solo dentro le aree AF registrate*. Sui volti usa Vision, renderizza i RAW senza nitidezza, corregge per la diffrazione e per gli ISO alti.
- **AI Rating** e **AI Keywords** girano su Apple Private Cloud Compute, con Foundation Models e Apple Intelligence: macOS 27, Apple silicon, iCloud e un limite giornaliero.
- L'AI non imposta mai lo scarto.

### Cited Findings
- **Focus Score**:
  - Funzionamento: Tools > Process Focus Scores (⌥⌘S); elabora tutta la cartella del tab in background mentre si continua a lavorare; lo stesso tasto annulla.
  - Badge: una pillola blu sulla miniatura e una colonna nella List View.
  - Bande del filtro: 0–30, 31–60, 61–70, 71–80, 81–90, 91–94, 95–98, 99–100, più una riga "Unranked".
  - Ordinamento: Sort > Focus Score.

  [Guida]
- Metodo del Focus Score:
  - Misura alla risoluzione piena dentro le aree AF registrate dalla fotocamera. Quando un'area AF cade su un volto, il volto viene trovato con "neural network vision processing" e giudicato su occhi, ciglia e capelli.
  - I punteggi sono assoluti, non relativi alla cartella.
  - Ogni RAW viene renderizzato senza nitidezza nella sola area di fuoco. Sopra ISO 6400 c'è un secondo render con la riduzione rumore al massimo. Sopra ISO 10000 la foto va in "Unranked", salvo con il decoder ML Apple.
  - Il tetto del punteggio si abbassa per la diffrazione in base al diaframma e al passo del pixel: circa f/17 per il full frame a pixel grandi, f/15 per l'alta risoluzione, f/13 per il Micro Quattro Terzi.
  - Una coppia RAW+JPEG ha un solo punteggio, misurato sul RAW.

  [Guida]
- Salvataggio del Focus Score: per impostazione predefinita solo in memoria, per tab. Con "Save Focus Scores" va in un extended attribute per file e si ricalcola se il file cambia. La Guida consiglia di rielaborare dopo un aggiornamento importante di macOS. — [Guida]
- Limiti dichiarati: con l'area AF fissa al centro e un soggetto che si muove, il punteggio descrive il centro. Gli export di convertitori terzi danno punteggi diversi. Le cartelle che mescolano RAW e JPEG vanno confrontate con cautela. — [Guida]
- **AI Rating**:
  - Scala 1–5: 5 da stampare o pubblicare, 4 da condividere, 3 competente, 2 debole, 1 nulla da segnalare.
  - Criteri: luce, colore, composizione, leggibilità del soggetto, momento ed espressione.
  - "Sharpness never lowers a rating". Un Focus Score di 90 o più alza un 4 o un 5 dell'AI a 5 stelle.
  - Conserva fino a tre motivazioni e il conteggio dei volti, per esempio "8 faces, 2 with closed eyes".
  - Circa 300 foto in 3 minuti, quattro alla volta.

  [Guida], [Pagina prodotto](https://anogeissus.com/apolloone.html)
- Opzioni di AI Rating:
  - Focus Score minimo per l'invio (50, 60, 70, 80 o 90)
  - genere (General, Wildlife, Birds, Plants & Flowers, Landscape & Travel, Wedding & Events, People, Food)
  - prompt modificabile e salvabile in Documents/ApolloOne/prompts/rating
  - salto delle foto già valutate, gestione degli stack (valuta da 1 a 5 foto in cima per stack, al massimo 10 richieste per burst), salvataggio delle motivazioni in un extended attribute
  - "Revert AI Ratings", anche tra sessioni diverse

  [Guida]
- Privacy: a Private Cloud Compute va una copia ridotta a 1024 px sul lato lungo. Requisiti: macOS 27, Apple silicon, Apple Intelligence attivo, Mac collegato a iCloud, lingua del Mac uguale a quella di Siri, limite giornaliero per account iCloud. — [Guida]
- "The reject flag is never set by AI Rating": una foto con gli occhi chiusi riceve un voto più basso e una motivazione, ma resta nella cartella. — [Guida]
- **AI Keywords**: propone soggetto, specie con nome comune, luogo o monumento, piatto e fino a dieci keyword. Usa il GPS per aiutare a distinguere specie simili, accetta un campo "Region", ha preset per genere e la lingua scegliibile. Non scrive nulla finché l'utente non applica. Per uno stack chiuso invia solo la key photo e applica le keyword a tutto lo stack. Le colonne nella List View sono AI Keywords, Species e Keywords. — [Guida]
- Altre funzioni "AI": AI Image Metadata (4.4.0) legge i parametri di generazione di ComfyUI, A1111, Midjourney e NovelAI. Esiste una pagina di supporto "Keyword with Claude AI (free scripts)". — [Guida], [Supporto](https://anogeissus.com/support.html)

### Inferences
- Il Focus Score ancorato ai punti AF è un'implementazione concreta e documentata di cui RawLine Selects ha già i prerequisiti (lettura AF e decodifica Apple). Le regole su ISO e diffrazione sono un buon punto di partenza tecnico.
- La parte AI estetica dipende dal cloud Apple e da macOS 27. Un'alternativa sul dispositivo (Vision: occhi aperti, volti, aesthetics score) potrebbe essere un vantaggio competitivo.

### Gaps
- L'algoritmo esatto di misura della nitidezza (Laplaciano, FFT, CNN) non è dichiarato.
- Il rilevamento degli occhi chiusi non è un filtro dedicato: compare solo nelle motivazioni di AI Rating.
- Non c'è ricerca semantica per oggetti o scene, oltre alle keyword proposte.

## 6. Metadati: XMP, IPTC, sidecar, compatibilità, keyword, GPS

### Takeaway
Ci sono tre modalità di "Metadata Source": solo extended attributes e tag del Finder, solo XMP/IPTC, oppure entrambe. Per RAW e video le valutazioni vanno in sidecar .xmp, tranne i DNG, dove vanno nel file. Le etichette sono mappate su XMP:Label, limitate a cinque colori in modalità XMP. Le keyword gerarchiche sono compatibili con Lightroom e Photo Mechanic, e i file di code replacement di Photo Mechanic si usano senza modifiche.

### Cited Findings
- Le tre fonti dei metadati:
  - "Use macOS Extended Attributes" (predefinita, per la ricerca nel Finder): il file non viene mai toccato
  - "Use XMP / IPTC": solo cinque colori XMP:Label (Red, Yellow, Green, Blue, Purple), Orange e Gray nascosti; XMP:Rating da -1 a 5
  - "Combine both settings": in caso di conflitto i tag XMP/IPTC non vuoti prevalgono sugli extended attributes

  [Guida]
- Scrittura in parallelo: modificare le keyword aggiorna insieme IPTC:Keywords, XMP-dc:Subject e l'extended attribute; il commento aggiorna XMP:UserComment. — [Guida]
- Le stelle vanno in XMP Rating. Per RAW e video viene creato un sidecar XMP, o aggiornato se esiste già; per i DNG la scrittura è diretta nel file. Il Pick va in un extended attribute e/o nel sidecar XMP, a seconda dell'impostazione. — [Guida]
- Le etichette sono tag del Finder (7 colori), con sincronizzazione dei nomi personalizzati del Finder e label personalizzate. — [Guida]
- Pannello IPTC Core ed Extension completo, inclusi i campi per il badge "Licensable" di Google Images. Inspector EXIF, GPS e lenti con ricerca; doppio clic per modificare; template di metadati da file .xmp; Creator e Copyright all'import; "Preserve original filename in XMP" (XMP:OriginalDocumentID). — [Pagina prodotto](https://anogeissus.com/apolloone.html), [Guida]
- Keyword gerarchiche (Max): albero con sinonimi e categorie, "read by Lightroom and Photo Mechanic"; applicare un ramo fa trovare anche i termini genitori. Code Replacements (per esempio `=ny=`) nei metadati e nelle regole di rinomina, con "Photo Mechanic code replacement files work unchanged". Variabili come {filename} e la data di scatto. — [Guida], [Pagina prodotto](https://anogeissus.com/apolloone.html)
- Motori inclusi: ExifTool (aggiornato spesso, per esempio v13.43 nella 4.1.0), MediaInfo e LibRaw 0.22.0 (4.3.0). — [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- GPS e mappe: Apple Maps o Google Maps (con Street View); il marker si trascina per correggere la posizione; scrittura e cancellazione dei dati GPS; filtro per distanza GPS (formula di Vincenty) e per altitudine; misura della distanza tra due immagini. — [Guida], [Pagina prodotto](https://anogeissus.com/apolloone.html)
- AppleScript (Max): lettura e scrittura dei metadati sulla selezione. Stelle, etichetta e Pick sono di sola lettura da script. — [Guida]

### Inferences
- La scelta "extended attributes come predefinito, XMP opzionale" è un'impostazione centrata su macOS. Per l'interoperabilità con Lightroom conta la modalità XMP o quella combinata.

### Gaps
- Non è specificato se il Pick sia scritto in un campo XMP standard (per esempio xmpDM:pick o un campo Lightroom). La Guida dice solo "compatible with Lightroom CC".
- Compatibilità con Capture One: non menzionata.

## 7. Ricerca, filtri, smart folder, ordinamento

### Takeaway
I filtri si combinano: i gruppi dell'Inspector (etichette, stelle, keyword, Pick, Focus Score) e i filtri del menu (in AND tra loro). La ricerca nella toolbar copre nome, cartella o metadati, con wildcard e regex. Le smart folder sono quelle del Finder. Non ci sono collezioni intelligenti proprie.

### Cited Findings
- Filtri del menu:
  - per tipi di file, Quick Edit, Pick / senza Pick
  - per etichette (quelle correnti, una qualsiasi, nessuna)
  - per stelle (uguale o maggiore, corrente, una qualsiasi, nessuna)
  - senza keyword, con o senza GPS, distanza GPS, altitudine GPS
  - "Selections on Contact Sheet", inversione, spegnimento di tutti i filtri
  - quick rating filter con ⌘⌥numero, per "quel numero di stelle e oltre"

  [Guida]
- Ricerca nella toolbar per nome file, nome cartella o metadati: la virgola vale OR, il + vale AND, ? e * dalla 4.1.0. Il filtro sui metadati con regex è nell'edizione Pro. — [Guida]
- Ordinamenti: per Focus Score, personalizzato con due chiavi, User Defined Sequence (trascinando, salvato in .plist), casuale, mantenuto per cartella; ordinamento della List View cliccando sulle colonne. La 4.7.0 ha aggiunto il raggruppamento per cartella nella Contact Sheet. — [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- Smart folder: si appoggia alle ricerche salvate del Finder (~/Library/Saved Searches) aggiunte a Places. — [Guida]
- Tab (Standard, dalla 5.0): ogni tab ha cartella, selezione, filtri, ordinamento e modalità di visualizzazione propri, e può essere trascinato fuori in una nuova finestra. — [Pagina prodotto](https://anogeissus.com/apolloone.html)

### Inferences
- Le bande non lineari del Focus Score, strette in cima alla scala, sono una scelta progettuale ben motivata e copiabile.

### Gaps
- Nessuna collezione intelligente interna salvabile.

## 8. Operazioni sui file: import da scheda, copia/sposta/rinomina/cancella, export, batch, condivisione

### Takeaway
L'import da scheda è completo: ripresa dall'ultimo file, sottocartelle per data, rinomina con template, metadati, backup su una seconda destinazione, filtro con i Pick fatti su iPhone in ApolloOne GO. A questo si aggiungono batch rename, resize e convert, InstaBake ed export HDR.

### Cited Findings
- Import (File > Import Files…):
  - Si sceglie la scheda e il primo file; vengono copiati tutti i file più recenti di quello.
  - Ripresa dall'ultimo import della stessa scheda, con ripresa automatica nell'edizione Pro.
  - Opzioni: "Do not import files after" una data; inclusione di JPEG, HEIF, TIFF, RAW e video; sovrascrittura o rinomina dei duplicati; suono a fine import; espulsione della scheda; cancellazione degli originali (nel Cestino).
  - Sottocartelle per data da EXIF, nel formato scelto (per esempio YYMMDD); rinomina con testo più sequenza a 4 cifre o con template.
  - "Backup to:" (5.0, Pro); import fino a 2 volte più veloce (5.0).

  [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- Integrazione con ApolloOne GO (4.7.0, 22 luglio 2026):
  - su iPhone o iPad si fanno Pick e Reject, scritti come tag verde e rosso del Finder via iCloud Drive
  - all'import sul Mac si sceglie tra "Import All Files", "Import Files Picked in ApolloOne GO" e "Import All Except Rejected"
  - il verde diventa Picked e il rosso Reject (-1); "Your memory card is never modified"

  [Guida], [GO](https://anogeissus.com/apolloone-go.html)
- "Import from the Current File…" parte dal file selezionato sulla scheda. — [Guida]
- Cestino: "Undo Move to Trash" finché l'app è aperta, più un'opzione per abilitare "Put Back". — [Guida]
- Batch rename (Standard); batch resize e conversione, copia o spostamento con ridimensionamento, batch export, cioè da RAW a JPEG (Pro). — [Guida], [FAQ](https://anogeissus.com/apolloone-faq.html)
- Export: JPEG, HEIC, PNG, WebP, TIFF, AVIF, JPEG XL; HDR in JPEG XL, AVIF, gain map JPEG/HEIC e OpenEXR (4.4.0, 20 aprile 2026), con metadati completi (Exif, IPTC, XMP, GPS, MakerNotes). InstaBake applica le Quick Edit in JPEG via AirDrop o trascinamento. — [Guida]
- Quick Edit non distruttivo: esposizione, alte luci, ombre, temperatura, tinta, contrasto, saturazione, vividezza, maschera di contrasto; Dehaze dalla 5.1.0. I parametri sono sincronizzati con Camera RawX per Quick Look. Correzione automatica delle lenti (4.6.0, 19 giugno 2026). — [Pagina prodotto](https://anogeissus.com/apolloone.html), [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- Editor esterno con ⌘E e menu separati per immagini, RAW e video. Folder monitor: aggiorna in automatico quando i file cambiano. — [Guida]

### Inferences
- Il flusso "culling sul telefono, import solo dei Pick sul Mac" basato sui tag del Finder è un'idea interessante per un ecosistema RawLine.

### Gaps
- Nessuna funzione di condivisione oltre ad AirDrop e al foglio di condivisione di sistema.

## 9. Video, Live Photo e altri formati

### Takeaway
L'app è un viewer multimediale ampio: video fotogramma per fotogramma con sottotitoli SRT, Live Photo, memo vocali della fotocamera, file .afphoto e .pxd, AVIF, SVG, WebP, OpenEXR.

### Cited Findings
- Video: le frecce avanzano fotogramma per fotogramma; sottotitoli SRT (UTF-8, stesso nome del video); opzione per saltare la riproduzione navigando con le frecce (4.0.0). — [Guida]
- Live Photo: riproduzione passando il mouse sul badge LIVE o tenendo premuto K. — [Guida]
- Memo vocali della fotocamera (WAV con lo stesso nome), con ⌘V. — [Guida]
- Miniature dei file Affinity Photo (.afphoto) e Pixelmator (.pxd). — [Guida]
- Supporto AVIF e SVG (4.3.0); WebP e OpenEXR (4.4.0); Olympus Pixel Shift (4.5.1); oltre 40 formati di fotocamera tramite RawBridge. — [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12), [Pagina prodotto](https://anogeissus.com/apolloone.html)
- Slideshow (F5) con musica da Apple Music, registrazione in video, slideshow HDR. — [Guida]

### Inferences
- La gamma di formati è molto più ampia di quella di un'app pura da culling. Per RawLine Selects non è prioritaria.

### Gaps
- L'elenco completo dei codec video supportati non è riportato. La Guida rimanda a MediaInfo e AVFoundation.

## 10. Prestazioni, impostazioni e personalizzazione

### Takeaway
La velocità è il cuore del marketing: niente database, cache adattiva, fino a 55 fps a piena risoluzione su M1 Ultra. L'interfaccia è molto personalizzabile: scorciatoie, voci di menu nascoste, toolbar, status bar, Liquid Glass, tab.

### Cited Findings
- "No database imports", e si naviga direttamente nelle cartelle con Places (le cartelle con permesso sandbox). — [Pagina prodotto](https://anogeissus.com/apolloone.html), [Guida]
- La raccolta delle proprietà per ordinamento e filtri avviene in background: una rotella in Places la segnala, e ordinamento e filtri si attivano a raccolta finita. Le colonne della List View compaiono un momento dopo le righe sulle cartelle RAW grandi. — [Guida]
- Personalizzazione: scorciatoie per ogni voce di menu (tasti riservati: frecce, spazio, ⌥frecce, ⌘[ e ⌘]); voci o menu interi nascosti, con la scorciatoia che sparisce insieme (5.0); toolbar personalizzabile; status bar trascinabile (Max); Browser come barra laterale o fluttuante; procedura di primo avvio (4.9.0); "Reopen last file on startup"; impostazioni nascoste tramite Terminale ("Special User Defaults"). — [Guida], [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- Un tab fuori schermo smette di disegnare e mette in pausa i video. — [Guida]
- Problemi noti dichiarati: blocchi con NAS su AFP in Monterey e Ventura (consigliato SMB); un crash all'avvio su macOS 14–15 corretto nella 5.0.1. — [FAQ](https://anogeissus.com/apolloone-faq.html), [Blog](https://anogeissus.com/blog.html)

### Inferences
- Il ritmo di rilascio è altissimo: circa 25 versioni tra novembre 2025 e ottobre 2026, spesso a distanza di una o due settimane. Lo sviluppatore è molto attivo, ma le funzioni Max sono recenti (poco più di un mese) e poco collaudate dal pubblico.

### Gaps
- Non ci sono benchmark indipendenti sulla velocità di apertura delle cartelle. Il dato "55 fps" è solo dello sviluppatore.
- Recensioni indipendenti di fotografi: non ne ho trovate di sostanziali. I confronti trovati sono di concorrenti AI (Aftershoot, FilterPixel), quindi di parte. Il thread DPReview "ApolloOne v4 and Camera RawX v2" (https://www.dpreview.com/forums/threads/apolloone-v4-and-camera-rawx-v2.4815583) ha risposto 403 e non l'ho potuto leggere.
