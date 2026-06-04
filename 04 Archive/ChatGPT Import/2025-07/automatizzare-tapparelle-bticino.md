---
title: "Automatizzare tapparelle BTicino"
created: 2025-07-23
updated: 2025-07-23
model: gpt-4o
messages: 2
source: chatgpt-import
tags: []
---

# Automatizzare tapparelle BTicino

> Importato da ChatGPT export · 2 messaggi · gpt-4o · 2025-07-23

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Allora a casa ho questa serie di interruttori a parete dell'abiticino, se non sbaglio dovrebbe essere la serie Living, e ti spiego qual è il problema, ho delle tapparelle elettriche, quindi c'è il pulsante che ha i due sub pulsanti su e giù che servono per alzare o abbassare le tapparelle, il problema è che funzionano soltanto fintanto che tengo premuto il pulsante, se lo rilascio si blocca, io vorrei implementare un sistema per cui semplicemente quando schiaccio lui me la porta fino in fondo e piuttosto devo schiacciare l'altro pulsante per bloccarla, se la voglio bloccare a metà strada, ma il problema è che siccome ho sette tapparelle, se ci metto un minuto per tirarla giù, spendo ogni volta che devo andare via di casa, soprattutto d'estate che fa caldo, 7 minuti ogni giorno per tirarle su, 7 minuti ogni giorno per tirarle giù, e un quarto d'ora al giorno buttato nel cesso soltanto per tirarle su e giù le tapparelle sembra un po' eccessivo, idealmente sarebbe bello se oltre a questo controllo qua ci fosse la possibilità di avere un controllo generale che ne so vicino alla porta d'uscita che uno schiaccia e si abbassano tutte le tapparelle di casa.

---

## 🤖 Assistant

Hai descritto un’esigenza molto comune e del tutto sensata, soprattutto in abitazioni con più tapparelle motorizzate. Ti confermo che quello nella foto è un punto comandi della serie **Living** di BTicino (in particolare sembra *LivingLight*, colore antracite).

### Situazione attuale
Gli interruttori che hai sono **pulsanti a ritorno automatico**, quindi inviano corrente al motore solo mentre vengono tenuti premuti. Questo tipo di comando **non permette la discesa o salita automatica completa**.

---

### Soluzione: automatizzare il movimento delle tapparelle

#### 1. **Sostituzione pulsanti con comandi elettronici temporizzati (tipo relè tapparella)**
Puoi sostituire gli attuali pulsanti con moduli elettronici BTicino specifici per tapparelle che:

- Avviano la salita o la discesa con un solo impulso.
- Fermano automaticamente a fine corsa (il motore deve avere fine corsa meccanico o elettronico).
- Possono essere fermati manualmente con un secondo impulso.

🔧 **Prodotti BTicino consigliati (compatibili con LivingLight):**
- **F411/2** – Relè tapparella per comandi a impulsi.
- **F411U2** – Versione universale compatibile anche con BUS SCS (in caso tu voglia passare a una gestione domotica).
- **F411N** – Relè tapparella temporizzato, anche con funzione centralizzata.

> Nota: questi moduli vanno installati nel retro del punto comando oppure nel quadro, in funzione dello schema dell’impianto.

---

#### 2. **Controllo centralizzato**
Puoi installare un **modulo centralizzato** (es. vicino alla porta d'ingresso) che:
- Comanda tutte le tapparelle insieme con un solo tasto.
- Può essere cablato in parallelo agli altri comandi o tramite un sistema domotico (es. MyHome BTicino o altro sistema BUS/KNX).

---

#### 3. **Soluzione domotica più evoluta**
Se vuoi fare un upgrade più moderno (magari anche controllabile da app o assistente vocale):

- Passa a **BTicino MyHome** (SCS) o a un sistema **BUS KNX**.
- Oppure, una soluzione **wifi retrofit**, come:
- **Shelly 2.5** (compatibile con Home Assistant e Google/Alexa).
- **Fibaro Roller Shutter 3** (Z-Wave, se hai/hai intenzione di avere un hub domotico).
- **Sonoff Dual R3** (con Tasmota o eWeLink).

Questi moduli si installano dietro l'interruttore o in scatole di derivazione, mantengono la funzione manuale e aggiungono l’automazione.

---

### Conclusione
La soluzione più semplice è **sostituire i pulsanti con relè tapparella temporizzati** BTicino, compatibili con la serie Living. Se vuoi anche un controllo centralizzato e magari da remoto, puoi estendere l’impianto con **relè intelligenti** o passare a una vera **gestione domotica**.

Se vuoi, posso aiutarti a disegnare lo schema più adatto in base alla tua configurazione attuale. Ti servirebbero però alcune info:
- Se i motori sono tutti cablati con linea dedicata fino al quadro.
- Se hai già canaline/scatole disponibili per aggiungere moduli.
- Se i motori hanno finecorsa automatici.
- Se vuoi il controllo via app o solo centralizzato locale.

Fammi sapere e ti guido passo-passo.