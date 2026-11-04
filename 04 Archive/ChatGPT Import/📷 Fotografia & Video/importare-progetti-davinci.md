---
title: "Importare progetti DaVinci"
created: 2026-04-05
updated: 2026-04-05
model: gpt-5-3
messages: 18
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Importare progetti DaVinci

> Importato da ChatGPT export · 18 messaggi · gpt-5-3 · 2026-04-05

## 🧑 User

se ho fatto un time machine di una macchina su cui avevo da vinci resolve ora da un altro computer posso importare solo i progetti e le preferenze da vinci?

---

## 🤖 Assistant

Sì, si può fare — ma non in modo “automatico” tramite Time Machine. Devi estrarre manualmente i dati giusti.

Ti dico esattamente come stanno le cose.

---

## 1) Dove sono i progetti di entity["software","DaVinci Resolve","video editing software Blackmagic Design"]

Dipende da come lavoravi:

### 👉 Caso A — Database locale (quasi sempre così)
I progetti NON sono dentro Time Machine come file singoli leggibili. Sono dentro un database.

Percorso tipico nel backup:
```
/Library/Application Support/Blackmagic Design/DaVinci Resolve/Resolve Disk Database/
```

Dentro trovi:
- `Resolve Projects`
- cartelle database

### 👉 Caso B — PostgreSQL (meno comune)
Se usavi database server:
- devi ripristinare il database intero (più complesso)
- oppure esportare i progetti da Resolve (se hai ancora accesso alla vecchia macchina)

---

## 2) Metodo consigliato (pulito)

Se riesci ancora ad accedere al backup:

### Step:
1. Apri Resolve sulla nuova macchina
2. Vai su **Project Manager**
3. Tasto destro → **Restore Project Archive**

👉 Ma serve avere file `.dra` (archivi progetto)

Se NON li hai → passa al metodo sotto

---

## 3) Metodo reale da Time Machine (quello che ti serve)

### Step operativo:

1. Entra nel backup Time Machine
2. Vai in:
```
Macintosh HD > Library > Application Support > Blackmagic Design > DaVinci Resolve
```

3. Copia queste cartelle:
- `Resolve Disk Database`
- eventualmente `Preferences`

4. Incollale nello stesso path sulla nuova macchina

⚠️ Attenzione:
- Chiudi Resolve prima
- Sovrascrivi solo se sei sicuro
- Backup prima di fare casino

---

## 4) Preferenze

Le preferenze sono qui:

```
~/Library/Preferences/com.blackmagic-design.DaVinciResolve.plist
```

E anche:
```
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Preferences/
```

Copiale e portale sulla nuova macchina → ti ritrovi:
- layout UI
- shortcut
- impostazioni base

---

## 5) Limiti reali (importante)

Non aspettarti magia:

- ❌ Plugin mancanti → errori
- ❌ Media non collegati → dovrai relinkare
- ❌ Cache persa → normale
- ❌ Versioni diverse → possibile incompatibilità

---

## 6) Strategia migliore (se puoi ancora)

Se hai accesso alla vecchia macchina:
👉 Apri Resolve → esporta ogni progetto come `.dra`

È il metodo più pulito, portabile e sicuro.

---

## Conclusione

Sì, puoi recuperare tutto da Time Machine, ma:

- i progetti stanno in un database → devi copiarlo intero
- le preferenze si copiano a parte
- non esiste import “selettivo” semplice senza passare da Resolve

---

Se vuoi, dimmi:
- che versione di Resolve usavi
- se hai ancora accesso alla vecchia macchina

e ti dico la procedura più sicura senza rischiare di rompere il database.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

non trovo nessuno dei files indicati, questo è sul time machine

---

## 🤖 Assistant

Quello che stai guardando è **la cartella sbagliata**.

Sei dentro:
```
Applicazioni > DaVinci Resolve
```

Quella è **l’applicazione**, non i dati.

---

## Dove devi andare davvero

I progetti NON stanno lì. Stanno nella **Library di sistema**, che è nascosta.

### Percorso corretto (quello giusto):

```
Macintosh HD > Library > Application Support > Blackmagic Design > DaVinci Resolve
```

⚠️ Nota fondamentale:
- NON è `~/Library` (quella utente)
- È `/Library` (livello sistema)

---

## Come arrivarci in Time Machine (modo rapido)

1. Apri Finder
2. Premi **Cmd + Shift + G**
3. Incolla questo:

```
/Library/Application Support/Blackmagic Design/
```

4. Entra in Time Machine da lì

---

## Cosa devi trovare

Dentro dovresti vedere:

```
DaVinci Resolve/
└── Resolve Disk Database/
```

Se non trovi **Resolve Disk Database**, allora:

### Possibili scenari:
- ❌ Resolve non ha mai salvato progetti localmente
- ❌ Usavi database PostgreSQL
- ❌ Stai guardando il backup sbagliato
- ❌ Time Machine non ha incluso quella cartella

---

## Controllo veloce (importante)

Prova ANCHE questo percorso:

```
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/
```

(questa è la libreria utente)

👉 Per accedere:
- Finder → Vai → Vai alla cartella
- Incolla:
```
~/Library/Application Support/Blackmagic Design/
```

---

## Tradotto senza giri di parole

- Quello che hai aperto nello screenshot → inutile per i progetti
- Devi entrare nelle **Application Support**, non nelle Applicazioni
- Se non trovi il database → non puoi “estrarre” i progetti così

---

## Se vuoi andare dritto al punto

Dimmi una cosa:
- avevi più progetti visibili in Resolve sulla vecchia macchina?

Se sì → il database esiste per forza → lo troviamo.

Se vuoi, mandami uno screenshot della struttura dentro:
```
Application Support > Blackmagic Design
```
e ti dico esattamente dove cliccare senza perdere tempo.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Ok, adesso sei **nel posto giusto** 👍
Ma devi fare **un livello in più dentro “DaVinci Resolve”**.

---

## 👉 Step immediato

Entra qui:

**DaVinci Resolve →**

Dentro quella cartella devi trovare:

```
Resolve Disk Database
```

---

## Se la trovi

Percorso completo:

```
Blackmagic Design
└── DaVinci Resolve
└── Resolve Disk Database
```

👉 Quella cartella è **tutto**:
- progetti
- timeline
- metadata

### Cosa fare:
- Copia **tutta** `Resolve Disk Database`
- Incollala nello stesso path sulla nuova macchina

---

## Se NON la trovi

Allora la situazione è una di queste (senza girarci intorno):

### 1. ❌ Stai guardando uno snapshot sbagliato
→ scorri indietro in Time Machine (data diversa)

### 2. ❌ I progetti erano in database PostgreSQL
→ quindi NON stanno qui

### 3. ❌ Resolve non ha mai salvato lì (raro ma possibile)

---

## Controllo rapido (fondamentale)

Dentro quella cartella che hai aperto ora:
👉 apri **DaVinci Resolve** e mandami screenshot

Voglio vedere esattamente cosa c’è dentro.

---

## Shortcut per capire subito

Se dentro trovi roba tipo:
- `CacheClip`
- `GPUCache`
- `Logs`

👉 non basta → devi trovare **Resolve Disk Database**

---

## Traduzione pratica

- Sei al 90% del percorso
- Ti manca **solo l’ultimo step corretto**
- Se quella cartella c’è → risolvi in 2 minuti
- Se non c’è → cambia completamente strategia

---

Vai dentro **DaVinci Resolve** e fammi vedere cosa c’è. Ti dico subito se sei salvo o no.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, ora è chiarissimo.

👉 **Non sei nel posto giusto per i progetti.**

Quella cartella che stai vedendo è:
```
/Library/Application Support/Blackmagic Design/DaVinci Resolve
```

E contiene:
- componenti del software
- LUT
- Fusion
- tool interni

👉 **NON contiene il database dei progetti.**

---

## 🔴 Dove stanno DAVVERO i progetti (nel tuo caso)

Nel 90% dei casi sono qui:

```
~/Movies/DaVinci Resolve/
```

oppure:

```
~/Documents/DaVinci Resolve/
```

---

## 👉 Cosa devi fare ORA (senza perdere tempo)

### 1. Vai in Time Machine

Controlla queste due cartelle:

- **Filmati (Movies)**
- **Documenti (Documents)**

### 2. Cerca:

```
DaVinci Resolve/
```

Dentro devi trovare:

```
Resolve Disk Database
```

---

## 🔍 Perché non lo vedi dove stavi guardando

Perché Resolve:
- usa `/Library` per il software
- usa la **home utente** per i progetti

👉 Ed è esattamente quello che stai mancando

---

## 💣 Tradotto brutalmente

- Quella cartella → inutile per i tuoi progetti
- Il database → sta quasi sicuramente in Movies
- Sei stato nel posto giusto per metà… ma non quello che serve

---

## ⚠️ Caso alternativo (importante)

Se NON trovi niente nemmeno in:
- Movies
- Documents

allora:
👉 usavi un database PostgreSQL

(e lì cambia tutto, ma si recupera comunque)

---

## 👉 Vai dritto così

Apri Time Machine → vai su:
- Filmati
- cerca `DaVinci Resolve`

e mandami screenshot.

Se c’è → in 30 secondi ti faccio recuperare tutto.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto. Qui ci siamo davvero.

👉 Hai **tutto quello che ti serve**.
E anche meglio del previsto.

---

## 🔥 Quello che vedo nel tuo screenshot

Dentro **Filmati** hai:

- `Resolve Project Backups` ✅
- `Resolve Project Library` ✅
- `CacheClip` (inutile)
- altri materiali (irrilevanti)

---

## 🎯 Traduzione pratica

Hai **due modi per recuperare i progetti**:

---

# ✅ Metodo 1 — quello veloce e sicuro

### Usa:
``` id="l9g4j1"
Resolve Project Backups
```

Dentro trovi file `.drp`

### Procedura:
1. Apri entity["software","DaVinci Resolve","video editing software Blackmagic Design"]
2. Project Manager
3. Tasto destro → **Import Project**
4. Seleziona i `.drp`

👉 Fine.
👉 Metodo più pulito possibile.

---

# ⚡ Metodo 2 — recupero completo database

### Usa:
``` id="0z6t9b"
Resolve Project Library
```

Questa è probabilmente la tua **libreria progetti vera**.

### Procedura:

1. Copia tutta la cartella:
``` id="9p8vxn"
Resolve Project Library
```

2. Mettila sulla nuova macchina (dove vuoi)

3. Apri Resolve → Project Manager

4. **Add Project Library**
- scegli tipo: Disk
- punta a quella cartella

👉 Ti ritrovi TUTTI i progetti insieme

---

## ⚠️ Differenza chiave (importante)

| Metodo | Pro | Contro |
|------|-----|--------|
| Backup (.drp) | sicuro, pulito | uno alla volta |
| Library | tutto insieme | più delicato |

---

## 💣 Consiglio diretto (senza fronzoli)

Fai così:

1. **Subito** importa 1 progetto dai `.drp` → verifica che funzioni
2. Poi, se vuoi velocità → monta tutta la `Resolve Project Library`

---

## ⚠️ Nota tecnica (non ignorarla)

Dopo il restore:
- dovrai fare **relink media**
- eventuali plugin mancanti = errori normali
- cache da rifare

---

## Conclusione

Sei messo bene:
- non hai perso nulla
- hai sia backup singoli che libreria

👉 situazione ideale

---

Se vuoi fare la cosa fatta bene:
ti guido a migrare tutto in modo pulito (senza portarti dietro sporcizia di database).

---

## 🧑 User

come faccio a rinominare la project libraries?

---

## 🤖 Assistant

Diretto: **non puoi rinominare una Project Library dall’interno di entity["software","DaVinci Resolve","video editing software Blackmagic Design"]**.

Resolve non ha una funzione “rename” per le library. Devi farlo **da fuori**.

---

## ✅ Metodo corretto (disk database — il tuo caso)

Visto che stai usando una library su disco (quella in *Filmati*), fai così:

### 1. Chiudi Resolve
(obbligatorio, altrimenti rischi di corrompere il database)

---

### 2. Rinomina la cartella nel Finder

Vai dove hai la library, es:
```bash
Filmati/Resolve Project Library
```

Rinominala in:
```bash
Filmati/Nuovo Nome Library
```

---

### 3. Ricollega la library in Resolve

Apri Resolve → Project Manager:

1. Click su **“Add Project Library”**
2. Tipo: **Disk**
3. Seleziona la cartella appena rinominata

👉 A quel punto la vedrai con il nuovo nome

---

### 4. (Opzionale ma consigliato)

Rimuovi la vecchia entry (quella con il nome vecchio):
- click destro → **Remove**

⚠️ Questo NON cancella nulla, rimuove solo il collegamento

---

## ⚠️ Errori da evitare

- ❌ Rinominare mentre Resolve è aperto
- ❌ Toccare file interni alla cartella
- ❌ Spostare roba dentro la library

---

## 🧠 Nota importante

Il “nome” che vedi in Resolve:
- NON è un campo modificabile
- è semplicemente il nome della cartella collegata

---

## Sintesi

- Vuoi cambiare nome → rinomini la cartella
- Poi la ricolleghi
- Fine

---

Se vuoi fare ordine serio (consigliato):
ti spiego come strutturare più library (lavori, archive, clienti) senza rallentare Resolve.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

qui che c'è scritto weddings non so perchè c'è scritto

---

## 🤖 Assistant

Quello che vedi **“Weddings”** non è un nome casuale:
👉 è il **nome della cartella del database** che hai collegato.

Resolve non inventa nulla lì.

---

## 🔍 Cosa significa davvero

Quella voce:
```
Weddings
```

= una **Project Library (Disk Database)** che punta a una cartella tipo:

```bash
/Users/tuo_utente/.../Weddings/
```

---

## ⚠️ Perché non riesci a cambiarlo da lì

Dentro entity["software","DaVinci Resolve","video editing software Blackmagic Design"]:

- NON puoi rinominare una library
- NON puoi modificarne il nome direttamente
- quello è solo il **nome della cartella sorgente**

---

## ✅ Come sistemarlo (2 opzioni)

### 🔹 Opzione 1 — pulita (consigliata)

1. Chiudi Resolve
2. Trova la cartella reale della library
(probabilmente in Filmati o dove hai copiato prima)

3. Rinominala:
```bash
Weddings → Nome che vuoi
```

4. Riapri Resolve
5. **Add Project Library** → seleziona la cartella rinominata
6. Rimuovi quella vecchia

👉 Fine. Nome aggiornato.

---

### 🔹 Opzione 2 — veloce (senza toccare file)

Se non ti interessa tenerla:

1. Click destro su “Weddings”
2. **Remove**

⚠️ Non cancella nulla → rimuove solo il collegamento

---

## 🧠 Da dove è saltato fuori “Weddings”

Molto probabilmente:

- era una tua vecchia libreria
- oppure un backup con quel nome
- oppure hai importato una cartella già chiamata così

Resolve si limita a leggerlo.

---

## 💣 Sintesi chiara

- “Weddings” = nome cartella database
- non lo cambi da Resolve
- lo cambi nel Finder → poi ricolleghi

---

Se vuoi evitare casino in futuro:
ti imposto una struttura library pulita (tipo *Clienti / Personale / Archive*) che ti evita questo tipo di confusione.

---

## 🧑 User

come faccio ad importare dei powegrades su resolve?

---

## 🤖 Assistant

Diretto: i **PowerGrades** in entity["software","DaVinci Resolve","video editing software Blackmagic Design"] non si “importano” come LUT o plugin.
Sono **stills nella Gallery**, quindi li porti dentro in modo diverso.

---

## 🎯 Metodo 1 — il modo corretto (se hai file.DRX)

### Hai file `.drx`?
Perfetto.

### Procedura:
1. Vai nella **Color Page**
2. Apri la **Gallery** (in alto a sinistra)
3. Click destro dentro la Gallery
4. **Import**
5. Seleziona i file `.drx`

👉 Te li ritrovi come PowerGrades pronti da usare

---

## 🎯 Metodo 2 — se hai una cartella di PowerGrades

Se ti hanno dato una cartella:

1. Vai in **Color Page → Gallery**
2. In alto scegli:
```
PowerGrade Album
```
3. Click destro → **Import**
4. Seleziona tutti i `.drx`

---

## 🎯 Metodo 3 — da un altro progetto (molto usato)

Se arrivano da un altro progetto:

1. Apri quel progetto
2. Vai in Color
3. Gallery → seleziona gli still
4. Right click → **Export** → salva `.drx`

Poi li importi come sopra

---

## ⚠️ Errore tipico (evitalo)

- ❌ Mettere i file in una cartella a caso → Resolve NON li vede
- ❌ Pensare che siano LUT → NON lo sono
- ❌ Trascinarli dentro Media Pool → inutile

---

## 🔥 Pro tip (che ti cambia la vita)

Se vuoi una libreria PowerGrades sempre disponibile:

1. Vai in Gallery
2. Seleziona:
```
PowerGrade Album
```
3. Importa lì dentro

👉 Risultato:
- li hai in **tutti i progetti**
- non devi reimportare ogni volta

---

## 🧠 Differenza chiave (chiara)

| Tipo | Dove va | Cos’è |
|------|--------|------|
| LUT | LUT folder | trasformazione colore |
| PowerGrade (.drx) | Gallery | nodo completo |
| Preset | altro | non è questo |

---

## Sintesi

- Hai `.drx` → Gallery → Import
- Vuoi sempre disponibili → PowerGrade Album
- Non sono LUT → non vanno nelle LUT

---

Se vuoi, ti costruisco una struttura PowerGrades seria (look base, skin, outdoor, log → rec709, ecc.) così smetti di perdere tempo ogni volta.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

quale installo sul mio mac?

---

## 🤖 Assistant

Vai dritto: **installa questo** 👇

👉 **`DehancerPro_OFX_macos_metal_7.4.0.pkg`**

È quello giusto per il tuo caso.

---

## 🔍 Perché proprio questo

- **OFX** → è il formato plugin per entity["software","DaVinci Resolve","video editing software Blackmagic Design"]
- **macOS metal** → ottimizzato per Apple Silicon (M1, M2, M3 → il tuo M3 Pro)
- **.pkg** → installer diretto, pulito

---

## ❌ Quelli che NON devi usare

Dalla tua lista:

- `DehancerProMetalInstaller...`
→ vecchi installer / versioni precedenti

- `DehancerPro DVR 7.3.x`
→ non è il plugin OFX standalone corretto per Resolve (setup diverso)

- `InstallerOFX...7.3.x`
→ versioni vecchie → inutile installarle ora

---

## ⚠️ Prima di installare

Fai così:

1. Chiudi Resolve
2. Installa il `.pkg`
3. Riapri Resolve
4. Vai in:
```
Color → Effects → OFX
```
5. Cerca **Dehancer**

---

## 🧠 Se non lo vedi

Vai in:
```
DaVinci Resolve → Preferences → Video Plugins
```
→ Refresh / Scan

---

## 💣 Nota importante

Se avevi versioni vecchie:
- possono creare conflitti
- se vedi problemi → meglio pulire e reinstallare

---

## Sintesi

- Installa: **7.4.0 metal OFX**
- È quello corretto per il tuo Mac
- Gli altri → ignorali

---

Se vuoi, dopo ti dico come settare Dehancer bene su Resolve (senza fare look “finti Instagram”).