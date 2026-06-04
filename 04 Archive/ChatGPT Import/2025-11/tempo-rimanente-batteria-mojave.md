---
title: "Tempo rimanente batteria Mojave"
created: 2025-11-26
updated: 2025-11-26
model: gpt-5-1
messages: 16
source: chatgpt-import
tags: []
---

# Tempo rimanente batteria Mojave

> Importato da ChatGPT export · 16 messaggi · gpt-5-1 · 2025-11-26

## 🧑 User

su mac mojave come faccio a far si che l'indicatore della batteria mi dica anche il tempo rimanente se ci clicco sopra?

---

## 🤖 Assistant

Su macOS Mojave **non esiste più l’opzione nativa** per mostrare *“tempo rimanente”* della batteria. Apple l’ha rimossa a partire da macOS Sierra 10.12.2. Mojave **non lo supporta** né nel menu della batteria né nelle Preferenze di Sistema.

Se vuoi comunque visualizzarlo, hai **due possibilità**:

## 1. App di terze parti affidabili
Sono l’unico modo pratico. Le più usate:

- **CoconutBattery** (gratuita)
Mostra tempo stimato rimanente, cicli, capacità reale, stato salute.
- **iStat Menus** (a pagamento)
Integra nel menubar tempo rimanente, watt, consumo in tempo reale, temperature, ecc.

Queste app leggono direttamente i dati SMC, quindi l’indicazione è precisa quanto quella che Apple avrebbe mostrato.

## 2. Terminale (solo test, non comodo)
Puoi ottenere la stima con:

```bash
pmset -g batt
```

Otterrai un output tipo:
```
Now drawing from 'Battery Power'
-InternalBattery-0 (id=XXXX): 78%; discharging; (time remaining) 2:34
```

Ma **non compare nel menù batteria**, devi aprire il Terminale ogni volta.

---

### Conclusione
Su Mojave il tempo rimanente **non può essere reinserito** nel menu nativo. Se ti serve nel menubar, installa CoconutBattery (gratis) o iStat Menus (il migliore).

Se vuoi ti indico esattamente quale versione scaricare per Mojave.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Il comando mostra correttamente il *tempo rimanente*, quindi la stima il sistema la calcola ancora.
Il punto è che **Apple non permette più di visualizzarla dal menu della batteria**, indipendentemente dal fatto che `pmset` la mostri.

Chiarisco rapidamente la situazione, visto anche lo screenshot:

### 1. Il tuo output è corretto
`pmset -g batt` mostra:

```
91%; discharging; 3:06 remaining
```

Quindi il sistema stima il tempo, semplicemente **non lo espone nell’interfaccia grafica**.

### 2. Non c’è modo di riabilitare il “tempo rimanente” nel menu batteria
Nemmeno con comandi nascosti, modifiche plist o patch. Da macOS 10.12.2 Apple ha eliminato:

- il tempo rimanente nella barra menu
- la stima mostrata al click sull’icona

Mojave mantiene questa limitazione.
L’unica eccezione erano vecchi hack (tipo modifiche alle menuextra) che oggi non funzionano più.

### 3. Soluzione reale e più pulita
Usi una delle app che reintroducono l’indicazione nella menubar:

**Opzione consigliata (gratis):**
- CoconutBattery

**Opzione migliore (a pagamento):**
- iStat Menus (consigliato, preciso, stabile)

Sono le uniche due soluzioni affidabili che replicano esattamente quello che Apple ha tolto.

---

Se vuoi, ti preparo una configurazione minimale (icone + tempo rimanente) in iStat Menus in modo che nel menubar tu veda solo:

**🔋 3:06**

senza altre informazioni inutili.

---

## 🧑 User

come tempistica ti sembra in linea per un macbook pro 14 m3?

---

## 🤖 Assistant

Sì, il valore che vedi è **assolutamente in linea** per un MacBook Pro 14" con chip **M3**.

A 91% con uso reale, 3 ore e qualcosa rimanenti significa solo una cosa:
**stai consumando parecchia potenza in quel momento.**

La stima non riflette l’autonomia totale teorica, ma **l’andamento istantaneo**.
Sul tuo M3 Pro/M3 normale possono verificarsi questi scenari:

## Quando sono normali 3–4 ore rimanenti
Sono normali se stai facendo cose come:

- schermo quasi al massimo
- app pesanti aperte (Chrome, Lightroom, Discord, iStat, Zoom, ecc.)
- molte finestre attive
- monitor esterno collegato
- dock alimentato
- GPU in uso
- plugin o estensioni attive

In questi casi, anche un M3 arriva tranquillamente a **4–6 W – 15 W – 25 W** di consumo, e la stima scende subito a 3–4 ore.

## Quando l’autonomia reale deve essere più alta
Se stai solo:

- navigando leggero
- lavorando su testi
- YouTube non HDR
- schermo al ~40%
- niente monitor esterni

allora un M3 14" deve dare più o meno:

- **8–10 ore** effettive (M3 base)
- **7–9 ore** effettive (M3 Pro)

Con punte più alte se stai in modalità “low power”.

## Conclusione
La stima **non indica un problema**.
Indica solo che in quel momento il sistema stava prevedendo circa 3 ore rimanenti *basandosi sul consumo istantaneo*.

Se vuoi, mi dici:

- che app avevi aperte
- luminosità schermo
- monitor esterni/dock
- percentuale CPU/GPU ±

e ti dico se il tuo consumo è perfettamente nella norma o se c’è qualche processo energivoro.

---

## 🧑 User

veramente se clicco sulla batteria mi dice che nessuna app sta consumando molta energia. a parte chetgpt non ho niente di aperto

---

## 🤖 Assistant

Se ti dà **solo 3 ore rimanenti al 90%** *pur non avendo app energivore aperte*, allora la causa non è nelle app, ma in uno di questi fattori hardware/di sistema che **la voce “Nessuna app consuma molta energia” NON rileva**.

Ti dico direttamente cosa può causare questo comportamento su un **MacBook Pro 14" M3** e come capirlo al volo.

---

# 1. **Luminosità schermo alta (anche senza app energivore)**
Su un 14" M3, se tieni la luminosità all’80–100%, da sola può consumare **7–10 W**.

Con questo consumo, la stima diventa:
- all’80–100% luminosità → **3–5 ore totali**

È normale.
Molti utenti si stupiscono perché Apple non segnala “Schermo sta usando molta energia”, ma **non lo segnala mai**.

---

# 2. **Refresh a 120 Hz**
Se il tuo display è su **ProMotion 120 Hz**, l’autonomia crolla del 20–30%.

Controlla qui:
Impostazioni → Monitor → Frequenza → imposta 60 Hz
(o “Automatica”, se vuoi lasciare la gestione dinamica).

---

# 3. **ChatGPT Desktop (app) consuma più di quanto sembri**
L’app ufficiale ChatGPT mantiene processi attivi in background anche se non sembra.
In particolare:

- mantiene la GPU attiva per il rendering dell’interfaccia
- mantiene un processo “Electron-like” che può stare sui 4–8 W da solo

La voce “Non usa molta energia” guarda solo il *picco* e non il *consumo totale nel tempo*.

Quindi può consumare senza essere segnalato.

---

# 4. **Browser o WebKit lasciati aperti in background (Safari, Chrome, Arc)**
Anche una singola scheda può:

- attivare animazioni
- usare WebGL
- aggiornare contenuti

Senza che venga segnalata come “energiva”.

---

# 5. **Background system power (indexing, Photos, iCloud)**
Mojave non c’entra: il Mac che stai usando è su Sonoma/Sequoia.

Su macOS nuovo succede spesso che:

- **PhotoAnalysis** (riconoscimento volti)
- **MediaAnalysisD**
- **knowledgeconstructiond**
- **BirdOverlayAgent**
- **backupd**
- **mds/mdworker (Spotlight)**

lavorino in background senza comparire nel menu batteria.

---

# 6. **Dock Ugreen Revodok Max 213**
Se hai il dock collegato, anche *senza monitor attivo*, consuma:

- 4–9 W continui per il solo HUB
- + eventuale alimentazione USB
- + DisplayPort handshake (anche se il monitor è spento)

Questo è uno dei motivi più frequenti per cui vedi solo **3 ore stimate**.

Il dock Ugreen è famoso per essere energivoro.

---

# 7. **Monitor collegati**
Anche se il display è spento, la GPU resta “awake”.

---

# 8. **ChatGPT Desktop + Dock = autonomia ridotta**
È una combinazione che consuma, anche se visivamente sembra di non avere nulla aperto.

---

# Cosa fare per controllare davvero
Apri **Monitoraggio Attività → Energia → Ultime 12 ore**.

Dimmi:

- quali processi sono sopra **1.00** nella colonna *Energia*
- se bird, photoanalysisd, mediaservicesd o mds compaiono
- se il dock è collegato
- luminosità schermo
- refresh 60/120 Hz

Con questi dati ti dico subito dove stai perdendo watt e quanto è normale sul tuo M3.

---

## Risposta finale breve
**Sì: 3 ore rimanenti al 90% possono essere perfettamente normali su un M3**,
se hai luminosità alta, ProMotion attivo, app come ChatGPT aperta o un dock collegato.
Apple non segnala molte di queste condizioni come “app energivora”, quindi è normale che il menu batteria risulti “vuoto”.

Dimmi solo luminosità / refresh / dock / processi attivi e ti quantifico esattamente dov’è il consumo.

---

## 🧑 User

riformula

---

## 🤖 Assistant

Ecco la versione diretta e professionale.

Se ti mostra **3 ore rimanenti al 90%** anche senza app pesanti, la causa non è nelle applicazioni. È un consumo di sistema dovuto a uno di questi fattori, che **macOS non segnala come “app energivora”**:

1. **Luminosità alta** (70–100%).
Da sola può toglierti metà autonomia.

2. **Display a 120 Hz**.
ProMotion riduce l’autonomia

---

## 🧑 User

intendo i benefici di promotion

---

## 🤖 Assistant

ProMotion porta tre vantaggi reali:

## 1. **Fluidità visiva superiore**
Lo schermo arriva a **120 Hz** e si adatta dinamicamente.
Risultato: scrolling, animazioni, UI e transizioni molto più morbide.
La differenza è evidente soprattutto:

- nello scrolling veloce
- nel movimento delle finestre
- nelle animazioni di macOS
- in Photoshop/Lightroom quando sposti immagini o slider

## 2. **Riduzione dell’effetto “blur”**
A 120 Hz il movimento appare più nitido.
Quando scorri testo, liste o timeline, gli elementi restano più leggibili, senza scie.

## 3. **Maggiore reattività percepita**
La latenza tra input e risposta visiva è più bassa.
Il sistema *sembra* più veloce:
aperture di finestre, gesture trackpad, mission control, tutto risulta più immediato.

---

### Contro (che è giusto considerare)
- Consumo superiore rispetto a 60 Hz.
- Sulle app non ottimizzate la differenza è minima.
- Non porta vantaggi concreti nelle attività statiche (editing foto/video quando non stai muovendo elementi).

---

### In pratica
Per la maggior parte dell’uso quotidiano, ProMotion migliora l’esperienza.
Se vuoi massimizzare la batteria, passa temporaneamente a **60 Hz**.

---

## 🧑 User

col passaggio a 60hz siamo a 90% 4h e e 16min

---

## 🤖 Assistant

Perfettamente coerente.
Il passaggio da **120 Hz** a **60 Hz** tipicamente recupera **30–40% di autonomia reale** sui MacBook Pro 14".

Il salto che hai ottenuto:

- **Prima:** ~3h a 90%
- **Dopo:** **4h 16min a 90%**

è esattamente quello che ci si aspetta.
Significa che buona parte del consumo era dovuta alla frequenza del display, non alle app.

### Valutazione tecnica
Su un 14" M3, ProMotion può arrivare a consumare:

- +2–4 W in idle
- +5–7 W durante scrolling/animazioni

A 60 Hz togli quel carico extra e la stima sale immediatamente.

### In pratica
- Se devi lavorare **in mobilità**, tieni 60 Hz.
- Se lavori in studio o vuoi massima fluidità, torna a ProMotion senza problemi.

Se vuoi ti dico anche come capire, in tempo reale, quanti watt stai risparmiando passando da 120 a 60 Hz.

---

## 🧑 User

un 16" quando ha di differenza effettiva in termini di batteria?

---

## 🤖 Assistant

La differenza **reale**, non quella dichiarata da Apple, tra un **MacBook Pro 14"** e un **16"** in termini di autonomia è netta.
Il 16" ha un vantaggio costante che si traduce in **1.5–3 ore in più**, a parità di utilizzo.

Ecco i numeri veri.

---

# DIFFERENZA EFFETTIVA DI AUTONOMIA
## **MacBook Pro 14" M3 / M3 Pro**
Autonomia realistica (uso misto):
- **7–9 ore** M3 Pro
- **8–10 ore** M3 base
- In carichi medi → 5–7 ore
- Con ProMotion → calo anche del 30%

## **MacBook Pro 16" M3 Pro / M3 Max**
Autonomia realistica (uso misto):
- **10–13 ore** con M3 Pro
- **9–11 ore** con M3 Max
- In carichi medi → 7–9 ore
- ProMotion incide meno grazie alla batteria più grande

---

# DIFFERENZA TRA 14" E 16"
In condizioni equivalenti:

- Navigazione / lavoro leggero → **+2.5 ore** per il 16"
- Editing foto (Lightroom / Photoshop) → **+2 ore**
- Editing video leggero → **+1.5 ore**
- Standby/lavoro intermittente → **+3 ore**

La differenza deriva dal fatto che il 16" monta una batteria da:

- **99 Wh** (massimo consentito su un laptop)
- contro **70 Wh** del 14"

Quasi **il 40% in più di capacità**.

---

# DUE NOTE IMPORTANTI
1. **Il 16" scala meglio i consumi del display**
Lo schermo è più grande, ma il costo energetico di ProMotion incide percentualmente meno rispetto al 14". Per questo il tuo salto 120→60 Hz è enorme sul 14", molto meno sul 16".

2. **Su attività GPU-intensive il 16" resta acceso di più, non di meno**
Questo è controintuitivo per molti:
la GPU del 16" è più grande, ma essendo più efficiente per watt, la batteria enorme compensa.

---

# RISPOSTA BREVE
Il 16" offre **tra +1.5 e +3 ore** rispetto al 14", a seconda dell’uso.
È la macchina da scegliere se la batteria è una priorità.

Se vuoi ti faccio un confronto su misura basato sul tuo utilizzo reale (Lightroom, editing RAW, dock esterni, monitor, sessioni di editing fuori casa).