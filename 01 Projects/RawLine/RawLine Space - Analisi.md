# RawLine Space: analisi di fondo su sicurezza, architettura e strada

Data: 2026-11-11. Questo documento rilegge tutto quello che c'è in [[RawLine Space]] (decisioni di Andrea, 23 note di ricerca, dati veri del G-SPEED) e cerca i punti deboli, le scelte migliori e l'ordine in cui costruire.

> Tutto quello che c'è qui è **una proposta mia**, salvo dove è scritto "già deciso". Niente di questo documento cambia le decisioni di Andrea finché lui non lo conferma.
> Dove un'affermazione viene dalla ricerca già fatta, è nel documento principale con la fonte. Dove è un mio ragionamento non ancora provato, è segnata **(da provare)**.

---

## 0. In breve

1. **Il rischio non è distribuito in modo uniforme.** In tutta l'app c'è un solo gesto davvero senza ritorno: svuotare la quarantena. Tutto il resto, se costruito bene, si annulla. La cura maggiore va messa lì e nelle decisioni che ci portano.
2. **Riordinare sullo stesso disco quasi non mette a rischio i file. Mette a rischio i collegamenti**: cataloghi di Lightroom, librerie video, backup. Per Andrea il danno sarebbe soprattutto di tempo: le elaborazioni stanno anche negli XMP (verificato la sera dell'11 nov, sezione 10).
3. **In "Libera spazio" il pericolo non è tecnico, è di giudizio**: togliere, con il pieno consenso dell'utente, un RAW che in realtà era servito, perché l'abbinamento con l'export era sbagliato. Serve una regola che renda visibile questo errore prima che accada (sezione 3.2).
4. **La sicurezza si ottiene restringendo, non aggiungendo conferme.** Un solo pezzo di codice può scrivere sui dischi, con sette azioni possibili. Una sola funzione in tutta l'app può eliminare per davvero.
5. **Ogni disco è in sola lettura per Space finché l'utente non lo sblocca.** La regola del G-SPEED diventa il comportamento normale dell'app, per tutti.
6. **Le prove sono il prodotto.** Un simulatore che spegne la corrente in ogni punto, dischi finti di ogni formato, e la prova "andata e ritorno" su una copia di un pezzo vero dell'archivio.
7. **Si esce a scalini, dal meno rischioso al più rischioso.** La prima versione legge soltanto. L'eliminazione definitiva arriva per ultima.
8. **Space non sostituisce un backup**, e deve dirlo. La domanda più importante ancora aperta è se dell'archivio sul G-SPEED esiste una seconda copia.

---

## 1. Dove sta davvero il rischio

Ho messo in fila tutto quello che Space può fare, dal gesto più innocuo a quello senza ritorno.

| Gesto | Cosa può andare storto nel caso peggiore | Si torna indietro? |
|---|---|---|
| **Leggere** (catalogare, analizzare, proporre) | Niente sui file. Al massimo una proposta sbagliata. | Non c'è niente da annullare. |
| **Spostare o rinominare sullo stesso disco** | I file restano intatti. Si rompono i collegamenti di altre app (Lightroom, Final Cut, Premiere, InDesign) e i backup ricopiano tutto. | Sì, sempre. |
| **Copiare su un altro disco** | L'originale non si tocca. Il pericolo è una copia dichiarata buona che non lo è. | Sì: si toglie la copia. |
| **Mettere in quarantena** | Il file c'è ancora, ma è nascosto. Le altre app lo vedono mancante. | Sì, finché la quarantena non viene svuotata. |
| **Svuotare la quarantena** | Il file non esiste più. | **No.** |
| **Scrivere dentro file di altri** (catalogo di Lightroom, XMP) | Un catalogo rovinato. | Solo se c'è una copia. |

Da questa scala vengono tre conseguenze.

- **Tutte le strade che portano a perdere un file passano da "svuota la quarantena".** Se quel punto è costruito bene, un errore in qualunque altro punto dell'app costa tempo, non foto.
- **La quarantena da sola non basta.** Chi usa "Libera spazio" lo fa perché gli manca spazio. La quarantena non ne libera, quindi la tentazione è svuotarla subito. Una protezione che l'utente ha fretta di togliere protegge poco. Per questo al momento di svuotare servono controlli veri (sezione 3.2), non solo una conferma più faticosa.
- **Scrivere nei file di altri resta fuori dalla prima versione.** Lo era già nel documento. Lo confermo con più forza.

---

## 2. Sette scelte di architettura

### 2.1 Una sola porta per scrivere

Oggi il documento descrive bene *come* si sposta e si copia un file. Manca una regola su *chi* nel codice può farlo.

**Proposta:** un modulo piccolo in RawlineKit, il **motore di scrittura**, è l'unico pezzo dell'app che può modificare un disco dell'utente. Sa fare sette cose e nient'altro:

1. rinominare o spostare sullo stesso disco, senza mai sovrascrivere;
2. creare una cartella;
3. copiare su un altro disco con la verifica;
4. mettere in quarantena;
5. riportare dalla quarantena;
6. svuotare la quarantena;
7. cancellare i propri file temporanei.

Tutto il resto dell'app (analisi, proposte, intelligenza artificiale, interfaccia) produce solo un **piano**: un elenco di azioni scritto come dato. Non tocca mai un file.

Tre conseguenze pratiche:

- **In tutto il codice l'eliminazione vera di un file dell'utente esiste in una sola funzione**, quella che svuota la quarantena. Un controllo automatico, a ogni modifica del codice, verifica che non compaia da nessun'altra parte.
- **Anche le cartelle rimaste vuote non si cancellano**: vanno in quarantena. Una cartella "vuota" può contenere file nascosti.
- Un errore nell'analisi, per esempio un percorso calcolato male, non può fare danni da solo: deve passare dal motore, che lo rifiuta.

### 2.2 Il piano viene controllato da un secondo paio d'occhi

Prima di eseguire, un **verificatore** scritto a parte, che non condivide codice con chi ha preparato il piano, controlla che il piano rispetti regole fisse. Se una sola regola fallisce, il piano non parte.

- **Legge di conservazione.** In un riordino il numero dei file, i byte totali e l'identità di ogni file prima e dopo sono uguali. Un riordino non può far sparire niente, per costruzione.
- **Un piano di riordino non può contenere quarantene.** Sono due tipi di piano diversi. Un riordino che "per sbaglio" elimina non si può nemmeno scrivere.
- Nessuna destinazione coincide con un file esistente o con un'altra destinazione, confrontando i nomi senza badare a maiuscole e accenti.
- Nessun percorso esce dalle cartelle che l'utente ha indicato.
- Nessuna famiglia viene spezzata (RAW, XMP, JPEG gemello, WAV; clip e suoi file).
- Nessun disco protetto viene toccato (sezione 2.3).

Dopo l'esecuzione lo stesso verificatore rifà il conto sul disco: ogni file che c'era prima c'è ancora, nel posto previsto. Sullo stesso disco questo controllo costa pochi secondi, perché non rilegge il contenuto.

Questo risponde alla lezione di Big Mean Folder Machine, ritirata perché l'anteprima non corrispondeva a quello che faceva: l'anteprima, il piano e l'esecuzione sono lo stesso dato, e c'è un controllo indipendente prima e dopo.

### 2.3 Ogni disco è protetto finché non lo sblocchi

La regola di Andrea sul G-SPEED è la più sana di tutto il progetto. Propongo di farla diventare il comportamento normale dell'app.

- **Un disco nuovo per Space è in sola lettura.** Si può catalogare e analizzare. Per scriverci l'utente deve sbloccarlo, disco per disco, con un gesto esplicito. Lo sblocco si può togliere in ogni momento.
- **Il blocco sta nel motore di scrittura**, non nell'interfaccia. Un piano che tocca un disco protetto viene rifiutato anche se un errore lo ha fatto arrivare fin lì.
- **Cartelle protette**, oltre ai dischi: i lavori in corso. Proposta: di default Space non propone riordini né "Libera spazio" sui servizi che hanno file modificati negli ultimi N giorni (N a scelta, per esempio 90). Ciò che è vivo non si tocca.

Per Andrea vuol dire che il G-SPEED resta chiuso finché non decide lui, e che la prima versione di Space ci può già lavorare sopra senza violare la regola (sezione 6).

### 2.4 Il ripristino è un riordino verso un'istantanea

Oggi la sezione 6 dice che per tornare a una data Space annulla le operazioni una alla volta, dalla più recente all'indietro. Funziona solo se tra un'operazione e l'altra nessuno ha toccato niente. Nella realtà Andrea sposta una cartella nel Finder, Lightroom riscrive un XMP, arriva un lavoro nuovo.

**Proposta:** "Ripristina schema precedente" non ripercorre le operazioni al contrario. Prende l'istantanea di quella data, guarda com'è il disco adesso e prepara **un piano nuovo** che porta dallo stato di oggi a quello di allora. Quel piano passa dal verificatore, dall'anteprima e dalla conferma come ogni altro.

Vantaggi:
- regge a qualunque cosa sia successa nel frattempo, anche fuori da Space;
- usa lo stesso motore e gli stessi controlli, quindi non c'è un secondo percorso di codice meno provato;
- i file arrivati dopo restano dove sono e vengono elencati.

Per funzionare serve riconoscere lo stesso file anche se ha cambiato nome o posto. Propongo un'**identità a cascata**:
1. l'identificativo interno del file sul disco, che su HFS+ e APFS non cambia con le rinomine (già provato sul Mac);
2. se manca, impronta dello scatto (numero di serie + ora) o hash del contenuto;
3. se manca anche quello, nome più dimensione più data, e in quel caso Space chiede.

Un limite da tenere presente: alcune app, quando salvano, sostituiscono il file con uno nuovo, e l'identificativo cambia **(da provare con Photoshop e con gli XMP scritti da Lightroom e Camera Raw)**. Per gli XMP non è un problema, perché seguono il loro RAW per nome.

### 2.5 Il registro: tre cose da aggiungere

Il progetto del registro nella nota tecnica è solido. Aggiungo tre punti.

- **Deve restare leggibile per sempre.** Andrea vuole annullare anche mesi dopo. In quei mesi l'app si aggiorna. Ogni versione futura di Space deve saper leggere i registri scritti da tutte le versioni precedenti, e questo va provato a ogni rilascio con registri veri conservati apposta. Un aggiornamento non deve mai partire mentre un'operazione è in corso.
- **Chi comanda tra la copia sul Mac e quella sul disco.** La copia sul disco è quella che fa fede, perché viaggia con i file. Quella sul Mac serve a cercare in fretta. Se le due non coincidono, Space non indovina: si ferma e lo dice. Dove la copia sul disco non si può tenere (il G-SPEED, finché vale la regola), il registro sul Mac va incluso nel backup del Mac ed esportato a ogni operazione.
- **La copia sul disco è un file di testo a sole aggiunte**, in cui ogni riga porta l'impronta della precedente. Se il file viene troncato o alterato, Space se ne accorge.

### 2.6 Porta zero: le condizioni prima di cominciare

Prima delle cinque porte ne serve una che non chiede niente all'utente, ma controlla le condizioni. Se una manca, Space lo dice e non applica.

- **Le app che usano quei file sono chiuse.** Lightroom aperto mentre Space sposta una cartella può riscrivere un XMP nel vecchio posto. Space vede quali app sono aperte e chiede di chiuderle quando il piano tocca cartelle catalogate.
- **Il disco non ha dato errori di lettura o scrittura** in questa sessione. Al primo errore Space si ferma su quel disco e passa in sola lettura.
- **Il Mac non va in stop** durante l'operazione, e uno scollegamento mette in pausa.
- **C'è spazio**, con margine, per tutto il piano.
- **Promemoria sul backup** alla prima operazione grande su un disco: "Di questo disco esiste un'altra copia?". Non blocca, ma la risposta resta nel registro.

### 2.7 Le prove sono il prodotto

Per un'app così la fiducia non viene dalle funzioni, viene da come è stata provata. Propongo quattro livelli, tutti automatici tranne l'ultimo.

1. **Simulatore.** Il motore di scrittura non parla direttamente col disco: parla con un'interfaccia. Nelle prove dietro l'interfaccia c'è un disco finto che può fallire a comando: corrente che salta, disco pieno, disco scollegato, scrittura che il disco dichiara fatta e non lo è. Si generano migliaia di archivi e di piani a caso, si interrompe in ogni punto, si fa ripartire. La regola da rispettare è sempre la stessa: **ogni file di partenza esiste ancora, una volta sola, con lo stesso contenuto**.
2. **Dischi finti ma veri.** macOS sa creare immagini disco in ogni formato: APFS, HFS+, exFAT, con e senza distinzione delle maiuscole. Le prove le montano, ci lavorano sopra e le staccano di forza a metà operazione. Così si prova ogni formato senza comprare dischi e senza toccare un archivio vero. Il NAS va provato a parte, su un NAS di prova.
3. **Andata e ritorno.** Su una copia di un pezzo vero dell'archivio (qualche centinaio di GB, su un disco di prova): si fa l'elenco completo con gli hash, si applica un riordino, si ripristina, si rifà l'elenco. I due elenchi devono essere identici, comprese date ed etichette. È la prova d'accettazione di ogni versione.
4. **Uso vero, a scalini** (sezione 6).

Vale la pena pubblicare come Space viene provato. Nessuna delle app studiate lo fa, ed è l'argomento più forte verso un professionista.

---

## 3. Funzione per funzione

### 3.1 Riordino: il danno vero sono i collegamenti

Sullo stesso disco i file non corrono rischi seri: il contenuto non viene mai riscritto. Quello che si rompe è intorno.

**Lightroom.** Dal documento: se si sposta un albero intero senza cambiare niente dentro, in Lightroom basta ricollegare la cartella più alta. Ma il riordino di Space fa proprio l'opposto: cambia la struttura. Se una cartella catalogata da 27.000 RAW (come `2020:2021/2020`) viene divisa in sessanta servizi, in Lightroom quelle foto risultano mancanti e vanno ritrovate cartella per cartella. **Correzione (11 nov sera):** avevo scritto che per Andrea il rischio era alto perché circa 125.000 RAW non hanno l'XMP accanto. Era sbagliato: quasi tutti quei RAW non sono mai stati elaborati. Nel catalogo la scrittura automatica degli XMP è attiva, e i RAW sviluppati senza XMP risultano almeno 1.498 (sezione 10). Reimportando, gli sviluppi tornano dagli XMP. Restano solo nel catalogo le collezioni, la cronologia e le 413 copie virtuali.

Quattro proposte, dalla più semplice:

1. **Controllare che gli XMP siano aggiornati.** Nel catalogo di Andrea la scrittura automatica è già attiva (sezione 10), quindi di norma non c'è niente da fare. Per gli altri utenti Space avvisa se è spenta. Gli XMP non contengono tutto: collezioni, copie virtuali e cronologia restano solo nel catalogo, e da quanto so anche le bandierine **(da verificare)**.
2. **Il costo di ricollegamento, in numeri.** Per ogni piano Space calcola quante azioni di ricollegamento serviranno in Lightroom e lo mostra nel controllo finale: "questo riordino richiede 3 ricollegamenti" oppure "412". Chi prepara il piano preferisce le soluzioni che ne richiedono meno.
3. **Le cartelle catalogate si spostano intere, di default.** Dividere una cartella catalogata richiede un consenso esplicito, con il costo di ricollegamento in vista.
4. **Più avanti, una copia aggiornata del catalogo.** Space non modifica mai il catalogo dove sta. Ne fa una copia, aggiorna i percorsi in quella, ne controlla l'integrità, e Andrea apre la copia. L'originale resta com'era e serve per tornare indietro. È più sicuro dell'"aggiornamento diretto" descritto oggi nella sezione 8. Resta la parte più delicata e va per ultima.

**Backup e sincronizzazioni.** Un riordino grande fa ricopiare tutto a Time Machine e a molti programmi di backup. Il documento lo prevede già (8bis.4, punto 8). Aggiungo: se la cartella sta dentro un programma di sincronizzazione, Space non applica finché l'utente non l'ha messo in pausa.

**Una correzione al documento.** La sezione 3.1 chiama "sconsigliata" la modalità "direttamente sulla sorgente". Dopo la decisione di Andrea sulla 3.2 non regge più, e a ragione: per un riordino, spostare sul posto è la strada che mette meno a rischio i file, perché nessun dato viene riscritto. Copiare 15 TB su un altro disco per riordinarli porta poi a dover eliminare il vecchio archivio, che è un'operazione più pericolosa. Propongo:
- **riordino sul posto come modalità normale**;
- **"su copia"** quando si vuole provare o si sta comunque migrando su un disco nuovo;
- **togliere dalla prima versione il clone APFS**: ottiene lo stesso risultato della rinomina sul posto, ma alla fine bisogna eliminare la struttura vecchia. Più complessità e un'eliminazione in più, senza vantaggi.

### 3.2 Libera spazio: l'errore vero è l'abbinamento sbagliato

Qui il sistema può funzionare alla perfezione e fare lo stesso un danno: Space dice "questi 2.966 RAW non sono serviti", l'utente conferma, e tra quelli ce ne sono 180 che invece erano stati consegnati, perché l'export era stato rinominato e l'abbinamento non l'ha trovato. Nessuna conferma protegge da questo, perché l'utente si fida dell'elenco.

**La regola che lo rende visibile: si conta dal lato degli export.** Ogni export deve aver trovato il suo RAW. Se un export non ha un RAW abbinato, vuol dire che il suo RAW è finito nel mucchio dei "non usati". Quindi:

- **finché esiste anche un solo export senza RAW abbinato, quel progetto non si può alleggerire.** Space mostra gli export orfani e Andrea decide caso per caso: lo abbina a mano, oppure dichiara che quell'export non ha un RAW (una foto del telefono, un fotogramma di un video, un JPEG della fotocamera).
- Sul G-SPEED ci sono 11 servizi in cui nessun export ha il nome del RAW. Con questa regola quei progetti restano bloccati finché l'abbinamento non è risolto. È il comportamento giusto.

Altri quattro casi che oggi il documento non copre:

- **Un export nato da più RAW.** Panorami, HDR, esposizioni multiple, composizioni in Photoshop. L'abbinamento ne trova al massimo uno. Selects riconosce già pile HDR e panorami: se un RAW di una pila è stato usato, **tutta la pila resta**.
- **I JPEG della fotocamera non sono export.** Chi scatta in RAW+JPEG ha cartelle di JPEG che sembrano export. Si distinguono dal programma che li ha scritti (la fotocamera, non Lightroom) e dalle dimensioni piene.
- **Le strade A e B sono più gravi della C.** "Tieni solo gli export" elimina anche i RAW usati, cioè i negativi dei lavori consegnati. Vanno trattate come un gradino sopra: conferma più forte, e proposte solo oltre un'età più alta.
- **Regole di conservazione per cliente.** Andrea ha detto che i lavori di 5–7 anni fa sono liberi. Altri professionisti hanno contratti che impongono di conservare. Nelle impostazioni per cliente va un campo "non proporre prima di N anni".

**Al momento di svuotare la quarantena**, che è l'unico gesto senza ritorno, Space rifà i controlli da capo, non si fida di quelli di un mese prima:
- gli export che giustificavano l'eliminazione ci sono ancora e si aprono;
- nessuno dei file in quarantena è nel frattempo entrato in un catalogo o in un progetto;
- il conto dei file corrisponde al manifesto.

**Due proposte nuove.**

- **La soffitta.** Tra "tenere" ed "eliminare" c'è una terza strada che molti preferirebbero: spostare i RAW non usati su un disco lento ed economico, con copia verificata, e liberare il disco veloce. Usa lo stesso motore dello spostamento tra dischi. Il catalogo ricorda dove sono. Chi non se la sente di eliminare ha comunque un modo per liberare spazio.
- **Il ricordo.** Prima di un'eliminazione definitiva Space conserva una miniatura e i dati di ogni scatto tolto (poche decine di KB a foto). Il documento lo chiama già "segnaposto leggero" e lo lega a una copia di sicurezza. Propongo di tenerlo sempre, anche quando non esiste una copia: almeno resta la traccia di cosa c'era.

**Una cosa da chiarire sulla scadenza.** La quarantena "con scadenza" non deve mai eliminare da sola allo scadere. La scadenza è solo un promemoria. Nel documento è così, ma conviene scriverlo in chiaro: niente viene mai eliminato da un timer.

### 3.3 Da un disco all'altro: cosa la verifica non vede

Lo schema deciso da Andrea (copia, verifica a più passaggi, conferma separata) è quello giusto ed è lo stesso del cinema. Restano quattro punti ciechi.

1. **Una sorgente che legge male.** Se il disco di partenza restituisce dati sbagliati senza segnalarlo, l'hash si calcola sui dati sbagliati e la copia risulta "verificata". Rimedio: quando Space ha già un hash di quel file da un inventario precedente, lo confronta. Se il contenuto è cambiato e la data di modifica no, il file si è rovinato da solo: Space lo segnala e non lo dà per buono. È un motivo in più per fare l'inventario con gli hash presto.
2. **Il ricontrollo prima di togliere gli originali** oggi è "rapido". Propongo che sia completo (rilettura dell'hash sulla destinazione) quando dalla copia è passato più di qualche giorno. È il momento in cui si decide di eliminare: vale il tempo che costa.
3. **File già rotti alla partenza.** La prova di apertura non verifica la copia, verifica la salute del file. Va presentata così: "12 file erano già illeggibili sul disco di partenza". Un file troncato non conta mai come copia valida.
4. **Formati deboli.** Su exFAT e sulle condivisioni di rete alcune garanzie non ci sono (rinomina che non sovrascrive, scrittura forzata). Proposta: nella prima versione si scrive solo su APFS e HFS+. exFAT si può leggere e usare come sorgente. La scrittura su NAS arriva dopo le prove su un NAS vero.

### 3.4 Doppioni: non fidarsi nemmeno dell'hash

Due file con lo stesso hash a 128 bit sono identici con una certezza enorme. Ma togliere un doppione è un'eliminazione, e il confronto diretto costa poco. **Proposta:** prima di mettere in quarantena un doppione, se le due copie sono collegate, Space le confronta byte per byte. Se una delle due è su un disco scollegato, il doppione non si toglie.

### 3.5 Video

Le regole scritte in 0quater e in 8bis.4 (punto 9) reggono. Un solo punto in più: "il girato non usato" si ricava leggendo librerie di Final Cut e progetti di DaVinci, e se quella lettura è incompleta si ripete l'errore della sezione 3.2. Per i video propongo di partire solo dai **file rigenerabili** (proxy, render, cache), dove un errore non costa niente, e di rimandare il girato non usato a quando la lettura dei progetti sarà stata provata su progetti veri.

### 3.6 Le proposte automatiche

Un errore in una proposta (un cliente scambiato per un altro, una giornata tagliata male per il fuso orario di un viaggio) non fa perdere file. Il rischio è che l'utente accetti duemila proposte senza guardarle. Tre contromisure:
- le proposte sono divise per certezza: **sicure**, **probabili**, **da guardare**;
- solo le sicure sono già spuntate;
- nell'anteprima Space mostra per prime le venti di cui è meno sicuro.

---

## 4. Cosa cambierei nel documento principale

| Dove | Oggi | Proposta |
|---|---|---|
| 3.1 | "Direttamente sulla sorgente" è sconsigliata | Riordino sul posto come modalità normale; "su copia" per provare o migrare |
| 3.1 | Clone APFS tra le tre modalità | Fuori dalla prima versione |
| 6 | Il ripristino annulla le operazioni una alla volta | Il ripristino è un piano nuovo verso l'istantanea (2.4) |
| 6 | "Scadenza" della quarantena | Esplicito: nessun timer elimina mai; allo svuotamento si rifanno i controlli |
| 6 | Certificato ASC MHL per ogni servizio | ~~Rimandato~~ **Resta, fin dalla prima versione che copia** (Andrea, 11 nov sera: vuole il livello di sicurezza del cinema; sezione 10) |
| 5.1 | "Il primo che funziona vince", più controllo di contraddizione | Aggiungere il conto dal lato degli export e le pile (3.2) |
| 5 | Strade A, B e C alla pari | A e B un gradino più gravi di C |
| 8 | Aggiornamento diretto del catalogo come opzione avanzata | Solo su una copia del catalogo, mai sull'originale |
| nuovo | — | Motore di scrittura unico e verificatore del piano (2.1, 2.2) |
| nuovo | — | Dischi protetti di default e lavori in corso esclusi (2.3) |
| nuovo | — | Porta zero (2.6), piano delle prove (2.7), scala delle uscite (6) |

---

## 5. Concorrenza e posizione

Riletta tutta la ricerca, il quadro è questo.

- **Chi cataloga** (Diem, NeoFinder, DriveShelf e simili) non riordina e non libera spazio. Diem ha dietro un nome forte e punta su abbonamento, account e AI che può passare dal cloud: il contrario di RawLine.
- **Chi riordina** (Hazel, Big Mean Folder Machine) lo fa a regole cieche, senza sapere cosa c'è nei file, senza annulla e senza verifica.
- **Chi sa dove sono le copie** (Tusk) non sa cosa è inutile.
- **Chi copia in modo verificato** (Hedge, Pomfort) lavora sul set, non sull'archivio.
- **Adobe** si sta muovendo: la vista Duplicati di Lightroom 15.4 è un primo passo, ed è uscita con un difetto che eliminava tutte le copie. È probabile che continui in questa direzione, ma solo dentro il catalogo.
- **Photo Mechanic Plus** è uscito dal mercato e ha lasciato utenti senza catalogo.

Tre conclusioni.

1. **Il posto libero c'è**, ed è l'incrocio di tre cose che nessuno ha insieme: capire il contenuto, liberare spazio con criterio fotografico, sicurezza da cinema.
2. **Quello che Space ha e gli altri non possono copiare in fretta è la famiglia.** Selects scrive stelle e scelte, e riconosce pile e panorami. Rename lascia il nome originale nel nome del file. Sono proprio i dati che servono all'abbinamento.
3. **Il rischio più grande per il prodotto non è un concorrente, è la larghezza.** Il documento oggi contiene riordino, libera spazio, catalogo, consolida, doppioni, integrità, video, sette modelli di archivio, amatori. Sono tre o quattro prodotti. Per un'app in cui ogni funzione che scrive moltiplica le prove da fare, la regola che propongo è: **larga in lettura, stretta in scrittura.** Le funzioni che leggono possono essere tante. Quelle che scrivono si aggiungono una alla volta, ognuna solo quando la precedente è provata.

---

## 6. La scala delle uscite

Ordine proposto, dal meno al più rischioso. Rispetta le priorità di Andrea: le fondamenta sotto, poi Riordino e Libera spazio. La differenza è che ognuna delle due esce prima nella sua metà che legge e poi in quella che scrive.

| Scalino | Cosa esce | Cosa scrive sui dischi dell'utente |
|---|---|---|
| **0** | Motore di scrittura, registro, verificatore, simulatore e prove. Nessuna interfaccia. | Solo dischi finti |
| **1** | **Space in sola lettura:** inventario del disco, mappa dello spazio, analisi delle cartelle disordinate, clienti sparsi, nomi degli export, doppioni identici, stima di "Libera spazio" con l'abbinamento, rapporto. | **Niente.** L'indice sta sul Mac |
| **2** | Riordino **su copia**, verso un disco di destinazione | Solo la destinazione |
| **3** | Riordino **sul posto**, con Storico e "Ripristina schema precedente" | Rinomine sul disco sbloccato |
| **4** | Libera spazio con la **quarantena** | Rinomine verso la quarantena |
| **5** | Svuotare la quarantena, la soffitta | L'unica eliminazione vera |
| **6** | Spostamento completo tra dischi, Consolida | Copie e quarantene su più dischi |
| **7** | Girato video non usato, copia aggiornata del catalogo, NAS | Da decidere allora |

Perché conviene partire dallo scalino 1:

- **dà già valore ad Andrea**: dove sta cosa, quanto spazio si può liberare, quali doppioni ci sono, con numeri veri al posto delle stime grezze della sezione 0ter;
- **lavora sul G-SPEED rispettando la regola**, perché legge e basta;
- **mette alla prova la parte più difficile da giudicare**, cioè le proposte e l'abbinamento, su 671.000 file veri, quando un errore non costa niente;
- chi prova la beta si fida di più di un'app che per prima cosa non tocca niente.

Ogni scalino successivo si prova prima sui dischi finti, poi su un disco di prova con una copia, poi su un disco secondario. Il G-SPEED viene per ultimo, quando lo decide Andrea.

---

## 7. Quello che nessun software risolve

Va detto a chi usa l'app, senza giri di parole.

- **Un disco che si rompe.** Space può accorgersi degli errori e fermarsi. Non può salvare un archivio che esiste in una copia sola.
- **Un disco che mente.** Alcuni dischi dichiarano di aver scritto e non l'hanno fatto. Nessun programma può scoprirlo. Per questo l'originale non si elimina mai subito.
- **L'utente che svuota la quarantena.** Space può fargli vedere bene cosa sta per fare. Non può decidere al suo posto.
- **Un RAID non è un backup.** Protegge da un disco rotto, non da un errore, da un furto o da un guasto dell'intero apparecchio.

Per questo Space non deve mai promettere "impossibile perdere dati". Deve promettere quello che può mantenere: niente si muove senza anteprima, tutto resta scritto, tutto si annulla fino all'ultimo gesto, e l'ultimo gesto è uno solo.

---

## 8. Rischi che restano, anche con tutto questo

| Rischio | Quanto è probabile | Cosa lo riduce | Cosa resta |
|---|---|---|---|
| Un RAW usato finisce tra i "non usati" | Medio, senza la regola degli export | Conto dal lato degli export, pile, stelle ed elaborazioni protette, quarantena, ricordo | L'utente che dichiara "senza RAW" un export che invece ce l'aveva |
| Collegamenti di Lightroom persi | Alto, se si dividono cartelle catalogate | XMP già aggiornati, cartelle intere di default, costo di ricollegamento, copia aggiornata del catalogo | Collezioni, cronologia e copie virtuali, se si reimporta invece di ricollegare |
| Copia "verificata" di un file già rovinato | Basso | Hash dell'inventario, prova di apertura | File rovinati prima del primo inventario |
| Registro perso o illeggibile | Basso | Due copie, formato di testo, compatibilità provata a ogni versione | Mac e disco persi insieme |
| Errore nel motore di scrittura | Basso, ma è il più grave | Motore piccolo, simulatore, andata e ritorno, uscita a scalini | Mai zero: per questo l'eliminazione vera è una sola e viene per ultima |
| Disco che cede durante un'operazione | Basso | Porta zero, stop al primo errore | Serve un backup |

---

## 9. Cosa serve da Andrea

In ordine d'importanza.

1. **Esiste una seconda copia dell'archivio del G-SPEED?** È la domanda 6 della sezione 10, ancora aperta, e pesa più di qualunque scelta sull'app. Se la risposta è no, il primo lavoro utile di Space è aiutare a farla (copia verificata verso un altro disco, senza toccare il G-SPEED).
2. **La scala delle uscite** (sezione 6): prima la versione in sola lettura.
3. **Riordino sul posto come modalità normale**, clone APFS fuori dalla prima versione (3.1).
4. **Ogni disco protetto finché non lo sblocchi**, e lavori in corso esclusi di default (2.3).
5. **Ripristino come piano verso l'istantanea** (2.4).
6. **Lightroom:** far scrivere gli XMP prima di qualunque riordino, e cartelle catalogate spostate intere di default (3.1).
7. **La soffitta** come terza strada di "Libera spazio" (3.2).

---

## 10. Aggiornamento dopo le risposte di Andrea (11 nov, sera)

### 10.1 L'archivio esiste solo sul G-SPEED

Andrea ha risposto che non c'è una seconda copia. Sul disco ci sono 17 TB (decimali) su 42. In questo momento al Mac non è collegato nessun altro disco, e il disco interno ha 168 GB liberi.

È il rischio più grande di tutto il quadro, e non dipende da Space: un guasto dell'apparecchio, un furto o un errore oggi porterebbero via tutto. Un RAID protegge da un disco rotto, non dal resto.

- **Non conviene aspettare Space.** La seconda copia va fatta con uno strumento che esiste già e che verifica quello che copia.
- Serve un disco da almeno 20 TB, meglio 24 o più per crescere.
- La copia legge soltanto dal G-SPEED, quindi rispetta la regola.
- **Da chiarire:** i vecchi dischi nominati nel catalogo (vedi sotto) esistono ancora con i dati dentro? Se sì, una parte dell'archivio una seconda copia ce l'ha già, anche se non verificata.

### 10.2 Il catalogo di Lightroom, guardato davvero

Ho letto **una copia** del catalogo attivo, fatta nella cartella di lavoro di questa sessione e poi cancellata. Il catalogo vero non è stato aperto né toccato: Lightroom era in uso.

| Dato | Valore |
|---|---|
| Foto nel catalogo | 170.837, di cui 413 copie virtuali |
| Cartelle | 735, sotto 194 cartelle radice |
| Scrittura automatica degli XMP | **attiva** (risponde alla domanda aperta 1) |
| RAW nel catalogo | 158.231 |
| RAW senza XMP accanto, secondo il catalogo | 41.068 |
| di cui sviluppati | almeno 1.498 (per molte foto il catalogo non ha ancora calcolato il dato) |

**La scoperta più importante: il catalogo punta quasi tutto a dischi che non sono collegati.**

| Disco scritto nel catalogo | File |
|---|---|
| Big Quadra | 43.120 |
| RAID BigDisk 2020 | 41.854 |
| RAID BigDisk 2018 | 34.239 |
| RAID BigDisk 2022 | 21.572 |
| RAID BigDisk 2024 | 8.793 |
| RAID BigDisk 2023 | 7.122 |
| Mac interno | 4.702 |
| **G-SPEED** | **4.336** |
| Altri (SSD vari) | circa 4.700 |

Solo il 2,5% dei file del catalogo punta al G-SPEED. Ho preso a caso 400 file che il catalogo dà su "RAID BigDisk 2024" e "RAID BigDisk 2020": **300 su 400 esistono sul G-SPEED, con lo stesso percorso interno**, sotto una cartella diversa. Quindi quei dischi sono stati travasati sul G-SPEED e il catalogo non è stato aggiornato. Il problema del ricollegamento non nascerà con Space: c'è già oggi.

### 10.3 Aggiornare il catalogo in automatico: si può fare

Andrea lo vuole, con la condizione giusta: prima una copia, si modifica quella, si controlla che funzioni.

**Com'è fatto il catalogo (verificato sulla copia).** È un database SQLite. I percorsi stanno in tre tabelle:
- la cartella radice, con il percorso completo sul disco;
- la cartella, con il percorso a partire dalla radice;
- il file, con nome, estensione e la cartella in cui sta.

Di conseguenza:
- **spostare una cartella intera** è una riga da cambiare;
- **spostare un file in un'altra cartella** è un campo da cambiare su quel file;
- **una cartella nuova** è una riga da aggiungere, con un numero preso dal contatore del catalogo;
- il catalogo rifiuta da solo due file con lo stesso nome nella stessa cartella.

**Come lo farebbe Space (proposta):**
1. Lightroom deve essere chiuso.
2. Space copia il catalogo. L'originale non viene mai aperto in scrittura.
3. Modifica solo le tre tabelle dei percorsi, nella copia.
4. Controlla la copia in tre modi: l'integrità del database; il numero di foto, cartelle, collezioni e sviluppi uguale a prima; **ogni file del catalogo esiste davvero sul disco al nuovo percorso**.
5. Andrea apre la copia in Lightroom e guarda che non ci siano foto mancanti. Solo allora diventa il catalogo di lavoro.
6. Il catalogo vecchio resta dov'è, intatto, per tornare indietro.

**Limiti onesti.**
- Adobe non documenta questa struttura e può cambiarla a ogni versione. Space deve riconoscere la versione del catalogo e rifiutarsi con quelle che non conosce.
- La prova vera è aprire la copia in Lightroom. Finché non l'abbiamo fatto su un catalogo di prova, resta **da provare**.
- Rinominare i file è più delicato che spostarli: nel catalogo il nome sta in più campi. Va per secondo.

**Un primo uso che non tocca niente.** Ricollegare il catalogo di oggi al G-SPEED: Space produce una copia del catalogo in cui i 166.000 file che puntano ai vecchi dischi puntano al G-SPEED, dove sono adesso. Non scrive niente sul G-SPEED e non modifica il catalogo originale. Sarebbe la prova ideale di questa funzione, e risolverebbe un problema che Andrea ha già.

Questo cambia la scala delle uscite: la copia aggiornata del catalogo era allo scalino 7. Propongo di portarne la prima metà, il ricollegamento senza spostare file, **subito dopo lo scalino 1**.

### 10.4 Copie sempre verificate, come nel cinema

Quello che Andrea ricordava sono i programmi di scarico del girato sul set: Hedge OffShoot, Pomfort Silverstack, ShotPut Pro. Fanno tutti la stessa cosa, ed è lo schema già deciso nella sezione 3.2 del documento principale: leggono l'originale calcolando un'impronta, scrivono, rileggono la copia dal disco e confrontano.

- **I programmi non si possono incorporare**: sono commerciali.
- **Il metodo e lo standard sì, e sono aperti.** L'impronta è xxHash, una libreria libera che si mette dentro l'app e lavora senza rete. Il certificato è **ASC MHL**, il formato della American Society of Cinematographers: un piccolo file accanto alle foto con l'impronta di ognuna e la storia delle verifiche.
- **Il vantaggio di usare lo standard:** una copia fatta da Space si può ricontrollare con i programmi del cinema, e Space può ricontrollare una copia fatta da loro. La sicurezza non dipende da Space.

Nella sezione 4 avevo proposto di rimandare il certificato MHL. Lo ritiro: resta fin dalla prima versione che copia. In Space **non esiste una copia non verificata**: non è un'opzione che si può spegnere.

### 10.5 I vecchi dischi esistono ancora (Andrea, 11 nov sera)

Andrea conferma che Big Quadra e i RAID BigDisk hanno ancora i dati dentro. Cambia il quadro in due modi.

**Una parte dell'archivio una seconda copia ce l'ha.** Non è verificata, è ferma al giorno del travaso e sta su dischi che hanno fino a otto anni. È meglio di niente, ma non è un backup.

**Dimensioni delle cartelle del G-SPEED** (lettura dell'11 nov sera, solo dimensioni):

| Cartella | TB | Sui vecchi dischi? |
|---|---|---|
| 2026 | 2,36 | **No di sicuro**: nel catalogo non esiste un disco per il 2026 |
| 2025 | 2,00 | **No di sicuro**: come sopra |
| 2023:2024 | 1,98 | Probabile (RAID BigDisk 2023 e 2024) |
| 2024 | 1,33 | Probabile (RAID BigDisk 2024) |
| 2022 | 1,94 | Probabile (RAID BigDisk 2022) |
| 2020:2021 | 1,97 | Probabile (RAID BigDisk 2020) |
| Namibia - NLT 2023 | 2,45 | Da controllare |
| Forever | 1,65 | Da controllare (nel catalogo c'è un disco FOREVER_ARCHIVIO_10TB) |
| SSDSandisk, GRIVEL, Patagonia, DRONE, altri | 1,17 | Da controllare |
| **Totale** | **16,85** | |

- **Almeno 4,4 TB (2025 e 2026) non hanno nessuna seconda copia.** Sono i lavori più recenti, quindi quelli con i clienti ancora attivi.
- "Probabile" vuol dire solo che esiste un disco con quel nome. Quello che è stato aggiunto o modificato dopo il travaso sul G-SPEED non c'è.

**Il rovescio: i vecchi dischi contengono cose che sul G-SPEED non ci sono.** Sul G-SPEED non esistono cartelle per gli anni prima del 2020. Nel catalogo però Big Quadra e RAID BigDisk 2018 contano circa 77.000 file. Quindi con ogni probabilità i lavori fino al 2019 esistono **solo** su quei due dischi vecchi **(da verificare collegandoli)**. L'archivio intero quindi non è il G-SPEED: è il G-SPEED più i vecchi dischi, e ogni pezzo ha il suo punto debole.

**Cosa conviene fare, in ordine.**
1. **I vecchi dischi non si svuotano e non si riusano**, finché non esiste una copia verificata di quello che contengono. Vanno tenuti scollegati e, se possibile, in un posto diverso dal G-SPEED.
2. **Subito, se c'è già un disco libero da 5 TB o più:** una copia verificata di 2025 e 2026.
3. **Appena possibile:** un disco da 20–24 TB o più per la copia verificata di tutto il G-SPEED.
4. **Confronto in sola lettura.** Collegando un vecchio disco alla volta si può leggere cosa contiene (nomi e dimensioni, poi le impronte) e dire con precisione: cosa è uguale al G-SPEED, cosa è diverso, cosa esiste solo lì. È lo scenario "Consolida" descritto da Andrea, nella sua metà che legge soltanto.

Questo conferma la scala delle uscite: la versione in sola lettura di Space, con il catalogo dei dischi e l'elenco delle **copie uniche**, è la prima cosa che serve ad Andrea, prima ancora del riordino.
