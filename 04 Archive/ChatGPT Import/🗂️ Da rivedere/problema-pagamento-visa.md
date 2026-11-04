---
title: "Problema pagamento Visa"
created: 2026-05-28
updated: 2026-05-28
model: gpt-5-5
messages: 6
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Problema pagamento Visa

> Importato da ChatGPT export · 6 messaggi · gpt-5-5 · 2026-05-28

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

_[contenuto non testuale: image_asset_pointer]_

_[contenuto non testuale: image_asset_pointer]_

_[contenuto non testuale: image_asset_pointer]_

per il pagamento di visa abbiamo ricevuto una mail con la richiesta di alcuni dati bancari per procedere al pagamento. ma a quanto pare a loro non è sufficiente. questo è il file che produce il nostro account revolut business. come possiamo fare?

---

## 🤖 Assistant

Il problema non è tanto Revolut. Il problema è che il documento che state inviando non contiene i dati che il reparto finance vuole vedere per compliance interna.

Nella mail loro chiedono esplicitamente:

- account name
- account details
- account number
- sort code

La “Lettera di attestazione” di Revolut che avete allegato è una semplice audit confirmation. Conferma che il conto esiste e che è attivo, ma non mostra IBAN, account number o sort code in modo chiaro. Per un reparto accounting corporate spesso non basta.

Quello che dovete mandare è invece uno di questi:

1. Bank account confirmation / Proof of account
2. Estratto conto con IBAN visibile
3. Documento “Account details” di Revolut Business

La soluzione più pulita è questa:

### Da Revolut Business scaricate:
Settings → Accounts → selezionate il conto → Details → “Download account confirmation” oppure “Statement”.

Deve comparire chiaramente:

- Nome società: MOUNTAIN FLOW TRAVEL SERVICES LTD
- IBAN
- BIC/SWIFT
- Account number
- Sort code
- eventualmente indirizzo azienda

Se usate conto UK locale Revolut:
- sort code + account number devono essere visibili.

Se invece state usando solo IBAN europeo:
- spiegate che il conto è IBAN-based e non usa sort code tradizionale.

In pratica vi serve un documento simile a:
“Proof of bank account ownership”.

Non la lettera audit che avete inviato.

Poi risponderei così, molto semplice e professionale:

> Hi Aatish,
>
> Please find attached the bank account confirmation document showing the account holder name, IBAN/account number and bank details required for your records.
>
> Let us know if anything else is needed in order to proceed with the payment.
>
> Kind regards,
> Andrea Passerini
> Forever Snow Trips

Se vuoi, posso anche dirti esattamente dove trovare dentro Revolut Business il documento corretto, perché cambia leggermente tra app web e mobile.

---

## 🧑 User

conto uk con impostazione lingua in italiano, mi guidi

---

## 🤖 Assistant

Certo. Da browser desktop, con Revolut Business in italiano, fai così:

1. Apri Revolut Business
2. Nel menu a sinistra vai su **Conti**
3. Seleziona il conto GBP (quello UK)
4. In alto o sulla destra cerca:
- **Dettagli**
- oppure **Informazioni**
- oppure l’icona con i tre puntini `•••`

Dentro quella schermata dovresti vedere:

- Nome beneficiario
- Nome banca
- Sort code
- Account number
- IBAN
- BIC

A quel punto:

5. Clicca su:
- **Scarica**
- oppure **Conferma dati bancari**
- oppure **Scarica conferma del conto**

Il PDF corretto deve mostrare chiaramente:
- nome società
- account number
- sort code
- IBAN

NON dovete scaricare:
- “lettera di attestazione”
- “audit confirmation”

Perché è il documento sbagliato per questo uso.

Se non trovi “Conferma dati bancari”:

### Metodo alternativo
Sempre dentro il conto GBP:

1. Vai su **Estratti conto**
2. Genera un estratto PDF
3. Intervallo:
- ultimi 30 giorni
4. Assicurati che nella preview compaiano:
- account number
- sort code
- intestazione azienda

Se compaiono, va benissimo anche quello.

Appena hai il PDF, controlla prima di inviarlo:
- che non siano censurati i numeri
- che si leggano bene sort code e account number
- che il nome società coincida esattamente con quello in fattura

Poi invialo dicendo che è il “bank account confirmation document”.

---

## 🧑 User

è questo?

---

## 🤖 Assistant

Sì, questo è il documento corretto.
Adesso contiene esattamente quello che il reparto finance vi stava chiedendo:

- account number
- sort code
- nome società
- indirizzo
- IBAN
- banca
- conferma ufficiale Revolut

Quindi questa volta non dovrebbero avere motivi validi per respingerlo. fileciteturn0file0

In particolare queste righe sono quelle fondamentali:

- Numero di conto: `21849358`
- Codice avviamento bancario / Sort code: `04-29-09`
- Beneficiario: `MOUNTAIN FLOW TRAVEL SERVICES LTD`

Adesso risponderei semplicemente così:

> Hi Aatish,
>
> Please find attached the updated bank account confirmation document showing the account number and sort code clearly visible for your records and payment processing.
>
> Please let us know if anything else is required.
>
> Kind regards,
> Andrea Passerini
> Forever Snow Trips

A questo punto siete allineati con le richieste standard di accounting UK.