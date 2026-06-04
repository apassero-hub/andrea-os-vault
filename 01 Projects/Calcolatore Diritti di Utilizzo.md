---
title: "Calcolatore Diritti di Utilizzo"
area: Projects
status: in-progress
updated: 2026-06-04
tags: [progetto, diritti-utilizzo, licensing, fotografia, italia, web-tool]
---

# Calcolatore Diritti di Utilizzo

> Nota di progetto · `01 Projects/`  
> Aggiornata: 2026-06-04

Piattaforma web per aiutare fotografi italiani a calcolare in modo oggettivo le tariffe di utilizzo delle immagini. Uso personale + potenziale prodotto pubblico.

---

## 🎯 Obiettivo e missione

**Problema da risolvere — doppio livello:**

1. **Pratico (personale):** avere un punto di riferimento oggettivo quando costruisco un preventivo per lavori con diritti di utilizzo, invece di andare sempre a naso o chiedere in giro.

2. **Culturale (mercato IT):** i fotografi italiani spesso non distinguono la *shooting fee* dalla *licensing fee* — o non sanno valorizzare quest'ultima. Il calcolatore vuole anche educare su questa differenza.

**Posizionamento rispetto al TAU Visual:**  
I listini TAU Visual esistono ma sono percepiti come troppo alti per il mercato italiano reale. Il calcolatore punta a valori più aderenti alla realtà del mercato, non al massimo teorico.

---

## 📐 Metodologia

### Modello: tariffa giornaliera × moltiplicatori

L'ancora del calcolo è la **tariffa giornaliera base** del fotografo (quella che si usa anche per preventivare lo shooting). Da lì, i diritti di utilizzo si calcolano applicando moltiplicatori per ogni variabile rilevante.

```
Tariffa licensing = Tariffa giornaliera base × M(utilizzo) × M(durata) × M(territorio) × M(esclusività) × M(cliente) × M(genere)
```

### Moltiplicatori

#### Tipo di utilizzo
| Tipo | Moltiplicatore |
|---|---|
| Editoriale (stampa, online non commercial) | basso |
| Social media organico | basso-medio |
| Corporate (interno, presentazioni) | medio |
| Web / digitale commerciale | medio |
| Advertising (campagne) | alto |
| OOH (affissioni, outdoor) | alto |

#### Durata
| Durata | Moltiplicatore |
|---|---|
| 1 mese | base |
| 3 mesi | × |
| 6 mesi | × |
| 1 anno | × |
| Perpetuo / buyout | × (massimo) |

#### Territorio
| Territorio | Moltiplicatore |
|---|---|
| Locale / regionale | base |
| Nazionale | × |
| Europeo | × |
| Internazionale / worldwide | × (massimo) |

#### Esclusività
| Tipo | Moltiplicatore |
|---|---|
| Non esclusivo | 1× |
| Esclusivo di categoria | ~1.5× |
| Esclusivo totale | ~2–3× |

#### Tipo cliente
| Cliente | Moltiplicatore |
|---|---|
| Freelance / persona fisica | base |
| Startup / micro-impresa | base-medio |
| PMI | medio |
| Grande azienda | alto |
| Enterprise / multinazionale | massimo |

#### Genere fotografico
| Genere | Note |
|---|---|
| Lifestyle / reportage | — |
| Prodotto / still life | — |
| Food | — |
| Sport / action | — |
| Moda / fashion | — |
| Architettura / interni | — |

> ⚠️ I valori specifici dei moltiplicatori sono da definire/validare — vedi sezione "Cose aperte"

### Output: range invece di numero fisso

Il calcolatore non restituisce un numero secco ma una **forbice ±15% intorno alla mediana**.  
Esempio: "Per questo brief, la tariffa di riferimento è €800–€1.080"

**Perché:** un numero solo crea un'âncora rigida. Un range comunica che c'è spazio di trattativa pur mantenendo un riferimento oggettivo. Riflette meglio la realtà del mercato italiano.

---

## 🖥 Prodotto — MVP e roadmap

### MVP (versione minima pubblica)
- Calcolatore web con parametri base (tipo utilizzo, durata, territorio, esclusività)
- Input: tariffa giornaliera + parametri
- Output: range ±15%
- Design pulito, orientato ai fotografi italiani
- Gratuito per l'uso base

### Tier Pro (fase successiva)
- Parametri avanzati (cliente, genere, combinazioni complesse)
- Export PDF del report (da allegare al preventivo)
- Storico dei calcoli fatti
- Modello di business: abbonamento mensile/annuale

### Canale / distribuzione
- Piattaforma web standalone
- Target primario: fotografi professionisti italiani
- Possibile community/newsletter associata (da valutare)

---

## ✅ Decisioni già prese

- Modello tariffa giornaliera × moltiplicatori (non lookup table fissa)
- Output come range ±15%, non numero singolo
- Calibrato sotto TAU Visual (realismo mercato IT > massimo teorico)
- Separazione shooting fee / licensing fee come concetto centrale
- MVP gratuito + Pro a pagamento per PDF e funzioni avanzate
- Mercato italiano come focus iniziale

---

## 📌 Cose aperte / da decidire

- [ ] Nome del prodotto/piattaforma
- [ ] Valori precisi dei moltiplicatori per ogni variabile (da testare e validare)
- [ ] Tariffa giornaliera base: range consigliato per il mercato IT (da usare come default per chi non sa da dove partire)
- [ ] Stack tecnico: come è costruito / sarà costruito il frontend
- [ ] Come gestire combinazioni insolite (es. buyout + internazionale + esclusivo totale)
- [ ] Strategia di lancio e acquisizione utenti
- [ ] Se e come integrare un componente educativo (spiegazione dei concetti, non solo calcolo)

---

## 🔗 Note correlate

- [[Business Photography — Preventivi e Commerciale]] — contesto d'uso del calcolatore
- [[Workflow Fotografia Sony]] — il workflow operativo a monte
- Archivio ChatGPT: cerca `calcolatore`, `tariffe`, `licensing`, `diritti utilizzo`, `TAU Visual`, `moltiplicatori`

