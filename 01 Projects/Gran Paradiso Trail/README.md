# Cogne Trail

Nuova gara trail a Cogne (Valle d'Aosta, Parco Nazionale Gran Paradiso), ideata da Alessandro Abram con il supporto del Comune di Cogne. Andrea cura identità visiva, sito e materiali per i partner.

## La gara

| | Invergneux 47 | Miniere 28 |
|---|---|---|
| Distanza | 46,5 km | 28 km |
| Dislivello | 2.730 m+ | 1.340 m+ |
| Quota massima | 2.895 m (Passo Invergneux) | 2.425 m (Miniere di Colonna) |
| Partenza | 06:30 | 08:30 |

- **Data proposta:** sabato 12 giugno 2027, weekend 11–13 giugno (seconda scelta 19 giugno). Settembre è scartato perché troppo vicino al TORX. Calendario e motivi in `DATA.md`. Da confermare con il Comune, con il Parco e con lo stato della neve al Passo Invergneux.
- **Atleti alla prima edizione:** 400–500.
- **Organizzazione:** "Cogne Trail". Il nome di Alessandro non compare come organizzatore.

## Identità visiva

- **Font:** Lexend Zetta per i titoli e Inter Tight per il testo.
- **Colori:**
  - neve `#E4E6DA`
  - magnetite `#1E2119`
  - larice (rosso ruggine) `#B5412A`, oppure `#D4573D` sul fondo scuro
  - lichene `#6B7258`
  - roccia `#8D917F`
- **Logo:** sito e PDF usano solo la scritta "Cogne Trail" in Lexend Zetta 700, italica e stretta. Il segno della valle (la V di Cogne con il Gran Paradiso dietro) e il timbro sono in `logo/`, messi da parte per il futuro e non ancora usati.
- **Foto:** bianco e nero con grana.

## Cartelle

- **`site/`:** sito temporaneo protetto da password.
  - `src/content.html`: testi e sezioni.
  - `src/template.html`: schermata della password, stile e modulo contatti.
  - `src/img/`: foto in bianco e nero usate da sito e PDF.
  - `src/img/originali/`: le foto a colori di partenza.
  - `functions/api/contatto.js`: riceve il modulo contatti su Cloudflare Pages e salva le richieste nel KV `CONTATTI`. L'export CSV si scarica aprendo `/api/contatto` nel browser: chiede utente (qualsiasi) e password (`ADMIN_KEY`).
  - `functions/api/accesso.js`: registra chi entra nell'anteprima (email, data, paese, città, browser) nel KV `ACCESSI`. Ogni accesso è una riga; rientrare nella stessa sessione del browser non crea un nuovo accesso.
  - `dist/index.html`: il sito pronto da pubblicare, con il contenuto cifrato.

## Accessi e contatti

Per entrare nel sito bisogna inserire email e password. L'email viene registrata e precompila anche il modulo contatti.

Una volta pubblicato su Cloudflare Pages, gli elenchi si scaricano in CSV aprendo questi indirizzi nel browser. Il browser chiede utente e password: l'utente è libero, la password è la variabile `ADMIN_KEY` impostata su Cloudflare.

- tutti gli accessi: `/api/accesso`
- una riga per persona, con numero di accessi, primo e ultimo: `/api/accesso?riepilogo=1`
- richieste dal modulo contatti: `/api/contatto`
- **`logo/`:** loghi messi da parte, generati da `tools/logo.mjs`. Per ora non sono usati da sito e PDF.
  - `segno.svg` e `segno-scuro.svg`: il segno da solo, per fondo chiaro e fondo scuro.
  - `segno-scritta.svg`: segno con scritta.
  - `timbro.svg`: versione circolare per medaglie, toppe e adesivi.
  - `archivio/`: le bozze scartate, tenute come riferimento.
- **`deck/`:** presentazione per i partner.
  - `build-deck.mjs`: testi e struttura delle slide.
  - `Cogne-Trail-Presentazione.pdf`: il PDF di 18 pagine generato dallo script.
  - `build-cas.mjs` e `Cogne-Trail-Proposta-CAS.pdf`: la proposta di 10 pagine per Cogne Acciai Speciali. Riprende lo stile da `build-deck.mjs`. Note e testo dell'email sono in `PROPOSTA-CAS.md`.
- **`budget/`:** `Cogne_Trail_2027_Budget_v2.xlsx`, il budget unico a tre scenari costruito sui file di Ale. Si rigenera con `tools/budget_v2.py`. La revisione e i risultati sono in `BUDGET.md`.
- **`PARTNER.md`:** ricerca dei possibili partner, dei fondi e dei contatti.

## Comandi

Per convertire una nuova foto nello stile del progetto:

```bash
swift tools/bw.swift site/src/img/originali/nome.jpg site/src/img/nome.jpg
```


Per rigenerare i file del logo:

```bash
node tools/logo.mjs
```

Per rigenerare il sito, con la password del sito:

```bash
cd site && node build.mjs "password"
```

Per rigenerare il PDF (serve Google Chrome installato):

```bash
node deck/build-deck.mjs
```

Per rigenerare la proposta per Cogne Acciai Speciali:

```bash
node deck/build-cas.mjs
```

Per vedere il sito in anteprima:

```bash
python3 -m http.server 4321 -d site/dist
```

Il modulo contatti funziona solo una volta pubblicato su Cloudflare Pages. In locale la richiesta fallisce.
