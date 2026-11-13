# Controllo RAID BigDisk 2025 4TB contro G-SPEED

Data: 2026-11-13. Ho controllato se tutto quello che c'è sul **RAID BigDisk 2025 4TB** si trova anche sul **G-SPEED Shuttle XL TB3**. I due dischi li ho solo letti: non ho scritto, spostato o rinominato niente su nessuno dei due. Gli elenchi e i programmi di confronto stanno nella cartella di lavoro della sessione, sul Mac.

## Risultato: sul G-SPEED non manca niente

Il BigDisk ha 49.440 file, per 1,36 TB, in tre cartelle:

| Cartella | GB |
|---|---|
| 2025 | 859,8 |
| Fondazione Montagna Sicura | 355,0 |
| 2026 | 143,6 |

Ho confrontato ogni file per nome e dimensione, ignorando i file di sistema di macOS (`.DS_Store`, `._*`, `.fseventsd`, `.Spotlight-V100`).

| Esito | File | GB |
|---|---|---|
| Sul G-SPEED, stessi nome e dimensione | 48.967 | 1.353,2 |
| Sul G-SPEED, stessi nome e dimensione ma in un'altra sottocartella | 302 | 5,1 |
| Sul G-SPEED con lo stesso nome ma una dimensione diversa | 30 | 0,03 |
| **Non presenti sul G-SPEED** | **0** | **0** |

### Le differenze, una per una

- **Fondazione Montagna Sicura** sul BigDisk sta nella cartella principale del disco. Sul G-SPEED sta dentro `2025/`. Il contenuto all'interno è identico.
- **The Pill - Test Negozianti Pila 26**: 302 export che sul BigDisk sono in `Export/`. Sul G-SPEED sono in `Export_Andrea Passerini_PilaBaseCamp2026/`.
- **La Thuile Trail 2025**: 28 XMP e 2 JPEG export hanno una dimensione diversa. **In tutti e 30 i casi la versione sul G-SPEED è più recente.** Sul BigDisk sono del 30 luglio 2025, sul G-SPEED tra luglio e ottobre 2026. Sono rielaborazioni fatte dopo, quindi la versione buona è quella del G-SPEED, e sul BigDisk ci sono le vecchie.

## Controllo del contenuto byte per byte

Ho letto per intero da tutti e due i dischi **2.831 file, circa 80 GB per disco**. Il campione comprende un file da ognuna delle 2.793 cartelle del BigDisk, più file presi a caso. Per ogni coppia ho calcolato l'impronta (BLAKE2b) e le ho confrontate.

- **2.587 file nello stesso percorso: tutti identici.**
- **244 file di Fondazione Montagna Sicura e di Pila**, confrontati con il loro percorso sul G-SPEED: **tutti identici.**
- **Nessuna differenza** e nessun errore di lettura. Velocità misurata: circa 115 MB/s, in bassa priorità.

Il campione copre ogni cartella, ma non è il 100% dei byte. Il confronto completo richiederebbe di leggere 1,36 TB da ciascun disco: alla velocità misurata sono circa tre ore e mezza, anche sul G-SPEED.

## Una cosa da sapere prima di usare il BigDisk per le prove

Il BigDisk è oggi **l'unica seconda copia** di questi 1,36 TB di lavori 2025 e 2026. Il G-SPEED non ha altri backup. Se il BigDisk viene usato per le prove e i dati vengono spostati o cancellati, quei lavori tornano a vivere su un solo disco.

Le strade possibili:
1. **Prove solo nello spazio libero.** Sul disco ci sono 2,6 TB liberi. Le prove si fanno dentro una cartella nuova, per esempio `RawLine Space - Prove`, usando copie dei dati veri, e le cartelle esistenti non si toccano. La seconda copia resta intatta.
2. **Prove anche sulle cartelle esistenti**, solo dopo che di quei 1,36 TB esiste un'altra copia verificata su un terzo disco.
3. **Uso libero del disco intero**, accettando che 2025 e 2026 restino senza seconda copia finché non ne viene fatta una nuova.

La strada che consiglio è la 1: le prove di Space hanno bisogno di spazio e di dati veri da copiare, non di rinunciare a una copia esistente.
