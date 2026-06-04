---
title: "colormanagement.guide"
area: Projects
status: in-progress
updated: 2026-06-04
tags: [progetto, color-management, fotografia, sito, astro, newsletter, SEO, content]
---

# colormanagement.guide

> Nota di progetto · `01 Projects/colormanagement.guide/`  
> Aggiornata: 2026-06-04

Sito documentale bilingue (IT/EN) sulla gestione del colore in fotografia.  
URL: [colormanagement.guide](https://colormanagement.guide)

---

## 🎯 Obiettivo e posizionamento

**Target:** fotografi, videomaker e creativi freelance che vogliono un workflow colore affidabile dalla ripresa alla stampa. Non color scientist, non VFX engineer.

**Domanda filtro per ogni contenuto:** *"Questa informazione migliora concretamente il workflow dell'utente?"*

**Doppia funzione:**
- Risorsa pubblica educativa gratuita
- Vettore di autorità professionale e SEO per il brand Andrea Passerini

**Perché esiste:** la documentazione sul color management è frammentata, datata o scritta per tecnici — mancava una risorsa unitaria per il fotografo pratico. Il sito colma quel gap e costruisce nel tempo un asset di base per consulenze, partnership e un eventuale video course.

---

## 🔧 Stack tecnico

| Componente | Soluzione |
|---|---|
| Framework | Astro 4 + Starlight |
| Repo | GitHub privato (`apassero-hub/colormanagement-guide`) |
| Hosting | Cloudflare Pages (build auto al push su `main`) |
| DNS | Cloudflare (TXT Search Console + DMARC) |
| Analytics | Cloudflare Web Analytics + Google Search Console |
| Newsletter | Kit (ex ConvertKit) — piano free fino a 10k iscritti |
| Sviluppo | Claude Code + Superpowers + Frontend Design |
| Sito collegato | andreapasserini.com (backlink dofollow dall'About) |

**Email deliverability:** DMARC `p=quarantine` — il minimo per evitare spam e abilitare BIMI.  
**CSS:** tutte le regole sotto `.sl-markdown-content` (regola fondamentale dopo bug scoperto).

---

## 📂 Struttura dei contenuti

120+ pagine bilingue organizzate in 10 sezioni. Ogni pagina ha un badge livello come **indicatore di prerequisiti**, non come step di curriculum (decisione: PathNav rimosso).

| Sezione | Argomento |
|---|---|
| `start/` | Ingressi narrativi — il problema del colore, da dove iniziare |
| `foundations/` | Come vediamo il colore, CIE XYZ, gamma, delta E, chromatic adaptation |
| `monitor/` | Calibrazione vs profilazione, hardware calibration, wide gamut, HDR |
| `icc-profiles/` | Anatomia profili, rendering intents, matrix vs LUT, gamut mapping |
| `working-spaces/` | sRGB, Adobe RGB, ProPhoto, Display P3 |
| `raw-camera/` | RAW e colore, camera profiles, ColorChecker, scene-referred workflow |
| `printing/` | Soft proofing, rendering intent stampa, carte, OBA/FWA, fine art |
| `workflows/` | Lightroom e Capture One end-to-end |
| `tools/` | Strumenti di analisi (ColorThink, ecc.) |
| `troubleshooting/` | Stampe più scure, colori Instagram, diff LR/PS, wide gamut — SEO trasversale |

---

## 💰 Modello di business

**Nessuna monetizzazione diretta oggi.** Funnel di autorità in 5 fasi — **non bruciare le fasi** è la regola principale:

| Fase | Stato |
|---|---|
| 1. Sito gratuito SEO-ottimizzato | ✅ Live |
| 2. Newsletter Color Lab come lead nurture | ✅ Attiva |
| 3. Consulenze 1:1 come validazione domanda | ⏳ |
| 4. Pattern consulenze → FAQ → contenuti | ⏳ |
| 5. Video course (solo dopo validazione) | ⏳ |

**Stream futuri:** partnership hardware (Calibrite, Eizo, BenQ — già contattati) · split newsletter IT/EN sopra 300 iscritti (richiede Kit Creator a pagamento)

---

## 📧 Newsletter — Color Lab

- **Provider:** Kit (ex ConvertKit), piano free
- **Form IT:** ID `9464779` · **Form EN:** ID `9464998`
- **Automazione:** Visual Automation bilingue a due ingressi → sequenza unica "Color Lab — Onboarding"
- **Template:** HTML custom — barra spettro 7 colori, Georgia per H, Inter per body
- **Episodi live:** 3 evergreen (export da Photoshop, mismatch stampa-monitor, soft proofing)
- **Split IT/EN:** deferred fino a >300 iscritti (poi Kit Creator a pagamento)

---

## 📊 Stato attuale

### ✅ Completato
- Sito live con 120+ pagine bilingue
- Sitemap attiva · canonical fix su `/en/`
- Analytics e Search Console in raccolta
- Newsletter Color Lab con 3 episodi
- Form newsletter (inline homepage/about + compact sidebar TOC)
- UX Lotto 1 e 2 (font self-hosted, lead paragraph, dead CSS, table mobile, hero H1, CTA, icone, H2)
- PathNav rimosso
- About andreapasserini.com riscritto con backlink dofollow

### 🔄 In corso
- UX Lotto 3 (guard TOC duplicato, header shadow, reading time, scroll progress bar)

### 📌 Aperto
- ~47 traduzioni IT residue
- UX Lotto 4 (breadcrumbs, hero H1 -20/30%, redesign 3 SVG diagrammi)
- "Scegli il Tuo Percorso" → riscrivere come mappa di orientamento (slug invariato)
- Filtro sidebar livello con pillole multiselect + sessionStorage
- Pipeline n8n automazione newsletter (deferred — serve più contenuto prima)

---

## 🚀 Piano soft launch

**Sequenza:**
1. Chiudere ~47 traduzioni residue
2. Consolidare newsletter
3. Verificare analytics
4. Lancio pubblico: Juza · gruppi FB fotografia · outreach fotografi influenti

---

## 🧠 Decisioni chiave

**PathNav rimosso** (maggio 2026) — simulava un corso inesistente, confliggeva col futuro video course, competeva con la navigazione Starlight.

**Kit invece di Buttondown** — piano free più capiente (10k vs 1k iscritti).

**Cloudflare Pages** (da Hostinger → Netlify → Cloudflare) — Hostinger bloccava bot lato server rompendo i preview social.

**DMARC `p=quarantine`** — `p=none` non bastava, newsletter finiva in spam.

**Record TXT Search Console da verificare sempre** dopo ogni migrazione DNS.

**CSS scope** — tutte le regole sotto `.sl-markdown-content`, mai globali.

**No video sul dominio principale** — eventuale `colormanagement.video` separato in futuro.

---

## 🔗 Note correlate

- [[Stack Tecnico]] — hardware di calibrazione usato (BenQ SW270C + Calibrite)
- [[Sito andreapasserini.com]] — sito collegato con backlink dofollow
- [[Business Photography — Preventivi e Commerciale]] — consulenze come fase 3 del funnel
- Archivio ChatGPT: cerca `color management`, `colormanagement guide`, `astro`, `newsletter`, `kit`

