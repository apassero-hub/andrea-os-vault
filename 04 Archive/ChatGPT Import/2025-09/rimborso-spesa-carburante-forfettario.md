---
title: "Rimborso spesa carburante forfettario"
created: 2025-09-24
updated: 2025-09-24
model: gpt-5
messages: 11
source: chatgpt-import
tags: []
---

# Rimborso spesa carburante forfettario

> Importato da ChatGPT export · 11 messaggi · gpt-5 · 2025-09-24

## 🧑 User

se col forfettario devo richiedere un rimborso per una spesa anticipata per conto del cliente (e già fatta fatturare direttamente a loro ma pagata da me), qual è già la dicitura precisa da mettere? nello specifico parliamo della benzina

---

## 🤖 Assistant

Chiaro: se sei in **regime forfettario**, non puoi portare a costo spese come benzina o trasferte, né riaddebitare con IVA. L’unico modo corretto è trattarle come **spese anticipate in nome e per conto del cliente** (art. 15 DPR 633/72).

⚠️ Condizione fondamentale:
- la fattura della spesa (es. carburante) deve essere intestata **direttamente al cliente**, non a te.
- tu hai solo anticipato il pagamento.

In questo caso puoi riportare l’importo a piè di fattura, fuori dal reddito imponibile e senza IVA, con la seguente dicitura tipica:

> **“Rimborso spese anticipate in nome e per conto del cliente ex art. 15 DPR 633/72 – carburante”**

E indichi l’importo esatto che hai anticipato.

Se invece la fattura della benzina è stata intestata a te, non puoi farla rientrare come spesa anticipata ex art. 15: in quel caso l’unica via sarebbe inserirla come parte del compenso (quindi tassata e senza possibilità di scaricarla).

Vuoi che ti prepari un fac-simile di fattura con entrambe le casistiche (spesa intestata al cliente vs intestata a te) così vedi la differenza pratica?

---

## 🧑 User

per l'autostrada invece il cliente mi ha detto di maggiorarne il costo sulla base delle tasse di modo che poi a me resti al netto la spesa autostradale. quando conteggio?

---

## 🧑 User

non supporlo facciamo un calcolo giusto. gestione separata inps, tassazione al 15% in forfettario con indice di redditività al 78%

---

## 🤖 Assistant

Perfetto, andiamo al sodo con i tuoi parametri:

- **Regime forfettario servizi** → coefficiente redditività: **78%**
- **Gestione separata INPS** → contributi 26,07% (2025)
- **Imposta sostitutiva**: 15%
- Metodo:
1. Calcoliamo imponibile = fatturato × 78%
2. Su imponibile calcoliamo INPS e imposta sostitutiva
3. Li scaliamo dal lordo per sapere cosa ti resta

### Esempio spesa autostrada 100 € (anticipata ma da ribaltare su fattura)
Il cliente vuole che a te resti **netto = 100 €**.
Dobbiamo quindi “lordizzare” il rimborso.

---

#### Calcolo step by step
1. Supponiamo che tu fatturi un importo **X** come “rimborso spese autostrada”.
2. Reddito imponibile = X × 78%
3. Contributi INPS = imponibile × 26,07%
4. Imposta sostitutiva = imponibile × 15%
5. Netto che ti rimane = X – (INPS + imposta)

---

#### Formula semplificata
- Netto = X × [1 – (78% × (26,07% + 15%))]
- Netto = X × [1 – 0,780 × 0,4107]
- Netto = X × [1 – 0,320]
- Netto ≈ **X × 0,68**

Quindi a te rimane circa **68%** di quello che fatturi.

---

#### Ribaltamento corretto
Se vuoi che il netto = 100 €, devi fatturare:
X = 100 / 0,68 ≈ **147 €**

---

✅ Risultato:
Per ogni 100 € di spese reali che vuoi recuperare nette, devi maggiorare in fattura a circa **147 €**.

Vuoi che ti prepari una **tabella Excel pronta** (colonne: spesa effettiva, quanto fatturare, quanto resta al netto) così la usi ogni volta senza rifare i conti?

---

## 🧑 User

sono 45,80€ per tratta (2 tratte)

---

## 🤖 Assistant

Perfetto, quindi parliamo di:

- **45,80 € × 2 = 91,60 € di spesa reale**

Ora facciamo il ribaltamento come prima, con i tuoi parametri fiscali.

---

### Calcolo
- Netto target: **91,60 €**
- Coefficiente di riduzione: **0,68** (dato dal tuo regime forfettario con INPS + imposta)
- Importo da fatturare:
\(91,60 / 0,68 ≈ 134,71 € \)

---

✅ **Da mettere in fattura: 134,71 €**
Così a te resteranno netti circa **91,60 €**, cioè il costo reale delle due tratte.

Vuoi che ti prepari uno **schema/Excel automatico** dove inserisci la spesa (tipo “autostrada 45,80 × n tratte”) e ti sputa fuori direttamente l’importo da fatturare lordizzato?

---

## 🧑 User

non è poco?

---

## 🤖 Assistant

Ti rifaccio i conti in modo “spaccato”, così vedi dove va ogni euro.

---

### Partiamo da **134,71 € fatturati** (come ti ho calcolato prima)

1. **Imponibile forfettario (78%)**
134,71 × 0,78 = **105,07 €**

2. **Contributi INPS (26,07%)**
105,07 × 0,2607 = **27,38 €**

3. **Imposta sostitutiva (15%)**
105,07 × 0,15 = **15,76 €**

4. **Totale tasse**
27,38 + 15,76 = **43,14 €**

5. **Netto che ti rimane**
134,71 – 43,14 = **91,57 €** (praticamente i tuoi 91,60 € spesi)

---

### Quindi il calcolo è corretto
Con il tuo regime, per recuperare **netti 91,60 €**, devi fatturare circa **134,70 €**.
Il “moltiplicatore” che ti serve in generale è 1,47 (cioè spesa × 1,47).

---

Vuoi che ti imposti un **file Excel già con la formula automatica** (tu metti la spesa reale, lui ti dice subito quanto devi fatturare per rientrare al netto)?

---

## 🧑 User

quindi posso mettere 135

---

## 🤖 Assistant

Esatto.

Se fatturi **135 €**:

- Imponibile: 135 × 0,78 = **105,30 €**
- INPS (26,07%): **27,47 €**
- Imposta sostitutiva (15%): **15,80 €**
- Tasse totali: **43,27 €**
- Netto: 135 – 43,27 = **91,73 €**

👉 Ti rimane in tasca praticamente la tua spesa di **91,60 €**.

Quindi puoi tranquillamente scrivere in fattura **135 €** per il rimborso autostrada. Vuoi che ti scriva la dicitura precisa da inserire in fattura in questo caso (visto che non è una spesa anticipata ex art. 15 ma un rimborso maggiorato)?