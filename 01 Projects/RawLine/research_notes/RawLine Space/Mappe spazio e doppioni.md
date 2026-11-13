# Mappe dello spazio e cercatori di doppioni

Ricerca di prodotto per **RawLine Space** (riordino, catalogo e alleggerimento di archivi fotografici da 40–100 TB, 100% offline). Data: 11 novembre 2026.

Come leggere le note:
- **[V]** verificato su fonte ufficiale (sito, manuale, note di rilascio, App Store).
- **[R]** riportato da recensioni o fonti di terze parti.
- **[D]** dedotto da me, da verificare provando l'app.

Nessuna di queste app è stata provata a mano: tutto viene da documentazione e recensioni.

---

## Parte 1: mappe dello spazio occupato

### DaisyDisk

**Cos'è.** È l'analizzatore di spazio commerciale più noto su Mac: mostra il disco come anelli concentrici colorati.

**Funzioni.**
- Mappa ad anelli (sunburst) di cartelle e file: si "scende" negli anelli cliccando. [V]
- Scansione come amministratore, per vedere le cartelle protette. [V]
- Scompone le voci "Altro" e "Dati di sistema" di macOS e mostra le istantanee eliminabili (purgeable) di Time Machine. [V]
- Scansione in parallelo di più dischi. Riconosce da solo i dischi rotanti e mette in coda le scansioni dello stesso HDD, per non far saltare la testina; sugli SSD le lascia sempre in parallelo. [V]
- Dischi supportati: interni, esterni, USB, Thunderbolt, di rete e virtuali, più Dropbox, Google Drive, OneDrive e Box. [V]

**Interfaccia.** Anelli più una barra laterale con l'elenco ordinato per dimensione e l'anteprima dei file. [V]

**Eliminazione e sicurezza.**
- Si trascina un elemento nel **Collector** in fondo alla finestra (oppure ⌘⌫ o menu contestuale). È solo una "zona di parcheggio": finché non si preme Elimina, nessun file viene toccato. [V]
- Il Collector si apre come una lista: da lì si vede l'anteprima e si toglie un elemento con ×. [V]
- Rifiuta i percorsi protetti (`/System`, `/Library`, la cartella Inizio). [V]
- Premuto Elimina, parte un **conto alla rovescia di 5 secondi** con il tasto Annulla. [V]
- L'eliminazione è **definitiva, senza passare dal Cestino**, così lo spazio si libera subito. Dentro DaisyDisk non si può recuperare niente. [V]
- Avvisa che, se un'istantanea di Time Machine contiene il file, lo spazio non torna libero ma diventa eliminabile. [V]

**Velocità.** Il sito dichiara scansioni "in secondi", circa 15 s contro i minuti del Finder, ma su un disco di uso comune. [V] Non ho trovato dati su volumi da decine di TB, né su una cache delle scansioni. [D]

**Prezzo.** Licenza a vita da 9,99 $, fino a 5 Mac personali, senza abbonamento. Richiede macOS 10.13 o successivo, Apple Silicon e Intel. [V]

**Limiti.**
- Navigazione solo per cartelle: non raggruppa per anno, cliente o tipo di file. [D]
- L'eliminazione definitiva è pericolosa su un archivio di lavoro. [V/D]
- Niente doppioni. [V]

### GrandPerspective

**Cos'è.** Mappa ad albero (treemap), open source (GPL), mantenuta da molti anni. Ultima versione 3.8.1 del 13 settembre 2026; richiede macOS 14. [V]

**Funzioni.**
- Ogni file è un rettangolo con area proporzionale alla dimensione; i file della stessa cartella stanno vicini. [V]
- Colori per nome, estensione, tipo di file, cartella, livello, dimensione o data, con più tavolozze. [V]
- **Filtri avanzati** per nome, percorso, dimensione, tipo, hard link e pacchetti. Possono nascondere elementi nella vista, toglierli dalla vista o escluderli già in scansione, e restano salvati nelle preferenze. [V]
- **Salvataggio delle scansioni**, da ricaricare quando si vuole, e nuova scansione per confrontare prima e dopo la pulizia. [V]
- Quick Look, Mostra nel Finder, navigazione da tastiera. [V]

**Sicurezza.**
- Nelle preferenze si sceglie se l'eliminazione è disattivata, ammessa solo per singoli file o ammessa anche per le cartelle, e se chiedere conferma. [V]
- Le cartelle vanno nel Cestino, compresi i file **non visibili nella vista filtrata** (lo dice il manuale stesso). [V]

**Velocità.**
- Dalla 3.4 la scansione è stata riscritta e può essere fino a 2 volte più veloce. [V]
- Le cartelle sincronizzate col cloud sono un problema noto: in un caso l'app ha tentato di scaricare quasi 1 TB di Google Drive non presente in locale. [R]

**Prezzo.** Gratis su SourceForge, 2,99 $ sul Mac App Store; è la stessa app. [V]

**Limiti.**
- La treemap è poco leggibile su milioni di file piccoli: ci vuole il colore o il filtro per farla parlare. [D]
- Niente raggruppamenti logici come cliente o anno di scatto. [D]

### Disk Inventory X

**Cos'è.** Treemap gratuita (GPL), con l'algoritmo di disposizione preso da KDirStat. [V]

**Funzioni.** Treemap più un elenco per tipo di file, lo stile di KDirStat e WinDirStat. [R/D: il sito non lo descrive]

**Stato.** Ultima versione 1.3, indicata per macOS 10.13–10.15. Il sito non nomina Apple Silicon. [V] Di fatto è abbandonata. [D]

**Prezzo.** Gratis. [V]

**Limiti.** Non aggiornata e incerta sui macOS recenti. Serve solo come riferimento storico per l'idea "treemap più statistiche per tipo di file". [D]

### OmniDiskSweeper

**Cos'è.** Utility gratuita (non open source) di Omni Group: un elenco a colonne in stile Finder, ordinato dal più grande al più piccolo, senza grafica. [V/R]

**Sicurezza.**
- Il tasto elimina sposta i file nel **Cestino**. [V]
- Se gli elementi scelti sono già nel Cestino, il tasto diventa **Destroy** con un simbolo d'avviso; tenendo premuto Opzione compare l'eliminazione definitiva "per chi è davvero sicuro". [R: note di rilascio 1.10]
- Gli utenti si sono lamentati degli avvisi di sicurezza di macOS durante la scansione, senza spiegazioni; Omni ha poi aggiunto una descrizione che dice che l'app elenca i file ma non li apre. [R]

**Stato.** Aggiornamenti lenti; le build di prova 1.16 richiedono macOS 14. [R]

**Prezzo.** Gratis. [V]

**Limiti.** Nessuna vista d'insieme, nessun filtro per tipo o data, e si naviga solo cartella per cartella. [D]

---

## Parte 2: cercatori di doppioni

### PhotoSweeper (Overmacs)

**Cos'è.** Il cercatore di doppioni e foto simili più orientato ai fotografi su Mac. Sull'App Store costa 14,99 $; versione 5.5.5 per macOS 10.15 o successivo. [V] Il sito e i PDF del manuale hanno bloccato la lettura automatica (errore 403), quindi i dettagli vengono dall'App Store e dalle recensioni.

**Criteri.**
- Doppioni esatti e foto simili, valutando contenuto, composizione e ora di scatto; la soglia va dalle copie identiche alle raffiche e alle versioni modificate. [V]
- Nelle versioni precedenti i metodi erano bitmap, istogramma, intervallo di tempo e combinati. [R: recensione 2015]
- Dalla 4.9 c'è un metodo "Subjects" basato sull'intelligenza artificiale. [V]
- Ritrova anche foto ridimensionate o con saturazione diversa. [R]

**RAW più JPEG.** Supporta RAW, DNG, HEIC e TIFF e dalla 5.5 legge i sidecar XMP. [V] Un fotografo che scatta RAW più JPEG riferisce oltre 100.000 "doppioni" negli archivi e dice che le preferenze generali permettono di gestirli, ma non spiega come. [R] Non ho trovato la regola esatta per le coppie. [D: da verificare in prova]

**Scelta automatica (Auto Mark).**
- Regole personalizzabili, applicate in un ordine che si stabilisce trascinandole; per esempio la libreria di Lightroom può venire prima di quella di Foto. [V/R]
- "Quality Score" usa l'intelligenza artificiale per tenere lo scatto migliore. [V]
- Dalla 5.4 offre due modi, "tieni una foto per gruppo" e "segna solo le più deboli", **e mostra il motivo di ogni scelta**. [V]
- Con le impostazioni predefinite tiene l'immagine più grande (versione Lite). [R]
- Le foto bloccate vengono confrontate ma non possono essere segnate. [R]
- La marcatura è solo un suggerimento: non elimina niente da sola. [R]

**Anteprima.** Gruppi affiancati, modi Face-to-Face e One by One con zoom, dati EXIF, Quick Look e un badge col punteggio di qualità. [V]

**Eliminazione.** Non cancella mai in modo definitivo:
- i file vanno nel Cestino di sistema; [V]
- in Lightroom le foto vengono segnate "Rifiutate" e messe in una raccolta apposita; [V]
- in Foto vanno in un album speciale. [V]

**Librerie.** Foto di Apple, Lightroom Classic, Capture One, cartelle qualsiasi, dischi esterni e NAS (con migliorie per il NAS nella 5.4). Può ignorare le foto rifiutate in Lightroom. [V]

**Limiti.** Non confronta per hash tra dischi diversi come strumento d'archivio, e non ho trovato dati sui tempi su centinaia di migliaia di file. [D] Nella prova si possono eliminare solo 10 foto per ogni avvio. [R]

### Gemini 2 (MacPaw)

**Cos'è.** Cercatore di doppioni per tutti i tipi di file, per il grande pubblico. [V]

**Criteri.**
- "Doppioni esatti", confrontando la lunghezza dei dati e più parametri del file (il manuale non nomina l'hash). [V]
- "Simili", per esempio due foto scattate a 2 secondi di distanza. [V]
- Cartelle doppie intere e categorie per tipo: Immagini, Audio, Documenti, App. [V]
- Si può escludere la ricerca dei simili o alzare la dimensione minima per andare più veloci. [V]

**Scelta automatica (Smart Selection).**
- Con le impostazioni predefinite segna **solo i doppioni esatti** e mai i simili. [V]
- Filtri per gruppo: Automatico (segna i file più probabilmente inutili, cioè vecchi o poco usati), Più recenti, Più vecchi, A caso o Manuale. [V]
- Liste "Seleziona sempre" e "Non selezionare mai" per cartella. [V]
- **Impara dalle scelte** e propone nuove regole, che restano salvate e si possono azzerare. [V]
- Avvisa sempre se si stanno segnando tutte le copie di un file. [V]
- Ha un'opzione a parte per trattare gli hard link come file normali. [V]

**Anteprima.** Schermata di dettaglio con confronto tra le copie. [V]

**Eliminazione e annulla.**
- Con le impostazioni predefinite va nel Cestino; in alternativa sposta in una cartella o elimina in modo definitivo. [V]
- C'è un ripristino ("Review Trashed/Moved", poi Put Back), ma solo dalla schermata finale della sessione in corso: chiusa l'app, i file vanno rimessi a mano. [V]
- **Sui dischi esterni senza Cestino avvisa che può solo eliminare in modo definitivo.** [V]
- Monitor in background dei nuovi doppioni. [V]
- Ha "obiettivi da sbloccare" (gamification). [V]

**Prezzo.** Download gratuito, piani a pagamento da 1,95 $/mese secondo il sito. [V] È anche dentro Setapp. [D]

**Limiti.** Non è pensato per i RAW né per le librerie professionali, e non tiene conto dei sidecar XMP. Il manuale non dice niente di RAW più JPEG. [D]

### Czkawka / Krokiet

**Cos'è.** Suite open source in Rust con più strumenti di pulizia. Krokiet (interfaccia Slint, GPL-3) sostituisce la vecchia interfaccia GTK, che è ferma alla 12.0. Ultima versione 12.0.2 del 9 settembre 2026; per Mac ci sono solo binari arm64 (Intel non più fornito dalla 12.0). [V]

**Strumenti.** Doppioni, cartelle e file vuoti, file grandi, file temporanei, immagini simili, video simili (richiede ffmpeg), musica uguale, link rotti, file danneggiati, estensioni sbagliate, rimozione EXIF. [V]

**Criteri per i doppioni.**
- Nome, dimensione o hash, a più stadi: prima la dimensione, poi un prehash parziale, poi l'hash completo. [V]
- Hash a scelta tra Blake3, CRC32 e XXH3. [R]
- La **cache dei prehash** contiene i primi e gli ultimi 4 KB dei file grandi, così alle scansioni successive si calcola l'hash completo solo dei file nuovi o cambiati. [V]
- Per i **dischi rimovibili** si può disattivare la pulizia automatica della cache, così non si perde quando il disco è staccato. [V]

**Immagini simili.**
- Hash percettivi Gradient, Mean, VertGradient, DoubleGradient e Blockhash, su 4×4, 8×8 o 16×16, confrontati con la distanza di Hamming. [R: istruzioni del repository, versioni precedenti]
- Dalla 11.0 legge **l'anteprima JPEG incorporata nei RAW**. [V]

**Percorsi di riferimento.** Le cartelle segnate come riferimento non vengono mai spostate né eliminate; vale per doppioni, immagini, video e musica. [V]

**Scelta ed eliminazione.**
- Dalla 12.0 c'è una nuova finestra di selezione personalizzata. [V]
- Dalla 12.0 ci sono **tasti separati per "Sposta nel Cestino" ed "Elimina in modo definitivo"**. [V]
- Si può sostituire un doppione con un hard link o un link simbolico, e dalla 12.0.2 l'app segnala quando l'annullamento di queste operazioni non riesce. [V]
- Esistono anche spostamento e ordinamenti come "più vecchio" o "più grande". [D]

**Prezzo.** Gratis. [V]

**Limiti.** L'interfaccia è da strumento tecnico, non da fotografo. Le coppie RAW più JPEG non vengono trattate come un'unità. Non c'è una vista d'insieme dello spazio. [D]

### dupeGuru

**Cos'è.** Cercatore di doppioni open source (GPL-3) multipiattaforma, con modi Standard, Musica e Foto. Ultima versione 4.3.1, circa luglio 2022; build universale Intel e Apple Silicon. [V/R] Di fatto è poco mantenuto. [D]

**Criteri.**
- Contenuto: raggruppa per dimensione, scarta i file unici e confronta i restanti con MD5 sull'intero contenuto. Esiste anche una variante per le cartelle intere, che tiene solo le cartelle di livello più alto. [V]
- Nome: "a parole", con soglia di somiglianza regolabile. [V]
- Foto: griglia 15×15 di colori medi confrontata tile per tile. Il costo cresce col quadrato del numero di foto, anche se usa più core; c'è una **cache delle impronte**. [V]
- Timestamp EXIF `DateTimeOriginal`, che il manuale stesso dice dare molti falsi positivi. [V]

**Cartelle di riferimento.** Ogni cartella è Normale, Riferimento (i file sono protetti e possono solo fare da originale) o Esclusa. Le sottocartelle ereditano lo stato della cartella sopra. [V]

**Scelta di cosa tenere (Re-Prioritize).**
- Una lista ordinata di criteri, per esempio "Dimensione (la più alta)", "Cartella (/percorso)" o "Nome (non finisce con un numero)". [V]
- Il primo criterio decide e i successivi servono solo in caso di parità; l'ordine si cambia trascinando. [V]

**Revisione dei risultati.**
- Pannello Dettagli che mette il file accanto al suo riferimento. [V]
- **Valori delta**: le differenze rispetto al riferimento compaiono in arancione (per esempio -0,2 MB). [V]
- Modo "solo doppioni", "rendi riferimento il selezionato" e lista dei file da ignorare. [V]
- Esportazione in XHTML. [V]

**Eliminazione.**
- Cestino, oppure spostamento o copia mantenendo i percorsi. [V]
- Si può sostituire il doppione con un hard link o un link simbolico verso il riferimento. [V]
- L'eliminazione diretta esiste solo come ripiego per i NAS dove il Cestino non funziona. [V]

**Prezzo.** Gratis. [V]

**Limiti.** Interfaccia datata, niente RAW più JPEG, niente anteprime affiancate grandi, e il confronto delle foto è lento sulle grandi collezioni. [D]

### digiKam, funzione Doppioni

**Cos'è.** Gestore fotografico open source (KDE) con la ricerca dei doppioni dentro il suo database. [V]

**Criteri.**
- Impronte basate su wavelet di Haar ("Fast Multi-Resolution Image Querying"), da calcolare prima. Il manuale avverte che sulle grandi collezioni ci possono volere ore. [V]
- **Intervallo di somiglianza**: 100% vuol dire identiche. Mettendo il limite massimo poco sotto il 100% si escludono le copie esatte e si tengono raffiche e serie. [V]
- Si può limitare la ricerca ad album o tag scelti, perché ogni foto viene confrontata con tutte le altre. [V]

**Scelta dell'originale.** C'è un menu "metodo di scelta dell'immagine di riferimento": la più vecchia o la più grande (metodo precedente alla 8.1), preferire o evitare la cartella scelta, oppure la data di creazione o modifica più recente. Si può anche limitare la ricerca all'album di riferimento o escluderlo. [V]

**Anteprima.** Lista dei gruppi con miniatura di riferimento, numero di elementi e somiglianza media; nella vista tabella c'è anche una colonna somiglianza. [V] Nel 2025 un bug faceva contare i gruppi senza mostrarli. [R]

**Eliminazione.** "Remove Duplicates" elimina i doppioni del gruppo e lascia il riferimento. Se si passi dal Cestino non è indicato in quella pagina; digiKam di solito usa il proprio cestino. [V/D]

**Altre funzioni.** Ricerca per immagine trascinata e ricerca per **schizzo** a mano libera. [V]

**Limiti.** Bisogna importare tutto nel database di digiKam e calcolare le impronte, cosa pesante su 100 TB. È poco adatto a un confronto veloce tra dischi. [D]

### Altri strumenti utili da conoscere

- **Excire Foto / Excire Search** (plugin per Lightroom):
  - doppioni esatti tramite hash binario identico, e quasi doppioni visivi con severità da "molto rigida" a "molto larga" (la più rigida è quella consigliata); [V]
  - per i doppioni esatti il manuale ammette che **non c'è modo automatico di sapere quale tenere** e propone come criteri parti del nome o della cartella; [V]
  - per i quasi doppioni può tenere la foto a risoluzione più alta, **il RAW** o quella con più stelle, e l'intervallo massimo delle raffiche è regolabile; [V]
  - i database locali occupano circa 250 MB ogni 100.000 foto. [V] Il funzionamento offline non è confermato. [D]
- **fclones** (riga di comando, Rust): è dichiarato molto veloce su SSD e HDD e può deduplicare con reflink su Btrfs, XFS e ZFS. [R] Il wrapper **apfs-dedupe** lo usa per creare cloni APFS; con le impostazioni predefinite fa solo una prova (dry-run) e cambia qualcosa solo con `--apply`. [R]
- **Nota APFS (Eclectic Light)**:
  - sullo stesso volume APFS le copie fatte dal Finder sono di solito **cloni** che condividono i blocchi, quindi eliminarne uno non libera quasi niente; [R]
  - non esiste un modo ufficiale per sapere se due file sono ancora cloni; [R]
  - spostare i cloni su un altro volume li fa diventare file pieni; [R]
  - gli hard link sono un caso ancora diverso. [R]

---

## Tabella di confronto

| App | Tipo | Visualizzazione / criteri | Scelta automatica | Dove va ciò che si elimina | Annulla | Grandi archivi | Prezzo | Stato |
|---|---|---|---|---|---|---|---|---|
| DaisyDisk | Mappa | Anelli (sunburst) per cartella | — | **Eliminazione definitiva** dopo 5 s | Solo i 5 s del conto alla rovescia | Parallelo, coda sugli HDD; nessuna cache documentata | 9,99 $ una tantum | Attivo |
| GrandPerspective | Mappa | Treemap, colori per tipo o data, filtri | — | Cestino, con conferma configurabile | Cestino | Scansioni salvabili e ricaricabili | Gratis / 2,99 $ | Attivo (3.8.1, 2026) |
| Disk Inventory X | Mappa | Treemap più tipi di file | — | n.d. | n.d. | n.d. | Gratis | Fermo (macOS ≤10.15) |
| OmniDiskSweeper | Mappa | Elenco a colonne per dimensione | — | Cestino, poi Destroy | Cestino | Solo elenco | Gratis | Lento |
| PhotoSweeper | Doppioni foto | Esatti più simili (contenuto, tempo, intelligenza artificiale) | Regole ordinate, punteggio di qualità, motivo mostrato | Cestino, Rifiutate in Lightroom, album in Foto | Cestino | n.d. | 14,99 $ | Attivo (5.5.5) |
| Gemini 2 | Doppioni generici | Esatti più simili, per categoria | Più vecchio, più recente, automatico, impara; liste sempre/mai | Cestino, cartella o definitivo | Put Back solo nella sessione in corso | Opzioni per velocizzare | Abbonamento | Attivo |
| Czkawka/Krokiet | Doppioni più pulizia | Nome, dimensione o hash (Blake3, XXH3, CRC32); hash percettivi | Finestra di selezione personalizzata | Cestino o definitivo (tasti separati), link | Cestino | **Cache dei prehash**, adatta ai dischi rimovibili | Gratis (GPL/MIT) | Attivo (12.0.2, 2026) |
| dupeGuru | Doppioni | MD5 del contenuto, nome, griglia foto, EXIF | Criteri ordinati con spareggio | Cestino, sposta, copia, link | Cestino | Foto lente (costo quadratico) | Gratis (GPL) | Fermo dal 2022 |
| digiKam | Doppioni nel database | Impronte Haar, intervallo di somiglianza | Metodo di riferimento (più vecchio, più grande, cartella, data) | Cestino di digiKam [D] | [D] | Impronte da calcolare (ore) | Gratis | Attivo |
| Excire | Doppioni nel database | Hash più somiglianza visiva | Tiene il RAW, la risoluzione più alta o più stelle | Segni "rifiuta" | — | Database locale | A pagamento | Attivo |

---

## Idee da prendere per RawLine Space

1. **Collector in stile DaisyDisk, ma col Cestino.** Una zona di parcheggio dove si accumula ciò che si vuole togliere, con il totale dei GB che si liberano e i file che si possono ancora togliere dalla lista. Il conto alla rovescia di 5 secondi va bene come ultimo freno, non come unica sicurezza.
2. **Cartelle e dischi di riferimento** come in dupeGuru e Czkawka: per esempio "il disco ARCHIVIO-A è l'originale, mai toccarlo". È il modo più semplice e solido di evitare errori tra dischi diversi.
3. **Hash a stadi con cache persistente** come in Czkawka: prima la dimensione, poi un prehash dei primi e ultimi blocchi, poi l'hash completo (XXH3 o Blake3), solo dove serve. La cache va legata all'UUID del volume e non va cancellata quando il disco è staccato: su 100 TB è l'unica via praticabile, e si lavora con dischi esterni che vanno e vengono.
4. **Scansioni salvate e confrontabili** come in GrandPerspective: un catalogo che resta consultabile anche **a disco scollegato**. È anche il "catalogo" che il nome promette.
5. **Coda sugli HDD e parallelo sugli SSD** come in DaisyDisk: non scansionare in parallelo due cartelle dello stesso disco rotante.
6. **Criteri ordinati per scegliere l'originale, con spareggio** come in dupeGuru e PhotoSweeper, preparati per i fotografi:
   - tieni il file con sidecar XMP o con stelle;
   - tieni quello sul disco di riferimento;
   - tieni il percorso più "ordinato" (per esempio anno/cliente);
   - tieni il più vecchio per data di creazione;
   - tieni il nome che non finisce con "copia" o con un numero.
   **E mostrare sempre il perché di ogni scelta**, come PhotoSweeper 5.4.
7. **Valori delta** di dupeGuru: nel gruppo, evidenziare in colore ciò che differisce dall'originale (dimensione, data, percorso, presenza di XMP).
8. **Avviso "stai togliendo tutte le copie"** di Gemini: blocco netto se in un gruppo non resta nessuna copia.
9. **Coppie RAW più JPEG e sidecar trattati come un'unità**: idea già vista in Lightroom (stesso nome base, stessa cartella), che i cercatori generici non hanno. Un doppione è "doppio" solo se lo è tutto il pacchetto (RAW, XMP e JPEG). Si può anche proporre "elimina i JPEG gemelli di RAW già selezionati".
10. **Somiglianza visiva come modalità a parte e mai segnata in automatico** (impostazione di Gemini). Leggere l'anteprima JPEG incorporata nei RAW (come Czkawka 11) per restare leggeri; il calcolo resta in locale, coerente con la regola offline.
11. **Anteprima affiancata con zoom sincronizzato** (Face-to-Face di PhotoSweeper) per i casi dubbi.
12. **Filtri della mappa salvabili e usabili anche in scansione**, come GrandPerspective, più i raggruppamenti logici che a tutti mancano: **anno di scatto (EXIF), cliente (dal percorso o da una regola), tipo di file (RAW, JPEG, video, progetti FCP o Lightroom, proxy, cache)**.
13. **Riconoscere cloni APFS e hard link** e non contarli come spazio recuperabile (lezione di Eclectic Light). Mostrare "spazio che si libera davvero", non la somma delle dimensioni apparenti.
14. **Alternativa all'eliminazione**: "sposta in una cartella di quarantena" sullo stesso disco, oppure sostituisci con un link, come in dupeGuru e Gemini.
15. **Esportazione di un rapporto** (dupeGuru esporta in XHTML) di ciò che è stato tolto: percorso, hash, data, disco. È la base per un "annulla" vero anche dopo giorni.
16. **Gestione esplicita dei dischi senza Cestino** (NAS, exFAT): Gemini avvisa e cancella in modo definitivo; meglio proporre la quarantena.

## Cose da NON copiare

- **L'eliminazione definitiva come impostazione predefinita** (DaisyDisk). Su un archivio di lavoro, dove un file perso è un lavoro perso, ci vuole il Cestino o la quarantena, sempre.
- **Un annulla che vale solo nella sessione in corso** (Gemini). Il registro delle operazioni deve sopravvivere alla chiusura dell'app.
- **Eliminare una cartella intera con dentro file nascosti dal filtro** (GrandPerspective lo dichiara). Se c'è un filtro attivo, eliminare solo ciò che si vede, oppure avvisare con il conto dei file nascosti.
- **Una scelta automatica "che impara" senza spiegare** (Gemini) e le **regole che si possono solo azzerare**, non modificare. Su 100 TB servono regole leggibili e modificabili.
- **La gamification** (gli "obiettivi" di Gemini): non c'entra con un'app professionale.
- **Il confronto visivo di tutti contro tutti** (dupeGuru, digiKam): il costo quadratico non regge su milioni di file. Prima vanno ristretti i candidati (per data, dimensione, hash percettivo indicizzato).
- **Usare la sola data EXIF come criterio di doppione** (dupeGuru): troppi falsi positivi con raffiche e versioni modificate.
- **Importare tutto in un database proprietario prima di poter cercare** (digiKam, Excire): ore di calcolo. Il catalogo deve nascere dalla scansione stessa.
- **Mostrare come "recuperabile" lo spazio di cloni APFS e hard link**: promette GB che non si liberano.
- **Avvisi di sicurezza di macOS senza spiegazione** (OmniDiskSweeper): spiegare prima perché serve l'accesso completo al disco.
- **Seguire le cartelle cloud non presenti in locale** (GrandPerspective con Google Drive): RawLine Space è offline e non deve mai provocare download. Va escluso, o segnalato, tutto ciò che è solo nel cloud.

## Fonti (link)

**Mappe dello spazio**
- DaisyDisk, sito: https://daisydiskapp.com/
- DaisyDisk, guida all'eliminazione: https://daisydiskapp.com/guide/4/en/DeletingFiles/
- DaisyDisk, scansione in parallelo: https://daisydiskapp.com/guide/4/en/ParallelScan/
- DaisyDisk, indice della guida: https://daisydiskapp.com/guide/4/en/
- GrandPerspective, sito: https://grandperspectiv.sourceforge.net/
- GrandPerspective, preferenze (eliminazione): https://grandperspectiv.sourceforge.net/HelpDocumentation/Preferences.html
- GrandPerspective, novità: https://www.sourceforge.net/p/grandperspectiv/news
- GrandPerspective, bug cloud n. 105: https://sourceforge.net/p/grandperspectiv/bugs/105
- Disk Inventory X: https://www.derlien.com/
- OmniDiskSweeper: https://www.omnigroup.com/more
- OmniDiskSweeper, note di rilascio 1.10: https://omnigroup.com/releasenotes/omnidisksweeper/1.10
- OmniDiskSweeper su MacUpdate (recensioni): https://omnidisksweeper.macupdate.com

**Doppioni**
- PhotoSweeper sull'App Store: https://apps.apple.com/us/app/photosweeper-x/id463362050
- PhotoSweeper, recensione Northlight Images: https://www.northlight-images.co.uk/photosweeper-cleaning-up-photo-libraries/
- PhotoSweeper, recensione TNW 2015: https://thenextweb.com/news/photosweeper-upgrade-lets-you-take-control-of-your-photo-collection
- PhotoSweeper, manuale (non leggibile in automatico): https://overmacs.com/photosweeper/downloads/it/PhotoSweeperManual_IT.pdf
- Gemini 2, sito: https://macpaw.com/gemini
- Gemini 2, manuale utente (PDF): https://cdn2.macpaw.com/manuals/Gemin-2-User-Guide-29062021.pdf
- Czkawka/Krokiet, repository: https://github.com/qarmin/czkawka
- Czkawka, istruzioni: https://github.com/qarmin/czkawka/blob/master/instructions/Instruction.md
- Czkawka, rilasci: https://github.com/qarmin/czkawka/releases
- Krokiet, README: https://github.com/qarmin/czkawka/blob/master/krokiet/README.md
- Czkawka, recensione LinuxReviews: https://www.linuxreviews.org/Find_And_Remove_Duplicate_Files,_Similar_Images_And_More_With_Czkawka
- dupeGuru, aiuto: https://dupeguru.voltaicideas.net/help/en/
- dupeGuru, scansione: https://dupeguru.voltaicideas.net/help/en/scan.html
- dupeGuru, cartelle: https://dupeguru.voltaicideas.net/help/en/folders.html
- dupeGuru, risultati: https://dupeguru.voltaicideas.net/help/en/results.html
- dupeGuru, priorità: https://dupeguru.voltaicideas.net/help/en/reprioritize.html
- dupeGuru, rilasci: https://github.com/arsenetar/dupeguru/releases
- digiKam, vista somiglianza: https://docs.digikam.org/en/left_sidebar/similarity_view.html
- digiKam, strumento doppioni: https://docs.digikam.org/es/maintenance_tools/maintenance_duplicates.html
- digiKam, bug KDE 508733: https://bugs.kde.org/show_bug.cgi?id=508733
- Excire, ricerca doppioni: https://excire.com/en/tutorials/excire-search/duplikatefinder/
- Excire Foto, trovare i doppioni: https://excire.com/en/tutorials/excire-foto-2024/duplikate-finden/

**Altro**
- fclones: https://github.com/th1000s/fclones
- apfs-dedupe: https://awesome.ecosyste.ms/projects/github.com%2Fcurlewlabs-com%2Fapfs-dedupe
- Eclectic Light, "Should you remove duplicate files?": https://eclecticlight.co/2023/04/22/should-you-remove-duplicate-files/
- Eclectic Light, copie, cloni e hard link: https://eclecticlight.co/2025/05/13/how-to-tell-the-difference-between-copies-clone-files-and-hard-links/
