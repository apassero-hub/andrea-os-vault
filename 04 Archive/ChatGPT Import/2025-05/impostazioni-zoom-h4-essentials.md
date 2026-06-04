---
title: "Impostazioni Zoom H4 Essentials"
created: 2025-05-22
updated: 2025-05-22
model: gpt-4o
messages: 10
source: chatgpt-import
tags: []
---

# Impostazioni Zoom H4 Essentials

> Importato da ChatGPT export · 10 messaggi · gpt-4o · 2025-05-22

## 🧑 User

mi dici come settare al meglio il mio zoom h4 essential considerato che collegherò via jack mini il ricevitore del dji e in xlr un microfono rode ntg4?

---

## 🤖 Assistant

Perfetto, Andrea — con DJI via mini-jack e un **RØDE NTG4 in XLR** stai costruendo un setup molto solido per una registrazione audio professionale. Ecco come settare al meglio lo **Zoom H4essential** in questo scenario:

---

### 🎛️ Collegamenti fisici
1. **Ingresso 1 (XLR)**: collega qui il **RØDE NTG4**.
- Se usi il cavo XLR standard, questo è il canale che riceverà l'audio del microfono.
- L’NTG4 ha bisogno di **phantom power a 48V**.

2. **Ingresso 3/4 (mini-jack stereo)**: collega qui il **ricevitore DJI Mic**.
- Normalmente esce in **stereo non bilanciato**, con il segnale del mic A su L e mic B su R.

---

### ⚙️ Impostazioni consigliate nello Zoom H4essential

#### 🔌 Phantom Power
- Vai in **Menu > Input > Phantom Power** e abilita **48V** solo su **Input 1** (dove è collegato l’NTG4).

#### 🎚️ Gain input
- **Input 1 (NTG4)**: imposta un **gain iniziale a ~35-45** e fai un test parlato.
- Regolati in modo che i **picchi** arrivino tra **-12dB e -6dB**.
- **Input 3/4 (DJI)**: probabilmente non puoi regolare il gain separatamente, ma controlla che i livelli non siano troppo alti. Se saturano, regola l’output del DJI Mic.

#### 🎧 Monitoraggio
- Collega le cuffie e verifica il bilanciamento:
- **Canale 1** sarà l’NTG4.
- **Canale 3/4** sarà stereo: mic A sinistra, mic B destra (se usi entrambi).

#### 🎙️ Modalità di registrazione
- Vai su **Menu > Record Mode** e seleziona:
- **Multitrack (MTR)** se vuoi avere ogni sorgente su una traccia separata.
- **Canale 1 = NTG4**
- **Canale 3/4 = DJI stereo**
- Oppure **Stereo Mix** se vuoi un mixdown in una traccia stereo (sconsigliato per editing successivo).

---

### 🎥 Consigli finali per usi video
- **Clappa** a inizio take per sincronizzare facilmente in post.
- Se possibile, usa **registrazione dual gain** anche dal DJI Mic, per avere una traccia di backup a -6dB.
- Registra in **WAV 48kHz / 24bit**.

---

Se vuoi, ti preparo uno **schema visivo** o un preset scritto delle impostazioni da avere sempre con te. Vuoi anche sapere come gestire l’esportazione dei file o il flusso in post produzione?

---

## 🧑 User

uso solo un dji mic con rode lavalier quindi su canale l-r ci sarà quello

---

## 🤖 Assistant

Perfetto, grazie del chiarimento!

Quindi ricapitolando:
- **Canale 1 (XLR)** → **RØDE NTG4 (direzionale on camera)**
- **Canale 3/4 (mini-jack stereo)** → **DJI Mic con RØDE Lavalier** (solo 1 trasmettitore)

In questo caso, il **DJI Mic** manderà lo **stesso segnale mono su entrambi i canali L/R**, ma resterà un **segnale stereo duplicato** (utile saperlo per l’editing).

---

## ✅ Impostazioni consigliate su Zoom H4essential

### 1. 🔌 Phantom Power
- Vai su: `Menu > Input > Phantom Power`
- **Attiva 48V solo su INPUT 1** (per alimentare l’NTG4)

---

### 2. 🎚️ GAIN consigliati

| Ingresso | Dispositivo | Impostazione Gain | Note |
|--------------|--------------------|-------------------|------|
| **Input 1** | RØDE NTG4 | **35–45** | Regola in base al volume ambientale |
| **Input 3/4**| DJI Mic (Lavalier) | Fisso sul DJI | Regola il livello di uscita sul ricevitore DJI |

⚠️ **Controlla che il ricevitore DJI non stia clippando** prima di entrare nello Zoom! L’output va regolato sul ricevitore stesso (di solito tra -6dB e -12dB è ideale).

---

### 3. 🎛️ Modalità di registrazione
Vai su: `Menu > Record Mode`

📌 **Scegli “Multitrack”**
In questo modo:

- **Traccia 1** → RØDE NTG4 (microfono camera)
- **Traccia 3/4** → DJI Mic (RØDE Lavalier, registrato su L/R)

Così potrai mixarli separatamente in post (es. usare il lav per i dialoghi e il NTG4 come backup/ambiente).

---

### 4. 🎧 Monitoraggio cuffie
Premi il tasto **“Mixer”**, regola i volumi e verifica:

- NTG4 si sente solo a sinistra (canale 1)
- DJI Mic si sente su entrambi i canali, ma in stereo (L=R)

---

### 5. 💾 Registrazione
- **Formato consigliato**: WAV 48kHz / 24bit
- **Opzione utile**: attiva il **Pre-Rec** se sei in situazioni imprevedibili (salva 2 secondi prima del REC)

---

## 🎬 Consiglio finale per sincronizzazione
- All’inizio del take: **batti le mani** o usa una clapboard se puoi — ti aiuterà in post produzione per allineare audio/camera se non registri timecode.

---

Se vuoi, ti preparo un **PDF di riferimento rapido** con le impostazioni da usare per questo setup, così da tenerlo sempre nello zaino. Fammi sapere!

---

## 🧑 User

ma per la parte multi track non basta solo attivare i diversi microfoni da cui voglio registrare e premere rec?

---

## 🤖 Assistant

Sì, hai **perfettamente ragione** — sullo **Zoom H4essential**, non devi complicarti troppo la vita con la modalità **Multitrack** come succedeva in vecchie versioni o su modelli come l’H6. Ecco come funziona davvero **in pratica** per te:

---

## ✅ COME REGISTRARE MULTITRACCIA SU ZOOM H4essential

### 🎙️ Collegamento:
- **Input 1 (XLR)** → **RØDE NTG4**
- **Input 3/4 (mini-jack)** → **DJI Mic con RØDE Lavalier**

---

### ✅ Procedura *step-by-step* per registrare tutto correttamente:

1. **Accendi lo Zoom**
2. **Collega i microfoni**
3. Premi il tasto **[1]** per attivare il canale XLR
4. Premi il tasto **[3/4]** per attivare l’ingresso stereo mini-jack
5. Assicurati che:
- Il LED dei canali **[1]** e **[3/4]** sia **acceso (rosso)** → significa che registrerai da entrambe le fonti
6. Premi **REC una volta** per entrare in modalità standby/monitoring
- Controlla i livelli sul display: vedrai due barre
- Una per **Input 1**
- Una per **Input 3/4**
7. Premi **REC di nuovo** per avviare la registrazione
- Lo Zoom creerà **un file stereo**, ma se vuoi avere **tracce separate**, attiva la funzione che ti spiego qui sotto ↓

---

## 🛠️ Per avere file separati in post (vero multitrack):
- Vai su: `Menu > Record Settings > Mix Type`
- **Scegli: “Multi File”**
👉 Questo fa sì che ogni ingresso attivo venga salvato come file **WAV separato** (es. `TRACK01.WAV`, `TRACK03.WAV`), invece di un mix stereo unico.

---

## 🎧 In post produzione:
- Importi le due tracce (NTG4 + DJI)
- Allinei o scegli quale usare (es. lavalier per dialogo, NTG4 per ambiente)
- Oppure le mixi per avere più corpo nella voce

---

## ✅ Riepilogo operativo

| Fase | Azione |
|------------------|------------------------------------------------------------------------|
| Collegamenti | NTG4 su XLR / DJI su mini-jack |
| Phantom Power | ON solo per Input 1 |
| Attivazione canali | Premi [1] e [3/4] finché i LED sono rossi |
| Livelli | Regola con il tasto GAIN (input 1), output DJI sul ricevitore |
| Rec Mode | Menu > Record Settings > Mix Type > **Multi File** |
| Registrazione | REC → controlla livelli → REC di nuovo |

---

Fammi sapere se vuoi un mini cheat sheet stampabile con queste impostazioni!

---

## 🧑 User

sulle impostazioni di registrazione cosa setto?

---

## 🤖 Assistant

Ottima domanda! Ecco **esattamente cosa settare** nella sezione **Impostazioni di registrazione** del tuo **Zoom H4essential** per ottenere **audio professionale**, coerente con il tuo setup RØDE NTG4 + DJI Mic Lavalier:

---

## 🎛️ Zoom H4essential – Impostazioni di Registrazione Consigliate

Vai in **Menu > Record Settings** e imposta come segue:

---

### 🎙️ **1. Input Settings**
- **Phantom Power**: `ON su Input 1` (per il NTG4)
- **Low Cut Filter**:
- **ON su Input 1**, frequenza: **80Hz**
👉 utile per rimuovere rimbombi e rumori ambientali bassi.
- **OFF su Input 3/4** (a meno che il DJI Mic sia molto sensibile a rumori da maneggiamento)
- **Limiter**: `ON su entrambi i canali`
👉 protezione contro i picchi improvvisi.
- **Compressor/Enhancer**: `OFF`
👉 lascia la registrazione più naturale; meglio regolare in post.
- **Auto Gain**: `OFF`
👉 meglio regolare i livelli manualmente per un audio più controllato.

---

### 🎧 **2. Record Mode**
- **Mode**: `Stereo` se vuoi una traccia unica con NTG4 a sinistra e DJI a destra
**oppure:**
**Mode**: `Multi File` (consigliato)
👉 così il file del NTG4 e quello del DJI vengono salvati **separatamente**.

---

### 💾 **3. Format**
- **File Format**: `WAV`
- **Sample Rate**: `48kHz`
- **Bit Depth**: `24bit`
🎯 Standard broadcast/video: perfetto per post-produzione e sincronizzazione audio-video.

---

### 🕒 **4. Altre impostazioni utili**
- **Pre-Record**: `ON`
👉 Salva 2 secondi prima della pressione di REC. Ottimo per non perdere attacchi vocali.
- **Backup Recording** (se presente): `ON`
👉 registra una seconda traccia a -12dB (solo per certi input) – **verifica se è disponibile nel menu del tuo modello**.
- **Monitor Mix**: `Setta in modo da ascoltare entrambi i canali (1 e 3/4)` nel monitoraggio cuffie.

---

## 🎧 Livelli ideali
- Punta a picchi tra **-12dB e -6dB**
- Se lavori all’aperto o in situazioni instabili, meglio restare su **-12dB** e usare il **limiter**

---

Se vuoi, posso crearti un **PDF pronto all’uso con queste impostazioni**, oppure uno **screenshot-style mockup** dei menu Zoom per aiutarti a settarlo più velocemente. Fammi sapere.

---

## 🧑 User

sorgente di registrazione pre mixer o post mixer?

---

## 🤖 Assistant

Ottima domanda — e fondamentale per non rovinarti una registrazione 🔥

---

### 🎚️ **Zoom H4essential – "Recording Source": Pre Mixer vs Post Mixer**

Questa impostazione definisce **cosa viene effettivamente registrato**:

- **🔹 PRE MIXER**:
✅ Registra **il segnale puro** in ingresso (prima che venga influenzato da EQ, livelli, pan ecc.)
👉 **Ideale se vuoi avere più margine in post-produzione**, lavorare con le tracce “pulite” e non rischiare errori di mix.

- **🔸 POST MIXER**:
🎧 Registra **il segnale come lo senti nel monitor cuffie**, già processato da eventuali modifiche al pan, livelli e routing.
👉 Va bene **solo se vuoi un mix definitivo** da usare subito (tipo per livestream, backup semplificato o zero editing in post).

---

## ✅ Cosa usare nel tuo caso?

Hai due fonti diverse:
- **RØDE NTG4** → voce ambientale/direzionale
- **DJI Mic con lavalier** → voce close-up primaria

🔹 **Imposta su: `PRE MIXER`**

### Perché:
- Ti garantisce la **massima flessibilità** in post.
- Registra ogni ingresso **nudo e crudo**, senza errori accidentali di mix o bilanciamento.
- Il monitoraggio in cuffia sarà ancora mixato, ma la registrazione rimane “pulita”.

---

## 📍 Dove si imposta
Vai su:
```
Menu > Record Settings > Recording Source > PRE MIXER
```

---

Fammi sapere se vuoi una checklist completa definitiva del tuo setup così puoi salvarla o stamparla!