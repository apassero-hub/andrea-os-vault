---
title: "Problema inoltro Hostinger"
created: 2025-09-02
updated: 2025-09-02
model: gpt-5
messages: 2
source: chatgpt-import
tags: []
---

# Problema inoltro Hostinger

> Importato da ChatGPT export · 2 messaggi · gpt-5 · 2025-09-02

## 🧑 User

Allora, non capisco. Ho l'account quello su Hostinger, quello di InfocacciaAndreaPastorini.com per cui una mail non mi è arrivata rinoltrata su quello di Gmail, non so per quale motivo. Mail non la scarica. Sparita. L'ho ricevuta sul telefono. E la vedo soltanto se entro in Hostinger che chiaramente mi risulta essere l'unica mail in arrivo. Che cazzo è successo?

---

## 🤖 Assistant

Ti spiego senza giri di parole cosa può essere successo:

1. **Non è sparita, è rimasta su Hostinger.**
Se la vedi solo lì significa che il **forward verso Gmail non ha funzionato**. Quindi Gmail non l’ha mai ricevuta → normale che non la trovi.

2. **Cause probabili:**
- **Problema di inoltro lato Hostinger**: la regola di forward può essere rotta o temporaneamente non funzionante.
- **Spam/filtri Gmail**: a volte Gmail scarta senza nemmeno notificare, soprattutto se l’IP di Hostinger finisce in blacklist. Controlla in *Spam* e *Tutti i messaggi*.
- **Regola di forward errata**: se hai più alias o più regole di inoltro, può darsi che una sia impostata male.
- **Mailbox piena o sincronizzazione errata**: se la casella Hostinger ha dei limiti, può comportarsi in modo strano.

3. **Perché la vedi sul telefono e non su Gmail?**
Sul telefono probabilmente hai configurato **IMAP/POP direttamente con l’account Hostinger**, quindi lì scarica tutto alla fonte. Gmail invece dipende solo dall’inoltro, che stavolta non è avvenuto.

---

👉 Cosa fare adesso:
- Vai su **Hostinger → Email → Forwarding** e controlla se l’inoltro verso Gmail è ancora attivo.
- Verifica se Gmail l’ha bloccata (Spam / Tutti i messaggi / Filtri).
- Fatti mandare un’altra mail di prova allo stesso indirizzo e vedi se arriva su Gmail. Se non arriva, è un problema lato Hostinger.

Vuoi che ti faccia uno **step-by-step** per configurare l’account Hostinger direttamente su Gmail con **POP3/IMAP** così Gmail scarica le mail alla fonte e non dipendi più dal forward?