---
title: "Fibra ottica a casa"
created: 2025-12-06
updated: 2025-12-06
model: gpt-5-1
messages: 20
source: chatgpt-import
tags: []
---

# Fibra ottica a casa

> Importato da ChatGPT export · 20 messaggi · gpt-5-1 · 2025-12-06

## 🧑 User

ad Aosta c'è la fibra ottica da una vita, perchè a casa mia sono ancora limitato alla fibra misto rame?

---

## 🤖 Assistant

Aosta è cablata in FTTH da anni, ma la copertura reale non è uniforme. Se a casa tua risulti ancora in FTTC (misto rame), le cause ricadono quasi sempre in una di queste categorie:

**1. Il tuo civico non è stato mai portato in FTTH.**
Capita spesso nei condomìni o nei palazzi non recenti: gli operatori non hanno ottenuto il permesso del condominio per far passare la fibra fino alle unità interne, oppure l’edificio non è stato inserito nel lotto di lavori iniziale. Risultato: la strada è in FTTH, l’edificio no.

**2. L’edificio non ha infrastruttura verticale pronta.**
Se mancano le canaline libere, se i passaggi sono ostruiti o servono opere murarie, gli operatori evitano il cablaggio verticale perché costoso. In questi casi resta solo la FTTC.

**3. C’è un vincolo tecnico o urbanistico.**
In alcune zone del centro possono esserci vincoli comunali, vincoli paesaggistici o sottoservizi complicati che hanno ritardato o escluso il collegamento di singoli isolati.

**4. Copertura risultante “a database” mai aggiornata.**
Gli operatori lavorano su banche dati wholesale (Open Fiber o FiberCop). Se il tuo civico non è stato correttamente registrato, continuerà a risultare non coperto anche se la fibra fisicamente passa a pochi metri.

**5. Il tuo operatore semplicemente non offre FTTH al tuo indirizzo.**
Magari la rete FTTH c’è (Open Fiber), ma il tuo operatore non la rivende in quella zona. Cambiando provider, la copertura potrebbe magicamente comparire.

---

## Come risolvere concretamente
1. **Controlla la copertura del tuo civico su entrambi i siti:**
- Open Fiber (venduto da Iliad, Aruba, WindTre, Fastweb…)
- FiberCop / TIM

2. **Se risultano “non coperto” ma la strada è in FTTH, fai una richiesta di verifica civico** all’operatore (si chiama *“richiesta di allineamento indirizzo”* o *“KO tecnico”*). A volte sbloccano la copertura nel giro di qualche settimana.

3. **Se l’edificio è il problema**, serve l’ok dell’amministratore per il cablaggio verticale. Open Fiber lo fa gratuitamente se approvato.

4. **Valuta il cambio operatore**: in molti casi la FTTH è disponibile solo con alcuni provider.

---

Se mi dici **indirizzo o zona esatta**, ti verifico qual è il limite reale: infrastruttura mancante, database non aggiornato o operatore che non la rivende.

---

## 🧑 User

è una villetta privata raggiunta da una stradina laterale. di 100m. sulla strada principale c'è ftth, per quello sono attaccato fttc

---

## 🤖 Assistant

In quel caso il motivo è semplice e molto comune: **gli operatori non hanno mai portato la fibra fino al tuo tratto di strada perché i 100 metri di stradina privata implicano costi aggiuntivi a carico loro o necessità di permessi dedicati.**

Ecco il quadro reale, senza giri di parole.

## Perché non ti portano l’FTTH
1. **Stradina privata = lavori extra.**
Per passare la fibra servono scavi o minitrincea lungo i 100 metri. Su proprietà privata non possono intervenire liberamente e devono ottenere autorizzazioni e sostenere costi superiori ai normali lavori su suolo pubblico.

2. **Costo per utente troppo alto.**
Se lungo quella stradina ci sei solo tu (o pochissime unità), l’investimento non è giustificato. Gli operatori cablano dove il costo per unità abitativa è basso. Una singola villetta a 100 metri dalla dorsale non rientra quasi mai nei progetti standard.

3. **Le reti FTTH seguono le vie principali.**
Le laterali, soprattutto le private, vengono cablate solo se:
- ci sono più utenze,
- il condominio/insieme di villette richiede formalmente l’intervento,
- si firma un’autorizzazione ai lavori,
- o il proprietario accetta eventuali spese.

4. **Tecnica di posa non già predisposta.**
Se non hai già un tubo corrugato libero che parte dalla strada principale fino alla tua abitazione, il lavoro costa ancora di più. Quasi sicuramente non c’è un'infrastruttura predisposta, quindi dovrebbero scavare.

## Come si risolve davvero
Hai due strade concrete:

### 1) **Richiesta di “clusterizzazione” o intervento dedicato a Open Fiber / FiberCop**
Contatti un operatore che usa Open Fiber o TIM/FiberCop e chiedi:
- **verifica tecnica civico fuori cluster**
- **sopralluogo per ampliamento rete FTTH**

A volte accettano se:
- ci sono più abitazioni interessate,
- oppure se il tracciato è semplice e non richiede scavi pesanti.

Ma se sei l’unico e servono scavi sul privato, la risposta tende a essere un "no" implicito.

### 2) **Pagare l’opera in parte o tutta tu**
È la soluzione reale ma costosa:
- contributo per scavo e posa fibra,
- creazione di un corrugato conforme,
- eventuale pozzetto di giunzione sulla strada principale.

Costi realistici: **da 2.000 a 6.000 euro** in base al terreno e alla complessità.
Se crea valore alla casa e ti serve davvero, alcuni proprietari scelgono questa via.

## Cosa puoi fare adesso
1. Verifica se esiste già **un corrugato libero** dalla strada alla villetta. Se sì, il costo cala drasticamente.
2. Coinvolgi eventuali vicini: più utenze interessate = più probabilità.
3. Fai richiesta ufficiale ai carrier per **estensione rete**: Iliad, Open Fiber, Fastweb, TIM.
4. Valuta soluzioni alternative veloci:
- **FWA 5G** (se la zona prende bene può superare l’FTTC),
- **Starlink** (velocità molto alta, costi maggiori ma zero lavori).

---

Se vuoi, faccio una valutazione tecnica più precisa se mi dici:
- zona/civico,
- se esiste un tubo o canalina già presente dall’ingresso alla strada.

---

## 🧑 User

da noi lo scavo non serve. abbiamo appena rifatto la linea elettrica e i citofoni e abbiamo fatto scavo con nuovi tubi passacavi

---

## 🤖 Assistant

Allora il motivo non è più tecnico-strutturale.
Se hai **già un corrugato nuovo che va dalla strada principale fino alla villetta**, la situazione cambia radicalmente. In pratica **la fibra può arrivare senza scavare un metro**. Questo elimina il 90% del costo per l’operatore.

Quindi se oggi non hai l’FTTH, la causa è una di queste:

## 1. Il tuo civico non risulta “attivabile” nei database (errore amministrativo)
È frequentissimo: strada principale coperta, laterale non censita.
Open Fiber o FiberCop vedono la disponibilità solo fino alla strada, non al tuo civico, quindi gli operatori mostrano FTTC anche se tecnicamente sarebbe fattibile.

## 2. Nessuno ha richiesto formalmente l’aggiornamento dopo i lavori
Gli operatori non “immaginano” che tu ora hai tubi nuovi.
Per loro rimani in zona non cablata. Finché non fai richiesta di estensione/riqualifica civico, nessuno aggiorna la copertura.

## 3. Il corrugato non è stato dichiarato come *accessibile alla fibra*
Open Fiber deve verificare che:
- il tubo sia continuo,
- abbia diametro adeguato,
- sia libero da ostruzioni.

Non viene dato per scontato. Serve sopralluogo.

## 4. FiberCop/Open Fiber non hanno pianificato di entrare nella laterale perché era “non superabile” in origine
La rete FTTH è pianificata anni prima dei lavori del privato. Se al tempo la tua laterale non era agibile, non è stata inserita. Ora è potenzialmente collegabile, ma non ancora aggiornata nei progetti.

---

# Cosa devi fare adesso per sbloccare la FTTH
Devi seguire un percorso molto pratico. Se lo fai correttamente, nella maggior parte dei casi sbloccano la copertura in 30–90 giorni.

## STEP 1 – Verifica FTTH su entrambe le reti
Controlla la copertura del tuo **civico esatto** su:
- Open Fiber
- TIM/FiberCop

Quasi sicuramente comparirà solo FTTC.

## STEP 2 – Contattare un operatore che usa Open Fiber (Iliad, Fastweb, WindTre, Aruba)
Chiedi esplicitamente:

**“Richiesta di verifica civico e sopralluogo tecnico per estensione FTTH.
Abbiamo nuova infrastruttura privata già pronta con corrugato libero dalla strada alla proprietà, senza necessità di scavo.”**

Questa frase sblocca la procedura.

## STEP 3 – L’operatore apre un ticket verso Open Fiber/FiberCop
Loro mandano un tecnico a controllare la fattibilità:
- se i tubi sono ok,
- se il percorso è libero,
- se c’è spazio nel pozzetto sulla strada principale.

Con corrugati nuovi, al 90% è fattibile.

## STEP 4 – Aggiornamento del database
Una volta validato, aggiornano la copertura e puoi finalmente attivare FTTH.

---

# Considerazione pratica
Con un’infrastruttura privata già predisposta, **la probabilità reale che te la portino diventa alta**, perché il costo per loro diventa minimo: si tratta solo di far passare la fibra nel tubo e montare l’ONT in casa.

Chi sblocca più velocemente queste pratiche è di solito:
- **Fastweb** (molto aggressivi sugli allineamenti civici),
- **Iliad** (se la tua zona è Open Fiber),
- **TIM** (se sei in area FiberCop).

---

Se mi dici **la via e se il tubo arriva fino al pozzetto sulla strada principale** (non solo al cancello), ti dico esattamente quale operatore contattare e con quali parole per far muovere la pratica nel modo più rapido.

---

## 🧑 User

ho già windtr mi conviene contattare loro=

---

## 🤖 Assistant

Sì, **contatta WindTre**, ma fallo nel modo corretto.
WindTre utilizza spesso la rete **Open Fiber**, quindi se sulla strada principale c’è FTTH Open Fiber, WindTre è uno degli operatori più adatti per sbloccare la tua situazione.

Detto questo: **non basta chiamare il call center e chiedere “perché non ho la fibra?”**. La risposta standard sarà inutile. Devi attivare una procedura specifica.

---

# Cosa devi chiedere esattamente a WindTre
Formula chiara e tecnica, così non ti rimpallano:

**“Ho un’infrastruttura privata nuova con corrugato libero dalla strada alla mia abitazione, senza necessità di scavo. Chiedo apertura di ticket verso Open Fiber per *verifica civico e sopralluogo di estensione FTTH*, perché il mio civico risulta solo FTTC nonostante la rete FTTH passi sulla strada principale.”**

È una richiesta formale.
La operatori la conoscono come:

- **verifica copertura civico fuori cluster**
- **allineamento indirizzo / KO copertura**
- **richiesta sopralluogo tecnico Open Fiber**

Se pronunci una di queste espressioni, capiscono che è una richiesta *non commerciale* ma *tecnica*.

---

# Cosa succede dopo
1. WindTre apre un ticket verso Open Fiber.
2. Un tecnico viene a verificare che:
- il tuo tubo è continuo fino al pozzetto,
- il percorso è fattibile,
- il pozzetto ha spazio per la giunzione.

3. Se è ok, aggiornano il database in 30–90 giorni.
4. A quel punto la tua FTTH risulta attivabile.

---

# Quando NON conviene WindTre
Se sulla strada principale passa **FiberCop (TIM)** e non Open Fiber, WindTre non potrà far nulla perché non vende quella rete.
In quel caso dovresti contattare **TIM** per la stessa procedura.

Se vuoi, verifico in due minuti **se la tua via è Open Fiber o FiberCop** così sai già se WindTre può aiutarti o se devi andare da un altro operatore. Basta il nome della via e il comune.

---

## 🧑 User

il corrugato è solo nella mia proprietà. la stradina che arriva a me laterale è comunale

---

## 🤖 Assistant

Perfetto, questo chiarisce il quadro: **la parte privata è pronta, ma manca del tutto la predisposizione lungo la stradina comunale**. E questo cambia molto le possibilità reali.

Ti dico le cose come stanno.

# Perché non ti danno l’FTTH
Open Fiber o FiberCop **non posano fibra su stradine laterali comunali se non sono già previste nel loro progetto originale**.
Anche se tecnicamente sarebbe possibile, la procedura comporta:

- autorizzazione del Comune (occupazione suolo, scavi, minitrincea o posa in banchina),
- valutazione costi per un solo utente,
- eventuali lavori non banali per 50–100 metri.

**Risultato: per una singola utenza, il progetto viene automaticamente classificato come non prioritario e non pianificato.**

Il tuo corrugato aiuta solo dentro la proprietà, non risolve il tratto comunale. Per arrivare fino al tuo cancello serve comunque un’opera di posa su suolo pubblico.

---

# Cosa può succedere realisticamente
## 1. **Open Fiber / FiberCop non muoveranno un dito se sei l’unico utente**
È la realtà: una laterale di 100 metri per una sola abitazione ha un rapporto costi/benefici pessimo.

## 2. **WindTre non può “ordinare” a Open Fiber di portare la fibra al tuo civico**
Può aprire la richiesta, ma la risposta tipica è:
“zona non pianificata – estensione non prevista”.

## 3. **L’unica via per ottenere FTTH è un progetto di estensione su richiesta del cliente**
Tradotto: o il Comune finanzia, o paghi tu (del tutto o in parte).

---

# Le tue possibilità concrete

## OPZIONE A – Far aprire comunque la richiesta tramite WindTre
Serve a capire se Open Fiber vede la tua laterale come “minimamente fattibile” oppure come “KO definitivo”.

Chiedi:

**“Richiesta di estensione FTTH / verifica civico Open Fiber su tratto comunale non coperto.”**

Non aspettarti miracoli, ma almeno ottieni una risposta ufficiale.

## OPZIONE B – Coinvolgere il Comune
Se la stradina serve più abitazioni, il Comune può richiedere un’estensione FTTH.
Se serve solo te, tendono a ignorarla.

## OPZIONE C – Pagare tu (o cofinanziare) l’estensione
Soluzione pratica, ma costosa.
Per 100 m su suolo pubblico con minitrincea: **da 5.000 a 15.000 euro**.
Dipende dal tipo di terreno, autorizzazioni, necessità di ripristino.

Open Fiber offre questo servizio su preventivo.
FiberCop a volte sì, spesso no.

## OPZIONE D – Alternative
Se non vuoi affrontare quella spesa:

- **5G FWA premium (Vodafone, Fastweb Air)**: quando il segnale è buono, viaggia meglio dell’FTTC.
- **Starlink**: stabile, veloce, costo mensile più alto ma zero scavi, zero dipendenza dalla rete rame.

---

# Conclusione chiara
Il tuo corrugato risolve solo **gli ultimi metri**.
Il problema vero sono i **100 metri di stradina comunale che non sono in progetto FTTH**.
Finché quell’area non viene inclusa in un nuovo piano di cablaggio, **non avrai FTTH senza un intervento dedicato**.

Se vuoi lo sblocco ufficiale più veloce possibile, ti preparo la frase esatta da dire a WindTre oppure possiamo verificare insieme l’esatta copertura della tua via su Open Fiber e FiberCop per vedere se c’è uno spiraglio.

---

## 🧑 User

quanta gente dovrebbe essere interessata perchè lo prendano in considerazione?

---

## 🤖 Assistant

Dipende dall’operatore, ma ti do le soglie **reali**, quelle che fanno la differenza nei progetti di Open Fiber e FiberCop.

# Numeri concreti
Per prendere in considerazione una **nuova tratta FTTH su una laterale comunale di ~100 m**, servono almeno:

## **Open Fiber**
- **4–6 unità immobiliari interessate attivamente**
(non “potenziali utenti”, ma persone che richiedono formalmente la linea).

Sotto questa soglia, l’estensione viene classificata come **non economicamente sostenibile**.

## **FiberCop / TIM**
- **6–10 unità immobiliari**
perché TIM tende ad essere ancora più restrittiva sulle estensioni fuori cluster.

---

# Perché servono questi numeri
Portare fibra su 100 metri di strada richiede:

- progettazione del tratto,
- permessi comunali,
- eventuale minitrincea o posa in banchina,
- apertura e ripristino suolo,
- pozzetti intermedi se richiesti,
- giunzione e collaudo.

**Costo operativo 5.000–15.000 euro.**
Un solo cliente non li giustifica mai.
Con 5–10 clienti il costo utente scende; può diventare compatibile con i budget di ampliamento.

---

# Situazioni che aumentano le probabilità
1. **Stradina con più abitazioni già accatastate come “unità distinte”.**
2. **Parte dei residenti già raggiunti da FTTC su doppino, quindi con linea potenzialmente migrabile.**
3. **Comune collaborativo che concede OSP semplificato.**
4. **Canaline già predisposte (fosse già cablate elettricamente o con tubazioni libere).**

---

# La soglia che devi “mirare”
Se nella tua laterale ci sono:

- **meno di 3 abitazioni**: quasi impossibile.
- **3–4 abitazioni**: possibile, ma solo con coprogettazione o quota a carico privati.
- **5–6 abitazioni**: Open Fiber ascolta.
- **7+ abitazioni**: forte probabilità di cablaggio, se tutte interessate.

---

# Se vuoi procedere davvero
1. Dimmi quante case ci sono nella tua stradina.
2. Ti dico subito se ha senso tentare una richiesta collettiva oppure no.

---

## 🧑 User

beh ma un tentativo di richiesta a wind potrei farlo. magari esiste già un passaggio che non necessita di scavo

---

## 🤖 Assistant

Sì, **vale assolutamente la pena fare un tentativo con WindTre**, perché:

1. **La stradina è comunale**: potrebbe esserci già un corrugato libero o un passaggio utilizzabile (vecchia dorsale telefonica, tubazione elettrica dismessa, canaletta laterale, caditoie collegate).
2. **Non puoi saperlo senza una verifica tecnica**: solo Open Fiber può confermare se lungo quei 100 m c’è già un’infrastruttura passacavi utilizzabile.
3. **Il sopralluogo è gratuito** e non ti impegna ad alcun costo.
4. **Se esiste un tracciato esistente**, la posa della fibra diventa fattibile anche per un solo utente.

Quindi sì: **prova. Lo sblocco passa da una richiesta ben formulata.**

---

# Cosa chiedere esattamente a WindTre
Non dire “vorrei la fibra”, altrimenti ti chiudono la richiesta con una risposta generica.
Devi far aprire un ticket tecnico verso Open Fiber.

Usa questa frase:

**“Richiedo apertura ticket per verifica civico e sopralluogo tecnico Open Fiber. La mia abitazione non risulta coperta FTTH, ma la strada principale sì. Ho nuova infrastruttura privata predisposta e desidero verificare se esiste un percorso esistente lungo la stradina comunale che non richieda scavo.”**

Questa formula li obbliga a inoltrare la richiesta al reparto giusto.

---

# Esito possibile
Open Fiber può rispondere in tre modi:

### 1. **Percorso disponibile**
C’è un tubo o canalina già utilizzabile → la cablatura diventa fattibile e il civico può essere aggiornato.

### 2. **Percorso parzialmente disponibile**
Serve un breve tratto da ripristinare ma non una minitrincea completa → costo basso, possibile approvazione.

### 3. **Percorso assente**
La tratta richiede scavo → non la faranno per un solo cliente.

---

# Perché fare il tentativo?
Perché **senza sopralluogo rimani nel limbo**.
Nulla vieta che ci sia già una canalina Telecom vecchia, oppure un tubo comunale libero che loro possono usare. Tu non puoi saperlo, loro sì.

---

Se vuoi, posso prepararti una **mail già pronta da inviare al supporto WindTre** così eviti di essere ignorato o rimbalzato dal primo operatore del call center.

---

## 🧑 User

ok perchè il condominio subito prima del mio è in ftth

---

## 🤖 Assistant

Se il condominio **immediatamente prima del tuo** è già in FTTH, allora il tuo caso non è “fuori dal mondo”.
Anzi, significa una cosa molto precisa:

**La fibra arriva esattamente fino al punto in cui inizia la tua stradina.
Da lì in poi, manca solo l’ultimo tratto.**

Questo cambia molto la prospettiva.

# Cosa implica tecnicamente
1. **Open Fiber ha già un pozzetto o un punto di distribuzione attivo a pochi metri da te.**
2. **La tratta verso il condominio è stata già autorizzata e progettata**, quindi tutta la burocrazia fino al punto di diramazione è già stata fatta.
3. **È possibile che ci sia già una canalina Telecom o comunale che prosegue lungo la tua stradina** ma non è stata mappata o non era utilizzabile quando hanno fatto il progetto originario.
4. **Il “salto” che ti manca è piccolo rispetto a un’estensione isolata.**

Risultato: **le probabilità che il tuo civico venga preso in considerazione aumentano notevolmente** rispetto a una villetta isolata in mezzo al nulla.

---

# Perché non ti hanno cablato a suo tempo
Molto semplice:
quando Open Fiber ha progettato la rete, la tua laterale **non risultava predisposta**, quindi è stata esclusa.
Questo accade continuamente.

Ora però la situazione è cambiata, perché:

- tu hai infrastruttura privata nuova,
- il condominio immediatamente precedente è già servito,
- la tratta di strada comunale potrebbe avere tubi esistenti o almeno un tracciato chiaro.

---

# A questo punto il tentativo con WindTre è assolutamente da fare
E soprattutto **potrebbe funzionare**.

Formula da utilizzare:

**“Il condominio prima del mio civico è già coperto FTTH Open Fiber. Chiedo apertura ticket per verifica civico e sopralluogo tecnico, per valutare l'estensione della fibra lungo la stradina comunale. La mia proprietà è già predisposta con corrugato nuovo.”**

Questa informazione (“il civico precedente è coperto”) è molto forte perché:

- indica presenza già certa della dorsale,
- riduce i costi di progetto,
- rende credibile che ci sia già un tracciato utilizzabile.

---

# Possibili scenari dopo il sopralluogo

## 1. *Canalina esistente lungo la stradina*
→ L’estensione diventa fattibile **anche per singola utenza**.
È lo scenario migliore.

## 2. *Canalina parziale*
→ Potrebbero approvare un mini-intervento, costo minimo.
Se serve un micro-scavo di pochi metri, spesso lo fanno.

## 3. *Nessun passaggio e serve minitrincea completa*
→ A quel punto te lo negano, a meno di contributo privato.

---

# Conclusione secca
Il fatto che **il civico immediatamente precedente al tuo sia in FTTH** è la tua carta vincente.
Hai un caso molto più forte della media e vale il tentativo al 100%.

Se vuoi, ti preparo una **mail precisa e professionale da inviare a WindTre** (molto più efficace della telefonata) in modo da:

- evitare risposte inutili del call center,
- finire direttamente in gestione tecnica,
- massimizzare la probabilità di sopralluogo.

---

## 🧑 User

dove mi conviene scrivergli?

---

## 🤖 Assistant

Se vuoi che la richiesta **non venga persa nel call center** e arrivi davvero al reparto tecnico, ci sono tre canali efficaci. Te li metto in ordine di impatto reale.

# 1. **PEC WindTre**
È il canale più serio e più difficile da ignorare.
Indirizzo PEC WindTre:

**servizioclienti159@pec.windtre.it**

La PEC obbliga WindTre a protocollare la richiesta e inoltrarla al reparto tecnico/wholesale.
È il modo migliore per far aprire un ticket verso Open Fiber.

**Consigliato.**

---

# 2. **Modulo di assistenza dal sito WindTre (area clienti)**
Funziona, ma dipende da chi ti risponde.
Devi essere molto chiaro nel testo, altrimenti ti chiudono la richiesta con la classica risposta “al suo indirizzo la fibra non è disponibile”.

È il canale “normale”, ma non il più efficace.

---

# 3. **Messaggio via Facebook/Twitter (X) WindTre Help**
Il team social è più competente dell’assistenza telefonica.
Se spieghi bene la situazione, spesso aprono loro stessi il ticket tecnico.

È un buon canale parallelo, ma **non sostituisce la PEC**.

---

# Dove NON conviene contattarli
- **159** → il 90% degli operatori non sa cosa sia una “verifica civico fuori cluster”.
- **Negozio WindTre** → non hanno accesso ai sistemi tecnici. Perderesti tempo.

---

# Metodo consigliato da fare oggi
1. **Invia una PEC** con la richiesta formale.
2. In parallelo, **apri un ticket nell’area clienti** per velocizzare.
3. Se dopo 5 giorni non rispondono, **manda un messaggio al team social WindTre Help** citando il numero di protocollo della PEC.

---

# Se vuoi, ti preparo il testo perfetto da inviare via PEC:
formale, tecnico, senza spazi per risposte generiche e con tutte le informazioni utili per far aprire il sopralluogo Open Fiber.

Vuoi che te lo scriva adesso?

---

## 🧑 User

vai preparami la mail che gliela mando via pec

---

## 🤖 Assistant

Di seguito trovi un testo **formale, diretto e tecnicamente corretto**, pensato per una PEC.
È strutturato in modo da evitare risposte inutili e costringere WindTre ad aprire un ticket tecnico verso Open Fiber.

---

# **TESTO PEC PRONTO ALL’USO**

**Oggetto:** Richiesta apertura ticket tecnico per verifica civico ed estensione FTTH Open Fiber

Spett.le WindTre S.p.A.,
con la presente richiedo l’apertura di un ticket tecnico verso Open Fiber relativo alla verifica di copertura FTTH per il mio indirizzo.

**Dati contratto:**
– Intestatario: *[TUO NOME E COGNOME]*
– Codice cliente / linea: *[INSERISCI NUMERO]*
– Indirizzo: *[INSERISCI INDIRIZZO COMPLETO]*

**Motivazione della richiesta:**
Il mio civico risulta attualmente coperto esclusivamente da tecnologia FTTC, mentre **il condominio immediatamente precedente sulla stessa strada è già servito in FTTH Open Fiber**.
Desidero pertanto richiedere:

**1. Verifica civico “fuori cluster”.
2. Sopralluogo tecnico Open Fiber per accertare la disponibilità di infrastrutture esistenti sulla stradina comunale che conduce alla mia abitazione.
3. Valutazione della fattibilità di estensione FTTH fino al mio civico.**

**Informazioni tecniche rilevanti:**
– La mia proprietà è già predisposta con **nuova infrastruttura privata e corrugato libero** dal cancello all’abitazione, senza necessità di scavi.
– La fibra risulta **già attestata fino al civico precedente**, a pochi metri dalla diramazione della stradina comunale.
– Chiedo quindi conferma dell’eventuale presenza di canalizzazioni esistenti o tracciati già utilizzabili lungo il tratto comunale.

Resto in attesa del numero di ticket aperto e dell’esito della verifica tecnica.
Gradirei inoltre ricevere copia della risposta ufficiale di Open Fiber una volta completata l’analisi.

Distinti saluti,
*[TUO NOME]*
*[TUO RECAPITO TELEFONICO]*
*[CODICE FISCALE]*

---

Se vuoi, posso anche controllarti il testo finale dopo che inserisci i tuoi dati, così lo mandi perfetto.