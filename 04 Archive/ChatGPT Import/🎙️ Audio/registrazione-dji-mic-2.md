---
title: "Registrazione DJI Mic 2"
created: 2025-09-11
updated: 2025-09-11
model: gpt-5
messages: 10
source: chatgpt-import
tags: [audio]
category: "🎙️ Audio"
---

# Registrazione DJI Mic 2

> Importato da ChatGPT export · 10 messaggi · gpt-5 · 2025-09-11

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Allora, ho collegato i DJI Mic 2 tramite l'adapter, il camera adapter, alla mia A7IV e quello che ho visto è che utilizzando un microfonino esterno, sempre DJI ha collegato tutto quanto, la camera adesso ha fatto un aggiornamento, diciamo, al ricevitore, ma mi dice che la registrazione è in 48 kHz, 16 bit, due canali. Perché è in 16 e non è in 24 bit? Cioè la registrazione interna non dovrebbe essere 24 bit. Il recorderino, cioè il transmitter, internamente registra 32 bit float, però dovrebbe mandarmi un segnale 24 e non 16 bit.

---

## 🤖 Assistant

Quello che stai vedendo sullo schermo della tua **Sony A7IV** è corretto, non è un bug.

La differenza sta qui:

- **DJI Mic 2 – trasmettitori**: registrano internamente in **32-bit float** (solo nella memoria interna, quando li usi come recorder autonomi).
- **Uscita analogica via camera adapter** (quella che entra nella tua A7IV tramite jack 3.5 mm): il segnale viene **convertito in linea stereo 16-bit / 48 kHz**.
- La **Sony A7IV** non accetta segnali a 24-bit tramite l’ingresso minijack: tutte le registrazioni in-camera sono limitate a **16-bit / 48 kHz**, a prescindere dal microfono o dal recorder esterno collegato. È un limite del corpo macchina, non del DJI.

Quindi:
- Se vuoi sfruttare i **32-bit float** → devi registrare internamente sui trasmettitori DJI Mic 2.
- Se registri solo in-camera (tramite il ricevitore + camera adapter) → rimarrai sempre a **16-bit / 48 kHz**.

Vuoi che ti preparo uno schema pratico con le varie combinazioni (in-camera, con recorder esterno, con trasmettitori DJI) così hai chiaro dove ottieni 16, 24 o 32-bit?

---

## 🧑 User

Ah, ok, va bene per il discorso dei 16-bit se registro direttamente dal cavo jack mini, ma io in questo caso qua non sto usando il cavo jack mini, lo sto utilizzando il trasmettitore collegato direttamente con il camera adapter all'attacco quello dell'Hotshoe, che ha appunto tutta la parte di connettori, e lo sto tenendo direttamente connesso così. Credevo, anzi davo per scontato, che in questa soluzione qua ci fosse una trasmissione di dati digitale, non analogica, e quindi ci fosse una qualità migliore.

---

## 🤖 Assistant

Chiaro, hai ragione a pensarla così perché in effetti l’hotshoe digitale di Sony (**MI Shoe**) supporta l’audio digitale. Però c’è una distinzione importante:

- **Con il DJI Mic 2 Camera Adapter su hotshoe MI Shoe**:
il segnale che passa è sì digitale, ma DJI lo limita comunque a **48 kHz / 16-bit, 2ch**. Non viene inviato un 24-bit, né tantomeno un 32-bit float.
→ Questo è un limite del sistema DJI, non della A7IV.

- **Con microfoni Sony digitali compatibili (es. ECM-B1M, ECM-B10, XLR-K3M ecc.)**:
la A7IV può ricevere fino a **24-bit / 48 kHz** in digitale direttamente dall’hotshoe.

In pratica:
- DJI ha scelto di mandare un flusso digitale “standardizzato” a 16-bit quando usi il Camera Adapter sull’hotshoe.
- I 24-bit (e i 32-bit float) rimangono esclusiva della registrazione interna ai trasmettitori.

Quindi sì, col Camera Adapter stai usando un collegamento **digitale**, ma la qualità rimane comunque bloccata a **16-bit / 48 kHz** per design.

Vuoi che ti indichi un workflow ibrido per avere:
- traccia di sicurezza 32-bit float interna ai trasmettitori DJI
- più file in 24-bit/48 kHz registrati direttamente in camera tramite MI Shoe (senza passare dal jack)?

---

## 🧑 User

Dai, vai, sentiamo.

---

## 🤖 Assistant

Perfetto, ti faccio un quadro chiaro e pratico. Con i DJI Mic 2 + Sony A7IV hai tre opzioni reali:

---

### **1. Solo registrazione interna DJI (32-bit float)**
- I trasmettitori registrano in **32-bit float** nella loro memoria.
- In camera ricevi comunque un **16-bit / 48 kHz** (via MI Shoe o jack).
- Workflow: usi l’audio camera solo come sync/reference, e in post importi i file 32-bit float dai trasmettitori.
- Pro: massima qualità e sicurezza dinamica.
- Contro: serve sempre fare sync in post.

---

### **2. Registrazione ibrida (consigliata per lavori seri)**
- Attivi **registrazione interna 32-bit float** sui trasmettitori DJI.
- In parallelo mandi il flusso al ricevitore collegato alla A7IV via MI Shoe.
- Risultato:
- In camera hai un file già pronto (16-bit / 48 kHz), sincronizzato con il video.
- Se serve recupero dinamica o fix, prendi i **32-bit float** dai trasmettitori e sostituisci in post.
- Pro: workflow veloce (hai subito l’audio in camera), ma con backup di lusso.
- Contro: un filo più di lavoro se devi rientrare sui file 32-bit.

---

### **3. Solo flusso diretto in camera (fast & dirty)**
- Registri solo con il Camera Adapter via MI Shoe → **16-bit / 48 kHz** direttamente dentro i file video.
- Pro: niente sync, file subito pronto.
- Contro: zero margine, se clippi o registri basso sei fregato.

---

📌 **Consiglio pratico per te (lavori professionali)**
Vai sempre con la **soluzione 2 (ibrida)**:
- Traccia camera subito pronta per montaggi veloci.
- Backup 32-bit float interno ai trasmettitori per salvataggi o progetti importanti.

Vuoi che ti preparo un **diagramma operativo step-by-step** (setup trasmettitori, impostazioni camera, gestione file in post) così te lo tieni come reference rapido?

---

## 🧑 User

Ok, grazie delle informazioni. Invece sto guardando sul menu del ricevitore e praticamente ho accenso e spegnimento simultaneo della fotocamera che si è attivato. Il ricevitore si accenderà e spegnerà automaticamente insieme alla fotocamera quando è collegato tramite TRS e quindi se ce l'ho collegato con il camera adapter che legge il segnale direttamente dalla camera tramite Mishu. Cioè non mi legge se la camera è acceso e spenta e quindi non si accende e si spegne in automatico. Sembra una troiata. Cioè lo fa dal cavo esterno ma non lo fa se è collegato direttamente.

---

## 🤖 Assistant

Hai centrato un punto che in effetti sembra assurdo, ma è proprio così.

- **Collegamento TRS (cavo jack 3.5 mm)** → il ricevitore “sente” la tensione che arriva dal jack microfono della fotocamera e quindi può sincronizzare l’accensione/spegnimento.
- **Collegamento MI Shoe (camera adapter)** → il collegamento è digitale, ma DJI non ha implementato il trigger di power sync via hotshoe. Risultato: il ricevitore non legge lo stato on/off della A7IV e quindi resta scollegato dal ciclo di accensione della camera.

Questo è un **limite firmware/hardware del DJI Mic 2**, non della A7IV. Infatti con i microfoni Sony digitali (tipo ECM-B1M o XLR-K3M) il power sync via hotshoe funziona perfettamente: quando accendi la camera, si accende anche il microfono.

Quindi sì, è un po’ una “troiata” da parte di DJI: ti danno l’adapter digitale, ma non hanno integrato tutte le funzioni che Sony invece supporta nativamente con i suoi microfoni.

Vuoi che ti verifichi se DJI ha previsto un **firmware update** per abilitare il power sync via hotshoe o se è proprio un limite strutturale dell’adapter?

---

## 🧑 User

Sì, controlla pure se hai aver visto qualcosa e controlla anche se per caso c'è un aggiornamento firmware che va fatto in relazione al camera adapter perché io ho controllato che il firmware che è installato su DJI Mix sia l'ultima versione e effettivamente è l'unica ultima versione con cui è stato rilasciato che risulta essere la stessa che c'è sul sito ma con un nome diverso perché ovviamente è stato rilasciato dopo però appunto siccome quando ho connesso il power adapter mi ha dato un aggiornamento vorrei che magari ci fosse qualche altro update che si può fare

---

## 🤖 Assistant

Ecco cosa ho trovato, senza giri di parole: non c’è evidenza che DJI abbia abilitato il power-sync (accensione/spegnimento con la fotocamera) quando il ricevitore è collegato via **Camera Adapter / MI Shoe**. È dichiarato esplicitamente nei documenti DJI che quella funzione *non* è supportata in quella configurazione. cite

---

### 🔍 Cosa dice la documentazione DJI

- Nel documento “DJI Mic 2 Camera Adapter - Support” si afferma chiaramente:
> *“The DJI Mic 2 receiver (RX) **does not support Power On/Off Camera Simultaneously when connected to the camera via the DJI Mic 2 Camera Adapter.”* cite

- La guida utente (User Manual) descrive la funzione “Power On/Off Camera Simultaneously” come operativa **solo se collegato tramite cavo TRS 3,5 mm** analogico. cite

- Viene anche specificato che l’adapter per la videocamera supporta audio digitale e alimentazione, ma non menziona il power-sync. cite

---

### ⚙️ Per quanto riguarda firmware / aggiornamenti

- L’adapter ha un firmware aggiornabile: la documentazione DJI dice che una volta aggiornato il ricevitore, se l’adapter è collegato, il ricevitore dovrebbe riconoscere l’adapter e aggiornare anche quello. cite

- Ma nessuna release notes / changelog che ho trovato aggiornata fino ad oggi include un cambiamento che abiliti il power sync via Camera Adapter. Nessun “what’s new” che dica “added support for power on/off with camera via camera adapter” per Mic-2. (Ho cercato online nei forum, pagine ufficiali aggiornamenti, FAQ).

---

### ✅ Conclusione

Sulla base delle info attuali:

- È un **limite volontario / progettuale**: DJI non ha implementato il power-sync tramite l’adapter digitale per il Mic 2.
- Non ci sono update noti che cambino questa cosa al momento.

---

Se vuoi, posso controllare nello specifico le versioni firmware installate sul tuo Mic 2 + adapter + A7IV e confrontare con le versioni che DJI ha per “feature request”, vedere se magari su forum cinesi/altrove qualcuno ha scoperto un firmware beta che introduce quella funzione. Vuoi che lo faccia?