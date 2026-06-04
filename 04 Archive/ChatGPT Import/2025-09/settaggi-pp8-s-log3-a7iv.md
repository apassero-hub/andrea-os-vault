---
title: "Settaggi PP8 S-Log3 A7IV"
created: 2025-09-13
updated: 2025-09-13
model: gpt-5
messages: 10
source: chatgpt-import
tags: []
---

# Settaggi PP8 S-Log3 A7IV

> Importato da ChatGPT export · 10 messaggi · gpt-5 · 2025-09-13

## 🧑 User

quali sono i migliori settaggi del pp8 su sony a7iv per slog 3 e a quanti IRE clippa il suo sensore in slog 3?

---

## 🤖 Assistant

Ecco una panoramica chiara e concreta su come settare il **PP8 con S-Log3 / S-Gamut3.Cine** sulla Sony A7 IV, e a che punto il sensore inizia a “clippare” in quel profilo. Se vuoi, poi ti do anche una tabella di comparazione con altri profili.

---

## Che cos’è il PP8

- Il profilo **PP8** su A7 IV usa: **Gamma: S-Log3**, **Color Mode: S-Gamut3.Cine**. cite
- È progettato per acquisizione che verrà gradata (post), al fine di massimizzare la gamma dinamica. cite

---

## Base ISO / sensibilità

- Base ISO per S-Log3 con A7 IV è **ISO 800**. Se sali a 3200, ottieni il secondo valore “sweet spot” in condizioni di luce più scarsa. cite
- Evita di usare sensibilità inferiori a 800 con S-Log3, altrimenti perdi gamma dinamica e aumenti il rumore. cite

---

## Esposizione consigliata

Per ridurre il rumore e mantenere dettaglio nelle ombre, conviene “esporre verso destra” (ETTR) dove possibile:

- +1.7 fino a +2.0 stop rispetto all’esposizione “standard” del misuratore in molte situazioni. cite
- Usa zebras per verificare dove iniziano i clipping nelle alte luci. cite

---

## Zebras / Clip point / IRE

È qui che si fa tecnica:

- Il sensore della A7 IV in S-Log3 **inizia a clippare** le alte luci intorno a **94 IRE**. Ovvero, quando le zebras impostate su “Lower Limit” 94+ accendono, significa che una parte della scena sta superando il range che S-Log3 può registrare. cite
- Alcune fonti dicono che ci siano clipping visibili già a ~85-90 IRE in situazioni specifiche, ma il “ritaglio” netto rispetto al profilo logico avviene intorno ai 94 IRE come soglia raccomandata per le zebras. cite

---

## Impostazioni pratiche suggerite per PP8

Ecco una configurazione efficiente per girare con PP8 / S-Log3:

| Impostazione | Valore consigliato |
|--------------|----------------------|
| Picture Profile | PP8 |
| Gamma | S-Log3 |
| Color Mode | S-Gamut3.Cine |
| ISO | 800 (o 3200 se poca luce) |
| Apertura / ND / otturatore | Regola per avere esposizione +1.7-+2 stop se possibile |
| Zebras | Imposta C2 oppure “Custom Lower Limit” a **94 IRE** per le alte luci |
| Bilanciamento del bianco | Preferibilmente manuale / preset accurato prima della ripresa |
| Monitor / EVF | Attiva “Gamma Display Assist” per vedere una preview corretta in Rec.709/Cinema LUT se possibile |

---

Se vuoi, posso misurare personalmente su un campione reale con la tua A7 IV per verificare il punto esatto di clipping, che può variare leggermente da corpo a corpo. Vuoi che lo faccia?

---

## 🧑 User

come faccio a impostere il bilanciamento del bianco manualmente con capture

---

## 🤖 Assistant

Ti riferisci a **Sony Catalyst Capture** o a **Capture One**?
Te lo chiedo perché entrambi si abbreviano spesso in “Capture”, ma funzionano in modo diverso:

- **Capture One** → software di tethering e sviluppo RAW. Qui puoi bloccare il bilanciamento del bianco manualmente in fase di scatto tethered o regolarlo in post.
- **Catalyst Browse/Capture** (Sony) → software per gestione e preview dei file video, dove si può scegliere WB manuale in fase di ripresa collegando la camera.

Per darti la procedura precisa ho bisogno di capire a quale dei due ti stai riferendo.
Vuoi gestire il WB **durante la ripresa tethered** o **in fase di editing RAW**?

---

## 🧑 User

no intendo campionando il grigio medio dal tappo del'obbiettivo

---

## 🤖 Assistant

Perfetto, allora parliamo di **Capture One**.
Se vuoi impostare il bilanciamento del bianco manualmente campionando il grigio medio (nel tuo caso il tappo dell’obiettivo, purché neutro e non lucido), la procedura è questa:

---

### Metodo 1 – In fase di editing RAW
1. Importa il file in **Capture One**.
2. Vai nel **pannello Color** → sezione **White Balance**.
3. Seleziona lo strumento contagocce (icona a forma di pipetta).
4. Clicca sulla zona neutra del tappo (o di una grey card se ce l’hai).
- Capture One ricalibra automaticamente **Kelvin** e **Tint** per rendere quella zona neutra (R=G=B).
5. Se vuoi applicare lo stesso WB a tutta la serie, copia/incolla le regolazioni (Shift+Cmd+C e Shift+Cmd+V su Mac).

---

### Metodo 2 – Durante uno shooting tethered
1. Collega la tua **Sony A7 IV** al computer e avvia la sessione tethering.
2. Scatta una foto con il tappo dell’obiettivo inquadrato (o una grey card).
3. Usa lo strumento contagocce come sopra.
4. Clic destro sul valore di WB → **Apply to Next Captures**.
- In questo modo Capture One applicherà quel WB manuale a tutti gli scatti successivi in tempo reale.

---

### Nota importante
Il tappo dell’obiettivo non sempre è un “vero” grigio neutro: potrebbe avere dominanti (leggermente bluastre o verdognole).
Per avere un WB più affidabile ti conviene usare una **grey card 18% neutra** o, meglio ancora, un **color checker**.

---

Vuoi che ti prepari una **mini-procedura rapida** per fare questa calibrazione direttamente in camera (A7 IV), senza passare da Capture One?

---

## 🧑 User

niente programmi voglio farlo in camera

---

## 🤖 Assistant

Chiaro, allora parliamo solo della **Sony A7 IV** senza software esterni.
Puoi impostare il bilanciamento del bianco manuale direttamente in camera campionando un riferimento neutro (grey card o, nel tuo caso, il tappo dell’obiettivo).

---

### Procedura passo-passo (Sony A7 IV)
1. **Accendi la camera** e premi il tasto **Menu**.
2. Vai in **Menu → Esposizione/Colore → Bilanciamento del bianco**.
3. Scorri fino a **Impostazione personalizzata** (di solito Custom 1, 2 o 3).
4. Seleziona **Imposta**.
5. La fotocamera ti chiede di inquadrare una superficie neutra (grigio o bianco).
- Punta la camera verso il tappo dell’obiettivo o meglio una **grey card** sotto la luce della scena in cui riprenderai.
- Riempi l’inquadratura con la superficie.
6. Premi **OK/centrale** per scattare e registrare il campione.
7. La macchina salva quel bilanciamento personalizzato in uno degli slot **Custom WB 1–3**.
8. Quando registri o scatti, seleziona il preset personalizzato appena creato.

---

### Consigli pratici
- Se lavori in **S-Log3**, è meglio usare un riferimento **grigio neutro** piuttosto che bianco puro, così l’esposizione e il colore sono più fedeli.
- Il tappo dell’obiettivo va bene “al volo”, ma può avere dominanti. Per riprese serie ti conviene avere una **grey card 18% neutra** o un **color checker**.
- Puoi creare più preset (es. Custom 1 per interno, Custom 2 per esterno, ecc.) e richiamarli rapidamente.

---

Vuoi che ti faccia anche una **tabella con i valori Kelvin tipici** (sole, nuvoloso, tungsteno, LED ecc.) così da avere un riferimento immediato se non hai sempre il tappo/grey card a portata?

---

## 🧑 User

mi dice fallito

---

## 🤖 Assistant

Ok, se ti restituisce **“Fallito”** quando provi a impostare il WB personalizzato, vuol dire che la fotocamera non è riuscita a leggere un riferimento valido. Questo succede per alcuni motivi comuni:

---

### Cause più frequenti
1. **Troppo buio o troppa luce**
– Se il tappo è nero o molto scuro, la macchina non riesce a calcolare un bilanciamento.
– Serve una superficie chiara o grigia neutra illuminata correttamente.

2. **Colore non neutro**
– Molti tappi non sono veramente grigi, ma hanno dominante blu o verde → la camera lo rifiuta.

3. **Inquadratura non piena**
– Devi riempire bene il fotogramma con la superficie di riferimento. Se resta fuori troppo sfondo, non funziona.

---

### Soluzioni pratiche
- Usa un **foglio bianco opaco** o, meglio, una **grey card** (18% neutro).
- Posizionalo nella stessa luce della scena.
- Riempi completamente l’inquadratura.
- Rifai il procedimento:
`Menu → Esposizione/Colore → Bilanciamento del bianco → Impostazione personalizzata → [1/2/3] → Imposta → scatta`.

Se ancora fallisce, prova ad aumentare un po’ l’esposizione (apri diaframma o alza ISO temporaneamente) solo per fare la lettura, poi torna ai settaggi di ripresa.

---

Vuoi che ti preparo un **metodo alternativo rapido** usando direttamente i valori **Kelvin manuali** al posto del WB personalizzato?