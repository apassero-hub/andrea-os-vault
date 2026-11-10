# Budget 2027: revisione dei file di Ale

Revisione del 10 novembre 2026 dei due file di Ale. Non li ho modificati.

- `Gran_Paradiso_Trail_2027_Budget_3_Scenari.xlsx`: scenari da 300, 400 e 500 iscritti, con parametri e ricavi.
- `Gran_Paradiso_Trail_2027_Dettaglio_Analitico_Costi.xlsx`: le voci di costo per lo scenario da 500 iscritti.

## In breve

I conti sono fatti bene. Le formule non hanno errori e i totali dei due file coincidono: 38.520 € di costi operativi, 42.372 € con gli imprevisti. Gli sponsor sono a zero, che è un'impostazione corretta.

Restano tre tipi di problemi:

1. **Il file non coincide con quello che abbiamo già presentato** su data, nomi e percorso.
2. **Mancano alcune voci di costo**, e altre sono probabilmente basse.
3. **I due file sono separati**, quindi se cambia una cifra nel dettaglio gli scenari non si aggiornano.

Le correzioni sono applicate nella versione 2 del file, [budget/Cogne_Trail_2027_Budget_v2.xlsx](budget/Cogne_Trail_2027_Budget_v2.xlsx). Con la v2 il fabbisogno da coprire passa da **15.000–19.000 €** a circa **19.000–22.500 €**. La richiesta da 15.000 € a CAS ne coprirebbe circa tre quarti.

## Cosa torna

| Verifica | Esito |
|---|---|
| Ricavi a 500 iscritti: 100 early + 300 standard + 100 ultima fascia = 27.500 € | Torna. La media è 55 € a iscritto |
| Iscritti standard: 140, 210 e 300, come dice la nota | Torna. A 500 la quota standard sale al 75%, contro il 70% degli altri scenari: probabilmente è voluto, ma va confermato |
| Totale del dettaglio uguale al totale degli scenari | Torna: 38.520 € in tutti e due |
| Ristori della 47 km: 1.400 € + 150 € = 1.550 €, con le righe R1–R4 a zero come promemoria | Torna, ed è segnalato bene |
| Costi variabili (maglie, medaglie, pasto, ristori) proporzionati agli iscritti | Torna |
| Imprevisti al 10% sui costi operativi | Torna |

## 1. Le differenze con il progetto

| Punto | File di Ale | Sito e PDF partner | Da decidere |
|---|---|---|---|
| **Giorno di gara** | Sabato 12 village e ritiro pettorali, **domenica 13 le due gare** | Venerdì 11 village, **sabato 12 le gare**, domenica corsa dei bambini | È la differenza più importante. Sito, deck e proposta CAS dicono tutti "sabato 12 giugno". DATA.md sceglie il sabato perché chi corre si ferma a dormire e il paese lavora tutto il weekend. |
| **Nome della gara** | Gran Paradiso Trail | Cogne Trail | Allineare il nome |
| **Nome della 28 km** | Colonna 28K | Miniere 28 | Allineare il nome |
| **Percorso della 47 km** | Ristoro R4 a Bardoney, km 38 | Profilo con il Lago delle Loie al km 39,5, Bardoney non compare | Serve la traccia GPX definitiva di Ale, per aggiornare profili e luoghi su sito e PDF |
| **Rifugio Sogno** | Ristoro R3 al km 30, **unico cancello orario** | Sul percorso | LoveVdA lo dà come temporaneamente chiuso (vedi PARTNER.md). Se lo è, il cancello e il ristoro vanno spostati o riorganizzati, magari con un trasporto in quota |
| **Corsa dei bambini e cena del paese** | Non presenti | Nel programma del weekend | Aggiungerle al budget o toglierle dal programma |

## 2. Voci mancanti o da rivedere

### Mancano

| Voce | Stima | Perché |
|---|---|---|
| Commissioni della piattaforma d'iscrizione | circa 4% degli incassi, cioè 650–1.100 € | Il file le mette a zero |
| Bagni chimici al village | circa 800 € | Con 500 atleti più pubblico, 6 bagni per due giorni |
| Rientro dei ritirati e trasporti in quota | circa 500 € | Chi si ritira a Grauson o al Sogno deve scendere. Oggi c'è solo la logistica di Colonna |
| Corsa dei bambini | circa 300 € | È nel programma |
| SIAE e musica per la festa | circa 300 € | Se c'è musica |
| Tasse FIDAL o di approvazione della gara | circa 300 € | Da verificare con FIDAL VdA |
| Volontari in più | circa 360 € (30 cestini) | 60 volontari sembrano pochi per 7 ristori, i controlli, la segnaletica e il village. Una stima più realistica è 80–100 |

In totale sono **circa 2.500–3.000 € in più**.

### Probabilmente basse

- **Soccorso sanitario (3.000 €).** Due gare in quota su percorsi diversi richiedono più ambulanze o presidi con medico, più il Soccorso Alpino. È la prima voce da far quotare.
- **Cronometraggio (2.300 €).** Va bene per il servizio base. I rilevamenti intermedi in quota (Colonna, Grauson, Sogno e il passo), il chip e la gestione delle iscrizioni potrebbero costare di più. Se faremo il Tratto del Ferro di CAS, serve comunque un punto di rilevamento a Colonna.
- **Imprevisti (10%).** Per una prima edizione con molti "zero non confermati" (piazza, transenne, permessi, foto degli atleti) conviene il **15%**.

### Dove si può risparmiare

- **Sito (1.950 €).** Il sito c'è già: l'ha fatto Andrea, su Cloudflare, con un costo di hosting quasi nullo. Restano le traduzioni in francese e inglese e il dominio. Si può scendere a circa 300–500 €.
- **Foto e video (3.300 €).** Andrea è fotografo e videomaker. Va deciso se è un lavoro pagato o un contributo in natura. Il racconto foto e video è anche una delle cose promesse a CAS.
- **Medaglie (3.000 €).** Se CAS fornisce l'acciaio per l'oggetto dei finisher, la voce si riduce alla sola lavorazione.

## 3. Come è costruito il file

- **I due file sono scollegati.** Il foglio "Costi dettagliati" ha le cifre scritte a mano (7.100, 2.300…) invece di prenderle dal dettaglio. Se Ale cambia una voce nel dettaglio, gli scenari non lo vedono. Meglio un solo file, con il dettaglio come foglio e gli scenari che sommano dal dettaglio.
- **I costi variabili sono calcolati in proporzione allo scenario da 500.** Funziona, ma si legge meglio "costo a persona × iscritti", con il costo a persona nei parametri: 12 € la maglia, 10 € il pasto, 6 € la medaglia.
- **Manca una riga per sponsor e contributi pubblici per livello.** Il campo esiste ma è un numero unico a zero. Con righe separate (title partner, partner minori, Regione, Comune in natura) si vede subito quanto copre ogni accordo.
- **Il costo dei pettorali gratuiti non c'è.** Secondo i numeri di Ale, ogni atleta costa circa 32–36 € tra maglia, pasto, medaglia e ristori. I 50 pettorali gratuiti della Squadra Cogne valgono quindi circa **1.700 €** di costi in più, se si aggiungono ai paganti. Se invece occupano posti che sarebbero stati venduti, valgono circa 2.750 € di incassi mancati.
- **Fiscalità.** Per una ASD gli incassi da sponsor hanno una disciplina IVA particolare, e le iscrizioni possono essere o non essere commerciali. È da chiedere al commercialista prima di firmare con CAS. Nella proposta ho già scritto "IVA esclusa".

## Il file v2

`budget/Cogne_Trail_2027_Budget_v2.xlsx` si rigenera con `python3 tools/budget_v2.py` (serve openpyxl). È un solo file, con questi fogli:

- **Leggimi:** come si usa, cosa cambia rispetto alla v1, cosa resta da decidere con Ale.
- **Quadro scenari:** incassi, costi, imprevisti, fabbisogno, saldo con gli sponsor confermati e con quelli obiettivo, costo per atleta, confronto con la v1.
- **Parametri:** iscritti, prezzi, commissioni, imprevisti, volontari, pettorali gratuiti per gli sponsor, Piano B.
- **Dettaglio costi:** ogni voce ha un **Tipo** (Fisso, Per atleta, Proporzionale…) che decide come cambia tra gli scenari. Le righe nuove sono segnate "Nuova v2".
- **Ricavi iscrizioni:** la stessa logica della v1 (early, standard, ultima fascia), applicata ai soli paganti, meno le commissioni.
- **Sponsor e contributi:** obiettivo e confermato tenuti separati. Nel saldo principale entrano solo i confermati, come voleva Ale.
- **Riepilogo capitoli:** totale per capitolo e peso sul totale.

Ho verificato il file calcolando tutte le 346 formule: nessun errore. Gli incassi coincidono con la v1 al centesimo. Alzando i pettorali gratuiti a 50 gli incassi a 500 iscritti scendono di 2.841 €, e attivando il Piano B si aggiungono 600 €.

### Risultati v2

| | 300 iscritti | 400 iscritti | 500 iscritti |
|---|---|---|---|
| Incassi netti | 15.571 € | 21.053 € | 26.400 € |
| Costi operativi | 33.090 € | 36.400 € | 39.710 € |
| Imprevisti 15% | 4.964 € | 5.460 € | 5.957 € |
| **Totale costi** | **38.054 €** | **41.860 €** | **45.667 €** |
| **Da coprire** | **22.482 €** | **20.807 €** | **19.267 €** |
| *Nella v1 di Ale* | *18.804 €* | *16.768 €* | *14.872 €* |
| Con CAS a 15.000 € | −7.482 € | −5.807 € | −4.267 € |

Un pettorale gratuito in più costa circa **33 €** di costi variabili (maglia, pasto, medaglia, ristori).

## Stima fatta prima della v2

Questa era la stima iniziale, prima di costruire il file, quando il risparmio sul sito non era ancora incluso. Ipotesi: voci mancanti per circa 2.560 €, imprevisti al 15%, commissioni del 4% sugli incassi.

| | 300 iscritti | 400 iscritti | 500 iscritti |
|---|---|---|---|
| Costi operativi di Ale | 31.840 € | 35.180 € | 38.520 € |
| + voci mancanti | 2.560 € | 2.560 € | 2.560 € |
| + imprevisti 15% | 5.160 € | 5.661 € | 6.162 € |
| **Totale costi** | **39.560 €** | **43.401 €** | **47.242 €** |
| Incassi netti (−4%) | 15.571 € | 21.053 € | 26.400 € |
| **Da coprire** | **23.989 €** | **22.348 €** | **20.842 €** |
| *Nel file di Ale* | *18.804 €* | *16.768 €* | *14.872 €* |

**Cosa vuol dire per gli sponsor.** Con la v2 e CAS a 15.000 € resta da coprire circa **4.000–7.500 €**, da trovare tra contributo della Regione, Comune, partner tecnici e Amici di Cogne. Se CAS sceglie il livello da 7.000 €, ne mancano 14.000–17.000.

## Domande per Ale

1. Gare di sabato o di domenica? Va deciso prima di tutto il resto.
2. Qual è la traccia definitiva della 47 km, e passa da Bardoney o dal Lago delle Loie?
3. Il Rifugio Sogno è aperto? Se no, dove va il cancello orario?
4. Chi è "il Presidente" nel file? Il budget è dell'ASD (Sci Club?) o di un nuovo soggetto?
5. Teniamo nel budget la corsa dei bambini e la cena del paese?
6. Quanti volontari servono davvero, ristoro per ristoro?
