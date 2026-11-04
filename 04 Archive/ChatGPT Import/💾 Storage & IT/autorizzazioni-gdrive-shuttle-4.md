---
title: "Autorizzazioni GDrive Shuttle 4"
created: 2026-03-29
updated: 2026-03-29
model: gpt-5-3
messages: 4
source: chatgpt-import
tags: [storage-it]
category: "💾 Storage & IT"
---

# Autorizzazioni GDrive Shuttle 4

> Importato da ChatGPT export · 4 messaggi · gpt-5-3 · 2026-03-29

## 🧑 User

Dopo l'installazione del GDrive Shuttle, Gride Shuttle 4, che autorizzazioni va data al sistema per macOS?

---

## 🤖 Assistant

Dopo aver installato il **entity["software","G-RAID Shuttle 4 Utility","G-Technology management software"]** (o **G-Drive / G-RAID software suite**) su macOS, le autorizzazioni da concedere sono poche ma **fondamentali**. Se le sbagli o le neghi, il RAID può funzionare male o non essere gestibile.

Vai dritto a queste:

---

## 🔐 1. Accesso completo al disco (Full Disk Access) — **OBBLIGATORIO**
Percorso:
**Impostazioni di Sistema → Privacy e Sicurezza → Accesso completo al disco**

➡️ Aggiungi:
- G-RAID / G-Drive Utility
- Eventuali processi associati (es. “SanDisk / G-Technology daemon”)

**Perché serve:**
Permette al software di:
- monitorare i dischi
- leggere SMART e stato RAID
- gestire rebuild / configurazioni

👉 Senza questo: il software spesso vede il RAID ma **non può controllarlo davvero**.

---

## ⚙️ 2. Accesso ai file e cartelle (File & Folders) — **Consigliato**
Percorso:
**Privacy e Sicurezza → File e cartelle**

➡️ Concedi accesso almeno a:
- Volumi esterni
- (Opzionale) Documenti / Desktop se lavori direttamente lì

**Perché serve:**
Evita problemi di lettura/scrittura su alcuni workflow (backup, ingest video, ecc.).

---

## 🔔 3. Notifiche — **Consigliato**
➡️ Attiva notifiche per il software

**Perché serve:**
Ti segnala:
- dischi in errore
- degrado RAID
- rebuild in corso

👉 Senza notifiche rischi di accorgerti tardi di problemi seri.

---

## 🧠 4. Elementi in background (Login Items) — **DA LASCIARE ATTIVO**
Percorso:
**Generali → Elementi login → Consenti in background**

➡️ Consenti eventuali servizi G-Technology / SanDisk

**Perché serve:**
Serve per il monitoraggio continuo del RAID.

---

## ❌ Cosa NON serve (in genere)
- Accesso a fotocamera / microfono
- Accessibilità (a meno che non venga richiesto esplicitamente — raro)

---

## ⚠️ Nota importante (macOS recenti)
Su macOS recenti (Ventura, Sonoma, Sequoia):
- Le autorizzazioni possono comparire **solo quando l'app le richiede**
- Se hai cliccato “nega” una volta, devi riattivarle manualmente

---

## 🧩 Check rapido post-installazione
Dopo aver dato i permessi:
1. Apri utility G-RAID
2. Verifica che:
- il RAID sia visibile
- lo stato sia “Healthy”
- puoi accedere alle info dei dischi

Se qualcosa non torna → quasi sempre è un problema di **Full Disk Access non dato correttamente**.

---

Se vuoi, dimmi:
- che configurazione RAID stai usando (RAID 0 / 1 / 5 ecc.)
- e su che Mac / macOS sei

e ti dico anche se la configurazione ha senso per il tuo workflow (soprattutto video/foto).

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Qui non è un problema generico di permessi: **ti manca l’autorizzazione della system extension (DEXT)**, che su macOS è bloccata di default.

Il messaggio è chiaro:
> “Awaiting approval… enable the G-RAID DEXT Driver extension”

---

## 🔧 Cosa devi fare (passaggi precisi)

1. Vai in:
**Impostazioni di Sistema → Privacy e Sicurezza**

2. Scorri in basso fino a **“Sicurezza”**

3. Dovresti vedere un messaggio tipo:
👉 *“Il software di sistema dello sviluppatore ‘SanDisk / G-Technology’ è stato bloccato”*

4. Clicca su **“Consenti”**

5. Inserisci password / Touch ID

6. **Riavvia il Mac** (spesso obbligatorio)

---

## ⚠️ Se NON vedi il pulsante “Consenti”
Succede spesso. Vai così:

### Opzione 1 — rifai partire l’installer
- Chiudi tutto
- Riapri il **G-RAID DEXT Installer**
- Torna subito in Privacy e Sicurezza
👉 Il messaggio compare per pochi minuti

---

### Opzione 2 — Mac Apple Silicon (M1/M2/M3)
Se ancora non compare, può essere bloccato a livello più profondo:

1. Spegni il Mac
2. Tieni premuto il tasto accensione → entra in **Recovery Mode**
3. Vai su:
- Utility → **Startup Security Utility**
4. Imposta:
- **Reduced Security**
- Spunta: *Allow user management of kernel extensions / system extensions*

👉 Poi riavvia e rifai installazione

---

## 🧠 Nota importante (senza giri di parole)
- Senza questa autorizzazione → il RAID **funziona a metà o male**
- Il disco può montare, ma:
- niente monitoraggio
- niente gestione RAID
- rischio di non accorgerti di errori

---

## ✅ Dopo che funziona
Poi torna a fare quello che ti dicevo prima:
- Full Disk Access → ON
- Background items → ON

---

Se vuoi, mandami:
- che RAID stai usando (0 / 1 / 5)
- e che connessione (Thunderbolt / USB)

Perché su questi G-RAID spesso si fanno configurazioni **veloci ma rischiose** per il tuo tipo di lavoro (video/foto), e lì ha senso sistemarlo bene subito.