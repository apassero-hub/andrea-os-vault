---
title: "Disinstallare DJI Assistant 2"
created: 2025-06-01
updated: 2025-06-01
model: gpt-4o
messages: 4
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Disinstallare DJI Assistant 2

> Importato da ChatGPT export · 4 messaggi · gpt-4o · 2025-06-01

## 🧑 User

come elimino dji assistant 2 dal mac?

---

## 🤖 Assistant

Per disinstallare completamente DJI Assistant 2 dal tuo Mac, segui attentamente i passaggi indicati di seguito. Questa procedura rimuoverà sia l'applicazione principale sia eventuali driver associati, come HoRNDIS, che potrebbero interferire con il corretto funzionamento del sistema.

---

### 🔧 Procedura di disinstallazione completa di DJI Assistant 2 su macOS

#### 1. Rimozione dell'applicazione DJI Assistant 2

1. Apri il **Finder**.
2. Vai alla cartella **Applicazioni**.
3. Individua l'applicazione denominata **Assistant** (nota: potrebbe non essere etichettata come "DJI Assistant 2").
4. Trascina l'applicazione nel **Cestino**.
5. Svuota il **Cestino** per completare la rimozione.

#### 2. Eliminazione dei file di supporto e delle preferenze

Per assicurarti che non rimangano file residui, elimina le seguenti cartelle e file:

- `~/Library/Application Support/DJI`
- `~/Library/Preferences/com.dji.assistant.plist`
- `~/Library/Caches/com.dji.assistant`
- `/Library/Extensions/HoRNDIS.kext` (se presente)

**Nota:** Per accedere alla cartella `~/Library`, nel Finder seleziona il menu **Vai** e poi **Vai alla cartella...**, quindi inserisci `~/Library` e premi Invio.

#### 3. Rimozione del driver HoRNDIS (se installato)

Il driver HoRNDIS è spesso installato insieme a DJI Assistant 2 per facilitare la comunicazione USB. Tuttavia, può causare conflitti o problemi di compatibilità.

1. Apri il **Terminale** (lo trovi in **Applicazioni > Utility**).
2. Esegui il seguente comando per rimuovere il driver:

```bash
sudo rm -rf /Library/Extensions/HoRNDIS.kext
```


3. Inserisci la password dell'amministratore quando richiesto.
4. Riavvia il Mac per completare la rimozione del driver.

#### 4. Verifica delle estensioni del kernel disabilitate (opzionale)

Per controllare se ci sono estensioni del kernel disabilitate che potrebbero interferire:

1. Apri il **Terminale**.
2. Esegui il comando:

```bash
kmutil showloaded | grep -i horndis
```


Se non viene restituito alcun risultato, significa che il driver HoRNDIS non è attualmente caricato.

---

### ⚠️ Considerazioni finali

- Se hai installato una versione specifica di DJI Assistant 2 (ad esempio, per droni FPV o Enterprise), assicurati di rimuovere anche eventuali componenti aggiuntivi associati.
- Alcuni utenti hanno segnalato problemi di compatibilità tra DJI Assistant 2 e le versioni più recenti di macOS, come Ventura o Sonoma. In tali casi, potrebbe essere necessario utilizzare un PC Windows per eseguire aggiornamenti firmware o altre operazioni. cite

Se necessiti di ulteriori informazioni o assistenza per reinstallare una versione compatibile di DJI Assistant 2, non esitare a chiedere.

---

## 🧑 User

non posso eliminare le cartelle del punto 2 da terminale?

---

## 🤖 Assistant

Sì, puoi eliminare tutte le cartelle e i file residui di **DJI Assistant 2** direttamente da **Terminale**, in modo rapido e completo. Di seguito ti fornisco i comandi da eseguire, tutti in modalità amministratore con `sudo` dove necessario.

---

### 🧹 **Comandi per eliminare DJI Assistant 2 via Terminale**

Apri Terminale e incolla uno alla volta i seguenti comandi (premi Invio dopo ciascuno):

```bash
# Elimina la cartella di supporto dell'app
rm -rf ~/Library/Application\ Support/DJI

# Elimina il file delle preferenze
rm -f ~/Library/Preferences/com.dji.assistant.plist

# Elimina la cache dell'app
rm -rf ~/Library/Caches/com.dji.assistant
```

Se hai installato **HoRNDIS** (driver USB di rete spesso incluso con DJI Assistant), elimina anche:

```bash
# Rimozione del driver HoRNDIS
sudo rm -rf /Library/Extensions/HoRNDIS.kext
```

Infine, **riavvia il Mac** per completare la rimozione delle estensioni del kernel.

---

### ✅ Consiglio

Se vuoi essere certo di non lasciare tracce, puoi anche cercare eventuali file residui con questo comando:

```bash
sudo find / -iname "*dji*" 2>/dev/null
```

Questo ti mostrerà tutti i file e cartelle che contengono "dji" nel nome. Elimina solo quelli chiaramente associati all’app DJI Assistant (evita quelli legati ad altri software DJI che potresti voler mantenere).

---

Fammi sapere se vuoi che ti prepari uno script automatico da incollare tutto in una volta.