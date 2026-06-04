---
title: "Crediti Netlify spiegati"
created: 2026-05-16
updated: 2026-05-16
model: gpt-5-5
messages: 8
source: chatgpt-import
tags: []
---

# Crediti Netlify spiegati

> Importato da ChatGPT export · 8 messaggi · gpt-5-5 · 2026-05-16

## 🧑 User

Come funzionano i crediti di utilizzo di netlify?

---

## 🤖 Assistant

Netlify sta passando da un modello “a limiti separati” (build minutes, bandwidth, function invocations ecc.) a un sistema a **crediti unificati**. In pratica hai un budget mensile di crediti e ogni operazione consuma una certa quantità. cite

In questo momento ci sono due sistemi:
- account “legacy” → vecchi limiti separati
- nuovi account → sistema a crediti

## Come funziona in pratica

Ogni piano include un tot di crediti al mese:

| Piano | Crediti/mese |
|---|---|
| Free | 300 |
| Personal | 1000 |
| Pro | 3000 |

cite

Questi crediti vengono consumati da:

| Operazione | Consumo |
|---|---|
| Deploy produzione | 15 crediti |
| Bandwidth | 20 crediti / GB |
| Compute (functions ecc.) | 10 crediti / GB-hour |
| Web requests | 2 crediti / 10.000 richieste |

cite

Le deploy preview invece normalmente non consumano crediti. cite

---

## Esempio concreto

Hai:
- portfolio fotografico statico
- qualche form contatti
- poche migliaia di visite al mese

Probabilmente:
- consumi pochissimo compute
- poche richieste
- il vero consumo è il bandwidth delle immagini/video

Quindi se:
- il sito genera 10 GB di traffico → ~200 crediti
- fai 5 deploy → 75 crediti

Totale circa:
- 275 crediti

Quindi rientri ancora nel Free.

---

## La cosa importante da capire

### Siti statici = costano poco
Se usi:
- Astro
- Next static export
- Hugo
- portfolio statico

il consumo resta molto basso.

### Funzioni serverless / AI = consumano molto
Se inizi a usare:
- API dinamiche
- image transformation
- AI
- backend complessi
- auth
- rendering server-side

i crediti salgono rapidamente.

---

## Cosa succede quando finiscono

### Piano Free
Hard limit:
- il sito può venire sospeso fino al reset mensile

cite

### Piani a pagamento
Puoi:
- comprare crediti extra
- attivare auto recharge

cite

---

## Per il tuo caso specifico

Per:
- portfolio fotografico
- landing page
- sito Forever
- blog leggero

Netlify è spesso ottimo:
- deploy semplici
- CDN globale
- HTTPS automatico
- CI/CD integrato
- costi bassi

Ma se prevedi:
- molto traffico immagini/video
- contenuti media pesanti
- funzionalità dinamiche importanti

allora devi monitorare bene il bandwidth, perché è la voce che può esplodere più facilmente per un fotografo/videomaker.

La dashboard usage di Netlify ti mostra esattamente dove stai consumando i crediti.

---

## 🧑 User

Il sito in questione è https://colormanagement.guide

---

## 🤖 Assistant

Per urlColorManagement.guidehttps://colormanagement.guide non vedo particolari rischi di “esplosione” dei crediti Netlify, almeno nella configurazione attuale.

Da quello che si vede:
- sito principalmente statico
- contenuti editoriali
- immagini
- nessuna web app pesante
- nessun backend complesso
- niente AI server-side
- niente video hostati direttamente

quindi il consumo principale sarà quasi esclusivamente:
1. bandwidth
2. deploy di produzione

---

## Il vero punto critico del tuo sito: le immagini

Essendo un sito sul color management:
- probabilmente userai screenshot
- comparazioni
- immagini ad alta qualità
- gallery abbastanza pesanti

E lì Netlify inizia a diventare meno conveniente.

Con il nuovo sistema:
- 1 GB traffico = 20 crediti cite
- piano Free = 300 crediti/mese cite

Tradotto:
- circa 15 GB/mese di traffico e hai già finito il Free.

---

## Facciamo una simulazione realistica

Supponiamo:
- homepage + articoli abbastanza visuali
- peso medio visita: 15–25 MB
- 1000 visitatori/mese

Hai facilmente:
- 15–25 GB di bandwidth

Quindi:
- 300–500 crediti solo di traffico

E sei già oltre il Free.

---

## Però attenzione: non significa che costerà tanto

Il punto è che:
- i credit pack extra costano poco
- Netlify resta abbastanza economico per siti medi cite

Ma devi ottimizzare bene:
- WebP/AVIF
- lazy loading
- responsive images
- evitare PNG enormi
- evitare immagini full-res inutili

Per un sito fotografia/color workflow, questa parte cambia tutto.

---

## Deploy: quasi irrilevanti nel tuo caso

Ogni deploy produzione:
- 15 crediti cite

Se deployi:
- 10 volte/mese
→ 150 crediti

Ma:
- preview deploy sono gratis cite

Quindi puoi lavorare quasi sempre in preview e pubblicare solo quando serve.

---

## Dove inizierebbe a diventare problematico

Se in futuro aggiungi:
- comparatore monitor interattivo
- upload immagini
- conversioni ICC server-side
- tool online
- image CDN aggressivo
- corsi/video hostati direttamente

allora il consumo cresce rapidamente.

---

## Per il tuo caso, oggi

Direi realisticamente:

| Scenario | Piano probabile |
|---|---|
| traffico basso (<500 utenti/mese) | Free |
| traffico medio con immagini pesanti | Personal |
| blog molto visto / SEO forte | Pro |

---

## Quello che farei io nel tuo caso

Per un progetto come questo:

- Netlify → ottimo per hosting/deploy
- immagini → meglio usare:
- Cloudflare Images
- BunnyCDN
- ImageKit
- oppure ottimizzazione locale seria

Perché Netlify oggi è molto competitivo sul deploy workflow, meno sul traffico media intenso.

Specialmente per un fotografo/videomaker che tende naturalmente a caricare asset grossi.

---

## 🧑 User

Mi ha appena detto che ho fatto il 50% del credito mensile. Questo da cosa può essere dovuto al fatto che ho fatto delle modifiche al sito abbastanza frequenti ogni volta che faccio un aggiornamento su CloudCode in automatico mi aggiorna anche sul sito e questi qui succhiano crediti, può essere quello. Se invece adesso non faccio più modifiche e lo lascio così, dovrebbero non esserci problemi.

---

## 🤖 Assistant

Sì, è molto probabile che una grossa parte del consumo venga dai deploy automatici continui.

Su Netlify:
- ogni **production deploy** consuma crediti
- anche se cambi solo una riga di testo
- CI/CD automatico + tanti push = crediti che evaporano velocemente

Nel tuo caso, usando CloudCode con aggiornamento automatico del sito, probabilmente hai creato involontariamente questo scenario:

```text
modifica → push → build → deploy produzione → crediti consumati
```

Se stavi iterando tanto:
- fix grafici
- testo
- CSS
- responsive
- immagini
- SEO
- debug

puoi tranquillamente aver fatto decine di deploy in pochi giorni.

E quello da solo può spiegare buona parte del 50%.

---

Ma c’è un’altra cosa importante:

## Il consumo che vedi NON è necessariamente solo bandwidth

Netlify somma:
- deploy
- bandwidth
- build compute
- function usage

Quindi in fase di sviluppo il problema spesso sono:
- deploy continui
- build ripetute

non tanto il traffico reale del sito.

---

## Se adesso smetti di modificarlo

Sì, molto probabilmente:
- il consumo rallenta drasticamente
- o quasi si ferma

Perché un sito statico lasciato online:
- consuma pochissimo compute
- nessun deploy
- solo bandwidth reale dei visitatori

E visto che il sito è ancora abbastanza nuovo, dubito che tu stia già facendo numeri di traffico tali da bruciare metà crediti solo con le visite.

---

## Cosa ti consiglio di fare subito

### 1. Guarda il breakdown usage
Vai in:
- Site settings
- Usage and billing
- Usage details

e controlla:
- Deploys
- Bandwidth
- Build minutes / compute

Lì capisci immediatamente il colpevole.

---

## 2. Disattiva deploy automatici inutili
Molto importante.

Puoi:
- deployare solo manualmente
- usare preview deploy
- oppure deployare produzione solo quando vuoi

Perché in sviluppo continuo Netlify può diventare sorprendentemente “costoso” in crediti.

---

## 3. Occhio alle immagini
Sul tuo sito questo resta il secondo possibile colpevole.

Se hai:
- PNG enormi
- screenshot 4K
- immagini non ottimizzate

anche pochi visitatori possono generare parecchio bandwidth.

---

## La buona notizia

Se il sito ora:
- è stabile
- non fai più 20 update al giorno

allora è molto probabile che il consumo mensile reale scenda tantissimo.

Quindi non sembra un problema strutturale del progetto, ma più una conseguenza della fase intensa di sviluppo.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, qui si vede chiaramente il problema.

Non è il traffico.
Non sono le immagini.
Non sono i visitatori.

Sono quasi esclusivamente i deploy automatici.

## Breakdown reale del tuo consumo

| Voce | Crediti |
|---|---|
| Production deploys | 150 |
| Web requests | 0.4 |
| Bandwidth | 0.3 |
| Compute | 0 |

Hai fatto:
- 10 deploy produzione
- 15 crediti ciascuno
- totale 150 crediti

Quindi:
- il 99,5% del consumo è dovuto agli aggiornamenti del sito

Il traffico reale del sito è praticamente irrilevante al momento.

---

## Tradotto concretamente

Se adesso:
- smetti di pushare continuamente
- lasci il sito online così com’è

allora:
- consumerai quasi zero crediti
- probabilmente pochi crediti al mese
- il Free plan ti basta tranquillamente

Perché:
- 1998 richieste web = solo 0.4 crediti
- bandwidth = 0.3 crediti

Questi numeri sono minuscoli.

---

## Quindi sì: CloudCode + auto deploy è il colpevole

Probabilmente ogni volta che:
- salvavi
- pushavi
- aggiornavi una sezione
- correggevi CSS/testi

partiva:
```text
build → production deploy → 15 crediti bruciati
```

10 modifiche = metà piano gratuito evaporato.

---

## Cosa fare adesso

Ti consiglio:

### Durante sviluppo intenso
NON deployare direttamente in produzione ogni volta.

Meglio:
- preview deploy
oppure
- branch separato
oppure
- deploy manuale finale

---

## Per il tuo caso specifico

Il tuo sito è molto “economico” da hostare.
Questo screenshot lo conferma.

Quindi:
- nessun problema strutturale
- nessun rischio serio
- nessuna necessità immediata di cambiare hosting

Hai semplicemente:
- usato il sito come ambiente di sviluppo continuo
- e Netlify ti ha conteggiato ogni pubblicazione live.

Adesso che il sito è più stabile, il consumo reale sarà bassissimo.