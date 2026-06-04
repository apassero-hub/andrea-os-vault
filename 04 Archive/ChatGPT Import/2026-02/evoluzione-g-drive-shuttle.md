---
title: "Evoluzione G-Drive Shuttle"
created: 2026-02-25
updated: 2026-02-25
model: gpt-5-2
messages: 12
source: chatgpt-import
tags: []
---

# Evoluzione G-Drive Shuttle

> Importato da ChatGPT export · 12 messaggi · gpt-5-2 · 2026-02-25

## 🧑 User

Allora, per il mio lavoro sto cercando una soluzione di archiviazione di grosse dimensioni, che abbia un po' di velocità e che abbia parecchi slot. Adesso la soluzione che ho trovato e che mi piace abbastanza, è la G-Drive, in tecnologia. Nello specifico è la G-Speed Shuttle XL, credo sia. Quella che ha otto baie, eight bays, e ho visto che negli anni l'hanno fatto di diversa tipologie. Hanno fatto la... come si chiama? Eight bays, prima era montato Thunderbolt 2, poi hanno aggiornato la versione a Thunderbolt 3, e adesso che G-Technology è stata acquisita da SanDisk, hanno fatto la versione quella SanDisk Professional, ho visto che si chiama G-Drive Shuttle XL, invece che G-Speed, mi pare di aver capito che appunto la G-Speed sia stata sostituita dalla G-Drive Shuttle. Vorrei capire un attimino l'evoluzione che è stata fatta, quindi, vabbè, chiaramente dai modelli iniziali si è passati dal Thunderbolt 2 al Thunderbolt 3. Chiaramente Thunderbolt 3 è su piattaforma USB-C, con tutte le differenze del caso ovviamente. Però, a parte quello, vorrei capire se con l'introduzione dei nuovi modelli SanDisk Professional hanno fatto ancora un upgrade a livello di connessioni, a livello di piattaforma, a livello di tutto. Chiaramente che ne so, firmware, oppure se quelle precedenti hanno un firmware aggiornabile perché è comparabile, se ci sono le differenze di velocità, se ci sono delle differenze hardware, se tra appunto il discorso G-RAID Shuttle o G-Speed ci sono delle differenze a livello di piattaforma RAID, ci sono delle differenze a livello di velocità, a livello di proprio tutta la piattaforma, e vorrei capire un po' meglio questa dinamica, perché quel sistema mi sembra parecchio funzionale per gli utilizzi che voglio fare io, avendo due connessioni Thunderbolt dietro, e ho visto che comunque, potendo mettere otto dischi in parallelo e registrandoli in RAID 5, o eventualmente RAID 6, comunque le performance sono alte.

---

## 🤖 Assistant

## entity["product","G-Speed Shuttle XL","8-bay thunderbolt raid"] → entity["product","SanDisk Professional G-Drive Shuttle 8","8-bay thunderbolt 3 raid"]
Evoluzione reale, non marketing.

---

## 1️⃣ Prima generazione – Thunderbolt 2
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["G-Speed Shuttle XL Thunderbolt 2 rear panel","G-Speed Shuttle XL TB2 ports","G-Technology G-Speed Shuttle XL 8-bay","G-Speed Shuttle XL Thunderbolt 2 front bays"],"num_per_query":1}

**Periodo:** circa 2014–2016
**Connessioni:**
- 2× Thunderbolt 2 (20 Gb/s)
- niente USB-C

**Controller RAID:** hardware dedicato (Areca based)
**RAID supportati:** 0, 1, 5, 6, 10, 50
**Prestazioni reali:** ~1000–1100 MB/s in RAID 5 con dischi HDD enterprise

👉 Limite principale: banda Thunderbolt 2.
Per editing 4K era ok. Oggi è un collo di bottiglia.

---

## 2️⃣ Seconda generazione – Thunderbolt 3 (USB-C fisico)
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["G-Speed Shuttle XL Thunderbolt 3 rear","G-Speed Shuttle XL TB3 ports","G-Technology G-Speed Shuttle XL Thunderbolt 3","G-Speed Shuttle XL 8-bay TB3 front"],"num_per_query":1}

**Periodo:** 2017–2020
**Connessioni:**
- 2× Thunderbolt 3 (40 Gb/s)
- 1× USB-C 3.1 (10 Gb/s) in alcune versioni

**Controller RAID:** sempre hardware dedicato
**Prestazioni:** ~1350–1500 MB/s in RAID 5 con HDD

Qui il salto è reale.
Thunderbolt 3 raddoppia la banda. Non sei più limitato dal bus.

Per un workflow tipo il tuo (RAW Sony A7S III / A1, video 4K 120, multicam, cache Resolve), questa è la prima versione davvero sensata oggi.

---

## 3️⃣ Rebrand SanDisk Professional – G-Drive Shuttle 8
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["SanDisk Professional G-Drive Shuttle 8 rear","SanDisk Professional G-Drive Shuttle 8 ports","SanDisk Professional G-Drive Shuttle 8 front bays","SanDisk Professional G-Drive Shuttle 8 Thunderbolt 3"],"num_per_query":1}

**Periodo:** 2021–oggi
G-Technology viene assorbita da Western Digital → poi branding SanDisk Professional.

⚠️ Cambiamenti reali:
- Stesso chassis concettuale
- Sempre 2× Thunderbolt 3
- USB-C compatibilità migliorata
- Controller RAID hardware aggiornato (ma architettura simile)
- Firmware più recente
- Migliore gestione alimentazione e ventole

**Prestazioni:** praticamente identiche alla versione TB3 precedente.

Non è una rivoluzione. È un aggiornamento e rebranding.

---

# Differenze chiave tra le generazioni

| Modello | TB2 | TB3 | SanDisk |
|----------|------|------|-----------|
| Banda | 20 Gb/s | 40 Gb/s | 40 Gb/s |
| USB-C | No | Sì | Sì |
| Controller RAID | Hardware | Hardware | Hardware aggiornato |
| Firmware aggiornabile | Limitato | Sì | Sì |
| Velocità max | ~1100 MB/s | ~1500 MB/s | ~1500 MB/s |

---

# G-Speed vs G-Drive Shuttle

- **G-Speed** = nome storico della linea RAID performance
- **G-Drive Shuttle** = nuova denominazione post-rebranding
- Piattaforma RAID: sempre hardware dedicato
- Non è software RAID tipo Synology o macOS RAID Utility
- Pensato per workstation locali, non NAS

---

# RAID 5 o RAID 6 nel tuo caso?

Con 8 dischi:

- RAID 5 → 7 dischi utili, 1 di parità
- RAID 6 → 6 dischi utili, 2 di parità

In RAID 5 con HDD 7200 rpm enterprise arrivi tranquillamente a 1.3–1.5 GB/s.
In RAID 6 perdi un po’ di scrittura ma guadagni sicurezza.

Per un archivio professionale grande come il tuo, RAID 6 è più sensato. I rebuild su 8 dischi grandi sono lunghi e rischiosi.

---

# Firmware e compatibilità

- Le versioni TB3 e SanDisk hanno firmware aggiornabile via utility
- TB2 è più limitato e ormai legacy
- Non c’è un vero upgrade hardware possibile tra TB2 e TB3

---

# Conviene oggi?

Se lo trovi:

- ❌ Thunderbolt 2 → solo se costa pochissimo
- ✅ Thunderbolt 3 → ottimo compromesso
- ✅ SanDisk Professional → scelta più pulita e attuale

---

# Considerazione strategica per te

Con il tuo volume dati (video 4K 120, shooting outdoor, progetti documentaristici, Forever Snowtrips + clienti commerciali):

Questa macchina è perfetta come:
- Storage di lavoro attivo
- Libreria fotografica master
- Archivio RAW consolidato

Non è un backup. È uno storage primario ad alte prestazioni.

Se vuoi, nel prossimo messaggio facciamo un confronto serio tra:
- G-Drive Shuttle 8
- Synology high-end
- NAS 10GbE custom
- DAS RAID con SSD

Così capiamo se stai andando nella direzione più intelligente o solo in quella più affascinante.

---

## 🧑 User

Allora, il G Technology Logispeed Thunderbolt 3 mi fa dire capire che a livello hardware praticamente non cambia niente, a livello di performance non cambia niente. Mi chiedo se le altre versioni, in qualche modo, cioè se questa versione qua, Thunderbolt 3, in qualche modo è aggiornabile a livello di firmware con lo stesso firmware che ha il SanDisk Professional attuale. So che hanno la possibilità di avere firmware aggiornabili manualmente, quindi mi chiedo, cioè avrebbe senso se quella roba lì potesse essere fatta, visto anche il prezzo del prodotto, cioè non è un prodotto consumer che tu, cioè dopo due anni lo cambi e dici ah uscito, hanno fatto il passaggio a SanDisk Professional, allora, cioè, il mio l'ho sostituisco e mi compro la versione aggiornata, cioè, stiamo parlando di unità che costano, cioè, al di là degli ondrive, che sono sopra, qualche migliaia di euro, cioè il 48 Tera costa 5.000 euro, il 96 Tera costa 8.000 euro, quindi avrebbe molto senso. È una roba secondo te aggiornabile?

---

## 🤖 Assistant

Sì, **ha senso aspettarsi aggiornamenti firmware** su unità di quella fascia. Però la parte importante è questa: **non puoi ragionevolmente dare per scontato che un G-Technology “vecchio” prenda lo stesso firmware identico della linea SanDisk Professional**, anche se a livello esterno sembrano “la stessa macchina”.

### Cosa è realistico (e cosa no)

**1) Aggiornare il firmware del tuo G-SPEED Shuttle XL TB3: sì, se WD/SanDisk lo rilascia per quel modello**
- Esistono aggiornamenti firmware per la serie (anche storicamente: utenti che ricevevano prompt di update firmware su Shuttle XL TB3). cite
- L’ecosistema di gestione è basato su utility/driver “G-RAID Software Utility” e relativi driver. Le release note dell’utility continuano a essere aggiornate anche di recente. cite
- La lista OS supportati include esplicitamente **Shuttle XL TB3** (segno che la piattaforma è ancora dentro al perimetro supporto, quindi potenzialmente anche lato firmware). cite

**2) Flashare “il firmware SanDisk Professional” su un’unità G-Technology TB3: in pratica no (o comunque non è una cosa che consiglio)**
- I firmware sono quasi sempre **vincolati a product ID / controller / board revision**. Anche se il prodotto è un “rebrand”, possono cambiare micro-revisioni hardware, controller RAID, bootloader, layout NAND/EEPROM, ecc.
- Le utility serie (quelle ufficiali) normalmente **ti propongono solo firmware compatibili**. Se non te lo propone, non è “perché non si può”: è perché **non è previsto per quel PID**.
- Tentare un cross-flash “a mano” (se trovi un pacchetto) è il modo più veloce per **brickare** un DAS RAID e buttare via tempo e soldi. E lato garanzia sei scoperto.

### Quindi: può valere la pena comprare una TB3 G-Technology “pre-SanDisk”?
Sì, **se la tratti come piattaforma TB3 della stessa famiglia** e verifichi una cosa concreta:

**Regola pratica:**
Se la tua unità è riconosciuta dall’utility ufficiale più recente e risulta “supported”, allora:
- **driver/utility sì** (quasi certamente)
- **firmware: solo se esiste un pacchetto rilasciato per quel modello specifico**, e te lo propone l’utility

L’utility (almeno per la famiglia Shuttle) dichiara anche la funzione di **installare firmware update**. cite (è una pagina focalizzata sulla linea Shuttle SSD, ma la logica di gestione firmware via utility è la stessa impostazione di piattaforma).

### Come lo verifichi in modo definitivo (senza ipotesi)
1) Prima dell’acquisto, chiedi al venditore:
- **foto dell’etichetta con Model Number / P/N**
- **screenshot dell’utility** che mostra versione firmware / controller (o almeno versione firmware)

2) Una volta collegato:
- installi **ultima G-RAID Software Utility + driver ufficiali**
- se esiste firmware più recente per quel *tuo* modello, **te lo segnala e lo installa**; se non lo segnala, **sei già al massimo supportato per quella revisione**

Se mi incolli **il Model Number / P/N esatto** (quello dell’etichetta) del tuo G-SPEED Shuttle XL TB3 e, se disponibile, la **versione firmware attuale**, ti dico con precisione dove cade: ramo “ancora aggiornato” vs ramo “legacy” e quali pacchetti ufficiali risultano associati.

---

## 🧑 User

Volevo chiedere, però, è una roba che non riesci a fare una ricerca e a capire se è una roba che è fattibile su quei modelli. Voglio evitare di acquistarla e poi dover andare successivamente a fare una ricerca per capire se è compatibile oppure no. L'altra questione è la seguente. A livello di velocità, mi hai detto che un unità qua impostata in RAID 5, con dischi grossi, cioè in RAID 5 con una resistenza di 1200 giri, posso arrivare a 1300-1400 mega aspettati. Che però è un problema perché sono dischi grossi e rischioso, perché qualora si sfruttassimo una disco, a quel punto per poter andare a ricreare il file, deve dire che se ci guarda tutto il tempo si sfrutta un altro disco. Mi pare di aver capito. Quindi sarebbe più consigliabile puntare su un RAID 6 se gli altri dischi grossi. E quindi sarebbe sensato. Qualora io optassi per RAID 6, che velocità mi posso aspettare? Perché sicuramente saranno più lente rispetto al RAID 5, ma quanto più lente? Per i miei flussi di lavoro sono comunque sostenibili?

---

## 🤖 Assistant

Sì. La tua intuizione sulla **performance tra RAID 5 e RAID 6** è corretta: RAID 6 è più sicuro, ma ha un **costo prestazionale**, e questo costo va quantificato per capire se rimane accettabile nel tuo flusso di lavoro.

## ⚙️ Come cambia la velocità tra RAID 5 e RAID 6

### 📊 Letture
- In un array di tipo *parity* (come RAID 5 e RAID 6) **la velocità di lettura è molto simile in entrambi i casi**. I dati sono stripati su tutti i dischi e il controller può leggere in parallelo da più dischi. Le implementazioni RAID moderne non penalizzano praticamente il read rispetto al tipo di parità. cite

### 📝 Scritture
La differenza principale è nella **penalizzazione delle scritture** causata dal calcolo della parità.
- RAID 5 richiede un singolo blocco di parità per ogni stripe.
- RAID 6 richiede **due blocchi di parità**, quindi più calcolo e più dischi coinvolti. cite

In pratica:

- **Write sequenziali**: la penalità RAID 6 rispetto a RAID 5 si traduce in un throughput leggermente più basso. Benchmark reali segnalano che RAID 6 può avere una penalità di **~20–40 % sulle scritture** rispetto a RAID 5. cite
- **Read sequenziali**: molto vicini, spesso indistinguibili nella pratica per workflow video. cite
- **Scritture casuali/I-O**: la doppia parità aggiunge overhead maggiore di RAID 5, ma non è il colpo mortale che molti immaginano (la differenza è reale, ma non proibitiva per carichi sequenziali pesanti). cite

### 📈 Esempio pratico ipotetico
In un array da 8 dischi (tipo il tuo caso):

- RAID 5 potrebbe darti **~1,3–1,5 GB/s in sequenziale** in lettura e scrittura (dipende da dischi e controller, ma è realistico con dischi Enterprise in RAID 5 su controller adeguato).
- RAID 6 potrebbe arrivare a **~1,0–1,2 GB/s in scrittura sequenziale**, mentre le letture rimangono simili a RAID 5.

Non esiste un numero “fisso”, perché dipende da dischi, controller e cache del controller.

**In sostanza:**
- **RAID 6 è più lento in scrittura**, ma non di un ordine di grandezza.
- **Letture quasi identiche a RAID 5** (quindi editing e playback non soffrono significativamente).
- Penalità maggiore si vede in *piccoli I/O random* o in *operation di metadata intensivi*, non nella scrittura sequenziale di grandi blocchi (tipica dei video). cite

## 📌 Sostenibilità rispetto ai tuoi flussi di lavoro

Per un utilizzo tipo:

- **Montaggio/editing video 4K/8K**
- **Catalogazione e sviluppo RAW**
- **Media streaming e backup interni**

la perdita di performance in RAID 6 **non dovrebbe rendere l’array inutilizzabile**.
Anche con una penalità del 20–30 % sulle scritture, se RAID 5 ti arriva a ~1300–1500 MB/s, RAID 6 dovrebbe rimanere **ben sopra il limite pratico di molti workflow HDD-bound**, ovvero ben oltre i 1000 MB/s sequenziali in lettura/scrittura, il che è più che sufficiente per editing nativo di multi-stream 4K/8K e file RAW di grandi dimensioni. cite

## 🧠 Perché RAID 6 può convenire

I vantaggi concreti di RAID 6 rispetto a RAID 5 in un’unità da 8 dischi grandi:

- **Tolleranza a due guasti simultanei** → fondamentale con dischi di grande capacità e lunghi tempi di rebuild. cite
- **Maggiore sicurezza generale senza dover stringere i denti** rispetto alla “speranza che non si guasti un altro disco durante il rebuild”. cite
- Per gestire grandi volumi video e RAW, questa stabilità vale quasi sempre la piccola perdita di performance.

## 📌 Conclusione professionale

- **RAID 6 perfettamente sostenibile per editing e lavoro professionale**, con una penalità di velocità accettabile (scritture sequenziali ancora alte).
- **Differenza pratica sulle velocità reali**: RAID 5 è un po’ più veloce in scrittura, ma **non così tanto da diventare un collo di bottiglia nei casi d’uso sequenziali tipici** dell’audio/video heavy.
- **RAID 6 è consigliabile** se usi dischi grandi > 8 TB e vuoi ridurre il rischio di perdita dati e ricostruzioni rischiose.

Se vuoi, posso quantificare **una stima numerica più precisa** basata sulla **dimensione di dischi specifici che stai considerando** (es. 10 TB vs 18 TB) e sulla **configurazione RAID (5 vs 6)**: ti direi a livello numerico cosa aspettarti in throughput reale. Per farlo, dammi marca/capacità dei dischi che pensi di montare nell’array.

---

## 🧑 User

Ok, quindi per i dischi... Poi in realtà, se io faccio per esempio video editing dal disco, non dovrebbe essere differenziato perché poi in quel caso i dati sono già stipati all'interno di un hard drive e quindi io quando faccio video editing principalmente lavoro in lettura, non tanto in scrittura. cioè quello che mi dà la velocità è la velocità con cui il computer accede alle informazioni e quindi è lettura più che scrittura. Idem se faccio editing fotografico.

---

## 🤖 Assistant

Esatto. Qui bisogna essere chirurgici.

Nel tuo caso, quando fai:

- editing video
- grading in Resolve
- sviluppo RAW
- browsing cataloghi Lightroom
- playback multicam

sei **quasi sempre in lettura sequenziale**, non in scrittura.

La scrittura diventa rilevante solo quando:

- importi grossi batch
- esporti timeline finali
- fai copie massive
- generi proxy o cache pesanti

Durante il lavoro vero e proprio, il disco sta principalmente leggendo.

---

## Cosa significa per RAID 5 vs RAID 6

Con 8 dischi 7200 rpm enterprise:

### 🔹 Lettura sequenziale
RAID 5 ≈ RAID 6
Praticamente identiche.

Con dischi moderni:
- 1.2–1.5 GB/s è realistico
- Il limite spesso diventa il controller o Thunderbolt, non il livello RAID

Per il tuo flusso:

- Sony A1 RAW → nessun problema
- 4K 120 XAVC S-I → nessun problema
- ProRes 4K multicam → nessun problema
- Anche 8K compresso è gestibile

La lettura non è il collo di bottiglia.

---

### 🔹 Scrittura sequenziale
RAID 6 perde qualcosa rispetto a RAID 5.

Ma attenzione:
su controller hardware seri (come Shuttle XL), la differenza non è devastante.

Indicativamente:

- RAID 5: ~1300–1500 MB/s
- RAID 6: ~1000–1200 MB/s

Non stai passando da 1500 a 400.
Stai perdendo il 20–30%, non l’80%.

Per esportazioni video o ingest massivo, non è un dramma.

---

## La vera questione: dischi grandi

Con 8 dischi da 16–18–20 TB:

- rebuild può durare molte ore
- durante rebuild l’array è sotto stress
- con RAID 5 basta un secondo errore → perdita totale

E qui la matematica non perdona.

Su array grandi RAID 6 è oggettivamente più sensato.

---

## Per il tuo profilo professionale

Tu:

- produci tanto materiale
- non lavori con proxy leggeri sempre
- hai flussi documentaristici e commerciali
- archivi a lungo termine

Per te RAID 6 è la scelta più lucida.

Perderai un po’ di velocità in scrittura.
Non perderai velocità significativa in lettura.
Guadagnerai molta più tranquillità.

---

## Una cosa importante che pochi considerano

La differenza percepita di velocità nel tuo workflow dipenderà più da:

- cache RAM
- NVMe scratch disk
- gestione cache Resolve
- disco di sistema

che dal fatto che sia RAID 5 o 6.

Se vuoi un setup veramente ottimizzato:

- NVMe interno per cache / working project
- Shuttle XL RAID 6 come storage master

Questa è una configurazione solida, coerente con il tuo tipo di produzione.

---

Se vuoi facciamo il passo successivo:
ti dico quali dischi scegliere per massimizzare affidabilità e performance dentro quello chassis.

---

## 🧑 User

OK, se io recuperassi invece un vecchio, come si dice, dispositivo che è Thunderbolt 2, chiaramente in quel caso ho bisogno di un adattatore, se io nei miei dispositivi ho tutti quanti l'attacco che è almeno Thunderbolt 3. Che, presumo, non sia questo il problema. Mi diceva un mio amico che ce l'ha, che però ha avuto dei problemi di compatibilità con i Mac Apple Silicon, che ha dovuto flashare un firmware perché altrimenti non gli dava la compatibilità e la rottura di scatole è che ogni volta che esce un sistema operativo nuovo devi andare a cercarsi questa roba qua perché perde la compatibilità. Questa roba qua per me chiaramente è il vero colpo di bottiglia, non è tanto la velocità del dispositivo, perché oggettivamente andare a 1000 mega, come siamo abbondantemente sopra le necessità che ci sono per il tipo di video che faccio io, anche quel dispositivo lì è compatibile, compatibile Red 5 e 6, che è quello che interessa a me. L'altra questione è voler capire a livello di compatibilità di hard drive, che cosa cambia tra il Thunderbolt 2, il Thunderbolt 3 e il SanDisk Professional.

---

## 🤖 Assistant

Qui il punto non è la velocità.
Il punto è **compatibilità futura e rotture con macOS + Apple Silicon**.

Ti rispondo diretto.

---

# 1️⃣ Thunderbolt 2 oggi su Apple Silicon

Tecnicamente funziona così:

- Serve **adattatore Apple Thunderbolt 3 ↔ Thunderbolt 2**
- Funziona solo con adattatore originale Apple (non equivalenti)
- Catena: Mac TB3/4 → adattatore → cavo TB2 → Shuttle TB2

Finché parliamo di puro protocollo Thunderbolt, è retrocompatibile.

Il problema non è il bus.

Il problema è **il software del controller RAID**.

---

## Dove nascono i problemi

I vecchi G-Speed TB2 usano:

- driver kernel legacy
- utility RAID non sempre aggiornate
- firmware scritti in epoca Intel

Con Apple Silicon:

- niente driver kernel non firmati
- niente estensioni legacy
- Rosetta non aiuta con driver a basso livello
- macOS aggiorna spesso la gestione sicurezza I/O

Risultato:
alcuni utenti hanno dovuto:

- aggiornare firmware del controller
- aspettare utility compatibili ARM
- reinstallare driver dopo update macOS

Ogni major release di macOS può diventare un’incognita.

E questo per un sistema da 5–8 mila euro è una cosa che non vuoi.

---

# 2️⃣ Thunderbolt 3 (versione G-Technology pre-SanDisk)

Qui la situazione cambia molto.

I modelli TB3:

- sono nati in era macOS più moderna
- hanno driver e utility aggiornate più a lungo
- sono ufficialmente dentro il perimetro di supporto WD/SanDisk più recente
- sono già stati usati ampiamente su Apple Silicon

Qui la probabilità di rotture post-update è molto più bassa.

Non zero. Ma molto più bassa.

---

# 3️⃣ SanDisk Professional (attuale)

È sostanzialmente:

- evoluzione della piattaforma TB3
- stessa architettura concettuale
- firmware più recente
- supporto ufficiale attivo

Qui sei nella situazione più tranquilla in assoluto.

---

# 4️⃣ Compatibilità hard drive tra TB2 / TB3 / SanDisk

Quasi nulla cambia.

Lo chassis monta:

- SATA 3 6Gb/s backplane
- controller RAID hardware

I dischi compatibili sono gli stessi:

- HDD SATA 3 7200rpm
- enterprise consigliati
- nessuna differenza tra TB2 e TB3 lato compatibilità disco

Quello che cambia è:

- controller revision
- firmware
- supporto OS

Non la compatibilità dei dischi.

---

# 5️⃣ Il vero rischio del TB2

Non è la velocità.
Non è RAID 5 vs 6.
Non sono i dischi.

È questo:

Fra 2 anni esce macOS 18.
Il driver RAID TB2 non viene più aggiornato.
Il sistema non monta più l’array.

E tu sei fermo finché non trovi workaround.

Per un freelance che lavora su commissione, è un rischio inutile.

---

# 6️⃣ Valutazione razionale per te

Tu:

- lavori su Mac moderni
- aggiorni sistema operativo
- usi Apple Silicon
- non vuoi instabilità

Il TB2 ha senso solo se:

- costa pochissimo
- lo usi come archivio secondario offline
- non è storage primario di lavoro

Se deve essere storage principale → evita TB2.

---

# 7️⃣ Sintesi brutalmente onesta

Se il prezzo è simile:

- ❌ TB2 → no
- ✅ TB3 G-Technology → sì
- ✅ SanDisk Professional → scelta più pulita

Non stai comprando solo banda.
Stai comprando **anni di compatibilità futura**.

---

Se vuoi, nel prossimo messaggio ti faccio una valutazione numerica concreta:

- quanto dovrebbe costare un TB2 per valere il rischio
- quanto vale economicamente la differenza di compatibilità TB3
- se a questo punto conviene guardare un’alternativa moderna (es. DAS 10GbE o chassis diverso)

Così la decisione la prendiamo su base economica, non emotiva.

---

## 🧑 User

Ok, mi dici quindi le differenze che ci sono a livello di compatibilità con le dimensioni degli hard disk?

---

## 🤖 Assistant

Qui andiamo molto concreti.

La differenza tra **Thunderbolt 2**, **Thunderbolt 3** e **SanDisk Professional** *non è nel Thunderbolt*.
È nel **controller RAID interno e nel firmware**.

Il bus esterno non limita la dimensione dei dischi.
Il controller sì.

---

# 1️⃣ Limiti di capacità dischi – cosa conta davvero

Le variabili che determinano la compatibilità sono:

- Controller RAID (Areca based nei G-Speed)
- Firmware del controller
- Supporto LBA 48-bit
- Gestione dischi > 2 TB
- Gestione dischi > 16 TB / > 18 TB (4K native)

---

# 2️⃣ G-Speed Shuttle XL Thunderbolt 2

⚠️ Qui bisogna stare attenti.

I modelli TB2 più vecchi:

- Nascevano quando i dischi da 4–8 TB erano lo standard
- Molti sono stati aggiornati via firmware per supportare 10–12–14 TB
- I 16 TB spesso funzionano
- 18 TB e 20 TB dipende dalla revisione firmware

Non tutti i TB2 sono uguali.

Se il firmware è aggiornato all’ultima revisione disponibile, in genere:

- 14 TB → sicuro
- 16 TB → molto probabile
- 18 TB → da verificare
- 20 TB → incerto

Il rischio è comprare l’unità e scoprire che non monta correttamente dischi molto recenti.

---

# 3️⃣ G-Speed Thunderbolt 3

Qui la situazione è più tranquilla.

Essendo più recente:

- nato in epoca dischi 12–14 TB
- firmware più moderno
- migliore gestione 4Kn

In genere:

- 16 TB → ok
- 18 TB → ok
- 20 TB → quasi sempre ok
- 22 TB → da verificare ma probabile

---

# 4️⃣ SanDisk Professional G-Drive Shuttle 8

È la versione più aggiornata.

Supporta ufficialmente dischi enterprise di ultima generazione.

Qui realisticamente:

- 18 TB → ok
- 20 TB → ok
- 22 TB → molto probabile
- 24 TB → dipende ma molto più sicuro rispetto a TB2

---

# 5️⃣ Attenzione alla questione 4Kn vs 512e

Dischi moderni grandi spesso sono:

- 512e (emulazione 512 byte)
- oppure 4Kn nativi

I controller più vecchi possono avere problemi con 4Kn puro.

TB2 → rischio maggiore
TB3 → molto meno
SanDisk → minimo

---

# 6️⃣ La cosa davvero importante per te

Se stai pensando a:

8 dischi × 18 TB
oppure
8 dischi × 20 TB

stai parlando di:

- 144 TB raw
- 160 TB raw

Qui io eviterei TB2 senza nemmeno pensarci.

Non perché non funzioni.
Ma perché non vuoi essere tu a scoprire il limite.

---

# 7️⃣ Riassunto pratico

Se vuoi stare tranquillo con dischi grandi moderni:

- TB2 → solo se monti 12–14 TB e vuoi risparmiare
- TB3 → buon compromesso
- SanDisk → scelta più sicura per dischi 18–22 TB

---

# 8️⃣ Considerazione strategica per il tuo archivio

Tu produci tanto materiale video.

Se vuoi costruire un archivio serio che ti duri 5–7 anni:

- meglio piattaforma moderna
- meglio compatibilità con dischi grandi
- meglio firmware ancora supportato

Perché tra 3 anni i 20 TB saranno lo standard, non l’eccezione.

---

Se vuoi, dimmi che taglio stai considerando (16? 18? 20 TB?)
e ti faccio una simulazione precisa:

- capacità effettiva RAID 5
- capacità effettiva RAID 6
- rischio rebuild
- costo per TB reale.