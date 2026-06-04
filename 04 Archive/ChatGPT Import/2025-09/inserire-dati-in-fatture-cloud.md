---
title: "Inserire dati in Fatture Cloud"
created: 2025-09-29
updated: 2025-09-29
model: gpt-5
messages: 14
source: chatgpt-import
tags: []
---

# Inserire dati in Fatture Cloud

> Importato da ChatGPT export · 14 messaggi · gpt-5 · 2025-09-29

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

mi dici come inserire questi dati in fatture in cloud?

---

## 🤖 Assistant

Perfetto, ti spiego passo passo come inserire questi dati in **Fatture in Cloud** per emettere la fattura correttamente:

---

### 1. **Dati del cliente**
- Vai su **Clienti > Nuovo Cliente** (o modifica se già inserito).
- **Ragione sociale:** Mokusei Publishers Inc.
- **Indirizzo:** 55-1, Hirai cho, Simogyo ku, Kyoto city, Kyoto, Japan 600 8118
- **Nazione:** Giappone
- Gli altri campi (P.IVA, Codice fiscale, ecc.) puoi lasciarli vuoti perché fuori UE e probabilmente non disponibili.

---

### 2. **Creazione fattura**
- Vai su **Fatture > Nuova Fattura di vendita**.
- Seleziona **Cliente: Mokusei Publishers Inc.**

---

### 3. **Dettagli riga fattura**
Inserisci le voci come richiesto da loro, così risulta chiaro:

1. **Servizio fotografico Goldwin Executive shooting** → € 500,00
2. **Rimborso spese gas/highway** → € 80,00
3. **Rimborso spese tunnel** → € 70,00

**Totale imponibile: € 650,00**

---

### 4. **Regime fiscale**
- In quanto sei in **forfettario**:
- imposta l’aliquota IVA a **0% – Operazione non soggetta (art. 1, c. 54-89, L. 190/2014 – Regime Forfettario)**.
- aggiungi la **marca da bollo da 2 €** se l’importo supera i 77,47 € (puoi selezionarla in automatico su Fatture in Cloud).

---

### 5. **Sezione pagamento**
- Metodo: **Bonifico bancario**.
- Inserisci i tuoi dati:
- Nome e cognome
- Indirizzo e CAP
- Numero di telefono
- IBAN
- Nome e indirizzo della banca
- SWIFT/BIC

(Nel campo **Note al pagamento** puoi specificare: *“Pagamento tramite bonifico bancario. Coordinate indicate in calce alla fattura”*).

---

### 6. **Note aggiuntive**
Nelle **Note** della fattura puoi riportare qualcosa tipo:
*"Fattura emessa per servizi fotografici e rimborsi spese in occasione del Goldwin Executive shooting."*

---

Vuoi che ti prepari io un **fac-simile compilato** in PDF (con intestazione e struttura pronta) che poi puoi copiare/incollare dentro Fatture in Cloud, così hai già il modello corretto?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

allora prima di tutto devo compilare questo

---

## 🤖 Assistant

Esatto, prima di tutto devi inserire correttamente il cliente in **anagrafica**. Ti compilo i campi con i dati che hai:

---

### **Compilazione campi**
- **Ragione sociale / nome:**
Mokusei Publishers Inc.

- **Indirizzo:**
55-1, Hirai cho, Simogyo ku

- **Comune:**
Kyoto

- **CAP:**
6008118

- **Provincia:**
(puoi lasciare vuoto, perché è un dato italiano; per l’estero non serve)

- **Note indirizzo (opzionale):**
Kyoto City

- **Paese:**
Giappone

- **Partita IVA (o Tax ID):**
vuoto (non è obbligatorio per clienti extra-UE se non te l’hanno fornito)

- **Codice fiscale:**
vuoto

- **Codice cliente:**
opzionale (puoi inventarne uno, es. MOKUSEI01, se vuoi tener traccia)

- **Indirizzo e-mail:**
metti l’email della persona che ti ha scritto (se vuoi inviare la fattura direttamente da Fatture in Cloud).

---

👉 Così puoi salvare l’anagrafica cliente e poi passare a creare la fattura.

Vuoi che ti scriva anche esattamente come configurare le **righe della fattura** dentro Fatture in Cloud (descrizioni + importi + causali fiscali)?

---

## 🧑 User

non mi fa lasciare la provincia vuota

---

## 🤖 Assistant

Chiaro, in **Fatture in Cloud** il campo *Provincia* è obbligatorio, ma serve solo per clienti italiani.
Per clienti esteri si mette un valore neutro.

In questi casi hai due opzioni pratiche:

1. **Inserire la sigla internazionale “JP”** → è accettato e chiaro che si tratta di Giappone.
2. **Ripetere “KY” (Kyoto)** come se fosse la provincia → soluzione che molti usano per clienti giapponesi/americani.

---

### Compilazione finale consigliata
- **Indirizzo:** 55-1, Hirai cho, Simogyo ku
- **Comune:** Kyoto
- **CAP:** 6008118
- **Provincia:** JP (oppure KY)
- **Paese:** Giappone

---

Vuoi che ti prepari una schermata completa con tutte le righe già pronte da copiare dentro Fatture in Cloud (cliente + fattura)?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

per i dati di pagamento mi fa mettere solo questi

---

## 🤖 Assistant

Perfetto, ti confermo che in **Fatture in Cloud** la sezione “Fatturazione elettronica > Dati pagamento” ha dei campi limitati.
Quindi puoi gestirla così:

---

### Campi standard
- **Metodo di pagamento:** Bonifico
- **Nome istituto di credito:** N26 Bank
- **IBAN:** IT74T03646016005265…
- **Nome beneficiario:** Andrea Passerini

---

### Dove mettere gli altri dati richiesti dal cliente (SWIFT, indirizzo banca, telefono ecc.)
Li puoi inserire in **Note in calce alla fattura**.
Ad esempio:

```
Dati bancari completi per bonifico internazionale:
IBAN: IT74T03646016005265…
SWIFT/BIC: NTSBDEB1XXX
Intestato a: Andrea Passerini
Banca: N26 Bank, Klosterstraße 62, 10179 Berlin, Germania
Indirizzo beneficiario: [il tuo indirizzo completo]
Telefono beneficiario: +39 xxx xxx xxxx
```

---

In questo modo la fattura resta formalmente corretta in Fatture in Cloud e il cliente giapponese riceve comunque tutti i dati necessari per pagarti.

Vuoi che ti prepari un testo “Note in calce” già pronto da copiare dentro Fatture in Cloud con tutti i dati (IBAN, SWIFT, banca, tuo indirizzo ecc.)?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

ma poi in realtà mi esce così

---

## 🤖 Assistant

Esatto, è normale: **Fatture in Cloud** nel corpo della fattura mostra solo i dati standard di pagamento (IBAN, intestatario, BIC).
Per clienti italiani basta, ma per pagamenti extra-UE (come il Giappone) spesso chiedono anche indirizzo banca e indirizzo beneficiario.

👉 La soluzione è aggiungere una riga di testo in **Note in calce alla fattura**.
Così il cliente riceve tutto in un unico documento.

Esempio pronto da incollare:

```
Dati completi per bonifico internazionale:
IBAN: IT74T036460160052653498328
BIC/SWIFT: NTSBITM1XXX
Intestato a: Andrea Passerini
Banca: N26 Bank GmbH, Klosterstraße 62, 10179 Berlin, Germania
Indirizzo beneficiario: [il tuo indirizzo completo in Italia]
Telefono beneficiario: +39 393 4330610
```

---

Vuoi che ti prepari direttamente il testo completo (con il tuo indirizzo già messo) così puoi copiarlo pari pari dentro Fatture in Cloud senza doverci rimettere mano?

---

## 🧑 User

METTIMELI IN INGLESE

---

## 🤖 Assistant

Perfetto, eccoti il testo in **inglese** pronto da incollare in *Note in calce alla fattura* su Fatture in Cloud:

```
Bank details for international wire transfer:

IBAN: IT74T036460160052653498328
BIC/SWIFT: NTSBITM1XXX
Account holder: Andrea Passerini
Bank: N26 Bank GmbH, Klosterstraße 62, 10179 Berlin, Germany
Beneficiary address: [Your full address in Italy]
Beneficiary phone: +39 393 4330610
```

Vuoi che ti inserisca direttamente anche il tuo indirizzo completo (via, CAP, città) così non devi aggiungerlo a mano ogni volta?

---

## 🧑 User

ma con l'iban italiano n26 fa sempre riferimento alla banca tedesca o l'indirizzo è italiano?

---

## 🤖 Assistant

Domanda molto precisa. Ti chiarisco:

- **IBAN N26 italiano** → inizia con **IT**, quindi è un conto aperto in Italia e regolato in Italia.
- **BIC/SWIFT (NTSBITM1XXX)** → identifica **N26 Bank – Italia**, con sede a Milano.
- L’indirizzo di riferimento da usare nelle fatture non è quello della sede tedesca di Berlino, ma quello italiano.

---

### Indirizzo ufficiale N26 in Italia
**N26 Bank AG – Succursale Italiana**
Via Sile 18, 20139 Milano, Italy

---

👉 Quindi nella fattura per il cliente giapponese ti conviene scrivere:

```
Bank details for international wire transfer:

IBAN: IT74T036460160052653498328
BIC/SWIFT: NTSBITM1XXX
Account holder: Andrea Passerini
Bank: N26 Bank AG, Italian Branch, Via Sile 18, 20139 Milan, Italy
Beneficiary address: [Your full address in Italy]
Beneficiary phone: +39 393 4330610
```

Vuoi che ti prepari la versione finale completa con già dentro il tuo indirizzo beneficiario (così pronta da copiare)?