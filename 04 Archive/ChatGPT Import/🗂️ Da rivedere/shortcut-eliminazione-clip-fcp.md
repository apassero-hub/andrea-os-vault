---
title: "Shortcut eliminazione clip FCP"
created: 2025-12-07
updated: 2025-12-07
model: gpt-5-1
messages: 2
source: chatgpt-import
tags: [da-rivedere]
category: "🗂️ Da rivedere"
---

# Shortcut eliminazione clip FCP

> Importato da ChatGPT export · 2 messaggi · gpt-5-1 · 2025-12-07

## 🧑 User

qual è lo shortcut su final cut per eliminare la clip in riproduzione senza doverla selezionare? tipo il ripple delete ma che cancella tutta la clip

---

## 🤖 Assistant

In Final Cut Pro **non esiste uno shortcut nativo che elimini direttamente la clip sotto il playhead senza selezionarla**. La funzione "ripple delete della clip in riproduzione" non è prevista come comando predefinito.

La soluzione operativa è questa:

1. **Seleziona Clip sotto il Playhead**
Comando: **Select Clip**
Shortcut: `C`
Questo seleziona immediatamente la clip che sta toccando il playhead.

2. **Elimina con riduzione (Ripple Delete)**
Shortcut: **Delete**
Se la clip è una primaria storyline, il delete fa automaticamente il ripple.

Se vuoi ottenere un vero "delete without selecting", devi creare una **scorciatoia personalizzata**:

### Come creare lo shortcut personalizzato
1. Vai su **Final Cut Pro > Commands > Customize…**
2. Cerca il comando **Select Clip**.
3. Cerca il comando **Delete**.
4. Assegna a entrambi una singola combinazione tramite **Command Grouping** (macros interne di FCP).
Questo ti permette di premere un unico tasto per:
- selezionare automaticamente la clip sotto il playhead
- eliminarla subito dopo

È la soluzione usata da molti montatori perché FCP, a differenza di Premiere o Avid, non ha un "Ripple Delete at Playhead".

### Nota importante
Se la clip non tocca esattamente il playhead (anche di 1 frame), il comando non la selezionerà. Conviene abilitare lo **snapping (N)** per essere sempre perfettamente a contatto.

Se vuoi, ti preparo uno schema di tasti consigliato per ottenere una workflow rapido tipo “blade + delete” in stile Premiere.