---
title: "Ripristino accesso Gmail"
created: 2025-10-28
updated: 2025-10-28
model: gpt-5
messages: 10
source: chatgpt-import
tags: [fotografia-video, storage-it]
category: "💾 Storage & IT"
---

# Ripristino accesso Gmail

> Importato da ChatGPT export · 10 messaggi · gpt-5 · 2025-10-28

## 🧑 User

ho dovuto aggiornare la password del mio account gmail e ora non mi si connette ne su mail del mac ne dall'iphone

---

## 🤖 Assistant

Ok. Ti spiego in modo chiaro e diretto come risolvere.

Quando aggiorni la password del tuo account Gmail, **tutti i dispositivi collegati con le vecchie credenziali perdono l’accesso**. Per ripristinarlo devi **rimuovere e reinserire l’account** oppure **reinserire la password manualmente**, a seconda dei casi.

### Procedura su Mac (app Mail)
1. Apri **Preferenze di Sistema** → **Internet Account**.
2. Seleziona l’account **Gmail** che non funziona.
3. Ti chiederà di **reinserire la password** o di **“Ricollegare l’account”**.
- Se compare il pulsante “Apri pagina di Google per aggiornare”, cliccalo e accedi con la nuova password.
- Se invece non te lo chiede, **rimuovi completamente l’account Gmail** e aggiungilo di nuovo:
- Clicca il segno “–” per eliminarlo.
- Poi clicca “+” → Google → accedi con la nuova password.

### Procedura su iPhone
1. Vai su **Impostazioni** → **Mail** → **Account**.
2. Tocca il tuo **account Gmail**.
3. Se compare l’opzione per **aggiornare o reinserire la password**, fallo.
- In caso contrario, disattiva e **rimuovi l’account**, poi aggiungilo da zero:
- “Aggiungi account” → Google → accedi con la nuova password.

### Attenzione:
- Se hai **verifica in due passaggi attiva**, assicurati di inserire il **codice di sicurezza** quando richiesto.
- Se usi un’app “meno sicura” o un vecchio client di posta, potresti dover creare una **password per l’app** da [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

Fammi sapere se ti dà un errore preciso (tipo “autenticazione non riuscita” o “impossibile verificare account”), così ti dico esattamente dove intervenire. Vuoi che ti guidi nella sequenza corretta per uno dei due dispositivi prima — Mac o iPhone?

---

## 🧑 User

in nessuna delle due opzioni mi chiede di aggiornare la password

---

## 🤖 Assistant

Perfetto, allora significa che Mail e iOS stanno ancora tentando di autenticarsi con le **vecchie credenziali memorizzate nel portachiavi** e non riescono a forzare l’aggiornamento. Ti spiego come risolvere in modo pulito.

---

## 🔧 MAC – procedura completa
1. **Chiudi Mail.**
2. Apri **Preferenze di Sistema → Internet Account.**
3. Seleziona l’account **Gmail** e clicca **“–”** per rimuoverlo completamente.
4. Apri **Accesso Portachiavi (Keychain Access)** → cerca “Google” o “Gmail”.
- Elimina eventuali **voci di password Gmail obsolete** (es. `accounts.google.com`, `smtp.gmail.com`, `imap.gmail.com`).
5. Torna in **Internet Account → + → Google** e aggiungi di nuovo il tuo account.
- Si aprirà la finestra di login ufficiale di Google.
- Inserisci la **nuova password** e autorizza l’accesso.
6. Riavvia Mail.
Ora le email dovrebbero sincronizzarsi senza errori.

---

## 📱 IPHONE – procedura completa
1. Vai su **Impostazioni → Mail → Account.**
2. Tocca l’account Gmail e poi **Elimina account.**
3. Vai su **Impostazioni → Generali → VPN e gestione dispositivo → Gestione password e account** (oppure usa la ricerca “Password” nelle Impostazioni).
- Rimuovi eventuali **password Gmail memorizzate** se presenti.
4. Torna su **Impostazioni → Mail → Aggiungi account → Google.**
- Inserisci l’email, poi la **nuova password.**
- Accetta le autorizzazioni.

---

Dopo questi passaggi, sia Mac che iPhone useranno il token di accesso nuovo e il login tornerà operativo.

---

Se dopo aver rifatto tutto ti appare un messaggio tipo **“Impossibile verificare nome utente o password”**, allora devi probabilmente creare una **password per app** (succede se hai l’autenticazione a due fattori attiva e usi Mail anziché l’app Gmail).
Vuoi che ti spieghi come generarla passo per passo?

---

## 🧑 User

non posso rimuoverlo. è un account di lavoro con un sacco di dati sensibili

---

## 🤖 Assistant

Capito. Allora **non rimuoverlo**: ti spiego la procedura **sicura** per aggiornare l’autenticazione senza eliminare l’account né perdere dati.

---

### 🔹 Obiettivo
Forzare Mail e iOS a chiedere di nuovo l’accesso, **senza cancellare nulla**.
L’operazione aggiorna il token di Google mantenendo tutti i dati locali e remoti intatti.

---

## 💻 MAC

1. **Chiudi Mail.**
2. Apri **Preferenze di Sistema → Internet Account.**
3. Seleziona il tuo **account Gmail**.
4. **Disattiva temporaneamente tutte le spunte** (Mail, Contatti, Calendari, ecc.).
- Attendi 30–60 secondi.
5. **Riattiva le spunte** (soprattutto Mail).
- In molti casi ti apparirà una finestra di Google che dice “Accedi per continuare”.
- Inserisci la **nuova password** e completa l’autenticazione (anche con eventuale codice 2FA).

Se non compare ancora la finestra di login:

6. Apri **Accesso Portachiavi (Keychain Access)**.
- Cerca “google” o “accounts.google.com”.
- **Elimina solo** la voce di tipo *Password Internet* relativa a `accounts.google.com` (non altre).
7. Riapri Mail → ti chiederà di nuovo l’autenticazione Google.
- Inserisci la **nuova password**.

Questo aggiorna il token senza rimuovere l’account né i dati sincronizzati.

---

## 📱 IPHONE / IPAD

1. Vai su **Impostazioni → Mail → Account → [tuo account Gmail]**.
2. **Disattiva Mail** (togli la spunta).
3. Aspetta 30 secondi, poi **riattiva Mail**.
- Se serve, ti riporta automaticamente alla finestra di login Google.
4. Inserisci la **nuova password**.

Se ancora non appare la richiesta:

5. Vai su **Impostazioni → Password** (usa la ricerca “Password”).
6. Cerca “google” o “accounts.google.com” e **rimuovi solo la password obsoleta**.
7. Torna in **Mail → Account → Gmail** e riattiva Mail: ti richiederà l’accesso con la nuova password.

---

In nessuno di questi passaggi vengono toccati o cancellati i messaggi, contatti o calendari: restano sincronizzati via server Google.

---

Se dopo tutto questo **non compare ancora la finestra di login** sul Mac, posso indicarti il comando terminale che forza macOS a invalidare il token OAuth specifico per Gmail (è reversibile e sicuro).
Vuoi che ti mostri anche quello?

---

## 🧑 User

dov'è internet account? non lo trovo in preferenze di sistema

---

## 🤖 Assistant

Perfetto, ti spiego dove trovarlo in base alla **versione di macOS** — Apple ha cambiato il nome e la posizione più volte.

---

### 🔹 Se hai **macOS Ventura, Sonoma o successivo (versioni recenti)**
1. Apri **Impostazioni di Sistema** (l’icona dell’ingranaggio).
2. Nel menù laterale, scorri fino a **“Internet Account”** (è nella sezione **“Utenti e Account”** o più in basso, sotto “Password e account” a seconda della versione).
3. Clicca sul tuo account **Google**: da lì puoi **disattivare/riattivare Mail** o forzare l’accesso.

👉 In alternativa, puoi cercarlo direttamente scrivendo **“Internet Account”** nella barra di ricerca in alto dell’app Impostazioni di Sistema.

---

### 🔹 Se hai **macOS Monterey o precedenti**
1. Apri **Preferenze di Sistema**.
2. Clicca sull’icona **“Internet Account”** (dovrebbe essere una sfera azzurra con il simbolo @).
3. Troverai lì tutti gli account configurati (Google, iCloud, Exchange, ecc.).

---

Se mi dici **che versione di macOS** hai (es. Sonoma, Ventura, Monterey...), ti indico il percorso preciso con i nomi esatti dei menù.
Vuoi che te lo specifichi subito per la tua versione?

---

## 🧑 User

e sull'iphone?

---

## 🤖 Assistant

Su iPhone dipende anche lì dalla versione di iOS, ma ti indico i due percorsi possibili:

---

### 🔹 iOS 16 / 17 / 18 (i più recenti)
1. Apri **Impostazioni**.
2. Scorri e tocca **Mail**.
3. Tocca **Account**.
4. Vedrai l’elenco dei tuoi account di posta.
- Seleziona quello **Gmail**.
- Qui puoi **disattivare e riattivare Mail** o **toccare “Riconnetti account”** se compare.
- Se non appare nulla, prosegui con il passaggio sotto.

#### Per forzare il nuovo login:
5. Vai in **Impostazioni → Password** (puoi anche scriverlo nella barra di ricerca in alto).
6. Cerca “google” o “accounts.google.com”.
- Elimina la password salvata associata.
7. Torna in **Impostazioni → Mail → Account → Gmail**.
- Riattiva Mail: a questo punto iOS ti porterà sulla pagina ufficiale di **Google** per reinserire la password aggiornata.

---

### 🔹 Versioni precedenti di iOS (fino a iOS 15)
Il percorso è quasi identico, ma il menù può chiamarsi **“Password e account”** invece di “Mail → Account”.
Quindi:
**Impostazioni → Password e account → Gmail → reinserisci password o disattiva/riattiva Mail.**

---

Tutti questi passaggi **non cancellano né email né impostazioni**, servono solo a far ripartire l’autenticazione con la nuova password.

Vuoi che ti dica anche come verificare se l’iPhone sta davvero provando a connettersi con la password aggiornata (tramite le impostazioni avanzate di Mail)?