---
title: "Aggiornamento mappe Discover Media"
created: 2025-09-19
updated: 2025-09-19
model: gpt-5
messages: 4
source: chatgpt-import
tags: []
---

# Aggiornamento mappe Discover Media

> Importato da ChatGPT export · 4 messaggi · gpt-5 · 2025-09-19

## 🧑 User

C'è un modo per aggiornare autonomamente le mappe del mio navigatore della Volkswagen Golf, quello del......che si chiama......Discover Media MIP1, della mia Golf del 2014, perché adesso iniziano ad essere da aggiornare.

---

## 🤖 Assistant

Sì, si può fare da solo. Il tuo sistema è **Discover Media MIB1** (quello con due slot SD, in uso circa fino al 2015).
Ecco come aggiornare le mappe:

1. **Recupera la scheda SD originale**
- Le mappe sono memorizzate nella SD Volkswagen che si trova nello slot dedicato.
- Non usare una SD qualsiasi: quella originale è associata al tuo sistema.

2. **Vai sul portale ufficiale Volkswagen**
- Collegati a [Volkswagen Map Updates](https://webspecial.volkswagen.de/vwin/en/navigation-discover-media/) (se non funziona la versione italiana, usa quella internazionale).
- Seleziona **Discover Media (Gen1)**.
- Ti proporrà i pacchetti aggiornati.

3. **Scarica l’aggiornamento**
- Il file è grande (10–15 GB).
- Verrà scaricato come archivio ZIP.

4. **Prepara la scheda SD**
- Inserisci la SD originale nel computer.
- Fai un backup sul PC per sicurezza.
- Cancella il contenuto (formattazione in FAT32, non exFAT).

5. **Copia le nuove mappe**
- Estrai i file dall’archivio ZIP scaricato.
- Copiali sulla scheda SD, mantenendo esattamente la struttura delle cartelle.

6. **Reinserisci la SD nel navigatore**
- Riaccendi la Golf, inserisci la scheda nello slot.
- Il sistema riconoscerà automaticamente l’aggiornamento.
- Potrebbe metterci diversi minuti al primo avvio.

⚠️ Nota importante:
- Gli aggiornamenti ufficiali per **MIB1** sono stati interrotti da Volkswagen intorno al 2019/2020.
- Se trovi ancora pacchetti sul sito ufficiale, sono gli ultimi disponibili.
- Per mappe più recenti bisogna rivolgersi a soluzioni non ufficiali (terze parti, non sempre stabili o legali).

Vuoi che ti cerchi se esiste ancora l’ultimo pacchetto ufficiale scaricabile per il tuo Discover Media MIB1 del 2014?

---

## 🧑 User

Allora, sul sito che mi hai mandato non c'è nessun tipo di dettaglio di possibilità di scegliere il navigatore per le mappe né niente, quindi non so se l'hanno tolto, ma boh, è qualche sito di terze parti che magari l'ha conservato in un archivio o qualcosa con i modelli quelli più aggiornati.

---

## 🤖 Assistant

Sì, ma con un limite chiaro: per **Discover Media MIB1** l’ultimo **aggiornamento ufficiale Europa è “Giugno 2020”**. Da allora Volkswagen ha chiuso i download pubblici e spostato tutto dentro **myVolkswagen**; per i sistemi vecchi come MIB1 non compaiono più nuove mappe. Fonte ufficiale: il manuale VW per Discover Media Gen1 indica esplicitamente “Europe map material June 2020 – currently last status”. cite

# Cosa puoi fare adesso
1) **Scaricare e installare l’ultima versione ufficiale disponibile (EU 06/2020)**
- Accedi alla pagina mappe VW che oggi reindirizza a myVolkswagen. Lì vedrai solo quanto ancora supportato, con login e VIN. cite
- Segui la procedura del manuale ufficiale Gen1: usa **la SD originale Volkswagen** del tuo navigatore, fai backup, **formatta FAT32**, estrai lo **.7z** e copia mantenendo la struttura cartelle. Con macOS usa un unzip compatibile (es. Keka) ed elimina i file nascosti prima di rimettere la SD in auto. **Blocca** la levetta della SD su “Lock” prima di inserire in vettura. cite

2) **Se vuoi tentare archivi non ufficiali**
- Esistono siti e forum che raccolgono i pacchetti storici per MIB1, ma **non sono VW** e possono essere incompleti o modificati. Inoltre il Discover Media MIB1 verifica l’**SD originale**: una SD qualunque spesso non viene accettata. Valuta i rischi. Esempio di archivio community: MIB-Helper, puramente informativo. cite

# Note operative importanti
- **Serve la SD originale VW**: senza il suo identificativo la radio può mostrare “Inserire supporto con dati di navigazione validi” anche se i file sono corretti. cite
- **Formato**: FAT32, non exFAT, per Discover Media Gen1. cite
- **macOS**: usa un estrattore compatibile e ripulisci i file nascosti per evitare che il sistema non riconosca le mappe. cite

Se vuoi, ti preparo i passaggi esatti per verificare a bordo la tua versione attuale e una checklist “clic per clic” per aggiornare la SD alla EU 06/2020 secondo il manuale VW.