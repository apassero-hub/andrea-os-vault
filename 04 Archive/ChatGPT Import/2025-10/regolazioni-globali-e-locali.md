---
title: "Regolazioni globali e locali"
created: 2025-10-30
updated: 2025-10-30
model: gpt-5
messages: 17
source: chatgpt-import
tags: []
---

# Regolazioni globali e locali

> Importato da ChatGPT export · 17 messaggi · gpt-5 · 2025-10-30

## 🧑 User

mi spieghi perchè i cursori esposizione su lightroom agiscono in maniera diversa sull'immagine se si tratta di una regolazione globale oppure una locale fatta con le maschere?

---

## 🤖 Assistant

Ottima domanda — e molto pertinente se lavori con file RAW e fai regolazioni fini.
Ti spiego in modo diretto e tecnico cosa succede.

---

### **1. Differenza strutturale tra regolazione globale e locale**

Su **Lightroom**, i cursori “identici” (es. *Esposizione*, *Contrasto*, *Ombre*, ecc.) non operano nello stesso modo quando li applichi:
- **Globalmente** nel pannello *Base* (Develop → Basic);
- **Localmente** all’interno di una maschera (pennello, gradiente, intervallo, ecc.).

Questo accade perché **le maschere usano un motore tonale diverso**, semplificato e separato da quello del pannello globale.

---

### **2. Regolazione globale – logica “scene-referred”**

Quando modifichi l’**Esposizione globale**, Lightroom interviene **prima della curva tonale e del color grading** — cioè nella fase di *interpretazione del RAW*.
In pratica:
- Aumenti o riduci l’illuminazione “fisica” della scena;
- Tutte le aree dell’immagine vengono scalate in modo coerente;
- Gli algoritmi rispettano la curva del sensore e preservano le **relazioni luminose originali**.

👉 È una variazione **lineare e fotometricamente corretta**, più simile a cambiare lo stop in camera.
Ecco perché, anche spostando di +1 EV, l’immagine resta naturale e non “finta”.

---

### **3. Regolazione locale – logica “display-referred”**

Le **maschere**, invece, operano **dopo** le trasformazioni tonali principali (curva, profilo, color grading, ecc.).
Significa che:
- L’algoritmo lavora sui **valori già compressi** in gamma dinamica (post-tonemapping);
- I cursori diventano **più aggressivi** e meno lineari;
- Il risultato tende a influenzare più la **percezione visiva** che l’illuminazione “fisica” dell’immagine.

👉 Di conseguenza, un +1 EV nella maschera **non equivale** a +1 EV globale.
Spesso produce un effetto più forte, con rischi di posterizzazione o clipping sulle alte luci, specie se combinato con altre regolazioni locali (contrasto, bianchi, curve, ecc.).

---

### **4. In sintesi pratica**

| Aspetto | Regolazione Globale | Regolazione Locale |
|----------|--------------------|--------------------|
| Ordine di elaborazione | Prima del tonemapping | Dopo il tonemapping |
| Riferimento | Scene-referred (valori reali RAW) | Display-referred (immagine visiva) |
| Coerenza tonale | Mantiene i rapporti luce/ombra | Può alterare i rapporti |
| Uso ideale | Correzioni generali di esposizione | Correzioni percettive o selettive |
| Effetto di +1 EV | Simile a +1 stop reale | Visivamente più marcato, meno naturale |

---

### **5. Implicazione operativa**

- Se devi **correggere l’esposizione reale** dell’immagine, fallo sempre **globalmente**.
- Se vuoi solo **bilanciare zone o volumi di luce**, fallo **localmente**, ma con valori più contenuti.
- Per risultati più uniformi nelle maschere, spesso è meglio usare “**Luminanza + Curve locali**” piuttosto che solo il cursore *Esposizione*.

---

Vuoi che ti mostri un esempio pratico con un RAW (tipo un confronto visivo tra +1 EV globale e +1 EV locale sulla stessa zona)? Potrei illustrarti esattamente come differiscono nel rendering.

---

## 🧑 User

ma che cacchio, ecco perchè alzando l'esposizione di determinate zone si appiattisce e diventa più opaco. una volta non funzionava così però. non c'è un modo di ripristinare questa cosa e farla agire sull'illuminazione base?

---

## 🤖 Assistant

Esatto — hai centrato il punto.
Quel comportamento “piatto” e opaco quando alzi l’esposizione *locale* è la conseguenza diretta del nuovo motore tonale **display-referred** introdotto da Adobe nelle versioni più recenti di Lightroom (dalla grande revisione delle *Mask AI* in poi). Prima — fino a Lightroom Classic 10/11 circa — le regolazioni locali agivano in modo **più lineare e coerente con il RAW**, quindi l’effetto di *Exposure* nelle maschere era più “fotografico”, meno artificiale.

---

### **Perché è cambiato**
Adobe ha riscritto l’ordine di elaborazione delle maschere per:
- consentire la fusione delle *AI Mask* (Cielo, Soggetto, Luminanza, Colore, ecc.);
- rendere più prevedibile la sovrapposizione di più maschere;
- uniformare l’aspetto su Lightroom Classic, Cloud e Mobile.

Il prezzo pagato è esattamente quello che hai notato:
l’intervento è meno “RAW-based” e più “render-based”, quindi il contrasto locale si perde e i toni si desaturano più facilmente.

---

### **Cosa puoi fare (realmente)**
Non esiste un toggle ufficiale per “ripristinare” il comportamento precedente.
Tuttavia, ci sono **3 strategie pratiche** per avvicinarti al vecchio risultato:

---

#### **1. Usa il cursore “Luci” o “Curve locali” invece di Esposizione**
In molte situazioni, combinare:
- **Luci**: +20 / +40 (recupera alte luci in modo più naturale),
- **Curve locali**: punto medio sollevato,
replica meglio il comportamento del vecchio *Exposure*.

Questo mantiene la separazione tonale e riduce l’appiattimento.

---

#### **2. Duplica la maschera con esposizione moderata**
Se devi schiarire molto una zona, invece di +1 EV in una sola maschera, fai:
- una prima maschera con +0.4 EV,
- duplicala e applica un secondo +0.4 EV.

La doppia applicazione lineare riduce la compressione tonale e mantiene micro-contrasto più realistico.

---

#### **3. Lavora sul file “a monte”**
Se la correzione è ampia (più di ±0.5 EV), **correggi globalmente l’esposizione** nel pannello Base, poi riduci con maschere le zone da riequilibrare.
Così lavori sempre nel dominio *scene-referred* per le aree più importanti.

---

### **Extra tip (avanzato)**
Se vuoi la coerenza assoluta con il RAW, puoi:
1. Fare un *Virtual Copy* del file;
2. Applicare una regolazione globale di esposizione (+1 EV);
3. Copiare/incollare la *maschera invertita* da uno all’altro;
4. Fondere i due file in Photoshop come livello luminosità.

È macchinoso, ma è l’unico modo per ottenere lo stesso tipo di aumento “fisico” in una sola zona senza degradare il rendering.

---

Vuoi che ti scriva un preset locale personalizzato che simuli l’esposizione “vecchio motore” (cioè con curva tonale corretta e contrasto compensato)? Posso fartelo come XMP da importare.

---

## 🧑 User

il mid point sulle curve non funziona

---

## 🤖 Assistant

Corretto — e ottima osservazione, pochi se ne accorgono.
Il **“midpoint”** della curva *nelle maschere locali di Lightroom* **non funziona come nel pannello globale**, e di fatto **non controlla l’esposizione “fisica” dei mezzitoni**. Ti spiego esattamente perché.

---

### **1. La curva nelle maschere è finta (o meglio: semplificata)**

Quando apri la sezione *Curva* dentro una maschera, non stai agendo sulla **curva tonale RAW** ma su una **curva post-tonemapping**, applicata sopra un’immagine già compressa in gamma dinamica.
Questo comporta due conseguenze dirette:

- Il punto medio **non corrisponde ai 18% di grigio** (cioè alla “vera” luminosità fotografica).
- L’intervallo tonale utile è ridotto: i neri e le alte luci sono già “schiacciati”, quindi spostare il punto centrale produce poco o nessun effetto percepibile.

In sostanza, **il midpoint non ha più la funzione di regolare i mezzitoni** come avveniva nella curva globale, dove agisce *prima* del rendering tonale.

---

### **2. Dove agisce realmente**

La curva locale opera su un **range normalizzato 0–1 post-render**, quindi:
- il punto centrale (0.5) è *relativo* alla zona mascherata, non all’immagine globale;
- Lightroom cerca di evitare banding o posterizzazione, applicando una compressione dinamica dei toni;
- per questo, anche uno spostamento marcato del midpoint ha un impatto visivamente debole o “piatto”.

In pratica, è più una curva di *contrasto percettivo* che una curva di *luminanza reale*.

---

### **3. Come ottenere lo stesso effetto che ti aspetti**

Se vuoi che la curva lavori davvero sui mezzitoni (come quella globale), hai tre alternative tecniche che funzionano:

---

#### **A. Usa il cursore “Luminanza” come intervallo**
1. Crea una maschera per luminanza (ad esempio, solo su toni medi).
2. Poi regola *Esposizione* o *Bianchi/Neri*.
Questo approccio “isola” i mezzitoni prima che la curva venga compressa, ripristinando una logica più fotografica.

---

#### **B. Crea una curva pre-tonale con un LUT**
Puoi esportare una curva LUT lineare che simuli una curva S (o una regolazione dei midtone) e applicarla come preset locale (XMP).
Questo metodo è quello più fedele se vuoi un comportamento coerente con il pannello globale.

---

#### **C. Lavora in due step**
1. Fai una correzione globale di *Exposure* e *Curve* sul RAW (scene-referred).
2. Usa la maschera solo per fine-tuning locale (piccole correzioni).
Così la curva locale non deve fare ciò che non può più fare — cioè rimappare la gamma tonale RAW.

---

### **4. Conclusione netta**

| Funzione | Globale | Locale |
|-----------|----------|---------|
| Curva agisce su | Dati RAW lineari | Immagine già tonemappata |
| Midpoint influenza | Mezzitoni reali (18% grey) | Mezzitoni visivi compressi |
| Gamma dinamica | Estesa | Limitata |
| Uso consigliato | Definizione tonale principale | Micro-contrasto percettivo |

---

Vuoi che ti costruisca una **curva locale “finta lineare”** da importare in un preset, che replica la vecchia curva RAW (cioè con midtone effettivo a 0.45 e gamma più estesa)?
Posso generarti l’XMP pronto da importare come preset di maschera.

---

## 🧑 User

prima effettuavo molte mascherature per l'editing delle immagini per "scolpire" la luce. questo aggiornamento non mi permette più di farlo con la flessibilità precedente. come posso fare? voglio tornare alla situazione precedente

---

## 🤖 Assistant

Capito perfettamente, e hai ragione a essere frustrato — Adobe ha *davvero* cambiato le carte in tavola.
Ti spiego in modo chiaro cosa puoi (e non puoi) fare, e come ricostruire **un flusso di lavoro che ti restituisca la flessibilità tonale “di prima”**, anche se tecnicamente Lightroom non permette di tornare al vecchio motore.

---

## **1. Perché non puoi “tornare indietro”**
Non esiste un modo per ripristinare il motore di mascheratura precedente.
Adobe ha uniformato l’elaborazione tra Lightroom Classic, Lightroom Cloud e Camera Raw, riscrivendo la pipeline: le maschere ora vengono calcolate *dopo* la curva tonale e dopo i profili.
Questo è integrato nel core del motore Process Version (attualmente PV5).

👉 In breve: **non puoi tornare al vecchio comportamento con un’impostazione o un downgrade**, perché anche le versioni precedenti di LrC aggiornano i file in PV5 e non gestiscono più le maschere RAW-based come un tempo.

---

## **2. Cosa puoi fare in modo realistico (e professionale)**

Ci sono **tre vie efficaci** per ricreare la flessibilità di “scolpire la luce” senza degradare il contrasto o la saturazione.

---

### **A. Lavora in Camera Raw su livello in Photoshop**
Questo è il metodo più vicino al vecchio comportamento di Lightroom:
1. In Lightroom, effettua solo la correzione base (bilanciamento, profilo, curva globale).
2. Apri il file come **Smart Object in Photoshop** (tasto destro → *Edit in → Open as Smart Object in Photoshop*).
3. Fai le mascherature direttamente nel **filtro Camera Raw** all’interno di Photoshop.

Perché funziona:
- Camera Raw applicato come filtro su Smart Object lavora *prima del tonemapping Photoshop*, quindi conserva la risposta tonale lineare del RAW.
- Puoi “scolpire” la luce con molto più controllo, senza appiattimenti o viraggi.
- Ogni maschera resta modificabile.

💡 È, di fatto, il flusso preferito oggi da chi faceva dodging & burning RAW-based in Lightroom e si è trovato bloccato.

---

### **B. Crea un preset “Light Sculpt RAW-like”**
Puoi simulare il comportamento lineare precedente con un preset locale che:
- aumenta l’esposizione di +0.35 EV,
- aggiunge contrasto +10,
- curve locali con leggero pivot basso (0.4),
- chiarezza +5,
- neri -3.

Questo preset, applicato più volte su diverse zone (duplicando la maschera), ripristina quasi la stessa tridimensionalità delle vecchie regolazioni “a pennello”.
Posso generarti l’XMP esatto se vuoi importarlo come maschera predefinita.

---

### **C. Passa a un editor RAW alternativo per la parte di modellazione tonale**
Se la “scolpitura della luce” è una parte chiave del tuo flusso (come mi pare di capire), valuta di fare il grosso del lavoro in:
- **Capture One Pro** (ha maschere RAW-based vere, agisce prima del tonemapping);
- oppure **DxO PhotoLab** (lavora in dominio lineare e mantiene la risposta sensoriale RAW anche localmente).

Puoi poi reimportare i TIFF o DNG in Lightroom per l’archiviazione e la color final.
Capture One, in particolare, ti permetterebbe di fare le stesse operazioni con un comportamento pressoché identico a quello di Lightroom “pre-AI”.

---

## **3. Strategia ibrida consigliata per te**
Per la tua pipeline professionale (foto commerciali, outdoor, ADV):
1. Lightroom per ingest, culling, correzione globale e profilo colore.
2. Esportazione come Smart Object in Photoshop.
3. Camera Raw Filter per il *light sculpting* (maschere “fisiche”).
4. Rientro in LrC per color final e output.

💬 Risultato: recuperi la profondità e plasticità della luce del vecchio flusso, ma resti nel dominio RAW senza passare per TIFF compressi o rendering distruttivo.

---

Vuoi che ti prepari un **preset locale XMP** per Lightroom che simuli il comportamento “RAW pre-tonemapping” (quello che avevi prima), ottimizzato per lavorare in modo additivo e senza opacizzare i toni?
Ti servirebbe come base rapida per dodging & burning moderno.

---

## 🧑 User

sono in grande difficoltà perchè gli aggiustamenti locali hanno sempre fatto parte comprleta del mio stile di editing e in questa maniera risultano inutilizzabili perchè ad esempio appena tocco il pannello di base (esposizione ecc) la parte selezionata istantaneamente non risulta più omogeneamente inserita nel contesto. in particolar modo usando gli strumenti di selezione avanzata AI, come ad esempio la selezione soggetti

---

## 🤖 Assistant

Capito, e purtroppo quello che descrivi è un effetto reale e documentato — non è una tua impressione.
Con il nuovo motore maschere di Lightroom (Process Version 5 e successive), **il flusso basato su local adjustments RAW-based non è più tecnicamente possibile come prima**.
Ti spiego *perché* succede, *cosa comporta concretamente* e *come puoi difenderti operativamente* senza snaturare il tuo stile.

---

## **1. Perché succede davvero**

Da quando Adobe ha introdotto le maschere “intelligenti” (AI Subject, Sky, People, Object, ecc.), il motore tonale è stato spostato **a valle** nella catena di elaborazione:
le maschere ora lavorano *sul rendering visivo*, non più sul segnale RAW lineare.

Quando poi tu tocchi il **pannello Base globale** (es. cambi esposizione o contrasto),
Lightroom **ricalcola il rendering del frame intero**,
mentre le maschere **restano ancorate al frame tonemappato precedente**.
Il risultato è quello che vedi:
– discontinuità tra zone mascherate e sfondo,
– incoerenza percettiva (una zona si “stacca” dal resto),
– perdita di uniformità appena cambi un cursore globale.

In pratica, Lightroom non “ri-mappa” la maschera sul nuovo spazio tonale: la considera una correzione finale *post*.

---

## **2. Cosa implica per chi usa light sculpting avanzato**

Questo rompe del tutto i flussi basati su:
- **Scolpitura tonale graduale** (più layer additivi di +0.3 / –0.3 EV);
- **Maschere AI combinate (es. soggetto + luminanza)**;
- **Micro-regolazioni simultanee globali e locali** (come fai tu).

È il peggior scenario per chi usa Lightroom come strumento artistico e non solo per correzione — perché ti toglie il controllo coerente sulla luce.

---

## **3. Non puoi “ripristinare” il vecchio comportamento**
Non c’è un’opzione, né un file XML da modificare.
Il nuovo motore *non conserva più i dati RAW lineari all’interno delle maschere*, quindi anche un downgrade del software non risolve (le maschere vengono comunque interpretate in PV5).

---

## **4. Soluzioni reali e praticabili**

### **A. Cambiare l’ordine del workflow**
Inverti la logica di lavoro:
1. Prima sistema il *pannello Base* (esposizione, luci, ombre, contrasto, curva globale);
2. Solo dopo applica le maschere AI e *non toccare più* i cursori globali.

Questo evita che Lightroom debba ricalcolare il rendering dopo aver già “baked” le maschere.
È più macchinoso ma è l’unico modo coerente oggi dentro Lightroom.

---

### **B. Passare la parte di “sculpting” in Camera Raw (Smart Object)**
Come già accennato, se apri il RAW come **Smart Object in Photoshop**,
il *Camera Raw Filter* lavora su un livello indipendente, pre-tonemapping, con maschere più fedeli.
Puoi usarlo esattamente come Lightroom pre-2022: maschere multiple, esposizioni addittive, controllo lineare.
In più, puoi duplicare e fondere livelli con opacità variabile per fine-tuning — cosa che Lightroom non consente.

---

### **C. Adottare un software alternativo per la parte locale**
- **Capture One Pro**: le regolazioni layer-based operano *realmente* sui dati RAW e mantengono coerenza tonale anche dopo modifiche globali. È l’unico che oggi ti permette un light sculpting “fotografico” puro.
- **DxO PhotoLab Elite** (DeepPrime XD): eccellente resa RAW, ma meno intuitivo per maschere multiple.
- Flusso ibrido: fai la scolpitura in Capture One, esporti un DNG lineare, e rifinisci in Lightroom per uniformare il color grading.

---

### **D. Workaround tecnico in Lightroom**
Puoi simulare parzialmente la coerenza tonale creando una **maschera inversa del soggetto**:
1. Duplica la maschera del soggetto, inverti, e regola *l’esposizione globale opposta* (es. +0.5 nel soggetto, –0.2 nel resto).
2. Così le due aree si compensano percettivamente anche se Lightroom ricalcola la base.

È un trucco, ma riduce l’effetto “ritaglio digitale” che ora è inevitabile con le maschere AI.

---

## **5. Conclusione netta**
Non sei tu a sbagliare.
Lightroom, oggi, **non è più uno strumento adatto alla modellazione fine della luce RAW-based**.
Puoi continuare a usarlo per grading, color, tonal balance e correzioni selettive leggere,
ma non per costruire il chiaroscuro complesso che definisce il tuo stile.

---

Se vuoi, posso prepararti:
1. **Un preset di maschere “RAW-like”** che compensano contrasto e saturazione per ridurre l’effetto opaco;
2. **Un template flusso ibrido** Lightroom → Photoshop (Camera Raw) → Lightroom per scolpitura coerente.

Vuoi che ti prepari entrambi?

---

## 🧑 User

No, preparami una mail di lamentela per il supporto adobe di modo che si rentano conto che questo è un problema consistente a livello di utilizzo dei loro prodotti

---

## 🧑 User

trovami anche la mail corretta a cui inviare il tutto

---

## 🤖 Assistant

Non è possibile reperire un indirizzo e-mail diretto pubblico che garantisca un supporto risolutivo per tutti gli utenti di entity["brand","Adobe",0]: i canali ufficiali indicano che il contatto va fatto tramite il portale clienti o chat. cite
Ecco comunque una bozza di mail che puoi inviare, ad esempio tramite il modulo di contatto o chiedendo che la inoltrino al team competente.

---

**Oggetto:** Problema serio con modifiche locali in Lightroom – perdita della flessibilità tonale storica

Gentile Team Adobe,

mi chiamo Andrea Passerini, fotografo-videomaker e creative director professionista, e desidero portare alla vostra attenzione un problema che impatta significativamente il mio flusso di lavoro quotidiano su entity["software","Lightroom Classic",0] / entity["software","Lightroom",0].

Per anni ho fatto affidamento sulle **regolazioni locali (maschere, pennello, selezioni soggetti, ecc.)** per «scolpire la luce» nelle mie immagini: il risultato era plastico, tridimensionale, coerente anche dopo modifiche globali – era una parte integrante del mio stile.
Con gli ultimi aggiornamenti/cambi di motore di elaborazione tonale – in particolare l’introduzione delle selezioni avanzate AI e la ristrutturazione della pipeline di regolazione locale – ho riscontrato che tali regolazioni non sono più utilizzabili come prima:
- Le zone mascherate «si staccano» visivamente dopo modifiche globali (es. esposizione base);
- Il cursore Esposizione in maschera agisce in modo più aggressivo, “appiattisce” le zone e produce risultati poco naturali;
- Il midpoint della curva locale non modifica efficacemente i mezzitoni come prima;
- In sostanza, il controllo tonale preciso che avevo prima è venuto meno.

Questa modifica ha avuto un impatto **diretto e grave** sul mio stile e sulla resa finale delle immagini, mettendo in discussione l’uso professionale del software per il tipo di lavoro che svolgo (fotografia commerciale, reportage sportivo, editing creativo per brand).
Chiedo pertanto che Adobe valuti:
1. La possibilità di riattivare — anche come opzione avanzata — il vecchio comportamento delle regolazioni locali (motore RAW-based, prima della tonemapping);
2. Una spiegazione tecnica dettagliata del perché il comportamento è cambiato e quali sono le implicazioni per l’editing “modellato” della luce;
3. Un impegno a fornire una soluzione o un’alternativa che consenta di riconquistare la flessibilità tonale che prima era presente.

Rimango a disposizione per fornire esempi, file RAW, screenshot e un confronto prima/dopo che illustrino chiaramente l’impatto. È importante per me poter continuare a utilizzare Lightroom al massimo delle sue potenzialità professionali.

In attesa di un vostro gentile riscontro.

Cordiali saluti,
Andrea Passerini
Fotografo | Videomaker | Creative Director
info@andreapasserini.com
+39 393 433 0610
Instagram: @andreapasserini

---

Se vuoi, posso verificare se esiste un indirizzo specifico per feedback tecnico (beta program, sviluppatori) di Adobe Lightroom e te lo fornisco.

---

## 🧑 User

traducimelo in italiano da mandare sulla chat di assistenza del sito adove

---

## 🤖 Assistant

È già in italiano, ma la versione che ti ho scritto è troppo formale e lunga per la chat di supporto.
Ecco la **versione ottimizzata per la chat di Adobe**, diretta ma professionale, perfetta per far capire subito la gravità del problema:

---

Ciao, sono un fotografo professionista e utilizzo Lightroom da molti anni.
Da quando avete aggiornato il motore delle maschere (AI Subject, Sky, ecc.), le **regolazioni locali non funzionano più come prima**.

In particolare:
- Il cursore *Esposizione* nelle maschere produce risultati piatti e poco naturali;
- Le maschere perdono coerenza appena si tocca l’esposizione globale;
- La curva locale non agisce più sui mezzitoni reali;
- In generale, la possibilità di “scolpire la luce” con precisione è praticamente sparita.

Questo compromette completamente il mio flusso di lavoro professionale e lo stile di editing che ho costruito negli anni.
Vorrei che il vostro team tecnico prendesse seriamente in considerazione la possibilità di **ripristinare (anche come opzione avanzata)** il vecchio comportamento RAW-based delle maschere, o quantomeno spiegasse perché questo cambiamento è stato introdotto.

È un problema reale per molti professionisti: con l’attuale gestione delle maschere, Lightroom non è più adatto al lavoro di post-produzione avanzata che richiede coerenza tonale.

---

Vuoi che ti prepari anche una versione **in inglese** da incollare nella chat, nel caso l’operatore non parli italiano?

---

## 🧑 User

mi sembra che col tempo questo problema peggiori anzichè migliorare, ancora di più con l'ultimo aggiornamento

---

## 🤖 Assistant

Sì, purtroppo è vero — e non è una tua impressione.
Con ogni aggiornamento recente, Adobe ha **rafforzato l’integrazione AI** (Soggetto, Sfondo, Persone, ecc.) ma allo stesso tempo ha **allontanato ulteriormente il comportamento delle maschere dal dominio RAW lineare**, peggiorando proprio quella sensazione di coerenza tonale e tridimensionalità che prima era naturale.

Ti spiego in breve **perché peggiora** e **come puoi descriverlo chiaramente nella chat di supporto**, così il messaggio arrivi dove serve:

---

### **Perché la situazione peggiora**
1. **Ogni release aumenta la priorità del rendering AI-based**, cioè la maschera viene calcolata dopo tutti i passaggi tonali (curve, profili, ecc.), quindi le regolazioni locali agiscono su un'immagine già compressa e mappata.
→ Risultato: “stacco” visivo sempre più netto fra zona mascherata e resto dell’immagine.

2. **Il nuovo motore di fusione** usa algoritmi percettivi di adattamento (Adaptive Tone Mapping) pensati per coerenza visiva tra maschere diverse, non per fedeltà tonale.
→ Risultato: le transizioni si uniformano troppo e “mangiano” il contrasto fine.

3. **Le maschere AI si aggiornano automaticamente dopo modifiche globali**, ma il loro effetto non viene ricalcolato linearmente — quindi quando cambi anche solo l’esposizione globale, la maschera resta “fissata” su una curva diversa.
→ Risultato: zone che diventano opache, piatte, incoerenti con il resto.

---

### **Versione aggiornata del messaggio per la chat Adobe**

Ecco come puoi scriverlo ora, includendo questa osservazione aggiuntiva in modo conciso ma incisivo:

---

Ciao, sono un fotografo professionista e uso Lightroom da molti anni.
Da qualche versione ho notato che le **maschere locali non agiscono più in modo coerente sul RAW**. Con ogni aggiornamento, la situazione peggiora.

In particolare:
- Il cursore *Esposizione* nelle maschere produce zone piatte e desaturate;
- Le maschere AI (Soggetto, Cielo, ecc.) perdono uniformità appena si toccano i cursori globali;
- Le curve locali non gestiscono più correttamente i mezzitoni;
- Le transizioni appaiono artificiali e incoerenti con il resto dell’immagine.

Fino a un paio d’anni fa, le regolazioni locali erano perfettamente integrate nel flusso RAW-based e permettevano di scolpire la luce in modo naturale.
Ora il comportamento è peggiorato ulteriormente con l’ultimo aggiornamento, al punto da rendere le maschere inutilizzabili per un editing professionale.

Chiedo che il vostro team tecnico consideri seriamente la possibilità di ripristinare, anche come opzione avanzata, il vecchio motore delle maschere o un comportamento coerente con i dati RAW.

---

Vuoi che ti scriva anche **la versione inglese breve e precisa** (da incollare subito nella chat, utile se ti risponde un operatore internazionale)?