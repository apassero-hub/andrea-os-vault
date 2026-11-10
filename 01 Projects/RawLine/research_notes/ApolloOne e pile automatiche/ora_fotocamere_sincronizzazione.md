# Sincronizzazione automatica dell'ora tra più fotocamere (RawLine Selects)

Note di ricerca, 10 novembre 2026. Ho tenuto separati i fatti con fonte (Cited Findings) dalle deduzioni mie (Inferences). Le fonti sono soprattutto documentazione ufficiale, un paper accademico letto per intero (Sansone et al., arXiv 1608.06770) e forum di fotografi.

## 1. Come fanno le app esistenti la sincronizzazione multi-fotocamera

### Takeaway
Nessuna app diffusa (Lightroom Classic, Photo Mechanic, Capture One, digiKam, ExifTool, Apple Photos) stima lo scarto da sola. Tutte applicano uno spostamento che l'utente misura a mano: una foto di un orologio o due foto dello stesso istante, poi si filtra per numero di serie della fotocamera. Gli unici sistemi automatici che ho trovato vengono dalla ricerca accademica (MediaEval SEM 2014–2015) e da alcuni brevetti. Per un'app di culling la proposta automatica sarebbe quindi un elemento distintivo.

### Cited Findings
- **Photo Mechanic (documentazione ufficiale Camera Bits)**
  - Lo strumento "Adjust Capture Dates and Times" ha due modalità. "Adjust Relative" sposta di un numero di ore, minuti o giorni (esempi: −3 h per una fotocamera rimasta sull'ora di Boston usata a San Diego, −20 min per una che va 20 minuti avanti). "Adjust Absolute" imposta l'ora esatta di una foto, calcola lo scarto e lo applica a tutte le foto selezionate — [Camera Bits docs](https://docs.camerabits.com/support/solutions/articles/48001200335-adjust-capture-dates-and-times)
  - Il metodo ufficiale per più fotocamere: ogni corpo fotografa un orologio che mostri i secondi ("game clock"). Poi si selezionano le foto di una fotocamera, si trova la foto dell'orologio e si scrive nel campo Time l'ora che vi si legge. Opzione aggiuntiva: "Also update file system creation date/time" — [Camera Bits docs](https://docs.camerabits.com/support/solutions/articles/48001200335-adjust-capture-dates-and-times)
  - Secondo le note di versione di Photo Mechanic citate in un thread, il comando ora aggiorna anche il tag Exif Digitized Date/Time. Dopo questa modifica Capture One mostrava l'ora corretta — [Capture One community](https://support.captureone.com/hc/fr/community/posts/360012219257-Adjust-Dates-and-Times-C1-and-Photo-Mechanic)
- **Flusso tipico nei tutorial per matrimoni ed eventi**
  - Serve una foto per fotocamera che mostri l'ora corrente, oppure foto scattate nello stesso istante. Si ordina per Camera Serial Number, si selezionano le foto di un corpo e si usa Tools > Adjust Capture Date and Time. Si può fare anche settimane dopo, purché nel frattempo non si tocchi l'orologio della fotocamera. Come riferimento si usa time.is oppure l'app CameraTimeSync, che mostra l'ora GPS — riassunto della ricerca, fonti: [Fundy Designer](https://fundydesigner.com/time-sync-cameras-storytelling/), [Fundy "lazy way"](https://www.fundydesigner.com/time-sync-cameras-lazy-way/), [Photography Life](https://photographylife.com/wedding-photography-tips-synchronize-your-cameras), [Light Stalking](https://www.lightstalking.com/how-to-sync-multiple-cameras-on-a-wedding-shoot/), [Photofocus](https://photofocus.com/2016/06/10/using-2-cameras-make-it-easy-sync-the-time/)
  - In Lightroom si filtra per "Camera Serial Number" e non per modello: così due corpi dello stesso modello non finiscono insieme — [SLR Lounge](https://www.slrlounge.com/how-to-fix-timestamp-issues-multiple-cameras/), [Lightroom Queen](https://www.lightroomqueen.com/time-camera-incorrect-change-capture-time/)
- **Lightroom Classic**
  - Metadata > Edit Capture Time offre "Adjust to a specified date and time" e "Shift by set number of hours (time zone adjust)". Lo spostamento accetta solo ore intere (problema per l'India, UTC+5:30), quindi per minuti e secondi si usa la data specificata — [Adobe community, fusi non interi](https://community.adobe.com/t5/lightroom-classic-discussions/p-edit-capture-time-doesn-t-allow-for-non-whole-hour-time-zones/m-p/12669541)
  - Bug segnalato: con l'ora legale la finestra mostra orari un'ora indietro — [Adobe bug report](https://community.adobe.com/t5/lightroom-classic-bugs/p-edit-capture-time-displays-times-one-hour-earlier-during-daylight-savings-time/idi-p/15581099)
  - Bug segnalato in 14.1: Sync cambia l'ora di scatto. "Revert to Original Capture Time" la ripristina, ma fa perdere le correzioni manuali fatte apposta — [Adobe bug report](https://community.adobe.com/t5/lightroom-classic-bugs/p-edit-sync-photo-changes-the-capture-time/m-p/15039859)
  - La pagina helpx ufficiale di Adobe mi ha risposto HTTP 403 e non l'ho letta. Il comportamento descritto sopra viene dai forum.
- **digiKam (documentazione ufficiale)**
  - Item > Adjust Time & Date (Ctrl+Shift+D) aggiunge o sottrae uno scarto fisso e copia valori tra i campi data. C'è anche "Determine difference from clock photo": scegli la foto di un orologio di riferimento e il programma calcola la differenza — [digiKam docs](https://docs.digikam.org/en/post_processing/time_adjust.html)
  - La funzione è nata da una richiesta per compensare la deriva fotografando l'ora mostrata da un GPS — [KDE bug 194768](https://bugs.kde.org/show_bug.cgi?id=194768). È stato segnalato e poi risolto un bug che mostrava un'ora diversa da quella inserita — [KDE bug 496389](https://bugs.kde.org/show_bug.cgi?id=496389). Il supporto ai fusi orari è ancora limitato — [KDE bug 510261](https://bugs.kde.org/show_bug.cgi?id=510261)
- **ExifTool**
  - La stringa di spostamento accetta `Y:M:D h:m:s` e i fusi `+h:m`. Il segno dà la direzione, sono ammessi i decimali e il formato originale si conserva (cambiano solo i numeri). In un batch, per mesi e anni la prima tag si sposta della quantità indicata e le altre dei secondi equivalenti. Un fuso non viene mai aggiunto a un valore che ne è privo — [ExifTool Shift.html](https://exiftool.org/Shift.html)
  - Esempio dalla documentazione: `'2005:11:02 11:54:00'` spostato di `-2.5 0` diventa `'2005:10:30 23:54:00'` — [ExifTool Shift.html](https://exiftool.org/Shift.html)
- **Narrative Select, Aftershoot, FilterPixel**: non ho trovato alcuna menzione di sincronizzazione automatica dell'ora tra corpi. Narrative ha una "Scene View" che raggruppa per composizione e soggetto, ma non risulta che corregga gli orari — [Shotkit review](https://shotkit.com/narrative-select-review/), [Narrative blog](https://narrative.so/blog/narrative-review)
- **Ricerca accademica**: il task MediaEval "Synchronization of multi-user Event Media" (SEM, 2014–2015) chiedeva di allineare gallerie di più utenti con orari inaffidabili. Lo scarto si calcola per galleria, assumendo un dispositivo per utente — [Sansone et al., arXiv 1608.06770](https://arxiv.org/abs/1608.06770), [CEUR MediaEval 2015](https://dcmpx.remotevs.com/org/ceur-ws/SL/Vol-1436/Paper9.pdf)
- Esistono brevetti sulla generazione di orari sincronizzati tra dispositivi per gestire i media (non li ho letti) — [USPTO 12271419](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12271419), [US9984354B1](https://patents.google.com/patent/US9984354B1/en)

### Inferences
- La tabella manuale di RawLine (numero di serie → secondi, ricavata da due foto dello stesso istante) fa già quello che fanno Photo Mechanic e digiKam. Il salto in avanti è far proporre l'abbinamento all'app invece di farlo cercare all'utente.
- Il numero di serie è la chiave giusta: i tutorial lo usano proprio per separare corpi dello stesso modello.
- Il campo "ora letta nella foto dell'orologio" di Photo Mechanic e digiKam si può automatizzare con l'OCR (vedi sezione 2).

### Gaps
- Non ho verificato il comportamento attuale di Capture One (solo thread della community), Apple Photos (la pagina di supporto che ho aperto non conteneva la sezione) e Google Photos.
- Non ho letto la documentazione ufficiale Adobe (errore 403). Non so con certezza se Edit Capture Time sposti tutte le foto selezionate in base alla foto attiva: i forum lo descrivono così, ma non ho una fonte ufficiale.
- Non ho trovato PhotoSync o GeoSetter con stima automatica dello scarto.

## 2. Metodi per stimare lo scarto in automatico

### Takeaway
Il metodo pubblicato più solido funziona così: si trovano coppie di foto visivamente simili tra due corpi, ogni coppia "vota" uno scarto (differenza degli orari), e si sceglie lo scarto più coerente. Sansone et al. (2016) lo fanno con un modello probabilistico su un albero ricoprente minimo (MST) delle gallerie. L'aspetto chiave: le feature visive di livello intermedio funzionano molto meglio di quelle puramente semantiche. La correlazione delle raffiche di scatto, l'OCR di un orologio e il GPS di un telefono sono indizi complementari. Per i primi due non ho trovato valutazioni pubblicate specifiche.

### Cited Findings
- **Corrispondenza visiva più voto (Sansone et al., "Automatic synchronization of multi-user photo galleries", arXiv 1608.06770v2, 2017)**
  - Il metodo ha tre fasi: (1) feature DCNN (GoogLeNet pre-addestrata su ImageNet, risposte di uno strato intermedio aggregate con VLAD su un vocabolario di 256 parole) per la somiglianza visiva; (2) coppie di foto simili tra gallerie diverse diventano archi di un grafo i cui nodi sono le gallerie; (3) un modello grafico probabilistico (MRF, inferenza max-sum) stima lo scarto di ogni coppia di gallerie percorrendo l'MST del grafo — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Come scarti candidati il modello considera solo le differenze di orario tra foto simili di due gallerie, non tutti i valori possibili. Questo rende l'inferenza circa mille volte più veloce del loro metodo precedente — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Il potenziale temporale premia la coerenza tra coppie consecutive: se il corpo B ha una coppia abbinata a 10:00 e una a 10:05, anche le corrispondenti del corpo A devono distare circa 5 minuti (norma l1). Quando c'è il GPS, un potenziale spaziale penalizza le coppie scattate in luoghi lontani (distanza ortodromica). Senza GPS il termine vale zero — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Ipotesi di partenza: dentro una galleria (un dispositivo) gli orari relativi sono corretti e c'è un solo scarto incognito per coppia di gallerie — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Dati di prova: quattro dataset MediaEval (Olimpiadi di Vancouver 2010, Olimpiadi di Londra 2012, fiera NAMM 2015, Tour de France 2014), da 420 a 2.471 foto e da 19 a 37 gallerie — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Una galleria conta come "sincronizzata" se l'errore resta sotto 1.800 s (30 minuti), come da protocollo MediaEval. Risultato migliore (strato "inception3a/output"): precisione 80,3%, accuratezza 83,8%, media armonica 81,7% — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Le feature dello strato classificatore finale ("loss3/classifier", somiglianza semantica) hanno dato i risultati peggiori. Gli autori spiegano che misurano la somiglianza semantica e non quella visiva — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Le feature migliori hanno portato la media armonica da 64,5% a 72,7%. La stima con MRF l'ha portata a 81,7% — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Modo di fallire documentato: se due gallerie hanno pochi o nessun abbinamento diretto, l'errore si propaga lungo il grafo. I metodi che assumono che tutte le gallerie si sovrappongano molto a quella di riferimento falliscono spesso. I metodi pieni di soglie non generalizzano tra dataset — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
  - Approcci precedenti, rassegnati nello stesso paper: SIFT/SURF più istogrammi HSV. Gli scarti si trovano con percorsi nel grafo di somiglianza verso una galleria di riferimento, con un sistema lineare approssimato, oppure con ipotesi casuali ripetute da cui si prende il medoide (cioè un consenso di tipo RANSAC). Broilo et al. stimano lo scarto dalle differenze di orario tra coppie simili, ma richiedono che i fotografi riprendano gli stessi sotto-eventi — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770); il medoide delle ipotesi è confermato da [CEUR MediaEval 2015](https://dcmpx.remotevs.com/org/ceur-ws/SL/Vol-1436/Paper9.pdf)
- **Apple Vision: feature print**
  - `VNFeaturePrintObservation.computeDistance` misura la distanza tra due "impronte". Più è piccola, più le immagini sono simili. Apple non documenta soglie. Secondo un'analisi esterna è in sostanza una distanza euclidea tra vettori — [MWM su Medium](https://medium.com/@MWM.io/apples-vision-framework-exploring-advanced-image-similarity-techniques-f7bb7d008763), [Fritz.ai](https://fritz.ai/?p=8864)
  - Le impronte di revisioni diverse della richiesta non si possono confrontare: il confronto va in errore. Va quindi fissata e salvata la revisione — [Apple Developer Forums 732876](https://developer.apple.com/forums/thread/732876)
  - Uno sviluppatore ha ottenuto una distanza diversa da zero confrontando la stessa immagine con sé stessa — [Apple Developer Forums 721760](https://developer.apple.com/forums/thread/721760)
- **Apple Vision: registrazione omografica**
  - `VNHomographicImageRegistrationRequest` calcola la matrice di omografia 3×3 che deforma un'immagine "floating" sull'immagine di riferimento. Secondo i binding objc2 la richiesta fallisce se le dimensioni in pixel del riferimento non coincidono con la regione d'interesse del floating — [docs.rs objc2-vision](https://docs.rs/objc2-vision/0.3.2/objc2_vision/struct.VNHomographicImageRegistrationRequest.html), [docs.rs apple-vision](https://docs.rs/apple-vision/latest/apple_vision/) (fonti di terze parti che rispecchiano la documentazione Apple)
- **Orologio fotografato e OCR**: digiKam e Photo Mechanic partono dalla foto di un orologio o di un GPS (sezione 1). Per lo stesso scopo esiste l'app CameraTimeSync, che mostra l'ora GPS da fotografare — [Fundy Designer](https://fundydesigner.com/time-sync-cameras-storytelling/), [App Store](https://apps.apple.com/app/id1145951288)

### Inferences
- **Correlazione delle raffiche (densità di scatto)** — deduzione mia, non ho trovato studi specifici. Si costruisce per ogni corpo un istogramma di scatti al secondo, lo si smussa (per esempio con una gaussiana di 2–5 s) e si cerca il ritardo che massimizza la correlazione incrociata normalizzata con il corpo di riferimento. Sui file è economico: bastano gli orari, niente pixel. È però ambiguo quando l'attività è regolare (tanti scatti continui, pochi momenti di picco) o quando i fotografi coprono momenti diversi, che è proprio l'ipotesi che Broilo et al. considerano troppo restrittiva. Funziona meglio nei momenti forti dei matrimoni (ingresso, anelli, bacio, lancio del bouquet). Come candidato grezzo è buono, va poi confermato con la corrispondenza visiva.
- **Strategia consigliata per Selects**, adattata dal paper e semplificata per 2–4 corpi:
  1. Candidati grossolani: correlazione delle raffiche più ipotesi "ore intere" (fuso o ora legale), più l'eventuale differenza tra gli OffsetTimeOriginal.
  2. Per ogni coppia di corpi: impronte Vision sulle anteprime già decodificate (decodifica leggera), k vicini più prossimi tra i corpi, e ogni coppia vicina vota Δt = t_A − t_B in un istogramma a contenitori di 1–2 s.
  3. Si sceglie il picco, poi si raffina con la mediana dei Δt delle coppie che rientrano nella finestra del picco (inlier di tipo RANSAC).
  4. Conferma geometrica sulle coppie migliori: la registrazione omografica o il ritaglio del frame tele dentro il grandangolo devono reggere. Così si scartano le coppie false nelle scene ripetitive.
  5. Con più di due corpi si usa un albero ricoprente (o un piccolo sistema ai minimi quadrati) per tenere le stime coerenti: A→B più B→C deve dare circa A→C.
- **Tele contro grandangolo**: dal paper ricavo che conta la somiglianza visiva più che quella semantica. Le impronte globali tendono a perdere forza quando un frame è un ritaglio stretto dell'altro. Una soluzione possibile: confrontare il tele anche con ritagli centrali o a griglia del grandangolo (multi-crop) prima di passare all'omografia. Il vincolo sulle dimensioni di `VNHomographicImageRegistrationRequest` richiede di ricampionare le due immagini alla stessa misura. La registrazione omografica è pensata per immagini quasi sovrapposte (allineamento di sequenze o panorami). Per un tele molto stretto conviene stimare prima la regione nel grandangolo.
- **Volti**: con la stessa persona ripresa da due corpi a pochi secondi di distanza (sposi) si possono pesare di più le coppie con volti simili. È utile come peso, non come prova: gli sposi compaiono per tutta la giornata, quindi i volti da soli non datano il momento.
- **OCR dell'orologio**: con `VNRecognizeTextRequest` si cerca un pattern HH:MM:SS nelle prime o ultime foto di ogni scheda. Se c'è, dà l'ora assoluta, la fiducia più alta di tutte, ed è anche l'unico modo per agganciare l'ora "vera" e non solo l'ora relativa tra i corpi.
- **MobileCLIP** e altri embedding semantici: per analogia con il risultato di "loss3/classifier", rischiano di abbinare foto "dello stesso tipo" (due ritratti degli sposi) scattate a ore diverse. Li userei solo come filtro.

### Gaps
- Non ho trovato valutazioni della correlazione delle raffiche per sincronizzare fotocamere fisse, né numeri su quante foto servano.
- Non ho trovato misure pubblicate della robustezza di VNGenerateImageFeaturePrintRequest a ritaglio e zoom: va testata sul campo con coppie tele e grandangolo reali.
- MobileCLIP, GPS dei telefoni come riferimento e date imprint: non li ho approfonditi in questa ricerca.
- Il protocollo MediaEval considera accettabili 30 minuti. Per il culling servono pochi secondi, quindi le percentuali del paper non dicono nulla della precisione al secondo.

## 3. Schemi tipici degli scarti: ore intere contro deriva

### Takeaway
Gli scarti reali sono di due famiglie. Le ore intere (o mezz'ore) nascono da fuso o ora legale impostati male. Minuti e secondi nascono da orologi impostati a mano e dalla deriva del quarzo. La deriva tipica va da pochi secondi a circa un minuto al mese, quindi dentro un servizio di una giornata lo scarto si può trattare come costante.

### Cited Findings
- Nikon D200: +8 s in circa tre mesi, cioè circa 2,5 s/mese. Ogni esemplare è diverso — [Ken Rockwell](https://kenrockwell.com/nikon/d200/d200-clock.htm)
- Utente Canon: 14 s in una settimana (circa 25 ppm). Un buon quarzo è spesso dato a circa 10 ppm. Con quarzi standard da circa 20 ppm si stimano circa 12 s a settimana — [Canon Community](https://community.usa.canon.com/t5/EOS-DSLR-Mirrorless-Cameras/GPS-Time-differing-among-cameras/m-p/298996), [Talk Photography](https://www.talkphotography.co.uk/threads/creeping-camera-clocks-no-gps-sync.737694/)
- Nikon scrive nel manuale che l'orologio della fotocamera è meno preciso di quelli di casa e consiglia di controllarlo spesso — [Nikon 1 J1 manual](https://www.manualslib.com/manual/491659/Nikon-1-J1.html?page=39)
- La temperatura e la batteria tampone influiscono sulla deriva — [Canon Community](https://community.usa.canon.com/t5/EOS-DSLR-Mirrorless-Cameras/GPS-Time-differing-among-cameras/m-p/298947)
- Gli errori per fuso e ora legale sono una causa documentata (bug di Lightroom con l'ora legale, fusi non interi come +5:30) — [Adobe community](https://community.adobe.com/t5/lightroom-classic-discussions/p-edit-capture-time-doesn-t-allow-for-non-whole-hour-time-zones/m-p/12669541)
- Il paper MediaEval elenca come cause: orologio impostato male o mai impostato, fusi diversi, orari rimossi o modificati in post-produzione — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)

### Inferences
- **Scomposizione da mostrare all'utente**: per esempio Δ = −1h 03m 12s si scompone in −1 h (probabile fuso o ora legale) più −3m 12s (orologio). Se il residuo dopo aver tolto le ore intere (o le mezz'ore e i quarti d'ora per fusi tipo +5:30 o +5:45) è sotto circa 1–2 minuti, la proposta "fuso o ora legale" è molto probabile.
- **Deriva in un servizio**: a 25 ppm un servizio di 12 ore accumula circa 1 s, trascurabile. In un viaggio di più settimane senza rimettere l'orologio si accumulano decine di secondi. Per servizi di più giorni conviene stimare uno scarto per giorno, o un modello lineare scarto + deriva, e mostrarlo solo se la pendenza è significativa.
- **Fiducia da mostrare**:
  - alta: OCR dell'orologio, oppure molte coppie visive confermate dalla geometria con varianza bassa (per esempio più di 5 coppie con dispersione sotto 2 s);
  - media: un solo picco netto nell'istogramma;
  - bassa: più picchi.
- **Alternative**: con più picchi si mostrano i due o tre migliori come scelte, ciascuno con la sua miniatura affiancata ("questi due scatti sono lo stesso momento?"). L'utente può confermare con un clic, che equivale ad aggiungere un abbinamento manuale ad alto peso.

### Gaps
- Non ho trovato statistiche su quanto spesso negli archivi reali ci siano errori di fuso o ora legale rispetto alla deriva.

## 4. Combinare gli indizi in modo robusto

### Takeaway
La combinazione robusta che emerge dalla letteratura è questa: scarti candidati presi solo dalle differenze di orario tra coppie simili, voto o consenso (istogramma, medoide di ipotesi), coerenza temporale tra coppie successive, eventuale GPS come vincolo spaziale, e un albero o grafo per propagare tra più corpi. Le coppie false nelle scene ripetitive si filtrano con la coerenza tra coppie e con la verifica geometrica.

### Cited Findings
- Il paper limita gli scarti candidati alle differenze di orario tra coppie simili e premia le sequenze di coppie la cui distanza temporale è coerente nei due corpi (potenziale ψ, norma l1) — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
- Il medoide di ipotesi ripetute come stima finale (approccio probabilistico di tipo RANSAC) è stato usato in MediaEval 2015 — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770), [CEUR Vol-1436](https://dcmpx.remotevs.com/org/ceur-ws/SL/Vol-1436/Paper9.pdf)
- Il clustering gerarchico agglomerativo sulle coppie, con scarti calcolati in modo transitivo, è stato usato in MediaEval 2014 — [ricerca su MediaEval SEM](https://dcmpx.remotevs.com/org/ceur-ws/SL/Vol-1263/mediaeval2014_submission_32.pdf)
- La posizione GPS aiuta perché foto scattate in luoghi diversi difficilmente sono lo stesso evento — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)
- Un metodo senza soglie generalizza meglio tra tipi di evento diversi di metodi pieni di soglie — [arXiv 1608.06770](https://arxiv.org/abs/1608.06770)

### Inferences
- **Scene ripetitive** (stessa sala, tavoli uguali, cerimonia statica): una coppia sola non basta mai. Serve il consenso di più coppie in momenti diversi della giornata, cioè coppie che votano lo stesso Δt pur stando a ore diverse. Il ragionamento: un abbinamento falso vota un Δt a caso, mentre quelli veri convergono.
- **Peso dei voti**: somiglianza visiva × esito della verifica geometrica × fattore raffica (le coppie dentro picchi di attività in entrambi i corpi valgono di più).
- **Abbinamenti manuali già esistenti** in Selects: vanno nel modello come voti ad altissimo peso, e restano la scelta finale se l'utente li ha confermati.
- **Annullabilità**: lo scarto proposto va salvato separato da quello confermato. La tabella numero di serie → secondi diventa numero di serie → {proposto, confermato, origine, fiducia}, e l'annullamento torna al valore precedente.

### Gaps
- Non ho trovato implementazioni open source pronte (GitHub) da riusare per questo specifico problema.

## 5. Campi EXIF utili e scrittura dell'ora corretta (XMP o solo nell'app)

### Takeaway
OffsetTimeOriginal (EXIF 2.31) e i tag proprietari del fuso aiutano a separare gli errori di fuso. SubSecTimeOriginal aiuta a ordinare le raffiche. Il modo in cui Lightroom sceglie l'ora tra XMP ed EXIF non ha documentazione ufficiale: i forum riportano comportamenti contraddittori e bug recenti. La scelta più sicura è tenere la correzione nell'app (non distruttiva). La scrittura in XMP va resa opzionale ed esplicita.

### Cited Findings
- `Composite:SubSecDateTimeOriginal` di ExifTool esiste solo se ci sono DateTimeOriginal e SubSecTimeOriginal oppure OffsetTimeOriginal. I tag di offset vengono dalla specifica EXIF più recente e servono ExifTool 10.28 o successivi — [ExifTool forum](https://exiftool.org/forum/index.php?msg=72725), [ExifTool Composite tags](https://www.chiark.greenend.org.uk/doc/libimage-exiftool-perl/html/TagNames/Composite.html)
- Sony scrive OffsetTimeOriginal (esempio +10:00) più il tag proprietario SonyDateTime. Canon scrive OffsetTime, OffsetTimeOriginal e OffsetTimeDigitized nell'ExifIFD. Nikon ha tag propri timezone e daylightsavings. Molte fotocamere non scrivono i tag di offset — [ExifTool forum 89325](https://exiftool.org/forum/index.php?msg=89325), [ExifTool forum 91730](https://exiftool.org/forum/index.php?msg=91730), [ExifTool forum 86387](https://exiftool.org/forum/index.php?msg=86387)
- **Precedenza in Lightroom (solo forum, non confermata)**: con "Read Metadata From File" Lightroom leggerebbe l'ora da XMP:DateCreated, contro le linee guida del Metadata Working Group che preferiscono EXIF. Un altro thread parla di XMP:DateTimeOriginal. Per gli MP4 l'ordine osservato è XMP:DateCreated, poi EXIF:DateTimeOriginal, poi QuickTime:CreateDate — [Adobe community](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-14-4-changing-capture-date-time-in-raw-files/m-p/15394397), [Adobe community MP4](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-determine-date-time-of-mp4-file/td-p/14359635)
- Lightroom Classic scrive i sidecar XMP per i raw proprietari. Per i formati con metadati incorporati (DNG, JPEG) scrive dentro il file — [Adobe community](https://community.adobe.com/t5/lightroom-classic-discussions/enabling-quot-automatically-write-changes-to-xmp-quot-changes-orig-file-creation-modification-dates/m-p/12554055)
- Lightroom ha un'opzione (Catalog Settings > Metadata > EXIF) per scrivere le modifiche dell'ora anche nei raw proprietari — [Adobe community](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-14-4-changing-capture-date-time-in-raw-files/m-p/15394601)
- Bug segnalati in Lightroom:
  - in 14.4 "Save Metadata to File" ha cambiato l'ora nei raw, e la soluzione suggerita era ripristinarla con ExifTool dal sidecar — [Adobe community](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-14-4-changing-capture-date-time-in-raw-files/m-p/15394123)
  - "Save metadata to file" sovrascrive SubSecTimeOriginal — [Adobe bug](https://community.adobe.com/t5/lightroom-classic-bugs/p-quot-save-metadata-to-file-quot-overwrites-exif-tag-subsectimeoriginal/idi-p/14821262)
  - Lightroom non conserva OffsetTime nei DNG — [Adobe idea](https://community.adobe.com/t5/lightroom-classic-ideas/p-lightroom-should-preserve-offsettime-attribute-in-dng-files/idc-p/14740543)
- Con l'opzione ExifTool di digiKam, sottrarre un'ora ha cambiato anche la data QuickTime, con effetti sulle altre app — [discuss.kde.org](https://discuss.kde.org/t/digikam-adjust-time/14196)

### Inferences
- **Politica consigliata**:
  1. Correzione solo nell'app per default: la tabella per numero di serie, annullabile.
  2. Scrittura opzionale in XMP sidecar con exif:DateTimeOriginal, photoshop:DateCreated e xmp:CreateDate coerenti (con fuso, se noto), senza mai toccare il raw.
  3. Avviso che Lightroom potrebbe dare precedenza ai valori XMP solo con "Read Metadata From File", e che il comportamento non è documentato ufficialmente: va verificato con un test nella cartella "prova selects lightroom".
- **Rischi della scrittura**: doppia correzione (Selects corregge, poi l'utente corregge di nuovo in Lightroom), sidecar non letti all'import se il catalogo li ha già, conflitti con sidecar già scritti da Lightroom o Capture One, perdita dei sottosecondi.
- Per sicurezza conviene tenere nel sidecar o nel database un campo con l'ora originale e lo scarto applicato, così da poter sempre tornare indietro (simile a "Revert to Original Capture Time").

### Gaps
- Non ho trovato documentazione ufficiale Adobe sull'ordine di lettura dell'ora tra XMP ed EXIF. Va provato empiricamente.
- Non ho verificato come Capture One e Photo Mechanic leggono l'ora da un sidecar XMP scritto da terzi.
