# Cogne Trail

Nuova gara trail a Cogne (Valle d'Aosta, Parco Nazionale Gran Paradiso), ideata da Alessandro Abram con il supporto del Comune di Cogne. Andrea cura identità visiva, sito e materiali per i partner.

## La gara

| | Invergneux 47 | Miniere 28 |
|---|---|---|
| Distanza | 46,5 km | 28 km |
| Dislivello | 2.730 m+ | 1.340 m+ |
| Quota massima | 2.895 m (Passo Invergneux) | 2.425 m (Miniere di Colonna) |
| Partenza | 06:30 | 08:30 |

- **Data proposta:** sabato 4 settembre 2027, weekend 3–5 settembre. È ancora da confermare con il Comune: Cogne è base vita del Tor des Géants, quindi va verificata la disponibilità dei volontari.
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
- **Logo provvisorio:** la scritta "Cogne Trail" in Lexend Zetta 700, italica e con le lettere strette. Il logo definitivo è in sospeso.
- **Foto:** bianco e nero con grana.

## Cartelle

- **`site/`:** sito temporaneo protetto da password.
  - `src/content.html`: testi e sezioni.
  - `src/template.html`: schermata della password, stile e modulo contatti.
  - `src/img/`: foto in bianco e nero usate da sito e PDF.
  - `src/img/originali/`: le foto a colori di partenza.
  - `functions/api/contatto.js`: riceve il modulo contatti su Cloudflare Pages e salva le richieste nel KV `CONTATTI`. L'export CSV si scarica aprendo `/api/contatto` nel browser: chiede utente (qualsiasi) e password (`ADMIN_KEY`).
  - `dist/index.html`: il sito pronto da pubblicare, con il contenuto cifrato.
- **`deck/`:** presentazione per i partner.
  - `build-deck.mjs`: testi e struttura delle slide.
  - `Cogne-Trail-Presentazione.pdf`: il PDF di 18 pagine generato dallo script.

## Comandi

Per convertire una nuova foto nello stile del progetto:

```bash
swift tools/bw.swift site/src/img/originali/nome.jpg site/src/img/nome.jpg
```


Per rigenerare il sito, con la password del sito:

```bash
cd site && node build.mjs "password"
```

Per rigenerare il PDF (serve Google Chrome installato):

```bash
node deck/build-deck.mjs
```

Per vedere il sito in anteprima:

```bash
python3 -m http.server 4321 -d site/dist
```

Il modulo contatti funziona solo una volta pubblicato su Cloudflare Pages. In locale la richiesta fallisce.
