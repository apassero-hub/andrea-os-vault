---
title: "Eliminare backup Time Machine"
created: 2026-01-07
updated: 2026-01-07
model: gpt-5-2
messages: 2
source: chatgpt-import
tags: [storage-it]
category: "💾 Storage & IT"
---

# Eliminare backup Time Machine

> Importato da ChatGPT export · 2 messaggi · gpt-5-2 · 2026-01-07

## 🧑 User

come si eliminano manualmente i vecchi backup di time machine?

---

## 🤖 Assistant

Per eliminare **manualmente** i vecchi backup di **Time Machine** ci sono tre casi distinti. Vai dritto a quello che ti serve.

---

## 1. Eliminare singoli backup da **Time Machine (metodo corretto e sicuro)**

image_group{"query":["macOS Time Machine delete backup","Time Machine interface delete backup","Time Machine backup timeline"]}

1. Apri **Time Machine**.
2. Entra nella timeline dei backup.
3. Naviga fino alla data del backup da rimuovere.
4. Clicca sull’icona **⚙︎** (o tasto destro).
5. Seleziona **“Elimina backup”**.
6. Inserisci la password di amministratore.

**Nota:** è l’unico metodo 100% supportato da Apple per cancellazioni selettive.

---

## 2. Eliminare backup da **Terminale** (consigliato se sai cosa stai facendo)

image_group{"query":["macOS Terminal tmutil","tmutil listbackups","tmutil delete backup"]}

### Elenco dei backup
```bash
tmutil listbackups
```

Otterrai percorsi simili a:
```
/Volumes/TimeMachine/Backups.backupdb/MacBook/2024-11-02-120015
```

### Eliminazione di un backup specifico
```bash
sudo tmutil delete /percorso/completo/del/backup
```

Inserisci la password admin.

**Vantaggi**
- Preciso
- Funziona anche quando l’interfaccia grafica fallisce

**Rischi**
- Se sbagli percorso, fai danni
- Non interrompere il processo

---

## 3. Eliminare **interi backup o dischi** dal Finder (sconsigliato)

image_group{"query":["Time Machine Backups.backupdb Finder","macOS Time Machine backup disk Finder","Time Machine sparsebundle"]}

Possibile **solo** se:
- Il disco è **HFS+** (vecchi backup)
- Oppure è un **.sparsebundle** su NAS

### Procedura
1. Monta il disco Time Machine.
2. Vai in:
```
Backups.backupdb
```
3. Cancella **l’intera cartella del Mac** o il file `.sparsebundle`.

**Attenzione**
- Rischio alto di corrompere l’archivio
- Mai cancellare singoli snapshot dal Finder

---

## Caso speciale: backup su **APFS**

Se il disco Time Machine è **APFS**:
- I backup sono snapshot
- **Non vanno mai eliminati dal Finder**
- Usa **Time Machine** o **tmutil**

---

## Pulizia automatica che spesso basta

Se il disco è pieno:
- Time Machine elimina automaticamente i backup più vecchi
- Se non lo fa, spesso il problema è:
- permessi
- disco montato in sola lettura
- errori di filesystem

---

## Consiglio pratico

Se vuoi **liberare spazio subito** senza rischi:
- usa **tmutil**
- elimina i backup più vecchi
- verifica con:
```bash
tmutil listbackups
df -h
```

Se vuoi, dimmi:
- macOS
- tipo di disco (USB, NAS, APFS/HFS+)
- errore specifico (se presente)

e ti do il comando esatto senza giri inutili.