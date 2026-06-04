---
title: "Aputure 300d con Yeti 500X"
created: 2026-04-17
updated: 2026-04-17
model: gpt-5-3
messages: 12
source: chatgpt-import
tags: []
---

# Aputure 300d con Yeti 500X

> Importato da ChatGPT export · 12 messaggi · gpt-5-3 · 2026-04-17

## 🧑 User

Se devo utilizzare una luce tipo aputure 300d in esterna e alimentarla da una batteria, se questa fosse il goal zero 500x?

---

## 🤖 Assistant

Sì, **puoi usare una entity["product","Goal Zero Yeti 500X","portable power station"] per alimentare una entity["product","Aputure LS 300d II","LED light"]**, ma devi capire bene due limiti: **potenza istantanea** e **autonomia reale**.

---

## 1. Compatibilità: funziona?
Sì, senza problemi.

- La 300d II assorbe fino a **~350W** cite
- La Yeti 500X eroga **300W continui (1200W di picco)** cite

👉 Tradotto:
- A **100% potenza** sei **al limite** (e potresti avere instabilità o cutoff)
- A **70–80%** lavori tranquillo

---

## 2. Autonomia reale (il punto critico)
La batteria è da circa **505Wh** cite

Regola base:
> Wh / Watt = ore di autonomia cite

### Stima concreta:

- **300d al 100% (350W)**
→ 500 / 350 ≈ **1.2 h teoriche**
→ reale: **45–60 min**

- **300d al 70% (~240W)**
→ ≈ **1.5–2 h**

- **300d al 50% (~170W)**
→ ≈ **2.5–3 h**

👉 Considera sempre perdite inverter → togli un 15–20%.

---

## 3. Problemi pratici che incontrerai
Te lo dico diretto:

- A piena potenza sei **borderline sulla potenza AC**
- Autonomia **ridicola per un set serio**
- È una soluzione ok per:
- shooting veloci
- fill light
- run & gun

Non è una soluzione da produzione strutturata.

---

## 4. Soluzioni migliori (se vuoi lavorare bene)

### Opzione A — stessa logica, più seria
- Yeti 700 / EcoFlow / simili (700–1000Wh+)
- Ti porti a casa **2–3h reali a piena potenza**

### Opzione B — soluzione “da set”
- Batterie V-Mount (2x o 3x in parallelo)
- Più modulare, meno perdite

### Opzione C — soluzione definitiva
- Power station 1000–2000Wh
→ standard reale per produzioni outdoor

---

## Conclusione
Funziona, ma:

- ✔ sì per uso leggero e spot veloce
- ❌ no se devi lavorarci seriamente

Se mi dici che tipo di shooting fai (durata, setup, quante luci), ti dimensiono una soluzione sensata senza portarti dietro peso inutile.

---

## 🧑 User

E fosse la zhiyun molus g309?

---

## 🤖 Assistant

Qui cambia tutto. La **entity["","Zhiyun Molus G300"]** NON è equivalente alla 300d dal punto di vista dell’alimentazione.

---

## ❌ Problema principale: non è pensata per batteria
Te lo dico diretto:

- La Molus G300 **funziona solo via alimentatore esterno (AC)** cite
- Non ha plate V-mount / ingresso DC utilizzabile “seriamente”
- Ha un **power box separato** che va comunque collegato alla corrente

👉 Tradotto:
Non è una luce “battery-friendly” come le Aputure.

---

## ⚡ Con la Goal Zero 500X: funziona?
Sì… ma è una soluzione forzata.

### Setup reale:
- Colleghi la **entity["","Goal Zero Yeti 500X"]** → presa AC
- Poi alimenti il controller della G300

### Ma:

- La G300 è **300W reali (fino a ~500W in boost)** cite
- La Yeti 500X fa **300W continui**

👉 Sei di nuovo:
- **al limite costante**
- con rischio di spegnimenti o throttling

---

## ⏱️ Autonomia (ancora peggio)
Essendo sempre su inverter AC:

- 300W → circa **45–60 min reali**
- con perdite più alte rispetto a V-mount

👉 Quindi:
- meno efficiente rispetto alla 300d su batterie dedicate
- più spreco energetico

---

## ⚖️ Differenza chiave rispetto alla 300d

| | 300d II | Molus G300 |
|---|---|---|
| Alimentazione | V-mount / AC | Solo AC |
| Efficienza su batteria | Alta | Bassa |
| Uso outdoor | Pensata per quello | Adattata |
| Modularità | Alta | Limitata |

---

## 🧠 Conclusione (senza girarci attorno)

- ✔ **Funziona con la Goal Zero**
- ❌ **Non è la scelta giusta per lavorare in esterna**

La G300 è:
> una luce da studio “compatta”, non una luce da location seria.

---

## 👉 Se il tuo obiettivo è outdoor reale

Hai tre strade sensate:

1. **Aputure 300d / 300x**
- V-mount → soluzione pulita

2. **Zhiyun Molus X / G più piccoli**
- quelli con power bank dedicati

3. **Power station più grossa (1000Wh+)**
- se vuoi usare G300 comunque

---

## Sintesi brutale
Se vuoi lavorare bene fuori:

- 300d → scelta corretta
- G300 → compromesso poco intelligente su batteria

---

Se vuoi, ti costruisco un setup concreto (peso, autonomia, costi) per i tuoi shooting reali—così eviti di portarti dietro roba che ti lascia a piedi dopo un’ora.

---

## 🧑 User

Avendo bisogno di una luce di quel vattaggio o magari 500watt qual è la miglior soluzione on location a livello di batteria e luce stessa?

---

## 🤖 Assistant

Se vuoi lavorare **seriamente in esterna con 300–500W**, la scelta non è più “che batteria uso”, ma:

> **che sistema luce + alimentazione è progettato per lavorare insieme**

Ti semplifico tutto senza giri di parole.

---

# 🎯 PRINCIPIO BASE (quello che devi tenere a mente)
- Power station (Goal Zero ecc.) = **soluzione di emergenza**
- V-mount / high-voltage battery = **standard professionale**

👉 Sopra i **300W**, cambia proprio la tecnologia:
servono **batterie ad alto voltaggio (26–48V)**, non le classiche 14.4V.

---

# 🔥 MIGLIORI SOLUZIONI REALI (300–600W OUTDOOR)

## 🥇 Best overall (setup professionale vero)
### Aputure 600d / 600x
product["","Aputure LS 600d Pro",{"render_as":"hero","description":"Standard industriale per luce potente outdoor con alimentazione V-mount o high-voltage."}]

### Perché è la scelta giusta:
- Nata per lavorare **a batteria**
- Supporta:
- 2× V-mount (half power)
- **high voltage battery → 100% output**
- Ecosistema enorme (modificatori, accessori)

👉 È letteralmente lo standard nei set veri.

---

## 🥈 Alternativa diretta (stesso livello)
### Nanlite Forza 500 II
product["","Nanlite Forza 500 II",{"render_as":"block","description":"Alternativa diretta alla 600d, più compatta ma comunque pensata per uso professionale."}]

- Ottimo compromesso peso/potenza
- Sistema battery abbastanza solido
- Leggermente più “portabile”

---

## 🥉 Budget / compromesso
### Zhiyun Molus G300
product["","Zhiyun Molus G300",{"render_as":"block","description":"Compatta e potente ma limitata in alimentazione: più da studio che da location seria."}]

- Potenza buona
- Ma:
- AC only (di fatto)
- inefficiente su batteria

👉 Non è una vera soluzione outdoor

---

# ⚡ BATTERIE: QUI SI FA LA DIFFERENZA

## ❌ Quello che NON devi fare
- Goal Zero / power station piccole
→ inefficienza + peso + autonomia scarsa

---

## ✅ Quello che devi usare

### Batterie high-voltage (tipo SWIT)
- es: HB-C420S
- **420Wh / 500W continui** cite
- progettate per luci cine

👉 2 batterie =
- 600W full power
- ~1h / 1h20 reale cite

---

## ⚙️ Configurazione reale da set

### Setup serio 500–600W:
- 1x Aputure 600d
- 2x batterie HV (tipo SWIT)
- adattatore dual V-mount / 48V

👉 risultato:
- piena potenza
- mobilità reale
- niente inverter → zero sprechi

---

# 📊 CONFRONTO REALE (quello che conta davvero)

| Sistema | Efficienza | Potenza reale | Autonomia | Usabilità |
|---|---|---|---|---|
| Power station (Goal Zero) | ❌ bassa | instabile | scarsa | scomoda |
| V-mount standard (14.4V) | ⚠️ limitata | metà potenza | media | ok |
| **High-voltage V-mount (28–48V)** | ✅ alta | piena | buona | professionale |

---

# 🧠 CONCLUSIONE (chiara)

Se vuoi lavorare davvero outdoor:

- **300W → puoi arrangiarti**
- **500–600W → devi salire di livello**

👉 La soluzione corretta è:
> **Aputure 600d (o equivalente) + batterie high-voltage**

Tutto il resto è:
- workaround
- perdita di tempo
- rischio di rimanere senza luce

---

# 👉 Se vuoi ottimizzare davvero
Posso costruirti un setup preciso in base a:
- tipo di shooting (foto / video / commerciale)
- durata reale delle sessioni
- mobilità (a piedi, bici, auto)

Così eviti di spendere 2–3k nel modo sbagliato.

---

## 🧑 User

Amaran ha qualche altra opzione?

---

## 🤖 Assistant

Sì — **Amaran ha fatto un passo avanti rispetto a prima**, ma devi essere lucido su una cosa:

> Amaran è ancora una linea **semi-pro / creator**, non una vera soluzione “heavy duty” da location come Aputure LS.

Detto questo, oggi **qualcosa di utilizzabile outdoor c’è**.

---

# 🔥 LE UNICHE OPZIONI AMARAN SENSATE (300W)

## 🥇 Amaran 300c (la più interessante)
product["","Amaran 300c",{"render_as":"hero","description":"COB RGBWW da 300W con attacco Bowens e possibilità di alimentazione a batteria tramite power station dedicata."}]

### ✔ Cosa cambia rispetto alla roba vecchia:
- 300W reali
- RGBWW (non solo bi-color)
- Attacco Bowens
- **Supporta batteria (ma attenzione)** cite

👉 Puoi alimentarla con:
- **Aputure 2-Bay Battery Station (V-mount)**
- quindi finalmente → utilizzo outdoor reale

---

### ❗ Il problema (sempre quello)
- Non ha battery plate integrato
- Serve box esterno
- Non è efficiente come Aputure LS

👉 Tradotto:
funziona, ma è **meno pulita e meno robusta come soluzione**

---

## 🥈 Amaran 150c (più intelligente per molti casi)
product["","Amaran 150c",{"render_as":"block","description":"Versione più compatta e gestibile del 300c, molto più adatta a uso reale a batteria."}]

### Perché potrebbe essere la scelta migliore:
- 150W → **gestibile facilmente a batteria**
- stessa qualità colore
- molto più efficiente

👉 In esterna spesso:
> meglio 150W ben gestiti che 300W che ti mollano dopo 40 min

---

## 🥉 Fascia più bassa (non il tuo caso)
product["","Amaran 100x S",{"render_as":"block","description":"COB da 100W compatto e leggero, pensato per setup piccoli e portatili."}]

- perfetto run & gun
- inutile se stai cercando 300–500W

---

# ⚡ QUESTIONE BATTERIA SU AMARAN (qui devi stare attento)

Amaran NON ha:
- sistema integrato tipo Aputure LS
- gestione smart high-voltage

Funziona così:
- luce → ingresso 48V DC
- batteria → tramite **power station esterna (2-Bay V-mount)**

👉 quindi:
- più cavi
- più ingombro
- più punti di errore

---

# 📊 CONFRONTO REALE (quello che ti interessa)

| | Amaran 300c | Aputure 300d II | Aputure 600d |
|---|---|---|---|
| Potenza | 300W | 350W | 600W |
| Batteria | ⚠️ esterna | ✅ integrata | ✅ pro |
| Efficienza | media | alta | molto alta |
| Outdoor serio | ⚠️ | ✅ | ✅ |
| Prezzo | 💰 | 💰💰 | 💰💰💰 |

---

# 🧠 VERITÀ OPERATIVA

Se stai valutando Amaran per questo motivo:
> “risparmio ma voglio comunque lavorare outdoor”

Allora:

- ✔ **150c → senso reale**
- ⚠️ **300c → borderline**
- ❌ sopra i 300W → Amaran non è il brand giusto

---

# 🎯 CONCLUSIONE DIRETTA

Amaran oggi:
- è diventato **usabile in esterna**
- ma non è ancora una piattaforma “pro battery-first”

👉 Se vuoi lavorare bene:
- 150c → scelta intelligente e concreta
- 300c → compromesso
- 500W → esci da Amaran

---

# 👉 Ti faccio risparmiare tempo (e soldi)
Se mi dici:
- che tipo di shooting fai (ritratto, sport, brand, video)
- quanto devi camminare/spostarti
- quanto dura una sessione

ti dico esattamente:
> quante batterie ti servono + che luce comprare senza buttare budget.

---

## 🧑 User

Nello specifico devo filmare in outdoor 6 video di 20 min l'uno. Saranno video corsi e voglono filmare tutto in esterna. Siccome posso incorrere in condizioni di luce che va e viene per le nuvole, in tal caso mi serve un piano b di una key light abbastanza forte da illuminare il soggetto di giorno

---

## 🤖 Assistant

Qui entriamo nel concreto: il tuo scenario è **intervista/corso outdoor di giorno**, con luce variabile → quindi il problema non è solo “potenza”, ma:

> **consistenza della luce + autonomia reale per ~2 ore totali (6×20 min)**

Ti dico subito la verità operativa:

---

# 🎯 COSA TI SERVE DAVVERO

Per non avere un risultato amatoriale:

- **potenza reale: minimo 300W, meglio 500–600W**
- **luce direzionale (COB + softbox)**
- **batteria stabile per almeno 2 ore totali**
- **setup rapido (perché stai girando, non montando un set cinema)**

👉 Tradotto:
> una 150W non basta se il sole entra/esce
> una 300W è borderline
> una 500–600W è la soluzione corretta

---

# 🔥 SETUP CONSIGLIATI (REALI, NON TEORICI)

## 🥇 Best overall (quello che risolve davvero il problema)

### Aputure 600d + batterie high-voltage
👉 riferimento batteria:
product["","SWIT PB-C420S 420Wh High Load Battery",{"render_as":"hero","description":"Batteria high-load progettata per alimentare luci fino a 500W reali senza perdita di potenza."}]

### Perché è la scelta giusta:
- 600W → riesci a “tenere testa” al sole
- con softbox hai ancora output utile
- autonomia:
- 1 batteria → ~40–60 min reali
- 2 batterie → copri il tuo shooting

👉 Questo è il setup che usano nei set seri.

---

## 🥈 Alternativa più compatta (ma ancora valida)

### Nanlite Forza 500
- 500W reali
- funziona a V-mount
- circa **1h a piena potenza** cite

👉 compromesso intelligente:
- meno peso
- meno costo
- ancora utilizzabile come key di giorno

---

## 🥉 Se vuoi stare su Amaran (ma devi accettare i limiti)

### Amaran 300c
product["","Amaran 300c",{"render_as":"block","description":"COB RGBWW da 300W, portabile ma meno efficiente e potente per uso outdoor rispetto ai sistemi pro."}]

### Funziona, ma:
- 300W → al limite in daylight
- appena metti diffusione → perdi troppo output
- sistema batteria meno efficiente

👉 Tradotto:
> ok se lavori in ombra / golden hour
> non ok come piano B “sicuro”

---

# ⚡ BATTERIE: QUANTE TE NE SERVONO DAVVERO

## Setup corretto per il tuo caso (2 ore totali)

### 600W setup:
- 2× batterie tipo:
- entity["","SWIT PB-C420S 420Wh High Load Battery"]
- lavori tranquillo

### 500W setup:
- 2 batterie → sufficiente
- 3 batterie → sicurezza totale

### 300W setup:
- autonomia ok
- ma **potenza insufficiente**

---

# ❗ ERRORE CHE DEVI EVITARE (importante)

👉 Power station tipo Goal Zero:
- inefficienza (AC conversion)
- peso inutile
- autonomia peggiore

👉 nel tuo caso:
> è la soluzione sbagliata

---

# 🎥 CONSIDERAZIONI DA VIDEOMAKER (questa è la parte che conta)

Per corsi/interviste outdoor:

- meglio:
- luce **hard + diffusione controllata**
- oppure bounce forte
- evita:
- softbox enormi → mangiano output

👉 setup intelligente:
- 600d + light dome mini / softbox medio
- oppure reflector + diffusione leggera

---

# 🧠 CONCLUSIONE (senza giri)

Se vuoi un risultato professionale:

- ✔ soluzione corretta → **600W + batterie HV**
- ⚠️ soluzione accettabile → **500W**
- ❌ soluzione rischiosa → **300W**

---

# 👉 Tradotto per il tuo caso specifico

Stai girando:
- 6 clip da 20 min
- luce variabile
- outdoor

👉 quindi:

> **se vuoi zero problemi: Aputure 600d + 2 batterie serie**

Tutto il resto è:
- compromesso
- o rischio di girare materiale inutilizzabile

---

Se vuoi, ti costruisco un setup preciso (zaino, peso, stativi, modificatori) pensato per lavorare davvero in esterna senza assistente.

---

## 🧑 User

Frena. I 6 video sono in sei giorni diversi. I 20 minuti di video saranno l'output finale

---

## 🤖 Assistant

Perfetto, questo cambia completamente lo scenario.
Non devi alimentare 2 ore continuative: devi coprire **sessioni relativamente brevi per giorno**, anche se realisticamente tra setup, retry e pause sarai comunque su **60–90 minuti di luce accesa**.

👉 Tradotto: **non ti serve un setup “cinema da 600W obbligatorio”**, ma nemmeno una soluzione sottodimensionata.

---

# 🎯 OBIETTIVO REALE
- compensare variazioni di luce (nuvole)
- mantenere esposizione coerente sul volto
- lavorare leggero e veloce (sei da solo)

---

# 🔥 SCELTA DELLA LUCE (QUI STA LA DIFFERENZA)

## 🥇 Scelta più equilibrata
### entity["product","Aputure LS 300d II","LED light"]
È il punto giusto tra:
- potenza sufficiente in daylight (se lavori bene)
- gestione batteria semplice
- portabilità reale

👉 Con un minimo di shaping:
- regge tranquillamente situazioni con sole intermittente
- non sei sovradimensionato come con una 600d

---

## 🥈 Alternativa valida
### entity["product","Nanlite Forza 300 II","LED light"]
- stessa fascia
- leggermente più compatta
- output comparabile

---

## ⚠️ Quando servirebbe davvero una 600W?
Tipo entity["product","Aputure LS 600d Pro","LED light"]

Solo se:
- sei in pieno sole diretto **senza possibilità di controllarlo**
- vuoi fare key “dominante” sul sole

👉 ma:
- pesa di più
- consuma molto di più
- è overkill per un corso/intervista

---

# ⚡ BATTERIA (dimensionamento corretto)

## Setup consigliato

### ✔ 2 batterie V-mount serie (tipo 150–190Wh)
- sulla 300d:
- ~70–80% potenza → **1h / 1h20 reali**
- con 2 coppie (4 batterie totali):
- copri una giornata senza stress

👉 soluzione:
- modulare
- veloce da cambiare
- zero inverter

---

## ❌ Power station (Goal Zero ecc.)
Scartala per questo lavoro:
- più ingombrante
- meno efficiente
- inutile per durate brevi

---

# 🎥 COME OTTENERE RISULTATO PROFESSIONALE (più importante dei watt)

La luce da sola non basta. Devi controllare il sole.

## Setup intelligente:

- **key light (300d)** → costante sul soggetto
- **diffusione sul sole (se possibile)**
oppure
- **posizionamento in ombra controllata**

👉 La vera strategia è:
> abbassare il sole, non combatterlo

---

## Modificatori (scelta cruciale)

Evita:
- softbox enormi → perdi potenza

Usa:
- light dome medio
- oppure diffusione leggera + reflector

---

# 📊 Riassunto diretto

| Scelta | Ha senso? | Perché |
|---|---|---|
| 150W | ❌ | troppo debole |
| 300W (300d / Forza 300) | ✅ | equilibrio perfetto |
| 600W | ⚠️ | solo casi estremi |

---

# 🧠 CONCLUSIONE

Per il tuo caso specifico:

> **Aputure 300d II + 4 batterie V-mount è la scelta più intelligente**

- abbastanza potente
- gestibile da solo
- autonomia sufficiente
- risultato consistente

---

Se vuoi fare un lavoro fatto davvero bene, il passo successivo non è aumentare i watt ma:
- capire **dove posizionarti rispetto al sole**
- e che **setup di diffusione usare**

Se vuoi, ti costruisco uno schema preciso di setup (posizione luce + sole + camera) per avere risultato pulito sempre, anche con nuvole che vanno e vengono.