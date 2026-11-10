# Raggruppamento automatico di raffiche, quasi-doppioni, bracketing e panorami: le app a confronto e le tecniche on-device su macOS

Note di ricerca, 10 novembre 2026. Legenda: **[UFFICIALE]** viene da documentazione o pagine del produttore; **[TERZI]** viene da recensioni, forum o concorrenti; **[INFERITO]** è un ragionamento mio o un ricordo non verificato in questa sessione.

## 1. Come raggruppano le singole app (cosa, come, automatico o regolabile, presentazione, azioni, sopravvivenza in Lightroom)

### Takeaway
Quasi tutte le app di culling basate sull'AI (Narrative, Aftershoot, FilterPixel, Imagen, Excire, Peakto) raggruppano per **somiglianza visiva**, spesso limitata a una finestra temporale. La sensibilità si regola con un cursore o con preset a tre livelli. All'interno del gruppo si sceglie la foto migliore. Lightroom Classic invece raggruppa **solo in base all'intervallo di tempo tra gli scatti**, ed è proprio lì che sbaglia con bracketing e panorami. Nessuna delle fonti trovate dice che un'app di terze parti riesca a portare in Lightroom delle *pile* vere e proprie. Le app passano soltanto voti, etichette e flag tramite XMP.

### Cited Findings

**Lightroom Classic**
- [UFFICIALE] "Auto-Stack by Capture Time" lavora su una cartella o una collezione intera, a prescindere dalla selezione. Il parametro "Time Between Stacks" va da 0 secondi a 1 ora. Si apre una nuova pila quando la foto successiva ha un'ora di scatto distante dalla precedente almeno quanto l'intervallo impostato. Adobe lo indica per raffiche, bracketing e panorami. — [Adobe Help: Group photos into stacks](https://helpx.adobe.com/lightroom-classic/desktop/organize-photos-in-lightroom-classic/grouping-photos-stacks.html)
- [TERZI] L'auto-stack non si può applicare all'importazione: si lancia solo su una cartella o una collezione già presente. — risposta in forum riportata dal riepilogo di ricerca, [Adobe Help (stessa pagina)](https://helpx.adobe.com/lightroom-classic/help/grouping-photos-stacks.html) e [PetaPixel 2017](https://petapixel.com/2017/09/18/harnessing-power-auto-stacking-lightroom/)
- [TERZI] Bug segnalati: foto separate da più dell'intervallo impostato finiscono comunque nella stessa pila. A volte "Export as Catalog" o una reimportazione con "Scan for metadata updates" disattivato risolve il problema. Un utente sospetta i DNG di DxO PureRaw, ma è solo un'ipotesi. — [Adobe Community bug 12390600](https://community.adobe.com/t5/lightroom-classic-bugs/auto-stack-by-capture-time-sometimes-stacks-photos-incorrectly/idi-p/12390600)
- [TERZI] Con il bracketing raggruppa spesso troppe o troppe poche esposizioni, perché misura il tempo *tra* gli scatti e non la durata di ciascuno: le pose lunghe ingannano il calcolo. Gli utenti chiedono un raggruppamento "per numero di foto" o basato sull'AI. Il plugin "Any Source" viene citato come più bravo su queste sequenze. — [Feature request: better auto stacking for bracketing, HDR, focus stacking and panoramas](https://community.adobe.com/feature-requests-676/p-better-auto-stacking-for-bracketing-hdr-focus-stacking-and-panoramas-666365); [Auto stacking doesn't group bracketed photos](https://community.adobe.com/questions-675/auto-stacking-doesn-t-group-bracketed-photos-965830); [Bug: auto stack panorama HDR not grouping correctly](https://community.adobe.com/bug-reports-557/auto-stack-panorama-hdr-not-working-doesn-t-group-correctly-1528597); [AI-supported HDR/panorama stacking (request)](https://community.adobe.com/feature-requests-676/p-ai-supported-hdr-panorama-stacking-665848)
- [TERZI] Sui cataloghi grandi la funzione è molto lenta. — [Adobe bug: auto stack by capture time is extremely slow](https://community.adobe.com/bug-reports-674/p-auto-stack-by-capture-time-is-extremely-slow-663099)
- [TERZI] AutoHDR, servizio esterno per immobiliari, dichiara un raggruppamento dei bracketing "vision-based". — [AutoHDR FAQ](https://faq.autohdr.com/does-autohdr-auto-merge-hdr-brackets)

**Narrative Select**
- [UFFICIALE] Le "Scenes" sono insiemi di immagini molto simili, in ordine di scatto. Si aprono con S quando l'elaborazione è finita. Ordinando per "Scene rank", in ogni scena le foto migliori compaiono per prime. Una volta analizzate dall'AI, le scene non si possono riorganizzare a mano. — [Narrative help: Using Scenes](https://help.narrative.so/en/articles/8119179-using-scenes-in-select)
- [UFFICIALE] Il pannello "Close-ups" mostra i ritagli di tutti i volti rilevati nell'immagine, accanto all'immagine intera. È uno strumento per giudicare occhi e messa a fuoco, non un raggruppamento. — [Narrative: Scenes view](https://narrative.so/select/scenes-view); [Getting started with Select](https://help.narrative.so/en/articles/7337363-getting-started-with-select)
- [CONFLITTO] In quale piano siano incluse le Scenes: il help center dice Standard/Premium/Ultra, una pagina marketing dice solo Pro. — [help center](https://help.narrative.so/en/articles/8119179-using-scenes-in-narrative) vs [narrative.so/select/scenes-view](https://narrative.so/select/scenes-view)

**Aftershoot**
- [UFFICIALE, note di rilascio] Il preset di raggruppamento "Similarish" ha sostituito "Strict": crea gruppi più grandi e quindi meno foto selezionate. — [Aftershoot October Culling Release](https://events.aftershoot.com/?p=43908)
- [UFFICIALE, pagina comparativa] Il rilevamento dei doppioni è descritto come "advanced grouping with configurable sensitivity" ed è indicato come beta. "Auto Target" e "Cull to Target" (10–60%) decidono quanti gruppi creare e quanto grandi. — [Aftershoot vs Photo Mechanic](https://aftershoot.com/aftershoot-v-s-photomechanic/); [Setting culling preferences](https://support.aftershoot.com/en/articles/6508163-setting-your-culling-preferences-in-aftershoot)

**FilterPixel**
- [TERZI, da sito concorrente] "Autogroup" crea pile di foto simili nella griglia. Si sceglie con P e si salta il resto del gruppo con Tab. L'export manda le scelte a Lightroom; senza Lightroom le foto finiscono in una cartella "FP/Accepted". — riepilogo da [Imagen: FilterPixel vs Imagen](https://imagen-ai.com/post/filterpixel-vs-imagen/) e [FilterPixel blog](https://filterpixel.com/blog/posts/avoiding-analysis-paralysis-while-culling/)

**Imagen**
- [UFFICIALE] Il Culling Studio impila i doppioni e suggerisce la foto migliore di ogni pila in base a fuoco, espressione e composizione. La somiglianza si regola con "Less Similar / Similar / Very Similar". Voti ed etichette vengono scritti in XMP e Lightroom li legge. — [Imagen: stop scrolling through duplicate photos](https://imagen-ai.com/ai-photo-editing-tools/stop-scrolling-through-duplicate-photos.md); [Imagen: remove duplicate photos](https://imagen-ai.com/solution/remove-duplicate-photos/); [Imagen: Lightroom assisted culling](https://imagen-ai.com/post/lightroom-assisted-culling.md)
- [TERZI] Esempio d'uso reale: un matrimonio da 7.500 foto ridotto a circa 1.500. — [Fstoppers](https://fstoppers.com/post-production/how-manage-thousands-photos-quickly-imagen-ai-and-lightroom-698500)

**Excire Search (plugin Lightroom) / Excire Foto**
- [UFFICIALE] Il cercatore di doppioni ha tre modalità. **Esatti**: hash binario identico. **Quasi-doppioni**: somiglianza visiva regolabile da "very strict" a "very loose", con "very strict" consigliato. **Serie**: immagini con ora di scatto vicina, con un cursore per l'intervallo. Si può fissare la dimensione minima del gruppo. I gruppi diventano **collezioni** e i doppioni si marcano con il flag "reject" e poi si eliminano con un clic. — [Excire Search: Duplicate finder](https://excire.com/en/tutorials/excire-search/duplikatefinder/); [Excire Search 2024 duplicate finder](https://excire.com/en/tutorials/excire-search-2024/duplikatefinder/); [Excire Foto 2024: find similar photos](https://excire.com/en/tutorials/excire-foto-2024/aehnliche-fotos-finden/)
- [TERZI] La ricerca degli esatti richiede l'accesso alle cartelle originali; le ricerche più larghe no, perché probabilmente usano le anteprime già indicizzate. — [ExpertPhotography: Excire Foto review 2026](https://expertphotography.com/excire-foto-review)

**Peakto**
- [TERZI, citato in un riepilogo] Ha un cursore "Similarity": a sinistra deduplica stretta, a destra culling largo. — dal riepilogo della ricerca su Aftershoot; non ho aperto direttamente una pagina di Peakto (vedi Gaps)

**Capture One**
- [TERZI] Non ha pile di immagini diverse alla maniera di Aperture o Lightroom. Ha solo le **varianti** dello stesso file, che si possono impilare ed espandere. Gli utenti chiedono da anni un "Auto Stacking Images By Time": la richiesta è "future consideration" e in un thread di supporto risulta "Not currently planned". — [C1 community: Please add stacking to the Library](https://support.captureone.com/hc/fr/community/posts/10520560920733-Please-add-stacking-to-the-Library); [C1 ideas FR-I-790](https://captureone.ideas.aha.io/ideas/FR-I-790); [Batch HDR / stacking bracketed photos](https://support.captureone.com/hc/fr/community/posts/12610065634589-Batch-HDR-Stacking-bracketed-photos); [Organizational Tools: Stacks and Variants](https://support.captureone.com/hc/en-us/community/posts/360014412358-Organizational-Tools-Stacks-and-Variants)

**Photo Mechanic**
- [TERZI, sito concorrente] ShotSelect dice di imitare la "Burst sequence" di Photo Mechanic, con frame entro 1 secondo l'uno dall'altro (soglia regolabile), e di scrivere XMP compatibili con Photo Mechanic. — [ShotSelect for sports](https://shotselect.pages.dev/for/sports)
- [TERZI] Chi lo usa prima di Capture One lo apprezza perché scrive i metadati sia nel JPG sia nell'XMP. — [C1 community: Stacking/Grouping images](https://support.captureone.com/hc/fr/community/posts/11048240325021-Stacking-Grouping-images)

**Apple Photos**
- [TERZI] L'album "Duplicati" compare solo quando ci sono doppioni e sparisce quando sono risolti; la scansione continua in background. Comprende sia file identici sia foto simili. "Unisci" tiene un elemento, combinando qualità e metadati, e manda gli altri in "Eliminati di recente". — [MacRumors](https://www.macrumors.com/how-to/find-duplicate-photos-mac); [MacMost](https://macmost.com/finding-duplicate-photos-in-the-photos-app.html); [Apple Community 256021424](https://discussions.apple.com/thread/256021424)
- [CONFLITTO] Dopo l'unione, la foto resta in tutti gli album? MacMost dice di sì, una risposta su Apple Community dice che la rimozione si propaga a tutti gli album. — [MacMost](https://macmost.com/finding-duplicate-photos-in-the-photos-app.html) vs [Apple Community 255735331](https://discussions.apple.com/thread/255735331)

**ApolloOne**
- [UFFICIALE, scheda App Store] Visualizzatore veloce, con confronto affiancato fino a 4 immagini per il culling e Split View con zoom e scorrimento sincronizzati. Non ho trovato alcuna funzione di pile automatiche o di raggruppamento per somiglianza. — [ApolloOne su Mac App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12); [MacUpdate](https://www.macupdate.com/app/mac/59148/apolloone)
- [TERZI] Optyx viene indicato come alternativa che raggruppa automaticamente le immagini simili e sceglie la migliore. — [SourceForge: ApolloOne vs Optyx](https://www.sourceforge.net/software/compare/ApolloOne-vs-Optyx/)

### Inferences
- [INFERITO] Lo schema comune è in due stadi: **finestra temporale**, poi **somiglianza visiva** dentro la finestra, con un preset di sensibilità a tre livelli e l'AI che propone la foto migliore del gruppo. Excire lo rende esplicito con la modalità "serie" a tempo separata da quella "somiglianza".
- [INFERITO] Le app di AI culling (Narrative, Aftershoot, Imagen, FilterPixel) mostrano i gruppi come "scene" o "pile" in un elenco o in una griglia compatta, e l'azione tipica è "scegli 1 per gruppo". Nessuna parla di gruppi *per bracketing HDR* o *per panorama* come tipi a sé: sono pensate per matrimoni ed eventi, non per l'outdoor.
- [INFERITO, da ricordo non riverificato] In Lightroom Classic, le finestre Photo Merge HDR e Panorama hanno l'opzione "Create Stack", che impila il file DNG risultante con gli originali. Da verificare nella versione corrente.
- [INFERITO] Per RawLine Selects c'è spazio per qualcosa che nessuno fa bene: riconoscere i **bracketing** usando l'EXIF (sequenza di ExposureBiasValue, modalità bracketing nei makernote) e i **panorami** controllando la sovrapposizione con la registrazione delle immagini.

### Gaps
- Photo Mechanic: non ho trovato documentazione ufficiale di Camera Bits su "Burst sequence" e raggruppamento; l'unica fonte è un concorrente.
- Peakto, Google Photos e Aftershoot (come si passano i gruppi a Lightroom): non ho aperto pagine ufficiali entro il limite di ricerca.
- Apple Photos: le raffiche (BurstUUID, foto chiave) non sono uscite nelle ricerche; dal ricordo, l'iPhone scrive un identificatore di raffica nei metadati Apple, ma non è verificato qui.
- Non ho trovato test indipendenti sull'accuratezza dei raggruppamenti di nessuna app.

## 2. Si possono passare le pile a Lightroom Classic? Soluzioni alternative

### Takeaway
No, non direttamente: le pile vivono nel catalogo `.lrcat` e non nell'XMP, e la cosa è confermata da Adobe Community, anche se con un thread datato. La strada percorribile è scrivere nell'XMP un **identificatore di gruppo**: parola chiave gerarchica, etichetta colore o campo IPTC. In Lightroom l'utente filtra per quel valore, oppure lancia l'auto-stack. In alternativa si separa il gruppo con nomi file o sottocartelle.

### Cited Findings
- [TERZI, thread datato 2011] Collezioni, pile, copie virtuali, flag e cronologia di sviluppo non finiscono nell'XMP. Gli utenti chiedono da anni di includerci pile e collezioni, con il loro ordine. — [Adobe Community idea: include additional metadata in XMP (flags, collections, VCs...)](https://community.adobe.com/t5/lightroom-classic-ideas/p-include-additional-metadata-in-xmp-flags-collections-vc-s-etc/idi-p/12662756)
- [UFFICIALE] L'auto-stack si lancia su una cartella o una collezione. Se ogni gruppo arriva in una sottocartella sua, l'utente può impilare cartella per cartella, oppure selezionare tutto e usare Group into Stack. — [Adobe Help](https://helpx.adobe.com/lightroom-classic/desktop/organize-photos-in-lightroom-classic/grouping-photos-stacks.html)
- [UFFICIALE Excire] Excire Search, che è un plugin interno a Lightroom e usa l'SDK, crea direttamente **collezioni** per gruppo, non pile. È la conferma pratica che un'app esterna non ha un modo pulito per creare pile. — [Excire duplicate finder](https://excire.com/en/tutorials/excire-search/duplikatefinder/)
- [UFFICIALE Imagen] Gli strumenti di AI culling passano a Lightroom voti ed etichette via XMP, non pile. — [Imagen: Lightroom assisted culling](https://imagen-ai.com/post/lightroom-assisted-culling.md)
- [TERZI] Esiste un plugin di terze parti ("Any Source", Auto Stack) che impila meglio delle funzioni native; i plugin Lua dell'SDK di Lightroom girano dentro Lightroom. — [Feature request thread](https://community.adobe.com/feature-requests-676/p-better-auto-stacking-for-bracketing-hdr-focus-stacking-and-panoramas-666365)

### Inferences
- [INFERITO] Soluzioni alternative, dalla più semplice alla più potente:
  1. **Parola chiave gerarchica nell'XMP** (`dc:subject` più `lr:hierarchicalSubject`), per esempio `RawLine|HDR|HDR-0007` o `RawLine|Pano|PANO-0003`. Lightroom la legge all'importazione; poi si filtra nel Library Filter, si seleziona e si fa Ctrl/Cmd+G. È la soluzione più robusta e non rovina nient'altro.
  2. **Etichetta colore alternata** per gruppo (gruppo A viola, gruppo B blu...): visibile subito in griglia, ma consuma un campo che l'utente usa per altro.
  3. **Nome file** con prefisso di gruppo, per esempio `HDR007_01.ARW`: richiede di rinominare, cosa naturale per RawLine Rename. L'ordine per nome tiene vicini i membri, e l'auto-stack per tempo con un intervallo corto funziona meglio.
  4. **Sottocartella per gruppo**: Lightroom importa ogni cartella separata, e l'auto-stack o il merge si fanno per cartella. È invasivo sulla struttura dei file.
  5. **Plugin Lua per Lightroom** (in futuro): un plugin RawLine che legge la parola chiave e crea davvero le pile. Da verificare se l'SDK Lua espone una funzione per creare pile; ricordo che non è documentata bene (vedi Gaps).
- [INFERITO] Per l'XMP dei RAW Sony, i campi vanno nel sidecar `.xmp`. Per i DNG si possono scrivere dentro il file, ma è meglio non toccarlo.

### Gaps
- Non ho trovato una conferma Adobe recente (2024–2026) che le pile siano rimaste solo nel catalogo; il thread 2011 e le richieste ancora aperte lo fanno supporre.
- Non ho verificato se l'SDK Lua di Lightroom Classic consenta di creare pile in modo programmato.
- Non ho trovato fonti su come Photo Mechanic o Aftershoot trasmettano i gruppi a Lightroom.

## 3. Tecniche on-device in Swift su macOS

### Takeaway
La base pratica è `VNGenerateImageFeaturePrintRequest` sulle anteprime JPEG incorporate, con distanza euclidea, una soglia intorno a **0,35** da tarare sui propri dati, e confronti solo dentro finestre temporali. Va affiancata da EXIF per il bracketing (bias di esposizione), da `VNHomographicImageRegistrationRequest` per confermare allineamento e sovrapposizione, e da `CalculateImageAestheticsScoresRequest` (macOS 15+) per proporre la foto migliore. MobileCLIP in Core ML è un'alternativa più semantica ma più pesante.

### Cited Findings

**Feature print di Vision**
- [TERZI, blog di sviluppatore, gennaio 2026] `VNGenerateImageFeaturePrintRequest` restituisce `VNFeaturePrintObservation`; la distanza si calcola con `computeDistance(_:to:)`, dove 0 vuol dire identico. Soglia predefinita **0,35**, ricavata etichettando a mano qualche centinaio di coppie. A 0,2 sfuggivano doppioni veri, a 0,5 si univano foto diverse della stessa scena generica. Prima si raggruppa per tempo (nuovo cluster se passano più di 10 minuti), poi si confronta solo dentro il cluster: 35.000 foto diventano circa 5.300 cluster con mediana di 2–3 foto, e i confronti scendono da circa 600 milioni a poche centinaia di migliaia. Cache SQLite di feature print e distanze tra coppie; una nuova scansione con la cache dura meno di un minuto. Il punteggio di qualità pesa nitidezza 25%, volti 30%, composizione 15%, risoluzione 20%, recenza 10%. Limiti: il modello è una scatola nera e a volte sceglie la foto sbagliata. — [ShutterSlim blog: Vision framework image similarity](https://shutterslim.com/blog/2026/01/18/vision-framework-image-similarity)
- [TERZI] Dalla revisione iOS 17 / macOS 14 i feature print sono vettori normalizzati di **768** valori; la distanza va da 0,0 a 2,0, e nel set di test il massimo era 1,4. — [MWM su Medium (solo l'estratto di ricerca, la pagina restituisce 403)](https://medium.com/@MWM.io/apples-vision-framework-exploring-advanced-image-similarity-techniques-f7bb7d008763)
- [TERZI] Immagini identiche che danno distanza diversa da zero, e `computeDistance` che fallisce: la causa tipica sono feature print di **revisioni diverse**. Bisogna fissare `revision` in modo esplicito e salvarla in cache insieme al vettore. — [Apple Developer Forums 732876](https://developer.apple.com/forums/thread/732876); [Forums 721760](https://developer.apple.com/forums/thread/721760)
- [TERZI] Altri esempi con le soglie: [Fritz.ai: Vision image similarity](https://fritz.ai/compute-image-similarity-using-computer-vision-in-ios/); [zenn.dev shu223](https://zenn.dev/shu223/articles/vision_image-feature-print)

**Punteggio estetico (macOS 15)**
- [UFFICIALE] `CalculateImageAestheticsScoresRequest` (in Objective-C `VNCalculateImageAestheticsScoresRequest`) esiste da iOS 18 / macOS 15 e restituisce `ImageAestheticsScoresObservation`, con `overallScore` da -1 a 1 (1 è il più desiderabile) e `isUtility`, vero per immagini non necessariamente brutte ma senza contenuto memorabile: screenshot, documenti, foto di servizio. — [Apple docs: CalculateImageAestheticsScoresRequest](https://developer.apple.com/documentation/vision/calculateimageaestheticsscoresrequest.md); [Apple docs: isUtility](https://developer.apple.com/tutorials/data/documentation/vision/vnimageaestheticsscoresobservation/isutility.md); [Create with Swift](https://www.createwithswift.com/scoring-the-aesthetics-of-an-image-with-the-vision-framework/)
- [TERZI] Nella pratica escono valori negativi; uno sviluppatore chiede conferma che l'intervallo sia davvero -1…1. — [Apple Developer Forums 781561](https://developer.apple.com/forums/thread/781561)

**Registrazione delle immagini (allineamento bracketing e sovrapposizione panorami)**
- [UFFICIALE] Vision offre la registrazione traslazionale (`VNTranslationalImageRegistrationRequest`, trasformazione affine) e omografica (`VNHomographicImageRegistrationRequest`, matrice 3×3). — [Apple docs: Aligning similar images](https://developer.apple.com/documentation/vision/aligning-similar-images.md); [objc2-vision docs](https://docs.rs/objc2-vision/latest/objc2_vision/struct.VNTranslationalImageRegistrationRequest.html)
- [TERZI] Esempio d'uso: allineare frame di raffica o bracketing con `VNTranslationalImageRegistrationRequest(targetedCIImage:)` e `VNSequenceRequestHandler`, poi fonderli con un filtro Metal. — [Kodeco: Photo stacking in iOS with Vision and Metal](https://www.kodeco.com/3733151-photo-stacking-in-ios-with-vision-and-metal?page=2)

**MobileCLIP**
- [UFFICIALE] Apple distribuisce su Hugging Face gli encoder di testo e immagine di MobileCLIP già convertiti in Core ML. Latenze indicative dell'encoder immagine: S0 circa 11,4 ms, S1 circa 21,5 ms, S2 circa 35,7 ms, B circa 86,3 ms. Il paper le misura su **iPhone 12 Pro Max**, non su Mac. Esiste anche MobileCLIP2. — [HF apple/coreml-mobileclip](https://huggingface.co/apple/coreml-mobileclip); [arXiv 2311.17049](https://arxiv.org/html/2311.17049v2); [GitHub apple/ml-mobileclip](https://github.com/apple/ml-mobileclip)

### Inferences
- [INFERITO] **Pipeline proposta per Selects**:
  1. **Stadio 0, metadati (gratis)**: ora di scatto con i sottosecondi (`SubSecTimeOriginal`), numero di file, `ExposureBiasValue`, `ExposureTime`, `FNumber`, ISO, focale, `DriveMode` e modalità bracketing dai makernote quando ci sono. Una sequenza 0, -1, +1 (o simile) di bias, con apertura e focale costanti e intervallo breve, è quasi certamente un bracketing, anche senza guardare i pixel.
  2. **Stadio 1, segmentazione temporale**: si spezza la sequenza quando l'intervallo supera una soglia adattiva, per esempio pochi secondi per raffiche e bracketing. Va misurato il tempo trascorso dalla *fine* dello scatto precedente (ora + `ExposureTime`), che è proprio l'errore che fa Lightroom con le pose lunghe.
  3. **Stadio 2, somiglianza visiva** sull'anteprima JPEG incorporata ridotta (circa 300–512 px): feature print a revisione fissa, distanza ≤ circa 0,35 per i quasi-doppioni, da tarare sui RAW di Andrea. Per il bracketing **non** usare la luminosità: l'impronta Vision è abbastanza robusta all'esposizione, ma per sicurezza si può confrontare dopo aver normalizzato l'istogramma, o usare un dHash calcolato sul **gradiente/bordi** (Sobel o Canny con Core Image) invece che sui valori grezzi.
  4. **Stadio 3, conferma geometrica**: per il bracketing, `VNTranslationalImageRegistrationRequest` con spostamento piccolo (per esempio sotto il 2–3% del lato). Per il panorama, `VNHomographicImageRegistrationRequest` tra frame consecutivi, con una traslazione apparente del 20–70% del lato (sovrapposizione parziale) e direzione coerente nella sequenza. Le soglie sono ipotesi mie da validare.
  5. **Stadio 4, scelta della migliore**: `overallScore` (macOS 15+) combinato con nitidezza (varianza del Laplaciano) e occhi/volti (`VNDetectFaceCaptureQualityRequest`), con ripiego per macOS 14.
- [INFERITO] **Prestazioni**: nessuna fonte affidabile trovata con il throughput dei feature print su Apple Silicon. Ordine di grandezza da ricordo, non verificato: decine di millisecondi per immagine sulla CPU/ANE di un M1 a risoluzione ridotta, quindi circa 20–50 immagini al secondo per processo, di più in parallelo. Va misurato con un benchmark interno sulle anteprime incorporate dei RAW Sony, coerente con la regola "decodifica leggera" di Selects.
- [INFERITO] Il dHash e il pHash (64 bit, distanza di Hamming ≤ circa 5–10) costano quasi nulla e bastano per i doppioni esatti o quasi esatti, cioè raffiche a scena ferma. I feature print servono quando c'è movimento o un piccolo cambio di inquadratura.
- [INFERITO] La saliency (`VNGenerateAttentionBasedSaliencyImageRequest`) può servire per ritagliare il soggetto prima del confronto, così da distinguere raffiche dello stesso sciatore su sfondi uguali. È un'ottimizzazione secondaria.
- [INFERITO] La revisione 1 dei feature print, dei sistemi precedenti, dovrebbe avere un vettore di 2048 valori: è un ricordo non verificato. Fissando la revisione corrente, l'app richiede macOS 14+.

### Gaps
- Mancano numeri pubblicati e affidabili su ms per immagine di `VNGenerateImageFeaturePrintRequest` su M1, M2, M3 o M4.
- Le latenze di MobileCLIP misurate su Mac non le ho trovate (quelle pubblicate sono per iPhone).
- Apple non pubblica una soglia di distanza ufficiale. La sessione WWDC24 sull'estetica non l'ho verificata direttamente; l'attribuzione viene da un blog.
- Non ho trovato linee guida Apple sulla sovrapposizione minima necessaria perché la registrazione omografica funzioni.

## 4. Insidie: scene diverse unite, bracketing spezzati, cartelle miste

### Takeaway
I tre errori tipici hanno tre cause diverse. Le scene vicine finiscono unite perché ci si fida solo del tempo o la soglia è troppo larga. Il bracketing si spezza perché il tempo viene misurato male con le pose lunghe, o perché il confronto visivo è sensibile alla luminosità. Nelle cartelle miste, singole foto vengono assorbite dai bracketing vicini. Serve un criterio combinato tempo + EXIF + immagine, e serve far correggere i gruppi all'utente: Narrative, al contrario, non lo permette.

### Cited Findings
- [TERZI] Lightroom unisce foto separate da più dell'intervallo impostato (bug) e raggruppa troppe o troppe poche pose del bracketing. — [Adobe bug 12390600](https://community.adobe.com/t5/lightroom-classic-bugs/auto-stack-by-capture-time-sometimes-stacks-photos-incorrectly/idi-p/12390600); [Auto stacking doesn't group bracketed photos](https://community.adobe.com/questions-675/auto-stacking-doesn-t-group-bracketed-photos-965830)
- [TERZI] L'intervallo viene misurato tra gli istanti di scatto e non tiene conto della durata della posa. — [Adobe feature request](https://community.adobe.com/feature-requests-676/p-better-auto-stacking-for-bracketing-hdr-focus-stacking-and-panoramas-666365)
- [TERZI] Con soglia 0,5 sui feature print si uniscono foto diverse della stessa scena generica; con soglia 0,2 sfuggono doppioni veri. Il raggruppamento per tempo non vede i doppioni scattati a distanza di tempo. — [ShutterSlim](https://shutterslim.com/blog/2026/01/18/vision-framework-image-similarity)
- [UFFICIALE] In Narrative le scene non si possono riorganizzare dopo l'analisi: è un limite di prodotto da non copiare. — [Narrative help](https://help.narrative.so/en/articles/8119179-using-scenes-in-select)
- [TERZI] Aftershoot ha dovuto rivedere i preset ("Similarish" al posto di "Strict"): segno che la sensibilità giusta cambia da utente a utente. — [Aftershoot release](https://events.aftershoot.com/?p=43908)

### Inferences
- [INFERITO] **Scene diverse scattate in fretta** (per esempio due sciatori diversi nello stesso couloir a 3 secondi di distanza): il tempo da solo le unisce. Bisogna richiedere anche la somiglianza visiva, meglio se sul soggetto saliente, e spezzare il gruppo quando la distanza tra frame consecutivi fa un salto anche se i tempi sono vicini.
- [INFERITO] **Bracketing spezzato quando il fotografo si muove** (a mano libera, o tra due bracketing): tollerare spostamenti piccoli con la registrazione traslazionale. Se l'EXIF mostra una sequenza di bias completa (per esempio 3 o 5 pose con la stessa apertura e focale), preferire il criterio EXIF a quello visivo. Usare il numero di pose atteso, ricavato dal primo gruppo o dalle impostazioni della fotocamera, come vincolo: è proprio quello che gli utenti chiedono a Lightroom.
- [INFERITO] **Cartelle miste**: un singolo a 0 EV scattato subito prima o dopo un bracketing viene risucchiato nel gruppo. Si risolve controllando che il gruppo abbia uno schema di bias coerente (0/-/+ ripetuto) e che il numero di pose sia un multiplo di quello atteso. I frame in più restano singoli.
- [INFERITO] **Panorami vs raffiche**: entrambi hanno tempi ravvicinati ed esposizione costante. La differenza è la traslazione costante e consistente tra frame (panorama) contro una traslazione quasi nulla (raffica). La registrazione omografica li distingue. Attenzione ai panorami con bracketing (pano HDR): prima si raggruppa il bracketing, poi la sequenza dei gruppi come panorama.
- [INFERITO] **Interfaccia**: mostrare le pile chiuse con un badge del tipo (raffica / HDR / pano / simili) e del numero di foto, permettere di dividere e unire a mano, e tenere la sensibilità regolabile con un cursore o tre preset, come Imagen ed Excire.

### Gaps
- Non ho trovato studi o test pubblici che misurino i tassi di errore (falsi raggruppamenti o gruppi spezzati) delle app commerciali.
- Non ho trovato documentazione su come le varie marche (Sony, Canon, Nikon, Fuji) scrivano nei makernote la posizione nella sequenza di bracketing. Sarebbe importante per Selects multi-marca ed è da ricercare separatamente.
