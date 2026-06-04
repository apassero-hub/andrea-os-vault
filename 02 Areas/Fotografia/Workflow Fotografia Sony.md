---
title: "Workflow Fotografia Sony"
area: Fotografia
status: active
updated: 2026-06-04
tags: [workflow, sony, fotografia, lightroom, photomechanic, gear]
---

# Workflow Fotografia Sony

> Nota permanente · Area: Fotografia  
> Aggiornata: 2026-06-04

Documenta il workflow end-to-end per shooting commerciali, editoriali e sportivi con sistema Sony.

---

## 📷 Gear attuale

### Corpi
- **Sony Alpha 1** (1a gen) × 2 — corpi principali
- Sony Alpha 9 Mark II — in dismissione/vendita

### Obiettivi
| Focale | Ottica | Ruolo |
|---|---|---|
| 70–200mm f/2.8 | Sony FE 70-200 GM OSS II | Tele principale |
| 24–70mm f/2.8 | Sony FE 24-70 GM II | Standard polivalente |
| 16–35mm f/2.8 | Sony FE 16-35 GM II | Grandangolo |
| 16mm fisheye | Sony 16mm (1a gen, adattato) | Creativo/speciale |

**In programma:** lenti fisse (focale e modelli da definire)

---

## 💾 Schede e ridondanza in-camera

- **Tipo schede:** SD V90 (standard) · CFexpress Type B (lavori high-end)
- **Regola sempre attiva:** doppia scheda in-camera — ogni scatto va su entrambi gli slot in simultanea
- **Le schede non si formattano mai** fino a conferma di ≥ 2 copie fisiche sicure

---

## 🔄 Workflow di ingest

### Sul campo — durante lo shooting
- Doppia scheda attiva per tutta la durata
- Se le schede si riempiono → si cambiano **entrambe** contemporaneamente
- Le schede restano intatte e non si toccano fino a fine lavoro

### Fine shooting — download con Photo Mechanic
1. Doppia copia su **2 SSD esterni separati**
2. Durante il download: incorporo metadata con IPTC stationery pad
   - Dati personali/professionali (copyright, contatti)
   - Dati shooting: cliente, location, data

**Naming convention:**
```
AndreaPasserini_Cliente_Location_Data_NomeFileOriginale
```
Esempi:
```
AndreaPasserini_Grivel_Cervinia_20240315_A1_001234.ARW
AndreaPasserini_Ducati_Vallelunga_20240601_A1_005678.ARW
```

### A casa — storage definitivo
1. Copia su **G-Technology G-RAID Shuttle XL** (8 baie · 48 TB lordi · ~42 TB usabili in RAID 5)
2. Schede mantenute intatte fino a conferma copia su Shuttle XL
3. Solo a questo punto le schede possono essere formattate
4. **Fine anno:** i file dell'anno vengono archiviati su **HD esterno dedicato** → conservato come backup offsite aggiuntivo

---

## 🎯 Selezione

La selezione è la fase più critica (e più noiosa) dell'intero workflow.  
Fatta "a caldo" — stesso giorno del rientro — produce risultati migliori: occhio fresco, contesto ancora vivo.

### Quando seleziono io
1. Selezione completa in **Photo Mechanic** (flag/rating)
2. Solo i selezionati vengono importati in **Lightroom**

### Quando seleziona il cliente
1. Carico la galleria su **PickDrop** o **Pixieset**
2. Il cliente naviga la gallery e mette like alle foto preferite
3. Dal backend: filtro per like → **esporto la lista dei nomi file** selezionati
4. In Lightroom → Library → `⌘F` → ricerca per **Nome file** → incollo la lista
5. Lightroom filtra automaticamente e mostra solo le immagini selezionate dal cliente
6. Da lì: import/editing solo di quelle

> Nota: questo step avviene direttamente in Lightroom, non in Photo Mechanic (da verificare se PM supporta ricerca analoga).

> ⚠️ **Pain point principale:** fare la selezione in giornata è ideale ma spesso non fattibile. Da trovare un sistema per ridurre l'attrito.

---

## ✏️ Editing in Lightroom

1. **Prima:** rating/flag sull'intera selezione importata — noioso ma necessario
2. Edit di riferimento su **2–3 foto chiave** (rappresentative della luce e del mood)
3. **Batch apply** dell'edit sul resto del set
4. I **preset personali** funzionano da scaffolding iniziale — vanno sempre riadattati alle luci specifiche di ogni lavoro

> I preset non sono mai la versione finale: sono un punto di partenza da modellare.

---

## 🖥 Finishing in Photoshop

Passaggio finale per:
- Rimozione distrazioni ed elementi indesiderati
- Pulizia di dettagli di precisione
- Ritocchi che Lightroom non gestisce altrettanto bene
- Uso attivo degli strumenti **AI di Photoshop** (Remove Tool, Generative Fill)

---

## 📤 Export e formati di consegna

| Tipo lavoro | File | Lato lungo | DPI |
|---|---|---|---|
| Standard — alta qualità | JPEG | Massima risoluzione | 300 |
| Standard — web/social | JPEG | 2.000 px | 96 |
| Sportivo — alta qualità | JPEG | 4.000 px | 300 |
| Sportivo — web/social | JPEG | 2.000 px | 96 |
| Advertising | JPEG | Massima risoluzione | 300 |
| Stampa | TIFF | A specifica cliente | 300+ |

> La versione 96 DPI / 2.000 px è esclusivamente per uso digitale e social — mai per stampa.

---

## 🔧 Software e storage stack

| Tool | Ruolo nel workflow |
|---|---|
| **Photo Mechanic** | Ingest, metadata IPTC, naming, selezione propria |
| **Lightroom** | Import selezione, editing, ricerca file per nome |
| **Photoshop** | Finishing, ritocchi AI, pulizia di dettaglio |
| **PickDrop / Pixieset** | Gallery cliente, selezione remota con like |
| **G-RAID Shuttle XL** | Storage primario (8 baie, ~42 TB RAID 5) |
| **2× SSD esterni** | Buffer sul campo / doppia copia ingest |
| **HD esterno annuale** | Archivio offsite fine anno |

---

## ⚠️ Note operative

- Non formattare mai le schede prima di avere: 2 SSD esterni + G-RAID Shuttle confermati
- La selezione a caldo (stesso giorno) è la pratica migliore — da proteggere nel planning post-shooting
- I preset sono punti di partenza, non risultati: ogni lavoro ha le sue luci

---

## 📌 Cose aperte

- [ ] Prossima lente fissa: definire focale e modello
- [ ] Verificare se Photo Mechanic supporta ricerca/filtro per lista nomi file (analogo a ⌘F Lightroom)
- [ ] Definire workflow preciso per consegne TIFF (specifica con cliente)
- [ ] Trovare sistema per rendere la selezione a caldo più sostenibile

---

## 🔗 Conversazioni archivio correlate

> Da popolare — cerca in `04 Archive/ChatGPT Import/` per: `sony`, `lightroom`, `selezione`, `preset`, `workflow`, `photomechanic`, `export`, `shuttle`
