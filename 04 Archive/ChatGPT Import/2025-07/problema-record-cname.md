---
title: "Problema record CNAME"
created: 2025-07-04
updated: 2025-07-04
model: gpt-4o
messages: 4
source: chatgpt-import
tags: []
---

# Problema record CNAME

> Importato da ChatGPT export · 4 messaggi · gpt-4o · 2025-07-04

## 🧑 User

mi scrivi la mail da mandare al provider visto che non arriviamo ad un dunque? mi hanno scritto questo da google "Hello Andrea,

Thanks for your reply and for providing the additional information. I understand that you've tried adjusting the CNAME record for foreversnowtrips.com but are encountering an issue where it won't exclude.

To resolve this, you'll need to contact the support team of your domain hosting provider. They are best equipped to assist you directly with creating and modifying CNAME records within your domain's DNS settings.

They can help ensure the "Name" portion of the record is correctly set to 60940155 and troubleshoot any issues you're facing with the exclusion.

Once your domain host confirms the CNAME record has been updated, you can then use our Google Admin Toolbox [1] to verify its successful creation and propagation.

Please let me know if you have any other questions after speaking with your domain host.

Best Regards,

Ashley "

---

## 🤖 Assistant

Ecco una mail chiara, tecnica ma cortese, che puoi mandare al provider per risolvere la questione:

---

**Oggetto:** Assistenza per modifica record CNAME – Dominio foreversnowtrips.com

Buongiorno,
vi contatto in merito a un problema riscontrato nella configurazione del record CNAME per il dominio **foreversnowtrips.com**, necessaria per completare la verifica del dominio con Google Workspace.

Durante la procedura di verifica, Google richiede l'inserimento di un record CNAME con **Name (o Host)** impostato su **60940155** e **Value (o Target)** su `gv-xxxxxxxx.dv.googlehosted.com`. Ho già provato ad aggiungere il record, ma qualcosa sembra impedirne la corretta propagazione o esclusione del precedente.

Dal supporto Google mi è stato consigliato di contattarvi direttamente, poiché potreste assistermi meglio nella creazione e configurazione di questo record.
Vi chiedo gentilmente di:

1. Verificare se è presente un record CNAME conflittuale o errato.
2. Assicurarvi che il nuovo record abbia **Name = 60940155** e punti al valore corretto fornito da Google.
3. Confermare una volta applicata la modifica, così potrò procedere alla verifica tramite Google Admin Toolbox.

Resto a disposizione per fornire ulteriori dettagli o accessi se necessari.
Grazie per la disponibilità e l’assistenza.

Cordiali saluti,
**Andrea Passerini**
Forever Snow Trips

---

Fammi sapere se vuoi includere anche l'attuale valore da impostare come *Target* (gv-xxxxxx...), così lo inseriamo direttamente.

---

## 🧑 User

aggiungerei che io ho aggiunto il record ma che non viene visualizzato da loro per potermi liberare il workspace associato al dominio (cosa già fatta precedentemente ma per un errore di setup iniziale abbiamo dovuto rifare).
Quando ho mandato loro lo screenshot dei record dns mi hanno detto che non doveva risultare 60940155.foreversnowtrips.com ma mi pare sia solo una questione di standard di utilizzo

---

## 🤖 Assistant

Perfetto, ecco la versione aggiornata della mail con tutti i dettagli che hai indicato:

---

**Oggetto:** Assistenza urgente per configurazione record CNAME – Dominio foreversnowtrips.com

Buongiorno,
vi scrivo in merito alla verifica del dominio **foreversnowtrips.com** con Google Workspace, che al momento non va a buon fine a causa di un problema con il record CNAME.

Ho già provveduto ad **aggiungere manualmente il record CNAME richiesto da Google**, ma da parte loro non risulta visibile, impedendomi di completare la procedura e liberare l’account Workspace attualmente associato al dominio. Si tratta di un nuovo tentativo di verifica, resosi necessario dopo un errore nella configurazione iniziale.

Il valore richiesto da Google per il record CNAME è il seguente:
- **Name/Host:** `60940155`
- **Target/Value:** `gv-xxxxxxxx.dv.googlehosted.com` (valore completo disponibile su richiesta)

Tuttavia, quando ho inviato loro uno screenshot dei DNS, mi è stato risposto che il record non doveva risultare come `60940155.foreversnowtrips.com`, ma ritengo si tratti semplicemente di una **questione di visualizzazione standard della zona DNS**, poiché molti pannelli DNS aggiungono automaticamente il dominio principale al campo *Name*.

Da parte loro mi hanno chiesto esplicitamente di rivolgermi a voi per:
1. Verificare che il record sia correttamente inserito e non ci siano conflitti.
2. Assicurarvi che il campo **Name/Host** sia esattamente `60940155` (senza sottodomini o prefissi aggiuntivi).
3. Confermare che il record si sia propagato correttamente.

Una volta sistemato, procederò a verificarne la propagazione tramite Google Admin Toolbox.

Resto a disposizione per fornirvi l’accesso al pannello o ulteriori dettagli se necessario.
Vi ringrazio anticipatamente per la collaborazione.

Cordiali saluti,
**Andrea Passerini**
Forever Snow Trips

---

Fammi sapere se vuoi aggiungere anche il link allo strumento Admin Toolbox o uno screenshot, oppure se preferisci che li tenga da parte per un follow-up.