---
title: "Controllo form Elementor"
created: 2025-09-09
updated: 2025-09-09
model: gpt-5
messages: 6
source: chatgpt-import
tags: []
---

# Controllo form Elementor

> Importato da ChatGPT export · 6 messaggi · gpt-5 · 2025-09-09

## 🧑 User

con active campaign è possibile far si che quando un contatto viene aggiunto da form elementor sul nostro sito in automativo venga anche inserito sulle liste o l'unica cosa che si può fare è categorizzarlo coi tag?

---

## 🤖 Assistant

Ti dico le cose come stanno.

Con **ActiveCampaign** hai due strade principali:

1. **Liste**
- Quando configuri un’integrazione (es. Elementor Form → ActiveCampaign), puoi decidere che il contatto venga iscritto direttamente a una **lista specifica**.
- Questo dipende dal connettore che usi: con il widget **ActiveCampaign nativo di Elementor Pro** o tramite **integrazione API/Zapier/AutomatorWP**, puoi dire “aggiungi questo contatto alla lista X” al momento dell’iscrizione.
- Quindi sì, **è possibile iscriverlo subito a una lista**, non sei obbligato a passare solo dai tag.

2. **Tag**
- L’approccio moderno in ActiveCampaign è spingere molto sui **tag** per segmentare (es. “ha compilato form sito”, “interessato a snowboard”, ecc.).
- La lista viene usata come contenitore “macro” (es. Newsletter Generale), mentre i tag gestiscono i flussi e i segmenti.
- Per esempio: tutti i form portano i contatti in una sola lista (“Contatti Principali”), poi i tag ti dicono da dove arrivano e cosa hanno fatto.

👉 In sintesi:
- **Puoi inserirli direttamente in lista** già dal form Elementor.
- La **best practice** è: 1–2 liste totali (non decine), e usare i **tag** per distinguere provenienza e interessi.

Vuoi che ti prepari uno schema pratico con **come impostare la cosa in Elementor** (differenza se usi il widget nativo vs Zapier/integrazione esterna)?

---

## 🧑 User

siccome il form di elementor non l'ho fatto io diamo una controllata ai settaggi per capire meglio se è settato nel modo giusto?

---

## 🤖 Assistant

Perfetto, andiamo dritti al punto.
Per capire se il form Elementor che avete sul sito è configurato correttamente con ActiveCampaign, ti consiglio di fare questi passaggi rapidi:

### 1. Apri Elementor e seleziona il form
- Vai alla pagina dove si trova il form.
- Clicca sopra il form per aprire il **widget Form** nelle impostazioni a sinistra.

### 2. Vai su **Azioni dopo l’invio** (Actions After Submit)
- Qui dovresti vedere un elenco (es. Email, Redirect, Webhook, ecc.).
- **Controlla se c’è “ActiveCampaign”**. Se non c’è, vuol dire che non è mai stata configurata l’integrazione diretta.

### 3. Se c’è ActiveCampaign
- Scorri giù nel pannello di sinistra e apri la sezione **ActiveCampaign**.
- Qui dovresti trovare:
- **Account** (collegato tramite API Key e URL di ActiveCampaign).
- **List** → la lista a cui vengono iscritti i contatti.
- **Tags** → eventuali tag che vengono applicati.

👉 Se vedi che nel campo **List** non è selezionata nessuna lista, allora i contatti non entrano in una lista: vengono solo registrati con i tag.

### 4. Se non c’è ActiveCampaign
- Vuol dire che chi ha fatto il form ha usato un’altra strada:
- **Webhook** collegato a Zapier/Make.
- Oppure un’azione “Email” che manda i dati a mano.
- In questo caso i contatti possono non finire in lista se non è stato impostato esplicitamente.

---

Vuoi che ti prepari una **checklist pratica** (con screenshot di riferimento e dicitura esatta dei campi di Elementor) così puoi aprire il form e capire subito se i contatti entrano in lista o solo coi tag?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Ho guardato bene lo screenshot che hai caricato.

Dal pannello **ActiveCampaign** vedo chiaramente che:
- Il contatto “ProvaForever” è stato **iscritto alla lista FOREVER NEWSLETTER ITA tramite API** (quindi molto probabilmente via il form Elementor).
- Subito dopo risulta **“Respinto dall’elenco”**.
- Nei dettagli della lista si vede lo storico: prima *Iscritto tramite API* → poi *Respinto dall’elenco*.

Questo significa che:
1. **Il form Elementor sta già aggiungendo i contatti alla lista**, non solo coi tag.
2. Il problema non è che non entrino in lista, ma che ActiveCampaign li stia respingendo.

### Possibili cause del “Respinto”
- **Double Opt-In non confermato**: se la lista è impostata con conferma email e il contatto non clicca, rimane respinto.
- **Indirizzo email fittizio/test (es. Gmail con numeri a caso)**: ActiveCampaign potrebbe marcarlo come non valido.
- **Blacklist interna di ActiveCampaign**: se quell’email è già stata respinta o disiscritta in passato, non viene riammessa.

👉 Quindi il settaggio lato Elementor è corretto (iscrizione in lista c’è). Bisogna invece controllare in **ActiveCampaign → Liste → FOREVER NEWSLETTER ITA → Impostazioni**:
- Se è attivo il **double opt-in**.
- Qual è il messaggio di conferma inviato.
- Se la lista accetta direttamente i contatti o richiede la conferma manuale.

Vuoi che ti prepari uno schema su **come verificare e disattivare il double opt-in** (se preferisci che i contatti entrino subito attivi senza conferma)?