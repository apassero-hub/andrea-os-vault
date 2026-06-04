---
title: "Importare file mbox su Workspace"
created: 2025-08-01
updated: 2025-08-01
model: gpt-4o
messages: 4
source: chatgpt-import
tags: []
---

# Importare file mbox su Workspace

> Importato da ChatGPT export · 4 messaggi · gpt-4o · 2025-08-01

## 🧑 User

come posso importare un file mbox expord da mail aruba su workspace

---

## 🤖 Assistant

Per importare un file **MBOX esportato da Aruba Mail** (o qualunque client che supporti MBOX, come Thunderbird) su **Google Workspace (Gmail)**, Google **non fornisce un sistema diretto** per importare file `.mbox` in Gmail. Tuttavia, puoi farlo **in due fasi**, utilizzando **Thunderbird** come strumento intermedio. Ecco come:

---

## ✅ **Procedura passo-passo per importare un file `.mbox` in Gmail/Workspace:**

### 🔧 **FASE 1: Preparazione**

1. **Installa Thunderbird** (se non l’hai già):
- [Scaricalo da qui](https://www.thunderbird.net/it/)

2. **Aggiungi il tuo account Gmail su Thunderbird**:
- Apri Thunderbird → `Strumenti` > `Impostazioni account` > `Aggiungi account di posta`
- Inserisci le credenziali Gmail (account Workspace).
- Thunderbird configurerà in automatico IMAP.

3. **Scarica il componente aggiuntivo "ImportExportTools NG"**:
- Vai su: `Strumenti` > `Componenti aggiuntivi e temi`
- Cerca **ImportExportTools NG**, installalo, riavvia Thunderbird.

---

### 📥 **FASE 2: Importazione del file `.mbox`**

1. **Crea una cartella locale in Thunderbird**:
- Tasto destro su "Cartelle locali" → `Nuova cartella` → chiamala ad esempio "Import Aruba"

2. **Importa il file `.mbox`**:
- Tasto destro sulla nuova cartella → `ImportExportTools NG` > `Importa file mbox` > Seleziona il tuo file esportato da Aruba

3. **Controlla che i messaggi siano visibili nella cartella "Import Aruba"**

---

### ☁️ **FASE 3: Copia su Gmail (IMAP)**

1. **Dal pannello sinistro di Thunderbird**, trascina o copia (Ctrl+C > Ctrl+V) le email dalla cartella "Import Aruba" a una **cartella del tuo account Gmail** (es. `Archivio`, `Vecchie Mail Aruba`, etc.)

2. **Aspetta il completamento della sincronizzazione**: le email verranno caricate sul server di Google Workspace tramite IMAP (potrebbero volerci ore se ci sono molte email o allegati pesanti).

---

## 📝 **Note importanti**

- Il file MBOX **deve essere integro**: se è corrotto, Thunderbird potrebbe non leggerlo.
- Gmail ha un **limite giornaliero di upload IMAP** (circa 2–2.5 GB/giorno).
- Le mail così importate saranno **ricercabili e accessibili come tutte le altre** su Gmail/Workspace.

---

Se vuoi automatizzare questo processo per molti account (es. in una migrazione aziendale), esistono strumenti a pagamento (come **CloudM**, **Transend**, **SysTools**), oppure puoi configurare il **Data Migration Service di Google** *solo se hai accesso IMAP al vecchio account*, non da file MBOX.

---

Se vuoi ti posso preparare un PDF o checklist per seguirla passo passo. Vuoi?

---

## 🧑 User

e se uso mail del mac posso farloi?

---

## 🤖 Assistant

Sì, puoi farlo anche usando **Apple Mail (Mail su macOS)**, ma **non puoi importare direttamente un file `.mbox` in Gmail/Workspace via Mail**. Tuttavia, puoi **usare Mail come ponte**, proprio come con Thunderbird. Ti spiego come fare passo passo:

---

## ✅ **Importare MBOX su Gmail usando Mail (macOS)**

### 🔧 **FASE 1: Importa il file MBOX in Mail**

1. **Apri l'app Mail su macOS**
2. Vai in alto su `File` → `Importa caselle di posta`
3. Seleziona **Formato: file in formato Apple Mail o MBOX** → clicca su **Continua**
4. Naviga fino al tuo file `.mbox` esportato da Aruba → selezionalo → clicca su **Scegli**
5. Verrà importato in una nuova sezione chiamata **Importazione**

---

### ☁️ **FASE 2: Copia le email su Gmail (via IMAP)**

1. Assicurati di avere configurato **il tuo account Gmail Workspace** nell’app Mail (Impostazioni > Account > Aggiungi Gmail, in modalità IMAP)
2. Nella colonna laterale di Mail vedrai sia:
- La cartella "Importazione" con le mail Aruba
- L’account Gmail con tutte le cartelle

3. **Copia o trascina le email importate** (o l’intera casella) dalla sezione "Importazione" a una cartella del tuo account Gmail, ad esempio:
- `Archivio Aruba`
- `Vecchie mail importate`
4. Aspetta la sincronizzazione: le email verranno **caricate sul server Gmail**.

---

### 🔁 **Sincronizzazione & tempo**

- Questo metodo **funziona bene anche con grandi volumi**, ma può impiegare diverse ore.
- Ti consiglio di **verificare su Gmail via browser** (mail.google.com) se le email stanno comparendo.
- Puoi **fare più importazioni a blocchi** se hai più file `.mbox`.

---

## 📌 Vantaggi di usare Apple Mail:

- Interfaccia familiare per utenti Mac
- Integrazione diretta con Gmail via IMAP
- Non servono tool esterni (come con Thunderbird)

---

Se vuoi, posso fornirti una checklist stampabile o una mini guida in PDF. Ti serve?