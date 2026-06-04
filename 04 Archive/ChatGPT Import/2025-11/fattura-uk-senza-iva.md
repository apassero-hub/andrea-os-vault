---
title: "Fattura UK senza IVA"
created: 2025-11-17
updated: 2025-11-17
model: gpt-5-1
messages: 4
source: chatgpt-import
tags: []
---

# Fattura UK senza IVA

> Importato da ChatGPT export · 4 messaggi · gpt-5-1 · 2025-11-17

## 🧑 User

fer fattura ad azienda uk senza partita iva cosa posso inserire?

---

## 🤖 Assistant

Se fatturi a un’azienda UK **che non ha VAT number**, la questione è semplice: **emettere una normale fattura italiana in regime forfettario**, trattandola come **cliente privato estero**.

Di fatto, l’assenza di VAT UK significa che **non puoi applicare il reverse charge**. Quindi:

## 1. Dati fiscali del cliente
Nella sezione “Cliente” inserisci:
- Ragione sociale
- Indirizzo completo (via, città, CAP, Paese)
- Company number (se esiste; non è obbligatorio)
- Indica esplicitamente:
**“Cliente privo di VAT number nel Regno Unito”**

## 2. Cosa NON inserire
- Nessuna VAT UK
- Nessun reverse charge
- Nessuna dicitura intracomunitaria (perché *non* è un soggetto IVA)

## 3. IVA in fattura
Regime forfettario = **IVA non applicata**.

Inserisci la dicitura obbligatoria:
**“Operazione senza applicazione dell’IVA ai sensi dell’art. 1, commi 54–89, L. 190/2014 – regime forfetario.”**

## 4. Natura dell’operazione
Su Fatture in Cloud:
- Natura N2.2 o “Operazioni non soggette – regime forfettario”.

## 5. Ritenute / altre voci
- Nessuna ritenuta
- Nessuna marca da bollo (fattura elettronica non obbligatoria verso estero, ma se superi 77,47 euro devi comunque apporre **bollo virtuale da 2 euro**)

## 6. Pagamento
Indica metodo e coordinate (es. IBAN italiano, o conto UK se vuoi).

## 7. Note consigliate
Puoi aggiungere una nota che chiarisce la natura dell’operazione verso soggetto estero non IVA:
**“Cliente estero privo di partita IVA. Operazione equiparata a prestazione verso privato estero.”**

---

### In breve
Trattala come prestazione di servizi verso privato UK:
**niente IVA, niente reverse charge, dicitura forfettario e bollo se > 77,47.**

Se vuoi, ti preparo la fattura già impostata per Fatture in Cloud.

---

## 🧑 User

nella dicitura partita iva cosa posso inserire se è obbligatorio?

---

## 🤖 Assistant

Se il campo “Partita IVA / VAT number” è obbligatorio nel gestionale, hai due opzioni corrette e formalmente accettate:

## Opzione migliore
**Inserisci una dicitura esplicita:**
- **“N/A – cliente estero privo di VAT”**
oppure
- **“NO VAT – non registered”**

È la soluzione standard quando il cliente non è soggetto IVA.

## Alternativa (se il software non accetta lettere)
Alcuni gestionali obbligano caratteri numerici. In quel caso usa:
- **“00000000000”**
+ Aggiungi nelle note della fattura:
**“Cliente estero privo di VAT number. Operazione verso soggetto non IVA.”**

Questa è una prassi corretta, usata anche dagli studi commerciali quando i software richiedono un campo formalmente compilato.

---

Se mi dici che software usi (Fatture in Cloud o altro), ti dico esattamente cosa mettere nel campo specifico per evitare errori.