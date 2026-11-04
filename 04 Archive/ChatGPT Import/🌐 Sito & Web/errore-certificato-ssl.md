---
title: "Errore certificato SSL"
created: 2026-02-27
updated: 2026-02-27
model: gpt-5-2
messages: 2
source: chatgpt-import
tags: [sito-web]
category: "🌐 Sito & Web"
---

# Errore certificato SSL

> Importato da ChatGPT export · 2 messaggi · gpt-5-2 · 2026-02-27

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

Ci hanno segnalato questo del nostro sito forever

---

## 🤖 Assistant

Errore chiaro: **NET::ERR_CERT_COMMON_NAME_INVALID**.
Significa che il certificato SSL installato **non corrisponde al dominio richiesto** (probabilmente problema tra `foreversnowtrips.com` e `www.foreversnowtrips.com`).

In pratica:
- Il certificato è valido per un dominio
- Il browser sta caricando l’altro
- Oppure il certificato è scaduto / non rinnovato correttamente
- Oppure DNS e hosting non stanno puntando allo stesso server

---

## Cosa controllare subito

### 1️⃣ Verifica se il problema è su:
- `https://foreversnowtrips.com`
- `https://www.foreversnowtrips.com`

Spesso uno funziona e l’altro no.

---

### 2️⃣ Controlla il certificato SSL
Dal provider hosting o da:
- Cloudflare (se lo usate)
- cPanel
- Plesk
- Vercel / Netlify / altro se sito statico

Devi verificare:
- Che il certificato includa **sia dominio root che www**
- `foreversnowtrips.com`
- `www.foreversnowtrips.com`
- Che non sia scaduto
- Che sia correttamente assegnato al dominio

---

### 3️⃣ Controlla DNS
Se usate Cloudflare:
- Verifica che il record A del dominio e del www puntino allo stesso IP
- Verifica che SSL mode sia:
- **Full (Strict)** se il certificato è valido lato server
- Non “Flexible”

---

### 4️⃣ Problema molto probabile
Se qualcuno ha:
- cambiato hosting
- modificato DNS
- attivato www recentemente
- migrato server

Il certificato probabilmente non è stato rigenerato.

Soluzione veloce:
- Rigenerare certificato Let’s Encrypt
- Includere entrambi i domini
- Forzare redirect 301 da uno all’altro

---

## Cosa fare ora operativamente

Dimmi:
- Dove è hostato il sito?
- Usate Cloudflare?
- È WordPress o statico?

Ti do checklist precisa step-by-step per sistemarlo in 15 minuti.

Questo tipo di errore va risolto subito perché:
- Riduce fiducia
- Penalizza SEO
- Blocca utenti non tecnici

Non è grave. È solo configurazione SSL.