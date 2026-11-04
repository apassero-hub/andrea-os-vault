---
title: "Collegamento Zoom H4 Essential"
created: 2025-08-10
updated: 2025-08-10
model: gpt-5
messages: 2
source: chatgpt-import
tags: [audio]
category: "🎙️ Audio"
---

# Collegamento Zoom H4 Essential

> Importato da ChatGPT export · 2 messaggi · gpt-5 · 2025-08-10

## 🧑 User

Per collegare il mio Zoom H4 Essential, in questo caso in specifico devo registrare un concerto da poter utilizzare poi come base audio per il video che vado a fare. E mi hanno detto di collegarlo, di richiedere una matrice audio XLR e collegarlo direttamente in quel casorino. Trattandosi di matrice audio XLR, dopo aver scontato che i cavi, il metodo di collegamento su H4 Essential, siano i cavi XLR, qualora invece, quindi se fosse così, sarebbero canale destro e canale sinistro, riguardo a questi due canali e registro. In tal caso, devo avere il phantom acceso oppure spento, quindi l'alimentazione, credo spenta perché tanto è un microfono che va alimentato. Qualora invece non ci fosse quest'opzione, ma sul mixer ci fosse l'uscita RCA, come mi comporto in questo caso? Cioè, mi attacco da una parte RCA, dall'altra parte ho un cavo che è jack grosso, jack grosso, quindi potrei mettere i due RCA LR con le due uscite dall'altra parte, quei due jack grossi, li inserisco all'interno dell'attacco XLR, che tanto comunque è compatibile anche con i cavi jack jack. E ok, anche in questo caso, phantom sì, phantom no, la mia intenzione è chiaramente di registrare un 32 bit. Ho anche l'opzione di avere il cavo che fa XLR RCA, da un lato, destro e sinistro, e jack piccolo dall'altra parte. Solo che, come abbiamo già discusso, se io l'attacco in quella configurazione, non registrerò il 32 bit. Cosa mi conviene fare? Ha più senso che io faccia destro e sinistro, e poi magari metta entrambi, cioè jack piccolo e i due jack grossi, e registri su tutti e tre i canali, oppure non ha alcun senso.

---

## 🤖 Assistant

Ti faccio una spiegazione ordinata e senza giri di parole, così hai un flusso chiaro per ogni scenario possibile con il tuo **Zoom H4 Essential** quando ti danno una matrice audio del service.

---

## 1. Caso **matrice con uscite XLR bilanciate** (scenario migliore)
- **Collegamento**:
Due cavi XLR (L e R) → ingressi combo XLR del H4 Essential.
- **Phantom power**: **SPENTO**.
Motivo: l’uscita del mixer è già a livello linea o mic attivo, non ha bisogno di alimentazione. Dare phantom su un’uscita mixer può danneggiare il mixer o creare rumori.
- **Impostazioni H4 Essential**:
- Modalità di registrazione: **32-bit float** (così hai la massima headroom).
- Imposta input come **Line** se il mixer ti dà un livello linea (quasi sempre), oppure **Mic** se specificamente ti mandano segnale microfonico.
- **Vantaggi**: Segnale pulito, bilanciato, meno interferenze.

---

## 2. Caso **matrice con uscite RCA sbilanciate**
- **Opzione A (consigliata)**:
RCA → adattatore RCA→Jack TRS 6,3 mm (uno per L e uno per R) → ingressi combo del H4 Essential (usando la parte jack, non l’XLR).
- **Phantom**: **SPENTO**.
- Livello di input: setta su **Line**.
- **Opzione B**:
RCA → adattatore RCA→XLR (L e R separati) → ingressi combo H4 Essential.
- Sempre **Phantom SPENTO**.
- Nota: Con RCA hai un segnale sbilanciato, quindi il cavo deve essere corto per ridurre rumori.

---

## 3. Caso **uscita solo su jack piccolo stereo (TRS 3,5 mm)**
- Collegamento: TRS 3,5 mm stereo → ingresso “Mic/Line” da 3,5 mm del H4 Essential.
- **Limite**: In questa modalità l’H4 non registra in 32-bit float, perché quell’ingresso è gestito separatamente e lavora a 24-bit.
- **Uso**: Va bene solo come backup o se non ti serve l’headroom del 32-bit.

---

## 4. Registrare più ingressi contemporaneamente
- Puoi registrare **i due ingressi XLR (L/R)** e contemporaneamente anche l’ingresso stereo da 3,5 mm, così da avere:
- **Main take**: segnale bilanciato 32-bit da XLR (migliore qualità, zero clipping).
- **Backup**: segnale stereo sbilanciato dal 3,5 mm, utile se qualcosa va storto negli XLR.
- Non ha senso registrare “due volte” lo stesso segnale sugli stessi ingressi con jack e XLR insieme: scegli la connessione migliore.

---

## 5. Regole rapide
- **Phantom ON** → solo per alimentare microfoni a condensatore **che richiedono alimentazione**.
Per segnale da mixer: **sempre OFF**.
- **Cavi bilanciati (XLR o TRS)** → meno rumore, preferibili sempre.
- **Cavi sbilanciati (RCA o 3,5 mm)** → usare solo se non ci sono alternative e tenerli corti.
- **32-bit float** → disponibile solo sugli ingressi combo XLR/TRS, non sul mini-jack.

---

💡 **In pratica per il concerto**:
1. Prima scelta → chiedi **uscita stereo XLR** → due XLR → H4 Essential (phantom OFF, 32-bit, livello Line).
2. Backup → ingresso 3,5 mm dallo stesso mixer o da altra uscita (se disponibile).

---

Se vuoi, ti posso fare anche **uno schema visivo di collegamento** con tutte le opzioni e impostazioni per non sbagliare in loco. Sarebbe utilissimo da tenere sul telefono il giorno del concerto. Vuoi che lo faccia?