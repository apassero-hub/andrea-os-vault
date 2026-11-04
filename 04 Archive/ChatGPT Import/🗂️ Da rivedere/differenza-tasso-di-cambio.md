---
title: "Differenza tasso di cambio"
created: 2026-04-11
updated: 2026-04-11
model: gpt-5-3
messages: 20
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Differenza tasso di cambio

> Importato da ChatGPT export · 20 messaggi · gpt-5-3 · 2026-04-11

## 🧑 User

Allora, oggi il tasso di conversione effettivo dollaro-euro, cioè euro-dollaro, è 1,17. Cioè, 1,17 dollari fanno un euro. Sto facendo un acquisto dagli Stati Uniti. Quello che non capisco è perché su PayPal, cioè su PayPal, su eBay, mi dice paga adesso e mi fa il resoconto e mi dice sono 1600 e rotti. Poi faccio paga, mi fa il resoconto e sono tipo 50 euro in più. Che cazzo può essere?

---

## 🤖 Assistant

È normale. Non è un errore: stai vedendo **due tassi di cambio diversi + commissioni nascoste**.

Ti spiego cosa succede davvero, senza giri:

---

## 1) Il tasso 1,17 NON è quello che usi tu
Quel **1,17 USD/EUR** è il tasso **interbancario** (quello “pulito” dei mercati).

Tu però stai pagando tramite:
- entity["company","PayPal","pagamenti online"]
- entity["company","eBay","piattaforma ecommerce"]

Entrambi applicano un **tasso peggiorato**.

👉 Tipicamente:
- PayPal aggiunge un **+3% / +4%**
- eBay fa lo stesso se gestisce lui la conversione

Quindi il tuo 1,17 diventa facilmente tipo **1,13–1,14 reale**

---

## 2) Dove saltano fuori quei ~50€
Facciamo un esempio rapido:

- Importo: 1800 USD
- Con tasso reale (1,17): ~1538 €
- Con tasso PayPal (~1,13): ~1592 €

👉 Differenza: **50+ €**
Esattamente quello che stai vedendo.

---

## 3) Perché cambia tra “prima schermata” e “paga”
Questo è il punto chiave:

- Prima schermata → **stima / preview**
- Schermata finale → **conversione reale applicata**

E spesso:
- la preview usa un tasso più “ottimistico”
- oppure cambia il soggetto che converte (eBay vs PayPal)

---

## 4) Il vero problema (che puoi evitare)
Quasi sicuramente stai lasciando che PayPal faccia la conversione.

Errore.

👉 Devi sempre:
- Pagare in USD
- Far fare il cambio alla tua banca/carta

Perché:
- Visa/Mastercard stanno ~0.5–1% sopra il mercato
- PayPal sta ~3–4%

---

## 5) Cosa fare subito
Quando paghi con PayPal:

1. Vai su “opzioni di conversione”
2. Seleziona:
👉 **“Addebita nella valuta del venditore (USD)”**
3. NON usare la conversione PayPal

---

## Sintesi secca
Non ti stanno fregando “a caso”:
- Ti stanno applicando un cambio peggiore
- + margine nascosto di PayPal
- + possibile doppia conversione

👉 Quei 50€ sono **commissione mascherata nel cambio**.

---

Se vuoi, dimmi:
- importo in USD
- carta che stai usando

Ti calcolo quanto dovresti pagare “giusto” e quanto ti stanno caricando realmente.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

_[contenuto non testuale: image_asset_pointer]_

Ho provato a selezionare Apple Pay da come alternativa PayPal su eBay, però la cifra rimane la stessa.

---

## 🤖 Assistant

Qui è chiarissimo cosa sta succedendo. Non è PayPal il problema principale: è **entity["company","eBay","piattaforma ecommerce"] che sta già facendo il cambio prima ancora del pagamento**.

---

## 🔴 Il punto chiave (che ti sta fregando)
Nella seconda schermata c’è scritto:

> **€1 = $1,12596**

Questo è il tasso che stanno usando.

Tu hai detto:
- reale: **1,17**
- eBay usa: **1,12596**

👉 Differenza: circa **-3,8%**

Su 1958$:
- cambio reale → ~1673 € (quello che vedevi prima)
- cambio eBay → **1739 €**

👉 **+66 € di differenza**

Non è una coincidenza. È esattamente il margine.

---

## 🔴 Perché Apple Pay NON cambia nulla
Hai fatto una prova giusta, ma inutile in questo caso.

👉 Apple Pay entra **dopo**
👉 Il cambio lo ha già deciso eBay

Quindi:
- PayPal o Apple Pay = stesso importo
- perché stai pagando **già in euro**

---

## 🔴 Il vero problema
Stai usando:
👉 **conversione interna eBay**

E non puoi evitarla direttamente da lì perché:
- il listing è in USD
- ma eBay forza il checkout in EUR

---

## 🟢 Come risolvere davvero (se possibile)

### Opzione 1 — Pagare in USD (migliore)
Devi trovare il modo di:
- vedere il prezzo in USD
- pagare in USD

A volte puoi:
- cambiare valuta su eBay (in basso o nelle impostazioni)
- oppure usare versione desktop

Se funziona:
👉 paghi 1958$
👉 la carta fa il cambio (molto meglio)

---

### Opzione 2 — Contattare il venditore
Se è disponibile:
- chiedi pagamento diretto PayPal in USD (fuori eBay, meno sicuro)
- oppure invoice in USD

---

### Opzione 3 — Accettare la perdita
Se non puoi evitarlo:
👉 quei 60–70€ sono il “costo nascosto” di eBay

---

## 🔴 Sintesi brutale
- Non è un bug
- Non è PayPal
- È eBay che ti applica un cambio peggiorato
- Apple Pay non cambia nulla perché il danno è già fatto

---

Se vuoi, ti dico esattamente:
👉 come forzare eBay a mostrarti USD (funziona, ma dipende da come è impostato l’account)

---

## 🧑 User

Ok, se lo faccio in... posso selezionare i dollari, se posto i dollari americani e faccio il pagamento con PayPal, in questo caso qua magari farei un pagamento tipo dilazionato in tre rate, quello classico PayPal. Potrebbe essere più vantaggioso?

---

## 🤖 Assistant

Risposta secca: **no, non è più vantaggioso.**
Anzi, spesso è leggermente peggio.

---

## 🔴 Il punto chiave
Anche se:
- imposti USD su entity["company","eBay","piattaforma ecommerce"]
- paghi con entity["company","PayPal","pagamenti online"]

👉 **se usi il pagamento in 3 rate, quasi sempre il cambio lo fa PayPal**
E PayPal usa un tasso peggiore rispetto alla carta.

---

## ⚠️ Perché peggiora con “Pay in 3”
Quando attivi il pagamento rateale:

- PayPal **deve convertirti l’importo in EUR subito**
- blocca l’importo in euro
- e poi ti rateizza

👉 Risultato:
- perdi la possibilità di pagare in USD
- perdi il cambio buono della carta
- ti becchi il cambio PayPal (~3–4% peggiore)

---

## 📉 Tradotto in soldi (il tuo caso)
Importo: ~1958$

- Carta (Visa/Mastercard): ~1670–1690 €
- PayPal cambio suo: ~1730–1750 €

👉 Differenza: **50–80 € buttati**

---

## 🔴 Quindi:
| Metodo | Convenienza |
|--------|------------|
| Carta in USD | ✅ migliore |
| PayPal in USD (senza conversione) | ⚠️ ok |
| PayPal Pay in 3 | ❌ peggiore |

---

## 🟢 Quando ha senso usare PayPal in 3
Solo se:
- ti serve liquidità
- non puoi pagare tutto subito

👉 ma **stai pagando il finanziamento in modo nascosto nel cambio**

---

## 🔴 Strategia migliore in assoluto
1. Metti eBay in USD
2. Vai al pagamento
3. Usa PayPal SOLO come gateway
4. **Seleziona “paga nella valuta del venditore (USD)”**
5. Lascia fare il cambio alla carta

---

## Sintesi finale
Vuoi risparmiare → paga in USD con carta
Vuoi dilazionare → accetti 50–80€ in più

Non c’è una via “furba” che fa entrambe le cose.

---

Se vuoi, dimmi che carta usi (Revolut, banca classica, Amex ecc.)
Ti dico esattamente quanto pagheresti al centesimo.

---

## 🧑 User

Riusciamo a scoprire qual è il tasso a oggi di PayPal per i pagamenti?

---

## 🤖 Assistant

Sì, e possiamo essere precisi.

## 📊 Tasso PayPal oggi (come funziona davvero)
PayPal **non pubblica un tasso fisso tipo “1,13” valido sempre**.
Fa così:

👉 prende il tasso reale (interbancario)
👉 **aggiunge un margine sopra**

---

## 🔴 Quanto è questo margine?
Dati aggiornati:

- **~3% – 4% sopra il tasso reale** cite
- In alcuni casi specifici:
- ~3% minimo cite
- fino a ~4% o più cite

👉 Questo è esattamente quello che stai vedendo nel tuo caso.

---

## 📉 Tradotto sul tuo esempio reale
Hai detto:
- tasso reale: **1,17**
- eBay ti mostrava: **1,12596**

Calcolo:

- 1,17 → 1,12596 = **-3,8%**

👉 Perfettamente dentro il range PayPal (3–4%)

---

## 🔴 Quindi qual è il “tasso PayPal oggi”?
Non è uno solo, ma puoi stimarlo così:

👉 **tasso PayPal ≈ tasso reale - 3% / 4%**

Esempio pratico:
- reale: 1,17
- PayPal:
- ~1,13 (−3%)
- ~1,12 (−4%)

👉 Esattamente il numero che hai visto.

---

## ⚠️ Punto importante
Quello che ti frega è che:

- **NON vedi la commissione**
- è **nascosta nel cambio**

PayPal stesso conferma che:
👉 il costo è “incluso nel tasso di conversione mostrato prima del pagamento” cite

---

## 🟢 Confronto reale

| Metodo | Margine |
|--------|--------|
| Carta (Visa/Mastercard) | ~0.5% – 1% |
| PayPal | **~3% – 4%** |
| eBay (conversione interna) | simile a PayPal |

---

## 🎯 Sintesi netta
- PayPal non ha un tasso fisso
- Applica **sempre un cambio peggiorato del 3–4%**
- Il valore che hai visto (1,12596) è assolutamente coerente
- È lì che perdi quei 50–70€

---

Se vuoi, posso dirti **quanto pagheresti preciso al centesimo**:
- con PayPal
- con carta
- con Revolut (che è spesso il migliore)

Così capisci se vale la pena cambiare metodo oppure no.

---

## 🧑 User

E se lo facessi con la mia carta, con N26?

---

## 🤖 Assistant

Qui cambia tutto. Con **entity["company","N26","banca digitale"] sei nella situazione migliore possibile.**

---

## 🟢 Come funziona davvero N26 sul cambio
- Usa il circuito Mastercard
- Applica **tasso reale di mercato (quasi identico a quello che vedi su Google)**
- **Zero maggiorazioni di N26** cite

👉 Tradotto:
- niente +3/4% come PayPal
- niente cambio “gonfiato” come eBay

---

## 📊 Quanto pagheresti nel tuo caso

Importo: **1958$**

### Scenario 1 — eBay / PayPal (quello che stai vedendo)
- ~1739 €
👉 cambio pessimo (~1,125)

---

### Scenario 2 — N26 (pagando in USD)
- tasso reale ~1,17
- 1958$ → **~1673 €**

👉 Risparmio: **~60–70 €**

---

## 🔴 Condizione fondamentale (IMPORTANTISSIMO)
Devi fare UNA cosa giusta:

👉 **pagare in USD, NON in EUR**

Se sbagli questo:
- torni punto e a capo
- eBay ti applica il suo cambio di merda

---

## ✅ Setup corretto (passaggi chiari)
Quando paghi:

1. Su entity["company","eBay","piattaforma ecommerce"] → imposta USD
2. Vai al checkout
3. Se usi PayPal:
- scegli **“paga nella valuta del venditore (USD)”**
4. Oppure ancora meglio:
- paga direttamente con carta N26 (Apple Pay incluso)
- ma SOLO se l’importo è in USD

---

## ⚠️ Nota reale (non marketing)
- Mastercard non è **esattamente** il tasso interbancario
- ma è molto vicino (~0.2–0.5% differenza)

👉 praticamente trascurabile rispetto al 4% di PayPal

---

## 🔴 Confronto secco

| Metodo | Quanto paghi |
|--------|------------|
| eBay / PayPal (EUR) | ~1739 € |
| N26 (USD) | ~1670 € |
| Differenza | **~70 €** |

---

## 🎯 Sintesi brutale
- Con N26 stai giocando nel campionato giusto
- Il problema NON è la carta
- È **chi fa il cambio**

👉 Se lo fai fare a N26 → risparmi
👉 Se lo fa eBay/PayPal → perdi soldi

---

Se vuoi, ti dico **come forzare eBay a NON convertirti in EUR** (perché a volte è nascosto e rompe le palle).

---

## 🧑 User

Okay, quindi Apple Pay va bene, perché tanto lì si appoggia alla carta N26. Perfetto. E se lo faccio invece che con N26, se lo faccio con Revolut?

---

## 🤖 Assistant

Risposta pulita: **Revolut è leggermente meglio di N26… ma non sempre.**

Ti spiego senza confusione.

---

## 🟢 Revolut vs N26 (quello che ti interessa davvero)

### 👉 entity["company","Revolut","fintech bancaria"]
- Cambio **molto vicino al mercato reale**
- Nei giorni feriali: **praticamente zero commissioni** entro certi limiti cite
- Weekend: **+1% di fee** cite
- Sopra una certa soglia mensile: **+1% circa** cite

---

### 👉 entity["company","N26","banca digitale"]
- Usa circuito Mastercard
- Cambio **quasi reale**, leggermente meno preciso
- Nessuna sorpresa, nessun limite

---

## 📊 Nel tuo caso specifico (1958$)

### Scenario reale (giorno feriale, dentro limiti Revolut)
- Revolut: ~**1670 €**
- N26: ~**1673–1680 €**

👉 Differenza: **pochi euro**

---

### Scenario peggiore Revolut
- Se è weekend → +1%
- Se superi limiti → +1%

👉 1670 € → ~1685–1690 €

➡️ A quel punto diventa **uguale o peggio di N26**

---

## 🔴 Differenza vera tra i due

| Aspetto | Revolut | N26 |
|--------|--------|-----|
| Precisione cambio | 🔥 leggermente migliore | ottimo |
| Commissioni | 0% (ma con condizioni) | sempre 0% |
| Limiti | sì | no |
| Weekend | ❌ +1% | ✅ nessuna variazione |

---

## 🟢 Strategia intelligente (quella giusta)

👉 Usa **Revolut solo se:**
- sei in settimana
- sei sotto i limiti
- vuoi spremere anche gli ultimi 2–5€

👉 Usa **N26 se:**
- non vuoi pensare a niente
- è weekend
- non sai se sfori limiti

---

## 🔴 ERRORE DA NON FARE (vale per entrambi)
Sempre:

👉 **pagare in USD**
👉 mai accettare conversione eBay / PayPal

Se sbagli questo:
- perdi tutto il vantaggio
- torni a pagare +60/70€

---

## 🎯 Sintesi finale
- Revolut = **teoricamente il migliore**
- N26 = **più stabile e senza rotture**
- PayPal / eBay = **da evitare sempre**

👉 Nel tuo caso:
se stai pagando adesso → usa Revolut (se è feriale)
se è weekend → vai diretto di N26 e chiudi lì

---

Se vuoi ti faccio il calcolo preciso **in tempo reale** (ti dico quanto ti esce su Revolut ORA vs N26), così scegli senza andare a tentativi.

---

## 🧑 User

Tazio io, Revolut ho la carta Visa invece.

---

## 🤖 Assistant

Perfetto, cambia poco ma è giusto chiarirlo bene.

## 🔵 Revolut Visa vs Mastercard (impatto reale)
Con entity["company","Revolut","fintech bancaria"]:

- Se paghi **con saldo in USD già convertito** →
👉 **nessuna differenza** tra Visa e Mastercard
(stai usando il cambio Revolut, non quello del circuito)

- Se paghi **direttamente in USD senza saldo USD** →
👉 entra in gioco il circuito (Visa nel tuo caso)

---

## 📊 Quanto cambia davvero Visa
- entity["company","Visa","circuito di pagamento"] ha un tasso **quasi identico** a Mastercard
- differenza reale: **0.1% – 0.3% max**

👉 su 1700€:
- parliamo di **1–5€ di differenza**, non di più

---

## 🔴 Il vero punto (più importante del circuito)
Con Revolut la differenza grossa NON è Visa vs Mastercard, ma:

### 👉 se fai il cambio prima o durante il pagamento

---

## 🟢 Strategia migliore con Revolut (la più efficiente)

### Metodo TOP
1. Apri Revolut
2. Converti manualmente EUR → USD
3. Poi paghi in USD

👉 risultato:
- cambio reale puro
- zero sorprese
- zero extra nascosti

---

### Metodo “ok ma meno controllato”
- paghi direttamente in USD
- Revolut converte al momento

👉 comunque buono, ma:
- meno controllo su timing
- possibile +1% se weekend

---

## ⚠️ Attenzione reale (questa conta davvero)
Se oggi è:
- **giorno feriale** → perfetto
- **weekend** → Revolut ti aggiunge ~1%

👉 quindi:
- se sei nel weekend → meglio N26
- se sei in settimana → Revolut è top

---

## 🔴 Riepilogo secco

| Metodo | Risultato |
|--------|----------|
| Revolut (USD pre-convertiti) | 🔥 migliore in assoluto |
| Revolut diretto | ottimo |
| N26 | stabile e sicuro |
| PayPal / eBay | ❌ soldi buttati |

---

## 🎯 Conclusione
- Il fatto che sia Visa **non cambia nulla di rilevante**
- La vera differenza la fai **evitando il cambio eBay/PayPal**
- Se vuoi fare le cose perfette:
👉 converti in USD su Revolut e paga così

---

Se vuoi, dimmi quando stai pagando (oggi/orario)
ti dico al centesimo se ti conviene Revolut o N26 in quel momento preciso.

---

## 🧑 User

E se pago dal mio conto Unicredit?

---

## 🤖 Assistant

Risposta diretta: **UniCredit è meglio di PayPal… ma peggio di N26 e Revolut.**

---

## 🔴 Come funziona davvero UniCredit
Con entity["company","UniCredit","banca italiana"]:

- Usa il cambio del circuito (Visa/Mastercard)
- **+ maggiorazione aggiuntiva della banca**

👉 Tipicamente:
- **+0,9% (credito Visa)** cite
- **+1,75% (debito/prepagata)** cite

---

## 📊 Tradotto sul tuo caso (1958$)

### Scenario UniCredit (realistico)
- tasso reale: 1,17
- con +1% circa → ~1,155
- risultato: **~1695–1710 €**

---

## 📉 Confronto reale

| Metodo | Quanto paghi |
|--------|------------|
| eBay / PayPal | ~1739 € |
| UniCredit | ~1700 € |
| N26 | ~1670 € |
| Revolut (best case) | ~1670 € |

---

## 🔴 Quindi:
- Risparmi rispetto a PayPal → **sì (~30–40€)**
- Ma perdi rispetto a N26/Revolut → **sì (~20–30€)**

---

## ⚠️ Attenzione importante
Vale anche qui:

👉 se paghi in EUR → ti fregano (eBay)
👉 se paghi in USD → decide la banca

---

## 🟢 Quando ha senso usare UniCredit
- Se non hai alternative disponibili
- Se ti serve plafond alto (credito)
- Se non vuoi usare fintech

---

## 🔴 Quando NON usarla
Nel tuo caso specifico:

👉 hai già:
- N26
- Revolut

Quindi:
👉 **UniCredit è semplicemente la scelta peggiore tra quelle che hai**

---

## 🎯 Sintesi brutale
- PayPal / eBay → ❌ peggio in assoluto
- UniCredit → ⚠️ medio (ma costa comunque)
- N26 / Revolut → ✅ giusto

👉 Se vuoi pagare il meno possibile:
**Revolut (feriale) → N26 (backup) → UniCredit solo se costretto**

---

Se vuoi chiudiamo il cerchio:
dimmi che giorno/ora paghi e che tipo di carta UniCredit hai (debito o credito), ti dico **quanto ti esce preciso al centesimo**.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Pagato con n26 e ho pagato 1677

---

## 🤖 Assistant

Perfetto, ed è esattamente il risultato che dovevi ottenere.

## 📊 Analisi del tuo pagamento
Hai pagato:

- **1958,22 $**
- con entity["company","N26","banca digitale"]
- totale: **1677 €**

Il tasso che ti ha applicato è:
- **0,8564 EUR/USD** → equivalente a ~**1,167 USD/EUR**

👉 Questo è **praticamente il tasso reale di mercato**

---

## 🔥 Tradotto: hai fatto la scelta giusta
Confronto reale:

| Metodo | Totale |
|--------|--------|
| N26 (tuo pagamento) | **1677 €** |
| eBay / PayPal | ~1739 € |
| Differenza | **+62 € risparmiati** |

---

## 🔴 Cosa hai fatto giusto (senza errori)
- Hai pagato in **USD**
- Hai evitato conversione eBay
- Hai evitato conversione PayPal
- Hai lasciato fare il cambio alla carta

👉 risultato: **quasi perfetto**

---

## ⚠️ Nota tecnica sul tasso
Quel **0,8564**:
- include già il micro spread Mastercard (~0.2–0.4%)
- è assolutamente nella norma

👉 non potevi fare meglio in modo realistico

---

## 🎯 Sintesi finale
- Hai evitato una perdita inutile di ~60€
- Il tasso è corretto
- Il metodo è quello giusto

👉 Operazione fatta bene, punto.

---

Se vuoi ottimizzare ancora di più in futuro:
- ti spiego quando conviene usare Revolut invece di N26 (ci sono 2–3 casi specifici dove cambia davvero)

---

## 🧑 User

Grazie

---

## 🤖 Assistant

Perfetto, hai gestito tutto nel modo corretto.

Se ti ricapita:
- paga sempre in valuta originale
- evita conversioni di piattaforme
- usa N26 o Revolut in base al contesto

Se hai altri dubbi su pagamenti o acquisti dall’estero, vai diretto.