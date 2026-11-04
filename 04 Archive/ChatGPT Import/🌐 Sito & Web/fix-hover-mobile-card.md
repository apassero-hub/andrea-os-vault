---
title: "Fix hover mobile card"
created: 2025-11-02
updated: 2025-11-02
model: gpt-5
messages: 4
source: chatgpt-import
tags: [sito-web]
category: "🌐 Sito & Web"
---

# Fix hover mobile card

> Importato da ChatGPT export · 4 messaggi · gpt-5 · 2025-11-02

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

ho un problema col nostro sito https://www.foreversnowtrips.com/ nello specifico dove ci sono le card se ci passi sopra il mouse in hover la card diventa blu con scritto "scopri" ma non si vede più niente sotto. questo è accettabile da desktop ma da mobile crea problemi di visualizzazione visto che il pacchetto sparisce scrollando. è un template fatto dal web deigner su elementor ma siccome è un testa di cazzo vorrei trovare la soluzione di metterci mano e riolvere la questione io

---

## 🤖 Assistant

Capito il problema: l’overlay “Scopri” copre tutto in hover. Su mobile (dove non esiste “hover”) l’overlay resta attivo mentre scorri e ti nasconde la card. La soluzione più pulita è **mostrare l’overlay solo sui device che hanno davvero l’hover** e **disattivarlo su touch**.

Ti lascio un fix **copia-incolla** + come applicarlo in Elementor in 2 minuti.

# Fix consigliato (solo CSS)

1) In Elementor, apri la sezione che contiene le card (listing/grid)
→ tab **Avanzate → CSS Classes** e metti: `fst-cards`

2) Vai su **Site Settings → Custom CSS** (oppure CSS personalizzato del tema) e incolla:

```css
/* Attiva overlay solo su desktop con hover “vero” */
@media (hover: hover) and (pointer: fine) {
.fst-cards.card,
.fst-cards.elementor-column,
.fst-cards.jet-listing-grid__item {
position: relative;
}

/* Se l’overlay è un elemento dedicato */
.fst-cards.overlay,
.fst-cards.elementor-background-overlay,
.fst-cards.card::before {
transition: opacity.25s ease;
}

/* Mostra overlay SOLO al passaggio del mouse */
.fst-cards.card:hover.overlay,
.fst-cards.elementor-column:hover >.elementor-element-populated >.elementor-background-overlay,
.fst-cards.card:hover::before {
opacity: 1!important;
visibility: visible!important;
}
}

/* Disattiva overlay su touch/mobile */
@media (hover: none), (pointer: coarse) {
/* Se overlay è un DIV */
.fst-cards.overlay,
.fst-cards.elementor-background-overlay {
opacity: 0!important;
visibility: hidden!important;
display: none!important;
}
/* Se overlay è creato via pseudo-elemento */
.fst-cards.card::before,
.fst-cards.elementor-column::before {
content: none!important;
}
/* Evita che stili:hover si attivino comunque su tap */
.fst-cards.card:active.overlay,
.fst-cards.elementor-column:active >.elementor-element-populated >.elementor-background-overlay {
opacity: 0!important;
visibility: hidden!important;
}
}
```

> Nota: ho coperto **tutti i casi tipici Elementor/JetEngine**: overlay come `elementor-background-overlay`, overlay come `<div class="overlay">`, oppure overlay via `::before`. Con la classe contenitore `fst-cards` limitiamo il fix solo a quella sezione.

3) **Pulisci la cache** (plugin cache/CDN) e ricarica.

---

## Variante B (se vuoi mantenere “Scopri” anche su mobile)
Mostra solo un **badge** senza coprire la card:

```css
@media (hover: none), (pointer: coarse) {
.fst-cards.overlay {
background: none!important;
opacity: 1!important;
visibility: visible!important;
display: block!important;
pointer-events: none; /* non blocca i click sulla card */
}
.fst-cards.overlay.label-scopri {
position: absolute;
bottom:.75rem; right:.75rem;
padding:.4rem.6rem;
background: rgba(0,0,0,.6);
color: #fff;
border-radius:.4rem;
font-weight: 600;
}
}
```

Basta avere dentro l’overlay un elemento con classe `.label-scopri`. Così su mobile resta solo il bottoncino, la foto/testo non scompaiono.

---

## Dove può cambiare il selettore
- Se nell’editor vedi classi diverse (es. `jet-listing-dynamic-link`/`jet-engine-listing`), sostituiscile dentro ai blocchi mantenendo la struttura.
- Se l’overlay è legato alla **colonna** con *Elementor Background Overlay*, i selettori con `elementor-background-overlay` fanno già il lavoro.

---

## Perché questa soluzione è solida
- Usa le media query moderne `hover` e `pointer`, quindi non serve JS né sniffing user-agent.
- Mantiene l’effetto “coprente” su desktop (dove ha senso) e lo **disabilita su touch**, evitando i ghost-hover durante lo scroll.
- È limitata alla sezione con `fst-cards`, zero effetti collaterali su altre parti del sito.

Se vuoi, mandami uno screenshot del DOM di una card (lato Inspector) e ti restituisco i selettori “perfetti” già confezionati per il tuo template.

---

## 🧑 User

non potrebbe solo cambiare il fatto che invece di essere un solid color diventi colorata ma con trasparenza?

---

## 🤖 Assistant

Sì — ottima idea 👌
è la soluzione più semplice, “non distruttiva” e visivamente anche più bella: invece di nascondere tutto sotto un blocco blu opaco, rendi l’overlay **semi-trasparente**, così il testo “Scopri” resta leggibile ma si vede comunque la card sotto.

### Ti spiego come farlo in 1 minuto

#### 1️⃣ Trova dove sta l’overlay
Nel 99% dei casi Elementor la genera come:
```html
<div class="elementor-background-overlay"></div>
```
oppure
```html
<div class="overlay"></div>
```

#### 2️⃣ Aggiungi questo CSS
Vai su **Aspetto → Personalizza → CSS aggiuntivo** (oppure su Elementor → Impostazioni sito → CSS personalizzato) e incolla:

```css
/* Overlay trasparente al posto di pieno */
.elementor-background-overlay,
.overlay {
background: rgba(0, 51, 102, 0.6)!important; /* blu 60% opaco */
transition: background 0.3s ease;
}

/* Effetto hover più evidente ma sempre trasparente */
.elementor-column:hover >.elementor-element-populated >.elementor-background-overlay,
.card:hover.overlay {
background: rgba(0, 51, 102, 0.75)!important; /* un po’ più scuro al passaggio */
}
```

👉 puoi cambiare i valori a piacere:
- `rgba(0, 51, 102, 0.6)` → il primo numero (`0, 51, 102`) è il colore blu;
- l’ultimo (`0.6`) è la trasparenza (0 = trasparente, 1 = pieno).

Ad esempio:
- **0.5** = 50% trasparente
- **0.7** = più scuro
- **0.3** = più leggero

---

#### 3️⃣ (Facoltativo) Se vuoi una tinta diversa
Puoi sostituire il blu con il colore brand Forever:
```css
background: rgba(15, 40, 90, 0.65);
```
oppure anche usare un **gradiente**:
```css
background: linear-gradient(rgba(10,20,60,0.5), rgba(10,20,60,0.5));
```

---

#### ✅ Risultato
- Su desktop: l’hover mostra “Scopri” con sfondo traslucido → il contenuto sotto rimane visibile.
- Su mobile: se Elementor mantiene l’overlay attivo, non nasconde più la card, perché non è opaco.

---

Se vuoi, mandami il codice sorgente di una singola card (tasto destro → “Ispeziona” → copia `<div class="elementor-column...">...</div>`) e ti do la versione CSS perfetta con il tuo esatto colore e trasparenza.