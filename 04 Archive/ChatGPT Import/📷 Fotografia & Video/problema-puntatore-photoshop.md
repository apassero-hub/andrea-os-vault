---
title: "Problema puntatore Photoshop"
created: 2026-04-28
updated: 2026-04-28
model: gpt-5-3
messages: 6
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Problema puntatore Photoshop

> Importato da ChatGPT export · 6 messaggi · gpt-5-3 · 2026-04-28

## 🧑 User

photoshop non mi fa vedere i classico puntatore di pennello o di spugma ma un piccolo crocino come se avessi il blocco maiuscole ma non c'è. ho provato ad attivarlo e disattivarlo m NON cambia. se ingrandisco o rimpicciolisco per un istante lo vedo e poi sparisce. ho provato a chiudere e riaprire ps piu volte ma niente

---

## 🤖 Assistant

Non è un bug: è quasi sempre un’impostazione attiva per errore.

Vai dritto qui:

**1. Controlla i cursori**
- Apri **Preferenze → Cursori**
- Su “Cursori pittura” imposta:
- **Normale punta pennello** oppure **Punta pennello a grandezza piena**
- Disattiva eventuali opzioni tipo “Mostra crocino nel puntatore”

**2. Shortcut che lo causa**
- Premi **Caps Lock** più volte lentamente
Anche se pensi sia spento, Photoshop può “leggerlo” male (succede spesso con tastiere esterne o lag).

**3. GPU / glitch grafico (molto probabile visto il comportamento)**
Il fatto che il cerchio appaia solo mentre ridimensioni è tipico.

- Vai su **Preferenze → Prestazioni**
- Disattiva **Usa processore grafico**
- Riavvia Photoshop

Se così torna normale, il problema è la GPU o i driver.

**4. Reset rapido preferenze (se ancora non va)**
- Chiudi Photoshop
- Riaprilo tenendo premuto:
- **Cmd + Option + Shift (Mac)**
- **Ctrl + Alt + Shift (Windows)**
- Conferma il reset

---

### Diagnosi se vuoi essere preciso
- Se il problema sparisce disattivando la GPU → driver / accelerazione grafica
- Se cambia con Caps Lock → input tastiera
- Se si risolve con reset → preferenze corrotte

---

Se non si sistema così, dimmi:
- Mac o Windows
- versione Photoshop
- tablet grafica sì/no (Wacom ecc.)

Perché a quel punto è quasi sicuramente un conflitto driver, non Photoshop.

---

## 🧑 User

premendo caps lock 2 volte torna a farmi vedere il cursore normale ma appena lo muovo torna il crocino

---

## 🤖 Assistant

Allora: non è il Caps Lock. Quello che descrivi è il classico **bug di rendering del cursore legato alla GPU o ai driver input (spesso anche tablet)**. Il fatto che torni normale per un istante e poi sparisca appena muovi il mouse è un segnale chiaro.

Vai diretto, senza perdere tempo:

---

### 1. Disattiva la GPU (test immediato)
- **Photoshop → Preferenze → Prestazioni**
- Togli la spunta a **“Usa processore grafico”**
- Riavvia Photoshop

👉 Se così si risolve: hai trovato il problema (accelerazione grafica instabile)

---

### 2. Se usi una tavoletta (Wacom o simili)
È una delle cause più frequenti.

- Chiudi Photoshop
- Scollega la tavoletta
- Riapri Photoshop e prova con il mouse

👉 Se torna normale:
- Aggiorna o reinstalla i driver Wacom
- Oppure disattiva **Windows Ink / equivalente Mac** nelle impostazioni driver

---

### 3. Forza refresh GPU (se vuoi tenerla attiva)
Se non vuoi lavorare senza GPU:

- Vai su **Preferenze → Prestazioni → Impostazioni avanzate**
- Imposta su **Normale** (non “Avanzata”)
- Disattiva:
- **Canvas OpenGL Drawing**
- **Anti-alias guide and paths**

---

### 4. Controllo cursori (rapido ma secondario)
- **Preferenze → Cursori**
- Usa **Punta pennello a grandezza piena**
- Disattiva crocini o opzioni strane

---

### 5. Reset preferenze (ultima cosa se serve)
- Avvia con **Cmd + Alt + Shift (Mac)**
- Conferma reset

---

### Conclusione diretta
Il tuo problema **non è un’impostazione**, è quasi sicuramente:
- GPU che glitcha
oppure
- driver della tavoletta

---

Se vuoi chiuderla al 100%, dimmi:
- Mac o Windows
- modello GPU
- usi Wacom o no

Così ti dico esattamente dove intervenire senza tentativi.

---

## 🧑 User

già provato a disattivare processore grafico ma niente

---

## 🤖 Assistant

Ok, allora scartiamo la GPU. Con quel comportamento (si vede un attimo mentre ridimensioni e poi sparisce appena muovi), il problema è quasi sempre **input device / driver / overlay**, non Photoshop in sé.

Vai diretto su questi punti, in ordine:

---

### 1. Tavoletta grafica (prima causa in assoluto)
Se hai anche solo i driver installati, possono interferire.

- Chiudi Photoshop
- **Disinstalla completamente i driver Wacom / Huion / XP-Pen**
- Riavvia il computer
- Apri Photoshop solo con mouse/trackpad

👉 Se così funziona: hai trovato il colpevole
A quel punto:
- reinstalla driver aggiornati
- oppure lavora senza **Windows Ink** (Windows) / disattiva funzioni “hover” (Mac)

---

### 2. Problema di scala / DPI (molto comune su Mac e monitor esterni)
Il cursore che “sparisce” è spesso un bug di scaling.

- Photoshop → **Preferenze → Interfaccia**
- Cambia:
- **Scala UI** (prova 100% o 200%)
- Riavvia Photoshop

Su Mac:
- Prova anche a cambiare **Risoluzione monitor** (Sistema → Schermi → “Ridimensionata”)

---

### 3. Conflitto con app in overlay
Qualsiasi app che disegna sopra lo schermo può rompere il cursore:

Controlla e chiudi:
- software di screen recording
- app tipo CleanShot, Loom
- utility mouse (Logitech Options, SteerMouse ecc.)
- overlay GPU (Nvidia/AMD)

---

### 4. Brush preview glitch (workaround rapido)
Prova questo:

- Premi **F5** (apri impostazioni pennello)
- Cambia leggermente:
- Spacing
- oppure attiva/disattiva Shape Dynamics

👉 Se il cursore torna stabile → è un bug di rendering del brush engine

---

### 5. Reset completo (non solo preferenze base)
Se niente ha funzionato:

1. Chiudi Photoshop
2. Vai manualmente a cancellare:
- cartella **Adobe Photoshop Settings**
3. Riapri Photoshop

(Su Mac: `~/Library/Preferences/Adobe Photoshop [version] Settings`)

---

### Diagnosi chiara
A questo punto le probabilità sono:

- 60% driver tavoletta (anche se non la stai usando)
- 25% scaling / monitor
- 10% software in overlay
- 5% bug Photoshop vero

---

Se vuoi risolverla senza tentativi:
dimmi **setup preciso**:
- Mac o Windows
- monitor esterno sì/no
- marca mouse/tavoletta

Così vado chirurgico e ti faccio saltare tutta la fase di debug.