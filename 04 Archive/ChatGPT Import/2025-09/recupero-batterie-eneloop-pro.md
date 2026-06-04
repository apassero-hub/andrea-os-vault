---
title: "Recupero batterie Eneloop Pro"
created: 2025-09-13
updated: 2025-09-13
model: gpt-5
messages: 8
source: chatgpt-import
tags: []
---

# Recupero batterie Eneloop Pro

> Importato da ChatGPT export · 8 messaggi · gpt-5 · 2025-09-13

## 🧑 User

Allora, ho delle batterie Eneloop Pro, mini-stilo, quelle da 900 mAh, e dispongo anche di un caricabatterie Maha PowerX, dovrebbe essere MH9000, quello che carica, puoi scegliere la potenza di carica, puoi fare il breaking delle batterie, puoi fare il refresh, puoi fare tutta una serie di robe. Quando metto in carica però queste batterie Eneloop Pro di Sanio, adesso mi dà Hi, scritto, che interiore dovrebbe essere l'errore, probabilmente perché hanno un'impedenza sballata e tutto quanto. Ora mi chiedo, c'è un qualche modo per poter recuperare queste batterie perché le usate davvero pochissime, perché è un formato che non uso tanto, sono rimaste lì in un cassetto e non vorrei doverle buttare dopo pochissimo utilizzo. Questo caricatore secondo te ha qualche opzione, visto che comunque è un caricatore di alta gamma, per poterle recuperare, riprendere, facendogli un nuovo breaking, facendogli qualcosa.

---

## 🤖 Assistant

Chiaro, vediamo punto per punto.

### 1. Il messaggio **“Hi”** sul Maha Powerex
Sul MH-C9000 (immagino sia questo il tuo modello, non “9000”), il messaggio **“Hi”** indica che la resistenza interna della batteria è troppo alta. In pratica il caricatore “rifiuta” di caricare perché interpreta la cella come degradata o guasta.
Le cause più comuni:
- Le batterie sono state ferme a lungo, quindi la resistenza interna è salita.
- Scarica profonda o autoscarica fino a livelli molto bassi.
- Possibile perdita di elettrolita (anche invisibile).

### 2. Tentativi di recupero con il MH-C9000
Il tuo caricabatterie ha alcune funzioni utili:
- **Break-In**: carica lenta e controllata, utile per batterie nuove o rimaste ferme a lungo.
- **Refresh & Analyze**: cicli di scarica/carica multipli che possono ridurre l’impedenza interna.
- **Cycle**: cicli di carica-scarica ripetuti, simile al refresh.

Il problema è che quando mostra “Hi” non parte neppure il ciclo normale.
Due possibili approcci:
1. **Avviarle altrove**: metti la batteria su un caricatore più “tollerante” (anche uno economico che non misura IR), fai prendere un minimo di carica (es. 5–10 min). Poi spostala sul Maha e prova un ciclo *Refresh*.
2. **Carica forzata**: alcuni usano un alimentatore controllato (es. 1,2 V a corrente molto bassa, 50–100 mA per pochi minuti) per “risvegliare” la cella, ma è da fare solo se sei sicuro, perché una NiMH può scaldare o perdere.

### 3. Possibilità reali di recupero
- Se sono state ferme anni, è probabile che abbiano sviluppato resistenza interna elevata. In quel caso anche se riesci a “risvegliarle”, avranno autonomia ridotta e si scalderanno più facilmente in carica/uso.
- A volte il **break-in a bassa corrente (200 mA per le AAA)** funziona, ma serve che il caricatore accetti almeno di iniziare.

### 4. In sintesi
- Prova prima con un caricatore “semplice” per dargli un minimo di carica.
- Poi ripassa sul Maha con funzione **Refresh & Analyze** o **Break-In**.
- Se continuano a segnare “Hi”, purtroppo le celle sono compromesse (anche se poco usate, il problema è lo stoccaggio).

Vuoi che ti prepari una **procedura passo-passo** per tentare il recupero, usando sia il Maha sia eventualmente un caricatore base?

---

## 🧑 User

Scrive high non hi

---

## 🤖 Assistant

Perfetto, questo chiarisce.
Sul **Maha Powerex MH-C9000** quando compare **“HIGH”** non è un errore generico, ma la lettura della **resistenza interna** della batteria: significa che il caricatore misura un valore troppo elevato e quindi la considera non idonea a una carica corretta.

### Cosa vuol dire “HIGH”
- La resistenza interna (IR) è oltre la soglia di sicurezza → la batteria non riuscirà a erogare corrente senza scaldarsi o crollare di tensione.
- Succede spesso su pile NiMH rimaste **scariche per anni** o che hanno subito **autoscarica profonda**.
- Non è un problema del caricatore, è la cella che non viene più riconosciuta come “salvabile” in modo normale.

### Cosa puoi tentare
1. **Avvio con caricatore basico**
- Metti la batteria per 10-15 min in un caricatore economico (quelli che non misurano IR).
- Questo spesso porta la tensione a un livello accettabile (1,0–1,1 V).
- Poi rimettila nel Maha e prova “Refresh & Analyze” a bassa corrente (200 mA per AAA).

2. **Carica forzata a corrente minima (rischiosa, solo se sai cosa fai)**
- Collegare per pochi minuti a una fonte stabilizzata di 1,2–1,4 V con corrente limitata a 50-100 mA.
- Appena la tensione risale, riportarla sul Maha.
- Se noti surriscaldamento → interrompi subito.

3. **Break-In**
- Se riesci a far partire la modalità Break-In (200 mA per le AAA), quello è il metodo migliore per provare un recupero lento.

### Limiti reali
- Anche se riparte, la **capacità residua sarà ridotta** e l’autoscarica elevata.
- Se continuano a segnare “HIGH” anche dopo un tentativo di pre-carica, sono da considerarsi compromesse.

Vuoi che ti scriva una procedura **step-by-step pratica** per tentare il “risveglio” usando solo ciò che hai in casa (Maha + eventualmente un caricatore semplice), così vedi subito se ne vale la pena?

---

## 🧑 User

Io provo ad intanto caricarle con un caricatore basico, lascio il disk fino al di più, non provo a farlo, ciclo di carica completo.

---

## 🤖 Assistant

Ok, è la mossa giusta. Ti do uno schema chiaro:

### Procedura con caricatore basico
1. **Inserisci le AAA nel caricatore semplice** (quello senza misure avanzate).
2. **Lasciale completare un ciclo di carica normale** (anche se ci mette 6–8 ore). Non serve fermarle prima: l’obiettivo è portarle a piena tensione.
3. **Controlla calore**: se diventano molto calde al tatto (più di 50 °C), interrompi subito.
4. Una volta finite, **passale al Maha** e imposta una modalità lenta:
- **Refresh & Analyze** a **200 mA** (per le mini stilo).
- Oppure **Break-In** sempre a 200 mA, che fa carica lenta + scarica + ricarica.

### Cosa aspettarti
- Se il Maha ora le accetta, vedrai un valore di capacità (mAh) e di resistenza interna.
- Se restano su “HIGH”, anche dopo la pre-carica, significa che l’impedenza è troppo fuori specifica → la batteria è da considerarsi persa.

Vuoi che ti dia anche le **soglie indicative di resistenza interna (mΩ)** per capire, dal display del Maha, se la batteria è “ancora usabile” o solo buona da buttare?

---

## 🧑 User

Vabbè, se il macro non lo... non gli piace, ma il mio caricatore basico è sfigato, me le carica, e comunque un pochettino dura, dovevo illuminarci un pannello LED, e io lo uso così. Se poi mi viene a fuoco tutto, spero di no, butto via tutto.

---

## 🤖 Assistant

Capito. Se il caricatore basico riesce a portarle su e ti danno ancora un po’ di autonomia, per usi leggeri come un pannello LED possono andare, purché tu tenga a mente due cose:

1. **Rischio surriscaldamento**: non lasciarle mai incustodite in carica su un caricatore “stupido”. Metti sempre mano alle pile ogni tanto: se scottano → stop immediato.
2. **Autonomia ridotta**: le Eneloop Pro AAA da 900 mAh sane devono darti vicino agli 800–850 mAh reali. Se dopo mezz’ora di LED sono già giù, significa che la resistenza interna è alta e la scarica utile è poca.
3. **Uso pratico**: se ti servono per qualcosa di poco critico (pannellino LED, telecomandi, mouse), puoi spremerle finché durano.
4. **Stoccaggio sicuro**: se decidi di “usarle fino alla morte”, almeno evita di lasciarle cariche nel cassetto per mesi: scaricale parzialmente (40–50%) e conservale in luogo fresco.

Ti serve che ti indichi anche un **valore realistico di tensione e resistenza interna** sotto cui conviene buttarle senza rischiare di farti venire ansie ogni volta che le usi?