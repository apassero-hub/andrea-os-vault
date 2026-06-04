---
title: "Trasferimento dati veloce Mac"
created: 2025-11-16
updated: 2025-11-16
model: gpt-5-1
messages: 2
source: chatgpt-import
tags: []
---

# Trasferimento dati veloce Mac

> Importato da ChatGPT export · 2 messaggi · gpt-5-1 · 2025-11-16

## 🧑 User

Qual é il modo con massima velocità per trasferire dati da un mac all'altro?

---

## 🤖 Assistant

La via più veloce in assoluto, ad oggi, è questa:

**1. Thunderbolt 3/4 + Modalità Disco di Destinazione (Target Disk Mode / ShareDisk)**
È il metodo più rapido perché sfrutta la velocità nativa Thunderbolt (fino a 40 Gbps reali).
Su Apple Silicon la “Target Disk Mode” classica non esiste, ma c’è **Share Disk** da Recovery.

**Procedura (Apple Silicon → Apple Silicon):**
1. Spegni il Mac **destinazione**.
2. Accendilo tenendo premuto il tasto di accensione fino a vedere **Opzioni**.
3. Vai su **Opzioni → Utility → Condividi disco (Share Disk)**.
4. Collega i due Mac tramite **cavo Thunderbolt 3/4**.
5. Il disco del Mac in modalità Share Disk appare sull’altro come un normale volume esterno.
6. Trasferisci i dati via Finder.

**Velocità reali:** 2.200–2.800 MB/s, a seconda del disco interno di ciascun Mac.

---

**2. Thunderbolt direct + Assistente Migrazione**
Stesso principio, ma passa da Assistente Migrazione.
Un po’ più lento per overhead, ma comunque velocissimo.

---

**3. Disco esterno NVMe USB-C 3.2 gen 2x2 (se non hai Thunderbolt su entrambi)**
Raggiungi 1.500–2.000 MB/s reali.
Molto veloce, ma comunque sotto Thunderbolt.

---

**4. Rete 10GbE tra i due Mac**
Se hai adattatori 10 GbE: 800–1.200 MB/s.
Buona, ma Thunderbolt resta superiore.

---

**5. Wi-Fi o rete standard**
Da evitare se cerchi prestazioni.
Wi-Fi 6 → 70–120 MB/s reali.
Wi-Fi 5 → 40–60 MB/s.

---

### Conclusione netta
**Thunderbolt + Share Disk (o Target Disk Mode) è il metodo più rapido in assoluto.**
Se vuoi, ti preparo la procedura precisa per i tuoi due modelli specifici (M3 Pro con schermo rotto incluso).