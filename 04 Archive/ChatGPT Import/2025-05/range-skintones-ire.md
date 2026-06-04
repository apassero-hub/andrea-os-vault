---
title: "Range skintones IRE"
created: 2025-05-14
updated: 2025-05-14
model: gpt-4o
messages: 14
source: chatgpt-import
tags: []
---

# Range skintones IRE

> Importato da ChatGPT export · 14 messaggi · gpt-4o · 2025-05-14

## 🧑 User

qual è il range degli skintones nella scala ire

---

## 🤖 Assistant

Nella scala **IRE** (Institute of Radio Engineers), che misura il livello di luminosità di un segnale video su una scala da **0 a 100**, gli **skintone** (toni della pelle) umani **cadono generalmente tra i 55 e i 75 IRE**, a seconda del tipo di pelle e della luce.

### 📊 Range orientativo degli skintones in IRE:
- **Pelle molto chiara**: ~**65–75 IRE**
- **Pelle caucasica media**: ~**60–70 IRE**
- **Pelle olivastra o asiatica**: ~**55–65 IRE**
- **Pelle scura**: ~**40–55 IRE**

⚠️ **Nota importante**:
Questi valori non sono assoluti, ma linee guida. La luce incidente, il contrasto della scena, il colore riflesso e la camera (o LUT) usata influenzano il valore reale. In una scena ben esposta, il riferimento di massima usato da molti colorist è **un valore medio tra 60 e 70 IRE** per i toni della pelle, visibili nel **parade o waveform luminance**.

Se vuoi un controllo preciso, lo **skintone line** si può anche tracciare su un vectorscope per controllare la tonalità, oltre alla luminanza. Vuoi anche un riferimento pratico per monitorarlo in DaVinci Resolve o Premiere?

---

## 🧑 User

se dovessi impostare un range utilizzando le zebras per gli skintones quanto imposto?

---

## 🤖 Assistant

Se vuoi usare le **zebra stripes per monitorare gli skintones**, l'impostazione ideale dipende dal tipo di pelle e dalla scena, ma ecco una **linea guida solida e professionale**:

---

### 🎯 **Impostazione consigliata delle zebra stripes per skintones**:
- **Zebra 1**: **65% ±5**
- Quindi imposta le zebre a **60–70% IRE**
- Alcune camere permettono una zebra singola con tolleranza (es. *Set Zebra at 65%, range ±5%*)
- In alternativa, imposta:
- **Zebra 1 = 60%**
- **Zebra 2 = 70%**

---

### 💡 Perché proprio 65%?
- È il **valore medio standard** per i toni della pelle caucasica ben esposti sotto luce neutra.
- Funziona bene anche come riferimento generale, tenendo conto che:
- **Pelli più scure** staranno tra **40–60%**
- **Pelli molto chiare** possono spingersi anche a **70–75%**, ma solo in casi di luce intensa

---

### 🧪 Pro tip:
- Se stai girando in **log** (es. S-Log, V-Log, C-Log), i valori IRE saranno **più bassi e compressi**, quindi:
- Attiva la **LUT di monitoring** sulla camera o sul monitor esterno per avere zebre riferite all'immagine “Rec709” e leggibili correttamente.
- Se non puoi usare una LUT, allora le zebre **non rappresentano accuratamente i valori finali** post-correzione colore.

---

Se mi dici che macchina stai usando (Sony FX3, Canon, ecc.), ti posso indicare esattamente dove trovarla e se la funzione zebra lavora su segnale log o con LUT applicata.

---

## 🧑 User

nella nuova funzione log shooting setting della a7siii cosa posso fare?

---

## 🤖 Assistant

iLa nuova funzione **Log Shooting Setting** introdotta con l'aggiornamento firmware **v4.00** della Sony A7S III offre strumenti avanzati per migliorare l'esperienza di ripresa in log. Ecco cosa puoi fare:

---

### 🎬 **Monitoraggio con LUT durante la ripresa**
Puoi applicare una **LUT (Look-Up Table)** direttamente sul monitor della fotocamera mentre registri in **S-Log3**. Questo ti consente di visualizzare un'anteprima dell'immagine con una colorimetria più vicina al risultato finale, facilitando l'esposizione e la composizione.

---

### 🧰 **Altre funzionalità aggiuntive**
- **Focus Magnifier**: Ora utilizzabile anche in modalità manuale durante la ripresa in log, per una messa a fuoco più precisa.
- **Griglia con proporzione aurea**: Aggiunta una nuova opzione di griglia per aiutarti nella composizione.
- **Bracketing di messa a fuoco**: Possibilità di effettuare scatti continui con variazione automatica del punto di messa a fuoco.
- **Etichette OK/NG/KEEP**: Puoi contrassegnare le clip durante o dopo la registrazione per una gestione più efficiente in post-produzione.

---

### ⚙️ **Come attivare la funzione**
1. Assicurati di aver aggiornato la fotocamera al firmware **v4.00**.
2. Nel menu della fotocamera, vai su **Impostazioni di ripresa** e seleziona **Log Shooting Setting**.
3. Attiva la visualizzazione della LUT desiderata per monitorare l'immagine durante la registrazione.

---

### 💡 **Suggerimenti pratici**
- Utilizza una LUT che corrisponda al tuo flusso di lavoro di post-produzione per avere un'anteprima più realistica.
- Ricorda che la LUT applicata è solo per il monitoraggio e non influisce sul file registrato, che rimane in S-Log3.
- Sfrutta le nuove funzionalità per migliorare la precisione della messa a fuoco e la composizione durante le riprese.

---

Se desideri ulteriori dettagli su come utilizzare al meglio queste nuove funzionalità o su come integrare le LUT nel tuo flusso di lavoro, non esitare a chiedere!

---

## 🧑 User

con l'aggiornamento 4 come imposto l'slog-3?

---

## 🤖 Assistant

iCon l'aggiornamento firmware **v4.00** della Sony A7S III, l'impostazione dell'S-Log3 è stata semplificata grazie alla nuova modalità **Log Shooting Mode**, che consente di applicare una **LUT (Look-Up Table)** direttamente sul monitor della fotocamera durante la registrazione. cite

### 🎬 Come impostare l'S-Log3 sulla Sony A7S III (firmware v4.00)

1. **Aggiorna il firmware**: Assicurati di avere installato il firmware **v4.00**. Se stai aggiornando da una versione precedente alla 3.01, dovrai prima installare la versione 3.01 prima di procedere con la 4.00. cite

2. **Attiva il Log Shooting Mode**:
- Vai nel menu della fotocamera e seleziona **Impostazioni di ripresa**.
- Scegli **Log Shooting Mode**.
- Seleziona **S-Log3** come gamma. Nota che con questo aggiornamento, l'opzione S-Log2 è stata rimossa. cite

3. **Applica una LUT per il monitoraggio**:
- All'interno del **Log Shooting Mode**, puoi scegliere una LUT da applicare al monitor della fotocamera. Questo ti permetterà di visualizzare un'anteprima dell'immagine con una colorimetria più vicina al risultato finale, facilitando l'esposizione e la composizione. cite

4. **Utilizza il Gamma Display Assist**:
- Per una visualizzazione più accurata durante la ripresa in S-Log3, attiva il **Gamma Display Assist**:
- Vai su **Menu** > **Setup** > **Display Option**.
- Attiva **Gamma Display Assist** e seleziona il tipo **S-Log3 → 709(800%)**. Questo applicherà una LUT Rec.709 all'immagine visualizzata, aiutandoti a valutare meglio l'esposizione e i colori durante la ripresa.

Con queste impostazioni, potrai sfruttare al meglio le capacità dell'S-Log3 sulla tua Sony A7S III, ottenendo un'immagine più flessibile per la post-produzione e una migliore esperienza durante le riprese.

---

## 🧑 User

ho il menu in inglese

---

## 🤖 Assistant

Perfetto! Se il tuo menu è in **inglese** e stai usando il **firmware v4.00 o successivo** sulla Sony A7S III, ecco i passaggi per impostare correttamente **S-Log3** con le nuove funzionalità del **Log Shooting Mode**:

---

### 🎬 **Come impostare S-Log3 sulla A7S III (firmware 4.00+)**

#### 1. **Attivare il Log Shooting Mode**
- Vai in:
`Menu > Shooting > Image Quality > Log Shooting Setting`
- Imposta:
- **Log Shooting** → `On`
- **Log Gamma** → `S-Log3`
- **Log Color Gamut** → ad esempio `S-Gamut3.Cine` (standard per color grading in post)

---

#### 2. **Abilitare una LUT di monitoring**
Per vedere un’immagine “colorata” mentre registri in log:

- Vai in:
`Menu > Shooting > LUT > LUT Select`
- Seleziona una LUT predefinita (es. `709(800%)`) o una LUT personalizzata che hai caricato.
- Poi attiva la visione con LUT su monitor:
- `LUT Monitor Display` → `On`

> ⚠️ La LUT viene applicata **solo all’anteprima sul monitor**, **non** al file registrato (che resta log puro).

---

#### 3. **Gamma Display Assist (opzionale, legacy)**
Se **non vuoi usare le nuove LUT**, puoi usare il vecchio metodo:

- Vai in:
`Menu > Setup > Display Option > Gamma Display Assist`
- Imposta:
- **Gamma Display Assist** → `On`
- **Assist Type** → `S-Log3 → 709(800%)`

---

#### 4. **Monitoraggio esposizione (Zebra)**
- Vai in:
`Menu > Exposure > Zebra Display`
- Attiva Zebra: `Zebra Display → On`
- Imposta livello Zebra:
- `Zebra Level → Custom`
- `Set Level → 65`
*(oppure un range tipo 60–70 per monitorare gli skintone)*

---

Se vuoi, ti posso creare una checklist in PDF oppure una LUT Rec709 ottimizzata da caricare sulla camera. Vuoi?

---

## 🧑 User

mi da solo off o flexible iso

---

## 🤖 Assistant

Perfetto, ottima osservazione. Se nel menu **Log Shooting Setting** della tua Sony A7S III vedi solo:

- `Log Shooting: Off / Flexible ISO`

...allora **sei nella modalità corretta** per usare l’S-Log3 con il nuovo firmware, ma Sony ha **semplificato la voce di selezione**.

---

### 🔍 Cosa significa “Flexible ISO” in questo contesto?

Nel nuovo firmware, Sony ha **rimosso il dual setting “PP + ISO” classico** e ora trovi solo due opzioni per il Log Shooting:

- `Off` → disattiva il log (torni ai Picture Profile classici)
- `Flexible ISO` → attiva **S-Log3 + S-Gamut3.Cine** (o altro gamut) con ISO variabile

> ⚠️ Niente più S-Log2, e niente più “Cine EI” a meno che tu non usi la **FX3** o una FX6: sulla A7S III, **l’unico modo per girare in log è con "Flexible ISO"**.

---

### ✅ Come confermare che stai davvero usando S-Log3?

Dopo aver attivato:
- `Menu > Shooting > Log Shooting Setting > Log Shooting → Flexible ISO`

Vai su:
- `Gamma Display Assist` → dovrebbe essere attivo in automatico (oppure attivalo manualmente)
- `LUT > Monitor LUT` → attivabile se vuoi vedere il log con Rec709 sullo schermo
- `Color Gamut` → scegli: `S-Gamut3.Cine` (il più compatibile per grading Rec709)

---

### 📸 Esposizione in Flexible ISO (S-Log3)

In modalità Flexible ISO:
- L’ISO minimo per S-Log3 è **ISO 640** (nativo)
- Puoi salire fino a ISO 12800 o oltre, ma resta in range tra **640 e 2000** per il miglior rapporto segnale/rumore
- Per esposizione: monitora con **zebre al 60–70%** per gli skintones, e controlla waveform se disponibile

---

Vuoi un setup LUT Rec709 da caricare nella camera (formato `.cube`) o una tabella di esposizione per soggetti in S-Log3?

---

## 🧑 User

per la visualizzazione se non voglio una lut custom mi c onviene restare su s709 o su 709(800%)

---

## 🤖 Assistant

Ottima domanda — e la risposta dipende da **cosa vuoi ottenere in fase di monitoraggio**.

Vediamolo chiaramente:

---

### 🎨 **Confronto tra S-Log3 Monitor LUT: `S-Log3 → S709` vs `S-Log3 → 709(800%)`**

| LUT di monitoraggio | Look | Gamma | Colori | Quando usarla |
|---------------------|------|--------|--------|----------------|
| **S709** | Cinematografico, contrasto più morbido, curve più dolci | Non lineare (tipo cineon) | Più neutro/fedele, roll-off sugli highlight | ✅ Per chi vuole un’**anteprima simile a grading finale**, tipo Alexa look / Venice look |
| **709(800%)** | Standard Rec709 "broadcast", più brillante e contrastata | Lineare Rec709 800% (esteso) | Più vivace, saturazione alta | ✅ Utile per avere un **riferimento tecnico chiaro e immediato** durante riprese rapide o ENG |

---

### 🎯 Quindi quale conviene?

- **Se vuoi monitorare in modo "cinema style"**, avere un look più vicino a ciò che otterrai dopo la color correction e una preview più gradevole:
👉 **Usa `S709`**

- **Se vuoi una preview tecnica, forte e chiara per l’esposizione (soprattutto outdoor o interviste rapide)**:
👉 **Usa `709(800%)`**

---

### 💡 Consiglio pratico per la Sony A7S III:

> Se **non stai caricando LUT custom** e vuoi una preview neutra e bilanciata che simuli la color correction base:
✅ **`S709` è la scelta più equilibrata** per log monitor LUT.

---

Fammi sapere se vuoi anche una mini-tabella con riferimenti IRE per i principali elementi della scena (skintones, cielo, bianchi, neri) in S-Log3 con preview `S709` o `709(800%)`.