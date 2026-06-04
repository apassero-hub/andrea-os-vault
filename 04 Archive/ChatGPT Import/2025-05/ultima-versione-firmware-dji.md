---
title: "Ultima versione firmware DJI"
created: 2025-05-29
updated: 2025-05-29
model: gpt-4o
messages: 8
source: chatgpt-import
tags: []
---

# Ultima versione firmware DJI

> Importato da ChatGPT export · 8 messaggi · gpt-4o · 2025-05-29

## 🧑 User

Qual è l'ultima versione firmware del DJI Smart Controller?

---

## 🤖 Assistant

L'ultima versione del firmware disponibile per il DJI Smart Controller (modello RM500) è la **v01.01.0076**, rilasciata l'11 aprile 2024. cite

### Novità principali della versione v01.01.0076

- Correzione di alcuni bug.

Questa versione mantiene la compatibilità con le app DJI GO 4 (v4.3.54), DJI Pilot (v2.3.1.5) e DJI Fly (v1.4.2). cite

### Come aggiornare il firmware

Puoi aggiornare il tuo Smart Controller in due modi:

#### 1. Aggiornamento via Wi-Fi (direttamente dal controller)

1. Accendi il controller e connettilo a una rete Wi-Fi.
2. Vai su **Impostazioni di sistema** > **Aggiornamento sistema**.
3. Tocca **Verifica aggiornamenti** e segui le istruzioni a schermo.
4. Il controller si riavvierà automaticamente al termine dell'aggiornamento.

#### 2. Aggiornamento tramite DJI Assistant 2 (per PC)

1. Scarica e installa **DJI Assistant 2 for Mavic** (versione v2.0.14) dal sito ufficiale DJI.
2. Collega il controller al PC tramite cavo USB-C e accendilo.
3. Avvia DJI Assistant 2, effettua il login con il tuo account DJI.
4. Seleziona il dispositivo e clicca su **Aggiornamento firmware**.
5. Scegli la versione v01.01.0076 e clicca su **Aggiorna**.
6. Al termine, il controller si riavvierà automaticamente. cite

> **Nota**: Se il tuo controller ha una versione firmware precedente alla v01.00.04.75, l'aggiornamento può essere effettuato solo tramite DJI Assistant 2. cite

### Considerazioni finali

Sebbene il DJI Smart Controller RM500 sia un dispositivo robusto, alcuni utenti hanno segnalato che, a causa dell'hardware datato e del sistema operativo Android 7.1.2, potrebbe non supportare al meglio le app più recenti o offrire un'esperienza fluida con droni di nuova generazione. cite Se stai valutando l'acquisto di un nuovo drone o desideri funzionalità più avanzate, potresti considerare controller più recenti come il DJI RC Pro.

Se hai bisogno di assistenza nell'aggiornamento o desideri ulteriori informazioni sui controller compatibili con i droni DJI più recenti, non esitare a chiedere!

---

## 🧑 User

perchè dji assistant non vede lo smart controller?

---

## 🤖 Assistant

Se DJI Assistant 2 **non rileva il tuo Smart Controller**, le cause possono essere diverse. Ecco un elenco dei motivi più comuni e come risolverli:

---

### ✅ **1. Versione corretta di DJI Assistant 2**
Ci sono **più versioni di DJI Assistant 2** per prodotti diversi:

- Per il **DJI Smart Controller** (RM500), serve **DJI Assistant 2 (For Mavic)**.
- Scaricala da qui (versione compatibile):
👉 [DJI Assistant 2 for Mavic – Download](https://www.dji.com/it/downloads/softwares/dji-assistant-2-for-mavic)

**❗Errore comune:** installare la versione "For Enterprise" o "For Phantom", che **non è compatibile**.

---

### ✅ **2. Driver USB corretti e controller acceso**
- Assicurati che il controller sia **acceso**.
- Usa un **cavo USB-C funzionante**, preferibilmente quello originale DJI.
- Prova a **cambiare porta USB** del computer.
- Su Windows, assicurati che i driver siano stati installati correttamente (dovrebbe apparire il dispositivo nei dispositivi collegati).

---

### ✅ **3. Modalità Debug USB (Android)**
Il controller funziona su Android 7.1.2 e in alcuni casi ha bisogno del **Debug USB attivo**:

1. Vai su **Impostazioni** del controller.
2. Tocca **Info sul dispositivo**.
3. Tocca ripetutamente su **Numero build** finché non attivi le **Opzioni sviluppatore**.
4. Vai su **Opzioni sviluppatore** > **Debug USB** → **attivalo**.
5. Ricollega il controller al computer.

---

### ✅ **4. Software DJI Assistant aggiornato**
Usa l’ultima versione. Se hai già Assistant installato ma è vecchio, disinstallalo completamente e reinstalla da zero.

---

### ✅ **5. Firewall o antivirus**
A volte un **antivirus o firewall blocca DJI Assistant**. Prova a:
- Disattivare temporaneamente l'antivirus.
- Avviare DJI Assistant come **amministratore** (tasto destro > "Esegui come amministratore").

---

### ✅ **6. Il controller è troppo vecchio o corrotto**
Se il firmware del controller è **molto datato** o corrotto, il collegamento può fallire. In questo caso puoi:
- Provare su **un altro computer** (Windows consigliato).
- Provare via **Wi-Fi**, aggiornando direttamente dal controller se il sistema si avvia correttamente.

---

### ❓**Ancora problemi?**
Fammi sapere:
- Che sistema operativo usi (Windows/macOS)?
- Il tuo controller è il **modello Smart Controller RM500**, giusto?
- Hai già provato a collegarlo a un altro PC o con un altro cavo?

Posso aiutarti a isolare meglio il problema con queste info.

---

## 🧑 User

come dev'essere messo? modalità trasferimento dati?

---

## 🤖 Assistant

Sì, esatto: **quando colleghi il DJI Smart Controller al computer tramite USB**, deve essere impostato in **modalità di trasferimento dati (MTP)** per essere correttamente rilevato da **DJI Assistant 2 (for Mavic)**.

Ecco cosa fare passo passo:

---

### ✅ **1. Collega il controller acceso al computer tramite cavo USB-C.**

- Usa preferibilmente il **cavo originale** o uno USB-C di buona qualità **solo dati**, non solo ricarica.

---

### ✅ **2. Sul controller apparirà una notifica “USB in carica”, o simile.**
- Trascina il menu dall’alto (come su uno smartphone Android).
- Tocca la notifica con scritto qualcosa come:
> "Questo dispositivo si sta caricando tramite USB"

---

### ✅ **3. Cambia la modalità USB**
- Tocca l’opzione e seleziona:
> **“Trasferimento di file (MTP)”** oppure **“Trasferimento dati”**

Questo è fondamentale: **se resta in modalità solo ricarica**, il PC non vedrà correttamente il dispositivo e DJI Assistant 2 non riuscirà a rilevarlo.

---

### ✅ **4. Ora apri DJI Assistant 2 (for Mavic)**
- Assicurati che il programma sia **chiuso prima di collegare** il controller, e poi **avvialo solo dopo** aver impostato la modalità corretta.
- Dovrebbe ora comparire il controller nella schermata iniziale.

---

### Se **non compare nulla**:
- Prova a **cambiare cavo o porta USB**.
- Controlla che sia attivo il **Debug USB** nelle Opzioni sviluppatore (vedi messaggio precedente).
- Su Windows: apri **Gestione dispositivi** per vedere se il controller è almeno rilevato dal sistema operativo.

Fammi sapere se ti serve una guida con schermate passo passo!

---

## 🧑 User

non può essere aggiornato diversamente?

---

## 🤖 Assistant

iSì, è possibile aggiornare il firmware del DJI Smart Controller anche **senza utilizzare DJI Assistant 2**, sfruttando la **connessione Wi-Fi integrata** del controller.

---

### 🔄 Metodo Alternativo: Aggiornamento via Wi-Fi

Questo metodo è particolarmente utile se DJI Assistant 2 non riconosce il controller o se preferisci un aggiornamento diretto senza passare per il computer.

#### ✅ Requisiti:

- Il controller deve essere acceso.
- Deve essere connesso a una rete Wi-Fi stabile.
- La batteria del controller dovrebbe essere **carica almeno al 50%**.

#### 📲 Procedura:

1. Accendi il DJI Smart Controller.
2. Dal menu principale, vai su **Impostazioni**.
3. Scorri fino in fondo e seleziona **Aggiornamento sistema**.
4. Tocca **Verifica aggiornamenti**.
5. Se è disponibile un nuovo firmware, segui le istruzioni a schermo per scaricarlo e installarlo.
6. Al termine dell'aggiornamento, il controller si riavvierà automaticamente.

Questo metodo è ufficialmente supportato da DJI e descritto nel manuale utente del controller. cite

---

### ⚠️ Nota Importante

Se il tuo controller ha una versione firmware **precedente alla v01.00.04.75**, l'aggiornamento può essere effettuato **solo tramite DJI Assistant 2**. cite

---

### 💡 Consigli Utili

- Assicurati che la connessione Wi-Fi sia stabile durante l'aggiornamento.
- Evita di spegnere il controller o interrompere la connessione durante il processo.
- Se l'aggiornamento via Wi-Fi fallisce ripetutamente, considera l'uso di DJI Assistant 2 come alternativa.

---

Se hai bisogno di ulteriori dettagli o assistenza durante l'aggiornamento, non esitare a chiedere!