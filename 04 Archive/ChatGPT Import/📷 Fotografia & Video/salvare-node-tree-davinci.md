---
title: "Salvare Node Tree DaVinci"
created: 2026-02-03
updated: 2026-02-03
model: gpt-5-2
messages: 2
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Salvare Node Tree DaVinci

> Importato da ChatGPT export · 2 messaggi · gpt-5-2 · 2026-02-03

## 🧑 User

come faccio a salvare un node tree da applicare ad un altra timeline?

---

## 🤖 Assistant

In **DaVinci Resolve** il *node tree* non si salva come oggetto indipendente “globale”, ma puoi riutilizzarlo in tre modi corretti. Ecco quali, senza giri di parole.

---

## Metodo 1 – **PowerGrade** (consigliato)
È la soluzione giusta se vuoi riapplicare lo stesso grading su altre timeline o progetti.

**Procedura**
1. Vai nella **Color Page**.
2. Seleziona la clip con il node tree corretto.
3. Apri la **Gallery**.
4. Tasto destro sul viewer → **Grab Still**.
5. Trascina lo still nella sezione **PowerGrades** (non nella Gallery del progetto).

**Risultato**
- Il node tree è salvato.
- Lo puoi applicare a qualsiasi clip, timeline o progetto.
- Include nodi, key, mixer, CST, LUT, ecc.

---

## Metodo 2 – **Copy / Paste nodes**
Utile solo se lavori dentro lo stesso progetto.

**Procedura**
1. Seleziona la clip sorgente.
2. `Cmd + C` (Copy Grade).
3. Seleziona la clip di destinazione.
4. `Cmd + V` (Paste Grade).

Oppure:
- Tasto destro sul node graph → **Append Node Graph** / **Apply Grade**.

**Limite**
- Funziona solo nel progetto corrente.
- Nessun archivio riutilizzabile.

---

## Metodo 3 – **Shared Node** (per coerenza su più clip)
Non è un preset, ma è utile se vuoi lo stesso nodo su più clip.

**Procedura**
1. Tasto destro nel node graph → **Add Shared Node**.
2. Collega lo Shared Node dove serve.

**Limite**
- Vale solo all’interno della timeline/progetto.
- Se lo modifichi, cambia su tutte le clip collegate.

---

## Cosa **non** si può fare
- Salvare un node tree come file singolo (.drx) solo per i nodi.
- Esportare un node tree senza passare da Still / PowerGrade.

---

### In sintesi
- **Vuoi riutilizzarlo sempre** → **PowerGrade**
- **Stesso progetto, al volo** → Copy/Paste
- **Coerenza su più clip** → Shared Node

Se vuoi, dimmi **che tipo di node tree** stai salvando (CST, look creativo, gestione log) e ti dico come renderlo più robusto e riutilizzabile senza sorprese.