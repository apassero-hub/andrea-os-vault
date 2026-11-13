# Conferme e annulla: azioni distruttive in RawLine Space

Ricerca UX dell'11 novembre 2026 su conferme, annulla, hold-to-confirm, type-to-confirm e anteprime di grandi cambiamenti, applicata al flusso previsto di RawLine Space: conferma dell'intenzione → laboratorio virtuale → anteprima prima/dopo → controllo finale → "Applica" tenuto premuto 5 s (più il nome della cartella da scrivere per le eliminazioni) → storico con annulla → quarantena con scadenza.

Legenda usata nel testo:
- **[UFFICIALE]**: linea guida pubblicata da Apple, W3C/WCAG, Google Material o documentazione ufficiale di un prodotto.
- **[RICERCA]**: studio o articolo di un istituto di ricerca UX (NN/g, studi accademici).
- **[OPINIONE]**: articolo di blog, post di sviluppatori, forum, o una mia deduzione.

Limite della ricerca: il budget di ricerche web si è esaurito prima di due approfondimenti (critiche documentate al type-to-confirm e documentazione Apple su Switch Control e VoiceOver per la pressione prolungata su macOS). Le parti su questi temi sono segnate **[OPINIONE]** o "da verificare".

---

## 1. Cosa dicono le linee guida

### Apple Human Interface Guidelines [UFFICIALE]
- **Alert solo per azioni rare e non annullabili.** Apple sconsiglia gli alert per azioni comuni e annullabili, anche quando sono distruttive: per un file cancellato non serve l'avviso, perché si può annullare. Per un'azione distruttiva *non comune* e *non annullabile* invece l'alert è importante. Testo: "Avoid displaying alerts for common, undoable actions, even when they're destructive" ([Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)).
- **I pulsanti devono dire cosa fanno.** Niente "OK", "Sì" o "No": servono verbi come "Erase", "Delete" o "Convert". Se c'è un'azione distruttiva serve sempre un "Cancel" (Annulla), che però *non* deve essere il pulsante predefinito. Se vuoi che la gente legga invece di premere Invio d'istinto, **non mettere nessun pulsante predefinito**.
- **Lo stile distruttivo (rosso) va usato solo per azioni che l'utente non ha scelto deliberatamente.** Nell'alert di "Svuota cestino" il pulsante non è rosso, perché esegue proprio l'intenzione dell'utente.
- **Il simbolo di attenzione va usato con parsimonia**, solo quando c'è una perdita di dati *inattesa*. Usato troppo spesso perde significato.
- Su macOS l'alert si chiude anche con Esc e ⌘-punto. Gli alert che si ripetono possono avere la casella "Non chiedere più".
- **Annulla e ripristina** ([Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)): far prevedere cosa verrà annullato (voci di menu tipo "Annulla spostamento") e **mostrare il risultato** dell'annulla, anche se riguarda una parte non visibile. Niente limiti inutili al numero di annullamenti. Si può annullare in blocco un gruppo di modifiche correlate. Su Mac l'annulla sta nel menu Composizione con ⌘Z e ⇧⌘Z.

### Nielsen Norman Group [RICERCA]
- **Le conferme vanno riservate alle conseguenze serie**, soprattutto se non annullabili. Se ce ne sono troppe, la gente smette di leggerle: "if you cry wolf too many times, people will stop paying attention" ([Confirmation Dialogs](https://www.nngroup.com/articles/confirmation-dialog/)).
- **Le conferme devono essere specifiche**: nome del file e numero di elementi coinvolti, non "Sei sicuro?". I pulsanti devono indicare il risultato ("Elimina file" e "Tieni file") e non avere un "Sì" predefinito.
- **Le conferme "pesanti"** (scrivere una parola, come nell'esempio di Mailchimp) vanno tenute per i casi più gravi e rari. Se diventano abituali, si eseguono anche loro in automatico.
- **L'annulla resta indispensabile anche con le conferme**: NN/g invita a "go to great lengths to provide undo". L'euristica n. 3 ([User control and freedom](https://www.nngroup.com/articles/user-control-and-freedom/)) chiede annulla e ripristina a più livelli, con un pulsante visibile e non solo una scorciatoia o un avviso che sparisce.

### Google Material Design [UFFICIALE, versioni 1 e 2]
- "Use dialogs sparingly because they are interruptive" ([Material 1, Dialogs](https://m1.material.io/components/dialogs.html)). Il dialogo di conferma ha un pulsante di conferma e uno di annullamento espliciti, e non deve aprire altri dialoghi.
- Le snackbar seguono un'azione e spesso offrono l'annulla. Il criterio, ripreso anche da molti design system, è: **annulla quando l'azione è reversibile, conferma modale quando non lo è**. Nota: le pagine di Material 3 si caricano via JavaScript e non sono state lette direttamente. Questa parte viene da Material 1 e 2 e da fonti secondarie.

### WCAG 2.2 (accessibilità) [UFFICIALE]
- **2.1.1 Tastiera (livello A):** tutto deve funzionare da tastiera "without requiring specific timings for individual keystrokes". La pagina esplicativa cita proprio il caso di un tasto che va tenuto premuto a lungo prima che venga registrato ([Understanding 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard)). **È il criterio più pertinente per un "tieni premuto 5 secondi".**
- **2.5.2 Annullamento del puntatore (A):** l'azione non deve partire alla pressione. Deve partire al rilascio, oppure si deve poter interrompere o annullare. La pagina esplicativa parla del long press che si attiva quando il dito viene alzato ([Understanding 2.5.2](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation)).
- **2.5.7 Movimenti di trascinamento (AA):** riguarda solo il trascinamento. Una pressione ferma non ricade qui ([Understanding 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements)). Lo "slide to confirm" invece sì.
- **2.2.1 Tempo regolabile (A):** riguarda i limiti di tempo imposti dal contenuto. La pagina non parla di pressione prolungata ([Understanding 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable)). Ricondurre un hold a 2.2.1 è un'interpretazione **[OPINIONE]**: il vincolo vero viene da 2.1.1.
- Le WCAG sono pensate per il web. Per un'app nativa macOS sono un riferimento di buona pratica, non un obbligo.

### Assuefazione alle conferme ("confirmation fatigue") [RICERCA]
- Studi con risonanza magnetica funzionale (Anderson et al., CHI 2015, e Frontiers in Psychology 2020) mostrano che **l'elaborazione visiva di un avviso cala già alla seconda esposizione** e cala ancora con le ripetizioni, mentre aumenta l'attività associata alla mente che vaga ([Frontiers 2020](https://www.frontiersin.org/articles/10.3389/fpsyg.2020.528079/full), [sintesi della presentazione di Vance](https://www.cl.cam.ac.uk/events/shb/2017/vance1.pdf)). Gli avvisi che **cambiano aspetto** ("polimorfici") resistono meglio all'assuefazione.
- Jef Raskin e Aza Raskin ([A List Apart](https://alistapart.com/article/neveruseawarning)): "Never use a warning when you mean undo." **[OPINIONE autorevole]**. Guido van Rossum ricorda che, presa in senso assoluto, la regola esagera: le conferme hanno ancora un ruolo ([Are confirmation dialogs harmful?](https://gvanrossum.github.io/artima/are-confirmation-dialogs-harmful.html)).

### Lamentele degli utenti nelle app che gestiscono file [OPINIONE, forum]
- **Conferme fastidiose:** nei forum di Dropbox gli utenti che cancellano migliaia di file chiedono di poter disattivare il popup o di avere un "applica a tutti", e segnalano che il popup torna anche dopo aver scelto "non chiedere più" ([Dropbox Forum](https://www.dropboxforum.com/t5/Delete-edit-and-organize/How-to-permanently-disable-confirmation-prompt-for-file-deletion/td-p/324254)).
- **Conferme insufficienti:** in Lightroom Classic la confusione tra "Rimuovi" e "Elimina dal disco" fa perdere foto. Alcuni utenti segnalano che nella versione 13 "Elimina dal disco" scavalca il Cestino, e c'è chi lamenta l'assenza di avvisi in certi percorsi ([Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/quot-delete-from-disk-quot-bypasses-trash-now/m-p/14189793/highlight/true), [Remove vs Delete](https://community.adobe.com/t5/lightroom-classic-discussions/remove-from-collection-vs-delete-from-disk-and-remove-from-lightroom/m-p/12068247)).
- **Finder, "Sostituisci" invece di "Unisci":** spostando una cartella su un'altra con lo stesso nome, la cartella di destinazione viene sostituita e il suo contenuto si perde. L'opzione "Unisci" compare solo trascinando con Opzione ([John Gruber](https://daringfireball.net/2005/04/replace), [MacMost](https://macmost.com/how-to-merge-two-folders-on-a-mac.html)).

### Errori famosi che hanno causato perdite (lezioni per Space)
| Caso | Cosa è successo | Lezione per Space |
|---|---|---|
| Falso allarme missilistico, Hawaii 2018 | Voci quasi identiche ("test" e "reale") e lo stesso testo di conferma per entrambe. La FCC aggiunse poi che l'operatore credeva l'attacco vero ([NPR](https://www.npr.org/sections/thetwo-way/2018/01/30/581853255/hawaii-missile-drill-stated-this-is-not-a-drill-resulting-in-false-alert), [ITPro](https://www.itpro.com/security/30288/how-a-poor-user-interface-design-caused-the-hawaii-missile-scare)) | Il testo della conferma deve cambiare in base a cosa si fa (prova o reale, sposta o elimina) e riportare numeri e nomi |
| VS Code, "Annulla tutte le modifiche" (2017) | Il comando eseguiva anche `git clean` e cancellava file non tracciati: un utente perse 3 mesi di lavoro ([Hackread](https://www.hackread.com/developer-deletes-work-files-with-visual-studio-code/)) | L'etichetta deve dire **tutto** quello che succede, cancellazioni comprese |
| Steam per Linux (2015) | `rm -rf "$STEAMROOT/"*` con la variabile vuota cancellava a partire dalla radice del disco, dischi esterni compresi ([The Register](https://www.theregister.com/2015/01/17/scary_code_of_the_week_steam_cleans_linux_pcs)) | Guardia nel codice: non operare mai fuori dalla radice scelta, rifiutare percorsi vuoti o di sistema |
| Windows 10, aggiornamento 1809 (2018) | La pulizia di cartelle "vuote e duplicate" cancellò cartelle che vuote non erano ([Redmond Mag](https://redmondmag.com/articles/2018/10/09/microsoft-lost-files-issue-windows-10.aspx)) | Ricontrollare lo stato reale **al momento di Applica**, non fidarsi dell'analisi fatta prima |
| GitLab (2017) | `rm -rf` sul server sbagliato. Di sei sistemi di backup ne funzionava di fatto uno ([postmortem ufficiale](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/)) | Mostrare in grande **quale disco o volume** si tocca e provare davvero il ripristino della quarantena |
| Citibank e Revlon (2020) | Circa 900 milioni di dollari inviati per errore, dopo un'interpretazione sbagliata delle caselle di un'interfaccia bancaria ([Al Jazeera](https://www.aljazeera.com/economy/2021/2/16/900m-gaffe-citigroup-cant-recoup-payout-to-revlon-judge-rules)) | Le opzioni oscure non sono una protezione. L'anteprima deve mostrare il **risultato**, non le impostazioni |

---

## 2. Hold-to-confirm: pro, contro, accessibilità e come farlo bene su Mac

### Pro [OPINIONE]
- Chiede un'intenzione sostenuta e quindi è più difficile da "cliccare via" di un dialogo. Si può interrompere a metà rilasciando il pulsante.
- Non apre un altro dialogo e resta nel contesto. Un sviluppatore riferisce di zero cancellazioni accidentali dopo averlo introdotto, contro decine di richieste di assistenza al mese con i dialoghi. È un'esperienza personale, non uno studio ([dev.to](https://dev.to/tomj/why-holding-buttons-is-superior-to-confirmation-dialogs-in-ux-design-1fic)).
- Durate suggerite dallo stesso autore: **1–1,5 s** per azioni reversibili, **3 s** per eliminazioni, fino a **5 s** per azioni critiche che toccano altre persone.

### Contro [OPINIONE e deduzioni]
- **Anche l'hold diventa un'abitudine.** Dopo dieci volte si tiene premuto senza guardare, come si fa con un dialogo. La ricerca sull'assuefazione vale per ogni rito ripetuto.
- **5 secondi sono tanti.** Sono alla pari delle azioni "critiche" del caso più estremo citato. Se Space chiede 5 s anche per spostamenti annullabili, la frizione è sproporzionata. E se il mouse scivola al secondo 4 si ricomincia da capo.
- **Non è un gesto standard su Mac.** Su macOS tenere premuto un pulsante di norma non fa nulla di speciale, quindi bisogna spiegarlo ogni volta (etichetta "Tieni premuto per applicare" e avanzamento visibile).
- **Accessibilità:**
  - *Tremori e forza ridotta*: tenere fermo il puntatore sul pulsante per 5 s è difficile. Se il cursore esce dal pulsante, la pressione si interrompe ([Axess Lab](https://axesslab.com/hand-tremors/), [IBM Carbon](https://medium.com/carbondesign/not-dragging-our-feet-a03ea57150e)).
  - *Tastiera*: un tasto tenuto premuto per un tempo stabilito va contro il criterio WCAG 2.1.1. Inoltre su macOS la ripetizione automatica dei tasti e i "Tasti lenti" interferiscono con la pressione prolungata (da verificare in pratica).
  - *VoiceOver*: l'attivazione (VO-Spazio) è un "press" istantaneo, che non può durare 5 secondi. Un progetto open source ha dovuto aggiungere un'azione accessibile perché il suo hold non si poteva attivare con VoiceOver ([e6code PR #138](https://github.com/Emikael/e6code/pull/138)). **[OPINIONE]**
  - *Switch Control e Controllo vocale*: un comando come "clic Applica" fa un clic singolo, non una pressione prolungata. Lo stesso problema è documentato per le CAPTCHA "Press & Hold" ([articolo](https://news.lavx.hu/article/the-press-and-hold-captcha-security-evolution-or-accessibility-nightmare)). **[OPINIONE]**

### Come farlo bene su Mac (se si tiene)
1. **Durata adeguata:** 1,5–2 s per Applica (che resta annullabile). Al massimo 3 s per lo svuotamento definitivo della quarantena. Durata modificabile in Impostazioni ("Conferma: tieni premuto / clic più conferma").
2. **Avanzamento visibile e continuo** (riempimento del pulsante più il testo "Tieni premuto… 1,2 s"). Con "Riduci movimento" attivo, niente animazioni vistose ma un contatore.
3. **Rilascio prima della fine = annulla**, con un messaggio chiaro ("Non applicato: rilasciato troppo presto"). A riempimento completo l'azione parte **al rilascio** (in linea con WCAG 2.5.2), oppure subito ma con annulla immediato.
4. **Mouse e trackpad:** l'area attiva resta valida anche se il puntatore si sposta di qualche punto (tolleranza per i tremori). Sul trackpad funziona sia il clic fisico tenuto sia il tocco tenuto, ma attenzione al "Force Click": il clic profondo non deve attivare altro.
5. **Tastiera:** con il pulsante a fuoco, Spazio o Invio tenuti premuti fanno lo stesso riempimento, ignorando la ripetizione automatica. Deve esistere sempre anche **un'alternativa senza tempi**, per esempio ⌘Invio che apre un foglio di conferma classico con il pulsante "Applica N modifiche" non predefinito.
6. **VoiceOver, Switch Control e Controllo vocale:** il pulsante espone un'azione accessibile ("Applica 1.248 modifiche"), cioè `accessibilityAction(named:)` in SwiftUI o un'azione personalizzata in AppKit. L'azione apre la conferma standard, così chi usa le tecnologie assistive ha la stessa protezione con un altro mezzo. È quanto suggerisce un ingegnere Apple per lo "swipe to confirm" ([Apple Developer Forums](https://developer.apple.com/forums/thread/729098)). L'etichetta letta da VoiceOver deve includere i numeri.
7. **Mai un hold da solo:** è un rito in più, non sostituisce l'annulla.

---

## 3. Type-to-confirm e alternative

### Come lo usano i grandi [UFFICIALE, documentazione dei prodotti]
- **GitHub:** per eliminare un repository servono tre passaggi: "voglio eliminarlo", "ho letto le conseguenze" e la digitazione del nome. In più, **alcuni repository si possono ripristinare entro 90 giorni** ([GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)). Anche il campione del type-to-confirm tiene una rete di sicurezza.
- **AWS S3:** per svuotare un bucket si scrive "permanently delete", per eliminarlo il nome del bucket ([AWS Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html)). Le vere protezioni però sono altrove: policy, MFA Delete, Object Lock.
- **Mailchimp** (citato da NN/g): scrivere "DELETE" prima di eliminare una lista.

### Pro e contro
- **Pro:** obbliga a leggere il nome di **cosa** si elimina, quindi intercetta l'errore "cartella sbagliata" meglio di un hold, che conferma solo la volontà. NN/g lo considera adatto ai casi rari e gravi. **[RICERCA]**
- **Contro [OPINIONE e deduzioni]:**
  - Se l'azione è frequente diventa un rito (NN/g: se diventa routine, diventa un altro clic automatico).
  - Con il copia-incolla del nome mostrato accanto l'effetto si perde in parte. Conviene non mostrare il nome in un campo copiabile vicino all'input, ma senza ostacolare chi detta il testo.
  - Nomi di cartelle lunghi o con caratteri speciali (date, accenti, spazi doppi) creano frizione e falsi errori. Conviene ignorare maiuscole e spazi ai bordi.
  - Smashing Magazine nota che disabilitare il pulsante finché il testo non corrisponde è in genere una cattiva pratica, accettabile qui solo perché la richiesta è chiara ([Smashing 2024](https://www.smashingmagazine.com/2024/09/how-manage-dangerous-actions-user-interfaces)).
  - Per l'accessibilità è buono: niente tempi, funziona con tastiera, VoiceOver e dettatura.

### Alternative e complementi
- **Annulla al posto della conferma** (Apple, NN/g e Raskin concordano): la protezione migliore per le azioni reversibili.
- **Cancellazione morbida e quarantena:** mettere da parte invece di eliminare. Esempi: il Cestino di macOS (svuotamento automatico dopo 30 giorni, *disattivato* per impostazione predefinita) e "Eliminati di recente" di Foto (30 giorni).
- **Conferma a due passaggi nel pulsante** (il pulsante cambia in "Conferma eliminazione") con un breve ritardo di 100–200 ms contro i doppi clic ([Smashing](https://www.smashingmagazine.com/2024/09/how-manage-dangerous-actions-user-interfaces)).
- **Conferma che chiede un dato invece di un nome:** per esempio "quanti file verranno messi in quarantena?". Funziona solo se l'utente ha davvero guardato il riepilogo. È sperimentale. **[OPINIONE]**
- **Avvisi "polimorfici":** la conferma cambia aspetto o contenuto in base al rischio, per ridurre l'assuefazione. **[RICERCA]**

---

## 4. Anteprime di grandi cambiamenti: come renderle leggibili

Riferimenti: `terraform plan`, il dry run di rsync, gli strumenti di confronto tra cartelle. Quello che segue è pratica di settore e opinione, salvo dove indicato.

1. **Prima i numeri, poi il dettaglio.** Una riga di sintesi come quella di Terraform ("3 da aggiungere, 1 da modificare, 2 da distruggere") è la cosa che la gente legge davvero ([Spacelift](https://spacelift.io/blog/terraform-plan)). Per Space: *Sposta 1.248 · Rinomina 312 · In quarantena 86 (412 GB) · Spazio liberato alla scadenza: 412 GB · Non toccati: 40.112*.
2. **Le distruzioni in evidenza e separate.** Un caso documentato: un team ha fatto fallire automaticamente ogni piano con eliminazioni non autorizzate esplicitamente ([war story](https://grokdatum.github.io/grokdevops-wiki/library/war-stories/the-close-call/the-terraform-plan-that-would-have-destroyed-prod)). Per Space: la sezione "Quarantena" va sempre aperta e in cima, mentre spostamenti e rinomine si possono comprimere.
3. **Simboli più colore, mai il colore da solo** (requisito di accessibilità): + nuovo, → spostato, ✎ rinominato, ⌫ quarantena, ⚠ conflitto.
4. **Raggruppare per significato**, non per percorso grezzo: per cliente o lavoro, per cartella di primo livello, per tipo (RAW, export, video, sidecar). Gruppi comprimibili con il totale (numero di file e GB) sulla riga del gruppo.
5. **Albero prima/dopo affiancato e sincronizzato:** selezionando un elemento a sinistra, si evidenzia la sua nuova posizione a destra. Ricerca e filtri: "solo quarantena", "solo conflitti", "solo file > 1 GB", "solo modificati negli ultimi 30 giorni".
6. **Segnalare le anomalie, non tutto.** Mettere in evidenza i file "sospetti": modificati di recente, senza copia altrove, usati in un catalogo, l'unico RAW di un export, nomi che si scontrano a destinazione (la lezione del "Sostituisci" del Finder). Così l'occhio va dove serve.
7. **Campioni visivi:** per le foto, miniature di un campione per gruppo. Un fotografo riconosce un servizio a colpo d'occhio più facilmente che da un percorso.
8. **Mostrare dove si tocca:** nome del volume, icona del disco e percorso radice ben visibili, con un avviso se il volume è di rete o esterno (la lezione di GitLab).
9. **Esportare il piano** (CSV o testo) e salvarlo nel giornale, così si può rileggere dopo e confrontare con quanto è stato eseguito.
10. **Il piano è congelato:** al momento di Applica si ricontrolla ogni file (esiste ancora, stessa dimensione e data). Se qualcosa è cambiato, ci si ferma e si mostra la differenza (la lezione di Windows 1809).
11. **Prova a secco esplicita:** il "laboratorio virtuale" è esattamente il dry run ed è un punto di forza da tenere.

---

## 5. Raccomandazioni concrete per RawLine Space

### Da tenere
- **Laboratorio virtuale e anteprima prima/dopo**: è la protezione più forte, perché fa vedere il risultato e non chiede solo "sei sicuro?".
- **Storico con annulla anche giorni dopo**: è in linea con Apple e NN/g. Va completato (vedi sotto).
- **Quarantena con scadenza** al posto della cancellazione immediata, coerente con la regola di sicurezza di Space (anteprima, conferma, giornale, annulla sempre).
- **Scrivere il nome**, ma solo nell'unico punto davvero irreversibile.

### Da cambiare
1. **Frizione proporzionata al rischio, non uguale per tutto.** Oggi il flusso somma fino a 6 barriere (intenzione, laboratorio, anteprima, controllo finale, hold di 5 s, nome). È proprio la ricetta dell'assuefazione: dopo qualche settimana si passa tutto in automatico. Proposta a tre livelli:

   | Livello | Azioni | Protezione |
   |---|---|---|
   | Reversibile | sposta, rinomina, crea cartelle | anteprima più pulsante specifico ("Applica 1.560 modifiche") più annulla (⌘Z e storico). Nessun hold |
   | Reversibile ma pesante | messa in quarantena | anteprima con la sezione quarantena aperta, più **hold di 1,5–2 s** oppure conferma a due passaggi, più annulla |
   | Irreversibile | svuotare la quarantena prima della scadenza, eliminazione definitiva | foglio di conferma specifico più **nome della cartella o del volume da scrivere**, nessun pulsante predefinito |

2. **Hold da 5 s a 1,5–2 s**, regolabile, con l'alternativa senza tempi (⌘Invio più foglio di conferma) e un'azione accessibile per VoiceOver, Switch Control e Controllo vocale. Mai come unico mezzo.
3. **Il nome da scrivere va spostato dall'atto di mettere in quarantena all'eliminazione definitiva.** Se la quarantena è annullabile, chiedere il nome lì è frizione senza beneficio. Va chiesto dove l'annulla finisce.
4. **Etichette con verbi e numeri:** "Metti in quarantena 86 file (412 GB)" e non "Applica". Il testo cambia tra spostamento, quarantena ed eliminazione (lezione delle Hawaii e di VS Code).
5. **Accorpare "conferma dell'intenzione" e "controllo finale"** nel riepilogo dell'anteprima, oppure rendere la conferma dell'intenzione una scelta del *tipo* di operazione e non un altro "sei sicuro?".
6. **Annulla a lungo termine fatto bene:**
   - Ogni operazione è un blocco annullabile per intero, con la possibilità di annullare anche solo una parte (singole cartelle).
   - Prima di annullare si mostra l'anteprima dell'annulla, perché dopo giorni i file possono essere stati toccati ancora. In caso di conflitti si chiede cosa fare e non si sovrascrive mai.
   - Dopo l'annulla si mostra il risultato (Apple: "Show the results of an undo or redo").
   - ⌘Z annulla l'ultima operazione con l'etichetta "Annulla spostamento di 1.248 file". Lo storico serve per le operazioni più vecchie.
7. **Quarantena trasparente:**
   - Avvisare **prima** della scadenza (per esempio 7 giorni e 1 giorno prima). Lo svuotamento a scadenza non deve mai essere silenzioso e deve essere rimandabile.
   - Dire chiaramente che **lo spazio si libera solo alla scadenza** se la quarantena sta sullo stesso disco, perché è una possibile delusione per un'app che promette di "liberare spazio". Si può offrire "Libera ora" come azione irreversibile del livello 3.
   - Durata predefinita: 30 giorni come Foto e il Cestino, regolabile.
8. **Guardie nel codice** (lezioni di Steam e Windows 1809): mai operare fuori dalla radice scelta, rifiutare percorsi vuoti o di sistema, ricontrollare lo stato al momento di Applica, nessuna sostituzione silenziosa nei conflitti di nome (unire o rinominare, mai "Sostituisci"). Va previsto anche un elenco di volumi protetti in sola lettura su cui Space non scrive mai.
9. **Provare il ripristino:** test automatici che mettono in quarantena e ripristinano davvero (lezione di GitLab: un backup mai provato non è un backup).
10. **Avvisi variabili:** l'avviso forte (simbolo di attenzione, colore) solo quando l'anteprima trova anomalie, come file recenti o senza copia. Se compare sempre, smette di funzionare.

---

## 6. Fonti

**Linee guida ufficiali**
- Apple HIG, Alerts: https://developer.apple.com/design/human-interface-guidelines/alerts
- Apple HIG, Undo and redo: https://developer.apple.com/design/human-interface-guidelines/undo-and-redo
- Apple Developer Forums, Swipe to confirm and accessibility: https://developer.apple.com/forums/thread/729098
- Material Design 1, Dialogs: https://m1.material.io/components/dialogs.html
- Material Design 2, Confirmation & acknowledgement (non leggibile via fetch): https://m2.material.io/design/communication/confirmation-acknowledgement.html
- W3C, Understanding 2.1.1 Keyboard: https://www.w3.org/WAI/WCAG22/Understanding/keyboard
- W3C, Understanding 2.5.2 Pointer Cancellation: https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation
- W3C, Understanding 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements
- W3C, Understanding 2.2.1 Timing Adjustable: https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable
- GitHub Docs, Deleting a repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository
- AWS Docs, Deleting a bucket: https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html

**Ricerca UX**
- NN/g, Confirmation Dialogs: https://www.nngroup.com/articles/confirmation-dialog/
- NN/g, User Control and Freedom: https://www.nngroup.com/articles/user-control-and-freedom/
- Anderson et al., Frontiers in Psychology 2020: https://www.frontiersin.org/articles/10.3389/fpsyg.2020.528079/full
- Vance, presentazione SHB 2017 (assuefazione, fMRI): https://www.cl.cam.ac.uk/events/shb/2017/vance1.pdf

**Articoli e opinioni**
- Smashing Magazine, How To Manage Dangerous Actions In User Interfaces (2024): https://www.smashingmagazine.com/2024/09/how-manage-dangerous-actions-user-interfaces
- A List Apart, Never Use a Warning When You Mean Undo: https://alistapart.com/article/neveruseawarning
- Guido van Rossum, Are confirmation dialogs harmful?: https://gvanrossum.github.io/artima/are-confirmation-dialogs-harmful.html
- dev.to, Why holding buttons is superior to confirmation dialogs: https://dev.to/tomj/why-holding-buttons-is-superior-to-confirmation-dialogs-in-ux-design-1fic
- e6code PR #138 (hold e tecnologie assistive): https://github.com/Emikael/e6code/pull/138
- IBM Carbon, Not dragging our feet: https://medium.com/carbondesign/not-dragging-our-feet-a03ea57150e
- Axess Lab, Hand tremors: https://axesslab.com/hand-tremors/
- Press-and-hold CAPTCHA e accessibilità: https://news.lavx.hu/article/the-press-and-hold-captcha-security-evolution-or-accessibility-nightmare
- Spacelift, Terraform plan: https://spacelift.io/blog/terraform-plan
- Il piano Terraform che avrebbe distrutto la produzione: https://grokdatum.github.io/grokdevops-wiki/library/war-stories/the-close-call/the-terraform-plan-that-would-have-destroyed-prod

**Casi reali e lamentele**
- NPR, falso allarme alle Hawaii: https://www.npr.org/sections/thetwo-way/2018/01/30/581853255/hawaii-missile-drill-stated-this-is-not-a-drill-resulting-in-false-alert
- ITPro, interfaccia del falso allarme alle Hawaii: https://www.itpro.com/security/30288/how-a-poor-user-interface-design-caused-the-hawaii-missile-scare
- Hackread, VS Code e tre mesi di lavoro persi: https://www.hackread.com/developer-deletes-work-files-with-visual-studio-code/
- The Register, Steam per Linux: https://www.theregister.com/2015/01/17/scary_code_of_the_week_steam_cleans_linux_pcs
- Redmond Mag, Windows 10 1809: https://redmondmag.com/articles/2018/10/09/microsoft-lost-files-issue-windows-10.aspx
- Postmortem GitLab: https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/
- Al Jazeera, Citibank e Revlon: https://www.aljazeera.com/economy/2021/2/16/900m-gaffe-citigroup-cant-recoup-payout-to-revlon-judge-rules
- Daring Fireball, Finder e "Sostituisci": https://daringfireball.net/2005/04/replace
- MacMost, unire cartelle su Mac: https://macmost.com/how-to-merge-two-folders-on-a-mac.html
- Adobe Community, Lightroom "Delete from Disk" scavalca il Cestino: https://community.adobe.com/t5/lightroom-classic-discussions/quot-delete-from-disk-quot-bypasses-trash-now/m-p/14189793/highlight/true
- Adobe Community, Remove vs Delete from Disk: https://community.adobe.com/t5/lightroom-classic-discussions/remove-from-collection-vs-delete-from-disk-and-remove-from-lightroom/m-p/12068247
- Dropbox Forum, disattivare la conferma di eliminazione: https://www.dropboxforum.com/t5/Delete-edit-and-organize/How-to-permanently-disable-confirmation-prompt-for-file-deletion/td-p/324254
