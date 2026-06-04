---
title: "Problema spegnimento Elinchrom"
created: 2025-09-24
updated: 2025-09-25
model: gpt-5
messages: 8
source: chatgpt-import
tags: []
---

# Problema spegnimento Elinchrom

> Importato da ChatGPT export · 8 messaggi · gpt-5 · 2025-09-24

## 🧑 User

perchè l'elinchrom elb1200 se tengo premuto per spegnerlo si riavvia?

---

## 🤖 Assistant

Il comportamento che descrivi sull’Elinchrom ELB 1200 non è “normale” nel senso stretto: se tieni premuto il tasto **ON/OFF** dovrebbe spegnersi e restare spento, non riaccendersi da solo. Ci sono alcune possibili cause note:

1. **Durata della pressione del tasto**
- Sull’ELB 1200 il pulsante va tenuto premuto in modo prolungato (circa 3 secondi). Se il rilascio è troppo rapido o avviene in sincronia con il “beep” di conferma, può capitare che il sistema interpreti l’input come un riavvio invece che come uno spegnimento completo.

2. **Firmware / bug del sistema**
- In alcuni modelli con firmware non aggiornato, c’è un glitch che può causare il “reboot” invece dello spegnimento. Elinchrom ha rilasciato update firmware che correggono problemi simili.

3. **Problema di contatti nel pulsante**
- Se il tasto power è leggermente usurato o ha un falso contatto, la pressione prolungata può venire letta come una sequenza di due pressioni (quindi: spegnimento + accensione).

4. **Batteria difettosa o mal collegata**
- Una batteria con contatti sporchi/allentati o una cella che “droppa” tensione può causare riavvii automatici invece di uno spegnimento stabile.

👉 Ti consiglio di:
- Verificare se hai l’ultima versione firmware (si aggiorna via computer con il software Elinchrom Updater).
- Fare una prova con un’altra batteria, se disponibile.
- Tenere premuto il tasto almeno 3–4 secondi e rilasciarlo solo quando vedi che lo schermo si spegne del tutto.
- Se il problema persiste, potrebbe essere un guasto del pulsante power o della scheda di controllo → in quel caso serve assistenza tecnica.

Vuoi che ti recupero il link ufficiale al firmware e al manuale aggiornato ELB1200, così puoi verificare subito se rientri nel caso del bug?

---

## 🧑 User

mi fai una ricerca approfondita sul problema? la batteria è appena stata ricaricata prima non lo faceva. firmware aggiornato. il problema lo da solo in spegnimento, non in accensione. accendersi si accende normalmente

---

## 🤖 Assistant

Chiaro: non è un comportamento previsto. Con firmware già aggiornato e batteria appena carica, il “riavvio allo spegnimento” è tipicamente dovuto a uno di questi fattori:

1) Tasto power che “rimbalza” (debounce) o resta parzialmente premuto
Il long-press viene letto come due pressioni: spegni + riaccendi. Succede quando il micro-switch è usurato o sporco. Test rapido: spegni premendo con decisione e rilascia in modo netto; prova anche con guanto/punta morbida per evitare pressioni laterali. Se migliora, è quasi certamente il pulsante/front-panel. La funzione del tasto è documentata nel manuale come “Unit On/Off”. cite

2) Stato anomalo della batteria/pack al momento dell’arresto
Se la logica della batteria vede un transiente al power-down, il pack può riavviarsi. Fai due reset “puliti”:
- Reset batteria: tieni premuto il pulsante RESET sulla batteria ~6 s finché i 4 LED si spengono, poi riattivala (procedura ufficiale). cite
- Power cycle del pack: rimuovi la batteria, tieni premuto ON/OFF 10 s (scarica residui), reinserisci la batteria e riprova.

3) Periferiche/condizioni che forzano il wake
Scollega tutto e prova lo spegnimento “nudo”: niente teste, niente cavi sync, niente Dock di rete. Alcuni accessori (Dock/USB) possono alterare il comportamento alimentazione, e il Dock alimenta il pack in modo diverso dalla batteria. cite

4) Bug lato firmware già risolti vs. impostazioni correnti
Elinchrom ha corretto bug legati ai controlli e all’ergonomia in varie release (2.0/2.1). Se sei certo di avere l’ultima, escludiamo questo. In ogni caso verifica via Updater ufficiale. cite

Procedura consigliata (in ordine):

- Prova a spegnere con pressione netta 3–4 s, rilascio “secco”.
- Scollega teste/cavi/Dock e riprova. cite
- Esegui reset batteria (6 s sul tasto RESET) e poi power cycle del pack. cite
- Reinstalla/riconferma il firmware con l’Updater (anche stessa versione). cite
- Se persiste: è molto probabilmente un problema del micro-switch o della scheda frontale (hardware). A quel punto, assistenza.

Contatti utili per assistenza in Italia / ufficiale:
- Apromastore (procedura di invio in riparazione; centro storico per Elinchrom in IT). cite
- Supporto Elinchrom (puoi scrivere loro e ti indirizzano al distributore locale). cite

Se vuoi, ti preparo una checklist stampabile con i passaggi e un breve video-script per documentare il difetto da mandare all’assistenza.

---

## 🧑 User

resettata la batteria e il pack, sembrava a posto e poi dopo 5 minuti si è riacceso

---

## 🤖 Assistant

Questo dettaglio cambia le carte in tavola: se il pack, dopo un reset completo, resta spento e **poi si riaccende da solo senza che tu tocchi nulla**, non è più un problema di tasto, ma di **gestione logica della batteria o della scheda madre del pack**.

Ecco i punti chiave:

1. **Il pulsante non c’entra**
– Se si riaccende da solo a distanza di minuti, significa che il comando ON/OFF non viene interpretato male in quel momento, ma che qualcosa alimenta di nuovo la logica.

2. **Possibili cause tecniche**
- **BMS (Battery Management System) difettoso**: la scheda della batteria può inviare un “wake” al pack quando rileva anomalie di tensione o ribilanciamento celle.
- **Circuito di standby del pack**: potrebbe esserci un guasto sulla scheda di alimentazione interna che non interrompe davvero il flusso e riporta il sistema in ON.
- **Bug raro di firmware**: anche se aggiornato, può succedere che il firmware resti “bloccato” in un ciclo (ma in genere lo fa subito, non dopo minuti).

3. **Test per restringere il problema**
- Lascia il pack spento **senza batteria inserita** → se resta spento, la logica è nella batteria.
- Lascia il pack spento **con batteria inserita ma non caricata nel Dock** → se si riaccende, la batteria è la causa.
- Prova con un’altra batteria, se riesci a fartene prestare una → test definitivo per capire se il problema è nel pack o nella batteria.

4. **Cosa significa**
– Se il difetto segue la batteria: probabilmente è il BMS interno (ricellaggio non basta, serve sostituire la scheda di gestione).
– Se il difetto resta sul pack con qualsiasi batteria: guasto della scheda di controllo del generatore (front panel board o main board).

👉 In entrambi i casi non è una cosa che puoi risolvere da solo: serve assistenza tecnica, perché si tratta di elettronica interna.

Vuoi che ti cerchi i **centri che riparano specificamente ELB 1200 in Italia/Europa** e ti preparo già una mail da inviare con la descrizione del sintomo e il test che hai fatto (reset + riaccensione autonoma)?

---

## 🧑 User

cercami chi può fare assistenza all'unità

---

## 🤖 Assistant

Ecco i principali riferimenti per l’assistenza tecnica su un generatore Elinchrom ELB 1200 in Italia, con indicazioni provenienti da fonti ufficiali:

| Centro / località | Motivo per cui è rilevante | Contatti e informazioni utili |
|---|---|---|
| **Apromastore srl – Rho (MI)** | Apromastore è l’importatore esclusivo per l’Italia dei prodotti Elinchrom e l’unico centro di riparazione autorizzato per i flash Elinchrom. Sul loro blog specificano che **gestiscono le revisioni e le riparazioni di tutti i flash Elinchrom, anche fuori garanzia**. Nella stessa guida indicano di preparare un foglio con i propri recapiti, l’indirizzo di spedizione e la descrizione del guasto, da inserire nel pacco. | **Laboratorio riparazioni:** Via Magenta 77/13E, 20017 Rho (MI). **Tel.** 0238011138. Per la spedizione indicano di proteggere bene il flash e di allegare documenti d’acquisto se è ancora in garanzia. |
| **Nital Studio – Torino (TO)** | Nital è distributore italiano Nikon e gestisce anche il marchio Elinchrom. La pagina dedicata al Nital Studio spiega che lo studio dispone di attrezzature all’avanguardia e **offre assistenza tecnica professionale sia per Nikon sia per Elinchrom**. Pur non essendo un laboratorio di riparazioni, possono indirizzare i clienti all’assistenza tecnica ufficiale e consentono di provare le attrezzature. | **Indirizzo:** Via Vittime di Piazza Fontana – Torino (sede Nital Studio). Per informazioni sull’assistenza tecnica rimandano al servizio LTR (link “Assistenza tecnica” nel sito Nital). |
| **Electronic Service Photografic di Ardemagni – Milano (MI)** | Questo laboratorio milanese è specializzato nella riparazione di generatori e flash da studio/portatili. Nella loro pagina di presentazione dichiarano di fornire assistenza e modifiche per vari marchi tra cui **Balcar, Bowens, Elcrom (Elinchrom), Broncolor e altri**. Sono attivi dal 1977 e lavorano con marchi leader a livello mondiale. | **Sede:** Via Volvinio 22, 20141 Milano. **Telefono:** 02 58430106. **Cellulare:** 392 1057529. **E‑mail:** cartapesta04@libero.it. |
| **MPR Fratelli Rossi – Roma (RM)** | Officina storica (dal 1926) specializzata nell’assistenza di apparecchi fotografici digitali e analogici, obiettivi, **flash da studio** ed esposimetri. Pur non essendo un centro autorizzato Elinchrom, è una realtà con esperienza decennale in riparazioni di attrezzature professionali. | **Indirizzo:** Via Cesare Rasponi 11/13, Roma. **Telefono:** 06 86202258. È possibile consegnare le apparecchiature direttamente o spedirle compilando il modulo di riparazione disponibile sul loro sito. |

**Conclusioni**
Per una riparazione sotto garanzia o comunque certificata si consiglia di rivolgersi ad Apromastore, che è l’unico centro di riparazione ufficiale Elinchrom in Italia. Nital Studio può fornire supporto tecnico e indicazioni sui canali ufficiali. In alternativa, Electronic Service Photografic a Milano e MPR Fratelli Rossi a Roma sono laboratori con esperienza su flash da studio, anche se non sono centri ufficiali Elinchrom.