---
title: "Problema colore DaVinci"
created: 2026-03-07
updated: 2026-03-07
model: gpt-5-3
messages: 8
source: chatgpt-import
tags: []
---

# Problema colore DaVinci

> Importato da ChatGPT export · 8 messaggi · gpt-5-3 · 2026-03-07

## 🧑 User

Il montaggio di un video su DaVinci di un video appunto che ha ripreso Limondino, con il suo iPhone, lui ha il 16, mi sembra, ripreso in 4K a 60, porco 2 perché non ce l'ha impostato in NTSC, ma vabbè. E quindi farò il montaggio così. L'unica cosa che mi fa strana è che quando io guardo le immagini dal browser del del Mac le vedo bene, quando poi le carico su DaVinci le vedo tutte gialle. Che cosa può essere sta roba qua, come la risolvo?

---

## 🤖 Assistant

Quello che descrivi è **quasi certamente un problema di gestione del colore dei file iPhone (HDR / Dolby Vision / Rec.2020)** che **DaVinci Resolve interpreta in modo diverso dal Finder o da QuickTime**. È molto comune con i video girati con iPhone recenti.

Il risultato tipico è esattamente quello che vedi:
- nel **Finder / QuickTime** l’immagine appare normale
- in **DaVinci** diventa **gialla, calda o slavata**

Ti spiego cosa sta succedendo e come risolverlo.

---

## 1️⃣ Il motivo più probabile: video iPhone in HDR (Dolby Vision)

Gli iPhone recenti registrano spesso in:

- **HEVC**
- **HDR Dolby Vision**
- spazio colore **Rec.2020 HLG o PQ**

Il Mac li mostra correttamente perché **QuickTime applica automaticamente la conversione colore**.

DaVinci invece:
- legge il file **senza quella trasformazione**
- quindi l'immagine appare **gialla / con gamma sbagliata**.

---

# SOLUZIONE PIÙ RAPIDA (2 minuti)

### Metodo 1 — Imposta correttamente il color management

1. Vai in
**Project Settings**

2. Sezione
**Color Management**

3. Cambia:

**Color science**
→ `DaVinci YRGB Color Managed`

Poi imposta:

**Timeline Color Space**
→ `Rec.709 Gamma 2.4`

**Input Color Space**
→ `Rec.2100 HLG`

oppure
→ `Rec.2100 PQ`

(dipende da come ha registrato l’iPhone)

Spesso **HLG è quello giusto**.

---

# Metodo velocissimo (ancora più semplice)

Se non vuoi toccare il color management del progetto:

1. Seleziona la clip nella **Media Pool**
2. Tasto destro
3. **Input Color Space**
4. Prova:

```
Rec.2100 HLG
```

oppure

```
Rec.2100 PQ
```

Vedrai immediatamente l'immagine tornare normale.

---

# Metodo brutale ma efficace (quando vuoi zero sbatti)

Nel **Color tab** aggiungi un nodo con:

**Color Space Transform**

Input:

```
Color Space: Rec.2020
Gamma: HLG
```

Output:

```
Color Space: Rec.709
Gamma: Gamma 2.4
```

---

# Per capire subito se è HDR

Seleziona il file e fai:

```
Cmd + I
```

oppure in QuickTime:

```
Window → Show Movie Inspector
```

Se leggi:

- **Dolby Vision**
- **HLG**
- **HDR**

allora il problema è quello.

---

# Consiglio per il futuro (importantissimo)

Digli di disattivare:

**Impostazioni iPhone → Fotocamera → Registra video → HDR Video**

Perché:
- crea solo problemi in post
- soprattutto quando monti in **Rec709**

---

# Se vuoi posso dirti anche

- **come settare Resolve perfettamente per i video iPhone**
- **come evitare completamente questi problemi**
- **come convertire automaticamente tutto in Rec709**

Ci vogliono **30 secondi di settaggio** e poi non ci pensi più.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Sì, il **Color Space Transform che hai impostato è corretto per un iPhone HDR**.

I parametri che vedo nello screenshot sono quelli giusti:

- **Input Color Space:** Rec.2020
- **Input Gamma:** Rec.2100 HLG
- **Output Color Space:** Rec.709
- **Output Gamma:** Gamma 2.4

Questo fa esattamente quello che serve:
**converte il video HDR dell’iPhone in Rec709 standard**, cioè lo spazio colore corretto per la maggior parte dei montaggi e delle esportazioni.

---

## Però verifica una cosa importante

Subito dopo aver applicato il nodo:

- l’immagine dovrebbe **tornare neutra**
- il giallo dovrebbe sparire
- il contrasto dovrebbe diventare normale

Se invece **resta ancora gialla**, allora probabilmente il file è:

**Rec.2020 + PQ (Dolby Vision)**
non **HLG**.

In quel caso cambia solo questo parametro:

**Input Gamma**

da

```
Rec.2100 HLG
```

a

```
ST2084 (PQ)
```

Sugli iPhone 14-15-16 spesso è **PQ Dolby Vision**.

---

## Un'altra cosa importante (tipica dei file iPhone)

Resolve a volte applica anche il **tag Rec709-A** quando esporti per Mac.

Se esporti per web/Instagram/Youtube:

nel Deliver metti:

```
Gamma tag: Rec709-A
```

altrimenti i video possono apparire **più scuri su Mac/QuickTime**.

---

## Consiglio pratico per questo progetto

Per un montaggio veloce come quello che stai facendo:

1. Nodo 1
**CST iPhone → Rec709** (quello che hai fatto)

2. Nodo 2
**color correction normale**

Così tutto rimane pulito.

---

## Ultima cosa (che ti farà risparmiare tempo in futuro)

Quando importi clip iPhone puoi fare direttamente:

```
Media Pool
Right Click
Input Color Space
Rec.2100 HLG
```

Resolve farà la conversione **senza usare nodi**.

---

Se vuoi, posso anche spiegarti **perché i video iPhone diventano gialli in Resolve su Mac**.
È una cosa molto tecnica legata a **ColorSync + HDR metadata Apple**, ma è utile da capire perché succede spesso quando lavori con materiale girato da altri.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

no è hlg. però ancora lo vedo diverso da come lo carico in anteprima su macos

---

## 🤖 Assistant

Perfetto, lo screenshot conferma tutto. Il file è:

- **HDR: Dolby Vision**
- **Color primaries:** BT.2020
- **Transfer:** **HLG**
- **10-bit HEVC**

Quindi il tuo **CST è corretto**. Il problema che vedi adesso **non è più lo spazio colore**, ma il **tone mapping HDR → SDR** che macOS fa automaticamente e Resolve no.

In altre parole:

- **QuickTime / Finder** applicano una **conversione HDR intelligente** tramite **ColorSync**
- **DaVinci** fa una conversione **lineare tecnica**

Risultato:
Resolve appare **più giallo o più piatto** rispetto alla preview di macOS.

---

# La soluzione corretta in Resolve

Nel nodo **Color Space Transform** attiva queste opzioni (sono sotto):

### attiva

```
Tone Mapping Method → DaVinci
```

oppure

```
Tone Mapping Method → Luminance Mapping
```

e soprattutto:

```
Gamut Mapping → Saturation Compression
```

Questo è il pezzo che manca quasi sempre.

Senza gamut mapping i colori **BT2020 compressi in Rec709 diventano giallastri**.

---

# Quindi il CST corretto diventa

**Input**

```
Rec.2020
Rec.2100 HLG
```

**Output**

```
Rec.709
Gamma 2.4
```

**Opzioni sotto**

```
Tone Mapping → DaVinci
Gamut Mapping → Saturation Compression
```

---

# Un'altra cosa che può influenzare

Controlla anche:

**Project Settings → Color Management**

se hai:

```
Use Mac Display Color Profiles for Viewers
```

Se è attivo, Resolve cerca di comportarsi come macOS.

Molti colorist lo **disattivano** per avere una pipeline più pulita.

---

# La verità operativa (che pochi dicono)

I video iPhone HDR:

- **non avranno mai lo stesso look** tra QuickTime e Resolve
- perché QuickTime usa **ColorSync + Dolby metadata dinamico**

Resolve **ignora quei metadata Dolby Vision**.

Quindi quello che vedi in Resolve è spesso **più corretto tecnicamente**.

---

# Consiglio per questo progetto (veloce)

Fai così:

1. Nodo 1
**CST (HLG → Rec709)**

2. Nodo 2
**WB + contrasto**

3. Nodo 3
**leggero saturation**

In 30 secondi torni perfettamente al look iPhone.

---

Se vuoi, posso dirti anche **un trucco molto più pulito per lavorare con video iPhone in Resolve**, usato nei workflow documentari e YouTube, che evita completamente questi problemi HDR. È una roba che ti fa risparmiare tempo ogni volta che qualcuno ti manda file girati con il telefono.

---

## 🧑 User

gamut mapping non cambia nulla

---

## 🤖 Assistant

Hai ragione a controllare. In questo caso **non è il gamut mapping il problema**. Dallo screenshot che hai mandato si vede chiaramente qual è la causa reale.

Il file è:

- **Dolby Vision**
- **BT.2020**
- **HLG**
- **10 bit**

Il punto chiave è **Dolby Vision**.

QuickTime e macOS **leggono i metadata Dolby Vision** e applicano una **tone curve dinamica scena per scena**.
DaVinci Resolve **ignora completamente quei metadata**. Quando Resolve legge il file usa solo:

- Rec.2020
- HLG

quindi applica una conversione molto più semplice. Il risultato è esattamente quello che stai vedendo: **immagine più gialla / diversa rispetto alla preview del Mac**.

Quindi il comportamento che vedi è **normale**.

---

## Il modo corretto per farla combaciare con la preview del Mac

Nel **Color Space Transform** cambia solo una cosa.

Input gamma:

```
Rec.2100 HLG
```

→ prova invece

```
Rec.2100 HLG (Scene)
```

oppure

```
Rec.2100 HLG (Display)
```

Dipende dalla versione di Resolve ma spesso **HLG Scene** si avvicina molto di più al rendering Apple.

---

## Metodo che di solito funziona meglio con iPhone

Nel CST prova questa configurazione:

Input:

```
Color Space: Rec.2020
Gamma: Rec.2100 HLG
```

Output:

```
Color Space: Rec.709
Gamma: Rec.709-A
```

**Rec709-A** è la gamma che Apple usa nei player QuickTime.

Molto spesso è **questa la differenza che stai vedendo**.

---

## Altra cosa da controllare (importantissima)

Vai in:

```
DaVinci Resolve → Preferences → System → General
```

e guarda se è attivo:

```
Use Mac Display Color Profiles for viewers
```

Se è **spento**, Resolve mostrerà un'immagine diversa da QuickTime.

Prova ad attivarlo e riavvia Resolve.

---

## Riassunto veloce

Il giallo non è dovuto a:

- Rec2020
- HLG
- gamut mapping

ma a:

1. **Dolby Vision metadata ignorati**
2. **gamma Rec709 vs Rec709-A**
3. **ColorSync di macOS**

---

## Consiglio pratico (importantissimo per il futuro)

Digli di disattivare questa opzione sull'iPhone:

```
Impostazioni → Fotocamera → Registra video → HDR Video
```

Perché i video iPhone HDR sono **una rottura di palle enorme in post**.

---

Se vuoi ti dico anche **il metodo più pulito in assoluto per lavorare con file iPhone in Resolve (usato nei workflow documentari)** che elimina completamente queste differenze di colore. È una cosa di **20 secondi di setup**.