---
title: "Crea modello fattura personalizzato"
created: 2025-08-02
updated: 2025-08-02
model: gpt-4o
messages: 4
source: chatgpt-import
tags: []
---

# Crea modello fattura personalizzato

> Importato da ChatGPT export · 4 messaggi · gpt-4o · 2025-08-02

## 🧑 User

il mi sistema di fatturazione mi permette di inviare direttamente la copia di cortesia delle fatture ai miei clienti ma non mi piace com'è impostata. mi crei un modello personalizzato meglio fatto, professionale e che rispecchia chi sono e cosa faccio?

---

## 🤖 Assistant

Certo. Per creare un modello professionale e personalizzato della **copia di cortesia** da inviare ai tuoi clienti, mi servono alcune informazioni. Ecco cosa ti chiedo per realizzarlo al meglio:

---

### 📌 **Informazioni di base**
1. **Logo**: vuoi inserirlo in alto? Se sì, hai un file o lo stile (bianco/nero, colorato)?
2. **Colori preferiti o palette**: vuoi uno stile minimale (es. bianco e nero) o con un tocco grafico?
3. **Font preferiti** (se ne usi alcuni abitualmente, es. per il tuo sito o portfolio).

---

### 🧾 **Struttura della fattura**
4. **Intestazione mittente**:
- Nome e cognome o nome attività
- Indirizzo completo
- Partita IVA / CF
- Regime fiscale (forfettario, ordinario, ecc.)
- Eventuali diciture obbligatorie (es. “Operazione non soggetta a IVA ai sensi dell’art. 1, commi 54-89, Legge 190/2014”)

5. **Dati del cliente**:
- Quali dati raccogli e visualizzi? (Nome, azienda, indirizzo, CF/P.IVA, ecc.)

6. **Contenuto della fattura**:
- Vuoi mantenere righe con: descrizione / quantità / prezzo unitario / totale?
- Vuoi aggiungere **note personalizzate** per ogni fattura? (es. grazie per il lavoro svolto, uso delle immagini, scadenze ecc.)
- Serve una sezione per **riepilogo pagamenti o IBAN**?

---

### 💬 **Stile comunicativo**
7. Vuoi un tono più:
- [ ] Istituzionale e formale
- [ ] Caldo ma professionale
- [ ] Creativo e personale (es. con brevi messaggi come “Grazie per aver scelto di lavorare con me”)

---

### 🖼️ **Esempio visivo**
8. Preferisci un layout:
- [ ] Classico e lineare (come quelli fiscali)
- [ ] Editoriale e ben impaginato, simile a una presentazione
- [ ] Una via di mezzo

---

Appena mi dai queste indicazioni ti preparo un **modello grafico e testuale** (che potrai usare sia come PDF statico sia come template Word o InDesign). Posso anche prepararlo pronto da importare nel sistema che usi, se supporta HTML o personalizzazione grafica.

Fammi sapere.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

non mi serve un modello di fattura ma solo dell'email della copia di cortesia. vedi file qui allegato

---

## 🤖 Assistant

Perfetto, ho analizzato il contenuto dell’email attuale che usi per inviare la **copia di cortesia**. Al momento è piuttosto impersonale e generico.

Ti propongo ora **una versione migliorata**, più curata dal punto di vista del tono, della chiarezza e della presentazione. Mantiene tutte le variabili attive del sistema, ma con una comunicazione più professionale e in linea con il tuo profilo.

---

### ✅ **Nuovo modello suggerito — Email copia di cortesia**

**Oggetto:**
`{{nostro-nostra}} {{documento-numerato}} da parte di {{ragione-sociale}}`

**Corpo email:**
```text
Gentile {{cliente}},

in allegato trova la copia di cortesia relativa a {{nostro-nostra}} {{documento-numerato}} emessa da {{ragione-sociale}}.

Per visualizzarla o procedere al pagamento, può cliccare sul pulsante qui sotto:

{{tspay-tastodoc}}

Resto a disposizione per qualsiasi chiarimento.

Un cordiale saluto,
{{ragione-sociale}}
```

---

### 🧩 Varianti possibili:
#### Tonalità più calda, creativa:
```text
Ciao {{cliente}},

ti invio in allegato la copia di cortesia relativa a {{nostro-nostra}} {{documento-numerato}}.

Puoi visualizzarla o procedere al pagamento cliccando qui sotto:

{{tspay-tastodoc}}

Grazie per la fiducia,
{{ragione-sociale}}
```

#### Con oggetto visibile del documento:
```text
Oggetto: {{oggetto-visibile}} – {{nostro-nostra}} {{documento-numerato}} da {{ragione-sociale}}

Gentile {{cliente}},

qui di seguito trova la copia di cortesia della {{nostro-nostra}} {{documento-numerato}} per:
**{{oggetto-visibile}}**

Per visualizzare il documento o procedere al pagamento:

{{tspay-tastodoc}}

Cordiali saluti,
{{ragione-sociale}}
```

---

### 📌 Come usarlo
Puoi copiare e incollare uno dei modelli nel campo di testo del tuo sistema (come da screenshot), sostituendo quello esistente. Fammi sapere se vuoi una versione anche in inglese o bilingue.

Vuoi che te ne prepari uno con un tocco più distintivo o più diretto a seconda del cliente (ad esempio per agenzie, aziende, clienti privati)?