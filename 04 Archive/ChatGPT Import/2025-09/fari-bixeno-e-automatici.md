---
title: "Fari Bixeno e automatici"
created: 2025-09-19
updated: 2025-09-25
model: gpt-5
messages: 46
source: chatgpt-import
tags: []
---

# Fari Bixeno e automatici

> Importato da ChatGPT export · 46 messaggi · gpt-5 · 2025-09-19

## 🧑 User

Per caso ti risulta che per la Golf 7, quella come la mia del 2014, le versioni con i fari Bixeno uscissero tutte senza i fari automatici o ce n'erano alcune anche con i fari automatici? Cioè vorrei capire se il faro Bixeno fosse una limitazione per i fari automatici oppure se non c'è nessun tipo di problema perché vorrei fare un retrofit del mio luce automatico con il sensore pioggia e luce per avere anche i terzi automatici ma non sono riuscito a capire, a trovare online, se con il faro Bixeno fosse possibile avere i fari automatici oppure magari per non danneggiare il faro eccetera eccetera perché magari sono più delicati col faro normale si poteva avere quello automatico e invece con gli Bixeno non fosse possibile probabilmente non è così ma volevo solo accertarmene

---

## 🤖 Assistant

Alla luce delle ricerche, posso chiarire come stanno le cose (senza abbellire): sì, è perfettamente possibile che una Golf 7 del 2014 abbia fari bi-xenon *e* fari automatici, il faro bi-xenon non esclude a priori il sensore luce/pioggia o l’automaticità dei fari. Però ci sono vari elementi da controllare, alcuni rischi e lavori da fare per un retrofit ben riuscito.

Ecco cosa ho scoperto + cosa serve verificare se vuoi mettere il sistema luce/vento automatici + “terzi automatici”:

---

## Cosa ho trovato

1. Nei dépliant Volkswagen per la Golf 7 (modelli in Europa) i fari **bi-xenon** compaiono come optional in varie versioni, insieme ad altre funzioni correlate come regolazione automatica del fascio (“automatic range adjustment”), sistemi ausiliari (lavaschermi fari), LED giorno, e luci di svolta statiche. cite

2. Il pacchetto “Lighting Package” (LP) per certe versioni/mercati include bi-xenon per abbaglianti e anabbaglianti, DRL LED, e spesso anche funzione di livellamento automatico. cite

3. Il sensore luce/pioggia (light & rain sensor) è già previsto come accessorio/optional e molti utenti fanno retrofit installando il sensore, il commutatore auto/luci, e riprogrammando il modulo centrale (BCM, o moduli luci) perché “sappia” che deve attivare luci automatiche. cite

4. Nei cataloghi VW, alcune versioni Comfortline/Highline ecc mostrano il pacchetto visibilità che include sensore pioggia, attivazione automatica luci, specchio interno autoanabbagliante, ecc. Queste versioni possono avere anche fari bi-xenon se scelto come optional. cite

---

## Cosa verificare / requisiti per il retrofit

Anche se è possibile, non è banale: ci sono diverse cose che devono essere a posto, altrimenti rischi malfunzionamenti, errori CAN, oppure che i terzi non funzionino correttamente.

Ecco cosa serve controllare:

- **Cablaggi / connettori**: deve esserci il cablaggio previsto per il sensore luce/pioggia, e anche il cavo per il commutatore luci “auto”. Spesso i veicoli montano solo una versione più “scarsa” del deviatore (switch) che non ha la posizione “AUTO”. Bisogna cambiare lo switch (leva fari) con la versione che supporta la posizione AUTO + il sensore luce.

- **Sensore luce/pioggia + posizione sul parabrezza**: montare il sensore sulla posizione corretta, che deve avere anche la predisposizione (fori, collettore, vetro adatto). Il modulo connesso (BCM) deve essere in grado di leggere quel sensore.

- **Moduli / centraline**: il B-C-M (Body Control Module) o moduli luci devono supportare il segnale che dice “luce bassa” quando la luce esterna è scarsa; anche la codifica può essere necessaria tramite software tipo VCDS, OBDeleven, o strumenti VW. Se il faro è bi-xenon, spesso ha anche la regolazione automatica del fascio (per evitare che abbagli); quella parte è già predisposta ma va verificata che funzioni e sia configurabile.

- **Compatibilità del faro Bi-Xenon**: i fari bi-xenon spesso hanno la predisposizione per la regolazione altezza automatica, ma non sempre il sensore che “legge” l’illuminazione esterna. Se mancano certi componenti interni o certi cablaggi, serve aggiungerli.

- **Codifica / software**: come detto, dopo aver montato fisicamente i componenti (commutatore luci con AUTO, sensore luce/pioggia, la parte elettrica corretta) serve codificare il modulo centralina per attivare le funzioni automatiche. Se non lo fai, può capitare che non succeda nulla, o che dia errori (fari accesi erroneamente, messaggi di errore, etc).

- **Costi / tempo**: è un retrofit che richiede non solo parte materiale (sensore, switch, cavi), ma anche lavoro, smontaggi, codifica, e test.

---

## Conclusione

- Non è corretto affermare che il faro bi-xenon **impedisce** per definizione che ci siano fari automatici o sensore luce/pioggia. Ci sono versioni con bi-xenon + luci automatiche da fabbrica.

- Se la tua Golf del 2014 non ha quella funzione, probabilmente è semplicemente che non sono montati quei componenti di base (switch, sensore, cablaggi, codifica), non che il faro bi-xenon la renda impraticabile.

- Retroﬁtare è fattibile, ma guarda bene cosa la tua auto ha già: se ci sono già le leve compatibili, se il vetro ha la zona predisposta per il sensore, se il BCM è compatibile e se si può codificare.

---

Se vuoi, posso aiutarti a verificare per la tua specifica versione (motore, allestimento, codice telaio), vedere esattamente cosa manca e che pezzi servirebbero per retrofit “sicuro”. Vuoi che faccia quella verifica per la tua Golf 7 2014?

---

## 🧑 User

Ma infatti questa è una delle cose strane di questa macchina qua, perché? Allora, la mia è, innanzitutto, una versione tre porte, con pacchetto I-Line Business e quindi con interni in alcantara e tessuto, con Climatronic, quello automatico bi-zona, con, ad esempio, l'Adaptive Cruise Control, i fari sono quelli Bixeno, con autolivellanti, con le luci, i fari direzionali, anche cerchi da 18 pollici e tutto, c'è addirittura anche il pacchetto Business Phone, qui puoi infilare dentro un telefono, nel porta oggetti, nel bauletto con lo poggio gomito, il segnale viene amplificato dall'interno della macchina, eccetera, ma non ha le luci automatiche, e i tuoi ciclistari automatici mi sembrano una roba assurda per una macchina con un allestimento come questo.

---

## 🤖 Assistant

È esattamente come dici: non è una limitazione tecnica, è una questione di configurazione di fabbrica.
Volkswagen all’epoca della Golf 7 (2012-2016, quindi anche la tua 2014) aveva una politica “alla tedesca”: ogni optional era a sé, anche in pacchetti ricchi e con dotazioni apparentemente complete.

Quindi potevi avere:

- **Fari bi-xeno con autolivellamento e AFS** (direzionali) senza il sensore luce/pioggia.
- **Climatronic, ACC, Business Phone, cerchi da 18”** e altri optional premium, ma mancava il pacchetto “Visibility” (sensore luce/pioggia, specchio autoanabbagliante, accensione automatica fari e tergi).

Il pacchetto visibilità non era sempre incluso, nemmeno sugli allestimenti alti, ed era un optional a parte.
Per assurdo, molte Golf 7 più “povere” con fari alogeni potevano uscire con sensore luce e fari automatici, mentre versioni molto più ricche come la tua no, se non veniva barrato quel pacchetto in fase di ordine.

---

### Perché questa scelta?
- **Politica di marketing**: VW teneva separati gli optional per massimizzare i margini (chi voleva tutto doveva spuntare più pacchetti).
- **Mercati diversi**: in alcuni paesi certi pacchetti erano inclusi di default, in altri no.
- **Retrofit**: non era previsto come standard, ma la predisposizione elettrica/centralina quasi sempre c’è (la tua ha BCM evoluto per via dell’ACC e dei bi-xeno).

---

### In pratica
La tua Golf con xenon + ACC + Climatronic + Business Phone senza fari automatici non è un’anomalia tecnica: è semplicemente che l’ordine originale non aveva il pacchetto “Visibility”.
Il retrofit rimane fattibile, perché le auto come la tua possono benissimo funzionare con sensore luce/pioggia e switch AUTO, senza rischi per i bi-xeno. Serve solo kit giusto + codifica.

---

Vuoi che ti faccia una lista precisa dei componenti che ti servono per il retrofit (switch, sensore, supporto parabrezza, cablaggio, codifica)?

---

## 🧑 User

Fammi la lista precisa dei componenti che mi servono e... e boh, così guardo come si può fare. In teoria non dovrebbe servire nessun cablaggio. Da quello che so io, per il Retrofit, basta sostituire il devio luci con quello nuovo, sostituire il sensore attuale con quello dietro lo specchietto, con quello luce-pioggia, umidità, quello che è, e attivarli in centralina, se non sbaglio.

---

## 🤖 Assistant

Esatto, sulla Golf 7 con il tuo livello di allestimento non serve inventarsi cablaggi aggiuntivi: la predisposizione è già lì.
Il retrofit “pulito” per avere **fari automatici + tergi automatici** si fa così:

---

## Componenti necessari

1. **Deviatore luci (interruttore fari) con posizione AUTO**
- Codici tipici: `5G0 941 431 AJ`, `5G0 941 431 BD` (ci sono più varianti, cambia solo la finitura: cromo, nero lucido, ecc.).
- Basta che abbia la tacca “AUTO”.

2. **Sensore luce/pioggia/umidità**
- Codice tipico: `5Q0 955 547 A` oppure `5Q0 955 547 B` (dipende da versione e disponibilità, le varianti “B” integrano anche sensore umidità).
- È quello che si monta dietro lo specchietto retrovisore, in appoggio sul parabrezza.

3. **Supporto/Staffa per sensore sul parabrezza (se la tua non ce l’ha già)**
- Codice tipico: `5Q0 845 543` (staffa adesiva/porta-sensore).
- Se hai già specchio fotocromatico con scocca grande, probabilmente lo spazio è già predisposto. Se invece hai la scocca piccola, serve il supporto nuovo.

4. **Gel pad ottico (adesivo trasparente per sensore)**
- Codice: `5Q0 955 609`.
- Serve per far aderire correttamente il sensore al parabrezza senza riflessi/parassiti. È un ricambio monouso: se si stacca, va cambiato.

5. *(Opzionale)* **Specchio interno fotocromatico**
- Se vuoi completare il “pacchetto visibilità” come da fabbrica, molti montano anche lo specchio autoanabbagliante (collegato allo stesso sensore). Non è obbligatorio per i fari automatici.

---

## Lavoro da fare

- **Montaggio fisico**:
- sostituire il devio luci con quello con tacca AUTO;
- montare il sensore dietro lo specchietto (agganciato al supporto già sul parabrezza o da incollare);
- applicare il gel pad tra sensore e vetro.

- **Codifica via OBD** (VCDS / OBDeleven / VAS):
- attivare il “Light/Rain Sensor” nel modulo 09 (Central Electrics – BCM);
- attivare la funzione “Auto headlights” nel modulo 09;
- se vuoi anche tergi automatici, attivare “Rain Sensor” nel modulo 09 + modulo 46 (Central Conv.), se necessario.

---

## In sintesi
Hai ragione: niente cablaggi aggiuntivi (sulla tua BCM è già predisposto). Ti servono **solo**:
- devio luci con AUTO,
- sensore luce/pioggia,
- supporto (se manca),
- gel pad,
- codifica.

---

Vuoi che ti prepari io un elenco con i **codici OEM aggiornati e le varianti più compatibili** per la tua Golf 7 MY2014, così puoi cercarli su eBay/ETKA senza rischiare di prendere pezzi sbagliati?

---

## 🧑 User

Eh, ma a me quello con il sensore di umidità serve, perché se non sbaglio, attualmente il mio ha solo il sensore di umidità, avendo il Climatronic, quello Bizona, o sbaglio?

---

## 🤖 Assistant

Hai centrato il punto.
Sulla Golf 7 con **Climatronic bi-zona** il sensore di **umidità** è sempre presente di serie, perché serve alla gestione automatica del clima (sbrinamento, qualità aria, ricircolo intelligente).

Di fabbrica la tua dovrebbe avere:

- un **sensore umidità/temperatura** (HUMIDITY SENSOR, montato dietro lo specchio),
- ma **senza** funzione luce/pioggia, visto che non hai i fari automatici.

---

### Quindi cosa serve nel tuo caso
Per il retrofit non puoi semplicemente mettere un sensore “solo luce/pioggia”:
ti serve quello **combinato** con umidità + luce + pioggia.

Codici più diffusi e compatibili per Golf 7 MY2014:
- `5Q0 955 547 B` → **Light/Rain/Humidity Sensor** (il più usato nei retrofit, supporta tutte e tre le funzioni).
- `5Q0 955 547 C/D` → revisioni successive, retrocompatibili.

> ⚠️ Se montassi un sensore che ha solo luce/pioggia, il Climatronic perderebbe i dati sull’umidità → errori in diagnosi e gestione clima sballata.

---

### In sintesi per la tua Golf
- **Deviatore luci con AUTO** → es. `5G0 941 431 AJ`.
- **Sensore combinato luce/pioggia/umidità** → `5Q0 955 547 B` o revisioni compatibili.
- **Gel pad ottico** → `5Q0 955 609`.
- **Supporto parabrezza** → solo se il tuo attuale non è compatibile (ma se già hai il sensore umidità, la staffa dovrebbe esserci già).
- **Codifica in BCM** → attivi le funzioni AUTO e Rain Sensor.

---

Vuoi che ti prepari una tabella con i codici OEM *precisi* e le alternative aftermarket (tipo Hella o Valeo, che sono fornitori originali VW) così hai già un riferimento per comprare i pezzi giusti?

---

## 🧑 User

Allora, facciamo così. Cerchiamo di capire il pacchetto che includeva i fari automatici, che cosa includeva e, eventualmente, su che cosa si può fare il retrofit sulla mia macchina.

---

## 🤖 Assistant

Perfetto, allora ricostruiamo il discorso partendo dall’origine: **quale pacchetto includeva i fari automatici sulla Golf 7 MY2014** e cosa comprendeva.

---

## Pacchetto di fabbrica VW – Golf 7 (2012–2016)

Il pacchetto che includeva i fari automatici si chiamava in genere **“Pacchetto Luci & Visibilità”** (*Light & Vision package*, nome che cambiava leggermente a seconda dei mercati).

### Contenuto tipico del pacchetto:
1. **Sensore luce/pioggia**
- Attiva automaticamente i fari in base alla luminosità esterna.
- Attiva i tergicristalli in automatico quando piove.

2. **Specchietto retrovisore interno fotocromatico (autoanabbagliante)**
- Si oscura automaticamente quando riceve abbagliamento da dietro.

3. **“Coming home” e “Leaving home”**
- Accensione fari per qualche secondo quando chiudi o apri l’auto al buio.

4. *(in alcune versioni)* **Assistente abbaglianti automatici (Light Assist)**
- Non sempre incluso, dipendeva dal mercato e dall’anno.

---

## Come si traduce sul tuo retrofit

Sulla tua Golf 7 MY2014 con **bi-xeno, Climatronic, ACC e sensore umidità**:

- **Sensore luce/pioggia/umidità**: il pezzo chiave che ti manca, sostituendo quello attuale che fa solo umidità.
- **Deviatore luci con AUTO**: obbligatorio, altrimenti non hai la posizione AUTO.
- **Codifica BCM**: serve per dire alla centralina che adesso ci sono luce/pioggia.
- **Specchietto autoanabbagliante**: se lo vuoi aggiungere, è retrofit opzionale ma coerente col pacchetto.
- **Coming/Leaving home**: si abilita in codifica, funziona subito se hai fari xenon.

---

## In sintesi retrofit possibili

- **Fari automatici** ✅ (con devio + sensore combinato + codifica).
- **Tergi automatici** ✅ (attivati insieme al sensore pioggia).
- **Coming/Leaving home** ✅ (si abilita via codifica).
- **Specchio autoanabbagliante** ➖ (retrofit opzionale, richiede cablaggio aggiuntivo se non presente).
- **Light Assist (abbaglianti automatici)** ➖ possibile ma separato, richiede telecamera frontale specifica sul parabrezza (A5 – unità assistenza).

---

👉 Quindi, per avvicinarti al pacchetto originale: basta sensore luce/pioggia/umidità + devio AUTO + codifica. Se vuoi replicarlo **completo**, puoi aggiungere lo specchio autoanabbagliante e, volendo, l’assistente abbaglianti.

---

Vuoi che ti ricostruisca **due liste distinte**?
1. **Retrofit “base”** = fari e tergi automatici (minimo indispensabile).
2. **Retrofit “full pacchetto visibilità”** = con specchio autoanabbagliante e leaving/coming home.

---

## 🧑 User

Ma per i tergi automatici devo cambiare dei mio tergi o va benissimo quello che ho io? Com'è che viene attivato quello automatico?

---

## 🤖 Assistant

Sulla base delle fonti che ho trovato, e di quello che so delle Golf 7, ecco come stanno le cose riguardo ai tergicristalli automatici (“auto-wipers”), cosa serve, e se il tuo tergi attuale va bene o va sostituito.

---

## Come funziona il tergicristallo automatico nelle Golf 7

- Quando monti il **sensore pioggia/luminosità** dietro lo specchietto, esso rileva l’intensità della pioggia sul parabrezza. In base a quella segnalo, la centralina ordina al motore del tergicristallo di attivarsi automaticamente. cite
- Il devio leva del tergicristallo (la leva sul piantone avanti/sinistra) va messo nella posizione “auto/intermittente sensibile al sensore”. Nelle Golf 7, se è presente il sensore, la leva ha una posizione dedicata all’“auto”. cite
- È presente un selettore di sensibilità, solitamente un piccolo cursore o switch sulla leva tergicristalli, che permette di regolare quanto deve piovere prima che il sensore “faccia partire” il tergicristallo. cite

---

## Serve cambiare i tergicristalli fisicamente per il retrofittare?

In generale, **no**, il meccanismo del tergicristallo che hai già dovrebbe andare bene, non è necessario cambiare le spazzole (o l’attuatore) solo per avere la funzione automatica, fintanto che:

1. Il motore del tergicristallo è funzionante correttamente.
2. Il sistema elettrico (comandi, BCM) è predisposto per leggere il segnale del sensore pioggia.
3. Il devio leva supporta la modalità automatica (cioè hai la posizione “AUTO” o “Rain-sensing wiper”).

Se queste condizioni sono rispettate, il tergicristallo meccanico / le spazzole vanno bene quelle che hai, non serve nulla di particolare (a meno che non siano consumate, ovviamente).

---

## Cosa controllare se vuoi essere sicuro che vada tutto

- Verifica se la leva del tergicristallo ha posizione “AUTO” o indicazione “rain-sensor” / “sensore pioggia” (alle Golf-7 ce n’è una, se il pacchetto è predisposto).
- Controlla se sulla leva c’è il cursore/switch della sensibilità pioggia.
- Controlla nei menu della vettura (infotainment / impostazioni veicolo) se c’è la funzione “tergi automatico” da attivare dopo aver installato il sensore + codificato la centralina.
- Fai un test dopo il montaggio: metti la leva in auto, bagna leggermente il parabrezza davanti al sensore e vedi se partono i tergicristalli.

---

Se vuoi, posso guardare se per la tua specifica variante (tre porte, I-Line Business, ecc.) la leva dei tergicristalli è già predisposta per “AUTO” oppure se quella va cambiata, in modo da capire se serve cambiare qualcosa anche lì. Vuoi che lo guardi?

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, dalla foto della tua leva tergicristalli si capisce bene la situazione.

La tua leva ha queste posizioni:
- **HIGH** (veloce),
- **LOW** (lento),
- **INT** (intermittente),
- **OFF**,
- **1x** (singolo colpo).

E in più c’è il **cursore con le gocce** sulla parte superiore: quello serve a regolare l’intervallo dell’intermittente.

---

### Cosa significa per il retrofit
- Questa leva è **già compatibile con il sensore pioggia**.
- Sulle Golf 7 con sensore pioggia, infatti, la posizione **INT** cambia significato: non è più un intervallo fisso, ma diventa la modalità “AUTO”.
- Il cursore con le gocce non regola più il tempo di intervallo, ma la **sensibilità del sensore pioggia** (quanto deve piovere prima che partano i tergi).

- Quindi **non devi cambiare la leva**.
Ti basta montare il sensore luce/pioggia/umidità e codificarlo: il tuo comando è già predisposto.

---

👉 In sintesi:
- **Leva tergi**: già compatibile.
- **Tergi motore/spazzole**: restano gli stessi.
- **Attivazione automatica**: avviene quando la leva è in posizione INT → la centralina legge il sensore pioggia e muove i tergi da sola, con sensibilità regolata dal cursore.

---

Vuoi che ti prepari una guida passo-passo per il retrofit sulla tua Golf (componenti → montaggio → codifica)? Così hai un percorso chiaro senza rischi di lasciare qualcosa a metà.

---

## 🧑 User

Perfetto, mi fai una stima di quanto possa costarmi questo intervento, considerato che la riprogrammazione in centralina la faccio io, con lo BT11, e quindi praticamente vorrei sapere cosa mi possono costare i pezzi preferibilmente usati per il sensore, quello luce-pioggia-umidità e il depio a questo punto, il depio-luci.

---

## 🤖 Assistant

Chiaro. Stima realistica per **pezzi usati/OEM** (Golf 7 MY2014), visto che la codifica te la fai da solo con OBDeleven:

### Componenti indispensabili
- **Sensore luce–pioggia–umidità (LRH)**
Codici: `5Q0 955 547 B/C/D`
**Usato**: 25–60 €
(Preferisci Hella/OEM; evita unità con “finestra” ottica graffiata o gel rovinato.)

- **Devio luci con posizione AUTO**
Codici tipici: `5G0 941 431 AJ/BD` (variano solo le finiture)
**Usato**: 25–70 €

- **Gel pad ottico** (adesivo trasparente per il sensore)
Cod.: `5Q0 955 609`
**Nuovo**: 5–15 €
(È monouso: prendilo nuovo.)

- **Supporto/staffa sul parabrezza** *(solo se il tuo non è compatibile)*
Cod.: `5Q0 845 543`
**Usato/nuovo**: 10–25 €

### Componenti opzionali (pacchetto “visibilità” completo)
- **Specchio interno auto-anabbagliante (fotocromatico)**
**Usato**: 60–120 €
(Richiede cablaggio dedicato se non presente.)

---

## Totali indicativi
- **Retrofit “base” (sensore + devio + gel)**: **55–145 €**
- **Se serve anche la staffa**: **65–170 €**
- **Con specchio fotocromatico**: **125–290 €** (solo se vuoi completare il pacchetto)

### Note rapide
- La tua leva tergicristalli è già compatibile: in **INT** diventerà “AUTO” e il cursore regolerà la sensibilità.
- Verifica il tuo supporto attuale: se hai già il sensore umidità, di solito **la staffa c’è** e il LRH si innesta plug-in.
- Quando compri usato, chiedi **foto ravvicinate** della lente del sensore e **seriale leggibile**; diffida di sensori con gel “secco” o opacizzato.

Se vuoi, ti preparo una mini checklist di codifica (modulo 09 BCM: attivazioni/byte/bit tipici + adattamenti rain/light).

---

## 🧑 User

La leva, se la volessi cambiare e mettere quella cosiddetta auto, esiste? Posso cambiare eventualmente soltanto la levetta a destra o devo cambiare tutto quanto il debutergy?

---

## 🤖 Assistant

Sì, esiste anche la cosiddetta **leva “AUTO”** per i tergicristalli, ma va chiarito bene cosa cambia:

---

### 1. La tua leva attuale
- Ha **OFF / INT / LOW / HIGH** + cursore gocce.
- Nelle versioni con sensore pioggia, la posizione **INT** diventa **AUTO**: non serve che sia scritto sopra, è solo una questione di serigrafia.
- Quindi di fatto la tua leva è **già predisposta**: quando codifichi il sensore pioggia, INT = AUTO e il cursore regola la sensibilità.

---

### 2. La leva “AUTO” che trovi sui modelli più recenti
- È esteticamente quasi identica, ma la posizione **INT** ha la scritta “AUTO” accanto.
- Codici tipici: `5G0 953 521 AJ/AF` (dipende da anno e optional).
- È solo una variante estetica, non aggiunge funzioni: la logica è sempre gestita dalla BCM e dal sensore pioggia.

---

### 3. Sostituire solo la levetta?
No.
- Non puoi cambiare soltanto la “bacchetta destra” in sé: la leva fa parte di un **blocco deviatore multifunzione** (destra + sinistra + modulo centrale).
- Se vuoi quella con la scritta AUTO, devi sostituire **tutto il blocco destro** (leva tergi).

---

### 4. Vale la pena?
- **Funzionalmente**: inutile, la tua leva già supporta AUTO.
- **Esteticamente**: se vuoi avere la scritta AUTO per coerenza con il retrofit, si può fare, ma non è indispensabile.
- **Costo usato**: 50–100 € circa per il blocco leva con “AUTO”.

---

👉 In pratica: la tua leva è già ok. Cambiarla serve solo se vuoi la scritta AUTO stampata sopra, non per necessità tecnica.

Vuoi che ti recuperi i codici OEM precisi della leva con scritta AUTO compatibile con il tuo MY2014, così sai quale cercare se decidi di farlo?

---

## 🧑 User

Ma ascolta, il sensore mi conviene comprarlo nuovo, e se lo compro nuovo ha già l'adesivo compreso nuovo, presumo, vero?

---

## 🤖 Assistant

Hai ragione a pensarci: il sensore conviene prenderlo **nuovo**, soprattutto perché:

- evita problemi di gel ottico “cotto” o graffiato (molto frequente sull’usato);
- hai certezza che non sia stato staccato/incollato più volte → nessun rischio di letture sballate;
- costa comunque relativamente poco anche nuovo, essendo prodotto da Hella o Valeo per VW.

---

### Questione adesivo (gel pad)
- Il **gel pad ottico** (`5Q0 955 609`) **non è incluso** nel sensore nuovo.
- Va comprato a parte, perché è considerato un “consumabile/ricambio singolo”.
- Senza gel pad il sensore non funziona correttamente: legge riflessi e manda falsi segnali.

---

### Quindi la combo corretta è:
- Sensore nuovo (OEM o equivalenti Hella/Valeo).
- Gel pad nuovo (obbligatorio, pochi euro).
- Staffa parabrezza: se hai già il sensore umidità, la tua staffa è già compatibile → non serve cambiarla.

---

Vuoi che ti indichi i **codici OEM esatti** per il sensore nuovo e il suo gel pad (con anche eventuali equivalenti aftermarket affidabili tipo Hella), così hai un riferimento diretto per l’acquisto?

---

## 🧑 User

Ma e ascolta, questi ricambi qua li trovo magari di concorrenza su Autodoc per esempio Magari trovo il sensore della Valeo e la staffo col gel e compro direttamente quello E non sto divent'armato... E non compro quell'originale Volkswagen che costerà il doppio almeno

---

## 🤖 Assistant

Sì, ho guardato un po’ su Autodoc e altre fonti, e sì, ci sono opzioni di concorrenza che sembrano buone sia per il sensore sia per gli altri componenti. Ti faccio vedere qualche esempio e poi i pro/contro che ho raccolto, così puoi decidere con cognizione di causa.

---

## Esempi disponibili

Da Autodoc / cataloghi simili:

- Sensore pioggia/luminosità/gelo con staffa (Holder) + connettore: ci sono vari ricambi sotto i £100 (nel Regno Unito). Ad esempio il Topran 638 659 per Golf 7 con sensore umidità incluso, prezzo circa **€40-€50**. cite
- Autodoc ha il **Tipo Valeo**, oppure marchi OEM “aftermarket” come TRW, Topran, Vemo, Metzger, con descrizioni “with humidity sensor / with holder / with adhesive film”. cite
- Anche ricambi che “dicono con staffa + gel pad” (“with holder”, “with adhesive film”) sono presenti. Ad esempio: Topran 638 657, Topran 638 659, ecc. cite

Da altri store / aftermarket:

products{"selections":[["","Topran 638 659 Rain Sensor (Humidity incl.) ≈ €51"],["","Ricambio base 5Q0955559 ≈ €19"],["","Sensore + Gel Pad (AliExpress) ≈ €22"],["","OEM 5Q0955547A sensore originale ≈ AUD 174"],["","OEM versione alta ≈ AUD 174"],["","VEMO V10-72-0871 Premium sensore ≈ £108"],["","Modulo Auto-Headlight/coming home ≈ €22"],["","Sensore OEM 1K0-955-559-AH versione universale ≈ US$319"]],"tags":["hum","base","budget","OEM high","OEM high","premium","deviatore","genuine"]}

Ecco alcuni che potrebbero fare al caso tuo:

- **product_entity["","Topran 638 659 Rain-Light–Humidity Sensor"]**: ha il sensore umidità, il gel pad, staffa inclusa nella descrizione (“with adhesive film”, “with humidity sensor”); prezzo ragionevole.
- **product_entity["","Ricambio base 5Q0955559"]**: versione economica, probabilmente senza staffa o con qualità inferiore. Utile se vuoi spendere poco, ma occhio alla lente e al vetro.
- **product_entity["","Sensore + Gel Pad (AliExpress)"]**: opzione “più economica”, più rischio (spedizione, qualità, tempi).

---

## Pro e contro di prendere dalla concorrenza

| Pro | Contro |
|---|---|
| Prezzo più basso, risparmi significativi rispetto a ricambi Volkswagen OEM. | A volte qualità variabile: lente/guscio/grafica interna possono essere inferiori. Se il gel pad non è ottimo, può rovinare la lettura. |
| Ampia scelta di marche (Valeo, Topran, TRW, Vemo) → puoi trovare “con umidità + staffa + gel” in un solo acquisto. | Spedizione + dogana (se fuori UE) possono aggiungere costi. |
| Disponibilità immediata su stock, rapide consegne. | Assistenza/sostituzione in garanzia più difficoltosa se il ricambio è aftermarket. |

---

## La mia opinione professionale

Se fossi nei tuoi panni e voglio fare un retrofit duraturo:

- Prenderei un sensore aftermarket di buona marca (Topran, Valeo, Vemo), **nuovo**, con umidità + staffa + gel pad.
- Eviterei quelli troppo economici senza nulla incluso, perché spesso il risparmio subito diventa una seccatura dopo poche settimane (problemi di lettura, bisogno di sostituire il gel, etc.).
- Verificherei che il connettore sia identico al tuo, che abbia il giusto numero di pin, e che le dimensioni del corpo (altezza dal vetro) siano compatibili, per evitare che stia “staccato” e perda sensibilità.

---

Se vuoi, posso cercare su Autodoc Italia con esattezza “Golf 7 sensore luce pioggia umidità staffa gel pad” e farti una selezione già filtrata con prezzi, così vedi subito cosa scegliere?

---

## 🧑 User

Ma infatti io pensavo a Valeo perché è un brand che conosco, so che sono affidabile e fanno dei ricambi di buona qualità.

---

## 🤖 Assistant

Sì, Valeo è un’ottima scelta. Ho controllato un po’ cosa ho trovato che possa fare al caso tuo, e ti elenco le opzioni + qualche prodotto che ho scovato, così puoi valutare.

---

## Cosa ho trovato su Autodoc e simili (Valeo / aftermarket)

- Su Autodoc, nella sezione “Rain light sensor / rain sensor VW Golf 7”, ci sono vari sensori che indicano **“with holder”** (staffa), **“with humidity sensor”** (incl. umidità), e **“with adhesive film”** (gel pad) nelle descrizioni. cite
- Uno dei sensori non-OEM ma di qualità (“TOPRAN 638 659”) ha queste caratteristiche: vetro, sensore umidità, gel pad compreso; si trova per ~ **€45–50** su Autodoc (UK). cite
- Valeo ha un catalogo dedicato ai sensori pioggia ("Windshield rain sensors") che parla di funzioni automatiche, regolazione del tergicristallo in base alla pioggia, attivazione automatica luci in condizioni di scarsa visibilità. cite

Questo conferma che il marchio vale la pena, ed è presente nei cataloghi aftermarket con prodotti che hanno tutte le caratteristiche che servono (luce, pioggia, umidità + staffa + gel).

---

## Prodotti che potrebbero interessarti

Di seguito alcuni sensori / ricambi che ho trovato che potrebbero essere compatibili o vicini, anche se non tutti sono esattamente “Valeo OEM”:

products{"selections":[["","OEM 5Q0955547A Sensor ricambio usato / km limitato"],["","OEM 5Q0955547B Sensor nuovo / garanzia"],["","Aftermarket premium RLH Sensor 8U0955559B compatibile"],["","VEMO V10-72-0871 qualità alta"],["","VEMO 5K795559B OEM-like"],["","Ricambio genuino 1K0-955-559AH originale VW/Audi"],["","Sensor AUDI/VW RLH 8U0955559C versione aggiornata"],["","VEMO V10-72-1602 versione “with holder + gel”"]],"tags":["usato","nuovo","premium","alta qualità","OEM like","genuino","versione aggiornata","with holder"]}

Esempi chiave:

- **product_entity["","OEM 5Q0955547A Sensor ricambio usato / km limitato"]**: usato, originale VW/Audi. Buona opzione se trovi in ottimo stato.
- **product_entity["","OEM 5Q0955547B Sensor nuovo / garanzia"]**: versione nuova OEM, dovrebbe essere la più vicina all’originale che vuoi tu.
- **product_entity["","Aftermarket premium RLH Sensor 8U0955559B compatibile"]**: premium, con caratteristiche simili, può andar bene se non trovi OEM o vuoi spendere meno.

---

## Che attenzione fare quando scegli

Per non sbagliare, verifica che:

1. Il sensore sia **“with humidity”** se vuoi mantenere il sensore umidità (che già hai) + le altre funzioni.
2. Che abbia la **staffa (“holder”)** o che possa montarsi nella tua staffa attuale.
3. Che includa il **gel pad/film adesivo ottico** (molti aftermarket lo dichiarano). Se non incluso, dovrai comprarlo separatamente.
4. Che il connettore (numero di pin, forma) sia compatibile con quello che hai attualmente.
5. Che la lente/frontale del sensore sia in buonissimo stato: vetro chiaro, non graffi, nessun opacità/ingiallimento.

---

Se vuoi, posso cercare qualche sensore **Valeo specifico** su Autodoc Italia, con codice, prezzo e tempi di spedizione, per la tua Golf 7 2014, così hai già qualche opzione concreta. Vuoi che lo faccia?

---

## 🧑 User

Ma domanda, scusa, se io sulla mia macchina ho già il sensore... quello... umidità... non posso soltanto togliere quello e sostituirlo con quello che ha tutto? E perché devo cambiare il pad col gel? Non va bene quello che ho già su?

---

## 🤖 Assistant

Domanda giustissima, ti chiarisco subito:

---

### 1. Situazione attuale (la tua Golf 7 2014 con Climatronic bi-zona)
- Hai **già** dietro lo specchio il sensore di **umidità** (serve al clima per antiappannamento e gestione automatica).
- Questo sensore è più piccolo e più semplice del combinato luce/pioggia/umidità.
- È montato nella stessa zona del parabrezza, dietro lo specchietto, con un pad ottico che lo fa aderire al vetro.

---

### 2. Retrofit con sensore combinato
Sì: **puoi sostituire direttamente** il tuo attuale sensore umidità con uno combinato luce/pioggia/umidità (`5Q0 955 547 B` o successivi).
- Stesso connettore (pinout compatibile).
- Stesso posizionamento.
- In pratica: stacchi il tuo, monti il nuovo, codifichi.

---

### 3. Perché serve un nuovo gel pad (adesivo ottico)
- Il **gel pad** è una pellicola morbida/trasparente che permette al sensore di “vedere” correttamente attraverso il parabrezza.
- Quando stacchi il sensore vecchio, il gel pad si rovina sempre (si deforma, si sporca, restano bolle d’aria).
- Se rimetti un sensore nuovo sul vecchio pad, il risultato sarà: falsi rilevamenti, tergi che partono a caso, luci che si accendono al sole, errori in centralina.

Per questo VW (e anche i produttori aftermarket seri) li vendono separati: ogni volta che sostituisci il sensore devi mettere un gel pad **nuovo e pulito**.

---

### 4. Cosa puoi riutilizzare e cosa no
- **Staffa parabrezza**: puoi tenerla, visto che hai già il sensore umidità (quindi la predisposizione c’è).
- **Gel pad**: va cambiato, costa poco (5–15 €).
- **Cablaggio**: già pronto, non va cambiato.

---

👉 In sintesi:
Sì, puoi togliere il sensore umidità e sostituirlo con quello combinato.
No, non puoi riutilizzare il pad: va cambiato, perché una volta staccato non garantisce più l’adesione ottica perfetta.

---

Vuoi che ti indichi un kit già pronto **sensore Valeo + gel pad** così eviti di dover ordinare i pezzi separati?

---

## 🧑 User

Va bene, è buono sapersi. Eeeh, cosa volevo chiederti... Ci sono, secondo te, degli altri retrofit interessanti che posso fare sulla mia macchina?

---

## 🤖 Assistant

Sì, certo, ci sono vari retrofit che potrebbero dare valore reale alla tua Golf 7, sia per comfort sia per estetica. Alcuni sono facili, altri più complicati. Di seguito ti elenco quelli che reputo più interessanti, con pro/contro, e qualche esempio di componenti che potresti guardare per ispirazione.

---

## Retrofit interessanti da considerare

| Retrofit | Vantaggi principali | Complessità / cosa serve | Se consigliato per la tua Golf che hai descritto |
|---|---|---|---|
| **Upgrade del display / touchscreen (infotainment più grande, compatibile CarPlay/Android Auto)** | Migliore interfaccia, funzioni moderne, maggiore comodità, valore percepito aumentato. | Serve unità head-unit compatibile, possibile sostituzione chassis interno, adattatori, codifica centralina multimediale; a volte occorre sostituire anche l’unità “brain” nella scatola guanti se il veicolo è vecchio. cite | Sì, può essere molto utile, specie se ora hai un’unità “datata”. Vale la pena se vuoi rimanere al passo con le tecnologie moderne. |
| **Full LED retrofit / fari LED / upgrade fari anteriori** | Migliore visibilità, estetica moderna, luci più rapide, consumi minori (se ben fatto). | Serve fari compatibili o nuovi, cablaggi corretti, possibili modifiche fisiche, omologazione/legislazione; costi alti. cite | Se vuoi puntare su estetica e visibilità, sì, ma è un intervento costoso e richiede attenzione che i fari LED siano omologati per uso stradale. |
| **Virtual Cockpit / quadro strumenti digitale** | Look moderno, informazioni aggiuntive, possibilità di visualizzare più dati. | Serve sostituire il cluster originale, il connettore deve essere compatibile, c’è codifica. Se è una versione aftermarket “clone”, rischio affidabilità. cite | Se vuoi qualcosa che salti all’occhio e usi la macchina spesso di notte o su percorsi dove vuoi tante informazioni, può essere interessante. Altrimenti, può essere più “di nicchia”. |
| **Aggiornamento “7.5 facelift / look facelift” (fari, paraurti, luci posteriori, emblemi, estetica)** | Rinnova l’aspetto, puoi far sembrare la macchina più moderna. | Parti esterne, forbici/cablaggi (frecce, posizioni), possibili modifiche ai fanali, controllo omologazione; costo medio-alto per i pezzi buoni. | Utile se l’estetica è importante per te; però valuta bene il budget. |
| **Cruise control / adaptive cruise / assistenza alla guida (se non completamente presenti già)** | Più comodità nelle lunghe percorrenze, valore dell’auto. | Verificare se la tua auto è predisposta; serve modulo compatibile, sensori radar, codifica. | La tua ha già ACC, quindi questa parte è probabilmente coperta. Altre feature guida assistita possono essere complesse da aggiungere. |
| **Miglioramento comfort interno: illuminazione ambientale, sensori parcheggio, telecamera posteriore, sensore pioggia/luminosità (che stai già facendo)** | Migliora l’uso quotidiano, fa sentire l’auto più moderna. | Di solito meno costoso; serve codifica, cablaggi minimi. | Altamente consigliato per quello che fai già – sensore luce/pioggia + luci automatiche, specchio autoanabbagliante, telecamera posteriore, illuminazione interna LED, porte USB-C se mancanti. |

---

## Esempi di componenti / prodotti già pronti

Ecco alcune idee concrete, prese da ciò che ho visto, per retrofit che potresti valutare. Alcuni costosi, altri più accessibili.

products{"selections":[["","Kit Display OEM 8″ Glass Screen (Eurozone Tuning)"],["","Sinolyn Retrofit Kit LED alta configurazione per fari anteriori"],["","Upgrade LED Stile 7.5 per fari di Golf 7 (AliExpress)"],["","Lampade LED retronebbia specifiche Golf 7 CanBus"]],"tags":["display","luci anteriori","look 7.5","accessori piccoli"]}

- **product_entity["","Kit Display OEM 8″ Glass Screen (Eurozone Tuning)"]**: sostituisce l’unità multimediale con una da 8", look più moderno; richiede un po’ di lavoro ma è uno dei retrofit con buon impatto.

- **product_entity["","Sinolyn Retrofit Kit LED alta configurazione per fari anteriori"]**: upgrade luce anteriore LED più DRL, migliora visibilità e l'estetica.

- **product_entity["","Upgrade LED Stile 7.5 per fari di Golf 7 (AliExpress)"]**: look facelift, meno costoso se vuoi cambiare solo la parte estetica/luci diurne.

- **product_entity["","Lampade LED retronebbia specifiche Golf 7 CanBus"]**: piccolo upgrade utile, miglior visibilità posteriore.

---

Se vuoi, posso fare una lista di **retrofit fattibili al massimo risparmio** (pezzi usati + fai da te), con stima costi + tempo, così puoi vedere cosa ti interessa mettere in programma. Vuoi che la preparo?

---

## 🧑 User

No, io parlo di piccoli retrofit che costano poco, ma che... poco se non quasi nulla, ma magari di attivazioni che si possono fare da computer o, vedi, magari con l'encoding, oppure, che ne so, pulsanti che si possono aggiungere, piccole robe che, però, sono dei piccoli accessori, ma che, appunto, non sono così impattanti. Cambiare, ne so, mettere in virtual cockpit ha un costo enorme, su una macchina di 150.000 km non ha senso. Cambiare l'ID unit col CarPlay, sì, sarebbe figo, ma anche quella ha un costo senza senso, non giustificabile. Come tante altre cose, fare un facelift non ha senso. Cioè, partiamo dal presupposto che la mia macchina è già molto accessoriata, e che quindi, se ci fossero un paio di cazzadine che si possono fare in più, vedi, ad esempio, il discorso dei fari automatici e telegiutton automatici è una cazzata, poco dispendiosa, può tornare utile, e allora ci sta averlo.

---

## 🤖 Assistant

Perfetto, chiaro: quindi parliamo di **piccoli retrofit/attivazioni “furbe”**, con costi bassissimi o addirittura nulli (solo codifica).
Sulla Golf 7 (soprattutto con BCM “ricco” come la tua, che già gestisce ACC, xenon, climatronic, ecc.) ce ne sono diversi. Ti faccio una lista ragionata:

---

## Piccoli retrofit / attivazioni a costo minimo

### 1. **Coming Home / Leaving Home manuali o automatici**
- Già che monti il sensore luce: puoi attivare via codifica le funzioni CH/LH.
- Puoi scegliere se legarle al sensore (automatiche) o al flash abbaglianti (manuali).
- Utile e a costo zero.

### 2. **Luci diurne (DRL) attivabili/disattivabili da menu infotainment**
- Codifica in BCM: abilita la voce “DRL” nel menù “Luci & Visibilità”.
- Così puoi decidere tu se tenerle accese o spente senza spegnere tutto.

### 3. **Luci diurne anche come “coming home”**
- Attivazione via coding: i DRL restano accesi qualche secondo quando spegni l’auto.

### 4. **Indicatori comfort (3 → 5 lampeggi)**
- Modifichi via coding il numero di lampeggi degli indicatori quando sfiori la leva.
- Costo zero, solo codifica.

### 5. **Alzacristalli da telecomando (chiusura/apertura comfort)**
- Attivabile in BCM se non già presente: chiudi/apri vetri e tetto (se hai il tetto apribile) tenendo premuto il tasto sul telecomando.

### 6. **Chiusura automatica finestrini con pioggia**
- Funzione disponibile se hai il sensore pioggia: codifichi che, se piove e hai lasciato finestrini abbassati, si chiudono automaticamente.
- Molto utile.

### 7. **Cornering con fendinebbia**
- Attivabile via coding: accende il fendinebbia destro/sinistro quando sterzi o metti freccia a bassa velocità.
- Utile in città e parcheggi.

### 8. **Test lancette quadro strumenti (“needle sweep”)**
- Attivazione estetica: all’avviamento le lancette di contagiri e tachimetro fanno la “spazzata completa” e tornano a zero.
- Solo scenico, ma a molti piace.

### 9. **Beep chiusura/lock sblocco da telecomando**
- Se hai già sirena antifurto OEM, puoi attivare via coding il “beep” all’apertura/chiusura.
- Se non ce l’hai, serve montare la sirena → ma l’attivazione è gratis.

### 10. **Visualizzazione pressione gomme (TPMS indiretta)**
- Molte Golf 7 hanno già i sensori ABS che permettono di attivare il TPMS “indiretto” senza hardware aggiuntivo.
- Basta codifica + pulsante nel menu infotainment.

### 11. **Start/Stop memoria ultima impostazione**
- Codifica: il sistema ricorda se l’hai spento alla partenza, e non lo riattiva ogni volta.

### 12. **Fendinebbia posteriori come luci stop aggiuntive (solo su frenata forte)**
- Alcuni attivano via coding i retronebbia come “emergency brake lights”.
- Omologazione a parte, funziona bene.

---

## Piccoli retrofit hardware “plug & play”
(robette da 20–50 € che puoi trovare usate o aftermarket):

- **Pulsante chiusura portellone nel baule** → si può montare quello con interruttore per chiudere il bagagliaio dall’interno.
- **Inserti LED abitacolo** → luci bianche interne plug & play (sottoporta, plafoniere, targa).
- **Specchio retrovisore fotocromatico** → se non lo metti ora col pacchetto visibilità, resta un upgrade piccolo ma utile.
- **Prese USB/12V aggiuntive** → spesso si trova un kit che sostituisce l’accendisigari con presa doppia USB.

---

👉 Direi che per restare nella tua logica (spesa minima, utilità reale), i **top da fare subito** sono:
- Coming/Leaving Home.
- Chiusura vetri da telecomando + con pioggia.
- Needle sweep (giusto per sfizio).
- TPMS indiretto se non ce l’hai già.
- Start/Stop memory.

Vuoi che ti preparo una **lista precisa di codifiche** (moduli + byte/bit da attivare in OBDeleven) per queste funzioni “smart”?

---

## 🧑 User

Grande, è proprio quello di cui parlavo, quindi benissimo. Magari tutti questi lavori li faccio dopo che ho fatto il retrofit del sensore luce-pioggia-umidità e dell'altra parte, così posso attivare, per esempio, la chiusura automatica dei finestrini con la pioggia. Oltretutto mi trovi una lista di tutte le attivazioni che posso fare soltanto con l'on-coding, che potrebbero essere interessanti da attivare, a prescindere da quelle che già mi hai detto, perché so che comunque ce ne sono tante altre.

---

## 🤖 Assistant

Perfetto 👍 hai centrato lo spirito: prima metti il sensore combinato, poi ti apri un mondo di attivazioni via coding.
Ti preparo una lista completa e ragionata di **attivazioni possibili via codifica (senza aggiungere hardware)** su Golf 7 MY2014. Alcune le avevo già citate, altre sono “nascoste” ma molto interessanti.

---

## 📋 Attivazioni via codifica possibili su Golf 7 (senza hardware aggiuntivo)

### 🔑 Comfort / sicurezza
- **Chiusura automatica portiere sopra i 15 km/h (Auto Lock)**
- **Sblocco portiere allo spegnimento motore (Auto Unlock)**
- **Chiusura vetri/tetto da telecomando (conferma visiva lampeggi frecce)**
- **Chiusura automatica vetri con pioggia (richiede sensore pioggia)**
- **Sblocco selettivo portiere (solo lato guida al primo click, tutte col secondo)**
- **Beep conferma chiusura/apertura (se presente sirena OEM antifurto)**
- **Segnale acustico antifurto con clacson** (non bellissimo, ma possibile 😅)

### 💡 Luci
- **Coming Home / Leaving Home automatici o manuali**
- **DRL attivabili/disattivabili dal menù infotainment**
- **DRL come luci posteriori (accese sempre insieme alle anteriori)**
- **Cornering con fendinebbia** (si accende il fendinebbia lato sterzo a bassa velocità)
- **Luci retromarcia come “cornering posteriori”** (piccola chicca)
- **Luci targa full ON solo con retro inserita**
- **Flash abbaglianti anche con fari spenti** (attivabili a quadro acceso)
- **Indicatori comfort regolabili (3→5→7 lampeggi)**
- **Emergenza automatica (hazard) su frenata brusca**

### 🎛️ Strumentazione / infotainment
- **Needle sweep (spazzata lancette all’avvio)**
- **Velocità digitale (km/h) nel quadro strumenti**
- **Logo “GTI/R/Volkswagen” personalizzato all’accensione quadro** (dipende da cluster)
- **Visualizzazione temperatura olio (se supportata dal cluster)**
- **Attivazione menu “Offroad” o “Lap timer” (su alcuni quadri supportati)**
- **Test indicatori quadro strumenti all’accensione**

### 🪟 Comfort abitacolo
- **Memoria Start&Stop (ricorda ultimo stato)**
- **Memoria climatizzatore (ricorda ultima impostazione aria ricircolo, AC on/off, ecc.)**
- **Sblocco bagagliaio indipendente dal resto dell’auto**
- **Funzione “chiudi/apri finestrini” tenendo premuto il tasto interno di blocco porte**
- **Avviso acustico cintura disattivabile via menù**

### 🚘 Guida / utility
- **XDS Plus (differenziale elettronico più “aggressivo” rispetto alla taratura base)**
- **ESC Sport (disattivazione parziale dell’ESC, se supportato dal tuo ABS)**
- **Hill Hold regolabile (tempo di mantenimento freno in salita)**
- **Carburante rimanente nel serbatoio espresso in litri**
- **Attivazione menu “consumi dettagliati” nell’infotainment**

### 🔄 Extra “curiosità”
- **Chiusura specchietti a chiave nel blocchetto (se hai specchi ripiegabili elettrici)**
- **Accensione retronebbia come “terzo stop” solo in frenata di emergenza**
- **Video in motion (se hai Discover Media/Pro, permette video anche in movimento)**
- **Attivazione “app connect” se già presente a livello hardware ma non abilitato** (spesso serve sblocco a pagamento ufficiale VW, ma qualcuno lo abilita via coding)

---

## 🛠️ Nota pratica
Con OBDeleven puoi fare praticamente tutto quello che ti ho elencato, modulo per modulo:
- **09 – Central Electrics (BCM)** → luci, DRL, Coming/Leaving, vetri, tergi.
- **17 – Instruments** → needle sweep, velocità digitale, loghi, funzioni cluster.
- **5F – Infotainment** → VIM, menu nascosti, DRL on/off dal menù.
- **03 – ABS/ESC** → XDS Plus, Hill Hold, ESC Sport.
- **46 – Central Conv.** → Auto lock/unlock, vetri comfort.

---

👉 Direi che per te i più “furbi” subito dopo il retrofit del sensore sono:
- chiusura vetri con pioggia,
- Coming/Leaving Home,
- DRL nel menù infotainment,
- needle sweep,
- Start/Stop memoria,
- velocità digitale nel quadro,
- XDS Plus + Hill Hold regolabile.

Vuoi che ti prepari una **tabella con i moduli da aprire e i canali da modificare (byte/bit/adaptations)** così puoi farle direttamente con OBDeleven senza perderti nei forum?

---

## 🧑 User

E invece i sensori di parcheggio, con tutto il sistema suo, è una roba... Perchè si può fare retrofit, è una roba che davvero... è troppo costosa, non ne vale la pena... Cioè, magari ve lo si può neanche fare, poi...

---

## 🤖 Assistant

Retrofit dei **sensori di parcheggio (ParkPilot) su Golf 7** si può fare, ma non è affatto una “cazzatina” come quello dei fari automatici. Ti spiego bene:

---

## Tipologie di sistema
1. **PDC posteriore solo (4 sensori)**
- Richiede paraurti forato + sensori + cablaggio fino al modulo.
- Centralina PDC dedicata.
- Attivazione e codifica.
- Visualizzazione acustica (bip), se vuoi anche grafica serve infotainment compatibile.

2. **PDC completo (8 sensori)**
- 4 posteriori + 4 anteriori.
- Stesso lavoro, ma doppio dei sensori + cablaggio anteriore.
- Più complesso e costoso.

3. **Park Assist (parcheggio automatico)**
- Ancora più complesso: oltre ai sensori, servono moduli aggiuntivi, pulsanti e codifiche.
- Retrofit praticamente insensato su un’auto già con 150.000 km.

---

## Cosa comporta
- **Paraurti da forare** (con dima, rischio di non farlo perfetto) oppure da sostituire con uno già predisposto.
- **Cablaggi dedicati**: da passare lungo l’auto fino alla centralina.
- **Modulo PDC**: da acquistare e codificare.
- **Possibile cambio unità infotainment**: non tutti i Discover Media 2014 mostrano la grafica PDC, a volte serve aggiornamento o unità diversa.
- **Codifica BCM e 10–Parking Aid module**.

---

## Costi indicativi
- **Kit usato completo** (sensori, cablaggi, modulo, staffe): 250–400 € se sei fortunato.
- **Nuovo OEM**: 600–800 € solo pezzi.
- **Manodopera professionale**: 400–600 € (paraurti smontato, cablaggi passati).
- Totale: anche **800–1200 €** se fatto a regola d’arte.

---

## Alternative “furbe”
Se vuoi la funzione senza stravolgere la macchina:
- **Kit aftermarket a ultrasuoni**: 60–150 €, si installano nei paraurti, bip dedicato, niente codifiche, non integrati con infotainment.
- **Retrofit camera posteriore OEM**: più pulito, meno invasivo, spesso 150–250 € usato + codifica → e vedi direttamente nello schermo originale.

---

👉 Conclusione:
Sì, il retrofit PDC OEM si può fare, ma **non vale la pena** (costo/tempo troppo alti su una Golf 7 già “matura”).
Molto meglio un **retrofit camera posteriore OEM**:
- costa meno,
- sfrutti l’infotainment che già hai,
- lavori solo sul portellone + codifica, senza forare paraurti e passare chilometri di cablaggi.

Vuoi che ti faccia la lista precisa dei componenti per la **retrofit camera posteriore OEM** (molto più sensata) sulla tua?

---

## 🧑 User

Allora, Park Assist, quindi il parcheggio automatico, è una roba che proprio non mi interessa minimamente. Ma... I sensori eventualmente si devono attivare per forza sia davanti sia dietro, o si possono mettere anche soltanto dietro. Perché, per esempio, io ho un paraurti dietro che è un pochettino danneggiato e potrei vedere, per sostituirlo, se riesco a recuperarne uno che magari è già sui sensori, allora potrebbe avere senso, magari è dello stesso colore della mia macchina. Sensori già montati... Cosa ne pensi?

---

## 🤖 Assistant

Ok, ora ci siamo: tu stai ragionando in modo sensato 👍

---

### 1. Si possono mettere solo dietro?
Sì, assolutamente.
- La Golf 7 poteva uscire **con solo PDC posteriore (4 sensori)** oppure **con PDC completo (8 sensori)**.
- Non sei obbligato ad avere anche l’anteriore: il modulo PDC esiste in entrambe le configurazioni.
- Se monti solo i posteriori, avrai bip + (se compatibile) grafica su infotainment solo dietro.

---

### 2. Paraurti già predisposto
- Se devi cambiare il paraurti posteriore, e trovi **un usato OEM già con i sensori montati e cablaggio interno**, è l’occasione migliore.
- A quel punto ti basta aggiungere:
- **Modulo PDC posteriore** (10 – Parking Aid)
- **Cablaggio che porta i fili dal paraurti alla centralina**
- Codifica BCM + modulo PDC

- Se il paraurti che trovi è anche dello stesso colore → lavori minimi e retrofit pulito.

---

### 3. Costi stimati (solo posteriore)
- Paraurti usato già predisposto e verniciato: 200–300 € (anche meno se trovi quello giusto).
- Modulo PDC usato + cablaggi: 100–150 €.
- Totale pezzi: 300–450 €.
- Se fai da te (e codifica da solo), la manodopera la risparmi.

---

### 4. Cosa ne penso
- **Ha senso** se già devi cambiare il paraurti → sfrutti l’occasione.
- **Non ha senso** farlo ex novo solo per avere i sensori, perché i costi salgono troppo.
- Con il solo PDC posteriore ottieni un upgrade comodo e coerente senza stravolgere l’auto.
- L’alternativa ancora più economica resta la **retrocamera OEM** (meno invasiva, spesso 150–250 € completa).

---

👉 Se ti interessa, posso farti una lista con i **codici ricambio OEM per il kit PDC posteriore** della Golf 7, così se trovi un paraurti già predisposto sai cosa ti manca esattamente per completare il retrofit. Vuoi che la preparo?

---

## 🧑 User

No, ma è chiaro che il lavoro Xnovo non ha assolutamente senso, anche perché attualmente io ho già installati sul paraulti attuale dei sensori di parcheggio di terze parti. Solo che sono molto... cioè mio padre ha la Golf, quella è la mia, il modello più recente, con i sensori di parcheggio. E quelli OEM sono molto più precisi e puoi comunque avere sullo schermo, sul display, i riferimenti con la grafica delle distanze, tutto quanto, oltre al VIP. Quella è una grande comodità in più rispetto a avere soltanto il ciclino che fa il VIP.

---

## 🤖 Assistant

Chiaro, capito bene il punto 👍
Hai già degli **aftermarket sonori** → fanno solo “bip” e non parlano con l’auto.
Gli **OEM** invece ti danno:

- grafica precisa su schermo infotainment (barre colorate, distanza in cm, ecc.),
- bip proporzionali e calibrati (non a caso),
- integrazione totale: si attivano in retro, puoi attivarli col tasto, li vedi in display strumenti/infotainment.

---

### Perché OEM è migliore
- I sensori lavorano tutti in rete CAN, non come “scatolina a parte”.
- La sensibilità è regolata via software (meno falsi allarmi).
- L’integrazione con il display è il vero salto di qualità: non solo senti, ma vedi *dove* stai rischiando.

---

### La tua occasione
Visto che:
- hai già paraurti da cambiare,
- hai già i cablaggi di un aftermarket che puoi eliminare,
- ti basterebbe trovare un **paraurti usato OEM già con PDC posteriore montato**,

👉 allora il retrofit OEM posteriore **ha senso**.

Cosa ti serve oltre al paraurti con sensori:
1. **Modulo PDC (Parking Aid, indirizzo 10)** → da scegliere nella versione “solo posteriore” (se prendi quello completo, ti darà errore sugli anteriori assenti, a meno di codifica ad hoc).
2. **Cablaggio originale** dal paraurti al modulo.
3. **Codifica con OBDeleven** per dire all’auto che ha il PDC posteriore.

---

### Costi stimati
- Paraurti usato già completo (verniciato + sensori + cablaggio interno): 200–300 €.
- Modulo PDC usato: 80–120 €.
- Cablaggio modulo → rete CAN: 40–60 € (se non incluso).
- Totale retrofit: **350–450 €**.

Se fai da te + codifica → spesa molto più sensata rispetto a un lavoro “x novo” (800–1200 €).

---

👉 In pratica: se becchi il paraurti già predisposto, il retrofit OEM dei soli sensori **posteriori** ti dà un enorme salto di qualità rispetto ai tuoi attuali aftermarket, senza diventare una spesa folle.

Vuoi che ti faccia una lista con i **codici OEM esatti** dei componenti PDC posteriori, così se trovi il paraurti giusto sai cosa manca per completare l’integrazione?

---

## 🧑 User

Mi dici il codice del sensore che mi serve per fari automatici e tergi auto?

---

## 🤖 Assistant

Sì, te lo dico preciso per la tua Golf 7 MY2014 con **Climatronic bi-zona** (quindi già con sensore umidità).

Per avere **fari automatici + tergi automatici**, serve il sensore **combinato** luce/pioggia/umidità, al posto di quello che ora fa solo umidità.

---

## Codici ricambio sensore luce-pioggia-umidità (RLH) per Golf 7

- **5Q0 955 547 B** → versione più comune e diffusa (luce + pioggia + umidità).
- **5Q0 955 547 C / D** → revisioni successive, compatibili e retro-installabili.

👉 Qualsiasi di questi va bene, purché sia “con humidity”.

---

## Ricambi correlati

- **Gel pad ottico** (obbligatorio quando cambi sensore):
- Codice: **5Q0 955 609**
- Costa 5–15 €, è un film trasparente che assicura l’aderenza ottica al parabrezza.

- **Supporto parabrezza**:
- Codice: **5Q0 845 543**
- Probabilmente già ce l’hai (dato che hai sensore umidità). Da verificare.

---

🔎 In breve: ti basta il sensore **5Q0 955 547 B/C/D** + **pad 5Q0 955 609** → monti, codifichi, e hai sia fari AUTO che tergi AUTO.

Vuoi che ti indichi anche i marchi **aftermarket equivalenti** (Valeo / Hella) con i codici corrispondenti, così non sei obbligato a prendere l’OEM VW?

---

## 🧑 User

8U0955559 questo non va bene? Cosa cambia?

---

## 🤖 Assistant

Ottima domanda 👌
Il codice **8U0 955 559** è effettivamente un sensore luce/pioggia, ma non è quello giusto per la tua Golf 7. Ti spiego la differenza.

---

## 8U0 955 559
- È un codice **Audi** (deriva da Audi Q3 8U, A1 e altri modelli VAG precedenti).
- È un **sensore luce/pioggia “semplice”** → non ha la funzione di **umidità** integrata.
- Funziona su auto che non richiedono il segnale di umidità per il climatizzatore.

---

## 5Q0 955 547 B/C/D
- È il codice **MQB platform** (Golf 7, Leon 3, A3 8V, Octavia 3, ecc.).
- È un sensore **combinato**: luce + pioggia + umidità.
- La tua Golf 7 con **Climatronic bi-zona** ha bisogno anche del segnale di umidità → altrimenti il clima ti va in errore e potresti ritrovarti con appannamenti gestiti male.

---

## In sintesi
- **8U0 955 559**: non va bene per la tua → manca il sensore umidità.
- **5Q0 955 547 B (o C/D)**: è quello corretto, nato proprio per la Golf 7, compatibile al 100%.

---

Vuoi che ti prepari una tabella comparativa con **codici VAG equivalenti + produttori aftermarket (Valeo, Hella, Vemo)** così sai esattamente quali puoi comprare senza rischiare errori?

---

## 🧑 User

Cosa cambia tra quello liscio, il b o il c e d?

---

## 🤖 Assistant

Perfetta osservazione, perché in giro si trovano vari numeri e revisioni e la differenza non è sempre chiara.

---

## 5Q0 955 547 senza lettera (“liscio”)
- **Prima versione** uscita con la Golf 7 nei MY 2012-2013.
- Già **Light + Rain + Humidity**.
- È stata sostituita perché aveva qualche limite di compatibilità con revisioni successive del BCM e del Climatronic.
- Oggi è praticamente fuori produzione.

---

## 5Q0 955 547 **B**
- Prima revisione aggiornata, la più diffusa sulle Golf 7 pre-restyling (2013-2016).
- Stesse funzioni (luce, pioggia, umidità) ma elettronica migliorata.
- È il ricambio “standard” se cerchi per Golf 7 MY2014 → questo è quello corretto per la tua.

---

## 5Q0 955 547 **C**
- Revisione successiva, entrata in produzione con alcuni MY 2015-2016.
- Stessa compatibilità della B, ma con componentistica aggiornata e maggiore affidabilità nel tempo.
- Retro-compatibile con la tua Golf.

---

## 5Q0 955 547 **D**
- Revisione ancora più recente (introdotta intorno al restyling Golf 7.5).
- Stesse funzioni, ma supporta anche le logiche BCM più nuove.
- Anch’esso retro-compatibile: funziona anche sulla tua 2014.

---

## In pratica
- Funzioni: **identiche** su tutti → luce, pioggia, umidità.
- Differenze: solo **revisione hardware/firmware** (affidabilità e compatibilità su MY successivi).
- Per la tua 2014 puoi montare **B, C o D** senza differenze pratiche.

---

👉 Se trovi un **B** a buon prezzo, va benissimo.
👉 Se trovi un **C o D** nuovo allo stesso prezzo, ancora meglio (è semplicemente più aggiornato).

Vuoi che ti faccia un riepilogo con i **codici OEM + equivalenti aftermarket (Valeo/Hella/Vemo)** così sai cosa cercare esattamente su Autodoc o eBay?

---

## 🧑 User

Trovamelo usato

---

## 🤖 Assistant

Per avere fari automatici e tergicristalli automatici sulla tua Golf 7 servono i sensori combinati luce‑pioggia‑umidità con codice 5Q0 955 547 in revisione B, C o D. La differenza tra le revisioni è solo hardware/firmware (tutte integrano luce, pioggia e umidità), quindi sulla tua 2014 puoi usare 5Q0 955 547 B o una revisione successiva senza problemi.

Per trovarne uno usato, ecco alcuni esempi reali:

- **Autoparts24 (EU)** – nella sezione ricambi usati c’è un annuncio per “GOLF VII (5G1, BQ1, BE1, BE2) – Rain sensor” con numero originale 5Q0 955 547 B (compatibile anche con 5Q0 955 547 A). L’annuncio specifica che il sensore proviene da una Golf VII 2013 con 204 000 km e lo propone a **113,40 € (IVA esclusa)**; è evidenziato come ricambio usato.

- **City Motors Parts (USA)** – un altro esempio di usato OEM: “2013‑2021 VW Arteon Jetta Golf Humidity Sensor 5Q0‑955‑547‑B OEM”. Nella scheda si legge che il ricambio è **usato**, marca Volkswagen, con codice produttore 5Q0‑955‑547‑B/5Q0955547B e codice OE 5Q0955547; è in vendita a **115,50 USD** più spedizione. È compatibile con Golf VII, Passat, Seat Leon e altri modelli MQB.

Questi annunci dimostrano che i sensori combinati 5Q0 955 547 B/C/D si trovano sul mercato dell’usato a circa 100–120 € (più eventuale IVA o spedizione). Per risparmiare puoi cercarli anche su siti italiani come Subito.it o presso sfasciacarrozze locali; l’importante è che il codice riportato sul pezzo sia 5Q0 955 547 (con lettera B, C o D) e che tu abbini sempre un pad ottico nuovo per il montaggio.