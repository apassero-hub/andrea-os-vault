---
title: "Configurare IMAP su Mail"
created: 2025-08-20
updated: 2025-08-20
model: gpt-5
messages: 28
source: chatgpt-import
tags: [sito-web]
category: "🌐 Sito & Web"
---

# Configurare IMAP su Mail

> Importato da ChatGPT export · 28 messaggi · gpt-5 · 2025-08-20

## 🧑 User

ho dovuto ripristinare l'app mail del mac e poi ho recuperato facilmente tutte le mail dal sever quando le ho reimpostate. per la mia mail info@andreapasserini.com su hostinger invece non me le da più, presumo che dipenda dall'impostazione del server che una volta scaricate le cancella automaticamente. come faccio ad assicurarmi che questo non capiti più e che ne tenga copia?

---

## 🤖 Assistant

Quello che ti è successo dipende molto probabilmente dal **protocollo usato per configurare la casella di posta** su Mail (macOS):

- **POP3** → scarica i messaggi in locale e, salvo diversa impostazione, li elimina dal server dopo il download.
- **IMAP** → mantiene una copia sincronizzata sul server, quindi la posta rimane accessibile da più dispositivi (e non sparisce al ripristino).

Se con Hostinger la posta è sparita, significa quasi sicuramente che la casella era configurata in POP3.

### Come risolvere
1. **Controlla l’attuale configurazione**
- In Mail vai su `Mail > Impostazioni > Account > [info@andreapasserini.com]`.
- Vedi se è scritto **POP** o **IMAP** accanto al server in entrata.

2. **Passa a IMAP (consigliato)**
- Elimina l’account POP da Mail (attenzione: prima fai un backup delle mail che vuoi conservare).
- Aggiungi di nuovo l’account, ma questa volta scegli **IMAP**.
- I parametri Hostinger per IMAP sono solitamente:
- **Server IMAP**: `imap.hostinger.com`, Porta 993, SSL/TLS attivo.
- **Server SMTP**: `smtp.hostinger.com`, Porta 465 o 587, SSL/TLS attivo.

3. **Verifica lato server**
- Accedi al **pannello Hostinger → Email → Caselle di posta**.
- Controlla nelle impostazioni se c’è un’opzione relativa alla gestione POP (es. “conserva una copia sul server”). Se sì, abilitala.

4. **Da ora in poi**
- Tutte le mail rimarranno sempre sul server, accessibili via webmail e da qualsiasi altro dispositivo.
- Mail sul Mac non farà più da archivio unico ma solo da “specchio” (molto più sicuro).

Vuoi che ti scriva la procedura passo-passo per **migrare le mail già scaricate col POP** (quelle vecchie) in IMAP, così da non perderle e averle tutte sul server?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

ho controllato dalle impostazioni di mail, qui sul server non devo fare nulla?

---

## 🤖 Assistant

Ho visto lo screenshot: quella schermata è la **webmail di Hostinger** (Roundcube).
Qui ci sono solo opzioni di gestione interna dei messaggi (come vengono eliminati, svuotamento cestino, ecc.), ma **non c’è alcuna impostazione che impedisce la cancellazione dopo il download**: quella dipende dal **protocollo usato dal client (POP o IMAP)**.

Quindi:
- Sul server non devi fare nulla.
- Il punto cruciale è **riconfigurare l’account su Mail del Mac come IMAP**, non POP.

In pratica, se rimani in POP, anche se in webmail lasci tutto com’è, quando Mail scarica i messaggi può comunque cancellarli dal server (a seconda delle preferenze impostate in Mail). Con IMAP invece i messaggi rimangono sempre sul server e Mail si limita a sincronizzarli.

👉 Ti consiglio il passaggio a IMAP. Vuoi che ti scriva i passaggi esatti per:
1. Fare un backup delle mail POP già scaricate.
2. Eliminare l’account POP.
3. Riconfigurarlo come IMAP su Mail (con parametri Hostinger).
4. Rimettere dentro le vecchie mail così finiscono in IMAP e restano sul server?

---

## 🧑 User

fatto, non c'è modo di recuperare le vecchie mail?

---

## 🤖 Assistant

Se hai già **ricreato l’account come IMAP** e cancellato quello POP, le vecchie mail si possono recuperare **solo se erano ancora salvate in locale** sul Mac. Dipende da come hai eliminato l’account POP:

### 1. Caso fortunato: Mail locali ancora presenti
- In Mail, controlla nella barra laterale se vedi una sezione chiamata **“Sul mio Mac”** (o “On My Mac”).
- Se le mail erano state spostate lì (automaticamente o da te), allora ci sono ancora e basta trascinarle dentro la nuova casella IMAP (cartella Posta in arrivo o altre). Così tornano anche sul server.

### 2. Caso incerto: Mail eliminate con l’account
- Se quando hai eliminato l’account POP da Mail hai scelto **“Rimuovi anche i messaggi”**, allora il database di Mail li ha cancellati.
- In quel caso, puoi provare a recuperarli da un **backup di Time Machine** (se attivo) oppure recuperando manualmente il file mbox della casella POP.
- Percorso tipico:
```
~/Library/Mail/V10/POP-info@andreapasserini.com@imap.hostinger.com
```
(la cartella `V10` può cambiare in base alla versione di macOS, ad es. `V9`, `V11` ecc.)
- Dentro dovresti trovare file `.mbox` che contengono i messaggi. Questi si possono reimportare in Mail (`File > Importa caselle…`).

### 3. Caso perso: Nessun backup, account eliminato
- Se non hai Time Machine e non trovi più le cartelle `.mbox`, purtroppo quelle mail non sono più recuperabili.

---

Vuoi che ti scriva la procedura **per cercare nei file locali del Mac** se gli mbox delle mail POP sono ancora lì, così verifichi subito se hai una possibilità di recupero?

---

## 🧑 User

e se ce le ho tutte sul mail dell'iphone

---

## 🤖 Assistant

Ottima notizia: se sul tuo iPhone vedi ancora tutte le mail vecchie, vuol dire che **sono fisicamente memorizzate lì in locale** (anche se non più sul server).
A questo punto hai due strade per riportarle dentro al nuovo account IMAP (così tornano anche su Hostinger e sul Mac):

---

### 🔹 Metodo 1: Spostamento diretto dall’iPhone
1. Sul tuo iPhone assicurati che sia configurato **anche il nuovo account IMAP** (info@andreapasserini.com in modalità IMAP).
2. Apri l’app Mail e vai nella casella con i messaggi vecchi.
3. **Seleziona le mail o intere cartelle** → premi su “Sposta” → scegli una cartella del nuovo account IMAP (ad esempio “Posta in arrivo” o una cartella che crei apposta).
4. Il telefono le caricherà sul server Hostinger e si sincronizzeranno anche sul Mac.

⚠️ Limite: se hai migliaia di mail, dovrai farlo a blocchi (iOS non gestisce bene spostamenti massivi troppo grossi).

---

### 🔹 Metodo 2: Esportazione/backup tramite client desktop
Se vuoi fare la cosa più pulita:
1. Configura lo stesso account dell’iPhone (quello POP con i messaggi salvati) anche su un computer con un programma come **Thunderbird**.
2. Sincronizza tutto → così avrai una copia completa sul computer.
3. Poi aggiungi sullo stesso client anche il nuovo account IMAP.
4. Trascina le mail dal vecchio account POP al nuovo IMAP → il client le reinvia al server Hostinger.

---

### 🔹 Metodo 3: App di terze parti
Esistono app per iPhone che permettono di **esportare le mail in formato.mbox o.eml** (es. iMazing da Mac/PC). Da lì si possono reimportare su Mail del Mac e rispedirle al server.

---

👉 La soluzione più rapida e sicura è **Metodo 1: spostamento diretto dall’iPhone all’IMAP**.
Vuoi che ti scriva passo passo come farlo direttamente dall’app Mail su iOS, così provi subito?

---

## 🧑 User

ma con time machine posso ripristinare solo queste mail? o devo ripristinare tutto?

---

## 🤖 Assistant

Puoi ripristinare **solo le mail**, non serve riportare indietro tutto il Mac.
Time Machine salva anche i database locali di Mail, quindi puoi recuperare selettivamente i messaggi o le caselle che ti servono.

Ecco come:

---

### 🔹 Metodo 1: Recupero diretto da Mail con Time Machine
1. Apri **Mail** sul Mac.
2. Vai nella barra dei menu in alto e scegli **Mail → Casella → Inizia da Time Machine**.
(oppure apri direttamente Time Machine quando Mail è attiva: ti aprirà la vista “a scorrimento” delle caselle).
3. Sfoglia le date fino a quando le mail POP erano ancora presenti.
4. Seleziona le mail o l’intera casella → clicca su **Ripristina**.
- Verranno reimportate in Mail dentro una cartella chiamata **Importate**.
5. Da lì le puoi trascinare nel tuo nuovo account IMAP, così vanno anche sul server.

---

### 🔹 Metodo 2: Ripristino manuale dei file `.mbox`
1. Vai con Finder in:
```
~/Library/Mail/
```
(per entrarci premi **Vai → Vai alla cartella…** e incolla il percorso).
2. Dentro troverai una cartella tipo `V10` o `V11` (dipende da macOS).
3. Lì ci sono sottocartelle per ogni account di posta, comprese quelle POP.
4. Apri Time Machine in quella posizione e torna indietro a una data precedente alla cancellazione.
5. Ripristina la cartella dell’account POP.
6. Poi in Mail vai su **File → Importa caselle… → File in formato Apple Mail** e importa la cartella ripristinata.

---

👉 Ti conviene partire dal **Metodo 1** (molto più semplice).
Vuoi che ti scriva la procedura dettagliata **passo passo** per il Metodo 1, così provi subito a recuperarle da dentro Mail?

---

## 🧑 User

mi sa che era impostato col redirect sulla mia mail di gmail

---

## 🤖 Assistant

Chiaro, allora la situazione cambia parecchio:
se l’account **info@andreapasserini.com** su Hostinger era configurato con **inoltro/redirect automatico** verso Gmail, significa che **tutte le mail arrivate a quell’indirizzo dovrebbero trovarsi già archiviate in Gmail** (a meno che tu non abbia cancellato anche lì).

In pratica:
- Le mail **vecchie** che erano state inoltrate → puoi recuperarle accedendo a Gmail.
- Le mail che erano state scaricate in POP sul Mac e poi eliminate dal server Hostinger **senza essere state inoltrate** → quelle non le troverai né su Hostinger né su Gmail, ma solo dove sono state scaricate (Mac o iPhone).

---

### Cosa puoi fare ora
1. **Controlla in Gmail**
- Vai nella casella Gmail e cerca con `to:info@andreapasserini.com` per vedere tutte le mail inoltrate.
- Se ci sono, sei a posto: da Gmail puoi sempre reimportarle nell’account IMAP Hostinger.

2. **Per il futuro**
- Ti conviene disattivare il redirect *come unica forma di consegna*.
- Mantieni sempre le mail sul server Hostinger con protocollo IMAP (così non spariscono).
- Se vuoi, puoi lasciare attivo l’inoltro a Gmail ma solo come copia di backup.

---

👉 Vuoi che ti scriva la procedura per **prendere le mail archiviate in Gmail e riportarle dentro al tuo account IMAP su Hostinger** (così le ritrovi sincronizzate anche su Mail del Mac)?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

l'ho visto per questo e dentro sono tutte da quella mail

---

## 🤖 Assistant

Perfetto, allora sei in una situazione ottima: vedo dallo screenshot che in Mail hai ancora la cartella **info@andreapasserini.com** dentro l’account Gmail.
Questo significa che **le vecchie mail sono già state salvate in Gmail**, molto probabilmente grazie al redirect che avevi attivato.

Ora quello che ti resta da fare è solo **rimetterle nel nuovo account IMAP su Hostinger**, così diventano di nuovo sincronizzate con il server ufficiale e disponibili ovunque (Mac, iPhone, webmail Hostinger).

---

### Procedura per spostarle da Gmail → Hostinger IMAP
1. Nel pannello laterale di Mail (quello che hai nello screenshot) espandi l’account Gmail.
2. Vai dentro la cartella **info@andreapasserini.com** (dove ci sono le vecchie mail).
3. Seleziona tutte le mail (⌘A).
4. Trascinale nella cartella **In entrata** del nuovo account Hostinger IMAP (quello che hai appena ricreato).
- In alternativa puoi trascinarle in una cartella specifica dell’account Hostinger, se vuoi mantenerle separate.
5. Mail inizierà a caricarle sul server Hostinger: può metterci un po’ se sono tante, ma una volta finite saranno lì e compariranno anche sull’iPhone e sulla webmail.

---

👉 In questo modo ti ritrovi con una copia completa e centralizzata sul server Hostinger, e non dipendi più da Gmail.

Vuoi che ti prepari la stessa procedura anche per **iPhone**, così se preferisci puoi fare il trasferimento direttamente da lì senza passare dal Mac?

---

## 🧑 User

no ma mi andrebbe bene reimpostarle com'era prima, avevo dovuto inizializzare mail e non mi ricordavo di averlo impostato così

---

## 🤖 Assistant

Chiaro 👍
Quindi quello che avevi prima era questo schema:

- La casella **info@andreapasserini.com** su Hostinger non veniva mai consultata direttamente dal Mac.
- In Hostinger avevi impostato un **redirect automatico** verso Gmail.
- Sul Mac e sull’iPhone usavi l’account Gmail (IMAP), dove arrivavano anche tutte le mail indirizzate a info@andreapasserini.com.

È per questo che, dopo aver inizializzato Mail, non vedevi più nulla su Hostinger: in realtà il “vero archivio” era Gmail, che riceveva e conservava tutto.

---

### Se vuoi tornare a quella configurazione
1. **Su Hostinger**
- Vai nel pannello Email → inoltro/redirect → assicurati che sia attivo l’inoltro da `info@andreapasserini.com` a Gmail.
- Se non è più attivo, riattivalo.

2. **Su Gmail**
- Non serve toccare nulla: continuerà a ricevere tutto e a conservarlo.
- Puoi anche filtrare e mettere automaticamente in un’etichetta (“info@andreapasserini.com”) le mail che arrivano da quell’indirizzo, per tenerle ordinate.

3. **Su Mail (Mac e iPhone)**
- Configura solo l’account Gmail (IMAP).
- Tutto rimane sincronizzato e non rischi cancellazioni dal server Hostinger, perché l’archivio diventa Gmail.

---

📌 In sintesi: se ti va bene che **Gmail sia il contenitore principale delle mail** (molto sicuro e con ottima ricerca), puoi ripristinare l’inoltro e non serve usare Hostinger via IMAP.

Vuoi che ti scriva i passaggi esatti su **dove cliccare in Hostinger per riattivare l’inoltro** così riporti tutto identico a prima?

---

## 🧑 User

però comunque avevo modo di consultare due caselle separate dal mac, com'è possibile? una era andrea.passerini.ph@gmail.com e l'altra ce l'avevo come info@andreapasserini.com

---

## 🤖 Assistant

Ok, questo dettaglio cambia il quadro: se vedevi due caselle **distinte** in Mail (una `@gmail.com` e una `info@andreapasserini.com`), significa che **non usavi solo l’inoltro semplice di Hostinger**.
Le possibilità sono due:

---

### 🔹 Caso 1 – Gmail gestiva l’account Hostinger via **POP3**
- Dentro **Gmail** (Impostazioni → Tutte le impostazioni → Account e importazione → “Controlla la posta da altri account”), probabilmente avevi collegato `info@andreapasserini.com`.
- In questo modo Gmail scaricava le mail da Hostinger via POP, le archiviava in Gmail e le mostrava come arrivate lì.
- Sul Mac tu vedevi due account perché:
- uno era il tuo Gmail,
- l’altro era l’account Hostinger configurato direttamente in Mail (POP o IMAP).

---

### 🔹 Caso 2 – Gmail usato come **alias di invio**
- Sempre nelle impostazioni Gmail → “Invia messaggio come”, potevi aver aggiunto `info@andreapasserini.com`.
- Così, quando inviavi da Gmail, potevi scegliere come mittente `info@andreapasserini.com`.
- In Mail, se avevi configurato Gmail come IMAP, vedevi la casella Gmail ma con anche l’alias di invio.

---

### Perché ti comparivano due caselle separate su Mac
Molto probabile che sul Mac tu avessi **aggiunto sia Gmail (IMAP)** che **info@andreapasserini.com (POP o IMAP)** come account separati.
In parallelo, Gmail riceveva comunque una copia (via redirect o POP) e quindi le mail apparivano da entrambe le parti.

---

👉 Ti faccio una domanda mirata per capire esattamente cosa vuoi ricreare:
Vuoi di nuovo che **info@andreapasserini.com sia un account indipendente su Mail (quindi consultabile separatamente da Gmail)** oppure ti basta avere **tutto su Gmail** e usare `info@andreapasserini.com` solo come alias di invio?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

su gmail lo vedo così, magari puoi aiutarmi

---

## 🤖 Assistant

Perfetto, ora è chiarissimo grazie allo screenshot 👍

La tua configurazione Gmail è questa:

1. **Controllo posta POP3**
- Gmail scarica le mail da `info@andreapasserini.com` tramite POP3 (voce: *“Controlla la posta da altri account”*).
- Quindi tutte le mail inviate a `info@andreapasserini.com` finiscono automaticamente dentro Gmail.

2. **Invio come alias**
- Nella sezione *“Invia messaggio come”* hai aggiunto `info@andreapasserini.com`.
- Gmail quindi usa **smtp.hostinger.com** per inviare con quell’indirizzo, e dal punto di vista del destinatario sembri scrivere da `info@andreapasserini.com`.

---

### 🔹 Perché vedevi due caselle su Mac
- In Mail (macOS) tu avevi aggiunto **sia l’account Gmail (IMAP)**,
- sia direttamente **l’account info@andreapasserini.com** (probabilmente come IMAP).

Quindi erano due caselle separate:
- Gmail (che conteneva anche le copie scaricate via POP3),
- e Hostinger (diretto).

---

### 🔹 Ora che cosa vuoi fare?
Hai due possibilità:

**Opzione A – Continuare come prima (due caselle separate)**
- Su Gmail lasci così: continuerà a scaricare via POP3 le mail di info@andreapasserini.com e potrai inviarle come alias.
- Su Mail (macOS) aggiungi di nuovo anche l’account Hostinger in modalità **IMAP**, così lo vedi come casella separata.
👉 In questo modo ti ritrovi **Gmail** + **info@andreapasserini.com** separati, come eri abituato.

**Opzione B – Usare solo Gmail come centro di gestione**
- Non aggiungi più l’account Hostinger in Mail.
- Tutto passa solo da Gmail, che riceve (POP3) e invia (SMTP Hostinger).
👉 In questo modo hai una sola casella, ma continua a funzionare bene e più “pulita”.

---

📌 Consiglio pratico:
Se ti piaceva avere le due caselle separate in Mail, ti basta **riconfigurare info@andreapasserini.com in Mail con IMAP** (non POP). Gmail intanto continuerà a scaricare la sua copia via POP, ma la posta resterà anche sul server Hostinger.

Vuoi che ti scriva i **parametri esatti IMAP/SMTP Hostinger** da inserire su Mail così riaggiungi l’account `info@andreapasserini.com` accanto a Gmail e torni ad avere la doppia casella?

---

## 🧑 User

ok quindi le mail vecchie che ho nella cartella di gmail come posso averle nella info?

---

## 🤖 Assistant

Perfetta domanda 👌
Quelle mail che vedi ora nella casella **Gmail** in realtà sono lì perché:

- Gmail le ha scaricate via **POP3** da `info@andreapasserini.com`.
- Quando Gmail le scarica, di default non le rimette più sul server Hostinger (POP non funziona così: prende dal server e le archivia solo su Gmail).

Quindi: quelle mail “vecchie” **non esistono più su Hostinger**, ma solo dentro Gmail.
Se ora vuoi riportarle nella casella **info@andreapasserini.com (IMAP)**, bisogna **copiare fisicamente i messaggi da Gmail a Hostinger**.

---

### 🔹 Procedura per spostare le mail da Gmail → Hostinger (IMAP)
1. Su Mail (macOS) assicurati di avere configurato **entrambi gli account**:
- Gmail (IMAP)
- info@andreapasserini.com (IMAP)

2. Nel pannello laterale di Mail vai su Gmail → apri la cartella dove ci sono le vecchie mail (`info@andreapasserini.com` o [Gmail]/Tutti i messaggi).

3. Seleziona i messaggi o le cartelle che vuoi trasferire (⌘A per tutti).

4. Trascinali nella casella **In entrata** o in una cartella qualsiasi dell’account Hostinger (IMAP).

5. Mail li copierà sul server Hostinger → ci vorrà un po’ se i messaggi sono tanti, ma quando ha finito compariranno:
- in Mail dentro l’account info@andreapasserini.com,
- su iPhone,
- e soprattutto sulla **webmail Hostinger**.

---

📌 Così ti ritrovi tutte le mail vecchie *di nuovo dentro l’account ufficiale info@andreapasserini.com*, e non solo archiviate su Gmail.

Vuoi che ti prepari la procedura passo-passo **direttamente in Mail su Mac** (con i menu precisi da cliccare), così puoi fare il trasferimento senza rischiare di spostare invece che copiare?

---

## 🧑 User

se invece non la riconfiguro separata posso tenermi una mail chiamata "lavoro" nella quale ho entrambe e in automatico risponde a quella da cui sono state ricevute con l'stmp dedicato?

---

## 🤖 Assistant

Esatto ✅ puoi semplificarti la vita in questo modo:

- **Un solo account in Mail → Gmail** (IMAP).
- Dentro Gmail hai:
- l’indirizzo **andrea.passerini.ph@gmail.com**,
- l’indirizzo **info@andreapasserini.com** configurato come alias, con SMTP Hostinger dedicato.

---

### Come funziona in pratica
- Ricevi tutte le mail (sia quelle mandate a Gmail, sia quelle mandate a info@andreapasserini.com) **nella stessa casella Gmail**.
- Quando rispondi, Gmail (e quindi anche Mail sul Mac/iPhone) **usa automaticamente lo stesso indirizzo a cui hai ricevuto**.
- Se ti scrivono a `info@andreapasserini.com` → tu rispondi con `info@andreapasserini.com` (via SMTP Hostinger).
- Se ti scrivono a `andrea.passerini.ph@gmail.com` → rispondi con Gmail.

👉 Questo è già impostato nel tuo screenshot: hai spuntato **“Rispondi dallo stesso indirizzo al quale il messaggio è stato inviato”**.

---

### Vantaggi
- **Un’unica casella “Lavoro”** su Mac e iPhone, niente doppioni.
- Le risposte partono sempre con l’indirizzo giusto, senza che tu debba cambiare mittente a mano.
- Continui ad avere l’SMTP Hostinger, quindi chi riceve vede correttamente `info@andreapasserini.com`.

---

📌 In sintesi: sì, puoi tenere solo **Gmail in Mail** e usarla come “hub” per entrambi gli indirizzi, senza riconfigurare Hostinger separatamente.
Le vecchie mail resteranno in Gmail, le nuove arriveranno comunque lì (tramite POP3), e tu risponderai sempre con l’indirizzo corretto.

Vuoi che ti scriva come **rinominare in Mail l’account Gmail in “Lavoro”**, così non vedi più “Gmail” ma direttamente la voce che preferisci?

---

## 🧑 User

adesso però se voglio mandare una mail ex novo da info come faccio?

---

## 🤖 Assistant

Perfetta osservazione 👌
Finché rispondi a un’email ricevuta a `info@andreapasserini.com`, Gmail (e quindi anche Mail sul Mac/iPhone) userà automaticamente quell’indirizzo come mittente.

Se invece vuoi **scrivere una nuova mail partendo da zero** e inviarla da `info@andreapasserini.com`, hai due modi:

---

### 🔹 Da Mac (app Mail)
1. Clicca su **Nuovo Messaggio**.
2. Nel campo **Da:** vedrai un menu a tendina con i mittenti disponibili.
3. Seleziona **info@andreapasserini.com**.
- Mail userà l’SMTP Hostinger che hai configurato in Gmail.

*(Se non vedi il campo “Da”, attivalo dal menu “Vista” → “Campo Da”)*

---

### 🔹 Da iPhone (app Mail)
1. Tocca l’icona per scrivere una nuova mail.
2. Tocca il campo **Da**: ti apparirà la lista degli indirizzi configurati.
3. Seleziona **info@andreapasserini.com**.

---

### 🔹 Da Gmail web
- Quando scrivi un nuovo messaggio, nel campo **Da** puoi scegliere con quale indirizzo inviare (il tuo Gmail o l’alias `info@andreapasserini.com`).

---

📌 In sintesi:
- Gmail è l’“hub”, ma in qualsiasi client puoi scegliere manualmente con quale indirizzo inviare quando scrivi ex novo.
- Le risposte invece vengono automaticamente dall’indirizzo corretto (grazie all’opzione che hai attiva).

Vuoi che ti scriva come rendere **info@andreapasserini.com l’indirizzo predefinito per i nuovi messaggi**, così non devi selezionarlo ogni volta a mano?

---

## 🧑 User

non me lo fa vedere nelle opzioni delle mail mittente

---

## 🤖 Assistant

Chiaro, questo succede perché il Mac non “sa” che hai più indirizzi disponibili: al momento Mail vede solo **l’account Gmail** e non ti mostra l’alias `info@andreapasserini.com` come mittente selezionabile.
È normale se l’hai configurato solo dentro Gmail web.

Per poter scrivere **ex novo** da `info@andreapasserini.com` direttamente in Mail, devi fare un passaggio in più: aggiungere l’alias anche nelle preferenze di Mail su macOS.

---

### 🔹 Come aggiungere l’alias mittente in Mail (macOS)
1. Vai su **Mail → Impostazioni → Account**.
2. Seleziona il tuo account **Gmail**.
3. Nella scheda **Informazioni account**, troverai il campo **Indirizzo email**.
4. Lì puoi aggiungere più indirizzi, separati da virgola, ad esempio:
```
andrea.passerini.ph@gmail.com, info@andreapasserini.com
```
5. Chiudi le impostazioni.
6. Ora, quando scrivi una nuova mail, nel campo **Da** potrai scegliere se inviarla da Gmail o da `info@andreapasserini.com`.

⚠️ Importante:
- Perché funzioni davvero con `info@andreapasserini.com`, Gmail deve avere configurato l’**SMTP Hostinger** (lo vedo dallo screenshot che l’hai fatto).
- Quindi Mail userà Gmail come “ponte”, ma invierà correttamente con Hostinger, risultando autentico al destinatario.

---

📌 Così risolvi il problema: continui ad avere un solo account “Lavoro”, ma puoi inviare nuove mail scegliendo `info@andreapasserini.com` dal menu “Da”.

Vuoi che ti scriva la stessa procedura anche per l’iPhone (iOS), così puoi mandare nuove mail da `info@andreapasserini.com` pure lì senza doverle sempre rispondere?