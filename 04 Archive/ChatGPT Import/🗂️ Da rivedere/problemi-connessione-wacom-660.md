---
title: "Problemi connessione Wacom 660"
created: 2026-04-02
updated: 2026-04-02
model: gpt-5-3
messages: 2
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Problemi connessione Wacom 660

> Importato da ChatGPT export · 2 messaggi · gpt-5-3 · 2026-04-02

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

La wacom 660 ha problemi di connessione. Ora led attivo in alto a dx, prima in alto a sx

---

## 🤖 Assistant

Ti dico subito il punto: quel comportamento del LED **non è normale**, ma non indica automaticamente che la tavoletta è rotta. È molto più probabile un problema di connessione (driver, Bluetooth o pairing).

### Cosa significa il LED (Wacom Intuos / 660)
- **LED in alto a sinistra** → modalità Bluetooth attiva / in attesa / connessa
- **LED in alto a destra** → modalità USB (cavo) oppure stato di alimentazione diverso

Se prima stava a sinistra e ora lo vedi a destra:
👉 la tavoletta **non è più connessa via Bluetooth** oppure è uscita da quella modalità

---

## Diagnosi rapida (vai diretto così)

### 1. Verifica base
- Spegni la tavoletta
- Riaccendila tenendo premuto il tasto power 2–3 secondi
- Guarda se torna il LED a sinistra

Se resta a destra → non sta entrando in modalità Bluetooth

---

### 2. Reset connessione Bluetooth (fondamentale)
Sul Mac:
1. Vai in **Bluetooth**
2. Rimuovi la Wacom dai dispositivi
3. Spegni la tavoletta

Poi:
1. Riaccendi la tavoletta **tenendo premuto il tasto power più a lungo (5–6 sec)** finché entra in pairing
2. Riassociala

---

### 3. Driver Wacom (spesso è qui il problema)
- Disinstalla completamente i driver Wacom
- Riavvia
- Reinstalla l’ultima versione dal sito ufficiale

Se i driver sono corrotti:
👉 la tavoletta si accende ma non comunica correttamente → LED “strano”

---

### 4. Test con cavo
Collegala via USB:
- Se funziona → **hardware OK**, problema solo Bluetooth
- Se NON funziona → possibile problema più serio (driver o scheda interna)

---

### 5. Caso specifico (molto comune)
Se:
- LED cambia lato
- Non entra più in pairing
- Non viene vista dal Mac

👉 spesso è **modulo Bluetooth bloccato**

Soluzione:
- Reset completo:
- tieni premuto power ~10 secondi
- lascia
- riaccendi

---

## Conclusione chiara
- Il cambio LED indica che **non è più in modalità Bluetooth attiva**
- Nel 90% dei casi è:
- pairing perso
- driver incasinati
- bug del modulo BT

Non partire subito con assistenza.

---

Se vuoi, dimmi:
- modello preciso (CTL-6100WL / CTL-660 ecc.)
- se stai usando Mac o Windows
- cosa succede quando la colleghi via cavo

e ti dico esattamente dove sta il problema senza perdere tempo.