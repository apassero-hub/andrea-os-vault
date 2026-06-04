---
title: "Caricare sito su Hostinger"
created: 2026-05-06
updated: 2026-05-08
model: gpt-5-5
messages: 17
source: chatgpt-import
tags: []
---

# Caricare sito su Hostinger

> Importato da ChatGPT export · 17 messaggi · gpt-5-5 · 2026-05-06

## 🧑 User

ho un sito fatto da claude code in local host, come lo metto online su hostinger?

---

## 🤖 Assistant

Se hai un progetto generato con Claude Code in localhost, devi prima capire **che tipo di progetto è**. Su entity["company","Hostinger"] puoi pubblicare:

- un sito statico (HTML/CSS/JS)
- un frontend React/Vite/Next buildato
- un backend Node.js
- oppure un’app full stack

Il flusso cambia parecchio.
Quello che fai nel 90% dei casi è questo:

---

# 1. Controlla che progetto hai

Apri la cartella del progetto e guarda se hai:

- `package.json`
- `vite.config.js`
- `next.config.js`
- `src/`
- `dist/`
- `build/`

Se c’è `package.json`, quasi sicuramente è un progetto Node/React/Vite/Next.

Da terminale nella cartella:

```bash
cat package.json
```

Guarda gli script tipo:

```json
"scripts": {
"dev": "vite",
"build": "vite build"
}
```

oppure:

```json
"dev": "next dev"
```

---

# 2. Caso più comune: progetto Vite / React

Se Claude ti ha creato un frontend moderno, probabilmente è Vite.

## Build del sito

Nel terminale:

```bash
npm install
npm run build
```

Ti verrà creata una cartella:

```bash
dist/
```

Quella è la versione online del sito.

---

# 3. Carica su Hostinger

## Metodo più semplice: File Manager

Vai su Hostinger:

- Hosting
- Gestisci
- File Manager
- Apri `public_html`

Cancella eventuali file demo.

Poi carica dentro **tutto il contenuto della cartella `dist`**.

NON caricare la cartella stessa.
Carica i file dentro.

Esempio corretto:

```bash
public_html/index.html
public_html/assets/
```

NON:

```bash
public_html/dist/index.html
```

---

# 4. Se il sito dà pagina bianca

Problema classico con React/Vite.

Devi modificare `vite.config.js`:

```js
export default defineConfig({
base: './'
})
```

Poi rifai:

```bash
npm run build
```

e ricarica tutto.

---

# 5. Se usi Next.js

Next non funziona come semplice sito statico.

Hai tre opzioni:

### A. Export statico

Nel `next.config.js`:

```js
output: 'export'
```

Poi:

```bash
npm run build
```

Ti genera `out/`.

Carichi `out` su Hostinger.

---

### B. Hosting Node.js

Serve un piano Hostinger che supporti Node.js.

Molti piani economici NON sono ideali per Next moderno.

---

### C. Soluzione migliore per Next

Mettilo su:

- entity["company","Vercel"]
- oppure entity["company","Netlify"]

e usa Hostinger solo per dominio/email.

Per progetti AI generati automaticamente è spesso molto più stabile.

---

# 6. Metodo professionale consigliato

Non usare upload manuale.

Usa GitHub + deploy automatico.

Flusso corretto:

```bash
localhost
→ GitHub
→ Vercel/Netlify/Hostinger Git Deploy
```

Così ogni modifica viene pubblicata automaticamente.

---

# 7. Come capire subito cosa devi fare

Mandami:

- screenshot della struttura cartelle
oppure
- contenuto di `package.json`

e ti dico esattamente:

- che framework è
- come buildarlo
- dove caricarlo
- se Hostinger va bene oppure no
- eventuali problemi già prevedibili prima del deploy.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, da questa struttura si capisce già molto.

Hai un progetto moderno frontend, probabilmente basato su entity["software","Astro"] (si vede `astro.config.mjs`), e hai già la cartella `dist`.

Quindi il sito è già buildato e pronto per essere pubblicato.

La procedura è molto semplice.

---

# Metodo rapido su Hostinger

## 1. Apri `dist`

Dentro troverai qualcosa tipo:

```text
index.html
assets/
images/
...
```

---

# 2. Vai su Hostinger

Apri:

- Hosting
- Gestisci
- File Manager
- `public_html`

---

# 3. Cancella i file demo

Dentro `public_html` elimina:

- `default.php`
- eventuali file placeholder

---

# 4. Carica il contenuto di `dist`

IMPORTANTE:

Devi caricare il CONTENUTO della cartella `dist`, non la cartella stessa.

Quindi:

✅ corretto:

```text
public_html/index.html
public_html/assets/
```

❌ sbagliato:

```text
public_html/dist/index.html
```

---

# 5. Fine

Aspetta upload completato.

Apri il dominio.

Il sito dovrebbe già funzionare.

---

# Se vedi pagina bianca o CSS rotto

Molto comune.

In quel caso probabilmente Astro sta buildando con path assoluti.

Apri `astro.config.mjs`.

Probabilmente hai qualcosa tipo:

```js
export default defineConfig({
})
```

Modificalo così:

```js
import { defineConfig } from 'astro/config';

export default defineConfig({
site: 'https://tuodominio.it'
});
```

oppure, se serve deploy relativo:

```js
import { defineConfig } from 'astro/config';

export default defineConfig({
base: './'
});
```

Poi rifai:

```bash
npm run build
```

e ricarichi il nuovo `dist`.

---

# Metodo migliore (consigliato)

Dato che lavori spesso su progetti creativi e iterativi:

usa:

```text
GitHub + Vercel
```

molto meglio di Hostinger per questo tipo di siti.

Workflow serio:

```text
Claude Code
→ GitHub
→ deploy automatico
```

Ogni volta che aggiorni:

```bash
git push
```

e il sito si aggiorna da solo.

Per Astro è praticamente perfetto.

---

# Ti consiglio anche questo controllo PRIMA del deploy

Apri terminale nella cartella progetto:

```bash
npm run preview
```

e verifica che il sito buildato funzioni realmente, non solo il localhost dev.

Perché:

```bash
npm run dev
```

e

```bash
npm run build
```

spesso si comportano diversamente.

---

# Ultima cosa importante

NON caricare:

- `node_modules`
- `src`
- `package.json`

Su Hostinger shared hosting non servono.

Serve SOLO `dist`.

Quindi puoi anche zipparla e caricare direttamente quella.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto.
Nel tuo caso devi andare in:

### `PHP/HTML`

anche se il sito non usa PHP.
È semplicemente la sezione hosting classico/statico.

---

# Procedura precisa

## 1. Vai in `PHP/HTML`

Poi:

```text
Gestisci
```

sul dominio corretto.

---

# 2. Cerca `File Manager`

Di solito lo trovi in:

```text
Dashboard hosting
→ File Manager
```

oppure:

```text
Files
→ File Manager
```

---

# 3. Apri `public_html`

Quella è la root del sito.

---

# 4. Elimina i file esistenti

Tipo:

```text
default.php
index.php
```

o pagine demo Hostinger.

---

# 5. Carica il contenuto di `dist`

NON la cartella.

Apri `dist` sul Mac e seleziona:

```text
index.html
assets/
ecc
```

trascinali dentro `public_html`.

---

# 6. Aspetta upload completo

Se il sito è pesante può metterci un po’.

---

# 7. Apri il dominio

Dovrebbe essere online immediatamente.

---

# Se qualcosa non funziona

Dimmi:

- cosa succede
- eventuale errore
- screenshot

Perché i problemi tipici sono solo:

- path assets sbagliati
- cache
- routing SPA
- build non aggiornata

e si sistemano in 2 minuti.

---

## 🧑 User

mi esce 404

---

## 🤖 Assistant

Se esce subito `404`, le cause probabili sono poche:

1. hai caricato la cartella `dist` invece del suo contenuto
2. `index.html` non è dentro `public_html`
3. stai aprendo il dominio sbagliato
4. upload incompleto

Controlla subito così:

Dentro `public_html` devi vedere direttamente:

```text id="b7t2c9"
index.html
assets/
favicon.svg
...
```

NON:

```text id="9vf29m"
public_html/dist/index.html
```

---

# Controllo rapido

Apri File Manager e mandami screenshot di:

```text id="3k4p0m"
public_html
```

così vedo immediatamente dov’è il problema.

---

# Altra possibilità molto comune con Astro

Se il progetto è stato buildato per un sottopercorso, devi rifare la build.

Apri `astro.config.mjs`.

Se trovi qualcosa tipo:

```js id="yq0hgw"
site: 'https://example.com',
base: '/qualcosa/'
```

quello può rompere il deploy.

Mettilo temporaneamente così:

```js id="39mbrl"
import { defineConfig } from 'astro/config';

export default defineConfig({});
```

poi:

```bash id="as8vzr"
npm run build
```

e ricarica il NUOVO contenuto di `dist`.

---

# Verifica anche questo

Nel browser prova:

```text id="m5sx6m"
tuodominio.it/index.html
```

Se lì funziona, allora il problema è configurazione root/index.

Se invece dà ancora 404, il file non è nel posto corretto.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Ok, ora è chiaro.

Il problema è che il tuo progetto NON ha una homepage root (`index.html`) nella root di `dist`.

Hai un sito multilingua:

```text id="jg2gb6"
dist/
it/
en/
```

Quindi la homepage reale probabilmente è:

```text id="9m5cya"
/it/
```

oppure:

```text id="fw0jvq"
/en/
```

Per questo il dominio root dà 404.

---

# Soluzione veloce

Prova ad aprire:

```text id="3mwh6e"
tuodominio.it/it/
```

oppure:

```text id="wefxof"
tuodominio.it/en/
```

Vedrai che probabilmente funziona.

---

# Soluzione corretta

Devi fare in modo che Astro generi anche una homepage root.

Nel progetto probabilmente hai internationalization (i18n) configurata.

---

# Fix rapido professionale

Apri:

```text id="6ccz3e"
src/pages/
```

e crea un file:

```text id="0kjlwm"
index.astro
```

con dentro:

```astro id="e30up1"
---
Astro.redirect('/it/');
---
```

oppure HTML semplice:

```html id="6xpbmk"
<meta http-equiv="refresh" content="0; url=/it/">
```

---

# Poi rebuild

Terminale:

```bash id="ylx40r"
npm run build
```

e ricarichi il nuovo `dist`.

---

# Alternativa ancora più semplice

Se vuoi solo pubblicarlo subito:

carica direttamente il CONTENUTO della cartella `dist/it` dentro `public_html`.

Quindi:

```text id="25w9lh"
dist/it/*
→ public_html/
```

e ignori l’inglese per ora.

Questa è probabilmente la soluzione più veloce nel tuo caso.

---

## 🧑 User

continua a non funzionare, così va solo la home

---

## 🤖 Assistant

Allora il problema è quasi sicuramente il routing statico di Astro su hosting shared.

Succede perché:

- la home funziona
- le pagine interne danno 404

Questo significa che Hostinger sta cercando file fisici invece di gestire il fallback delle route.

---

# Prima cosa da capire

Dimmi che URL dà 404.

Esempio:

```text id="2llp5n"
/it/about
```

oppure:

```text id="9s7azl"
/it/about/
```

Perché cambia tutto.

---

# Problema tipico Astro static

Se le pagine funzionano SOLO con slash finale:

✅ funziona:

```text id="jrl6zl"
/it/about/
```

❌ non funziona:

```text id="n0kux7"
/it/about
```

allora devi forzare trailing slash.

---

# Fix corretto

Apri `astro.config.mjs`.

Metti:

```js id="rjlwmn"
import { defineConfig } from 'astro/config';

export default defineConfig({
trailingSlash: 'always'
});
```

---

# Poi rebuild

```bash id="k3r14g"
npm run build
```

---

# Poi cancella COMPLETAMENTE `public_html`

e ricarica il nuovo build.

---

# Importantissimo

Su Astro static:

```text id="y5s6ut"
/about/
```

funziona perché esiste:

```text id="d04n9y"
/about/index.html
```

mentre:

```text id="o7mglz"
/about
```

su alcuni hosting shared rompe tutto.

---

# Se vuoi la soluzione definitiva

A quel punto ti consiglio seriamente:

## deploy su entity["company","Vercel"]

perché:

- Astro è supportato nativamente
- routing automatico
- SSL automatico
- deploy GitHub automatico
- zero problemi di rewrite

Hostinger shared hosting è pensato più per:

- WordPress
- PHP
- HTML statico semplice

non per framework moderni.

---

## 🧑 User

si tratta di un sito astro + starlight

---

## 🤖 Assistant

Perfetto.
Allora il comportamento è normalissimo: entity["software","Starlight"] usa routing statico basato su directory, e Hostinger shared hosting spesso non gestisce bene le route senza slash finale.

Il fix corretto è questo.

---

# 1. Modifica `astro.config.mjs`

Metti:

```js id="whx54x"
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
trailingSlash: 'always',

integrations: [
starlight({
title: 'Nome sito',
}),
],
});
```

---

# 2. Rebuild completo

Da terminale:

```bash id="bm15rb"
npm run build
```

---

# 3. Cancella TUTTO da `public_html`

Molto importante.

---

# 4. Carica di nuovo il contenuto di `dist`

NON la cartella.

---

# 5. Testa gli URL con slash finale

Esempio:

```text id="8zsmph"
/it/guide/
```

NON:

```text id="jlwm07"
/it/guide
```

---

# Perché succede

Starlight genera:

```text id="k3gwjx"
/guide/index.html
```

e NON:

```text id="m52prk"
/guide.html
```

Hosting moderni fanno automaticamente il rewrite.

Hostinger shared spesso no.

---

# Soluzione migliore in assoluto

Per Astro + Starlight:

## usa entity["company","Vercel"]

È letteralmente il flusso standard per questi framework.

Ti basta:

```text id="r00jmn"
GitHub → import su Vercel → done
```

Zero configurazioni.

---

# Un altro dettaglio importante

Se stai usando:

```js id="ivxg74"
site:
```

in `astro.config.mjs`, assicurati che sia corretto:

```js id="f95hjt"
site: 'https://tuodominio.it',
```

senza slash finale.

---

# Ultima cosa

Se vuoi, puoi mandarmi:

- il contenuto di `astro.config.mjs`
- oppure screenshot della struttura `dist`

e ti dico esattamente:

- cosa sta rompendo
- se il build è corretto
- se conviene modificare routing/i18n
- oppure se è meglio passare direttamente a Vercel.

---

## 🤖 Assistant

Il problema è qui: il tuo config non definisce né `site` né `trailingSlash`. fileciteturn0file0

Con entity["software","Starlight"] su Hostinger shared hosting devi praticamente forzarlo.

Modifica il file così:

```js
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
site: 'https://TUODOMINIO.IT',
trailingSlash: 'always',

integrations: [
starlight({
title: 'Color Management Guide',
description: 'The definitive reference for color management in photography — La guida definitiva al color management in fotografia',

defaultLocale: 'en',

locales: {
en: {
label: 'English',
lang: 'en',
},
it: {
label: 'Italiano',
lang: 'it',
},
},

// resto invariato...
}),
],
});
```

---

# Poi fai QUESTO ORDINE PRECISO

## 1

Cancella completamente `dist`

## 2

Da terminale:

```bash
npm run build
```

## 3

Apri il nuovo `dist`

Ora dovresti vedere strutture tipo:

```text
it/
en/
```

con:

```text
index.html
```

dentro ogni cartella.

---

# 4

Su Hostinger:

- svuota COMPLETAMENTE `public_html`
- carica il nuovo build

---

# 5

Testa URL con slash finale:

✅

```text
/it/foundations/how-we-see-color/
```

❌

```text
/it/foundations/how-we-see-color
```

---

# Se vuoi evitare completamente questo problema

La soluzione pulita è:

## deploy su entity["company","Vercel"]

Perché:

- Astro/Starlight è supportato nativamente
- routing perfetto
- gestione i18n perfetta
- deploy GitHub automatico
- preview branch automatiche

Con Hostinger shared stai sostanzialmente adattando un framework moderno a un hosting pensato per PHP statico.

Funziona, ma con compromessi.

---

## 🧑 User

ma con questi siti come si gestisce il backend?

---

## 🤖 Assistant

Con entity["software","Astro"] + entity["software","Starlight"] normalmente NON hai un backend tradizionale.

Sono framework pensati principalmente per:

- siti statici
- documentazione
- blog
- knowledge base
- landing
- magazine

Quindi:

```text id="7bxpoh"
Markdown → build → HTML statico
```

e basta.

---

# Cosa significa concretamente

Quando fai:

```bash id="0z8n2m"
npm run build
```

Astro genera:

```text id="m7ksv9"
HTML
CSS
JS
```

statici.

Il server non “esegue” il sito.

Serve solo i file.

Per questo puoi hostarlo anche su:

- entity["company","Hostinger"]
- entity["company","Cloudflare"]
- entity["company","Netlify"]
- entity["company","Vercel"]
- GitHub Pages

---

# Ma allora come si fa il backend?

Dipende da cosa ti serve.

---

# Caso 1: sito documentazione/editoriale

Probabilmente il tuo caso.

NON serve backend.

I contenuti stanno in:

```text id="k2t0y9"
src/content/
```

oppure markdown `.md`.

---

# Caso 2: form contatti / newsletter

Usi servizi esterni:

- urlFormspreehttps://formspree.io
- urlResendhttps://resend.com
- urlMailchimphttps://mailchimp.com

senza backend tuo.

---

# Caso 3: auth / utenti / database

Qui entri nel mondo full-stack.

Allora usi:

- urlSupabasehttps://supabase.com
- urlFirebasehttps://firebase.google.com
- urlPocketBasehttps://pocketbase.io

oppure backend Node custom.

---

# Caso 4: backend vero integrato in Astro

Astro supporta:

- SSR
- API routes
- server rendering

MA:

non su hosting shared classico.

Serve:

- VPS
- Node hosting
- Vercel
- Netlify
- Docker

---

# Architettura moderna più comune oggi

Molti siti moderni funzionano così:

```text id="x9dylj"
Frontend statico Astro
+
Backend SaaS/API
```

Esempio:

```text id="vm7u9k"
Astro
+
Supabase (database/auth)
+
Resend (email)
+
Stripe (pagamenti)
```

senza avere un backend monolitico tuo.

---

# Nel tuo caso specifico

Per una guida/documentazione color management:

Astro + Starlight è una scelta ottima.

Hai:

- performance altissime
- SEO forte
- contenuti in markdown
- manutenzione minima
- costi hosting quasi nulli

Non ti serve un backend finché non vuoi:

- utenti
- login
- commenti
- CMS collaborativo
- ecommerce
- dashboard dinamiche

---

# Se vuoi fare il salto “professionale”

Il workflow serio oggi è:

```text id="44t7zj"
Claude Code
→ GitHub
→ Vercel
```

e poi integri backend/API solo quando servono.