---
title: "Celle flaggabili Excel"
created: 2026-05-19
updated: 2026-05-19
model: gpt-5-5
messages: 6
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Celle flaggabili Excel

> Importato da ChatGPT export · 6 messaggi · gpt-5-5 · 2026-05-19

## 🧑 User

come creo delle celle flaggabili su excel?

---

## 🤖 Assistant

Se intendi delle celle “cliccabili” tipo checkbox da spuntare, hai diversi modi. Quello corretto dipende da quanto vuoi fare semplice o professionale.

## Metodo migliore: Checkbox vere (Excel desktop)

### Su Windows
1. Vai su **File > Opzioni > Personalizzazione barra multifunzione**
2. Attiva **Sviluppo**
3. Nella barra in alto apri **Sviluppo**
4. Clicca **Inserisci**
5. Seleziona **Casella di controllo**
6. Disegna la checkbox nella cella

Poi:
- tasto destro sulla checkbox
- modifica testo → cancella la scritta
- ridimensionala dentro la cella

Per copiarla:
- copia/incolla normalmente

---

## Metodo rapido e pulito: menu a tendina con ✔

Molto più ordinato se devi fare checklist grandi.

### Procedura
1. Seleziona le celle
2. Vai su **Dati > Convalida dati**
3. Consenti: **Elenco**
4. Inserisci:
```text
✔,
```

Oppure:
```text
✔,✖
```

Adesso ogni cella avrà un menu a tendina con flag.

Vantaggi:
- leggerissimo
- compatibile ovunque
- perfetto per tracker e task list
- funziona bene anche su mobile e Google Sheets

---

## Metodo ultra rapido: simbolo cliccabile

Puoi anche usare:
- `☐` = vuoto
- `☑` = spuntato

Su Mac:
- `CTRL + CMD + SPACE`
- cerca “checkbox”

Poi cambi manualmente il simbolo.

---

## Metodo professionale con TRUE/FALSE collegato

Le checkbox vere possono essere collegate a una cella:
- spuntata → `TRUE`
- non spuntata → `FALSE`

Utile per:
- formule
- automazioni
- filtri
- dashboard

Per collegarla:
1. Tasto destro checkbox
2. **Formato controllo**
3. **Controllo**
4. **Collegamento cella**

---

## Se usi Excel 365 recente

Microsoft ha introdotto le checkbox native dentro le celle in alcune versioni recenti.

Se disponibili:
1. Seleziona celle
2. Vai su **Inserisci**
3. **Checkbox**

È il sistema migliore perché:
- restano dentro la cella
- si ordinano bene
- niente oggetti flottanti

Ma non tutti gli aggiornamenti di Excel le hanno ancora attive.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

COME CAMBIO LE OPZIONI DEL DROPDOWN MENU=

---

## 🤖 Assistant

Dal tuo screenshot quello non è un “vero” menu dropdown classico: sembra una **convalida dati** di Excel.

Per cambiare le opzioni:

1. Seleziona una delle celle con il dropdown
2. Vai su **Dati**
3. Clicca **Convalida dati**
4. Nella finestra:
- Tipo: **Elenco**
- Guarda il campo **Origine**

Lì troverai qualcosa tipo:
```text
✔,✖
```

oppure:
```text
SI,NO
```

o magari un intervallo tipo:
```text
=Foglio2!A1:A5
```

---

## Se trovi valori scritti direttamente
Esempio:
```text
✔,✖,PENDING
```

Modificali direttamente separandoli con virgole.

---

## Se trovi un intervallo
Esempio:
```text
=Liste!A1:A10
```

Allora le opzioni vengono prese da quelle celle:
- vai nel foglio/intervallo indicato
- modifica lì i valori

---

## Per togliere completamente il dropdown
Sempre in:
**Dati > Convalida dati**
→ clicca **Cancella tutto**

---

## Nota importante
Quel quadratino blu con la spunta nel tuo screenshot sembra quasi una **checkbox inserita sopra la cella**, non solo un dropdown.

Se infatti cliccandola si spunta/sdeseleziona:
- tasto destro sulla checkbox
- **Formato controllo**

Oppure:
- seleziona la checkbox
- premi `CANC`

Excel spesso mischia:
- checkbox vere
- menu dropdown
- simboli ✔ dentro celle

e visivamente sembrano simili.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Mi esce così in selezione unica

---

## 🤖 Assistant

Perfetto, allora stai modificando l’elenco direttamente nella cella, ma Excel lo interpreta come un’unica voce.

In Excel italiano spesso il separatore corretto NON è la virgola, ma il punto e virgola.

Prova così nella sorgente della convalida dati:

```text
SI;NO
```

non:

```text
SI,NO
```

---

Quindi:

1. Seleziona la cella
2. **Dati > Convalida dati**
3. In **Origine** scrivi:
```text
SI;NO
```
4. OK

Adesso nel menu avrai:
- SI
- NO

come due opzioni separate.