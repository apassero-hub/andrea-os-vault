---
title: "Retrofit sensori Golf 7"
created: 2025-10-13
updated: 2025-10-13
model: gpt-5
messages: 6
source: chatgpt-import
tags: []
---

# Retrofit sensori Golf 7

> Importato da ChatGPT export · 6 messaggi · gpt-5 · 2025-10-13

## 🧑 User

Se sulla mia Golf 7 2014 si fanno retrofit dei sensori posteriori soltanto, quelli originali da poter poi attivare sull'infotainment, può darsi che ci sia già, come per tante altre cose, la predisposizione sul cablaggio e a cui io devo assolutamente aggiungere la parte terminale del cablaggio con i sensori oppure devo cablare tutto quanto dall'infotainment.

---

## 🤖 Assistant

Nel caso della **Golf 7 del 2014 (piattaforma MQB)**, la situazione per i sensori di parcheggio **posteriori originali (OPS – Optical Parking System)** è la seguente:

---

### ⚙️ Predisposizione di fabbrica
- La **predisposizione parziale** è presente **solo su alcune versioni** (in genere *Comfortline* o superiori, o se l’auto aveva già il pacchetto “Preparazione Park Pilot”).
- Se la tua Golf **non aveva già sensori posteriori o anteriori di serie**, **quasi certamente non ha la predisposizione completa**: troverai al massimo dei connettori ciechi vicino al paraurti posteriore, ma **non il cablaggio fino alla centralina del Park Pilot (J446)**.

---

### 🔌 Componenti necessari per retrofit OEM completo
1. **4 sensori posteriori originali** (con staffe e supporti, codice tipico 5Q0919279).
2. **Cablaggio posteriore completo**, dal paraurti fino:
- alla **centralina Park Pilot (J446)** nel lato sinistro del bagagliaio, oppure
- direttamente all’unità CAN nel caso si voglia bypassare la J446 e usare l’infotainment con codifica “OPS lite”.
3. **Centralina Park Pilot J446** (se non già presente nel gateway; codice comune 5Q0919294 o varianti).
4. **Cablaggio di alimentazione e CAN-BUS** dalla J446 al gateway o al BCM.
5. **Codifica via OBDeleven/VCDS**:
- Abilitazione modulo Park Pilot (indirizzo 10 o 76).
- Attivazione visualizzazione OPS nell’infotainment.
- In alcuni casi, aggiornamento del **dataset nel 5F (infotainment)** per far comparire la grafica.

---

### 🔎 Come verificare se hai la predisposizione
Puoi controllare in modo semplice:
1. Rimuovi il **pannello laterale sinistro del bagagliaio**.
- Se trovi un connettore libero a 12 pin (grigio o nero) con fascetta che termina lì, **hai la predisposizione**: ti basta il cablaggio corto con sensori e la centralina.
2. Se non trovi nulla, significa che **devi stendere l’intero cablaggio** dal paraurti fino al gateway.

---

### 💡 In sintesi
| Situazione | Cosa serve fare |
|-------------|-----------------|
| Predisposizione presente | Collega i sensori + cablaggio corto e centralina, poi codifica. |
| Nessuna predisposizione | Cablaggio completo nuovo (dal posteriore al BCM/gateway), centralina + codifica OPS. |
| Vuoi solo acustico (no grafica OPS) | Esiste kit aftermarket OEM-like con buzzer e cablaggio semplificato, nessuna codifica infotainment. |

---

Se mi dai **il codice PR del veicolo** (lo trovi nell’etichetta del vano ruota di scorta o nel libretto uso e manutenzione), posso dirti con certezza se la tua versione ha o meno la predisposizione per il Park Pilot. Vuoi che lo controlli?

---

## 🧑 User

La mia è una versione Highline, con l'infotainment quello con il navigatore, MIB1 con il navigatore. Come cazzo si chiamava? Vabbè, adesso mi ricordo. Cos'altro? Versione Highline Business.

---

## 🤖 Assistant

Perfetto, allora il quadro è chiaro.
La **Golf 7 Highline Business 2014 con MIB1 Discover Media (navigatore integrato)** ha una dotazione elettrica piuttosto completa, ma **non necessariamente la predisposizione fisica dei sensori posteriori** — anche se è *molto probabile* che parte del cablaggio ci sia già.

Vediamolo punto per punto in modo tecnico:

---

### 🔍 1. Predisposizione effettiva su Highline Business
Su molte **Highline Business 2014** senza Park Pilot, **Volkswagen montava già parte del cablaggio nel retrotreno**, precisamente:
- il **connettore a 12 pin** nel lato sinistro del bagagliaio, vicino al passaruota interno,
- e la linea CAN già disponibile nel fascio cavi principale.

👉 Quindi **hai buone probabilità che la predisposizione sia presente fino al vano sinistro del bagagliaio**.
Manca però:
- il **cablaggio breve del paraurti posteriore (4 sensori)**,
- la **centralina J446 (Park/Steer Assist)**,
- e, ovviamente, la **codifica software**.

---

### ⚙️ 2. Componenti OEM richiesti per retrofit completo
Per fare il lavoro **come da fabbrica**, ti serve:

| Componente | Codice indicativo | Note |
|-------------|------------------|------|
| 4 sensori posteriori ultrasonici | 5Q0 919 275 (x4) | Solo posteriori |
| Cablaggio corto posteriore | 5Q0 971 084 L (o simile) | Dalla centralina ai sensori |
| Centralina Park Pilot | 5Q0 919 294 K (o G) | Versione solo posteriore |
| Staffe + supporti per paraurti | – | Da incollare o saldare a caldo |
| Cavo di collegamento centrale–CAN | 5Q0 971 425 | Dalla centralina al gateway (se non predisposta) |

💡 Alcuni cablaggi aftermarket (es. Kufatec o Carsystems) integrano già tutto, con connettori OEM e lunghezze corrette.

---

### 🧠 3. Attivazione via diagnosi
Dopo l’installazione serve:

- **Codifica modulo 10 o 76 (Park Assist)** → “Rear sensors installed”.
- **Attivazione OPS nel modulo 5F (Infotainment)** → per avere la visualizzazione grafica.
- Eventuale **adattamento del tono buzzer e distanza di intervento**.

Con OBDeleven o VCDS si fa in pochi minuti.

---

### 💬 4. Cosa succede se non hai la predisposizione
Se aprendo il pannello sinistro **non trovi il connettore a 12 pin**, allora devi:
- portare **un nuovo cablaggio dal retro al gateway sotto il cruscotto** (lavoro più lungo ma fattibile),
- oppure scegliere un **kit aftermarket “OEM style”** (con sensori originali ma centralina propria) da attivare solo acusticamente.

---

### ✅ 5. Conclusione pratica
Nel tuo caso (Highline Business + MIB1 Discover Media):
- **predisposizione probabile al 70–80%**, da verificare fisicamente;
- **infotainment già compatibile** con la grafica OPS originale;
- **retrofit perfettamente integrabile**, basta aggiungere il cablaggio corto, i sensori e la centralina, poi codificare.

---

Se vuoi, posso indicarti **il codice esatto del cablaggio Kufatec** più corretto per il tuo modello (quello plug-and-play da collegare dietro al rivestimento sinistro, senza tirare fili fino al cruscotto).
Vuoi che te lo cerchi?

---

## 🧑 User

Posso codificarlo con lo BD11, mi sembra, vero? E se così fosse, che bastassero solo questi pezzi qua, quanto sarebbe la spesa? Ovviamente usati, eh. L'ideale sarebbe trovare un parlor di grigio come nella mia macchina, con già i sensori e il pezzo di carlaggio. Quello sarebbe l'ideale.

---

## 🤖 Assistant

Sì: **lo codifichi con OBDeleven** senza problemi.
Se la vettura è una **Highline Business 2014 – MIB1 Discover Media**, l’infotainment supporta la grafica **OPS**.

# Cosa serve (solo posteriori, OEM)
- **4 sensori PDC** (es. 5Q0 919 275 A/B/C). Usato: ~25–40 € cad. cite
- **Cablaggio paraurti posteriore** (loom corto) + **staffe** per incollaggio. Usato/aftermarket: ~40–100 € complessivi. *(Kufatec vende kit completi)*. cite
- **Centralina Park Pilot J446** (solo posteriori, es. 5Q0 919 294 K/G). Usato: ~60–120 €. cite
- **Eventuale cablaggio J446→CAN** se non hai la predisposizione nel vano sinistro bagagliaio. *(Con predisposizione, non serve tirare cavi fino al cruscotto.)*

### Alternativa “pezzo unico”
- **Paraurti posteriore già con sensori e cablaggio** del donatore (ideale). Usato: ~200–400 € a seconda di colore/condizioni. cite

# Costi indicativi (usato, fai-da-te)
- **Scenario A – trovi paraurti completo con sensori/loom:** 200–400 € + codifica. cite
- **Scenario B – componi i pezzi:**
- Sensori 100–160 € (4 pz) + loom/staffe 40–100 € + J446 60–120 € ⇒ **~200–380 €**. cite
- **Scenario C – kit nuovo plug&play (Kufatec Park Pilot Rear):** ~400 € nuovo (senza verniciatura). cite

> Nota prezzi: kit completi F/R nuovi vanno oltre (**630–750 €**), utile come riferimento del tetto massimo. cite

# Codifica con OBDeleven (sintesi operativa)
1. **Modulo 10/76 – Park Assist:** long coding → *Rear sensors installed* = **attivo**.
2. **Modulo 5F – Information Electr.:**
- *Car_Function_List_BAP_Gen2 → parking_assist_0x0A* = **attivo + disponibile**.
- *Car_Function_Adaptations_Gen2 → menu_display_parking_assist* = **attivo/visibile**.
3. **Gateway (19):** verifica che il modulo Park Assist sia **spuntato** nella install list.
4. **Adattamenti:** volume/tonalità buzzer e soglie distanza (se presenti).
5. **Fault scan** finale e prova grafica OPS su 5F.

# Cosa controllare prima di comprare
- **Predisposizione:** cerca nel **lato sinistro del bagagliaio** un connettore libero (12 pin). Se c’è, ti basta loom corto + J446; se non c’è, serve il cavo J446→CAN.
- **Varianti centralina:** prendi **versione “rear only”** compatibile MQB (5Q0 919 294 *…*). cite
- **Sensori:** gli OEM spesso arrivano **primer (GRU)** e vanno verniciati in tinta; verifica numero (A/B/C) e **angolatori/staffe** corrette per il tuo paraurti. cite

# Risposta secca alla tua domanda
- **Sì, OBDeleven basta.**
- **Sì, puoi cavartela solo con questi pezzi** (sensori + loom paraurti + J446), **se** hai la **predisposizione nel vano sinistro**. In assenza, serve anche il **cavo verso il CAN**.
- Con un **paraurti grigio completo** del donatore riduci tempi e rischi; budget **~200–400 €** usato ben trovato. cite

Se vuoi, ti faccio una **checklist fotografica** dei connettori da cercare nel bagagliaio e degli ID etichetta su J446/sensori per evitare acquisti sbagliati.