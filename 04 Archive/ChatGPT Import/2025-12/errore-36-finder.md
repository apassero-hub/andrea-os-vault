---
title: "Errore 36 Finder"
created: 2025-12-11
updated: 2025-12-11
model: gpt-5-1
messages: 2
source: chatgpt-import
tags: []
---

# Errore 36 Finder

> Importato da ChatGPT export · 2 messaggi · gpt-5-1 · 2025-12-11

## 🧑 User

finder non può copiare i dati errrore 36

---

## 🤖 Assistant

Errore 36 in macOS è un classico problema di **I/O** legato al file system. Significa che Finder non riesce a leggere o scrivere correttamente un file. Le cause tipiche sono:

- File corrotto.
- Problemi nel supporto di archiviazione (HDD/SSD/SD).
- Percorsi con caratteri anomali.
- Permessi o metadata danneggiati.

Procedi così, in ordine secco:

---

## 1. **Usa il comando dot_clean sulla cartella**
Rimuove i metadata corrotti che generano spesso l’errore.

Apri Terminale e incolla:

```
dot_clean /percorso/della/cartella
```

Esempio veloce: trascina la cartella nel Terminale dopo `dot_clean ` e premi Invio.

Poi riprova la copia.

---

## 2. **Prova a copiare tramite Terminale**
Finder a volte fallisce, `cp` invece no.

```
cp -R /sorgente/ /destinazione/
```

Oppure prova con `rsync` (più tollerante):

```
rsync -avh /sorgente/ /destinazione/
```

Se rsync va, è quasi sicuramente un problema di metadata.

---

## 3. **Controlla il disco di destinazione e di origine**
Da Utility Disco → seleziona il supporto → **S.O.S.**.

Se trovi errori, sistemali prima di riprovare.

---

## 4. **Controlla file specifici corrotti**
Se l’errore si verifica sempre allo stesso punto, uno dei file coinvolti è corrotto.

Puoi individuare il file così:

```
cp -Rv /sorgente/ /destinazione/
```

Ti mostrerà su quale file si interrompe.

---

## 5. **Se copi su un SSD/HDD esterno in exFAT**
È uno dei file system più inclini a dare errore 36.
Soluzione: fai un backup e riformatta in **APFS** o **HFS+**.

---

## 6. **Se stai copiando file da una SD o CFExpress**
Errore 36 può segnalare blocchi danneggiati sulla scheda → copia con `rsync`, poi fai un controllo completo o sostituiscila se continua.

---

## Se mi dici da dove a dove stai copiando (tipo: disco esterno → interno, tipo di file system, cartella specifica) ti guido preciso sul caso.