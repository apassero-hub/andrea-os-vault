---
title: "Problemi alimentatore 96W MacBook"
created: 2026-03-26
updated: 2026-03-26
model: gpt-5-3
messages: 6
source: chatgpt-import
tags: [storage-it]
category: "💾 Storage & IT"
---

# Problemi alimentatore 96W MacBook

> Importato da ChatGPT export · 6 messaggi · gpt-5-3 · 2026-03-26

## 🧑 User

su un macbook pro m1 max 16" quali possono essere i problemi di usare un alimentatore 96w anzichè quello da 140?

---

## 🤖 Assistant

In breve: **puoi usare un alimentatore da 96W su un MacBook Pro 16" con M1 Max**, ma ci sono limiti concreti. Non è una soluzione equivalente al 140W.

## Cosa succede davvero

### 1) Ricarica più lenta (sempre)
Il 96W non è sufficiente per sfruttare la ricarica rapida prevista su quel modello.

- Con il **140W**: ricarica veloce (fino al 50% in ~30 min via MagSafe)
- Con il **96W**: ricarica normale, sensibilmente più lenta

### 2) Sotto carico può non bastare
Quando il Mac è sotto stress (editing video, export, rendering, AI, ecc.):

- Il consumo può **superare i 96W**
- Risultato:
- il Mac continua a funzionare
- ma **la batteria si scarica anche se è collegato alla corrente**

Questo è il punto più critico.

### 3) Nessun rischio hardware
Non danneggi nulla:

- Il Mac gestisce automaticamente l’assorbimento
- Non “forzi” la macchina
- Non rovini la batteria nel breve termine

### 4) Possibile effetto collaterale (pratico, non tecnico)
Se lo usi spesso sotto carico con alimentazione insufficiente:

- più cicli di batteria nel tempo
- quindi **usura leggermente maggiore della batteria**

Non è drammatico, ma esiste.

## Quando ha senso usare il 96W

✔️ Va benissimo se:
- uso leggero (browser, mail, Lightroom base, scrittura)
- macchina in idle o quasi
- ti serve un secondo caricatore più leggero

❌ Non è adeguato se:
- fai **video 4K/6K, export, color grading, AI**
- lavori collegato per ore sotto carico
- vuoi prestazioni costanti senza scaricare la batteria

## Conclusione netta

- **Funziona → sì**
- **È equivalente → no**
- **È la scelta giusta per lavoro serio → no**

Se quel Mac è uno strumento di lavoro (e nel tuo caso lo è), il 140W non è un optional: **è lo standard minimo per usarlo come va usato**.

Se vuoi, ti dico anche quando ha senso avere entrambi (140W + 96W) e come usarli in modo intelligente.

---

## 🧑 User

dove posso vedere quanti cores gpu ha la macchina?

---

## 🤖 Assistant

Hai tre modi rapidi. Il primo è quello corretto al 100%.

## Metodo principale (quello giusto)

1. Vai su **menu Apple () → Informazioni su questo Mac**
2. Nella schermata principale vedrai qualcosa tipo:
- “Chip entity["product","Apple M1 Max"]”
- subito sotto: **“GPU X-core”**

Se non lo vedi subito:

3. Clicca su **“Resoconto di sistema”**
4. Vai in **Hardware → Grafica/Monitor**
5. Troverai il dettaglio della GPU (numero di core incluso)

## Metodo veloce da Terminale

Apri Terminale e scrivi:

```bash
system_profiler SPDisplaysDataType
```

Ti stampa direttamente le info della GPU, incluso il numero di core.

## Metodo alternativo (più leggibile)

Sempre da Terminale:

```bash
system_profiler SPHardwareDataType
```

Qui trovi il chip completo (es. M1 Max 24-core GPU oppure 32-core GPU).

## Nota importante (specifica per M1 Max)

Il entity["product","Apple M1 Max"] esiste in due versioni:

- **24 core GPU**
- **32 core GPU**

Stesse prestazioni CPU, cambia solo la potenza grafica.

Se vuoi, mandami lo screenshot e ti dico esattamente che configurazione hai e quanto vale davvero sul mercato.

---

## 🧑 User

ok ho un macbook pro m1 max 32 cores gpu e 64gb ram. era la configurazione massima?

---

## 🤖 Assistant

Sì. Nel contesto della generazione con entity["product","Apple M1 Max"], **sei praticamente al massimo**.

## Configurazione CPU / GPU
image_group{"aspect_ratio":"1:1","query":["Apple M1 Max chip diagram GPU cores","MacBook Pro 16 M1 Max specs GPU 32 core","Apple silicon M1 Max architecture illustration","MacBook Pro 16 2021 ports and design"],"num_per_query":1}
- CPU: 10 core (8 performance + 2 efficiency) → **top, non esisteva superiore**
- GPU: **32 core → massimo disponibile**
- Neural Engine: identico su tutte le versioni

Non esisteva un M1 Max più potente lato compute.

## RAM
- **64 GB unificata → massimo disponibile**
- Con bandwidth molto alta (400 GB/s), ancora oggi molto solida per video, foto e lavori pesanti

## Dove NON è il massimo (unico punto)
- **Storage**: arrivava fino a **8 TB**
- se hai meno, non sei “full optional”
- ma lato prestazioni non cambia nulla

## Tradotto senza giri di parole
- Hai una macchina **top assoluta per quella generazione**
- A livello reale:
- ancora oggi **regge senza problemi lavori professionali seri**
- il collo di bottiglia, se arriva, non è CPU/GPU ma eventualmente storage o workflow

## Confronto onesto con oggi
- I modelli più recenti (M2/M3/M4 Max) sono più efficienti e più veloci
- Ma:
- il tuo setup **non è obsoleto**
- è ancora una **macchina da lavoro alta fascia**

## Conclusione
- **Sì, era il massimo disponibile (a parte eventuale SSD)**
- È una configurazione che oggi ha ancora pieno senso per uso professionale

Se vuoi, posso dirti quanto vale davvero oggi sul mercato, senza farti perdere soldi.