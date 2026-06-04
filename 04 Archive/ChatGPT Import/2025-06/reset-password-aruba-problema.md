---
title: "Reset password Aruba problema"
created: 2025-06-13
updated: 2025-06-13
model: gpt-4o
messages: 6
source: chatgpt-import
tags: []
---

# Reset password Aruba problema

> Importato da ChatGPT export · 6 messaggi · gpt-4o · 2025-06-13

## 🧑 User

Allora, mi è successa una roba strana. L'altro giorno che abbiamo avuto quei problemi con il tipo del web, ho fatto l'accesso sul portale, sulla piattaforma di Aruba, e ho cambiato la password, per essere più tranquilli, per Lost. Non so come lui è riuscito a ricambiarla. Per fortuna la situazione si è un po' appianata, naturalmente non è un grosso problema, però per me è un problema il non riuscire a capire come lui abbia fatto a fare un reset della password e mettere una password nuova.

---

## 🤖 Assistant

La situazione che descrivi è delicata e **va chiarita immediatamente** per evitare problemi di sicurezza futuri. Ti elenco le ipotesi più probabili su come quella persona sia riuscita a reimpostare la password anche dopo il tuo cambio:

---

### 🔐 **1. Ha ancora accesso all’email amministrativa**
Se l'email associata all'account Aruba è **una casella che lui controlla o ha controllato in passato**, potrebbe aver semplicemente avviato una procedura di "password dimenticata" e poi cliccato sul link di reset.

👉 **Verifica immediatamente** a quale indirizzo email Aruba invia i reset password e **modifica quella email** se non è sotto il tuo controllo esclusivo.

---

### 🔄 **2. Ha accesso come utente secondario o tecnico**
Aruba permette di creare **utenze tecniche** o deleghe (es. per sviluppatori) che possono accedere in autonomia al pannello o a sezioni specifiche.

👉 Accedi al **pannello Aruba > Gestione utenze** e controlla se ci sono utenti secondari attivi. Se sì, **revoca l'accesso**.

---

### 🛠️ **3. Ha registrato in passato l’account a suo nome**
Se l’account Aruba (non solo il dominio) è stato **inizialmente creato da lui con le sue credenziali o dati personali**, potrebbe avere ancora **controllo legale** sull’account.

👉 Controlla **intestazione dell’account Aruba**, compresi:
- nome del titolare del contratto
- codice cliente
- dati fiscali

Se non siete voi, va richiesta **una variazione intestazione** ad Aruba con PEC e/o documentazione.

---

### 🧠 **4. Hai fatto logout ma ha ancora sessioni attive**
Se lui aveva fatto login in passato e **non si è mai disconnesso** (es. da browser o password manager), potrebbe aver avuto modo di accedere anche dopo il cambio password, **fino alla scadenza della sessione**.

👉 Forza un **logout globale** da tutte le sessioni attive, se Aruba lo consente (controlla nelle impostazioni di sicurezza).

---

### 📞 COSA FARE ADESSO

1. **Cambia nuovamente la password**, scegliendone una lunga e complessa.
2. **Modifica l'email associata** all'account (solo se ne hai il controllo).
3. **Controlla e revoca eventuali accessi secondari.**
4. **Contatta Aruba (via ticket o call center)** e chiedi:
- a chi è intestato l'account
- se risultano modifiche o reset password non da parte tua
- se ci sono IP di accesso sospetti
5. Se necessario, **chiedi la sostituzione del contatto amministrativo e tecnico** del dominio.

---

Se vuoi, posso aiutarti a scrivere una mail formale ad Aruba o al supporto tecnico, oppure verificare con te le schermate nel pannello per controllare accessi e intestazioni. Fammi sapere.

---

## 🧑 User

Non trovo la gestione utenze

---

## 🤖 Assistant

Hai ragione: **nel pannello Aruba per utenti standard (es. domini e hosting condivisi)** *non esiste una sezione chiamata “Gestione Utenze”* nel senso classico di account multipli, come su Google Workspace o Office 365.

Aruba gestisce l’**accesso tramite una singola utenza principale associata a un codice cliente**, e non consente la creazione di account secondari direttamente dal pannello. Tuttavia, ci sono **altri punti critici dove può annidarsi l’accesso esterno**.

---

### 🎯 **Ecco dove controllare e cosa fare:**

---

#### ✅ **1. Verifica i dati del titolare**
Vai su:
👉 **[https://admin.aruba.it](https://admin.aruba.it)**
Accedi e poi:
**Area Clienti > Dati Intestatario Contratto**
Verifica **nome, cognome / ragione sociale, codice fiscale / partita IVA**.

Se compare il nome del web designer o una ditta sua:
📌 **Devi chiedere il cambio di intestazione**, perché *di fatto non siete proprietari dell’account*. Posso aiutarti a scrivere la richiesta.

---

#### ✅ **2. Verifica e cambia l’email di recupero**
Vai su:
**Area Clienti > Gestione Account > Modifica Dati Anagrafici / Email di Contatto**
Assicurati che:
- **email principale**
- **email per recupero password**
- siano **sotto il tuo controllo esclusivo** (no Gmail condivise o vecchi indirizzi).

---

#### ✅ **3. Controlla il pannello del dominio (separato)**
Se sei su un hosting condiviso (es. con dominio e spazio web), entra anche in:
👉 **[https://managehosting.aruba.it](https://managehosting.aruba.it)**
Da qui puoi:
- vedere **configurazioni tecniche**
- accedere a **webmail e caselle PEC**
- cambiare **record DNS, accessi FTP, database**, ecc.

📌 **Cambia tutte le password tecniche** (FTP, MySQL, accesso CMS tipo WordPress) se sospetti che le conosca ancora.

---

#### ✅ **4. Reimposta la password e forzane la validità**
Quando cambi la password principale da [admin.aruba.it](https://admin.aruba.it), **quella nuova sostituisce quella vecchia immediatamente**. Ma se chiunque può ancora richiederne una nuova, il problema resta.

💡 **Soluzione**:
- cambia password con una **molto lunga e casuale** (es. con un generatore tipo Bitwarden o 1Password)
- **modifica subito anche la mail** collegata
- attiva (se possibile) **l'autenticazione a due fattori (2FA)**: Aruba la offre per alcuni pannelli

---

#### ⚠️ Se nulla torna, contatta Aruba

Nel tuo caso, la priorità è capire **come sia stato possibile fare un reset della password**.

📩 Ti consiglio di inviare subito un ticket all’assistenza con questa richiesta (se vuoi, posso scriverti il testo). Chiedi:

- Da quale IP è stata fatta la modifica password
- Quale email ha ricevuto il link di reset
- Se risultano accessi o sessioni aperte da dispositivi non riconosciuti

---

Fammi sapere se vuoi:
- una **mail già pronta da inviare al supporto Aruba**
- un check insieme via screenshot o videochiamata per esaminare il pannello

Posso anche aiutarti a **fare un backup di tutto** e valutare **un cambio host** se la fiducia è compromessa.

---

## 🧑 User

Ma prima mi è consigliato di andare a vedere in un punto della gestione utenze che però non riesco a trovare, mi riesce a guidare per capire dove andare a parare.

---

## 🤖 Assistant

Hai ragione a chiedere chiarezza: ti guido passo passo **sulla piattaforma di Aruba**, tenendo conto che *non esiste una vera "gestione utenze" per account multipli*, ma ci sono **alcune sezioni dove possono essere salvate informazioni di accesso, email di recupero e deleghe tecniche**.

Ecco **dove andare esattamente**, in base a cosa vuoi controllare:

---

### ✅ **1. Controllare a chi è intestato l’account Aruba**

Vai su:
👉 [https://admin.aruba.it](https://admin.aruba.it)

- Effettua il login
- In alto a destra clicca su **"Area Clienti"**
- Vai su **"Gestione dati anagrafici"**
- Clicca su **"Dati intestatario contratto"**

📌 Qui vedrai **nome, cognome, codice fiscale / P.IVA** dell’intestatario. Se è il web designer, il contratto Aruba è ancora intestato a lui.

---

### ✅ **2. Verificare e cambiare email associata all’account (usata per reset password)**

Sempre da [https://admin.aruba.it](https://admin.aruba.it):

- Vai su **"Area Clienti"**
- Poi su **"Gestione account"**
- Clicca su **"Modifica Email/Cellulare"**

📌 Qui puoi vedere e modificare l’**email principale** usata per ricevere i link di reset password. **Se è un indirizzo che lui ha gestito in passato, va cambiato subito.**

---

### ✅ **3. Verificare contatti associati al dominio (admin / tecnico / fatturazione)**

Vai su:
👉 [https://managehosting.aruba.it](https://managehosting.aruba.it)

- Accedi con le tue credenziali
- Seleziona il **dominio in questione** (es: `tuodominio.it`)
- Vai nel menu laterale su **"Contatti associati"**

📌 Qui Aruba mostra i contatti per:
- **Contatto amministrativo**
- **Contatto tecnico**
- **Contatto per la fatturazione**

Se **il contatto tecnico è ancora lui**, potrebbe avere **accesso da pannelli esterni (es. DNS, FTP, ecc.)** anche se tu hai cambiato la password dell'area clienti. **Revoca o sostituisci quei dati.**

---

### ✅ **4. Cambiare tutte le password tecniche (FTP, MySQL, email)**

Sempre da **[managehosting.aruba.it](https://managehosting.aruba.it)**, entra nella sezione relativa al tuo dominio e poi:

- Vai su **Gestione FTP/MySQL > Cambia password**
- Vai su **Gestione caselle email > Cambia password**
- Vai su **CMS (es. WordPress) > cambia accessi admin**

---

### In sintesi, quello che Aruba chiama "gestione utenze" non è un sistema con ruoli multipli come su Google Workspace o Microsoft 365. È **un insieme di dati anagrafici e tecnici** da cui possono **dipendere accessi indesiderati se non aggiornati.**

---

Se vuoi, posso:
- scriverti un elenco azioni da fare in ordine cronologico
- aiutarti a verificare uno per uno questi punti con screenshot
- redigere la mail da inviare al supporto Aruba per segnalare l’accaduto

Fammi sapere come preferisci procedere.