# RawLine Space: prime prove sul BigDisk

Data: 2026-11-13. Prime prove delle fondamenta di Space (copia verificata, registro, ripresa dopo un'interruzione, riordino, quarantena, ripristino) su un disco vero, il **RAID BigDisk 2025 4TB**. Il disco è APFS, collegato via USB, UUID `7C7D113D-361E-4A68-B909-F387403C8730`.

- **Dove ho scritto:** solo nella cartella `RawLine Space - Prove`, sul BigDisk. Le cartelle 2025, 2026 e Fondazione Montagna Sicura non le ho toccate.
- **G-SPEED:** solo letto, come sorgente della copia e per la verifica.
- **Dati di prova:** il servizio vero *2025/Noli Home - Gillio*, 1.069 file e 18,41 GB:
  - 374 ARW, 374 XMP, 101 DNG;
  - 110 export Alta e 110 export Web.
- **Codice:** sono prototipi scritti per provare il metodo, non il codice dell'app. I sorgenti sono in `research_notes/RawLine Space/Prototipi 13 nov/`.

## Risultati in breve

| Prova | Esito |
|---|---|
| Sonda delle capacità del disco | Tutte le garanzie che servono a Space ci sono |
| Copia verificata dal G-SPEED | 1.069 file su 1.069 verificati, 0 mancanti, 0 in più |
| Verifica indipendente contro il G-SPEED | **Identici**: contenuto, date ed etichette, file per file |
| 8 interruzioni brutali durante la copia, poi ripresa | **Identici**, nessun pezzo a metà rimasto |
| Interruzione nell'attimo dopo la rinomina finale | Trovato un difetto, corretto e riprovato |
| Piano con due file verso lo stesso nome | **Rifiutato** prima di toccare qualunque file |
| Riordino interrotto a metà, poi ripreso | 1.069 file spostati, nessuno saltato |
| Quarantena di 100 RAW con il loro XMP | 200 file spostati, nessuna eliminazione |
| "Ripristina schema precedente" dopo modifiche esterne | Tutti i 1.069 file al loro posto; le modifiche fatte da fuori rispettate |

## 1. Sonda del disco

| Capacità | BigDisk (APFS, USB) | Serve a |
|---|---|---|
| Rinomina che non sovrascrive mai | sì: su un nome occupato rifiuta e il file esistente resta intatto | ogni spostamento |
| Identificativo del file uguale dopo la rinomina | sì | riconoscere i file nel ripristino |
| Cambio di sole maiuscole | sì, in un passo e in due | rinomine |
| Scambio di due file in un passo | sì | sostituzioni sicure |
| Cloni APFS e snapshot | sì | (non usati nella prima versione) |
| Scrittura forzata sul disco (`F_FULLFSYNC`) | sì, circa 0,1 s per file | copia verificata, registro |
| Lettura senza cache (`F_NOCACHE`) | sì | rileggere davvero dal disco |
| Cestino del disco | sì (`.Trashes`) | ripiego |
| Distingue le maiuscole | no | controllo dei conflitti di nome |
| `Città` con l'accento scritto in due forme | è lo stesso file | niente falsi doppioni per gli accenti |

## 2. Copia verificata

Il metodo è quello deciso nella sezione 3.2 del documento principale. Per ogni file:
1. si copia su un nome temporaneo, calcolando l'impronta mentre si legge;
2. si copiano attributi, permessi e date;
3. si forza la scrittura sul disco;
4. si rilegge la copia dal disco senza cache e si confrontano impronta, dimensione, date, permessi, flag e attributi estesi;
5. si dà il nome finale con una rinomina che non sovrascrive mai;
6. ogni passo viene scritto nel registro prima di essere fatto.

Alla fine c'è un controllo di completezza: stesso elenco di file e stessi byte.

**Risultato:** 1.069 file e 18,41 GB verificati. Poi un programma diverso, scritto a parte, ha confrontato la copia con l'originale sul G-SPEED file per file: **identici**.

**Due cose scoperte.**
- **macOS aggiunge da solo un attributo** (`com.apple.provenance`) a ogni file creato da un programma: segna quale app l'ha creato. Al primo tentativo la verifica lo ha visto come una differenza e **non ha dato il nome finale a nessun file**. È il comportamento giusto. L'attributo non è un dato dell'utente, quindi ora è escluso dal confronto. Va scritto nelle regole di Space.
- **Velocità: 27–36 MB/s**, molto sotto quello che il disco può dare. Le cause probabili sono quattro: ogni file viene letto due volte, la scrittura viene forzata file per file, il programma girava a bassa priorità e intanto il G-SPEED era in uso. Va misurata a parte prima di stimare i tempi di Consolida.

## 3. Interruzioni

**Otto interruzioni brutali** (`kill -9`, il programma muore senza poter fare niente) a tempi casuali, ciascuna seguita da una ripresa.
- A ogni ripresa il programma ha trovato il pezzo a metà lasciato dall'interruzione e l'ha tolto. Era un suo file temporaneo: è l'unica cosa che può cancellare da solo.
- Alla fine i 1.069 file sono di nuovo identici all'originale, e non resta nessun temporaneo.

**Il difetto trovato.** Una delle interruzioni è caduta esattamente tra "dai il nome finale" e "scrivi nel registro che è fatto". Alla ripresa c'era un file con il nome finale che il registro non conosceva. Il prototipo non l'ha toccato, ed era giusto. Però il file era buono, ed è rimasto segnato come "non verificato".

**La correzione.** Ora l'impronta verificata si scrive nel registro *prima* di dare il nome finale. Alla ripresa un file con il nome finale si dà per buono solo se la sua impronta è uguale a quella registrata e a quella dell'originale. L'ho provato facendo morire il programma subito dopo la rinomina, in due casi:
- file intatto: alla ripresa è stato riconosciuto e dato per verificato;
- file alterato di un solo byte: alla ripresa **non** è stato dato per buono e non è stato toccato.

## 4. Riordino, quarantena e ripristino

I passi della prova, sempre su una copia:
1. istantanea dello stato di partenza;
2. riordino secondo il modello approvato da Andrea: RAW e XMP in `RAW/`, export in `Export/Alta` ed `Export/Web`;
3. il riordino interrotto di colpo dopo 28 spostamenti e poi ripreso;
4. quarantena di 100 RAW con il loro XMP;
5. tre modifiche fatte "da fuori" nel frattempo:
   - un export nuovo;
   - un XMP modificato sul posto;
   - un XMP risalvato come file nuovo, come fanno alcune app: così cambia l'identificativo del file;
6. "Ripristina schema precedente" verso l'istantanea di partenza;
7. confronto con la copia di riferimento.

**Risultato finale:**
- tutti i 1.069 file sono tornati al loro posto, compresi i 200 della quarantena;
- l'export arrivato dopo è rimasto dov'era: niente di nuovo viene cancellato o spostato;
- i due XMP modificati sono tornati al loro posto, accanto al loro RAW, **con le modifiche intatte**;
- le cartelle rimaste vuote non vengono cancellate, solo elencate;
- il confronto con il riferimento mostra solo le tre differenze introdotte apposta.

**Il caso dell'XMP risalvato.** Al primo giro il ripristino non l'ha riconosciuto: l'identificativo era cambiato. È rimasto in `RAW/`, separato dal suo RAW. Ho aggiunto il secondo livello di riconoscimento, per nome, valido solo quando il nome è unico. Al secondo giro l'XMP è tornato accanto al suo RAW. Nel prodotto questo tipo di riconoscimento va segnato nell'anteprima come "riconosciuto dal nome", da confermare.

## 5. Cosa ne viene per Space

1. **Il metodo regge** su un disco vero e con dati veri: copia verificata, registro scritto prima di agire, ripresa che tocca solo i propri temporanei, rinomine che non sovrascrivono mai.
2. **Due regole nuove** da scrivere nel documento:
   - l'impronta va registrata prima della rinomina finale;
   - `com.apple.provenance` non conta come differenza.
3. **Il riconoscimento a cascata serve davvero:** prima l'identificativo, poi il nome. Lo conferma un caso reale, gli XMP risalvati da altre app.
4. **Ancora da provare:**
   - la velocità vera;
   - un disco staccato fisicamente a metà copia;
   - il disco pieno;
   - exFAT e NAS;
   - la stessa prova su un servizio con video;
   - la prova "andata e ritorno" su più servizi insieme.

## Dati di prova rimasti sul BigDisk

In `RawLine Space - Prove` ci sono tre copie del servizio di prova, circa 17 GB ciascuna: `Noli Home - Gillio` (il riferimento), `Interruzione` e `Riordino`. Si possono togliere quando non servono più.

---

## 6. Disco staccato a metà copia (pomeriggio del 13 nov)

| Prova | Esito |
|---|---|
| Destinazione smontata a forza durante una scrittura | Si ferma subito e registra "pausa: disco scollegato". I 52 file finiti sono identici all'originale. Al riattacco completa la copia: **identici** |
| Sorgente smontata a forza durante una scrittura | Si ferma subito, i 50 file finiti sono buoni. Al riattacco completa: **identici** |
| Ripresa con la sorgente ancora assente | **Difetto trovato e corretto**: la cartella mancante veniva letta come vuota. Ora la copia rifiuta di partire ("un disco assente non è un disco vuoto") |
| **Cavo USB staccato davvero** (alimentazione lasciata accesa) | Si ferma con 81 file verificati. Il file system controllato dopo è integro. Il pezzo a metà l'ha scartato APFS da solo. Al riattacco completa: **identici**. Le cartelle di Andrea (49.344 file) sono uguali a stamattina |
| **Controllo al riattacco**, disco sano | Controlla il file system, rilegge i 23 file già copiati, li trova integri e riprende |
| **Controllo al riattacco**, un byte alterato apposta | Trova il file danneggiato e **non scrive più niente** finché non si decide cosa fare |

Il controllo del file system del BigDisk (in sola lettura) è stato fatto prima e dopo lo stacco del cavo: integro tutte e due le volte. Il G-SPEED non è mai stato coinvolto, se non in lettura.

**Velocità:** dal BigDisk al Mac la copia verificata va a 125 MB/s, verso il BigDisk a 27–40 MB/s. Il collo di bottiglia è la scrittura sul BigDisk, oppure la lettura del G-SPEED mentre Andrea ci lavora. Non è il metodo di verifica.

Dati di prova rimasti sul BigDisk, in `RawLine Space - Prove`: cartelle `Noli Home - Gillio`, `Interruzione`, `Riordino`, `Staccato`, `Cavo`, `Riattacco-*`. In tutto circa 90 GB.

---

## 7. Riparazione in parallelo (pomeriggio del 13 nov)

**La prova.**
- Una copia verificata nuova di *Gillio Export* sul BigDisk: 220 file, 1,85 GB.
- Una seconda copia, lo "Specchio".
- Nella copia, 15 file rovinati apposta in modi diversi:
  - 10 con un solo bit cambiato;
  - 1 con un blocco azzerato a metà;
  - 2 troncati;
  - 2 cancellati.
- Nello Specchio, 5 di quegli stessi file rovinati a loro volta.

| Giro | Altre copie a disposizione | Esito |
|---|---|---|
| 1 | solo lo Specchio | 220 file controllati in 4 s, con 4 letture in parallelo: trovati tutti e 15. **10 riparati** dallo Specchio. I 5 rovinati anche lì sono stati **rifiutati**: la copia c'era, ma l'impronta era sbagliata. Non sono stati toccati |
| 2 | Specchio, poi G-SPEED (solo lettura) | I 5 rimasti riparati dal G-SPEED |
| 3 | controllo di nuovo | 0 file rovinati |

**Verifica indipendente contro il G-SPEED:** i 220 file sono identici per contenuto, date e attributi. In quarantena ci sono i 13 file rovinati, cioè i 15 meno i 2 che erano spariti: nessuno è stato cancellato. Non è rimasto nessun temporaneo. Il G-SPEED è stato solo letto.

Dopo la prova ho tolto tutti i dati di prova: la cartella `RawLine Space - Prove` sul BigDisk è vuota.

---

## 8. Recupero senza un'altra copia (sera del 13 nov)

Andrea ha chiesto se si possono recuperare i file rovinati quando non esiste nessun'altra copia. Ho provato due metodi che non occupano spazio sul disco. Il prototipo è `recupera.swift`.

1. **Letture ripetute.** Se la lettura di un pezzo fallisce, si riprova un settore alla volta (4 KB), fino a 8 volte, con pause crescenti.
   - Se il file torna integro, viene riscritto in un punto nuovo del disco e il vecchio va in quarantena.
2. **Correzione di 1 o 2 bit per MB.**
   - Per ogni file si salva, oltre all'impronta intera, un controllo CRC-64 per ogni MB: 8 byte per MB, lo 0,0008% dei dati. Per i 16,8 TB del G-SPEED sono circa 130 MB, nel database di Space.
   - Se un file risulta rovinato, il controllo indica quale MB lo è e, con un calcolo, quali bit.
   - La correzione si accetta solo se l'impronta SHA-256 dell'intero file torna identica.

**La prova.**
- Una copia verificata nuova di *Gillio Export* sul BigDisk: 220 file, 1,85 GB.
- Dentro, 13 file rovinati apposta in sei modi diversi.
- Più due settori illeggibili **simulati**. Un settore rotto vero non si può creare senza rovinare il disco: il programma faceva finta che quella lettura fallisse.

| Danno | File | Esito |
|---|---|---|
| 1 bit cambiato | 5 | **5 recuperati**, identici all'originale |
| 2 bit nello stesso MB | 3 | **3 recuperati** |
| 1 bit in due MB diversi | 2 | **2 recuperati** |
| 1 bit in un file piccolo (1,5 MB) | 1 | **recuperato** |
| Settore che si legge al 4° tentativo (simulato) | 1 | **recuperato** e riscritto in un punto nuovo |
| 3 bit nello stesso MB | 1 | non recuperabile: il danno è indicato con precisione e il file non è stato toccato |
| 512 byte azzerati | 1 | non recuperabile, come sopra |
| Settore che non si legge mai (simulato) | 1 | non recuperabile: il programma indica il punto (7.172 KB) e lascia il file com'è |

**Verifica indipendente contro il G-SPEED:** i 13 recuperati sono identici all'originale per contenuto e date. Differiscono solo i 2 non recuperabili, di 3 e 510 byte. In quarantena ci sono i 12 file sostituiti (11 corretti e 1 riscritto), nessuno cancellato. Non è rimasto nessun temporaneo.

**Tempi:** il primo calcolo dei controlli ha richiesto 11 s per 1,85 GB. Nel prodotto si calcolano durante la copia, senza una lettura in più. Il controllo con recupero di 220 file ha richiesto 18 s.

**Limiti.** Questi metodi riparano i danni piccoli, il "bit rot", e i settori deboli. Un pezzo grande perso si ripara solo con un'altra copia o con PAR2. Per quei casi restano da progettare il salvataggio dell'anteprima dai RAW e la ricostruzione di export e XMP dal catalogo.

Dati di prova tolti: la cartella `RawLine Space - Prove` è di nuovo vuota.
