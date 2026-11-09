# RawLine Selects: ricerca e proposta di prodotto

Data: 2026-11-08, aggiornata il 2026-11-09 con il rapporto [[Mercato culling fotografico]] (in `reports/`). Seconda app della famiglia RawLine, dopo [[RawLine Rename]]. È un'app indipendente per la selezione delle foto (culling). Più avanti confluirà nella modalità **Seleziona** di [[RawLine]], l'app completa: il motore va scritto in RawlineKit fin dal primo giorno, come per Rename.

Obiettivo: la selezione più rapida e affidabile sul mercato. Deve essere veloce come Photo Mechanic, moderna e pulita come RawLine Rename, avere l'aiuto intelligente delle app AI ma lavorare tutta in locale, e scrivere metadati che Lightroom, Bridge e Capture One leggono senza sorprese.

## 0. Decisioni prese (8 novembre 2026)

- **Si sviluppa tutto**, fase per fase, fino alla versione completa descritta qui.
- **Beta gratuita**, come RawLine Rename.
- **Fuori dall'App Store**, come RawLine Rename: firma Developer ID, notarizzazione, aggiornamenti con Sparkle.
- **Stesso sito**, rawline.app. La pagina di download offrirà la scelta tra RawLine Rename e RawLine Selects.
- **Una famiglia di app separate.** Ogni pezzo (Selects, Rename, poi copyright e metadati, importazione…) nasce e matura come app a sé, in beta. Quando saranno pronte confluiranno in **RawLine**, l'app unica a pagamento. Le app singole potranno restare gratuite, con funzioni ridotte.
- **Coerenza:** Selects deve sembrare nata dalla stessa testa di Rename: stessa grafica, stessi gesti, stesse parole. Vedi la sezione 11.
- **Punto di partenza:** il modo di lavorare di Photo Mechanic, che Andrea usa e apprezza. Non va snaturato, va migliorato. Vedi la sezione 12.
- **Tutte le marche (9 nov).** Selects deve funzionare con ogni fotocamera sul mercato (Canon, Nikon, Fujifilm, Panasonic, OM System, Pentax, Leica, Hasselblad, Phase One, Sigma, droni e smartphone), non solo con la Sony di Andrea. La Sony A1 resta il banco di prova personale, non il limite del prodotto.

---

## 1. Il mercato in breve

Oggi il mercato si divide in due campi, e nessuno li unisce bene.

| Campo | App | Punto di forza | Punto debole |
|---|---|---|---|
| **Velocità manuale** | Photo Mechanic, FastRawViewer, Bridge | Anteprime istantanee, tastiera, nessuna attesa | Niente aiuto intelligente; interfacce vecchie (PM, Bridge) o molto tecniche (FRV) |
| **AI** | Aftershoot, FilterPixel, Narrative Select, Imagen, Lightroom (Assisted Culling), Excire, imagic, ON1 | Raggruppa le raffiche, segnala occhi chiusi e mosso, propone la migliore | Quasi tutte in abbonamento (circa $10–60 al mese), analisi da aspettare prima di iniziare, a volte cloud, poco affidabili su sport, natura e momenti emotivi |
| **Dentro l'editor** | Lightroom Classic, Capture One (Cull) | Già nel flusso di sviluppo | Lenti sui RAW (Lightroom deve creare le anteprime), funzioni di culling limitate |

### Le app una per una

| App | Cosa fa meglio | Cosa le manca | Prezzo indicativo |
|---|---|---|---|
| **Photo Mechanic** (Camera Bits, build 2026.6 del 18 giugno 2026) | Lo standard della velocità: mostra il JPEG incorporato nel RAW. Otto classi colore con tasti numerici, Tag, avanzamento automatico, scorciatoie personalizzabili, selezione direttamente sulla scheda | Nessuna AI; interfaccia datata; niente punto AF e niente raffiche; le novità 2026 sono per le agenzie (upload, IPTC, AVIF, JPEG XL) | Standard $14,99/mese, $149/anno o $299 perpetua; Plus (con catalogo) $24,99/mese, $249/anno o $399 perpetua. La perpetua include un anno di aggiornamenti |
| **FastRawViewer** (2.0.11) | Istogramma RAW vero, sovra/sottoesposizione sui dati RAW, focus peaking, confronto 2–4 con zoom sincronizzato | Interfaccia da strumento tecnico; **rifiuta per principio di mostrare il punto AF** (dati non documentati), nonostante le richieste degli utenti; Nikon HE solo dalla 2.0.9 | $23,99 una tantum, due computer |
| **Adobe Bridge** | Gratuito, Review mode, loupe su più foto | Confronto affiancato debole, zoom 100% scomodo; etichette colore scritte in modo che Lightroom a volte non legge | Gratis con account Adobe |
| **Lightroom Classic** (15.x) | Assisted Culling locale (dalla 15.0, ottobre 2025): fuoco sul soggetto, fuoco e apertura degli occhi per ogni volto (pannello volti dalla 15.4, giugno 2026), duplicati e pile per somiglianza | Va importato tutto nel catalogo; circa 0,7 s per foto anche su M2 Pro; punteggi che cambiano tra un'analisi e l'altra; niente raffiche ordinate. I flag Scelta/Scarto **passano dall'XMP dalla 13.2** (`xmpDM:pick`) | Abbonamento Adobe |
| **Capture One Cull** | Usa le anteprime incorporate, vista a gruppi, Face Focus (zoom sui volti, dalla 16.2) | Scorciatoie limitate in modalità Cull, zoom massimo 100%, niente eliminazione diretta, nessuna AI di selezione | Abbonamento o licenza |
| **Adobe Camera Raw** (18.4.1, 2026) | "Show Autofocus Points" per Canon, Nikon e Sony | Sui file Sony spesso non mostra nulla, e non dice perché; segnalati fallimenti anche su Nikon D850/D500 | Con Adobe |
| **ApolloOne** (5.1, ottobre 2025) | Il concorrente Mac più vicino: confronto sincronizzato, pile, punteggio di fuoco, volti, video, punto AF a rotazione; legge corpi nuovi prima di Apple con un suo "RawBridge" | Punto AF sull'A1 da verificare; interfaccia da visualizzatore generico | $35,99–99,99 o abbonamento |
| **Narrative Select** | Scene (foto dello stesso momento raggruppate e ordinate da "migliore" a "da scartare"), pannello primi piani dei volti, valutazione di occhi e fuoco, gira in locale | **Piano gratuito eliminato**; Scene e primi piani solo da Standard in su; pensato per i matrimoni; i corpi nuovi richiedono un aggiornamento dell'app | Lite $15/mese ($10 annuale), Standard $29/$20, Premium $59/$40, Ultra $79/$60; prova di 30 giorni |
| **Aftershoot** | Dal 2026 una suite: selezione, sviluppo RAW, gallerie; "seleziona fino a N foto"; distingue "AI Automated" da "AI Assisted"; gira in locale | Abbonamento; velocità legata alla scheda grafica; "sicura di sé e sbagliata" abbastanza spesso da contare (Fstoppers) | Select $15/mese ($10 annuale); suite completa $55/$45 |
| **Imagen** | Profilo personale | Selezione nel cloud; il profilo richiede 2.000–3.000 foto già sviluppate | $18/mese ($12 annuale) |
| **FilterPixel** | Molto rapida nella prima passata AI, spiega ogni punteggio | Quote per servizio; **le miniature possono finire sui loro server** per addestrare l'AI se non si spegne l'opzione | Da $14,99/mese (20 servizi l'anno), Pro $34,99, Studio $64,99 |
| **Excire Foto 2027, imagic, ON1 Photo RAW 2027** | Il ritorno della licenza una tantum, con selezione AI in locale (Excire, imagic) | Selezione appena aggiunta (Excire, ottobre 2026; ON1, novembre 2026); ON1 non dice se lavora in locale | Excire $249; imagic €19–99 |
| **Nuove app Mac del 2025–2026** (Palomino, Photo Cull Pro, PickShot, PhotoCuller, Phiewer Select, FaceCull, BurstPick e altre) | Native, veloci; Palomino segna il fotogramma più nitido della raffica e zooma sul volto; molte inseguono la "più nitida della raffica" | Piccole, giovani; diverse fanno pagare l'esportazione XMP. "RawCull" sono due prodotti diversi: uno solo per A1, l'altro dieci marche con dcraw | $0–89, spesso una tantum |

Nota sulle fonti: molti confronti online sono scritti dai concorrenti stessi (Imagen, Aftershoot, FilterPixel, Narrative). Ho preso per buone le funzioni descritte nella documentazione ufficiale e ho trattato con cautela classifiche e percentuali di precisione.

### Il vuoto che RawLine Selects può occupare

Nessuna app oggi mette insieme tutte queste cose:

1. **La velocità di Photo Mechanic** (anteprima incorporata, zero attese).
2. **Un'interfaccia moderna e sobria**, come RawLine Rename.
3. **Selezione manuale velocissima, aiutata da AI in locale che non giudica**: lo zoom segue il soggetto, i volti si controllano in un colpo d'occhio, le raffiche si raggruppano da sole. Niente cloud, niente attese, foto mai caricate online.
4. **Il punto AF della fotocamera sulla foto, su ogni marca, e lo zoom che parte da lì**: si vede subito se è a fuoco dove la fotocamera ha messo a fuoco. Adobe Camera Raw e ApolloOne ci provano, ma falliscono in silenzio su molti corpi; FastRawViewer si rifiuta. Selects lo fa con un elenco pubblico dei corpi verificati e dice chiaramente "AF non disponibile per questo corpo".
5. **Video e foto nella stessa selezione**: valutare anche le clip, con scorrimento J-K-L. ApolloOne e Photo Mechanic riproducono i video, ma nessuno **seleziona** foto e clip nello stesso flusso.
6. **Metadati che non si rompono**: etichette colore compatibili con Lightroom, Bridge e Capture One, e sidecar XMP aggiornati senza toccare le regolazioni di Lightroom.
7. **Licenza una tantum.** Contro gli abbonamenti dei concorrenti AI resta un argomento, ma a fine 2026 è tornata anche da altri (Excire, imagic, Palomino): da sola non basta più.
8. **Tutte le marche, con onestà.** Anteprime incorporate lette per ogni formato, e un cartello chiaro quando l'anteprima è piccola ("solo anteprima incorporata, 1920 px") o il RAW non è ancora leggibile da macOS.
9. **Velocità misurata in pubblico**, per marca, contro Lightroom (circa 0,7 s per foto) e Photo Mechanic. Nessun concorrente pubblica numeri indipendenti.

Il terreno è cambiato nel 2026: Lightroom regala ormai i controlli tecnici (occhi, fuoco, duplicati), quindi "rileviamo gli occhi chiusi" non distingue più nessuno. Contano velocità, fuoco onesto su ogni marca e metadati che non si perdono.

---

## 2. Principi

- **Istantanea, sempre.** Passare alla foto successiva non deve mai mostrare uno sfocato o una rotella. Se una foto non è pronta, l'app ha sbagliato a prevedere: è un bug.
- **Mai un dato perso.** Ogni valutazione viene salvata subito su disco, anche se l'app si chiude di colpo.
- **I RAW non si toccano mai.** Si scrive solo nel sidecar XMP, oppure dentro JPEG, HEIF e DNG se l'utente lo sceglie.
- **Il fotografo decide, sempre.** L'AI locale decide solo dove guardare (zoom, volti, raffiche), mai cosa tenere (5.1).
- **Una mano sola.** Le operazioni comuni stanno sotto la mano sinistra. Il mouse resta facoltativo.
- **Compatibile con tutti.** Quello che scrive Selects si legge in Lightroom, Bridge, Capture One e Photo Mechanic.
- **Sobria.** Stessa palette di Rename: accento grafite, la foto al centro, interfaccia che sparisce.

---

## 3. Obiettivi di velocità (misurabili)

Sono i numeri da misurare a ogni build, su una cartella di prova di 2.000 ARW della Sony Alpha 1 **e sulla raccolta di file di prova per marca** (`~/Developer/Rawline/samples`, scaricata con `scripts/fetch-samples.sh` da raw.pixls.us: 27 RAW di 13 marche).

| Momento | Obiettivo |
|---|---|
| Apertura di una cartella da 2.000 file: griglia visibile | sotto 1 secondo (prime miniature), tutta la cartella in pochi secondi |
| Foto successiva a schermo intero, già precaricata | sotto 16 ms (un fotogramma a 60 Hz) |
| Foto successiva tenendo premuta la freccia | nessun fotogramma saltato |
| Zoom al 100% | sotto 50 ms |
| Assegnare stella, colore o scarto | risposta visiva immediata; scrittura su disco in sottofondo |
| Analisi AI (volti, occhi, nitidezza, raffiche) | in sottofondo, mentre si lavora; mai un'attesa prima di iniziare |

### Come si ottiene

- **Anteprima incorporata, letta in modo chirurgico, per ogni marca.** Lettori propri trovano la posizione del JPEG incorporato e leggono solo quei byte, senza aprire il file intero. È anche ciò che rende Selects indipendente dal ritardo di Apple sui corpi nuovi:
  - struttura TIFF: Sony ARW, Nikon NEF (anche HE), Canon CR2, Pentax PEF, DNG, 3FR; con le varianti Panasonic RW2 (JpgFromRaw) e Olympus/OM ORF (anteprima nelle MakerNotes);
  - contenitore a scatole: Canon CR3 (JPEG pieno nella traccia 1, più l'anteprima 1620×1080);
  - intestazione propria: Fujifilm RAF;
  - poi ripiego su ImageIO e sull'anteprima di `CIRAWFilter`: **nessun file resta mai senza immagine**.
  - Le anteprime hanno dimensioni molto diverse tra le marche: piene su Sony recenti, Canon CR3 e Nikon Z; circa 1920 px su molte Fujifilm; medie su Panasonic e OM; piccole su medio formato e droni. Per ogni file si salva la dimensione dell'anteprima rispetto al sensore (sezione 4.3).
- **Decodifica JPEG accelerata** e visualizzazione con Metal: lo zoom e il trascinamento girano sulla scheda grafica.
- **Decodifica commisurata allo schermo, leggera per il Mac** (deciso con Andrea il 9 novembre):
  - si decodifica solo quanto lo schermo può mostrare: il lato lungo dello schermo su cui sta la finestra, in pixel veri (per esempio 3456 sul MacBook Pro 16", 2560 sul BenQ 2K, 3840 sul 4K); se sposti la finestra su un altro schermo, la misura cambia (fatto il 9 novembre in SelectsLab: su uno schermo più grande le foto si rifanno alla nuova misura, su uno più piccolo bastano quelle già pronte; con la finestra a cavallo vale lo schermo che ne contiene la parte più grande);
  - il JPEG si decodifica già ridotto (a metà, a un quarto) quando basta, invece di aprirlo intero e rimpicciolirlo;
  - il lavoro in sottofondo (precaricamento lontano, cache, analisi) gira a priorità bassa, con un numero limitato di core, e rallenta o si ferma se il Mac è a batteria, si scalda o ha poca memoria; la foto che stai guardando ha sempre la precedenza;
  - si misura anche quanta CPU costa ogni foto, non solo quanto tempo: una build che diventa più pesante a parità di velocità non si pubblica.
  - **Misure del 9 novembre** su 20 JPEG pieni (8640 px) di ARW dell'Alpha 1, già in memoria, M1 Max:

| Metodo | Tempo per foto | CPU per foto | Note |
|---|---|---|---|
| Oggi: decodifica intera e riduzione con il processore (schermo 2560–3840) | 104–124 ms | 107–144 ms | tutto sul processore |
| Oggi, schermo 5K (5120) | 306 ms | 424 ms | |
| **Decodifica già ridotta a 1/2 (4320 px), decodificatore hardware del chip** | **43 ms** | **12 ms** | circa 3 volte più veloce, circa 11 volte meno CPU |
| Decodifica piena 8640 hardware (100% e 5K) | 91 ms | 38 ms | |
| Riduzione a misura esatta con Core Image e ritorno al processore | +50 ms | +13 ms | da evitare: la riduzione la fa la scheda grafica mentre disegna |
| Decodificatore hardware con più foto insieme | 22 foto al secondo | | **non lavora in parallelo**: una foto alla volta |

  Cosa ne segue (*mia proposta*):
  - la foto a schermo e le vicine si decodificano con l'hardware, già ridotte (a 1/2 fino al 4K, intere sul 5K); la scheda grafica le porta alla misura dello schermo mentre le disegna;
  - il processore entra solo quando vai più veloce di circa 22 foto al secondo (tasto tenuto premuto), con pochi core: lì si mostra l'anteprima 1616 (5 ms) e si sostituisce appena la versione nitida è pronta;
  - la versione decodificata a 1/2 occupa circa il 50% di memoria in più di quella a misura (4320 contro 3456 px): il tetto della cache tiene conto dei byte, non del numero di foto.
- **"Acceleratore hardware" nelle impostazioni, attivabile e disattivabile** (deciso con Andrea il 9 novembre). Acceso di serie (*mia scelta*); resta come l'hai lasciato ai riavvii. Si cambia mentre l'app gira: le foto già pronte si rifanno nel nuovo modo, a partire da quella a schermo. Acceso, la foto a schermo si decodifica già ridotta con il decodificatore JPEG del chip; spento, tutto si fa con il processore, come prima. Serve a confrontare e come uscita di sicurezza se un Mac o un'anteprima desse problemi. In SelectsLab è già nel menu SelectsLab.
  - **Misure del 9 novembre sulle ARW di La Thuile Trail** (rawline-bench, 50 file, M1 Max, file già in memoria):

| Schermo | Acceso: tempo / CPU per foto | Spento: tempo / CPU per foto | Acceso / spento in parallelo |
|---|---|---|---|
| 2880 | 69 ms / 32 ms | 116 ms / 129 ms | 23 / 51 foto al secondo |
| 3840 (4K) | 62 ms / 29 ms | 132 ms / 155 ms | 23 / 50 foto al secondo |
| 5120 (5K) | 160 ms / 187 ms | 343 ms / 456 ms | 34 / 19 foto al secondo |

  - Navigazione simulata (freccia ogni 150 ms e tasto tenuto premuto a 30 foto al secondo): foto pronta nel 100% dei casi in tutti e due i modi. Tutta la prova a 2880 costa **26 s di CPU acceso contro 78 s spento**: due terzi in meno di lavoro per il Mac.
  - Il prezzo: in memoria le foto acceso sono più grandi (4320 px invece di 2880), quindi la cache, che ha un tetto in byte, ne tiene meno (picco 4,2 GB contro 3,2 GB nella prova). Sul 5K la riduzione a metà non basta e si decodifica intera: lì il chip aiuta meno.
- **Precaricamento direzionale.** Mentre guardi la foto 120, l'app ha già pronte 121–126 e tiene 117–119. Se vai all'indietro, la finestra si sposta da quella parte. La quantità si adatta alla RAM disponibile.
- **Cache delle miniature su disco**, legata a percorso, dimensione e data di modifica: riaprire una cartella è istantaneo.
- **Cartelle enormi** (20.000 e più file): elenco caricato a pezzi, interfaccia che non si blocca mai.
- **RAW vero solo su richiesta** (un tasto): per controllare ombre e alte luci quando il JPEG incorporato non basta. Va sviluppato in sottofondo.
- **Verificato l'8 novembre** su file veri (ILCE-1, firmware 4.00, La Thuile Trail 2026), Mac M1 Max con schermo 5K:
  - Ogni ARW contiene tre JPEG: miniatura 160×120, anteprima 1616×1080 (circa 500 KB) e **JPEG a piena risoluzione 8640×5760** (circa 9,3 MB). Lo zoom al 100% si fa quindi senza sviluppare il RAW.
  - Tempi per foto: anteprima 1616 in 5 ms; foto a misura di schermo (2880 px) con ImageIO in **26 ms**; JPEG pieno 8640 in 91 ms; lettura dei 9,3 MB dal G-SPEED circa 30 ms a disco freddo.
  - In parallelo su tutti i core: **circa 310 foto al secondo** a misura di schermo, con i file già in memoria.
  - Conclusione: con il precaricamento la foto successiva è pronta prima che serva. Il collo di bottiglia sarà il disco, non la decodifica: su dischi lenti si legge prima l'anteprima 1616 (5 ms) e si sostituisce con quella piena appena pronta.
  - Da ripetere su altri corpi (A7 IV, A7R V), su ARW compressi senza perdita e su altre marche.
- **Fase 0 completata l'8 novembre** (ramo `selects/fase-0` in `~/Developer/Rawline`, modulo `MediaPreview` di RawlineKit, 39 test). Misure di `rawline-bench` su 50 ARW dell'Alpha 1 mai letti prima, dal G-SPEED, M1 Max:

| Misura | Risultato | Obiettivo |
|---|---|---|
| Struttura del RAW (disco freddo) | 15,6 ms | — |
| Anteprima piccola 1616 | 8,4 ms | — |
| Foto a misura di schermo 2880 | 22,6 ms (95° percentile 23,8) | — |
| JPEG pieno per il 100%, disco freddo | 187 ms (95° percentile 522) | sotto 50 ms: **non raggiunto a freddo** |
| In parallelo | 317 foto al secondo | — |
| Freccia ogni 150 ms, 200 foto | **100% già pronte** | sotto 16 ms: raggiunto |
| Tasto tenuto premuto (una foto ogni 33 ms), 100 foto | **100% già pronte** | raggiunto |

  Cosa ne segue:
  - Lo scorrimento è già all'altezza dell'obiettivo: con il precaricamento la foto c'è sempre prima che serva.
  - Il 100% va precaricato: in fase 2, quando lo zoom è acceso, si preparano il JPEG pieno della foto corrente e delle vicine nella raffica.
  - Marche: Sony recenti, Nikon (D850, Z8) e Pentax hanno il JPEG incorporato; i Sony più vecchi hanno solo l'anteprima 1616, e per loro il 100% sviluppa il RAW. L'IIQ di Phase One dà solo 300×220, un limite di macOS.
  - **Dopo la fase 0 (8–9 novembre):**
    - Lo schermo si prepara dal JPEG incorporato più grande, ridotto: prima ImageIO sceglieva l'anteprima 1616 degli ARW, morbida a tutto schermo. Costa 150 ms per foto invece di 21, nascosti dal precaricamento.
    - Zoom: `Z` tutto schermo nitido dal file pieno, `⇧Z` 100% con clic e trascina, clic tenuto premuto = lentino al 100%, spazio = 100% temporaneo.
    - In `Z` e `⇧Z` si precaricano la foto piena mostrata e le due successive: su RX100 VII pronta nel 97–100% dei casi.
    - Sony RX100 VII e ZV-1 hanno solo il JPEG 1616: la nitidezza si giudica con `Z`, che sviluppa il RAW (circa 0,5 s).
    - Lettori dedicati per CR3, RAF, ORF e RW2 scritti e provati su file costruiti nei test; **da verificare sui RAW veri** della raccolta di prova.
    - **Verifica sui RAW veri (9 novembre)**, in sola lettura, su 26 file di prova di 13 marche e su file di Andrea (Canon R5 Mark II, Panasonic, drone DJI). Tutti i file danno un'immagine, grazie al ripiego su macOS. I lettori propri funzionano su CR3 (R5 II: JPEG pieno 8192×5464), RAF, NEF recenti (D850, Z8 HE), ORF dell'OM-5, RW2, PEF, ARW e SR2.
    - **Corretto lo stesso giorno:** il lettore TIFF non trovava il JPEG grande su CR2 (6720×4480), DNG Leica M10-R (7840), DNG Pentax (6192), DNG iPhone (4032), un NEF di un corpo più vecchio (6048) e 3FR Hasselblad (4136). Nei primi cinque casi il JPEG è registrato come "strip"; nel NEF gli IFD stanno oltre i primi 256 KB. Ora li legge tutti. Restano a macOS: IIQ, FFF Hasselblad X1D, CRW Canon antichi e ORF Olympus E-1.
    - Per lo schermo, un'anteprima sotto metà del lato richiesto (DNG DJI da 960 px, vecchi SR2 Sony da 640) non viene più allargata: si sviluppa il RAW.
    - Anteprima davvero piccola, quindi cartello onesto e 100% dal RAW: DNG dei droni DJI (960 px, sensore 12288×8192), ORF dell'Olympus E-1 (1280), IIQ Phase One (300×220).
    - Raccolta di crash e segnalazioni (`⌘⇧B`) letta a ogni inizio sessione.
  - **Da fare con Andrea:** prova a mano di SelectsLab a fianco di Photo Mechanic sulla stessa cartella, e giudizio annotato qui.

---

## 4. Funzioni must have (versione 1.0)

*Nota sulle fasi (9 nov):* le funzioni di questa sezione che usano Vision arrivano nella 1.1 (fase 4): Scene, lampeggio allineato, volto e soggetto nell'ordine del primo zoom, zoom che segue il soggetto. Fino ad allora lo zoom **Intelligente** segue il riquadro AF e, dove manca, si comporta come **Fisso**; la zona dell'ordinamento per nitidezza resta ferma.

### 4.1 Aprire e vedere

- Apertura di una cartella, di più cartelle insieme, di una scheda di memoria direttamente (selezione prima dell'importazione, come Photo Mechanic).
- Trascinamento di cartelle sull'icona o sulla finestra.
- **Formati:** i RAW di tutte le marche (ARW, CR3, CR2, NEF anche HE/HE\*, RAF, DNG, ORF, RW2, PEF, 3FR, FFF, IIQ, X3F e altri), JPEG, HEIF/HEIC, TIFF, PNG, PSD, AVIF, WebP, JPEG XL. Video MP4, MOV, MTS (vedi 4.8).
- **Quando macOS non legge ancora il RAW** (corpi nuovi, Nikon HE prima di macOS 26.4, A7 V non lossless, RW2 neri su 26.4, Hasselblad 907X, Phase One IQ4, DJI) si mostra comunque l'anteprima incorporata, con il cartello "solo anteprima, RAW non leggibile da questa versione di macOS".
- **File gemelli** RAW + JPEG visti come una foto sola; la valutazione vale per entrambi. Riusa `TwinGroup` di RawlineKit. Su Fujifilm, OM e Panasonic, dove l'anteprima incorporata è piccola e si scatta spesso con le simulazioni pellicola, **il JPEG gemello è l'anteprima migliore** e va preferito.
- **Viste:** griglia (miniature di dimensione regolabile), foto singola a schermo intero, filmstrip sotto la foto, confronto (vedi 4.4).
- Rotazione automatica dall'EXIF e rotazione manuale.
- **Barra informazioni** essenziale, attivabile con un tasto: tempo, diaframma, ISO, focale, obiettivo, corpo (AP1/AP2), data e ora, nome del file.
- **Pannello metadati completo:** EXIF, IPTC, XMP, MakerNote, GPS con mappa. Deve leggere tutto quello che c'è nel file.

### 4.2 Valutare

**Deciso (8 nov):** stelle e colori insieme, come in Lightroom, non "o l'uno o l'altro" come in Photo Mechanic. Scelta e scarto come i flag di Lightroom.

| Cosa | Tasto | Dove si scrive |
|---|---|---|
| Stelle 1–5 | `1`–`5` | `xmp:Rating` |
| Togli le stelle | `0` (come Lightroom) | `xmp:Rating = 0` |
| Rosso, giallo, verde, blu | `6`, `7`, `8`, `9` (come Lightroom) | `xmp:Label` con i nomi di Lightroom |
| Viola | nessun tasto per ora (come Lightroom): dal menu o dal tasto destro, assegnabile nelle scorciatoie | come sopra |
| Togli il colore | ripremere lo stesso tasto colore (come Lightroom) | |
| Scelta (Pick) | `P` | `xmpDM:pick = 1`, il campo che Lightroom Classic scrive dalla versione 13.2 |
| Scarto (Reject) | `X` | `xmpDM:pick = -1` |
| Togli scelta o scarto | `U` | `xmpDM:pick = 0` |
| Valuta e passa alla successiva | `⇧` + tasto (come Lightroom), oppure Blocco maiuscole per l'avanzamento continuo | |
| Annulla / ripristina | `⌘Z` / `⇧⌘Z` | cronologia illimitata nella sessione |

Deciso con Andrea: identico a Lightroom. Lo `0` toglie le stelle, perché è troppo importante; il viola resta senza tasto, come in Lightroom.

Scelta e scarto: Lightroom Classic dalla versione 13.2 (febbraio 2024) salva i flag nell'XMP come `xmpDM:pick` (1, 0, -1) più `xmpDM:good` (true/false), e da lì passano anche a Lightroom desktop. Restano tre dubbi: il valore esatto di `xmpDM:good` per scarto e "senza flag", se Lightroom rilegge un `xmpDM:pick` scritto da un'altra app, e se il bug della 13.2 (flag non salvato quando il campo manca) è stato corretto. Per prudenza **Selects scrive sempre il campo in modo esplicito, anche lo 0**. **Va provato sul Lightroom di Andrea prima di scrivere il codice** (vedi 4.6, "File campione"). Per i programmi che non leggono `xmpDM:pick` (Bridge, Photo Mechanic), un'opzione scrive anche lo scarto come voto -1.

- **Avanzamento automatico** alla foto successiva, attivabile, con un ritardo regolabile (anche zero).
- **Valutazione multipla:** su tutte le foto selezionate in griglia, o su tutta una raffica (sulla pila chiusa tocca solo gli scatti senza marcatura, 4.4). È un solo passo di annulla.
- **Scorciatoie completamente personalizzabili**, con preset pronti "Come Photo Mechanic", "Come Lightroom" e "Come Bridge": chi arriva da un'altra app non deve reimparare niente.
- **Tasti riassegnabili anche a combinazioni**: un solo tasto per "3 stelle + verde".
- Valutazioni lette all'apertura: quelle già nel file o nell'XMP (`EXIF:Rating`, `XMP:Rating`) e quelle date in macchina.
- **Promozione dei voti dati in macchina (fase 2).** Si perdono con tutte le marche, e nessuno lo risolve: Fujifilm li salva nei MakerNote, che Lightroom non legge; Canon salva quelli dei video in `QuickTime:Rating`; con due schede la valutazione finisce solo sulla prima; nelle coppie RAW+JPEG a volte solo su uno dei due. Selects li cerca tutti, li unisce e li copia nell'XMP, dicendo "trovate 23 valutazioni date in macchina".

### 4.3 Controllare il fuoco

- **Zoom al 100% istantaneo** con `⇧Z` (`Z` è il tutto schermo nitido, decisione 6) o tenendo premuto lo spazio (zoom temporaneo: rilasci e torni alla foto intera).
- **Il 100% è davvero il 100%** (9 nov): un pixel della foto su un pixel dello schermo, né di più né di meno, e senza sacrificare la velocità.
- **Menu della percentuale in basso a sinistra**, come in Photoshop e Lightroom (per esempio 25%, 50%, 100%, 200%). Se scegli 50%, da lì in poi ogni zoom va al 50%, per tutta la sessione. A ogni avvio si riparte dal 100%; il valore di partenza si cambia nelle impostazioni. Il valore vale per `⇧Z` e per lo spazio tenuto premuto; il lentino resta sempre al 100% (decisione 6); anche il primo zoom sul punto AF (5.1) è quello di `⇧Z`. *Mia scelta.*
- Va pensato per tutti gli schermi. Quanto si vede di uno scatto dell'Alpha 1 (8640×5760) a tutto schermo:

| Schermo | al 100% | al 50% |
|---|---|---|
| MacBook Pro 16" (3456×2234) | circa 40% della larghezza | circa 80% |
| 27" 2K (2560×1440) | circa 30% | circa 60% |
| 4K (3840×2160) | circa 44% | circa 89% |
| 5K (5120×2880) | circa 59% | intera |
- **Zoom onesto su ogni marca.** Se l'anteprima incorporata è sotto circa metà della risoluzione del sensore, il 100% sviluppa un riquadro del RAW intorno al punto ingrandito e lo dice ("zoom dal RAW"). Ingrandire un'anteprima piccola **mente**: fa sembrare morbido quello che è nitido, o il contrario. È l'argomento con cui FastRawViewer sconsiglia di selezionare sulle anteprime, e la risposta di Selects.
- **Zoom sul punto giusto:** il primo zoom va sul punto AF registrato dalla fotocamera; senza punto AF, sul volto; senza volto, sul soggetto principale; solo alla fine al centro.
- **Zoom intelligente tra una foto e l'altra.** Il problema più citato da chi usa Lightroom è che lo zoom si azzera passando alla foto successiva. In Selects ci sono tre comportamenti, e il predefinito è **Intelligente**:

| Modo | Cosa succede passando alla foto successiva |
|---|---|
| **Intelligente** (predefinito) | Dentro la stessa raffica lo zoom resta e **segue il soggetto**: se tra uno scatto e l'altro hai seguito lo sciatore con la fotocamera, l'ingrandimento resta su di lui, non sullo stesso punto dello schermo. Uscendo dalla raffica, la foto nuova si apre intera |
| **Fisso** | Stesso punto e stesso ingrandimento sempre, come il confronto sincronizzato di FastRawViewer |
| **Azzera** | Ogni foto si apre intera, come Lightroom oggi |

  Come segue il soggetto: un'analisi locale (Vision di Apple, sezione 5.1) calcola di quanto si è spostata l'inquadratura tra due scatti vicini e sposta lo zoom della stessa quantità. Se il punto AF della foto nuova è lontano dal soggetto, vince il punto AF. Fattibilità: alta, Vision ha già le funzioni per allineare due immagini; va misurata la velocità sulle raffiche da 30 fotogrammi al secondo dell'Alpha 1.
- **Lampeggio fra due scatti:** un tasto alterna due foto della raffica, allineate e allo stesso zoom, per vedere al volo quale ha l'occhio più nitido.
- **Punto AF sovrapposto alla foto, con un tasto: `A`** (da "AF"; in Lightroom è libero). Acceso o spento vale per tutte le foto finché non lo ripremi, e funziona **anche sulla foto intera, non solo nello zoom**: un riquadro sottile mostra dove la fotocamera ha messo a fuoco, così si capisce al volo se il fuoco è finito sul soggetto o sullo sfondo. Facoltativo anche sulle miniature della griglia. Se il file non ha il punto AF, nessun riquadro e un piccolo segno "AF non disponibile" nella barra informazioni. Per Sony si legge dal MakerNote (`Sony:FocusLocation`, con `FocusFrameSize` e `FocusPosition2` sui corpi recenti).
  - **Elenco pubblico dei corpi "verificati" e "sperimentali"**, e la dicitura "dove la fotocamera dice di aver messo a fuoco". Mai un riquadro indovinato su un corpo non verificato: è proprio l'obiezione di FastRawViewer, e il difetto di Adobe che non mostra nulla senza dire perché.
  - Ordine: Sony (A1, A1 II, A9 III, A7 IV), poi Canon CR3 (`AFInfo2/AFInfo3`) e Nikon Z (`AFInfo2`) come sperimentali, poi Fujifilm (`FocusPixel`), OM/Olympus (`AFPoint`, `AFAreas`), Panasonic (`AFPointPosition`), Pentax (`AFPointsInFocus`). Medio formato e droni non hanno un punto AF utile.
  - Il codice di digiKam che legge questi campi è GPL: si impara dalla documentazione di ExifTool e si scrive un lettore proprio in Swift.
- **Focus peaking** sul JPEG, attivabile con un tasto.
- **Avvisi di esposizione:** alte luci bruciate e ombre chiuse evidenziate, istogramma; a richiesta calcolati sul RAW, come fa FastRawViewer.

### 4.4 Confrontare e raffiche

- **Confronto da 2 a 4 foto affiancate**, con zoom e trascinamento sincronizzati. Si valuta ogni foto senza uscire dal confronto.
- **Modalità sopravvivenza:** selezioni 8 foto, le vedi tutte insieme, togli le peggiori una per una finché resta la migliore. Lightroom la chiama Survey.
- **Scene:** foto simili ma non della stessa raffica raggruppate per somiglianza visiva, calcolata in locale (vedi 5.1).

#### Raffiche (deciso con Andrea il 9 novembre)

Il caso di Andrea: trail a 5–10 fotogrammi al secondo; tuffi, MTB e sci a 30 (Alpha 1), con raffiche lunghe nelle curve di freeride; la A9 III arriva a 120. Di solito tiene uno scatto per raffica, a volte 2–3, di più per un composito. Scatta a mano seguendo il rider, a volte in panning. Guarda prima il momento, poi il fuoco. A volte ricorda il momento giusto, a volte deve rivedere tutto.

Cosa fanno gli altri (ricerca del 9 novembre): BurstPick ha una modalità raffica separata, con candidati, confronto fino a 4 e "campione contro sfidante"; Narrative raggruppa in Scene con le frecce tra scene e dentro la scena; Aftershoot e FilterPixel riducono la raffica a 1–3 proposte con un punteggio; Lightroom fa pile per ora di scatto o per somiglianza. Nessuno parte dal momento e nessuno si adatta al ritmo di scatto. Selects non ha una modalità separata: la raffica vive dentro la selezione normale.

**Riconoscere le raffiche**
- Una raffica è una sequenza scattata senza staccare il dito. **Se rilasci e riparti, anche dopo mezzo secondo, sono due raffiche.**
- Si riconosce dal **ritmo della raffica stessa** (da 5 a 120 fotogrammi al secondo: una pausa molto più lunga dell'intervallo tra gli scatti chiude la raffica) **e dal numero di sequenza scritto dalla fotocamera** (Sony `SequenceNumber`, Canon `ContinuousDrive`, Panasonic `BurstMode`, OM `DriveMode` per il Pro Capture). Il solo tempo sbaglia su molti corpi. Quando c'è, **il numero di sequenza vince sul tempo**; sui corpi che non lo scrivono si usa solo il ritmo. Vale per tutte le marche. I file "roll" Canon con molti fotogrammi si mostrano come raffica, senza scrivere niente su disco; la marcatura vale per tutto il file, perché un sidecar non può tenere un voto per fotogramma (*mia scelta*; estrarre un fotogramma arriverà più avanti). Il Pro Capture OM scrive file separati e non ha questo problema.
- La soglia si cambia nelle impostazioni. *Mia proposta per il valore di serie:* la raffica si chiude con una pausa di 0,5 s, o prima se il ritmo è alto (a 30 fps una pausa di 0,2 s è già un rilascio).
- Un'impostazione spegne le pile: le raffiche si vedono come foto normali, una dopo l'altra.

**Nel flusso normale**
- La raffica è una **pila** con il numero di scatti e la durata (per esempio "42 · 1,4 s"), in griglia e nella foto grande.
- `←`/`→` la trattano come un passo solo: passi oltre la raffica intera.
- Su una pila chiusa: `P` tiene tutti gli scatti, `X` li scarta tutti. Stelle e colori valgono per tutta la pila.
- **Una marcatura sulla pila chiusa tocca solo gli scatti ancora senza marcatura** in quella stessa cosa: un flag va solo sugli scatti senza flag, le stelle solo su quelli senza stelle, il colore solo su quelli senza colore (sulla pila il tasto colore assegna, non alterna) (deciso con Andrea il 9 novembre). Se dentro hai già tenuto 2 scatti e poi premi `X` sulla pila, quei 2 restano tenuti. L'app lo dice con un avviso breve, per esempio "40 scartati · 2 già marcati non toccati". Così un tasto solo non annulla mai le scelte fatte scatto per scatto.
- Con un filtro attivo (per esempio solo le scelte) la pila mostra solo gli scatti che lo passano. Nel contatore (4.5) una pila passata senza entrarci conta come "da vedere". *Mia scelta.*
- Una raffica che passi senza entrarci resta **senza marcatura**. Niente va mai in `X` da solo: gli scatti non scelti restano senza marcatura, perché Andrea a volte li riprende (per esempio per Forever Snow Trips).

**Dentro la raffica (opzione A delle bozze)**
- Si entra con **Invio o doppio clic** sulla pila, si esce con **Esc**. Vale sia in griglia sia nella foto grande. Dalla griglia, Invio sulla pila porta direttamente dentro la raffica; poi Esc riporta alla foto grande sulla pila, e un altro Esc alla griglia: la scala dei livelli (4.10) resta sempre la stessa (*mia scelta*). `↑`/`↓` non servono per le raffiche.
- In alto una **panoramica scorrevole** con tutti gli scatti piccoli, per vedere dove sta il rider. *Mia proposta:* l'altezza della panoramica si regola trascinandone il bordo.
- Sotto, lo scatto selezionato in grande. Clic su una miniatura per saltarci; `←`/`→` scatto per scatto.
- **`←`/`→` restano dentro la raffica.** All'ultimo scatto si fermano, con un avviso ("ultimo scatto: Esc per uscire"). Non portano mai fuori.
- Si marca con i tasti di sempre. Gli scatti non marcati restano non marcati.
- **`P` dentro la raffica vuol dire "questo è lo scatto"** (deciso con Andrea il 9 novembre): segna lo scatto come scelta e porta subito fuori, alla foto o raffica successiva. Stelle (`1`–`5`), colori (`6`–`9`), `X` e `U` invece lasciano dentro: si marcano uno o più scatti con calma e si esce con Esc. Per sceglierne un altro con `P` si rientra con Invio: il nuovo si aggiunge, il primo resta scelto. Fuori dalle raffiche `P` resta il flag di sempre.
- Uscendo, la **copertina della pila diventa lo scatto tenuto** (se ne hai tenuti più d'uno, il primo in ordine di scatto), e la pila dice quanti ne hai tenuti (per esempio "42 · 2 tenute").

**Il fuoco dentro la raffica**
- Nessun semaforo e nessun voto di nitidezza: l'app non sa su cosa volevi mettere a fuoco.
- Lo zoom va sul **riquadro AF della fotocamera** e lo segue scatto per scatto (4.3). In fase 2 vale questo; sui corpi senza punto AF verificato lo zoom resta nello stesso punto e allo stesso ingrandimento. Lo zoom che segue il soggetto con Vision arriva in fase 4. *Mia scelta.*

**Promemoria**
- Una raffica mai aperta e senza marcature ha un piccolo segno sulla pila.
- A fine cartella l'app lo dice: "3 raffiche non ancora guardate", con un clic per andarci. *Il modo esatto è una mia proposta.*

**Velocità dentro la raffica**
- Il precaricamento carica più scatti pieni nella direzione in cui ti muovi.
- Se vai più veloce del disco, vedi prima l'anteprima e poi la versione nitida: non si blocca mai.

**Per ora fuori, come possibili aggiunte:** la lente sul riquadro AF sotto ogni miniatura (opzione B delle bozze) e la panoramica "dal grosso al fine" per le raffiche da 60–120 fps (opzione C). L'ordinamento per nitidezza a richiesta resta in fase 2 (5.1).

### 4.5 Filtrare e ordinare

- Filtri immediati da tastiera: almeno N stelle, solo un colore, solo non valutate, solo scartate, solo scelte.
- Filtri per corpo macchina (AP1, AP2, letti dal numero di serie come in Rename), obiettivo, focale, ISO, tempo, data e ora, tipo di file, orientamento.
- **Ordine cronologico reale tra più corpi**, con correzione dello scarto orario (riusa `CameraBodies` e `CaptureTime` di RawlineKit).
- Ricerca per nome file o per parte del nome.
- Contatore sempre visibile: "Viste 312 di 1.840, tenute 87, scartate 140".

### 4.6 Metadati compatibili (la parte che gli altri sbagliano)

- **Sidecar XMP aggiornato con precisione chirurgica.** Se l'XMP esiste già (per esempio scritto da Lightroom con le regolazioni di sviluppo), Selects cambia solo voto ed etichetta e lascia intatto tutto il resto. Mai riscrivere un XMP da zero.
- **Scrittura atomica:** file temporaneo e poi sostituzione, così un'interruzione non lascia un XMP rotto.
- **Diario delle modifiche** in un piccolo database locale: ogni valutazione ci finisce prima di andare nel file. Se l'app o il Mac si spengono, al riavvio niente è perso.
- **Profili per le etichette colore.** Il nome scritto nell'XMP deve coincidere con quello che si aspetta l'app che lo legge, nella **sua** lingua: Lightroom scrive il nome dell'etichetta come testo nella lingua della sua interfaccia (in tedesco `Rot`, `Gelb`…). Lightroom 15 (ottobre 2025) aggiunge un nuovo campo colore: verificato il 9 novembre sui sidecar di Andrea, è **`photoshop:LabelColor`** con il colore in inglese minuscolo (`yellow`, `green`…), scritto accanto al nome tradotto. Selects lo scrive sempre: non dipende dalla lingua. Le versioni recenti di Capture One danno la precedenza al **nome inglese** dell'etichetta; `photoshop:Urgency` serve solo ai Capture One vecchi (i numeri sono cambiati tra le versioni). Bridge usa nomi propri (Select, Second, Approved, Review, To Do). Profili pronti: Lightroom inglese, Lightroom italiano, Capture One (nomi inglesi), Capture One vecchio (con Urgency), Bridge (i suoi nomi più lo scarto -1), Photo Mechanic, più uno personalizzato.
- **Due lingue, due cose diverse.** L'interfaccia di Selects segue la lingua di macOS, in italiano o in inglese, come Rename: il bottone dice "Rosso" o "Red". Il testo scritto nell'XMP invece segue il profilo scelto, non la lingua dell'app. **Deciso con Andrea (9 nov): Lightroom italiano e Lightroom inglese sono previsti tutti e due**, pronti di serie. I sidecar di Andrea contengono `Gialla` e `Verde`. Al primo avvio su una cartella Selects legge gli XMP già presenti e propone il profilo che corrisponde ai nomi che trova; senza XMP si parte dal profilo della lingua di macOS (*mia scelta*). `photoshop:LabelColor` si scrive sempre.
- **Lettura tollerante:** in lettura Selects guarda prima `photoshop:LabelColor`, poi i nomi di tutti i profili e di tutte le lingue note, poi `photoshop:Urgency`, poi `photomechanic:ColorClass`, così un file etichettato da qualunque programma mostra il colore giusto.
- **Nomi dei sidecar.** Si scrive `NOMEFILE.xmp` in minuscolo, come Adobe, Capture One, Photo Mechanic e FastRawViewer. In lettura si cercano anche `.XMP` e `NOMEFILE.EXT.xmp` (darktable): su un disco che distingue maiuscole e minuscole la ricerca altrimenti si rompe.
- **Dove si scrive.** RAW proprietari: sidecar. DNG, JPEG, HEIF e TIFF: dentro il file di serie (Lightroom ignora i sidecar dei JPEG, Apple Foto legge solo i dati dentro il file), con l'opzione del sidecar. Coppie RAW+JPEG con lo stesso nome: sidecar del RAW **e** gli stessi valori dentro il JPEG, perché i due si contenderebbero un solo `.xmp`.
- **Cosa si tocca.** Se l'XMP contiene regolazioni di Lightroom, si cambiano solo voto (anche il -1 dello scarto, se l'opzione è accesa), etichetta, `photoshop:LabelColor`, `xmpDM:pick`/`xmpDM:good` e `xmp:MetadataDate`. Quest'ultimo si aggiorna sempre, perché è la data che decide quale copia vince. I campi IPTC 2025.1 sull'AI generativa e le Content Credentials (C2PA) non si cancellano mai. Mai scrivere nel catalogo di Lightroom.
- **Trovati sul Mac di Andrea (9 novembre)**, sul disco APOWC2_BACKUP; copie di prova in `~/Developer/Rawline-samples/andrea/`, gli originali non sono stati toccati:
  - XMP scritti da Lightroom Classic 15.2 e 15.5.1, anche con regolazioni di sviluppo, sui lavori Grivel e La Thuile Trail; parte dei sidecar è passata anche da Photo Mechanic 2025.1 (`photomechanic:ColorClass`, `photomechanic:Tagged`).
  - **Etichette:** Lightroom scrive `xmp:Label="Gialla"` e `"Verde"`, cioè nomi italiani, e accanto **`photoshop:LabelColor="yellow"`** / `"green"`. È il nuovo campo colore di Lightroom 15: il nome è `photoshop:LabelColor` e il valore è il colore in inglese, minuscolo. In lettura va usato per primo, perché non dipende dalla lingua.
  - **Flag:** scelta = `xmpDM:pick="1"` con `xmpDM:good="true"`; senza flag = `xmpDM:pick="0"` senza `xmpDM:good`. Nessuno scarto (`-1`) trovato: va ancora creato apposta in Lightroom.
  - Sidecar con l'estensione maiuscola `.XMP` accanto a quelli in minuscolo: la lettura tollerante dei nomi serve davvero.
  - Capture One non è installato: per i suoi XMP serve un altro computer o un file di prova.
- **File campione (prima del codice).** Andrea esporta da Lightroom Classic 15 un XMP per ogni caso: cinque colori, scelta, scarto, stelle, e una foto con regolazioni di sviluppo. Lo stesso da Capture One, se disponibile. Selects si costruisce e si testa su quei file veri, non su ipotesi. Si chiudono così i dubbi su `xmpDM:good` e sul nome del nuovo campo colore. Poi la prova al contrario: XMP scritti da Selects, letti da Lightroom con "Read Metadata from Files" e da Capture One.
- **Avviso se un altro programma modifica il file** mentre Selects è aperto (sorveglianza della cartella): si rilegge e si avvisa.
- **Scelta per JPEG, HEIF e DNG:** valutazione scritta dentro il file oppure in un sidecar.
- **Promemoria per Lightroom e Capture One:** se le foto sono già nel catalogo, Lightroom va aggiornato con "Leggi metadati da file" (Lightroom desktop non ha il comando: si aggiornano le foto). Su Capture One la configurazione da consigliare è "Auto Sync Sidecar XMP = Load" più "Sync Metadata" per le foto già presenti: la sincronizzazione completa rallenta molto i cataloghi grandi. L'app lo spiega la prima volta. Per Bridge, FastRawViewer e Photo Mechanic, che non leggono `xmpDM:pick`, resta l'opzione dello scarto come voto -1 (4.2).

### 4.7 Azioni sulla selezione

- Copia o sposta le tenute in una cartella (es. `_Selezione`), con i gemelli e gli XMP al seguito.
- Sposta le scartate in `_Scartate`. Mai cancellazione definitiva: al massimo il Cestino, con annullamento.
- **Apri in Lightroom, Capture One o Photoshop** solo le foto filtrate.
- **Esporta l'elenco dei nomi** (testo o CSV), da incollare nel filtro di Lightroom o da mandare al cliente.
- **Passa a RawLine Rename** con la selezione corrente.

### 4.8 Video

Andrea è anche videomaker: questa è una differenza vera dai concorrenti.

- Clip nella stessa griglia delle foto, con anteprima scorrevole al passaggio del mouse.
- Riproduzione con J-K-L, avanti e indietro fotogramma per fotogramma, velocità variabile.
- Stelle, colori e scarto anche per i video, scritti in un sidecar XMP compatibile con Lightroom, Bridge e Final Cut tramite i flussi abituali.
- **Punti di ingresso e di uscita** per segnare la parte buona di una clip (versione 1.x).
- Lettura dei file XML che le Sony creano accanto ai video (modello, data, impostazioni).

### 4.9 Sessione e affidabilità

- **Riprendi dove eri rimasto:** riaprendo la cartella torni alla stessa foto, con filtri e vista.
- **Avanzamento della selezione** per cartella: quante viste, quante da vedere.
- Funziona tutto offline.
- Non si blocca mai su file danneggiati: li segnala con un'icona e passa oltre.
- Test automatici su file reali di ogni marca, come per Rename.

### 4.10 Navigator e livelli (deciso con Andrea il 9 novembre)

**Il modello è Photo Mechanic.** La finestra principale (contact sheet) ha a sinistra tre pannelli: Navigator, l'albero di dischi e cartelle; Favorites, le cartelle che si riaprono spesso, aggiunte trascinandole o col tasto destro, anche come gruppo di più cartelle; Tasks, l'avanzamento di importazioni e copie. Le cartelle aperte sono schede in alto, riordinabili; una scheda può unire più cartelle. L'anteprima si apre con Spazio, con la lente o con ⌘R; Esc o ⌘W la chiudono e si torna al contact sheet. Per Andrea è più comodo che cercare le cartelle nel Finder. È utile, ma non essenziale.

**Il navigator di Selects**
- Barra laterale a sinistra (come in 11) con dischi e schede di memoria, l'albero delle cartelle e i **preferiti**. Un preferito può essere una cartella o un gruppo di cartelle.
- Le cartelle aperte sono **schede** in alto, riordinabili, da cambiare anche da tastiera. Una scheda può unire più cartelle, in ordine di scatto.
- Si apre una cartella con un clic o con Invio nell'albero.
- **Una sola barra laterale:** in alto dischi, cartelle e preferiti; sotto, filtri con i conteggi e corpi AP1/AP2 (11). Fino alla fase 3 il livello 0 è l'accoglienza con le cartelle recenti e poi la griglia, una cartella alla volta, senza schede. *Mia scelta.*
- **Spazio** apre la foto dalla griglia, come in Photo Mechanic. Su una pila, Spazio apre la foto grande sulla pila (livello 1); Invio o doppio clic entrano nella raffica (livello 2), come deciso con Andrea. *Mia scelta:* spazio tenuto premuto oltre 0,2 s = zoom temporaneo. Nella foto grande e dentro la raffica, tenuto premuto, è lo zoom temporaneo (4.3).

**Tre livelli. Esc risale sempre di uno solo**

| Livello | Cosa vedi | Come entri | Esc |
|---|---|---|---|
| 0 · Navigator e griglia | dischi, cartelle e preferiti a sinistra; schede delle cartelle aperte in alto; miniature al centro | apri una cartella | **non fa niente**: non chiude mai la cartella né la scheda (per quello c'è ⌘W) |
| 1 · Foto grande | la selezione vera e propria, con le foto e le pile delle raffiche | Invio, Spazio o doppio clic | torna alla griglia, sulla stessa foto |
| 2 · Dentro la raffica | panoramica e scatto grande (4.4) | Invio o doppio clic sulla pila | torna alla foto grande, sulla stessa pila |

Perché due Esc di troppo non fanno danni (Andrea ha detto che basta così, senza bloccare il secondo Esc):
- **Esc non perde niente.** Le marcature sono già salvate (4.6, 4.9) e l'app ricorda dove eri. Con Invio torni esattamente lì.
- **⌘W come in Photo Mechanic** (deciso con Andrea il 9 novembre): nella foto grande e dentro la raffica risale di un livello, come Esc. Solo nella griglia chiude la scheda o la cartella. Esc da solo non chiude mai niente.
- **In alto c'è sempre il percorso** del livello in cui sei, per esempio *Tenerife2026 › DSC01234 › Raffica · 42 scatti*. Si può cliccare per risalire.
- È anche la risposta al problema 23 (sezione 10): in Capture One un Esc per sbaglio fa uscire dalla modalità Cull.

---

## 5. Funzioni migliorative (versioni 1.x)

### 5.1 AI in locale che rende più veloce la mano, senza giudicare

**Deciso (8 nov): niente selezione assistita**, né "indizi" né "prima passata". L'app non dice mai quale foto è migliore e non scarta niente. La selezione è manuale. L'AI lavora solo per rendere più veloci gli occhi e le mani del fotografo: decide **dove guardare**, mai **cosa tenere**. La selezione assistita resta tra le idee future, da riprendere solo quando potrà funzionare davvero bene.

Tutto sul Mac, con Vision di Apple e il Neural Engine. Niente rete, niente account, nessuna foto caricata.

| Aiuto | Cosa fa per te | Come funziona | Fattibilità |
|---|---|---|---|
| **Zoom che segue il soggetto** | Nelle raffiche lo zoom resta sul soggetto anche se ti sei mosso con la fotocamera (4.3) | Allineamento tra due immagini di Vision, sulle anteprime ridotte | Alta |
| **Primo zoom nel punto giusto** | Il primo `⇧Z` va sul punto AF, poi sul volto, poi sul soggetto | MakerNote per marca + rilevamento volti e soggetto di Vision | Alta (il punto AF va decodificato e verificato corpo per corpo, Sony per prima) |
| **Salto tra i volti** | In una foto di gruppo, un tasto porta lo zoom al volto successivo | Rilevamento volti di Vision | Alta |
| **Striscia dei volti** | In una foto di gruppo, tutti i volti ingranditi in fila: controlli gli occhi di 12 persone in un colpo d'occhio, e decidi tu | Rilevamento volti, ritaglio | Alta |
| **Raffiche raggruppate** | La cartella si ordina da sola in gruppi: è struttura, non giudizio | Ritmo di scatto e numero di sequenza (4.4); la somiglianza visiva (impronte di Vision) serve alle Scene | Alta |
| **Lampeggio allineato** | Due scatti alternati, allineati, allo stesso zoom (4.3) | Allineamento di Vision | Alta |
| **Precaricamento che prevede** | Impara il tuo ritmo e la tua direzione: se in una raffica vai veloce, prepara più foto davanti | Statistiche locali, senza AI vera | Alta |
| **Focus peaking e mappa di nitidezza** | Colora le zone a fuoco, a richiesta: tu giudichi | Filtro di contorni sulla GPU | Alta |
| **Livella dell'orizzonte** | Una linea sottile mostra se l'orizzonte è storto | Rilevamento dell'orizzonte di Vision | Alta |
| **Ricerca per contenuto** (più avanti) | "Mostrami le foto con persone", "solo i paesaggi" | Classificazione di Vision, in sottofondo | Media: utile su archivi grandi, meno nella selezione di un servizio |
| **Numeri dei pettorali** (più avanti, sport) | Trovare tutte le foto dell'atleta 112 | Riconoscimento del testo di Vision | Media: da provare su foto reali di gara |

Cosa **non** facciamo, per scelta: classifiche di nitidezza visibili (numeri, badge, "la migliore"), punteggi estetici (anche quello di Vision, `CalculateImageAestheticsScoresRequest`), avvisi "occhi chiusi", proposte della foto migliore, scarti automatici, punteggi che cambiano da un'analisi all'altra.

**Deciso (9 nov): ordinamento della raffica a richiesta.** La richiesta più antica del mercato è "qual è la più nitida della raffica?" (aperta da Adobe dal 2011 al 2026), e almeno cinque app indie del 2025–2026 la inseguono. Andrea l'ha approvato in questa forma, che resta dentro il principio "l'AI decide dove guardare, mai cosa tenere":
- un tasto mette in fila i fotogrammi della raffica secondo il dettaglio misurato nel riquadro AF, o in una zona scelta dal fotografo che segue il soggetto;
- l'ordine serve solo a scegliere quali due far lampeggiare per primi;
- nessun numero sulla foto, nessun badge "migliore", nessuna foto nascosta o scartata;
- risultato sempre identico a parità di file;
- il confronto vale solo dentro la stessa raffica, perché il JPEG incorporato è già reso più nitido dalla fotocamera;
- spento di serie: parte solo quando lo chiedi, e si torna all'ordine degli scatti con lo stesso tasto.

Tecnicamente è un filtro di contorni sulla scheda grafica, calcolato per riquadri. Arriva in fase 2, insieme al punto AF e alla mappa di nitidezza.

**Altre tecnologie Apple da conoscere:** RAW 9 di Core Image (macOS 27, sviluppo con un modello sul Neural Engine, più pesante, utile ad alti ISO) come opzione per il controllo critico del fuoco; il modello linguistico sul dispositivo (Foundation Models) per filtri in linguaggio naturale ("solo verticali a 3 stelle dal corpo 2 dopo le 14") e bozze di didascalie IPTC, mai per giudicare; il rilevamento di obiettivo sporco (`DetectLensSmudgeRequest`, OS 26) come avviso sull'intero servizio, da provare sulle mirrorless.

Il calcolo pesante gira nel servizio separato (sezione 13), mai sul thread dell'interfaccia: se l'analisi di una foto non è ancora pronta, l'app si comporta come se non ci fosse (zoom al punto AF o al centro) e non aspetta mai.

### 5.2 Modalità di lavoro pensate per il fotografo

- **Passata rapida (sì/no):** solo due tasti, tieni e scarta, per la prima scrematura di migliaia di foto.
- **Duello:** due foto affiancate, scegli la migliore, la vincente resta e sfida la successiva. Per arrivare all'unica foto di copertina.
- **Selezione in due passate:** prima sì/no, poi stelle solo sulle tenute, con filtro automatico tra le due.
- **Obiettivo di consegna:** "devo consegnare 60 foto". L'app mostra quante ne hai tenute rispetto all'obiettivo.

### 5.3 Controller fisici

- **Controller da gioco** (Xbox, PlayStation) tramite il framework GameController di macOS, e **controller MIDI** con CoreMIDI: pochi giorni di lavoro, nessun concorrente li pubblicizza, e oggi i fotografi devono comprare app di mappatura.
- Comandi "più una stella" e "meno una stella" per manopole e rotelle (TourBox, Logitech MX Creative Console), come chiedono gli utenti. Loupedeck non si produce più.
- Stream Deck (SDK MIT) e MX Creative Console (Logi Actions SDK): nella 1.0 basta che le scorciatoie siano personalizzabili, più profili pronti; i plugin che mostrano lo stato della foto sui tasti vengono dopo.
- Trackpad: scorrimento a due dita tra le foto, pizzico per lo zoom.

### 5.4 Selezione sul campo e in viaggio

- Seleziona direttamente dalla scheda, poi passa all'importazione solo delle tenute (anticipa la modalità Importa di RawLine).
- Profili di velocità per dischi lenti e NAS: precarica di più quando la sorgente è lenta.

### 5.5 Collaborazione e cliente (più avanti)

- Esporta una galleria di prova per il cliente e reimporta le sue scelte come etichetta. Solo ShootProof ha un'API pubblica; per Pixieset e Pic-Time si reimporta l'elenco dei nomi scelti.
- **Plugin Lightroom** (Lua): applica i flag direttamente nel catalogo aggirando i bug dell'XMP, crea una raccolta e conta i file arrivati.
- **Geotag da GPX** (tracciati Garmin): tempo di scatto corretto con lo scarto dell'orologio di RawlineKit, coordinate nel sidecar.
- Due persone sulla stessa cartella in rete: le valutazioni si uniscono senza sovrascriversi.

### 5.6 Statistiche

- Tempo di selezione per servizio, percentuale tenuta, foto al minuto.
- Statistiche di fuoco per obiettivo o per corpo: un aiuto per capire se una lente è decentrata.

---

## 6. Cosa non fare

- Niente catalogo obbligatorio: si lavora sulle cartelle, come Photo Mechanic. Il database interno serve solo a cache, diario e sessioni.
- Niente sviluppo creativo (curve, preset): è il lavoro di Lightroom e Capture One.
- Niente cloud obbligatorio, niente account.
- Niente scarto automatico di serie.
- Niente analisi che faccia aspettare prima di iniziare: è il punto debole comune di tutte le app AI.
- Niente limiti all'esportazione dei metadati nella beta: diverse app indie fanno pagare l'XMP, per noi è una leva.
- Niente librerie GPL (Exiv2, codice di digiKam). LibRaw (LGPL/CDDL) si potrebbe usare, ma con `CIRAWFilter` serve poco. ExifTool solo nei test e, al massimo, per il pannello metadati completo: troppo lento durante lo scorrimento.
- iPad, collaborazione e firma C2PA non prima della 1.0: la domanda è bassa rispetto a velocità, fuoco e metadati.

---

## 7. Architettura

Stessa impostazione di Rename: logica in RawlineKit, interfaccia nell'app, così la modalità Seleziona di RawLine e un'eventuale versione Windows riusano tutto.

| Modulo (nuovo o esistente) | Contenuto |
|---|---|
| `MediaMetadata` (esiste) | Lettura EXIF, IPTC, XMP; si aggiungono i MakerNote per marca (punto AF, raffica, voti in macchina) |
| `RenameEngine` (esiste) | Riuso di `TwinGroup`, `CameraBodies`, `CaptureTime` |
| **`MediaPreview`** (esiste dalla fase 0) | Lettori delle anteprime per TIFF, CR3, RAF, ORF, RW2; decodifica, cache su disco e in memoria, precaricamento (anche della foto piena in `Z`) |
| **`Diagnostics`** (esiste dalla fase 0) | Registro di errori, lentezze e segnalazioni in `~/Library/Logs/RawLine Selects/events.jsonl` |
| **`CullCore`** (nuovo) | Modello di valutazione, sessioni, raffiche, filtri, cronologia annulla/ripristina; senza dipendenze da macOS |
| **`XMPWriter`** (nuovo) | Aggiornamento chirurgico dei sidecar, profili delle etichette, scrittura atomica, diario |
| **`CullAssist`** (nuovo) | Analisi con Vision e Core ML: volti, occhi, nitidezza, somiglianza |
| **`RawlineAppKit`** (nuovo, da Rename) | Tema grafite, beta, crash, aggiornamenti, guida, apertura dal Finder: comune a tutte le app della famiglia |
| **Servizio di decodifica** (XPC, nuovo) | RAW e analisi in un processo separato: un file che fa crashare il decoder non chiude l'app (sezione 13) |
| App **RawlineSelects** | SwiftUI per finestre, pannelli e impostazioni; visore in AppKit e Metal per la velocità |

Requisito: macOS 15 o successivo, come RawlineKit.

### Distribuzione e prezzo (deciso)

- Fuori store, come Rename: Developer ID, notarizzazione, Sparkle, download da rawline.app. Nessuna sandbox: accesso libero a schede, dischi esterni e NAS.
- Beta gratuita. Il prezzo si decide quando nascerà RawLine, l'app unica.
- Per riferimento, i concorrenti (novembre 2026): Photo Mechanic è passato all'abbonamento nel novembre 2023 (standard $149/anno o $299 perpetua; Plus $249/anno o $399 perpetua), e alcuni utenti di lunga data l'hanno lasciato per questo; Narrative da $10 a $60 al mese con l'annuale, senza più piano gratuito; Aftershoot Select $10/mese con l'annuale; Imagen $12/mese; FilterPixel da $14,99/mese; Excire Foto 2027 $249 una tantum; FastRawViewer $23,99; Palomino $29,99; BurstPick $89.

### Pezzi in comune con RawLine Rename

Oggi tema, segnalazione dei problemi, controllo dei crash, aggiornamenti e guida vivono dentro l'app Rename. Per Selects non vanno copiati: si spostano in un modulo comune, **`RawlineAppKit`**, usato da tutte le app della famiglia e poi da RawLine.

| Pezzo di Rename | Cosa fa | In Selects |
|---|---|---|
| `Theme.swift` | Accento grafite, colori di avviso ed errore, pulsante pieno grafite, link sottolineati | Identico |
| `BrandMark`, icona, `EmptyStateView` | Marchio, accoglienza con cartelle recenti | Stesso schema, con le cartelle di foto recenti |
| `BetaReporter`, `CrashWatch`, `BetaDiary`, `ReportProblemView` | Si accorge dei crash, raccoglie lo stack, finestra "Segnala un problema" | Identici: in beta servono più che mai |
| `AppUpdater` (Sparkle) | Controllo degli aggiornamenti a ogni avvio | Identico, con il proprio feed su rawline.app |
| `AppDelegate`: "Apri con", Dock, Servizi del Finder | Apre ciò che si trascina sull'icona | Stesso codice, con la regola di Photo Mechanic (sezione 12) |
| `GuideView`, `SettingsView`, `AppLanguage` | Guida alla prima apertura, impostazioni, italiano e inglese | Stessa struttura |
| `ClockOffset`, `BodyTable` | Corpi macchina AP1/AP2 e scarto degli orologi | Condivisi: le sigle dei corpi impostate in Rename valgono anche in Selects |

---

## 8. Piano di sviluppo

| Fase | Contenuto | Esito |
|---|---|---|
| **0. Prova di velocità** | Lettore del JPEG incorporato ARW, visore Metal, precaricamento; misura sui 2.000 ARW dell'Alpha 1. In parallelo: spostare tema, beta e aggiornamenti di Rename in `RawlineAppKit` | Numeri reali contro Photo Mechanic sullo stesso Mac. Se non vinciamo qui, il resto non conta |
| **1. Visore e valutazione** | Lo scrittore XMP parte solo dopo i file campione di Lightroom con uno scarto, per conoscere il valore di `xmpDM:good`. Si apre con una settimana di **raccolta dei campioni e prove di compatibilità**: RAW per marca, XMP da Lightroom 15 e Capture One, confronto con ApolloOne. Poi: lettori delle anteprime per tutte le marche verificati sui file veri, indice della dimensione dell'anteprima con il cartello onesto, benchmark per marca; griglia, foto singola, stelle, colori, scarto, avanzamento automatico, annulla, diario; i livelli 0 e 1 con Esc e il percorso in alto (4.10), menu della percentuale di zoom (4.3); scrittore XMP chirurgico e profili etichette aggiornati (4.6); lettura dei voti esistenti; spostamento delle scartate in `_Scartate` o nel Cestino | Già utilizzabile sui lavori veri, con ogni marca |
| **2. Fuoco e confronto** | Punto AF Sony con elenco pubblico dei corpi verificati; zoom 100% dal RAW quando l'anteprima è piccola; Canon e Nikon Z sperimentali; confronto 2–4 sincronizzato, lampeggio, zoom intelligente; raffiche per ritmo, numero di sequenza e corpo macchina, con pile, panoramica e promemoria (4.4), il livello 2 delle raffiche (4.10) e la griglia che non si muove (14.1); focus peaking e mappa di nitidezza; ordinamento della raffica a richiesta; promozione dei voti dati in macchina; filtri; AP1/AP2 | Beta 1, pubblica |
| **3. Video e azioni** | Clip nella griglia, J-K-L, azioni sulla selezione, profilo etichette personalizzato (quelli pronti sono in fase 1), scorciatoie tipo PM/LR; navigator completo con albero, preferiti e schede (4.10; *fase scelta da me*, perché per Andrea è utile ma non essenziale) | Versione 1.0 |
| **4. Aiuti locali** | Zoom che segue il soggetto, salto e striscia dei volti, lampeggio allineato, livella, scene per somiglianza (nessuna selezione assistita) | 1.1 |
| **5. Extra** | Duello, obiettivo di consegna, controller da gioco e MIDI, plugin Lightroom, geotag da GPX, statistiche, punto AF Fuji/OM/Panasonic/Pentax, RAW 9, selezione da scheda e passaggio a Importa | 1.2 e oltre |

---

## 9. Decisioni

**Prese l'8 novembre:**
1. **Scarto e scelta:** come i flag di Lightroom (`P`, `X`, `U`), scritti in `xmpDM:pick` (4.2).
2. **Tasti:** come Lightroom. `1`–`5` stelle, `0` toglie le stelle, `6`–`9` rosso, giallo, verde, blu; viola senza tasto. Stelle e colori insieme, non in alternativa come in Photo Mechanic. `A` mostra e nasconde il punto AF.
3. **Etichette:** profili Lightroom italiano e inglese entrambi previsti (deciso il 9 nov); si propone quello riconosciuto dagli XMP già presenti, altrimenti quello della lingua di macOS; sempre `photoshop:LabelColor` (4.6); interfaccia in italiano e inglese secondo la lingua di macOS, come Rename (4.6).
4. **Niente selezione assistita.** L'AI locale aiuta solo a guardare più in fretta (5.1).
5. **Zoom intelligente:** resta dentro la raffica, segue il soggetto, si azzera uscendo dalla raffica (4.3).

**Prese il 9 novembre:**
6. **Tasti dello zoom in SelectsLab:** `Z` tutto schermo nitido, `⇧Z` 100% con clic e trascina (⌘Z resta Annulla), clic tenuto premuto = lentino al 100%; passare sopra senza cliccare non fa niente.
7. **Tutte le marche** (sezione 0): supporto multimarca e metadati verificati salgono in fase 1.
8. **Specifica aggiornata** con il rapporto [[Mercato culling fotografico]].
9. **Ordinamento della raffica a richiesta** per dettaglio nel riquadro AF o in una zona scelta: solo per decidere cosa confrontare, senza numeri né badge né scarti, sempre uguale a parità di file (5.1).
10. **Raffiche dentro la selezione unica** (4.4): pila con numero di scatti e durata; Invio o doppio clic per entrare, Esc per uscire; dentro, panoramica scorrevole e scatto grande; `←`/`→` non escono mai dalla raffica; niente va in `X` da solo; promemoria per le raffiche mai guardate.
11. **Zoom** (4.3): il 100% è un pixel per pixel; menu della percentuale in basso a sinistra, valido per la sessione; si riparte dal 100% a ogni avvio.
12. **Navigator e tre livelli** (4.10): barra laterale con cartelle e preferiti, schede in alto; Esc risale di un livello e al livello più alto non fa niente; ⌘W risale come Esc nella foto e nella raffica, e chiude la scheda solo nella griglia.
13. **Marcatura sulla pila chiusa** (4.4): tocca solo gli scatti senza marcatura, e l'app dice quanti scatti già marcati ha lasciato com'erano.
14. **Etichette Lightroom italiano e inglese** entrambe previste; **il confronto resta com'è**, da 2 a 4 foto (4.6, 14.2).
15. **`P` dentro la raffica conferma lo scatto ed esce**; stelle, colori, `X` e `U` lasciano dentro (4.4).
16. **Acceleratore hardware** come impostazione attivabile e disattivabile, accesa di serie (3).

**Confermata l'8 novembre:** la vista foto scura di serie (sezione 11).

**Ancora da confermare:**
- I file campione di Lightroom 15 e Capture One (4.6): servono prima di scrivere il codice dei metadati.

---

## 10. Cosa dicono i fotografi: i problemi da risolvere

Reddit blocca sia i motori di ricerca sia il browser integrato, quindi non sono riuscito a leggerlo (anche Fred Miranda e BCG nella ricerca del 9 novembre): le frequenze sono stime, non conteggi. Ho usato i forum ufficiali (Camera Bits, Adobe Community, Capture One, FastRawViewer), i forum indipendenti (BCG, TalkPhotography, DPReview, MacRumors) e le recensioni degli utenti (G2, Trustpilot). Ogni problema ha la sua risposta in Selects.

| # | Problema riportato | Dove | La risposta di Selects |
|---|---|---|---|
| 1 | **Lightroom lento tra una foto e l'altra**: in alcuni casi 5–7 secondi, in uno anche 20 | Adobe Community | Anteprima incorporata e precaricamento; obiettivo sotto 16 ms (sezione 3) |
| 2 | **Lightroom non salva il flag Scelta nell'XMP** se il campo manca e nient'altro è cambiato (bug di Lightroom 13.2) | Adobe Community | Ogni valutazione scritta subito e verificata; diario locale; scarto e scelta scritti in campi che Lightroom legge davvero (4.2 e 4.6) |
| 3 | **Etichette colore perse** tra Photo Mechanic, Bridge, Lightroom e Capture One, per i nomi tradotti | Adobe Community, Capture One, FastRawViewer | Profili delle etichette per programma e per lingua (4.6) |
| 4 | **Photo Mechanic su macOS Sequoia**: rotelle da 5 a 30 secondi tornando all'app con ⌘-Tab, blocchi aprendo cartelle vuote; nessuna soluzione nel forum | Forum Camera Bits | Nessun lavoro sul thread principale; niente "ripasso della cartella" bloccante al ritorno nell'app: la sorveglianza dei file lavora in sottofondo (sezione 13) |
| 5 | **Svuotare la cache all'uscita blocca Photo Mechanic** | Forum Camera Bits | Cache con dimensione massima, pulita in sottofondo mentre l'app lavora, mai all'uscita |
| 6 | **Assisted Culling di Lightroom va in crash** durante l'analisi, a volte dopo circa 30 foto (anche con perdite di memoria su Windows) | Adobe Community | Analisi in un processo separato: se si blocca, l'app non se ne accorge e riprende da sola (sezione 13) |
| 7 | **Assisted Culling parte da solo** e analizza tutta la raccolta invece della selezione | Adobe Community | Nessuna selezione assistita; gli aiuti locali lavorano in sottofondo, senza bloccare e senza decidere |
| 8 | **Cursori AI a scatti**: con la soglia di fuoco a 20 escono 9 scarti, a 30 ne escono 387; con i valori predefiniti Assisted Culling ha scartato tutte le 1.877 foto di un evento | Adobe Community | Nessuna soglia e nessuno scarto automatico (decisione 4); gli strumenti mostrano, il fotografo decide |
| 9 | **Punteggi incoerenti**: foto segnata sfocata con i volti a fuoco, punteggi diversi tra due analisi, occhi riconosciuti bene circa 7 volte su 10 | Adobe Community | Nessun punteggio sulla foto; punto AF, zoom sul volto e mappa di nitidezza per vedere da sé |
| 10 | **Assisted Culling non mostra scelte e scarti** nella vista singola e nella filmstrip | Adobe Community | Stato sempre visibile, in ogni vista, con la stessa grafica |
| 11 | **Lo zoom si azzera passando alla foto successiva**: "rende quasi impossibile" controllare la nitidezza | Adobe Community | Zoom sincronizzato di serie nelle raffiche (4.3) |
| 12 | **Zoom sul volto**, con più persone non si sa su quale | Adobe Community | Primo zoom sul punto AF; un tasto passa al volto successivo |
| 13 | **"Trovami le 5 più nitide su una raffica di 20"**, e per gli animali "l'uccello a fuoco, non il ramo" | Adobe Community, BurstPick | Lampeggio e confronto allo stesso zoom sul punto AF; ordinamento a richiesta per dettaglio nel riquadro AF, senza badge né scarti (5.1) |
| 14 | **AI tarata sulle persone**: non vede gli occhi negli uccelli lontani | Adobe Community, MacRumors | Rilevamento soggetto generico di Vision (persone, animali, oggetti), non solo volti; per sport e animali conta il punto AF |
| 15 | **L'AI sceglie foto che non vuoi** e perde i momenti emotivi | G2 (Aftershoot) | Nessuna scelta automatica, nessuna prima passata (decisione 4) |
| 16 | **"Una foto che sembra storta potrei averla fatta apposta"** | DPReview | Nessuno scarto automatico; sfocato voluto e mosso creativo vanno distinti dal fuoco mancato |
| 17 | **Le foto scelte non arrivano tutte in Lightroom** (42 importate su 125) | Adobe Community (Aftershoot) | Esporta e verifica: dopo il passaggio, conta i file arrivati e avvisa se ne manca qualcuno |
| 18 | **Abbonamenti ovunque**; alcuni hanno lasciato Photo Mechanic quando è passato all'abbonamento | Fred Miranda, Fstoppers, PetaPixel | Beta gratuita; poi app singole gratuite e RawLine a pagamento |
| 19 | **Interfaccia di Photo Mechanic "ferma al 2010"** | Adobe Community | Interfaccia RawLine: grafite, sobria, nativa (sezione 11) |
| 20 | **Importazione lenta con molte schede**, e manca un unico passo per copiare, rinominare e fare il backup | Recensione 2026 | Selezione dalla scheda subito; più avanti RawLine unisce Importa, Rinomina e Seleziona |
| 21 | **Cartelle su NAS lente** da sfogliare | FastRawViewer | Cache locale delle anteprime e precaricamento più profondo sulle sorgenti lente (5.4) |
| 22 | **Richieste da FastRawViewer**: valori RGB sotto il cursore, filtri EXIF, HEIC, recupero dell'ultima selezione | FastRawViewer | Filtri EXIF (4.5), HEIC (4.1), "ripristina selezione precedente" con ⌘Z, valori sotto il cursore nel pannello dettagli |
| 23 | **Tasti bloccati in modalità Cull** di Capture One; Esc premuto per sbaglio fa uscire | Capture One | Tutte le scorciatoie attive in ogni vista; Esc torna indietro di un livello, mai fuori dal lavoro |
| 24 | **Ripetizione dei tasti a scatti** tenendo premuto Z o X in Lightroom | Adobe Community | La ripetizione del tasto non accoda lavoro: si salta direttamente alla foto pronta più vicina |
| 25 | **Lightroom lentissimo con i file grandi** (Sony A1, DJI Mavic 4 Pro) dalla scheda dopo un aggiornamento; FastRawViewer lento sui DNG convertiti da Adobe | Adobe Community, FastRawViewer | Solo i byte dell'anteprima; benchmark per marca a ogni build |
| 26 | **Voti dati in macchina persi** all'importazione: Canon R7, R6, 5D IV, Nikon D850, Fujifilm GFX | Adobe Community, Canon community | Promozione dei voti in macchina, da entrambe le schede e da RAW e JPEG (4.2) |
| 27 | **RAW di corpi nuovi o compressi che non si aprono**: Nikon HE "file corrotto" nelle app LibRaw, RAF compressi su macOS, CR3 dei corpi nuovi in ritardo; "datemi almeno il JPEG incorporato" | Tonfotos, Apple Discussions, Canon community | Lettori propri delle anteprime per ogni formato e cartello "RAW non ancora leggibile" (3, 4.1) |
| 28 | **Capture One non rilegge `xmp:Label`** come lo scrive, e il quinto colore deve chiamarsi Pink o Purple; `.XMP` maiuscolo che rompe il collegamento | Capture One community | Profili Capture One e lettura tollerante dei nomi dei sidecar (4.6) |
| 29 | **Controller:** tasti diretti per le stelle, più/meno una stella sulle manopole; per il gamepad su Mac serve un'app a pagamento | Forum vari | GameController e MIDI nativi, comandi relativi (5.3) |

---

## 11. Stessa famiglia di RawLine Rename

Chi ha usato Rename deve sentirsi a casa in Selects dal primo secondo.

**Uguale a Rename**
- **Colori:** accento grafite `#3A3A3C` (bianco caldo `#E8E7E2` sul tema scuro), selezioni in grigio leggero come nel Finder, arancio per gli avvisi, rosso per gli errori. Verde e menta del marchio solo su logo, icona e sito.
- **Caratteri:** San Francisco per l'interfaccia, SF Mono per i nomi dei file.
- **Finestra:** barra laterale a sinistra (cartelle aperte, filtri con i conteggi, corpi AP1/AP2), centro di lavoro, pannello del file a destra, barra di stato in basso. Si apre pulita, con l'accoglienza e le cartelle recenti.
- **Un solo pulsante pieno** per vista, in grafite: in Selects è l'azione sulla selezione ("Sposta 87 tenute…").
- **Linguaggio:** frasi brevi e concrete in italiano e inglese; i messaggi dicono cosa è successo e cosa fare.
- **Sicurezza:** nessun file perso, tutto annullabile, cronologia.
- **Beta:** segnalazione dei problemi, controllo dei crash, aggiornamenti a ogni avvio, guida alla prima apertura.

**Diverso, perché il lavoro è diverso**
- **Tema scuro di serie** nella vista foto: per giudicare le foto il grigio neutro scuro è lo standard (Lightroom, Photo Mechanic, Capture One). Il resto dell'app segue il tema di sistema come Rename. Confermato l'8 novembre.
- **Colori delle etichette** visibili: sono un dato del lavoro, non decorazione. Restano piccoli (pallino o bordo sottile), mai fondi colorati pieni.
- **Schermo intero senza interfaccia** con un tasto: solo la foto.

---

## 12. Photo Mechanic: cosa teniamo

Andrea usa Photo Mechanic e ne apprezza il modo di lavorare. Questi comportamenti restano, a volte migliorati.

| Comportamento di Photo Mechanic | In Selects |
|---|---|
| **Trascini una foto sull'icona e si apre tutta la sua cartella** | Uguale: si apre la cartella e la foto trascinata è già selezionata e mostrata. Trascinando una cartella si apre la cartella; trascinando più foto di cartelle diverse si aprono quelle cartelle |
| **Provino (contact sheet) e finestra di anteprima separate** | Griglia e foto singola nella stessa finestra, passando con Invio / spazio; la foto singola si può staccare su un secondo schermo. Livelli ed Esc come in 4.10 |
| **Navigator, Favorites e schede delle cartelle** | Uguale, nella barra laterale e in alto (4.10) |
| **Tag binario (`T`)** con "seleziona taggate", "copia o sposta taggate" | Scelta (`T` di serie nel preset Photo Mechanic) con le stesse azioni |
| **Classi colore con i numeri** | Uguale nel preset Photo Mechanic, con i nomi compatibili con Lightroom |
| **Avanzamento automatico dopo tag, colore o stelle** | Uguale |
| **Lavora sulle cartelle, nessun catalogo da importare** | Uguale |
| **Selezione sulla scheda prima dell'importazione** | Uguale, e più avanti passaggio diretto a Importa di RawLine |
| **Correzione dell'ora di scatto** | Riusa lo scarto degli orologi di Rename |
| **Più fotocamere ordinate per ora reale** | Riusa `CameraBodies` e `ClockOffset` |
| **Scorciatoie personalizzabili** | Uguale, con preset pronti e tasti combinati |
| **Code replacement** (`\gf` → "Giulia Ferri") | Non in Selects: è lavoro dei metadati, arriverà con l'app Copyright e metadati |
| **Rinomina in importazione** | Passa a RawLine Rename con la selezione |

Cosa miglioriamo rispetto a Photo Mechanic: interfaccia moderna, punto AF, zoom intelligente, raffiche e confronto sincronizzato, aiuti locali che non giudicano, video, etichette compatibili, nessun blocco su Sequoia.

---

## 13. Stabilità: come non andare mai in crash

La stabilità si progetta, non si spera. Regole tecniche per tutto il codice di Selects:

1. **Il thread principale disegna e basta.** Lettura dei file, decodifica, scrittura XMP e analisi stanno tutte in coda di sottofondo. Un file lento o un disco che dorme non possono bloccare l'interfaccia (è il problema di Photo Mechanic su Sequoia).
2. **Decodifica in un processo separato** (servizio XPC) per i RAW e per le analisi di Vision. Se un file danneggiato o un decoder di Apple va in crash, muore il servizio, non l'app: il servizio si riavvia da solo e il file viene segnato come illeggibile. Su macOS 15.8 il decoder RAW di Apple si è bloccato per alcuni utenti in tutte le app (DPReview): questa è la protezione.
3. **Tempi massimi per ogni lettura.** Se un file non risponde entro pochi secondi, si passa oltre e lo si riprova dopo.
4. **Memoria a budget.** Cache in RAM con un tetto calcolato sulla memoria del Mac; si svuota prima di tutto quando macOS segnala memoria scarsa.
5. **Scritture atomiche e diario** (4.6): nessun crash può corrompere un XMP o perdere un voto.
6. **Dischi che spariscono** (scheda tolta, NAS che cade): l'app lo dice, tiene i voti nel diario e li scrive quando il disco torna.
7. **Test di resistenza** a ogni build: cartella da 20.000 file, file troncati e danneggiati, tutti i RAW di prova di ogni marca, tasto freccia tenuto premuto per 10 minuti, disco staccato durante la scrittura.
8. **Misure automatiche di velocità** (sezione 3): una build più lenta della precedente non si pubblica.
9. **Segnalazione dei crash** di Rename riusata: in beta ogni crash arriva con il suo stack.

---

## 14. Revisione del 9 novembre: cosa manca e cosa rendere più efficace

Andrea ha chiesto di rileggere tutto con un solo metro: Selects deve essere la migliore app di selezione sul mercato. Qui sotto ci sono le funzioni che mancavano e i punti in cui due funzioni si pestavano i piedi. **Sono tutte proposte mie, da confermare**, salvo dove è scritto il contrario. La regola usata per decidere: ogni passaggio deve togliere un tasto, un'attesa o un dubbio al fotografo, senza mai decidere al posto suo.

### 14.1 Funzioni che mancavano

| # | Funzione | Perché serve | Fase |
|---|---|---|---|
| 1 | **Raffiche per corpo macchina.** Una raffica contiene solo scatti dello stesso corpo (numero di serie, come AP1/AP2 in Rename) | Con due fotocamere sullo stesso momento, l'ordine per ora reale (4.5) mescola i fotogrammi: senza questa regola due raffiche diventano una pila sola, sbagliata | 2 |
| 2 | **Candidati dentro la raffica.** Nella panoramica, `⌘`+clic segna da 2 a 4 scatti; `C` li apre nel confronto sincronizzato sul riquadro AF, che si apre sopra il livello da cui parti; Esc torna alla raffica | Per scegliere 1 su 42 il passaggio decisivo è il confronto fra i 2–4 migliori momenti. Oggi raffica (4.4) e confronto (4.4) sono due mondi separati: così diventano un gesto solo | 2 |
| 3 | **Lampeggio con lo scatto vicino.** Dentro la raffica, un tasto alterna lo scatto corrente con quello prima o dopo, allo stesso zoom sul riquadro AF | A 30 fps due scatti vicini sono quasi uguali: è il modo più rapido di vedere quale ha il fuoco migliore. Il lampeggio c'era (4.3), ma senza dire con chi | 2 |
| 4 | **Stato "vista" per ogni foto.** Una foto è vista quando resta a schermo almeno 0,3 s nella foto grande o nella raffica. La copertina di una pila non conta: di una raffica contano solo gli scatti visti al livello 2 | Servono al contatore (4.5), al filtro "solo non viste", al promemoria delle raffiche (4.4) e a "riprendi dove eri" (4.9). Senza una definizione, ognuno conta a modo suo | 1 |
| 5 | **Indicatore "tutto salvato".** Nella barra di stato: "XMP: tutto scritto" oppure "12 in scrittura…"; a fine cartella e prima di "Apri in Lightroom" si aspetta che sia a zero | Il diario non perde niente, ma Lightroom legge i file: se lo apri mentre Selects scrive ancora, vedi voti mancanti e pensi a un bug (problemi 2 e 17 in sezione 10) | 1 |
| 6 | **Profilo etichette indovinato dai file.** Al primo avvio su una cartella già etichettata si propone il profilo che corrisponde ai nomi trovati (4.6) | Nei sidecar di Andrea c'è `Gialla`, non `Yellow`: con un profilo sbagliato le etichette scritte da Selects non si vedrebbero in Lightroom | 1 |
| 7 | **Griglia che non si muove.** Le raffiche si riconoscono in sottofondo, ma una pila non si forma mai sotto la foto che stai guardando e la foto selezionata non cambia mai posto | L'analisi dei metadati di 2.000 file richiede qualche secondo: se la griglia si riordina mentre lavori, perdi il punto | 2 |
| 8 | ~~Opzione "esci dopo la scelta".~~ **Sostituita (9 nov):** è il comportamento normale di `P` dentro la raffica (4.4) | Andrea usa stelle e colori per marcare più scatti, `P` per confermare lo scatto scelto | 2 |
| 9 | **Tasto tenuto premuto sulle pile** (fase 2). Tenendo premuta la freccia sulla griglia si passano le pile come un passo solo, e l'app non apre mai una raffica da sola | Coerenza con 4.4: la raffica si apre solo con Invio o doppio clic | 2 |
| 10 | **Etichette leggibili anche senza colori.** Accanto al pallino colorato, a richiesta, la lettera (R, G, V, B, Vi) | Il daltonismo riguarda circa un uomo su dodici: un'app per professionisti non può affidarsi solo al colore | 3 |

### 14.2 Funzioni da rendere più efficaci

- **Deciso con Andrea (9 nov): il confronto resta com'è** (4.4: da 2 a 4 foto, zoom sincronizzato), separato da sopravvivenza e duello. La proposta qui sotto non si fa; resta valida solo la regola che togliere una foto da una vista non la scarta mai.
- ~~**Confronto, sopravvivenza e duello (4.4, 5.2) diventano una cosa sola.** Tre modalità che fanno quasi lo stesso lavoro confondono. Proposta: un solo **confronto** da 2 a 8 foto, con zoom sincronizzato. `X` toglie la foto sotto il cursore e le altre si allargano: con 2 foto è il duello, con 8 è la sopravvivenza. **Togliere una foto dal confronto non la scarta:** si usa un tasto a parte (*mia proposta:* `/`), perché `X` resta lo scarto e niente va mai in `X` da solo (decisione 10). Il confronto passa da 2–4 a 2–8 foto: da confermare con Andrea. Tasti come Lightroom: `C` confronto, `N` sopravvivenza (stessa vista, partenza da più foto).~~
- **Il primo zoom deve essere utile anche senza punto AF.** Ordine di 5.1: punto AF, volto, soggetto, centro. Sui corpi senza punto AF verificato, nelle raffiche lo zoom resta dove l'hai lasciato (4.4): così almeno il secondo scatto è già nel posto giusto.
- **Il precaricamento segue il livello.** Nella griglia si preparano miniature e foto a misura di schermo vicine. Nella foto grande, le foto successive e la copertina delle pile. Dentro la raffica, gli scatti pieni nella direzione di marcia e, se lo zoom è acceso, il JPEG pieno (sezione 3). Una sola regola, scritta in un posto solo (`Prefetcher`).
- **Contatore che dice la verità sulle raffiche.** "Viste 312 di 1.840" conta gli scatti, ma una raffica di 42 passata senza entrare non è "vista". Il contatore separa: "foto viste 280 · raffiche guardate 12 di 15".
- **L'ordinamento per nitidezza (5.1) parte dai candidati.** Se hai segnato dei candidati (14.1, punto 2), l'ordine riguarda solo quelli; altrimenti tutta la raffica. Così l'aiuto lavora sul tuo giudizio, non al posto suo.
- **Avanzamento automatico coerente con i livelli.** `⇧`+tasto passa alla foto successiva nel livello in cui sei: nella raffica allo scatto dopo, e all'ultimo si ferma con l'avviso (4.4). Non esce mai dal livello; l'unica eccezione è `P` dentro la raffica, che conferma lo scatto e porta fuori (4.4). I tasti si riconoscono dal codice del tasto più il vero `⇧`, non dalla lettera: col Blocco maiuscole `z` non deve diventare `⇧Z`.

Restano da assegnare i tasti di lampeggio, ordinamento della raffica, volto successivo, focus peaking, barra informazioni e schermo intero senza interfaccia: li sceglie chi costruisce, senza toccare quelli già decisi e partendo da quelli di Lightroom quando esistono.

### 14.3 Debug in tre passaggi (9 novembre)

1. **Coerenza della spec**, letta da un revisore come se dovesse costruire l'app: 9 contraddizioni corrette (la più grave: nel confronto unificato `X` avrebbe scartato le foto escluse), più una decina di punti da indovinare chiariti (fasi dei livelli, gesti sulle pile, cosa conta come "vista", Blocco maiuscole, lentino al 100%).
2. **Revisione del codice** del ramo `selects/fase-0`: corretti un crash con CR3 costruiti apposta, i RAF verticali ruotati due volte, un rallentamento delle Sony con la sola anteprima 1616 sugli schermi grandi, letture inutili da 8 MB, file segnati per sempre illeggibili per un JPEG incorporato rovinato, lavoro sul disco nel thread principale di SelectsLab (commit `90bb55d`).
3. **Prove di resistenza:** misure su 50 ARW veri dell'Alpha 1 dal disco di backup (navigazione pronta al 100%, schermo 125 ms per foto nascosti dal precaricamento) e 10.800 copie troncate o rovinate di RAW veri di 13 marche, in 5 secondi, senza crash né blocchi.

### 14.4 Cosa resta da decidere con Andrea

1. ~~La lingua delle etichette~~: deciso, italiano e inglese (4.6).
2. ~~Unire confronto, sopravvivenza e duello~~: deciso, il confronto resta com'è (14.2).
3. ~~Opzione "esci dopo la scelta"~~: deciso, `P` dentro la raffica conferma lo scatto ed esce (4.4).

---

## Fonti

Il rapporto completo del 9 novembre, con tutte le fonti citate nel testo, è [[Mercato culling fotografico]] (`reports/Mercato culling fotografico.md`); le note di ricerca sono in `research_notes/Mercato culling fotografico/`.

- [Narrative: Best Photo Culling Software 2026](https://narrative.so/blog/best-photo-culling-software)
- [Narrative Select, piani](https://narrative.so/select/pricing/)
- [Aftershoot: Best culling software](https://aftershoot.com/blog/best-culling-software/)
- [Imagen: Best AI photo culling software 2026](https://imagen-ai.com/valuable-tips/best-ai-photo-culling-software-2026/)
- [CYME: Best Photo Culling Software for Mac 2026](https://cyme.io/en/blog/best-photo-culling-software/)
- [Camera Bits: Color Class Ratings](https://docs.camerabits.com/support/solutions/articles/48001142942)
- [Camera Bits: scorciatoie personalizzabili, supporto AVIF](https://home.camerabits.com/photo-mechanic-update-with-new-custom-keyboard-shortcuts-avif-support-and-more/)
- [PetaPixel: Photo Mechanic 6 fino al 300% più veloce](https://petapixel.com/2019/04/02/photo-mechanic-6-up-to-300-faster-brings-new-ui-and-features)
- [Adobe: Assisted Culling in Lightroom Classic](https://helpx.adobe.com/lightroom-classic/help/assisted-culling.html)
- [Adobe Design: Behind the design, Assisted Culling](https://adobe.design/ideas/behind-the-design-assisted-culling-in-adobe-lightroom)
- [Adobe Bridge: anteprima e confronto](https://helpx.adobe.com/bridge/using/preview-compare-images-bridge.html)
- [Capture One: Cull View](https://support.captureone.com/hc/en-us/articles/8265235276957-Cull-View)
- [FastRawViewer: funzioni](https://www.fastrawviewer.com/features)
- [FilterPixel vs Aftershoot](https://filterpixel.com/filterpixel-vs-aftershoot)
- [RawCull: punti di fuoco](https://deploy-preview-3--rawcull.netlify.app/docs/focuspoints) e [parser MakerNote Sony](https://rawcull.netlify.app/blog/2026/03/25/sony-makernote-parser)
- [ExifTool forum: punto AF Sony α7 IV](https://exiftool.org/forum/index.php?msg=77145)
- [s_afv, visualizzatore AF Sony](https://github.com/SK-Hardwired/s_afv)
- [FastRawViewer: etichette XMP compatibili con C1 o LR, non entrambi](https://www.fastrawviewer.com/node/395)
- [Adobe Community: etichette colore tra Photo Mechanic e Lightroom](https://community.adobe.com/questions-675/color-label-not-matching-when-importing-from-photomechanic-984088)
- [KDE bug 412922: xmp:Label e colori non standard](https://bugs.kde.org/show_bug.cgi?id=412922)
- [Apple: CalculateImageAestheticsScoresRequest](https://developer.apple.com/documentation/vision/calculateimageaestheticsscoresrequest.md)
- [Apple: DetectFaceCaptureQualityRequest](https://developer.apple.com/documentation/vision/detectfacecapturequalityrequest.md)

Fonti della sezione 10 (critiche degli utenti):

- [Camera Bits forum: PM quasi inutilizzabile da Sequoia](https://forums.camerabits.com/index.php?topic=16647.0)
- [Camera Bits forum: Sequoia e miniature video](https://forums.camerabits.com/index.php?topic=16399.0)
- [Camera Bits forum: pulizia della cache all'uscita](https://forums.camerabits.com/index.php?topic=11155.0)
- [Camera Bits forum: Sonoma 14.3](https://forums.camerabits.com/index.php?topic=16020.0)
- [DPReview: problemi di macOS Sequoia 15.8 con il decoder RAW](https://www.dpreview.com/forums/threads/macos-sequoia-15-8-problems.4867284/)
- [Adobe Community: feedback su Assisted Culling](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467/index2.html)
- [Adobe Community: Assisted Culling va in crash su Windows](https://community.adobe.com/bug-reports-674/p-lrc-v15-5-on-windows-assisted-culling-triggers-crash-and-memory-leaks-1637630/index3.html)
- [Adobe Community: flag non salvato nell'XMP](https://community.adobe.com/t5/lightroom-classic-bugs/flag-not-saved-to-xmp-if-xmp-pick-missing-from-file-metadata/idi-p/14479660)
- [Adobe Community: 20 secondi tra una foto e l'altra](https://community.adobe.com/t5/lightroom-classic-discussions/switch-from-one-photo-to-the-next-takes-20-seconds/m-p/14679279/highlight/true)
- [Adobe Community: tasti Z/X a scatti](https://community.adobe.com/questions-675/holding-z-or-x-with-caps-lock-causes-stuttering-during-rapid-culling-1637633)
- [Adobe Community: mantenere lo zoom nella filmstrip](https://community.adobe.com/feature-requests-681/p-maintain-zoom-level-when-culling-photos-using-the-filmstrip-661851)
- [Adobe Community: zoom sul volto](https://community.adobe.com/feature-requests-676/p-zoom-to-face-665738)
- [Adobe Community: le più nitide in una raffica](https://community.adobe.com/feature-requests-676/p-culling-tools-to-pick-sharpest-image-665132)
- [Adobe Community: selezione AI delle raffiche per la fauna](https://community.adobe.com/feature-requests-681/p-ai-assisted-wildlife-burst-culling-in-lightroom-1628270)
- [Adobe Community: Aftershoot e importazione in Lightroom](https://community.adobe.com/questions-675/import-issues-aftershoot-to-lightroom-classic-964796)
- [Capture One: limiti delle scorciatoie in Cull](https://support.captureone.com/hc/fr/community/posts/7648346238877-Capture-One-23-Cull-Function-Keyboard-Shortcut-Restriction)
- [FastRawViewer: richieste di funzioni](https://fastrawviewer.com/node/33?page=3)
- [G2: recensioni di Aftershoot](https://www.g2.com/products/aftershoot)
- [DPReview: selezione automatica?](https://www.dpreview.com/forums/threads/automated-photo-culling.4764439/)
- [PetaPixel: Photo Mechanic passa all'abbonamento](https://petapixel.com/2023/11/15/photo-mechanic-caves-to-industry-trends-shifts-to-subscription-model)
- [Baty.net: Photo Mechanic 2024](https://baty.net/2024/06/photo-mechanic-2024)
- [BurstPick su AlternativeTo](https://alternativeto.net/software/burstpick/about/)

Fonti per scelta e scarto di Lightroom (4.2, 4.6):

- [Adobe: flag, etichette e stelle in Lightroom Classic](https://helpx.adobe.com/lightroom-classic/desktop/organize-photos-in-lightroom-classic/flag-label-rate-photos.html)
- [Adobe: scorciatoie di Lightroom Classic](https://helpx.adobe.com/lightroom-classic/desktop/introduction-to-lightroom-classic/keyboard-shortcuts.html)
- [Rawtonic PR 508: sidecar di Lightroom Classic e Capture One](https://github.com/rawtonic-app/rawtonic/pull/508)
- [Photopipe PR 233: flag scelta e scarto](https://github.com/RaphaelMitas/photopipe/pull/233)
- [Pickture: doppia convenzione XMP](https://github.com/0xDAFE/pickture/issues/5)
