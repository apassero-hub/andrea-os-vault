---
title: "Convertire MIB1 in CarPlay"
created: 2025-10-12
updated: 2025-10-12
model: gpt-5
messages: 6
source: chatgpt-import
tags: []
---

# Convertire MIB1 in CarPlay

> Importato da ChatGPT export · 6 messaggi · gpt-5 · 2025-10-12

## 🧑 User

C'è un modo per convertire un infotainment MIB1 di Volkswagen in Apple CarPlay, diciamo, senza dover fare il retrofit dell'interrunta?

---

## 🤖 Assistant

No, **non esiste un modo diretto o software-based per abilitare Apple CarPlay su un sistema MIB1 Volkswagen**. Ti spiego nel dettaglio perché, e quali alternative reali hai:

---

### 🔧 Perché non si può “sbloccare” il MIB1
Il **MIB1 (Modular Infotainment Platform 1)** è la primissima generazione della piattaforma VW (circa 2013-2015).
- Non dispone dell’hardware necessario (chipset specifico per CarPlay / MirrorLink).
- Il firmware non prevede il modulo “App-Connect”.
- Non ha porte USB “data” compatibili (solo ricarica).
➡️ In sintesi: **manca sia il supporto software che fisico**.

---

### ✅ Soluzioni possibili

#### **1. Retrofit completo a MIB2 / MIB2.5**
È la **soluzione OEM più pulita e stabile**.
Serve sostituire:
- **Unità principale (head unit)** → MIB2 o MIB2.5 compatibile con App-Connect;
- **Schermo** (se il tuo è piccolo o con connettori diversi);
- **Modulo USB / porta dati** (per il collegamento CarPlay);
- E poi servono **codifica + attivazione App-Connect** (via VCDS, OBDeleven Pro o patch software tipo FeC).

💰 Costo medio:
- Usato completo con codifica: **400–700 €** (fai-da-te o retrofitter serio);
- In concessionaria: anche oltre **1000 €**.

---

#### **2. Interfaccia CarPlay aftermarket**
Alternative plug-and-play che si collegano dietro al display originale:
- Marchi noti: **Carlinkit OEM style, Andream, JoyeAuto, NavInc, Unique Auto Developments (UAD)**.
- Mantieni lo schermo originale, aggiungono un modulo che gestisce CarPlay via USB o Wi-Fi.
- Si controllano dai tasti originali e commutano automaticamente sulla sorgente CarPlay.

💰 Costo medio: **250–450 €**, installazione reversibile e meno invasiva.

⚠️ Verifica sempre che il tuo MIB1 sia compatibile con il *display LVDS input* richiesto: alcuni moduli supportano solo MIB2 e successivi.

---

#### **3. Sostituzione radio con unità Android compatibile CarPlay**
Opzione più “custom”:
- Sostituisci completamente l’unità con una Android (es. Dasaita, Joying, Xtrons).
- CarPlay integrato (wired o wireless), compatibilità CAN-bus, e molto più moderna.

💰 Costo medio: **300–600 €**.
⚠️ Estetica e qualità audio variano molto a seconda del modello.

---

### 🔍 In sintesi

| Soluzione | Pro | Contro | Costo indicativo |
|------------|-----|---------|------------------|
| Retrofit MIB2/MIB2.5 OEM | Qualità originale, integrazione perfetta | Costoso, serve codifica | 400–700 € |
| Interfaccia CarPlay aftermarket | Reversibile, conserva schermo | Compatibilità non sempre garantita | 250–450 € |
| Radio Android | Tutto integrato, funzioni moderne | Estetica non OEM | 300–600 € |

---

Se mi dici **modello preciso e anno della tua auto (es. Golf 7 2014, 1.4 TSI)** e il **codice del tuo MIB1** (puoi leggerlo da VCDS o dall’etichetta dell’unità), ti indico **quali moduli retrofit o interfacce aftermarket sono effettivamente compatibili**. Vuoi che lo faccia?

---

## 🧑 User

Ma quale sarebbe... Cioè, come faccio a controllarlo? Io ho un MIB1, Discover Media, per Golf 7.

---

## 🤖 Assistant

Perfetto. Se hai **Golf 7 con Discover Media MIB1**, sei nella fascia **2013–inizio 2015**, quindi il tuo sistema è quello **prima del MIB2**.
Vediamo come verificare con precisione il modello della tua unità:

---

### 🔍 **Metodo 1 – Dal menu nascosto del sistema**
1. Accendi il quadro.
2. Premi contemporaneamente i tasti **MENU + MEDIA + CAR** (oppure **MENU + SETUP + CAR**, a seconda del firmware).
3. Dopo qualche secondo si apre il **menu “test mode” o “software update”**.
4. Vai su **Version Information** o **Software version management**.
5. Troverai una sigla tipo:
- `MST1_EU_VW_P0xxxxD` → **MIB1**
- `MST2_EU_VW_P0xxxxD` → **MIB2**

👉 Se la sigla inizia con **MST1**, è confermato: **MIB1**.
Se invece è **MST2**, sei già sul MIB2 e allora si può attivare CarPlay via codice o patch.

---

### 🔧 **Metodo 2 – Da VCDS o OBDeleven**
1. Entra nel modulo **5F - Information Electr.**
2. Leggi il campo “Part Number”.
- Esempi tipici MIB1:
- `5G0 035 819 A`
- `5G0 035 819 B`
- `5G0 035 819 C`
- Esempi tipici MIB2:
- `3Q0 035 819 A`
- `3Q0 035 819 C`

💡 Se vedi un **“5G0”** all’inizio → MIB1.
Se vedi un **“3Q0”** → MIB2 o MIB2.5.

---

### 📦 **Differenze visive**
- MIB1 ha slot **SD1 + SD2** e **NO porta USB dati**.
- MIB2 ha spesso **SD1 + SD2 + USB (nel bracciolo o vano)** e talvolta logo “App-Connect” nei menu.

---

### ⚙️ Cosa comporta sapere questo
Se confermi che è davvero un **MIB1 (MST1 / 5G0...)**, allora:
- **Non puoi abilitare CarPlay via software.**
- Le uniche opzioni sono **retrofit MIB2** o **interfaccia aftermarket**.

Se invece risulta **MIB2 (MST2 / 3Q0...)**, allora sì — puoi attivare **App-Connect / CarPlay** con una **attivazione FEC** (codice software) o una **patch OBD** senza cambiare hardware.

---

Vuoi che ti indichi **quale modulo MIB2 usato è plug-and-play** sulla tua Golf 7 (e dove trovarlo compatibile)?
Mi serve solo:
- conferma del codice (o una foto dell’etichetta sotto “Version info”),
- e se hai **radio Discover Media o Pro**.

---

## 🧑 User

No, ma so di per certo che è un MIB1. Dico, come faccio a capire se il mio permette il collegamento di uno di questi dongle che mi permetterebbero di avere CarPlay sul MIB1?

---

## 🤖 Assistant

Ottimo — allora partiamo da un punto fermo:
👉 **Hai un Discover Media MIB1**, quindi CarPlay *nativo* è escluso.
Quello che vuoi capire è se **puoi aggiungere un modulo CarPlay esterno (dongle / box)** *senza cambiare unità principale*.
E la risposta è: **solo in alcuni casi**, dipende dal **display e dal tipo di collegamento LVDS**.

Ecco come verificare con precisione.

---

## ⚙️ Passaggi per capire se il tuo MIB1 accetta un modulo CarPlay aftermarket

### **1. Identifica il modello del display**
Il display è collegato all’unità MIB1 tramite un **cavo LVDS (video digitale)**.
Per installare un modulo CarPlay, devi sapere **che tipo di connettore LVDS hai**.

Puoi verificarlo in tre modi:
- **OBDeleven/VCDS:** leggi il modulo 5F e annota il *“Display part number”* (es. `5G0 919 605 A`).
- **Fisicamente:** se riesci a smontare la cornice del display, guarda il retro.
- Se vedi un connettore **LVDS rettangolare grande (rosso o blu)** → compatibile con la maggior parte delle interfacce CarPlay.
- Se vedi un connettore **tondo (HSD)** → alcune interfacce lo supportano, ma meno diffuso.

📍 *Esempio:* display `5G0 919 605 A` (Golf 7 MIB1) → LVDS rettangolare → **compatibile con moduli Andream / Joyeauto specifici per MIB1**.

---

### **2. Verifica che il modulo abbia ingresso video LVDS**
Il modulo CarPlay deve *intercettare* il segnale video proveniente dal MIB1 e *inserire* quello del CarPlay.
Per questo deve avere:
- **IN e OUT LVDS** (entrata dal MIB1, uscita verso lo schermo);
- **CAN bus harness** per comunicare con i comandi dell’auto (rotella, tasti, ecc.);
- **Switch automatico** tra sorgenti.

Se il tuo display è LVDS, puoi installare un modulo che faccia da *video switcher*.
Questi moduli si chiamano spesso **“CarPlay interface for VW MIB1 / PQ platform”**.

---

### **3. Controlla la compatibilità dichiarata**
Cerca nelle specifiche (su siti come Unique Auto Developments, JoyeAuto, Andream, Carlinkit OEM style):
> Compatible with VW Golf 7 (2013–2015) Discover Media MIB1 (5G0 035 819 A/B/C).

Se è esplicitamente indicato **“MIB1”** e non “MIB2 only”, è installabile.
Altrimenti non funzionerà, perché MIB2 e MIB1 hanno connessioni video diverse.

---

### **4. Verifica i comandi compatibili**
Nei MIB1, **non tutti i comandi al volante** e **non tutti i touch panel** sono riconosciuti dal modulo.
In genere funziona:
- controllo tramite **manopola / tasti fisici**,
- touch in alcuni modelli,
- audio via AUX (non digitale).

⚠️ Il suono passerà spesso via **ingresso AUX**, quindi devi avere o attivare quella sorgente.

---

### **5. Conclusione pratica**
Se il tuo MIB1 ha:
- display LVDS rettangolare (es. `5G0 919 605 A/B`),
- ingresso AUX attivo,
- Discover Media 5G0 035 819 A/B/C,

allora puoi installare **un modulo CarPlay compatibile MIB1**, come:
- **JoyeAuto MIB1 interface**
- **Andream VW MIB1 CarPlay box**
- **Unique Auto Developments VW MIB1 kit**

💰 Prezzo medio: 300–400 €.
💡 Installazione: si collega in cascata dietro il monitor, nessuna codifica.

---

Se vuoi, mandami il **codice del tuo display (5G0 919...)** — ti dico **esattamente** quale modulo aftermarket è compatibile e dove trovarlo (Amazon, AliExpress o rivenditori EU). Vuoi che lo faccia?