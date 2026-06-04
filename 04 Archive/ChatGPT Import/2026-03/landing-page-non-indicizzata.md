---
title: "Landing Page Non Indicizzata"
created: 2026-03-17
updated: 2026-03-17
model: gpt-5-3
messages: 4
source: chatgpt-import
tags: []
---

# Landing Page Non Indicizzata

> Importato da ChatGPT export · 4 messaggi · gpt-5-3 · 2026-03-17

## 🧑 User

come mi assicuro che le landing pages pubblicate siano "not listed" e non ci si possa arrivare se non tramite link diretto?

---

## 🤖 Assistant

Vai diretto: una landing “non listata” non esiste davvero. Esistono solo pagine **non indicizzate** e **non collegate**. Se qualcuno ha il link, può entrarci. Punto.

Quello che puoi fare è ridurre al minimo la possibilità che venga trovata.

---

## 1. Disattiva l’indicizzazione (fondamentale)

### WordPress (Elementor o simili)
- Vai nella pagina → **Impostazioni SEO**
- Attiva:
- `noindex`
- `nofollow`

Se usi plugin tipo **Yoast SEO** o **RankMath**:
- Imposta:
**“Non mostrare nei risultati di ricerca”**

👉 Questo impedisce a Google di indicizzarla.

---

## 2. Non linkarla da nessuna parte

Sembra banale ma è il punto più importante.

- Niente link nel menu
- Niente link nel footer
- Niente link da altre pagine del sito
- Niente sitemap

👉 Se è linkata internamente, prima o poi viene trovata.

---

## 3. Rimuovila dalla sitemap

Se usi Yoast / RankMath:
- Escludi la pagina dalla sitemap XML

👉 Se resta nella sitemap, Google la vede comunque.

---

## 4. URL non intuitivo

Evita robe tipo:
- `/giappone`
- `/canada`

Usa:
- `/fst-honshu-2027-early-access`
- `/jp-pow-ax92`

👉 Non è sicurezza, ma riduce discovery casuale.

---

## 5. (Opzionale) Protezione con password

Se vuoi davvero limitarla:

- WordPress → **Visibilità: Protetta da password**

👉 Questo è l’unico modo per bloccare davvero accesso non voluto
(ma ovviamente aumenta friction per gli utenti)

---

## 6. Controllo robots.txt (extra)

Puoi aggiungere:

```
Disallow: /nome-pagina/
```

👉 Non è una barriera reale, ma un ulteriore segnale ai crawler.

---

## 7. Test finale (fallo sempre)

- Apri pagina in incognito → ok
- Cerca su Google → NON deve uscire
- Controlla con:
```
site:tuosito.com nomepagina
```

---

## Sintesi chiara

Se vuoi una landing “privata”:

- noindex ✔
- non linkata ✔
- fuori sitemap ✔

Se vuoi una landing **davvero chiusa**:
- password ✔

---

Se vuoi, guardiamo insieme la tua landing attuale e ti dico esattamente dove stai rischiando di farla emergere (succede spesso, soprattutto con sitemap e link interni).

---

## 🧑 User

abbiamo yoast

---

## 🤖 Assistant

Perfetto, allora fai così su Yoast. Diretto, senza perdere tempo.

---

## 1. Imposta la pagina come **noindex**

Apri la landing → scorri in basso → **Yoast SEO**

- Vai su **Avanzate**
- Imposta:
- **Consenti ai motori di ricerca di mostrare questa pagina nei risultati? → NO**
- **I motori di ricerca devono seguire i link? → NO**

👉 Risultato: `noindex, nofollow`

---

## 2. Escludila dalla sitemap

Yoast di solito:
- rimuove automaticamente le pagine in noindex dalla sitemap

Ma verifica:

- Vai su:
`tuosito.com/sitemap_index.xml`
- Apri la sitemap delle pagine
- Controlla che **NON ci sia la landing**

Se c’è → hai un problema di configurazione

---

## 3. Assicurati che non sia linkata

Controllo rapido:
- menu → niente
- footer → niente
- altre pagine → niente

Se usi Elementor:
- attenzione a **template globali** o sezioni duplicate

---

## 4. URL

Evita slug puliti tipo:
- `/giappone`

Meglio:
- `/fst-honshu-2027`
- `/early-jp-access`

---

## 5. Forza la rimozione (se era già online)

Se la pagina era già indicizzata:

- Vai su **Google Search Console**
- Inserisci URL → **Richiedi rimozione temporanea**

👉 altrimenti resta visibile per settimane

---

## 6. Check finale (obbligatorio)

Fai questo:

- incognito → apri link → ok
- Google:
```
site:tuosito.com nomepagina
```

Se non esce → sei a posto

---

## Realtà (importante)

Questa non è sicurezza:
- chi ha il link entra
- chi intercetta il link entra

Se devi usarla per:
- campagne ads → perfetto
- funnel → perfetto

Se devi tenerla davvero privata:
- usa password

---

Se vuoi, mandami una landing e ti faccio un audit veloce. Di solito il 90% degli errori sta nella sitemap o nei link interni.