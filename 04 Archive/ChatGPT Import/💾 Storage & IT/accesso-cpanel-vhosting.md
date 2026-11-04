---
title: "Accesso cPanel VHosting"
created: 2025-07-15
updated: 2025-07-15
model: gpt-4o
messages: 10
source: chatgpt-import
tags: [storage-it]
category: "💾 Storage & IT"
---

# Accesso cPanel VHosting

> Importato da ChatGPT export · 10 messaggi · gpt-4o · 2025-07-15

## 🧑 User

dove trovo il cpanel di vhosting?

---

## 🤖 Assistant

Per accedere al **cPanel di VHosting**, segui uno di questi metodi:

---

### ✅ **Metodo 1: Da email di attivazione**
Quando hai acquistato il tuo piano su VHosting, ti avranno inviato una **mail con oggetto tipo**:
> “Dati di accesso al tuo cPanel”

In quella mail trovi:
- **Link al cPanel** (es: `https://nomeserver.vhosting-it.com:2083`)
- **Username**
- **Password**

---

### ✅ **Metodo 2: Dal pannello clienti VHosting**
1. Vai su: [https://www.vhosting-it.com/clientarea.php](https://www.vhosting-it.com/clientarea.php)
2. Fai login con le tue credenziali.
3. Clicca su **“I miei servizi”** (o "Servizi attivi").
4. Seleziona il piano hosting attivo.
5. Troverai il pulsante **“Login to cPanel”** o **“Accesso al cPanel”**.

---

### ✅ **Metodo 3: Accesso diretto con dominio**
Se il tuo dominio è attivo e punta correttamente, puoi provare:
- `https://iltuodominio.com/cpanel`
- oppure `https://iltuodominio.com:2083`

⚠️ Attenzione: funzionano solo **se il dominio è già puntato ai DNS di VHosting**.

---

Hai bisogno che ti aiuti a trovare il link corretto o a recuperarne l'accesso? Se mi dici il dominio, posso darti una mano mirata.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Grazie per lo screenshot! Quello che hai aperto è il pannello di gestione **del dominio** su VHosting, **non ancora il cPanel del sito web**.

Per accedere al **cPanel vero e proprio**, segui questi passaggi:

---

### 🔹 **Dal Pannello Clienti VHosting (Area Clienti)**
1. Torna nella **dashboard principale** del tuo account VHosting:
👉 [https://www.vhosting-it.com/clientarea.php](https://www.vhosting-it.com/clientarea.php)

2. Vai nella sezione **"I miei servizi"** o **"Servizi attivi"** (non “Domini”).

3. Clicca sul **piano di hosting** associato al dominio `foreversnowtrips.com`.

4. All'interno della scheda del servizio hosting, dovresti vedere il pulsante:
🔵 **"Login to cPanel"** oppure **"Accedi al cPanel"**
Cliccandolo, verrai reindirizzato al cPanel senza bisogno di inserire username o password.

---

### 🔹 **Accesso diretto (se configurato)**

Puoi anche provare uno di questi indirizzi nel browser:
- `https://foreversnowtrips.com/cpanel`
- oppure `https://foreversnowtrips.com:2083`

> ⚠️ Funziona **solo se il dominio punta già correttamente al server VHosting** e l’hosting è attivo.

---

Se vuoi, puoi mandarmi uno screenshot della sezione **“Servizi”**, così ti indico esattamente dove cliccare.

---

## 🧑 User

dove trovo lo zone editor?

---

## 🤖 Assistant

Ottima domanda!

### 🔍 **Lo "Zone Editor" si trova nel cPanel**, **non** nel pannello domini che hai mostrato nello screenshot.
Ecco come arrivarci passo per passo:

---

## ✅ **Guida rapida per trovare lo Zone Editor su VHosting**

### 🔹 1. **Accedi al cPanel**
Segui uno di questi due metodi:

#### 🔸 Metodo 1 – Dall’area clienti VHosting
1. Vai su: [https://www.vhosting-it.com/clientarea.php](https://www.vhosting-it.com/clientarea.php)
2. Entra in **"I miei servizi"**
3. Clicca sul servizio di hosting associato a `foreversnowtrips.com`
4. Premi il bottone **“Accedi al cPanel”**

#### 🔸 Metodo 2 – Link diretto (se già configurato)
Vai su:
`https://foreversnowtrips.com/cpanel`
(o `https://serverXXX.vhosting-it.com:2083` se conosci l'hostname)

Inserisci username e password del cPanel (sono diversi da quelli dell’area clienti, a meno che tu non usi l’accesso automatico).

---

### 🔹 2. **Trova lo Zone Editor**
Una volta dentro il cPanel:

- Scrivi **"Zone Editor"** nella barra di ricerca in alto
🔍 oppure
- Scorri fino alla sezione **"Domini"**
→ Clicca su **“Zone Editor”**

---

### 🔧 Cosa puoi fare nello Zone Editor?
- Aggiungere o modificare record **A**, **CNAME**, **MX**, **TXT**, ecc.
- Gestire i puntamenti DNS (es. per email, sottodomini, verifica Google Search Console, ecc.)

---

Se vuoi, posso aiutarti anche a configurare un record specifico (es. per collegare un servizio esterno o impostare un sottodominio). Ti basta dirmi cosa vuoi ottenere.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

devo proprio aggiungere un cname ma non trovo lo zone editor

---

## 🤖 Assistant

Perfetto, grazie per l'immagine: conferma che il tuo dominio **usa i nameserver di VHosting**, quindi **devi gestire i record DNS dal cPanel**, nella sezione **Zone Editor > Gestione**, come ti hanno scritto.

---

## 🔍 **Ecco dove trovare lo Zone Editor passo per passo**

### ✅ **1. Entra nel cPanel (non nel pannello clienti dominio)**
Segui questi passaggi:

1. Vai su [https://www.vhosting-it.com/clientarea.php](https://www.vhosting-it.com/clientarea.php)
2. Vai su **Servizi > I miei servizi**
3. Clicca sul tuo piano di hosting (non sul dominio)
4. Premi **"Login al cPanel"**

---

### ✅ **2. Dentro al cPanel: cerca “Zone Editor”**
Una volta dentro al cPanel:
- Usa la barra di ricerca in alto e scrivi **“Zone Editor”**
- Oppure scorri fino alla sezione **“Domini”**
→ Clicca su **Zone Editor**

---

### ✅ **3. Aggiungi il record CNAME**
1. Trova il tuo dominio (`foreversnowtrips.com`)
2. Clicca su **“Gestione”** accanto al dominio
3. In alto a destra premi **“+ Aggiungi Record”**
4. Scegli **CNAME**
5. Compila i campi:
- **Nome**: es. `www` (o il sottodominio desiderato)
- **CNAME**: es. `g.page/tuonome` oppure `example.target.com.`
6. Salva.

> ⚠️ **Attenzione al punto finale** nel campo destinazione (`example.com.`). Alcuni pannelli lo richiedono, altri no. Se hai dubbi, scrivimi il valore esatto che vuoi inserire.

---

### ❓Serve una mano a compilare i campi del CNAME?
Mandami esattamente:
- Il sottodominio che vuoi creare (es: `mail.foreversnowtrips.com`)
- Il valore del CNAME da puntare

…e ti dico io cosa scrivere, campo per campo.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

nella ricerca non lo trova

---

## 🤖 Assistant

Grazie per lo screenshot: ora è tutto chiaro!

👉 **Non sei dentro il cPanel classico**, ma stai usando **DirectAdmin**, il pannello alternativo che VHosting usa in alcuni server.

Nel tuo caso, per aggiungere un record CNAME devi seguire questo percorso specifico per **DirectAdmin**, non per cPanel.

---

## ✅ **Guida per aggiungere un record CNAME in DirectAdmin**

1. Torna nella **dashboard principale** (dal menu a sinistra, clicca su 🏠 "Home" o su "Dashboard")
2. Vai in **“Account Manager” > “DNS Management”**
(oppure “Gestione DNS”, se la lingua è in italiano)

3. Vedrai una lista di record DNS (A, MX, CNAME, TXT ecc.)
4. Premi **“Add Record”** (o "Aggiungi Record")
5. Seleziona tipo **CNAME**
6. Compila i campi:
- **Name** → es. `www` (o il sottodominio che vuoi creare)
- **Value** → il dominio di destinazione (es: `example.target.com.`)
7. Salva

---

## ⚠️ Attenzione
- Non inserire il dominio completo nel campo *Name* se vuoi aggiungere un CNAME per `www`, basta scrivere `www`.
- Il valore *Value* **va con il punto finale (`.`)** solo se richiesto. Se hai dubbi, scrivimi il CNAME che vuoi impostare.

---

## 🧭 Se non trovi “DNS Management”:
- Prova a scrivere **“dns”** nel campo **"Search for pages"** (barra azzurra in alto)
- Oppure controlla in:
- **Account Manager**
- **Advanced Features**

---

Se vuoi, puoi dirmi:
- Esattamente **che record CNAME** vuoi aggiungere (es: `verify.brand.com -> your.app.link`)
- E ti dico **esattamente** come compilarlo nel tuo pannello.