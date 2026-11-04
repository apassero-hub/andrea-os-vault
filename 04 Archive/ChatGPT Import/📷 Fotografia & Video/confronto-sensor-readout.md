---
title: "Confronto sensor readout"
created: 2025-09-12
updated: 2025-09-12
model: gpt-5
messages: 16
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Confronto sensor readout

> Importato da ChatGPT export · 16 messaggi · gpt-5 · 2025-09-12

## 🧑 User

Mi metti a confronto i sensor readout speed della nuova nikon zr, canon c50, sony fx3 e canon r5c per diversi codec, risoluzioni e frame rate?

---

## 🤖 Assistant

Chiaro e diretto: ci sono misure solide solo per FX3 (stessa lettura dell’a7S III) e per R5 C. Per Nikon ZR e Canon C50, ad oggi non risultano test di laboratorio pubblicati con tempi in millisecondi per le singole modalità.

# Confronto (tempi di lettura sensore / rolling-shutter)

> Nota: il readout dipende dal **modo di lettura/sensore** (full-frame, S35/crop, oversample/binning). **Codec e bitrate non cambiano** il tempo di lettura; cambiare risoluzione/ritaglio sì. I valori sotto sono in millisecondi (ms): meno è meglio.

| Camera | Modalità sensore / Risoluzione | FPS tipici | Readout (ms) | Fonte |
|---|---|---:|---:|---|
| **Sony FX3** (stesso sensore di a7S III) | 4K FF (dal 12 MP) | 24–60p | **~8.7 ms** | Test CineD su a7S III (FX3 condivide il sensore e le prestazioni RS). cite |
| **Canon R5 C** | 8K DCI FF (oversample) | 24–30p | **15.5 ms** | CineD Lab Test. cite |
| | 5.9K S35 (CRaw / crop APS-C) | 24–30p | **11.5 ms** | CineD Lab Test. cite |
| **Canon C50** | Open-Gate 7K FF (3:2) | fino a 30p | **ND** (non disponibile). Annuncio con specifiche, nessuna misura RS pubblicata. | CineD annuncio C50. cite |
| **Nikon ZR** | 6K FF | fino a 60p | **ND** (non disponibile). Annunciato “partially-stacked” con focus su readout più rapido, ma senza dati di laboratorio. | Newsshooter hands-on; annuncio. cite |

## Cosa significa operativamente
- **FX3** è la più “rapida” tra quelle con dati verificati: ~8.7 ms in 4K FF è eccellente per carrellate, whip-pan, VFX plate, rolling minimale. cite
- **R5 C**: 8K FF a 15.5 ms è buono ma non fulmineo; se vuoi meno rolling-shutter, usa il **crop S35 5.9K** (~11.5 ms). cite
- **C50** e **ZR**: finché non escono misure indipendenti, considerale “ND”. Le preview indicano sensori e pipeline orientati a ridurre il rolling, ma non c’è un numero serio da mettere in tabella. cite

## Richiesta iniziale su “codec, risoluzioni e frame-rate”
- **Codec**: non incide sul tempo di lettura del sensore; influisce su qualità/file e talvolta sblocca modalità diverse, ma **il readout è funzione del modo di lettura** (es. FF vs S35) e della progettazione del sensore.
- **Risoluzione/ritaglio**: cambiare da FF a S35 spesso **riduce** il rolling-shutter (esempio R5 C: 15.5 → 11.5 ms). cite
- **Frame-rate**: il tempo di lettura **in ms** tipicamente resta simile per quella modalità; semmai determina **se** quel frame-rate è raggiungibile (se il readout è troppo lento, non arrivi a 60p/120p in quel mode).

Se vuoi, appena compaiono i test per **C50** e **ZR**, ti aggiorno la tabella con i numeri per **ogni modo** (FF/S35, open-gate, oversample/binning).

---

## 🧑 User

Ma la r5c in 4k invece?

---

## 🤖 Assistant

Non ho trovato una misura verificata che dia il **readout / rolling shutter** per la **Canon R5 C in modalità 4K** (full-frame o crop) in ms, per tutti i codec. Le fonti che ho controllato (CineD, test tecnici) riportano valori per 8K e 5.9K S35, ma non per il 4K come condizione generalizzata. cite

Se vuoi, posso provare a stimare un intervallo basato su dati disponibili, oppure cercare una fonte più recente se esiste. Vuoi che lo faccia?

---

## 🧑 User

Si anche perchè principalmente e quella la risoluzione usata

---

## 🤖 Assistant

Non ho trovato dati misurati affidabili che riportino il tempo di rolling-shutter della R5 C *specificamente* in modalità 4K per codec diversi. Tuttavia ho alcune informazioni utili per stimare:

---

## Cosa si sa

- Nel test di CineD, la R5 C ha un rolling shutter di **15,5 ms** in 8K full-frame. cite
- Sempre in CineD, in modalità 5.9K S35 (sensor crop), il rolling shutter si abbassa a **11,5 ms**. cite
- Newsshooter scrive che Canon afferma “high speed sensor readout to help reduce rolling shutter”, ma non dà valori per le modalità 4K. cite

---

## Stima per la modalità 4K

Partendo da questi dati, si può ragionare così:

- Il readout in 4K probabilmente userà o un ritaglio del sensore o un sottocampionamento (o binning / skipping di linee) rispetto all’8K full width.
- Quindi il tempo dovrebbe essere **inferiore a 15,5 ms** (valore dell’8K FF) ma **superiore o simile** al valore in S35 o crop se il ritaglio è meno drastico.

### Fascia probabile

Ecco una stima:

| Modalità 4K probabile | Frame rate | Stima rolling shutter |
|---|---|---|
| 4K FF (sensor full width, probabilmente in All-I / XF-AVC o Cinema RAW Light) a 24-30p | 24-30 fps | **≈ 11-14 ms** |
| 4K FF a frame rate più alto (60-120p), se supportato tramite ritaglio o skipping linee | 60 fps | **≈ 9-12 ms** |
| 4K crop / modalità S35 o ritagliata / usata come “super-35 readout” | 24-60 fps | **≈ 8-11 ms** |

---

Se vuoi, posso cercare se qualcuno ha già fatto un test misurato per 4K XF-AVC 10-bit / Cinema RAW Light / ProRes e riportare il valore reale, così non è solo stima. Vuoi che lo faccia?

---

## 🤖 Assistant

Breve e chiaro: **non ci sono misure pubblicate affidabili in ms per la R5 C in 4K**. I dati di laboratorio disponibili coprono **8K FF = 15,5 ms** e **5,9K S35 = 11,5 ms**; nulla di ufficiale sul 4K (né FF né crop). cite

### Stima ragionata per il 4K (utile per lavorare subito)
Basata sui test noti e sulla logica di readout (oversample vs binning/skip):

- **4K FF “oversampled”** (da 8K pieno): **~11–14 ms**
Inferiore a 8K FF (15,5 ms), ma non arriva ai livelli S35. cite
- **4K FF “normale”** (probabile binning/line-skip alle frequenze più alte): **~10–12 ms**
In genere tempi più rapidi quando si riduce il carico di lettura, a scapito di fine detail/aliasing. (Per analogia: su R5 Mark II il 4K “normal” scende molto rispetto al 4K “fine”.) cite
- **4K S35 / crop**: **~9–11 ms**
In linea con il 5,9K S35 misurato (11,5 ms), spesso leggermente meglio in 4K. cite

### Implicazioni pratiche
- Se vuoi **minimizzare il jello**, **preferisci 4K in S35/crop** nelle riprese con panning rapidi o soggetti veloci.
- In **4K FF oversampled** ottieni il miglior dettaglio ma con rolling leggermente più alto rispetto al crop.
- Il fatto che Canon dichiari 4K fino a 120p in FF implica un readout abbastanza rapido, ma **non pubblicano tempi**; Newsshooter nota che i **15,5 ms a piena larghezza** sono “just enough” per 60p e non per 120p in quel mode, a conferma dei limiti fisici del readout FF. cite

Vuoi che continui a monitorare test nuovi (CineD/Imatest, ecc.) e ti aggiorni appena esce una misura **in 4K** specifica per la R5 C?

---

## 🧑 User

Se io volessi filmare con la
Mia sony a9ii considerato che non è il massimo come camera video, come divrei impostarla per ottenere il meglio possibile dalle sue performances

---

## 🤖 Assistant

Chiaro: la **Sony A9 II** non nasce per il video, ma con qualche accorgimento puoi tirarne fuori il massimo.
Ecco le linee guida pratiche:

---

## 1. **Profilo colore e gamma**
- Non supporta S-Log o HLG. Usa:
- **PP Off** o **PP1/PP2** (gamma standard) per avere il file più “pulito” e meno rumoroso.
- Se vuoi più margine in grading, imposta **Gamma Cine2** + **Color Mode Pro** (o Still). Non è log, ma dà un look più morbido.
- Evita di “spingere” la saturazione in camera: meglio un’immagine neutra da rifinire in post.

---

## 2. **Risoluzione e frame rate**
- Registra in **4K 24p/25p** (uscita UHD 3840×2160 da 6K oversampling fino a 30p).
- È la modalità migliore in termini di dettaglio e riduzione del moiré.
- A 60p in 1080p la qualità cala (line skipping), quindi usalo solo se serve lo slow-motion.
- Se possibile, lavora sempre in **4K 24/25p** per avere la massima resa.

---

## 3. **Codec e bitrate**
- Imposta **XAVC S 4K** a **100 Mbps, 4:2:0 8-bit**: è il limite della A9 II, ma molto meglio del 60 Mbps.
- Registra su schede SD veloci (UHS-II) per evitare drop.

---

## 4. **Esposizione**
- ISO nativi per 4K: lavora intorno a **ISO 100–800** per preservare gamma e ridurre il rumore.
- Usa **zebra** intorno al 95% per proteggere le alte luci: il sensore non ha la stessa latitudine delle A7S/A1.
- ND esterni obbligatori in esterni luminosi: ti servono per restare su tempi corretti.

---

## 5. **Otturatore e framerate**
- Regola classica: **shutter angle ~180°** (es. 1/50 per 25p, 1/100 per 50p).
- Non scendere troppo con il tempo di otturatore, altrimenti otterrai effetto “strobo”.

---

## 6. **Messa a fuoco**
- L’AF è eccellente per foto e discreto in video, ma più limitato rispetto a FX3/A7SIII.
- Usa **AF-C + Face/Eye Tracking** se hai soggetti umani.
- Per soggetti rapidi, abbassa la “sensibilità di transizione AF” a **Responsive**.

---

## 7. **Stabilizzazione**
- Ha stabilizzazione IBIS, ma non è ottimizzata per il video.
- Usa un gimbal o almeno un monopiede per sequenze lunghe.
- In handheld, preferisci focali corte (16–35, 24mm, ecc.) e movimenti fluidi.

---

## 8. **Audio**
- Il preamp interno è mediocre.
- Meglio usare un microfono esterno via mini-jack (es. Rode, DJI Mic) o un registratore dedicato.
- Imposta il livello d’ingresso intorno a **–12 dB** sul picco massimo.

---

## 9. **Output esterno**
- Se vuoi spremere il massimo, usa l’**HDMI clean out**: esce in **8-bit 4:2:2**.
- Registrando su un Atomos o simili guadagni un file più robusto in post.

---

### In sintesi
- **4K 24/25p, XAVC S 100 Mbps, shutter 1/50, ND esterni**.
- **Profilo neutro (Cine2/Still)**, zebre al 95%, ISO contenuti.
- **Audio esterno + supporto (gimbal o cavalletto)**.
- Se serve di più, registra via **HDMI su recorder esterno**.

---

Vuoi che ti prepari un **set di preset rapidi** (impostazioni menu già pronte) da tenere salvati su “Memory 1/2” per passare al volo tra setup **documentary** e **slow-motion**?

---

## 🧑 User

Su recorder esterno da hdmi quanti mbps si riescono ad ottenere?

---

## 🤖 Assistant

Perfetto, andiamo dritti al punto:

La **Sony A9 II** ha uscita HDMI **4K fino a 30p**, campionamento **8-bit 4:2:2**.
Non è 10-bit come FX3/A7SIII, quindi il limite resta quello.

### Bitrate effettivi su recorder esterno
Dipende dal **codec scelto sul recorder** (es. Atomos Ninja V, Blackmagic Video Assist):

- **ProRes 422 HQ 4K 25/30p** ≈ **707 Mbps**
- **ProRes 422 4K 25/30p** ≈ **471 Mbps**
- **ProRes 422 LT 4K 25/30p** ≈ **328 Mbps**
- **ProRes RAW** → **non supportato**, perché la A9 II non fornisce segnale RAW via HDMI.
- **DNxHR HQX 4K 25/30p** ≈ **754 Mbps**

Quindi, rispetto all’in-camera (100 Mbps XAVC S 4:2:0), via recorder ottieni:
- **4–7 volte più bitrate**
- **campionamento 4:2:2** (anziché 4:2:0)
- compressione meno aggressiva, file più robusti in grading.

---

Vuoi che ti faccia un confronto diretto **in tabella** tra:
- XAVC S interno (100 Mbps)
- ProRes/DNxHR esterno (300–750 Mbps)
così vedi chiaramente pro e contro?

---

## 🤖 Assistant

Ecco il confronto diretto tra **registrazione interna su A9 II** e **registrazione esterna via HDMI su recorder**:

---

## Confronto registrazione A9 II: interno vs esterno

| Parametro | **Interna (XAVC S)** | **Esterna (Recorder HDMI)** |
|---|---|---|
| Risoluzione massima | 4K UHD (3840×2160) | 4K UHD (3840×2160) |
| Frame rate max | 30p (oversample da 6K) | 30p |
| Profondità colore | 8-bit | 8-bit |
| Campionamento | 4:2:0 | 4:2:2 |
| Codec | XAVC S (H.264 Long GOP) | ProRes 422 / HQ / LT, DNxHR HQX |
| Bitrate | 100 Mbps | ~328 Mbps (ProRes LT)<br>~471 Mbps (ProRes 422)<br>~707 Mbps (ProRes 422 HQ)<br>~754 Mbps (DNxHR HQX) |
| File |.MP4 |.MOV (ProRes / DNxHR) |
| Robustezza in grading | Limitata, rischio banding in cieli e gradienti | Molto più solido: meno banding, colore più “lavorabile” |
| Peso file | 45 min ≈ 32 GB | 45 min ≈ 200–450 GB (a seconda del preset) |
| Supporto supporti | SD UHS-II (economiche, pratiche) | SSD/HDD esterni sul recorder (più costosi, ingombranti) |
| RAW | Non disponibile | Non disponibile (la A9 II non manda RAW via HDMI) |

---

### In sintesi
- **Interna (XAVC S 100 Mbps)** → leggera, veloce, perfetta per lavori rapidi senza grande color grading.
- **Esterna (ProRes/DNxHR)** → file molto più pesanti ma con **colore più pulito e margine in post**, grazie al 4:2:2 e alla compressione meno aggressiva.
- Il **limite resta l’8-bit**: non c’è modo di “sbloccare” un 10-bit dalla A9 II.

---

Vuoi che ti prepari anche un **workflow pratico** (quando conviene usare interno e quando esterno, in base a tipo di progetto: eventi, docu, pubblicità, ecc.)?

---

## 🧑 User

Mi spieghi bene la questione file video? Quindi open gate, i diversi codec, 420 e 422 i bit e tutto quello che c'e da
Sapere

---

## 🤖 Assistant

Perfetto, ti faccio una panoramica completa e ordinata, senza fronzoli, così hai un quadro chiaro di tutto ciò che serve per capire i **file video** e come interpretarli.

---

# 1. **Open Gate e risoluzione di registrazione**
- **Open Gate** = registrare **l’intera area del sensore**, senza ritagliarla.
- Esempio: una camera con sensore 3:2 (come Canon R5C o Panasonic S1H) può registrare in 3:2 invece del classico 16:9, catturando più verticale.
- Vantaggi: massima flessibilità per **reframing**, **stabilizzazione in post**, o output **verticale/orizzontale** per social.
- Svantaggi: file più pesanti, spesso limitazioni di frame rate.

- **Crop / oversampling / binning**:
- **Oversampling**: si legge l’intero sensore (es. 6K) e si riduce a 4K → più dettaglio, meno aliasing.
- **Line skipping / binning**: la camera “salta” pixel per ridurre i dati → meno qualità, più artefatti ma meno stress su processore/scheda.

---

# 2. **Codec**
Il codec è **come i dati vengono compressi e salvati**.

### Principali famiglie:
- **H.264 / H.265 (HEVC)**
- Molto compressi, file leggeri.
- H.265 più efficiente ma più pesante da montare.
- Usati nelle mirrorless (es. Sony XAVC S, Canon XF-AVC).
- **ProRes / DNxHR**
- Codec “intraframe” (ogni fotogramma compresso singolarmente).
- File pesanti ma **facilissimi da montare** e più resistenti in post.
- Standard broadcast e cinema digitale.
- **RAW (Cinema RAW Light, BRAW, ProRes RAW, ARRIRAW, ecc.)**
- Dati quasi “puri” dal sensore.
- File enormi, grande flessibilità in grading (ISO, WB dopo lo scatto).
- Richiedono dischi veloci e post-produzione avanzata.

---

# 3. **Campionamento colore: 4:2:0 vs 4:2:2 vs 4:4:4**
- Indica **quanta informazione cromatica** viene registrata rispetto alla luminanza.
- **4:2:0**
- Colore registrato con meno dettaglio.
- Ottimo per file leggeri, streaming, uso “consumer”.
- Standard su registrazione interna mirrorless.
- **4:2:2**
- Più informazione cromatica, utile in post (chroma key, grading spinto).
- Standard broadcast.
- **4:4:4**
- Campionamento colore completo, usato in cinema e VFX.
- File molto pesanti, raramente nelle mirrorless.

---

# 4. **Bit depth (8-bit, 10-bit, 12-bit)**
- Indica **quanti valori per canale colore** puoi registrare.
- **8-bit** = 256 livelli per canale → 16,7 milioni di colori totali.
- Limite: banding nei gradienti (cieli, ombre morbide).
- **10-bit** = 1024 livelli per canale → 1 miliardo di colori.
- Molto più robusto per grading e log.
- **12-bit** = 4096 livelli per canale → standard per RAW di fascia alta.

---

# 5. **Bitrate**
- Velocità a cui i dati vengono scritti (Mb/s o Mbps).
- Più alto = meno compressione = file più pesanti ma con più informazione.
- Esempi:
- Sony A9 II: 4K 100 Mbps interno.
- ProRes 422 HQ 4K 25p: ~707 Mbps.
- Cinema RAW Light 8K: anche >2.000 Mbps.

---

# 6. **Combinazioni pratiche**
- **4K 8-bit 4:2:0 H.264 (100 Mbps)** = file leggero, buono per eventi, consegne rapide, poco margine in grading.
- **4K 10-bit 4:2:2 ProRes (500–700 Mbps)** = standard broadcast, ottimo equilibrio qualità/post.
- **6K/8K RAW 12-bit (1–2 Gbps)** = produzione cinema, enorme flessibilità ma workflow pesante.
- **Open Gate ProRes RAW** = massimo margine per reframing e grading in pipeline cinema/VFX.

---

# 7. **Quando scegliere cosa**
- **Social, eventi rapidi, file leggeri** → 8-bit 4:2:0 H.264 interno.
- **Docu, corporate, pubblicità media** → 10-bit 4:2:2 interno o esterno (ProRes).
- **Cinema, spot alto budget, VFX** → RAW (12-bit, 4:4:4, open gate).

---

Vuoi che ti prepari uno **schema visivo a tabella** con esempi reali (tipo: “A9 II → 8-bit 4:2:0 H.264, FX3 → 10-bit 4:2:2, R5C → 12-bit RAW” ecc.) così hai il quadro comparativo camera per camera?

---

## 🧑 User

Dai

---

## 🤖 Assistant

Perfetto, ecco lo schema comparativo **chiaro e pratico**. Ho messo alcune delle macchine che hai nominato di recente (Sony A9 II, FX3, Canon R5 C, Canon C70/C50 come esempio cinema EOS C), così vedi subito cosa offrono in termini di file.

---

## Tabella comparativa codec / bit depth / chroma subsampling

| Camera | Modalità | Codec | Bit depth | Campionamento | Bitrate tipico |
|--------|----------|-------|-----------|---------------|----------------|
| **Sony A9 II** | 4K interno | XAVC S (H.264) | 8-bit | 4:2:0 | 100 Mbps |
| | 4K esterno HDMI | ProRes / DNxHR (su recorder) | 8-bit | 4:2:2 | 300–750 Mbps |
| **Sony FX3** | 4K interno | XAVC S-I (H.264 All-I) | 10-bit | 4:2:2 | 240–600 Mbps |
| | 4K interno | XAVC HS (H.265) | 10-bit | 4:2:2 | 100–280 Mbps |
| | HDMI esterno | ProRes RAW (via Atomos Ninja V+) | 12-bit | RAW | ~1–2 Gbps |
| **Canon R5 C** | 8K/4K interno | XF-AVC (All-I o Long GOP) | 10-bit | 4:2:2 | 160–810 Mbps |
| | 8K/6K/4K interno | Cinema RAW Light | 12-bit | RAW | 1–2,6 Gbps |
| | 4K HQ | Oversample da 8K | 10-bit | 4:2:2 | ~500 Mbps |
| **Canon C70 / C50 (RF Cinema)** | 4K interno | XF-AVC | 10-bit | 4:2:2 | 160–410 Mbps |
| | Alcuni modelli (C70) | Cinema RAW Light (4K S16) | 12-bit | RAW | ~1 Gbps |

---

## Cosa significa in pratica
- **Sony A9 II** → limitata a 8-bit, 4:2:0 interno (rolling shutter veloce, ottima in sport ma poco margine in grading). Con recorder esterno guadagni 4:2:2 ma resti in 8-bit.
- **Sony FX3** → vera macchina video: 10-bit 4:2:2 interno, più RAW esterno 12-bit. Molto più margine in post.
- **Canon R5 C** → enorme flessibilità: 10-bit 4:2:2 in XF-AVC o 12-bit RAW interno fino a 8K. File più pesanti ma livello cinema.
- **Canon C70/C50** → pensate per produzione: 10-bit 4:2:2 come standard, con opzioni RAW su C70. Workflow broadcast pronto.

---

### Regola semplice
- **8-bit 4:2:0** → consegne rapide, file leggeri, no grading spinto.
- **10-bit 4:2:2** → standard per docu, adv, lavori seri (ottimo bilanciamento).
- **12-bit RAW** → cinema, spot di fascia alta, VFX, grandi dischi e potenza in post.
- **Open Gate** → usalo se ti serve reframing o formati multipli (orizzontale, verticale, 9:16, 2.39:1) dallo stesso file.

---

Vuoi che ti prepari anche un **diagramma “decision tree”** (tipo: se il progetto è social → usa X, se è corporate → Y, se è cinema → Z) così sai subito quale combinazione scegliere in base al lavoro?