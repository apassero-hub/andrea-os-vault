---
title: "Normalizzare audio DaVinci"
created: 2026-02-03
updated: 2026-02-03
model: gpt-5-2
messages: 14
source: chatgpt-import
tags: []
---

# Normalizzare audio DaVinci

> Importato da ChatGPT export · 14 messaggi · gpt-5-2 · 2026-02-03

## 🧑 User

come normalizzo l'audio per un reel insta su davinci?

---

## 🤖 Assistant

Vado dritto al punto.

## Normalizzare l’audio per un Reel Instagram in DaVinci Resolve

image_group{"query":["DaVinci Resolve Fairlight normalize audio","DaVinci Resolve audio waveform Fairlight","DaVinci Resolve audio mixer Fairlight"]}

### Impostazioni consigliate (Instagram)
- **Target loudness:** **–14 LUFS**
- **True Peak:** **–1.0 dBTP**
Questi valori sono lo standard de facto per i contenuti social. Evitano compressioni aggressive lato Instagram.

---

## Metodo corretto (consigliato) – Fairlight > Normalizzazione LUFS

1. Vai nella **pagina Fairlight**.
2. Seleziona **la clip audio** (voce, musica o mix finale).
3. **Tasto destro → Normalize Audio Levels**.
4. Imposta:
- **Mode:** `Loudness`
- **Standard:** `ITU-R BS.1770-4`
- **Target Loudness:** `-14 LUFS`
- **True Peak:** `-1.0 dBTP`
5. Conferma.

Fine. Audio pronto per Instagram.

---

## Se hai più clip (voce + musica)

### Passaggio consigliato
- Normalizza **prima la voce** a **–14 LUFS**.
- Poi abbassa la **musica** manualmente (di solito **–20 / –24 LUFS integrati**, oppure –15 / –20 dB sotto la voce).

Non normalizzare voce e musica insieme se vuoi controllo.

---

## Metodo rapido (meno preciso)
- Seleziona clip
- **Tasto destro → Normalize Audio Levels**
- **Mode:** `Sample Peak`
- **Level:** `–1 dB`

Funziona, ma **non controlla la percezione reale del volume**. Usalo solo se hai fretta.

---

## Controllo finale (obbligatorio)
- Apri **Loudness Meter** in Fairlight.
- Fai partire il playback dall’inizio alla fine.
- Verifica:
- **Integrated ≈ –14 LUFS**
- **True Peak ≤ –1 dBTP**

Se sei lì, Instagram non ti tocca l’audio.

---

### Nota se c’è voce parlata
Se la voce suona ancora “debole”:
- Micro-compressione **prima** della normalizzazione (ratio 2:1, gain reduction 2–4 dB).
- Poi **normalizzi a –14 LUFS**.

Se vuoi, dimmi:
- solo voce
- voce + musica
- musica only

e ti do **una chain precisa** (compressore, EQ, limiter) pronta da copiare.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto. Quella schermata **è corretta come finestra**, ma **i valori no** per un Reel Instagram.

Vado secco.

## Cosa NON va bene in quello screenshot
- **Target Loudness: –23 LKFS** → **sbagliato per Instagram**
- **Target Level: –2.0 dBTP** → troppo conservativo
- Così l’audio **uscirà basso** e Instagram lo rialzerà male.

---

## Impostazioni giuste per Reel Instagram

In **Normalize Audio Level** imposta così:

- **Normalization Mode:** `ITU-R BS.1770-4` (giusto, lascialo)
- **Target Loudness:** **–14 LKFS**
- **Target Level (True Peak):** **–1.0 dBTP**
- **Set Level:** `Relative` (giusto se stai normalizzando clip singole)

Poi **Normalize**.

Fine.

---

## Perché –14 e non –23
- **–23 LKFS** è standard **broadcast TV**
- **Instagram / social** lavorano intorno a **–14 LUFS**
- Se consegni a –23:
- suona debole
- IG comprime e pompa a cazzo
- perdi punch e chiarezza

---

## Check finale (fallo sempre)
In Fairlight:
- apri **Loudness Meter**
- play dall’inizio alla fine
- verifica:
- **Integrated ≈ –14 LUFS**
- **True Peak ≤ –1 dBTP**

Se sei lì, IG **non tocca nulla**.

---

### Nota importante (voce + musica)
Se stai normalizzando **una clip con dentro già musica + voce**: ok così.
Se invece sono **su tracce separate**:
- normalizza **solo la voce**
- la musica la dice il mix, non il Normalize

Se vuoi, mandami:
- screenshot del **Mixer**
- oppure dimmi **voce / voce+musica / musica only**

e ti dico esattamente **dove e cosa toccare**, senza tentativi.

---

## 🧑 User

quindi poi in fairlight alzo come per youtube con limiter e gain fino a portarlo a -14 lufs integrated?

---

## 🤖 Assistant

Sì. **Concettualmente è la stessa cosa di YouTube**, ma ti dico **come farlo bene in Resolve** senza fare casino.

Risposta secca:
👉 **non devi “alzare a mano finché arrivi a –14” se usi la normalizzazione LUFS.**
O fai **Normalize**, **oppure** fai **gain + limiter**. Non entrambe alla cieca.

---

## Workflow corretto (pulito e professionale)

### OPZIONE 1 – Consigliata per Reel (rapida e sicura)
**Usi SOLO la normalizzazione LUFS.**

1. Fairlight
2. Selezioni **clip finale** (o bus se stai facendo il mix lì)
3. `Normalize Audio Levels`
4. `ITU-R BS.1770-4`
5. **–14 LUFS / –1 dBTP**
6. Fine.

❌ **Non aggiungi gain dopo**
❌ **Non spingi col limiter**

Il loudness è già corretto.

---

### OPZIONE 2 – Come su YouTube (manuale, più controllo)
Qui **sì**, fai come stai dicendo tu.

#### Catena corretta sul **BUS**
1. **EQ / Compressor** (se serve)
2. **Gain**
3. **Limiter** (ultimo)

#### Limiter
- Output ceiling: **–1.0 dB**
- Lookahead: attivo
- Compressione leggera (1–3 dB GR max)

#### Procedura
1. Play dall’inizio
2. Alzi **GAIN**
3. Guardi **Loudness Meter**
4. Ti fermi quando **Integrated ≈ –14 LUFS**
5. Il limiter serve solo a **contenere i picchi**, non a pompare.

Questo è identico a YouTube. Cambia solo il target (che è lo stesso: –14).

---

## ERRORE comune (da evitare)
❌ Normalizzi a –14
❌ Poi alzi col gain fino a –14 di nuovo

Risultato:
- loudness sballato
- limiter che schiaccia
- Instagram che ti massacra l’audio

---

## Regola pratica
- **Clip singola / Reel veloce** → **Normalize LUFS**
- **Mix serio (voce + musica + sound design)** → **Gain + Limiter sul bus**

---

Se vuoi, dimmi **dove stai lavorando**:
- clip
- traccia
- bus
- master

e ti dico **esattamente dove mettere il limiter** e **quanto gain usare**, senza andare a tentativi.

---

## 🧑 User

con solo il normalize andando ad analizzare col meter restava poi a -20

---

## 🤖 Assistant

Perfetto, allora chiarisco **perché succede** e **come risolverlo senza workaround sbagliati**.

Risposta breve:
👉 **non è un errore tuo**. È **come funziona Resolve** in quel caso.

---

## Perché normalizzi a –14 ma il meter ti legge –20

In DaVinci Resolve la **Normalize Audio Levels**:

- normalizza **la clip selezionata**
- **non tiene conto** di:
- fader di traccia
- fader di bus
- eventuali plugin attivi
- se **il fader di traccia o bus è sotto 0**, il meter leggerà meno LUFS

Quindi:
- clip = –14 LUFS
- bus a –6 dB → meter ≈ –20 LUFS

È esattamente quello che stai vedendo.

---

## Check immediato (fallo ora)
Vai nel **Mixer** e verifica:
- **Traccia audio** a **0.0 dB**
- **Bus / Master** a **0.0 dB**

Se uno dei due è sotto:
- il meter scende
- la normalizzazione è “annullata” dal gain a valle

---

## Workflow che funziona SEMPRE

### Metodo consigliato (bus-based, zero sorprese)

1. **Non usare Normalize sulla clip**
2. Porta **tutti i fader a 0.0 dB**
3. Inserisci sul **Bus**:
- (eventuale) Compressor
- **Gain**
- **Limiter** (ultimo)
4. Play tutta la timeline
5. Alza il **Gain** finché il **Loudness Meter integrato ≈ –14 LUFS**
6. Limiter a **–1 dBTP**

Fine. Quello che leggi = quello che esporti.

---

## Se vuoi continuare a usare Normalize
Allora devi essere coerente:

- Normalizza **sul BUS**, non sulla clip
- seleziona il bus
- `Normalize Audio Levels`
- –14 LUFS / –1 dBTP
- Fader bus **a 0.0**
- Meter affidabile

---

## Regola d’oro
> **In Resolve il loudness “vero” è quello del BUS, non della clip.**

Se misuri a –20, **uscirà a –20**, anche se la clip “internamente” è a –14.

---

Se vuoi, mandami:
- screenshot del **Mixer**
- o dimmi **dove hai fatto Normalize (clip / traccia / bus)**

e ti dico **esattamente dove stai perdendo i 6 dB**.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto. Dallo **screenshot del Mixer** si vede chiaramente dov’è il problema. Vado diretto.

## Cosa sta succedendo (diagnosi)
- **A1 (traccia)**: fader a **0.0 dB** → corretto
- **Bus 1**: fader a **0.0 dB** → corretto
- **Limiter sul Bus 1**: **attivo**
- **Gain sul Bus 1**: **presente**

Il punto critico non è il fader.
È **l’ordine e l’uso di Normalize + Gain/Limiter insieme**.

Hai fatto:
1. **Normalize (LUFS)**
2. Poi **passi dal Bus con Gain + Limiter**
3. Misuri col meter → ti ritrovi a **–20 LUFS**

Questo accade perché:
- la **Normalize** ha portato la **clip** a –14
- ma **il limiter sul bus** sta già **contenendo i picchi**
- quindi quando Resolve ricalcola l’integrated **non ha più margine energetico**
- risultato: loudness integrato più basso

Non è un bug. È un **doppio controllo sul livello**.

---

## Come sistemarla (2 soluzioni corrette)

### SOLUZIONE A – Metodo pulito, quello che ti consiglio
**Dimentica il Normalize. Lavora solo di Bus.**

1. **Reset Normalize** (o ignoralo)
2. Sul **Bus 1**:
- EQ / Compressor (se serve)
- **Gain**
- **Limiter** (ultimo)
3. Limiter:
- Output: **–1.0 dBTP**
- Gain Reduction: max **1–3 dB**
4. Play tutta la timeline
5. Alza **Gain** finché:
- **Integrated ≈ –14 LUFS**

Fine.
Quello che leggi = quello che esce su Instagram.

---

### SOLUZIONE B – Se vuoi usare per forza Normalize
Allora devi essere coerente:

- **Normalize SOLO sul Bus 1**
- Target: **–14 LUFS / –1 dBTP**
- **Rimuovi il Gain**
- Limiter solo come safety (non deve lavorare)

Se il limiter sta lavorando, il loudness scende. Punto.

---

## Regola tecnica da ricordare
> **Normalize e Gain+Limiter non si sommano.
Ne usi uno o l’altro.**

Per Reel:
- lavoro rapido → **Normalize sul Bus**
- lavoro controllato → **Gain + Limiter sul Bus**

Tu ora sei a metà strada tra i due. Per questo vedi –20.

Se vuoi, al prossimo messaggio:
- dimmi **quanto gain reduction vedi sul limiter**
- oppure mandami **screenshot del Loudness Meter**

e ti dico **esattamente di quanti dB alzare il gain** per chiuderla a –14 al primo colpo.

---

## 🧑 User

limiter e gai li ho aggiunti io dopo aver normalizzato e analizzato, realizzando che il volume fosse troppo basso

---

## 🤖 Assistant

Perfetto. Allora chiudiamo il cerchio, senza ambiguità.

**Quello che hai fatto è logico**, ma in Resolve **non funziona come te lo aspetti**. Ti spiego **perché** e poi ti do **la procedura definitiva** da usare d’ora in poi.

---

## Perché NORMALIZE → meter basso → aggiungi gain
Succede questo:

1. **Normalize LUFS** porta la **clip** a –14 LUFS *a monte*.
2. Il meter che guardi è **post-bus**, quindi:
- EQ
- Dynamics
- Limiter
influenzano la lettura.
3. Il **limiter**, anche se sembra “quasi fermo”,:
- riduce i picchi
- abbassa l’energia media
- fa scendere l’**Integrated LUFS**.
4. Tu aggiungi **Gain**, ma:
- il limiter lo mangia
- il loudness integrato resta basso (–20 circa).

Quindi: **stai compensando contro un muro**.

---

## Verità tecnica (senza zucchero)
👉 **In Resolve il Normalize LUFS non è pensato per convivere con una catena dinamica attiva a valle.**

Se vuoi controllo dinamico:
- **non usare Normalize**
Se vuoi Normalize:
- **niente gain, niente limiter che lavori**

---

## Procedura DEFINITIVA per Reel Instagram
Questa funziona sempre. Fine.

### Setup Bus 1
Ordine plugin:
1. **EQ** (se serve)
2. **Compressor** (opzionale, leggero)
3. **Gain**
4. **Limiter** (ultimo)

### Limiter
- Output: **–1.0 dBTP**
- GR max: **2 dB**

### Procedura
1. **Non normalizzare nulla**
2. Play tutta la timeline
3. Guarda **Loudness Meter**
4. Alza **GAIN** finché:
- **Integrated = –14 LUFS**
5. Stop.

Quello che leggi è quello che esce su Instagram.

---

## Perché questo è meglio del Normalize
- Meter affidabile
- Nessuna doppia compensazione
- Audio più “denso” e presente
- Zero sorprese dopo l’export

---

## Shortcut mentale (ricordatelo)
- **Normalize = automatico, senza controllo**
- **Gain + Limiter = manuale, corretto**

Tu stai già lavorando come uno che vuole controllo.
Quindi **abbandona Normalize** per i Reel.

Se vuoi, prossimo step posso:
- darti **numeri precisi** per compressore voce (attack, release, ratio)
- oppure una **chain “Reel voice”** pronta da salvare come preset.

---

## 🧑 User

mi dai le impostazioni corrette di esportazione per insta?

---

## 🤖 Assistant

Sì. Te le do **pulite, definitive e senza folklore**.
Queste sono **le impostazioni corrette di esportazione per Instagram Reel** da DaVinci Resolve. Copiale e basta.

---

## EXPORT REEL INSTAGRAM – DA VINCI RESOLVE

### TAB VIDEO

**Format**
- `MP4`

**Codec**
- `H.264`
- (H.265 no: più compressione, nessun vantaggio su IG)

**Resolution**
- **1080 × 1920** (verticale 9:16)
- NON 4K: Instagram ricomprime comunque

**Frame rate**
- **Uguale alla timeline**
- Consigliato: **25 fps** (se lavori EU)
- Evita conversioni inutili

**Quality**
- `Restrict to`
- **12.000 – 16.000 kbps**
- sotto: perdi dettaglio
- sopra: inutile, IG ricomprime

**Encoding Profile**
- `High`

**Key Frames**
- Automatic

---

### TAB AUDIO (IMPORTANTISSIMO)

**Format**
- `AAC`

**Sample Rate**
- **48.000 Hz**
(coerente con Resolve e Instagram)

**Bitrate**
- **320 kbps**

**Output Track**
- `Bus 1` (o Master, ma uno solo)

---

### TAB ADVANCED

- ✅ `Force sizing to highest quality`
- ✅ `Force debayer to highest quality`
- ❌ Nessun color space strano
- ❌ Nessun tag HDR

---

## CHECK PRIMA DI ESPORTARE (OBBLIGATORIO)
In Fairlight:
- Loudness Meter:
- **Integrated ≈ –14 LUFS**
- **True Peak ≤ –1 dBTP**

Se sei lì:
- Instagram **non ti abbassa**
- non pompa
- non distorce

---

## ERRORI DA EVITARE
❌ 4K “così è più definito”
❌ Bitrate 40–60 Mbps
❌ Audio a –23 LUFS
❌ 44.1 kHz
❌ H.265

Tutta roba che **peggiora il risultato finale**.

---

## TL;DR (preset mentale)
- 1080×1920
- H.264
- 12–16 Mbps
- AAC 48kHz 320 kbps
- –14 LUFS / –1 dBTP

Se vuoi, al prossimo messaggio:
- ti preparo **un preset.drx** pronto da importare
- oppure uno **specifico per Stories** (che hanno compressione leggermente diversa).