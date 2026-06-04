---
title: "Trasformare testo in minuscolo"
created: 2026-05-26
updated: 2026-05-26
model: gpt-5-5
messages: 2
source: chatgpt-import
tags: []
---

# Trasformare testo in minuscolo

> Importato da ChatGPT export · 2 messaggi · gpt-5-5 · 2026-05-26

## 🧑 User

come trasformo in minuscolo testi su piu caselle tutte fatte con caps lock

---

## 🤖 Assistant

Se sei su Excel o Google Sheets e hai già scritto tutto in MAIUSCOLO, hai varie opzioni:

### Metodo rapido con formula
Supponiamo che il testo sia nella colonna A.

Nella colonna accanto scrivi:

```excel
=MINUSC(A1)
```

oppure in Google Sheets anche:

```excel
=LOWER(A1)
```

Poi:
1. Trascini la formula verso il basso.
2. Copi i risultati.
3. Incolla come “solo valori” sopra i testi originali.

---

### Se vuoi iniziale maiuscola e resto minuscolo
Usa:

```excel
=MAIUSC.INIZ(A1)
```

Esempio:
- `CIAO COME STAI` → `Ciao Come Stai`

---

### In Excel senza formule (Power Query)
Se hai tante celle:
1. Seleziona tabella
2. **Dati → Da tabella/intervallo**
3. In Power Query:
- seleziona colonna
- **Trasforma → Formato → minuscolo**
4. Chiudi e carica.

Molto più pulito su dataset grossi.

---

### Se sei su Mac e intendi testo normale (Word, Notes ecc.)
Puoi usare:
- **Shift + Fn + F3** su Word
- oppure strumenti tipo:
- urlConvert Casehttps://convertcase.net

che trasformano blocchi di testo al volo.