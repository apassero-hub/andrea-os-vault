---
title: "Guida configurazione adattatori"
created: 2025-09-21
updated: 2025-09-21
model: gpt-5
messages: 12
source: chatgpt-import
tags: []
---

# Guida configurazione adattatori

> Importato da ChatGPT export · 12 messaggi · gpt-5 · 2025-09-21

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Mi guidi nel loro settaggio?

---

## 🤖 Assistant

Perfetto, nella foto vedo due adattatori **TP-Link Powerline AV2000** (uno più grande con Wi-Fi e uno più piccolo senza). Ti guido passo per passo per configurarli:

---

### 1. Collegamento iniziale
- **Adattatore principale (senza Wi-Fi, quello più piccolo):**
- Inseriscilo in una presa elettrica **vicina al modem/router**.
- Collega il cavo Ethernet dal modem/router alla porta Ethernet di questo adattatore.

- **Adattatore secondario (quello più grande, con Wi-Fi):**
- Inseriscilo nella presa elettrica nella stanza dove vuoi estendere la rete.
- Se vuoi collegare un PC/TV via cavo, usa le sue porte Ethernet.
- Se vuoi usare il Wi-Fi, sarà questo a generarlo.

---

### 2. Accoppiamento (pairing)
- Premi il pulsante **Pair** sull’adattatore collegato al router per 1 secondo (la spia dovrebbe iniziare a lampeggiare).
- Entro 2 minuti, premi il pulsante **Pair** sull’altro adattatore per 1 secondo.
- Le spie di "casa" (icona con la casetta) dovrebbero diventare verdi fisse: significa che la connessione Powerline funziona.

---

### 3. Configurazione Wi-Fi
- Il Wi-Fi dell’adattatore grande può essere configurato in due modi:
1. **Copia dal router (WPS):**
- Premi il pulsante **Wi-Fi Clone/Wi-Fi/WPS** sull’adattatore grande.
- Entro 2 minuti, premi il pulsante **WPS** sul router.
- In questo modo il powerline clonerà nome e password della rete Wi-Fi principale.

2. **Configurazione manuale:**
- Collega un PC all’adattatore via cavo.
- Apri il browser e vai su `http://tplinkplc.net` (o l’IP che assegna il router).
- Login predefinito: **admin / admin**.
- Da lì puoi impostare **nome rete Wi-Fi (SSID)** e **password** a tuo piacere.

---

### 4. Verifica
- Controlla che le spie siano verdi (o almeno arancioni se la qualità della linea elettrica non è ottimale).
- Testa sia la connessione via cavo che quella Wi-Fi.

---

Vuoi che ti prepari una guida rapida **con schema visivo e passaggi numerati** così la puoi tenere a portata di mano mentre li installi?

---

## 🧑 User

Questo è il dialetto che sto usando, questi X-Standard questo tuo consiglio per portare la rete sotto in lavanderia che è due piani sotto con VPS, me lo leggi lo stesso, devono essere relativamente vicini

---

## 🤖 Assistant

Ok, chiarisco subito:

Gli adattatori **Powerline** (come quelli TP-Link AV2000 che hai) **non hanno bisogno di stare vicini fisicamente**, ma devono essere collegati **alla stessa rete elettrica**.

⚠️ I limiti reali sono questi:
- Funzionano solo se le prese sono alimentate dallo **stesso contatore/impianto elettrico**.
- Se tra il piano di sopra e la lavanderia ci sono **quadri elettrici separati, differenziali diversi o troppe derivazioni**, la connessione può degradare molto o non funzionare affatto.
- Due piani sotto può funzionare, ma la velocità reale potrebbe essere molto inferiore rispetto ai “2000 Mbps” dichiarati. Nella pratica potresti avere **50–200 Mbps effettivi**, dipende dalla qualità dell’impianto.
- Vanno collegati direttamente a una presa a muro, non a ciabatte o UPS (che filtrano e bloccano il segnale).

👉 Quindi sì, puoi provare a portarli fino alla lavanderia. Se sei sullo stesso impianto elettrico, **anche a due piani di distanza dovrebbero funzionare**.
Se invece l’impianto elettrico è suddiviso su più linee o quadri, allora **il segnale potrebbe non passare**.

Vuoi che ti dia anche un confronto pratico tra Powerline e un sistema **Mesh Wi-Fi (tipo Deco o Orbi)**, così capisci quale delle due soluzioni è più stabile nel tuo caso?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Dove lo attacco?

---

## 🤖 Assistant

Perfetto, nella foto vedo il retro del tuo modem/router.

Per collegare il tuo kit **Powerline TP-Link**:

1. **Prendi l’adattatore piccolo (senza Wi-Fi)**.
2. Collegalo a una presa elettrica vicina al modem.
3. Usa un cavo **Ethernet RJ45** e collegalo:
- da una delle porte **LAN gialle (LAN1, LAN2 o LAN3)** del modem
- alla porta Ethernet dell’adattatore Powerline piccolo.

⚠️ **Non collegarlo alla porta blu “WAN”**: quella serve solo se il modem venisse usato come router dietro un altro apparato.

Dopo questo passaggio, l’adattatore piccolo diventa il “trasmettitore” che porta la rete dentro l’impianto elettrico.
L’adattatore grande (quello con Wi-Fi) lo metti nella lavanderia, in presa diretta al muro → lì riceverà internet tramite la linea elettrica.

Vuoi che ti faccia uno **schemino semplice passo-passo con disegnino ASCII** così ti resta subito chiaro visivamente dove va ogni cavo?

---

## 🧑 User

Il tasto wps non c'é, c'é solo pair, led e wifi

---

## 🤖 Assistant

Chiaro 👍
I tuoi TP-Link non hanno un tasto WPS vero e proprio, ma solo:

- **Pair** → serve per accoppiare gli adattatori fra loro.
- **Wi-Fi** (a volte indicato come “Wi-Fi Clone” o simile) → serve per copiare il nome e la password del Wi-Fi del modem/router.
- **LED** → accende/spegne le spie.

Quindi la procedura per il Wi-Fi è diversa:

---

### 🔌 Passaggi corretti

1. **Collega l’adattatore piccolo al modem/router** (porta LAN gialla del modem → porta Ethernet adattatore).
2. **Inserisci l’adattatore grande** nella presa della stanza/lavanderia.
3. Premi il tasto **Pair** sul piccolo → entro 2 minuti premi il **Pair** sul grande.
- Se la spia con la “casetta” diventa verde fissa = connessione Powerline stabilita.

---

### 📶 Configurazione Wi-Fi
Hai due scelte:

1. **Wi-Fi Clone (consigliato se vuoi stesso nome e password del modem):**
- Sul modem premi il suo tasto **WPS** (sul retro nella foto che mi hai mandato c’è il pulsante “Wi-Fi WPS”).
- Entro 2 minuti premi il pulsante **Wi-Fi** sull’adattatore grande.
- L’adattatore copierà SSID e password del modem → avrai un’unica rete con lo stesso nome.

2. **Configurazione manuale (se vuoi una rete separata):**
- Collega un PC via cavo all’adattatore grande.
- Vai su `http://tplinkplc.net` (oppure vedi l’IP in DHCP dal modem).
- Entra (user/pass predefiniti: **admin / admin**).
- Imposta tu un nome rete (SSID) e password Wi-Fi dedicati.

---

👉 Ti va se ti scrivo una guida veloce tipo “5 step numerati” così quando sei lì davanti agli adattatori la segui al volo senza dover ripensare a tutto?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, ora si vede bene il lato dell’adattatore grande: i tasti sono **Pair**, **LED** e **Wi-Fi**.
Questo conferma che la procedura giusta è questa:

---

### 🔧 Configurazione rapida in 5 step

1. **Collega l’adattatore piccolo al modem/router**
- Cavo Ethernet da una porta **LAN gialla** del modem → porta Ethernet dell’adattatore piccolo.
- Inseriscilo in presa a muro (no ciabatta).

2. **Inserisci l’adattatore grande nella lavanderia**
- Solo presa a muro diretta.

3. **Accoppia gli adattatori**
- Premi **Pair** per 1 secondo sul piccolo → LED inizia a lampeggiare.
- Entro 2 minuti premi **Pair** per 1 secondo sul grande.
- Se la spia “casa” diventa verde fissa → collegamento ok.

4. **Configura il Wi-Fi**
- Se vuoi che usi lo stesso nome e password del modem:
- Premi **WPS sul modem** (è il pulsante che hai visto sul retro).
- Entro 2 minuti premi il tasto **Wi-Fi** sull’adattatore grande.
- Copierà nome e password della rete principale.
- Se invece vuoi un Wi-Fi separato:
- Collega un PC al grande via cavo.
- Vai su `http://tplinkplc.net` → login `admin / admin`.
- Imposta nome rete (SSID) e password che preferisci.

5. **Verifica connessione**
- LED “casa” verde → connessione Powerline stabile.
- LED Wi-Fi acceso → rete wireless attiva.
- Prova con telefono/PC a connetterti.

---

👉 Vuoi che ti scriva anche i **codici LED (verde/arancio/rosso e lampeggi)** così capisci subito se il segnale che arriva in lavanderia è buono o scarso?

---

## 🧑 User

Anzi sicuro, sul schiaccio, mi sembra che l'unica cosa che faccia è disattivare il Wi-Fi o attivarlo.

---

## 🤖 Assistant

Hai colto nel segno 👍
Il tasto **Wi-Fi** sul tuo modello non è un vero “clone button” universale, ma serve principalmente a:

- **Attivare/disattivare il Wi-Fi** dell’adattatore grande (un po’ come l’interruttore ON/OFF).
- Su alcuni modelli, **tenendolo premuto più a lungo** (2–3 secondi), entra in modalità “Wi-Fi Clone” → a quel punto può copiare SSID e password dal modem via WPS.

Quindi:
- **Pressione breve** → spegne/accende il Wi-Fi del powerline.
- **Pressione lunga (2–3 sec)** → attiva la funzione di clonazione (solo se il router supporta WPS e se lo premi anche lì).

Se ti sembra che faccia solo ON/OFF, molto probabile che:
1. Il router non stia mandando il segnale WPS quando tu provi (sul tuo modem il pulsante WPS va tenuto premuto 1–2 secondi).
2. L’adattatore stia solo ricevendo il comando ON/OFF perché non è entrato in “clone mode”.

👉 In alternativa, puoi sempre configurare manualmente l’SSID e la password accedendo a `tplinkplc.net`.

Vuoi che ti scriva la sequenza esatta dei **secondi di pressione** (router e powerline) per fare il clone, così provi a vedere se funziona davvero il WPS → Wi-Fi Clone?