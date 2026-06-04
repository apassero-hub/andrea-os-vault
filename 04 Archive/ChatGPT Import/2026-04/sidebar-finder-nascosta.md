---
title: "Sidebar Finder nascosta"
created: 2026-04-29
updated: 2026-04-29
model: gpt-5-3
messages: 10
source: chatgpt-import
tags: []
---

# Sidebar Finder nascosta

> Importato da ChatGPT export · 10 messaggi · gpt-5-3 · 2026-04-29

## 🧑 User

perch'è se clicco su mac hd su scrivania mi apre il finder senza barra laterale adesso?

---

## 🤖 Assistant

Succede perché stai aprendo una **nuova finestra del Finder con la barra laterale nascosta**. Non è un bug: hai semplicemente disattivato la sidebar in quella finestra (o hai salvato uno stato senza sidebar).

### Soluzione immediata
- Premi **⌥ + ⌘ + S** → riattiva la barra laterale
oppure
- Vai su **Vista → Mostra barra laterale**

### Perché succede
Quando fai doppio clic su “Macintosh HD” dalla scrivania:
- macOS apre una finestra Finder “pulita”
- se l’ultima volta quella finestra aveva la sidebar nascosta, mantiene quello stato

### Come evitare che ricapiti
Apri una finestra Finder normale (con sidebar visibile), poi:
- **Finder → Impostazioni → Generali**
- Imposta: **“Le nuove finestre del Finder mostrano” → Macintosh HD** (o quello che vuoi)

In questo modo userai sempre una finestra standard con sidebar, invece di quella “strana” senza struttura.

Se vuoi, si può anche forzare un layout Finder coerente su tutte le finestre (colonne, sidebar, path bar ecc.).

---

## 🧑 User

e su safari come faccio?

---

## 🤖 Assistant

Stessa logica: in entity["software","Safari","web browser by Apple"] hai nascosto la barra laterale in quella finestra.

### Ripristino immediato
- Premi **⌘ + ⇧ + L** → mostra/nasconde la barra laterale
oppure
- Vai su **Vista → Mostra barra laterale**

### Nota importante
La barra laterale in Safari cambia contenuto (Preferiti, Elenco lettura, Schede), quindi:
- se la riapri e non vedi quello che ti aspetti, clicca in alto nella sidebar per selezionare la sezione giusta (es. “Preferiti”)

### Perché ti succede
Safari salva lo stato della finestra:
- se chiudi una finestra senza sidebar → la prossima può aprirsi uguale

### Se vuoi un comportamento stabile
Non esiste un’impostazione precisa come nel Finder per forzare sempre la sidebar visibile. L’unico modo affidabile è:
- lasciare almeno una finestra aperta con la sidebar attiva
oppure
- riattivarla manualmente quando serve (shortcut e via)

Se vuoi, posso anche sistemarti un setup pulito e coerente tra Finder + Safari (layout, scorciatoie, gestione finestre) così smetti di perderci tempo.

---

## 🧑 User

scusa ho sbagliato. su safari come faccio a svuotare la cache?

---

## 🤖 Assistant

Su entity["software","Safari","web browser by Apple"] hai tre livelli, dal più “pulito” al più rapido.

---

## Metodo completo (consigliato)
Cancella cache + cookie + dati siti:

1. **Safari → Impostazioni → Privacy**
2. Clicca **“Gestisci dati siti web…”**
3. **“Rimuovi tutto”** → Conferma

👉 Risolve quasi sempre problemi di login, contenuti non aggiornati, script rotti.

---

## Metodo veloce (solo cache tecnica)
Serve attivare il menu sviluppatore:

1. **Safari → Impostazioni → Avanzate**
2. Spunta **“Mostra menu Sviluppo nella barra dei menu”**
3. Poi in alto: **Sviluppo → Svuota cache**

Shortcut: **⌥ + ⌘ + E**

👉 Non tocca cookie e login.

---

## Metodo “via di mezzo”
Cancella cronologia + dati recenti:

1. **Cronologia → Cancella cronologia…**
2. Scegli periodo (ultima ora / oggi / tutto)

👉 Più rapido ma meno preciso (toglie anche cronologia).

---

## Quale usare davvero
- Problema serio su un sito → **Metodo completo**
- Solo refresh aggressivo → **Sviluppo → Svuota cache**
- Pulizia generale veloce → **Cancella cronologia**

Se hai un sito specifico che non si aggiorna, dimmi quale: ti dico il modo più rapido per forzarlo senza perdere sessioni inutilmente.

---

## 🧑 User

command option e non fa niente

---

## 🤖 Assistant

È normale: **⌥ + ⌘ + E funziona solo se hai attivato il menu “Sviluppo”** in entity["software","Safari","web browser by Apple"]. Se non è attivo, la scorciatoia non fa nulla.

### Fai così, passo secco:
1. **Safari → Impostazioni → Avanzate**
2. Spunta **“Mostra menu Sviluppo nella barra dei menu”**
3. Ora in alto comparirà **Sviluppo**
4. Vai su **Sviluppo → Svuota cache**

A questo punto la shortcut **⌥ + ⌘ + E** inizierà a funzionare.

---

### Se ancora non succede niente
- Verifica che Safari sia **la finestra attiva** (non un’altra app)
- Controlla in **Impostazioni di Sistema → Tastiera → Abbreviazioni** che non ci sia un conflitto
- In alternativa, usa direttamente il menu **Sviluppo → Svuota cache** (fa esattamente la stessa cosa)

---

### Soluzione immediata senza sbatterti
Se non vuoi perdere tempo:
- **Cronologia → Cancella cronologia → “ultima ora”**
Risolve nel 90% dei casi, anche se è meno “chirurgico”.

Se mi dici cosa stai cercando di risolvere (es. sito che non si aggiorna, login bloccato), ti do il metodo più rapido senza cancellare roba inutile.

---

## 🧑 User

ma mosta menu sviluppo ce l'ho attivo

---

## 🤖 Assistant

Se il menu **Sviluppo è attivo** ma **⌥ + ⌘ + E non fa nulla**, il problema non è Safari in sé. Vai diretto su questi controlli, in ordine:

---

### 1) Verifica banale ma spesso è quello
- Assicurati che **entity["software","Safari","web browser by Apple"] sia l’app attiva**
- Clicca in alto su **Sviluppo → Svuota cache**

👉 Se dal menu funziona, la funzione è ok: è solo la scorciatoia che non viene intercettata.

---

### 2) Controlla conflitti di scorciatoie
Vai in:
- **Impostazioni di Sistema → Tastiera → Abbreviazioni → Abbreviazioni app**

Guarda se:
- esiste una scorciatoia globale o per Safari che usa **⌥ + ⌘ + E**
- oppure se qualche app (tipo tool di screenshot, utility tastiera, ecc.) l’ha “presa”

👉 Se sì, cambiala o rimuovila.

---

### 3) Layout tastiera / lingua
Se usi layout non standard (es. inglese, custom):
- alcune combinazioni con **Option** possono non essere registrate correttamente

Test rapido:
- prova a premere **⌥ + ⌘ + E** in un campo di testo → vedi se produce caratteri strani o nulla
👉 Se non registra nulla, è un problema di input/shortcut, non di Safari

---

### 4) Test definitivo (2 secondi)
Apri il menu:
- **Sviluppo**
- tienilo aperto

Poi premi **⌥ + ⌘ + E**

👉 Se la voce “Svuota cache” non si evidenzia, la shortcut non è collegata → quasi sicuramente conflitto o override di sistema

---

### 5) Soluzione pragmatica (senza perdere tempo)
Usa:
- **Sviluppo → Svuota cache** (manuale, identico risultato)

Oppure:
- **⌘ + R** → refresh normale
- **⌥ + ⌘ + R** → refresh forzato (spesso basta senza svuotare cache globale)

---

Se vuoi chiuderla definitivamente, posso dirti come **rimappare la shortcut** in modo che funzioni sempre (anche meglio di quella di default).