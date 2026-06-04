---
title: "Creazione CNAME VHosting"
created: 2025-06-21
updated: 2025-06-21
model: gpt-4o
messages: 14
source: chatgpt-import
tags: []
---

# Creazione CNAME VHosting

> Importato da ChatGPT export · 14 messaggi · gpt-4o · 2025-06-21

## 🧑 User

devo creare un cname hosting su vhosting mi guidi?

---

## 🤖 Assistant

Certamente. Di seguito ti guido passo passo per creare un record **CNAME** nel pannello di gestione DNS di **VHosting**, assumendo che il dominio sia già registrato e gestito da loro.

---

### ✅ **COSA TI SERVE PRIMA DI INIZIARE**
- Accesso al **pannello cliente di VHosting**
- Il nome del sottodominio che vuoi usare (es: `blog.tuodominio.it`)
- Il dominio di destinazione verso cui deve puntare il CNAME (es: `sites.wix.com` o simili)

---

### 🔧 **COME CREARE UN RECORD CNAME SU VHOSTING**

#### 1. **Accedi al tuo account VHosting**
Vai su [https://www.vhosting-it.com](https://www.vhosting-it.com) e accedi al pannello cliente.

#### 2. **Entra nella gestione del dominio**
- Clicca su **"Domini"** dal menu
- Seleziona il dominio interessato (es. `tuodominio.it`)
- Clicca su **"Gestione DNS"** (oppure su “Gestione zona DNS” se presente)

> ⚠️ Se il dominio usa **nameserver esterni** (es. quelli di Cloudflare), dovrai fare la modifica lì, non su VHosting.

#### 3. **Aggiungi un nuovo record**
- Scorri fino alla sezione **“Aggiungi nuovo record DNS”**
- **Tipo record**: seleziona **CNAME**
- **Nome (Host)**: inserisci solo il prefisso del sottodominio (es. `blog` per `blog.tuodominio.it`)
- **Valore (Punta a)**: il dominio verso cui vuoi puntare (es. `sites.wix.com`)
- TTL: puoi lasciare quello predefinito (es. 3600)

#### 4. **Salva le modifiche**
- Clicca su **Aggiungi record**
- Il nuovo CNAME sarà elencato nella zona DNS

#### 5. **Attendi la propagazione**
- I cambi DNS possono richiedere da pochi minuti a 24 ore per propagarsi globalmente, ma in genere su VHosting è questione di massimo 1–2 ore.

---

### 🔍 **Esempio pratico**

Vuoi che `blog.tuodominio.it` punti a un sito su Wix → dovrai inserire:

| Tipo | Nome | Punta a | TTL |
|-------|------|--------------------|------|
| CNAME | blog | `username.wixsite.com` | 3600 |

---

Se vuoi, indicami:
- Il sottodominio che vuoi creare
- Dove deve puntare (es. servizi esterni, un altro server, ecc.)

e ti preparo la riga esatta da inserire.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, stai già nella sezione corretta per modificare o aggiungere i record DNS su VHosting.

### ✅ Per aggiungere un nuovo **record CNAME**, procedi così:

---

### 🔧 **GUIDA PASSO-PASSO**

1. **Scorri in fondo alla tabella**, dove c'è scritto:

```
Name | Type | Content | Priority | TTL
```

2. Compila i campi come segue:

- **Name**: `sottodominio` che vuoi creare, ad esempio `blog`
_(non inserire il dominio completo)_
- **Type**: seleziona **CNAME** dal menu a tendina
- **Content**: il dominio di destinazione, ad esempio `sites.wix.com` o `hosting.esterno.com.`
_(deve terminare con un punto se vuoi essere formale con le specifiche DNS)_
- **Priority**: lascia **0**
- **TTL**: puoi lasciare **900** o alzarlo a 3600

3. Clicca su **“Add record”**

4. Poi clicca su **“Save changes”** (pulsante blu in alto sotto la tabella) per applicare definitivamente la modifica.

---

### 🔍 **Esempio pratico**
Se vuoi creare `app.foreversnowtrips.com` che punti a `host.esterno.com`, inserirai:

| Name | Type | Content | Priority | TTL |
|------|-------|------------------|----------|------|
| app | CNAME | host.esterno.com. | 0 | 900 |

---

Se mi dici *esattamente* il sottodominio e dove deve puntare, ti do la stringa precisa da copiare e incollare.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🧑 User

guarda questa foto che ti ho appena mandato

---

## 🤖 Assistant

Perfetto, dalla schermata che hai inviato devi creare un record CNAME con i seguenti parametri:

---

### 📌 **Dati del record CNAME da creare**

- **Name (Host/Label)**: `60283256`
- **Type**: `CNAME`
- **Content (Destination/Target)**: `google.com.`
- **TTL**: `3600`

---

### ✅ Ecco come compilarlo nel pannello di VHosting:

1. Scorri in fondo alla tabella della zona DNS dove c'è scritto:

```
Name | Type | Content | Priority | TTL
```

2. Inserisci:

- `60283256` nel campo **Name**
- seleziona `CNAME` nel campo **Type**
- `google.com.` nel campo **Content**
- lascia `0` in **Priority**
- inserisci `3600` in **TTL**

3. Clicca **“Add record”**

4. Poi clicca su **“Save changes”** (pulsante blu) per rendere effettiva la modifica.

---

Se hai bisogno che questo CNAME risponda da un dominio tipo `60283256.foreversnowtrips.com`, è tutto corretto. Fammi sapere se stai facendo una verifica Google, una configurazione per un servizio esterno o altro, così ti posso confermare se è sufficiente o serve altro (es. record TXT).

---

## 🧑 User

Hello Andrea,

Thanks for the update!

Regarding the CNAME record, the initial one [1] was removed. Could you please add it again so we can finalize the release process?

1. Create a CNAME record:

- Label/Host: 60283256
- Destination/Target: google.com
- Time to Live (TTL): 3600 seconds (or 60 minutes / 1 Hour)

2. If your hosting provider is different from where you registered your domain, ensure you're making these changes with your hosting provider. For detailed instructions on how to create a CNAME record, you can visit [2]. If you run into any trouble, your hosting provider's support team will be the best resource to help you create it.

I appreciate your understanding regarding our commitment to account privacy.

Best Regards,

Ashley | 18:00 - 04:00 PHT (UTC+8)
Google Workspace Support

---

## 🤖 Assistant

Grazie per aver condiviso anche la mail: la richiesta è chiarissima.

Hai **rimosso per errore il CNAME richiesto da Google**, identificato da:

- **Host/Name**: `60283256`
- **Target/Destination**: `google.com`
- **TTL**: `3600`

---

### ✅ Ecco come ripristinarlo subito in VHosting

Nel pannello DNS che mi hai mostrato, procedi così:

1. **In fondo alla tabella**, dove c’è scritto:

```
Name | Type | Content | Priority | TTL
```

Compila così:

- **Name**: `60283256`
- **Type**: seleziona `CNAME`
- **Content**: `google.com.`
- **Priority**: `0`
- **TTL**: `3600`

2. Clicca **“Add record”**

3. Poi clicca **“Save changes”** in alto (pulsante blu sotto la tabella)

---

### 📌 Nota
- Il punto finale (`.`) dopo `google.com.` è opzionale, ma consigliato per evitare interpretazioni errate del dominio nel sistema DNS.
- Il record creato sarà valido per `60283256.foreversnowtrips.com`.

Una volta aggiunto, **attendi fino a 1 ora** per la propagazione prima di ritentare la verifica con Google.

Fammi sapere se vuoi che ti prepari anche la risposta email per confermare l’operazione ad Ashley.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🧑 User

riguarda l'immagine

---

## 🤖 Assistant

Perfetto, ho controllato la schermata aggiornata e ti confermo che **il record CNAME è stato creato correttamente**.

---

### ✅ Verifica dettagli:

- **Nome (Host)**: `60283256.foreversnowtrips.com`
- **Tipo**: `CNAME`
- **Content**: `google.com`
- **TTL**: `3600`

---

### 🔄 Propagazione
Ora non devi fare altro che **attendere la propagazione** (generalmente entro 1 ora). A quel punto, Google potrà completare la verifica.

---

### ✉️ Vuoi rispondere ad Ashley?
Se vuoi, ecco un esempio di risposta già pronta:

---

**Oggetto:** CNAME Record Recreated for Domain Verification

```text
Hi Ashley,

Thanks for your message.

I’ve re-added the CNAME record as requested:

- Host: 60283256
- Target: google.com
- TTL: 3600

Please let me know if anything else is required to complete the verification process.

Best regards,
Andrea
```

---

Fammi sapere se vuoi adattarla o aggiungere altro.

---

## 🧑 User

qual è il miglior tool che possiamo usare gratuito per gli insights e gli analytics per il nostro account di instagram? specialmente per capire le performances dei post, e piu di tutto i momenti migliori per postare

---

## 🤖 Assistant

Per ottenere **insight approfonditi su Instagram**, inclusi i **migliori orari per postare**, le **performance dei contenuti** e il comportamento del pubblico, le soluzioni gratuite più efficaci (o con versioni gratuite molto valide) sono:

---

### ✅ **1. Meta Business Suite (ex Facebook Creator Studio)**
**➡️ Miglior strumento gratuito ufficiale**

**Cosa offre:**
- Insight dettagliati su **copertura, engagement, clic, salvataggi**
- Analisi delle performance **per post, storie e reel**
- Dati demografici e di comportamento del pubblico
- **Orari in cui i follower sono più attivi** (sezione “Insight” > “Pubblico”)

**Pro:**
- Gratuito, integrato con Instagram Business
- Nessun limite di account o contenuti
- Permette anche la **programmazione dei post**

**Contro:**
- Interfaccia lenta e a volte poco fluida
- I dati sono meno raffinati rispetto ad alcuni tool a pagamento

📍 Vai su: [https://business.facebook.com](https://business.facebook.com)

---

### ✅ **2. Not Just Analytics**
**➡️ Ottimo per vedere rapidamente come sta performando l’account**

**Cosa offre:**
- Overview gratuita con dati su crescita, engagement e top post
- Dati su **quando postare** in base alle performance storiche
- Analisi gratuite **su qualsiasi account pubblico**

**Pro:**
- Interfaccia chiara e veloce
- Non richiede login (per visualizzazioni base)
- Molto usato anche da brand e creator italiani

**Contro:**
- Alcune funzioni (es. storico dettagliato o grafici avanzati) sono premium

📍 Vai su: [https://www.notjustanalytics.com](https://www.notjustanalytics.com)

---

### ✅ **3. Later (free plan)**
**➡️ Buono per programmazione + suggerimento orari**

**Cosa offre nella versione gratuita:**
- Programmazione di 30 post al mese
- **"Best time to post"** (analizzato su base dei tuoi dati)
- Insight su reach, like, commenti

**Pro:**
- Interfaccia moderna e molto visuale
- Suggerimenti dinamici sugli orari migliori
- Funziona anche per altri social

**Contro:**
- Alcune funzioni di analytics avanzate richiedono il piano pro
- Richiede collegamento API

📍 Vai su: [https://later.com](https://later.com)

---

### ✅ **4. Metricool (free per 1 account)**
**➡️ Ottimo per report automatici e confronto tra contenuti**

**Cosa offre:**
- Analisi dettagliata di post, reel e storie
- Grafici sull’orario di maggiore attività dei follower
- Performance dei contenuti nel tempo
- Analisi multi-social in un’unica dashboard

**Pro:**
- Report esportabili anche nel free plan
- Interfaccia professionale
- Buon bilanciamento tra insight e semplicità

**Contro:**
- Solo 1 account per piano gratuito
- Alcuni grafici disponibili solo in Pro

📍 Vai su: [https://metricool.com](https://metricool.com)

---

### 🔍 **Conclusione – Quale scegliere**

| Tool | Best for | Free | Orari migliori |
|---------------------|----------------------------------|------|----------------|
| Meta Business Suite | Dati ufficiali e affidabili | ✅ | ✅ |
| Not Just Analytics | Analisi semplici e immediate | ✅ | ✅ |
| Later | Programmazione + suggerimenti | ✅ | ✅ |
| Metricool | Reportistica e comparazioni | ✅ | ✅ |

---

Se vuoi **solo il miglior orario per postare**, parti da **Meta Business Suite** e **Not Just Analytics**.
Se invece ti serve anche **reportistica** o **programmazione intelligente**, valuta **Metricool** o **Later**.

Posso aiutarti a configurarne uno o confrontare le dashboard se vuoi.