---
title: "Filtri cinematografici NDIR"
created: 2026-05-18
updated: 2026-05-18
model: gpt-5-5
messages: 16
source: chatgpt-import
tags: [fotografia-video]
category: "📷 Fotografia & Video"
---

# Filtri cinematografici NDIR

> Importato da ChatGPT export · 16 messaggi · gpt-5-5 · 2026-05-18

## 🧑 User

Allora, sono recentemente stato su un set cinematografico su cui si filmava con la Arri Alexa 35, super camera. E a parte questo, avevamo un... come si chiama? Un lens hood della Finta, di quelli in cui puoi mettere dentro i filtri a lastra. E come filtri a lastra c'erano dei filtri di altissima qualità, ovviamente, come puoi immaginare. E avevamo dei filtri mesi NDIR di diversi stop, 0.6 ad esempio c'era, 0.3 e 1.2 mi sembra anche, forse qualcun altro. Poi avevamo Glimmer Glass da 1/4 e da 1/8 e Black Mist, Black Frost Mist da 1/4 e da 1/8. Dimmi qualcosa di più su questi filtri, perché avere questo tipo di filtri in particolare, eccetera.

---

## 🤖 Assistant

Quello che hai visto è un setup molto standard da produzione cinema seria: matte box + filtri cinema a lastra di alta qualità. La differenza rispetto al mondo foto/content creator non è solo “qualità immagine”, ma soprattutto controllo, coerenza e velocità operativa sul set.

Il “lens hood” di cui parli probabilmente era una matte box di entity["brand","Tilta","cine accessories brand"] oppure di altri brand cinema tipo entity["brand","ARRI","cinema equipment brand"], entity["brand","Bright Tangerine","cine accessories brand"] o entity["brand","SmallRig","camera accessories brand"]. Serve a:
- montare filtri 4x5.65 o 6x6
- evitare flare indesiderati
- lavorare velocemente cambiando filtri
- stackare più filtri insieme
- mantenere uniformità tra ottiche diverse

La parte davvero importante però sono i filtri che hai citato.

---

# ND IR / NDIR

Gli ND che hai visto non erano semplici ND “fotografici”. Erano quasi sicuramente IRND o NDIR cinema-grade.

## A cosa servono

Ridurre la luce senza cambiare esposizione relativa, così puoi:
- girare a T-stop aperti anche in pieno sole
- mantenere shutter cinematografico corretto (tipo 180°)
- controllare profondità di campo
- preservare motion blur naturale

Esempio:
vuoi girare a 1/50, T2.0, ISO base con sole forte → senza ND sei completamente sovraesposto.

---

# Perché IRND e non ND normali

Qui entra il punto serio.

Quando tagli molta luce con ND economici, spesso il sensore continua a vedere parte dell’infrarosso. Risultato:
- neri che diventano marroni/magenta
- tessuti neri che virano
- pelle alterata
- contaminazione cromatica generale

Le camere cinema tipo entity["product","ARRI Alexa 35","digital cinema camera"] sono molto sensibili e precise cromaticamente, quindi questi problemi emergono subito.

Gli IRND:
- riducono luce visibile
- riducono anche l’infrarosso
- mantengono colori più neutri

Questo è fondamentale per grading serio.

---

# Gli stop che hai citato

## 0.3 ND
Riduce di 1 stop.

## 0.6 ND
Riduce di 2 stop.

## 1.2 ND
Riduce di 4 stop.

Scala standard:
- 0.3 = 1 stop
- 0.6 = 2 stop
- 0.9 = 3 stop
- 1.2 = 4 stop
- 1.5 = 5 stop
- 1.8 = 6 stop

Nel cinema si ragiona tantissimo in stop precisi perché il DoP vuole controllo assoluto.

---

# Perché filtri a lastra invece che filtri a vite

Perché nel cinema:
- cambi ottiche continuamente
- hai diametri frontali enormi
- vuoi usare lo stesso filtro su tutto il set di lenti
- vuoi combinare diffusion + ND
- devi evitare vignettatura
- vuoi rotazione indipendente dei filtri

Inoltre i filtri cinema seri:
- hanno migliore neutralità colore
- meno dominanti
- coating migliori
- maggiore consistenza tra pezzi

---

# Glimmer Glass

entity["brand","Tiffen","filter manufacturer"] Glimmer Glass è un diffusion filter molto raffinato.

Effetti principali:
- bloom leggero sulle alte luci
- pelle più morbida
- microcontrasto ridotto
- highlight più “cinematografici”
- effetto organico ma non troppo evidente

La caratteristica del Glimmer Glass è che:
- mantiene abbastanza nitidezza
- non distrugge il contrasto
- non crea halation eccessiva
- resta elegante

È spesso usato per:
- beauty
- commercial
- fashion
- close-up
- digitale troppo “clinico”

Con camere moderne super nitide come Alexa 35, RED V-Raptor o Sony Venice, un minimo di diffusion serve spesso a togliere quella sensazione troppo “perfetta”.

---

# Black Pro Mist / Black Frost

Qui si entra nel look cinematografico vero.

## Black Pro Mist
(probabilmente intendevi questo)

È uno dei filtri più usati nella storia recente.

Effetti:
- halation sulle luci
- glow
- contrasto abbassato
- neri leggermente sollevati
- immagine più morbida

Molto visibile:
- neon
- practical lights
- controluce

Look:
- cinematic
- dreamy
- analogico
- vintage moderno

È diventato quasi abusato negli ultimi anni nel mondo creator.

---

## Black Frost

Più raffinato e meno “Instagram look”.

Effetti:
- diffusion più uniforme
- meno halation aggressiva
- pelle bella
- contrasto leggermente ridotto
- bloom più controllato

Molti DoP preferiscono Frost rispetto a BPM perché:
- sembra meno artificiale
- più naturale
- più high-end

---

# 1/8 vs 1/4

Qui cambia tantissimo.

## 1/8
Molto sottile.
Spesso quasi invisibile a occhio inesperto.

Serve a:
- togliere digitale
- addolcire leggermente
- dare texture
- rendere più “cinema” senza far notare il filtro

Molti set grossi usano SEMPRE almeno un 1/8.

---

## 1/4
Più evidente.

Hai:
- bloom più forte
- halation più visibile
- contrasto più morbido
- atmosfera più marcata

Già qui il filtro diventa parte del look.

---

# Perché usarli su Alexa 35?

Paradossalmente:
più una camera è perfetta, più spesso si cerca di imperfettarla.

La Alexa 35:
- enorme gamma dinamica
- nitidezza altissima
- microcontrasto molto definito
- immagine estremamente “clean”

I diffusion:
- rendono l’immagine meno sterile
- aiutano skin tones
- creano separazione emotiva
- simulano parte del comportamento della pellicola/vetri vintage

È una questione estetica, non tecnica.

---

# Una cosa importante che molti ignorano

Nel cinema i filtri non vengono scelti “perché belli”.

Vengono scelti in funzione di:
- lenti usate
- tipo di luce
- scenografia
- incarnati
- costume
- grading finale
- texture desiderata

Un Black Pro Mist 1/4 su anamorfica vintage può essere ingestibile.
Lo stesso filtro su ottiche moderne super cliniche può essere perfetto.

Conta SEMPRE il sistema completo.

---

# Quello che probabilmente hai percepito sul set

Probabilmente hai visto un’immagine:
- meno “digitale”
- più profonda
- highlight più morbidi
- texture più organica
- passaggi tonali più delicati

E gran parte di quella sensazione non viene solo dalla Alexa.
Viene dalla combinazione:
- camera
- lenti
- filtri
- luce
- color pipeline
- esposizione
- production design

I filtri diffusion nel cinema servono proprio a scolpire il carattere dell’immagine prima ancora del grading.

---

## 🧑 User

Che cosa di queste camere posso riportare sulla mia Sony A1 o su una Sony FX6?

---

## 🤖 Assistant

Puoi riportare parecchie cose. Non tutto, perché una entity["product","ARRI Alexa 35","digital cinema camera"] resta un sistema pensato da zero per il cinema high-end, ma molte delle sensazioni “cinematografiche” che hai percepito derivano da scelte estetiche e operative replicabili anche su entity["product","Sony Alpha 1","mirrorless camera"] e entity["product","Sony FX6","cinema camera"].

Anzi: la FX6 è molto più vicina a una pipeline cinema reale di quanto pensi.

---

# La cosa più importante: non è la camera

Il salto grosso non arriva dal corpo macchina.
Arriva da:
- ottiche
- filtration
- illuminazione
- esposizione
- movement
- color pipeline

La gente compra camere cinema pensando che “facciamo il look”.
In realtà il look lo fanno soprattutto:
- vetro davanti
- luce
- contrasto
- texture

---

# Cosa puoi replicare DAVVERO

## 1. Diffusion filters

Questa è la cosa più immediata e con miglior rapporto risultato/prezzo.

Sulle Sony moderne è quasi obbligatorio se vuoi togliere il look digitale aggressivo.

La A1 soprattutto:
- è estremamente nitida
- molto contrastata
- molto “clinical”

La FX6 è già più organica.

---

## Cosa prenderei

### Per uso serio e versatile:
- entity["brand","Tiffen","filter manufacturer"] Black Pro Mist 1/8
- oppure Glimmer Glass 1/8

Sono i due punti di partenza migliori.

---

# Differenza pratica

## Black Pro Mist 1/8
Più cinematic evidente:
- bloom
- halation
- glow sulle luci

Perfetto:
- notte
- neon
- automotive
- lifestyle
- commercial cinematic

Rischio:
può diventare “YouTube cinematic”.

---

## Glimmer Glass 1/8
Più elegante e high-end:
- meno glow pesante
- pelle bellissima
- contrasto più morbido
- immagine sofisticata

Molto più “film production” come approccio.

Su Sony moderne lo preferisco spesso.

---

# 1/8 o 1/4?

Per iniziare:
- 1/8

Senza dubbio.

1/4:
- già molto evidente
- difficile da gestire
- soprattutto su night scenes

Molti creator usano 1/4 perché “si vede”.
Sul set cinema spesso stanno molto più leggeri.

---

# 2. IRND seri

Qui cambia davvero il livello.

Se usi ND economici:
- dominanti verdi/magenta
- pelle strana
- contrasto sporco

La FX6 merita IRND seri.

---

## Se vuoi fare le cose bene:
- entity["brand","NiSi","filter manufacturer"] True Color VND
- entity["brand","PolarPro","filter manufacturer"] Peter McKinnon VND
- entity["brand","Tiffen","filter manufacturer"] IRND
- entity["brand","Firecrest","filter manufacturer"] IRND

La differenza si vede davvero in grading.

---

# 3. Matte box

Non serve solo “per fare cinema”.

Una matte box vera:
- migliora flare control
- velocizza il set
- permette stack filtri
- rende workflow professionale

Per FX6 ha molto senso.

Per A1 dipende da che lavori fai.

---

# 4. Esposizione corretta

Qui tantissimi sbagliano.

Le camere cinema sembrano “più belle” anche perché vengono:
- esposte meglio
- illuminate meglio
- protette nelle highlight

Sony soffre tantissimo se:
- clippi highlight
- sottoesponi log

---

# FX6 in particolare

La FX6 può dare immagini enormi se:
- giri S-Log3
- esponi bene
- usi ND interni intelligentemente
- lavori bene in grading

Ha già:
- dual base ISO
- ND variabile elettronico
- rolling shutter contenuto
- motion abbastanza bello

È MOLTO più cinema-oriented della A1.

---

# 5. Lenti

Questo è il pezzo enorme.

L’Alexa che hai visto probabilmente montava:
- Sigma Cine
- Cooke
- Zeiss Supreme
- ARRI Signature
- anamorphic
- ecc.

Quelle lenti:
- hanno microcontrasto diverso
- flare diversi
- falloff diverso
- focus rendering diverso

---

# Su Sony cosa puoi fare

## Budget sensato:
vecchie ottiche vintage adattate.

Tipo:
- Canon FD
- Minolta Rokkor
- Contax Zeiss
- Helios
- Leica R

Ti cambiano l’immagine molto più di cambiare camera.

---

# Oppure

Le Sigma Cine che hai visto sono interessantissime perché:
- molto nitide
- ma rendering cinema
- focus throw lungo
- breathing controllato
- color consistency

Non sembrano semplici foto lenses.

---

# 6. Motion blur e shutter

Errore tipico creator:
1/400 perché “più sharp”.

Cinema:
motion blur naturale.

Regola base:
- 25fps → 1/50
- 24fps → 1/48

Questo cambia ENORMEMENTE la percezione.

---

# 7. Lighting

La verità più dura:
una Alexa illuminata male sembra mediocre.
Una FX6 illuminata bene sembra cinema.

La luce:
- crea profondità
- separa i piani
- definisce texture
- controlla contrasto

Il pubblico percepisce “cinematic” soprattutto dalla luce.

---

# La FX6 può sembrare davvero cinema?

Sì.
Assolutamente sì.

Moltissimi lavori commerciali, documentari e branded moderni usano:
- FX6
- FX3
- Venice mixate
- RED mixate

E spesso nessuno distingue.

---

# La A1 invece?

La A1 è devastante come:
- hybrid
- commerciale
- outdoor
- action
- fotografia

Ma di base:
- è più elettronica
- più digitale
- meno “organic”

Va un po’ più addomesticata.

Con:
- diffusion leggera
- ottiche giuste
- grading corretto

migliora tantissimo.

---

# Se volessi fare un kit “cinema feel” realistico per te

Per la FX6 farei:

- Glimmer Glass 1/8
- IRND serio
- matte box leggera
- monitor serio
- ottiche vintage o cine
- rig pulito
- focus su luce ed esposizione

E già entri in un territory molto vicino a produzioni vere.

---

## 🧑 User

Mi sono reso conto, mentre io facevo il secondo assistente su questo set, che il, come si dice, il DOP, in certe condizioni, aveva quasi sempre l'Electromist 1/8, e in certe situazioni passava a 1/4 e poi ritornava a 1/8. Mi è chiaro che cosa faccia il filtro, ma mi chiedo, quali sono quelle situazioni in cui, volendo utilizzare di massima sempre questo filtro, è bene passare da uno all'altro, perché magari ci sono delle situazioni particolari di luce, eccetera?

---

## 🤖 Assistant

Quello che hai osservato è esattamente il modo in cui vengono usati davvero i diffusion filter nei set seri: non come “effetto”, ma come strumento di controllo dell’immagine in base alla scena.

E infatti il fatto che il DoP tenesse quasi sempre un 1/8 e passasse selettivamente a 1/4 è una scelta molto intelligente e abbastanza tipica.

Probabilmente il filtro era un entity["brand","Tiffen","filter manufacturer"] Black Pro Mist, Black Satin, Glimmer Glass o Black Frost. Il principio però è lo stesso.

---

# La logica reale dietro 1/8 vs 1/4

Il diffusion non agisce solo sulla “morbidezza”.

Influenza:
- halation
- contrasto globale
- microcontrasto
- texture pelle
- comportamento delle highlight
- percezione della profondità
- densità atmosferica dell’immagine

Il DoP cambia intensità in funzione di:
- quantità di highlight
- durezza della luce
- contrasto scena
- presenza di practicals
- mood emotivo
- tipo di ottica
- distanza soggetto

---

# Perché il 1/8 resta spesso “base”

Perché:
- toglie digitale
- ammorbidisce appena
- non crea problemi
- è quasi invisibile
- mantiene flessibilità in grading

Molti DoP moderni trattano il diffusion 1/8 come una sorta di “pellicola digitale”.

È un leggerissimo strato organico sopra il sensore.

Soprattutto con camere:
- Sony
- RED
- Alexa 35
- Venice 2

che sono molto nitide e molto pulite.

---

# Quando si passa a 1/4

Di solito succede quando si vuole che il diffusion diventi parte attiva dell’immagine.

---

# Situazione 1: luce dura o contrastata

Se hai:
- sole forte
- controluce duro
- highlight aggressive
- specularità

il 1/4:
- ammorbidisce i rolloff
- rende le alte luci più cremose
- riduce sensazione “video sharp”

Questo è molto comune negli esterni daylight.

---

# Situazione 2: close-up beauty / pelle

Il 1/4:
- liscia la pelle
- riduce micro imperfezioni
- abbassa microcontrasto
- rende il volto più “cinema”

Specialmente:
- talent femminile
- commercial beauty
- fashion
- dialogue close-up

Spesso il DoP:
- wide → 1/8
- close-up → 1/4

Senza che lo spettatore se ne renda conto.

---

# Situazione 3: scena emotiva / romantica / contemplativa

Il diffusion più forte:
- aumenta atmosfera
- rende l’immagine più morbida emotivamente
- crea separazione psicologica

È una cosa molto sottile ma reale.

Il pubblico non pensa:
“ah c’è diffusion”.

Pensa:
“questa scena sembra più sognante/intima”.

---

# Situazione 4: practical lights interessanti

Se hai:
- lampade tungsteno
- neon
- fari auto
- riflessi
- controluci

il 1/4:
- genera bloom più visibile
- espande le highlight
- crea halation cinematografica

Qui il filtro diventa davvero estetica.

---

# Quando invece si torna a 1/8

Per evitare che il filtro inizi a distruggere l’immagine.

---

# Situazione 1: troppe luci puntiformi

Night scenes con:
- città
- insegne
- fari
- street lights

col 1/4 possono diventare ingestibili.

Problemi:
- glow ovunque
- immagine “milky”
- contrasto che crolla
- neri lavati

Quindi:
night urban = spesso meglio 1/8.

---

# Situazione 2: scena già morbida

Se la luce è:
- diffusa
- nebbiosa
- low contrast
- soft daylight

aggiungere troppo diffusion:
- appiattisce tutto
- fa perdere tridimensionalità

In questi casi il 1/4 può uccidere l’immagine.

---

# Situazione 3: ottiche già vintage o morbide

Se monti:
- anamorphic vintage
- Cooke vintage
- Canon K35
- Super Baltar
- vecchie Zeiss

hai già:
- flare
- lower contrast
- softness

Mettere troppo diffusion sopra:
= overdose.

---

# Situazione 4: scene dettagliate

Texture importanti:
- paesaggi
- architettura
- wide shot
- dettagli produttivi

Con troppo diffusion perdi:
- separazione
- dettaglio locale
- profondità percepita

---

# La cosa fondamentale che hai probabilmente notato senza realizzarlo

Il DoP non cambiava il filtro “perché il look fosse diverso”.

Lo cambiava per mantenere COERENTE il look del film.

Questo è il punto enorme.

Perché la luce cambia continuamente:
- sole
- cloud cover
- practicals
- contrasto
- location

Quindi il diffusion viene modulato per far percepire l’immagine sempre appartenente allo stesso universo visivo.

---

# In pratica il diffusion è anche uno strumento di compensazione

Esempio reale:

## Scena A
Luce dura mezzogiorno.
Senza filtro:
troppo video/sharp.

→ metti 1/4.

---

## Scena B
Golden hour morbida.
La luce è già cinematografica.

→ torni a 1/8.

---

## Risultato finale
Le due scene sembrano coerenti tra loro.

Questo è il vero lavoro del DoP.

---

# Un’altra cosa importante: il diffusion interagisce tantissimo con l’esposizione

Un 1/4:
- sembra MOLTO più forte se sovraesponi
- sembra più delicato se proteggi highlight

Quindi magari:
- stessa scena
- stesso filtro
- diversa esposizione

→ percezione completamente diversa.

---

# Sulla tua FX6/A1 questa cosa la vedresti tantissimo

Perché Sony:
- ha highlight molto elettroniche
- microcontrasto alto
- edge sharpness marcata

Un 1/8 spesso basta.

Il 1/4 sulle Sony moderne può diventare rapidamente:
- troppo bloom
- troppo “YouTube cinematic”
- troppo latteo

Specialmente di notte.

---

# Ti direi questo come approccio pratico

## Default:
1/8 quasi sempre.

## Passa a 1/4 quando:
- close-up
- sole duro
- beauty
- atmosfera emotiva
- vuoi glow evidente
- luce troppo clinica

## Torna a 1/8 quando:
- night city
- practicals aggressive
- nebbia/mood già soft
- scene molto dettagliate
- contrasto già basso

Ed è esattamente il tipo di ragionamento che hai visto fare su quel set.

---

## 🧑 User

Okay, io sul mio sistema Nisi Swift ho il Black Mist Nisi, ovviamente, da un quarto, quindi ha senso cercare il l'ottavo.

---

## 🤖 Assistant

Sì, assolutamente sì. Anzi, secondo me nel tuo caso ha molto più senso aggiungere l’1/8 che comprare altri diffusion più “forti”.

Il tuo entity["","Nisi Black Mist Filter 1/4 Sistema Swift"] è probabilmente perfetto per:
- night scenes
- controluce
- atmosfera evidente
- commercial cinematic
- mood più aggressivo

Ma su entity["product","Sony Alpha 1","mirrorless camera"] e entity["product","Sony FX6","cinema camera"] il rischio del 1/4 è che diventi facilmente:
- troppo bloom
- troppo latteo
- troppo “effetto diffusion”
- highlight un po’ sporche

Specialmente:
- città notturne
- fari auto
- insegne
- neve
- riflessi acqua
- scene contrastate

Ed è esattamente il motivo per cui quel DoP stava quasi sempre su 1/8.

---

Il filtro che probabilmente ti manca davvero è questo:

product["","NiSi Black Mist 1/8 per sistema Swift",{"render_as":"hero","description":"La gradazione più versatile per avere un look più organico e cinematografico senza rendere il diffusion troppo evidente."}]

---

La differenza reale tra i due sul campo è questa:

| Situazione | 1/8 | 1/4 |
|---|---|---|
| Uso quotidiano | Perfetto | Spesso troppo |
| Documentary / outdoor | Ottimo | Rischioso |
| Night city | Controllato | Glow molto forte |
| Skin tones | Naturali | Più beauty |
| Commercial cinematic | Elegante | Più stilizzato |
| Paesaggi | Mantiene dettaglio | Può appiattire |
| Highlight | Morbide | Molto diffuse |
| Look percepito | “Cinema invisibile” | “Effetto cinema” |

---

Il punto importante è questo:

Il 1/8 spesso non lo “vedi”.
Lo percepisci.

Ed è proprio lì che lavora bene.

Ti toglie:
- edge sharpness digitale
- microcontrasto aggressivo Sony
- clipping percepito sulle highlight
- look troppo elettronico

senza urlare “sto usando un filtro diffusion”.

---

Secondo me, conoscendo anche il tipo di immagini che fai:
- outdoor
- reportage
- branded
- travel
- neve
- lifestyle
- documentary feel

il tuo setup ideale sarebbe:
- 1/8 come default
- 1/4 come tool creativo/situazionale

Esattamente come faceva il DoP.

---

Tra l’altro il sistema Swift di urlNiSihttps://nisifilters.it/ ha proprio senso in questa logica:
- VND sempre montato
- swap rapidissimo diffusion
- workflow molto vicino a quello cinema cite

E onestamente è uno dei pochi sistemi “creator/prosumer” che ha davvero una filosofia operativa intelligente, non solo marketing.

---

Se vuoi spingerti ancora più vicino a quel feeling cinema che hai visto sul set, il passo successivo non sarebbe nemmeno un altro filtro.

Sarebbe:
- monitor serio calibrato
- esposizione molto precisa in log
- lighting più controllato
- ottiche con rendering meno clinico

Perché il diffusion da solo migliora tanto, ma è quando tutto il sistema inizia a lavorare insieme che succede davvero quella sensazione “Alexa-like”.

---

## 🧑 User

Ok, cercami online il prezzo migliore.

---

## 🤖 Assistant

Per il tuo sistema Swift, il miglior rapporto prezzo/affidabilità che ho trovato è questo:

## Miglior prezzo affidabile

product["","NiSi Black Mist 1/8 per sistema Swift",{"render_as":"hero","description":"La versione 1/8 ideale come diffusion quotidiano su Sony FX6 e A1, molto più versatile e controllabile del classico 1/4."}]

Attualmente:
- circa **85 €**
- venditore affidabile italiano
- compatibile col tuo sistema Swift cite

---

Alternative trovate:

| Versione | Prezzo migliore trovato | Note |
|---|---:|---|
| entity["","NiSi Black Mist 1/8 per sistema Swift"] | ~85 € | miglior equilibrio |
| entity["","NiSi Black Mist 1/4 Sistema Swift"] | ~89 € | praticamente il tuo |
| entity["","NiSi JetMag Pro Black Mist"] | ~90 € | nuovo sistema magnetico NiSi |
| entity["","Tiffen Filtro Black Mist Pro"] | ~105 €+ | più “cinema industry standard” |

---

| Caratteristica | entity["","NiSi Black Mist 1/8 per sistema Swift"] | entity["","NiSi Black Mist 1/4 Sistema Swift"] | entity["","Tiffen Filtro Black Mist Pro"] |
|---|---|---|---|
| Intensità diffusion | Subtle | Media | Variabile a seconda versione |
| Uso quotidiano | Eccellente | Più situazionale | Eccellente |
| Night city | Molto controllato | Glow forte | Dipende dalla densità |
| Outdoor daylight | Ottimo | Può essere troppo | Ottimo |
| Look Sony FX6/A1 | Molto naturale | Più evidente | Più “cinema classico” |
| Workflow Swift | Perfetto | Perfetto | No |
| Prezzo | ~85 € | ~89 € | ~105-190 € |

---

Secondo me, nel tuo caso specifico:
- tieni il 1/4 come filtro “creative”
- usa l’1/8 come default operativo

Ed è esattamente il workflow che hai visto sul set cinema.

---

## 🧑 User

gli anni dell'ottantadue?

---

## 🤖 Assistant

Non ho capito a cosa ti riferisci con “gli anni dell’ottantadue”. Puoi riformulare o darmi un minimo di contesto?

---

## 🧑 User

Dicevo che il diametro è 82.

---

## 🤖 Assistant

Perfetto, allora devi cercare la versione da **82mm** compatibile col tuo sistema entity["brand","NiSi","filter manufacturer"] Swift.

Quella giusta è questa categoria:

- NiSi Black Mist 1/8 Swift 82mm

Ed è una scelta sensatissima sulla tua entity["product","Sony FX6","cinema camera"] e sulla entity["product","Sony Alpha 1","mirrorless camera"].

Il vantaggio del sistema Swift è che:
- puoi lasciare il VND montato
- aggiungere/rimuovere il diffusion in pochi secondi
- lavorare quasi “da matte box leggera”

Che è molto più vicino al workflow cinema che cambiare filtri a vite continuamente.

Come prezzo, realisticamente:
- tra 80 e 110 €
- sotto gli 80 nuovo è difficile
- sopra i 110 non ha molto senso

Occhio solo a NON comprare:
- il filtro circolare standard normale
- oppure il JetMag

Perché tu hai già il sistema Swift.

Devi prendere:
- Swift System
- 82mm
- Black Mist 1/8

Non il mist “tradizionale” standalone.

---

## 🧑 User

Ma in realtà a posteriori dico che aveva più senso prendere quello da 95, perché comunque il 16-35 e il 24-70 che ho che sono i G Master 2, sono entrambi 82.

---

## 🤖 Assistant

Sì. A posteriori hai ragione.

Nel momento in cui inizi a costruire un workflow più “cinema” o comunque più professionale/video-oriented, standardizzare su un diametro più grande ha molto più senso che inseguire il diametro delle singole lenti.

E infatti 95mm è praticamente il primo step “serio” prima di passare direttamente a matte box e filtri 4x5.65.

---

# Perché 95mm ha più senso operativo

Con 95mm puoi:
- usare step-up ring su quasi tutto
- evitare di comprare filtri duplicati
- avere meno vignettatura
- lavorare meglio con diffusion + VND
- prepararti eventualmente a una matte box clamp-on

Mentre 82mm:
- è perfetto per fotografia
- ma appena inizi a fare video serio diventa limitante

---

# Il problema tipico dell’82mm

Succede SEMPRE questa cosa:

Hai:
- 24-70 GM II → 82
- 16-35 GM II → 82

Poi arriva:
- un prime diverso
- un cine lens
- un vintage
- un tele
- una lente rental

e improvvisamente:
- 77
- 72
- 95
- 114
- ecc.

Quindi finisci:
- con mille step-up
- stacking
- problemi meccanici
- setup meno rapido

---

# Perché il 95mm è uno standard intelligente

È abbastanza grande da:
- coprire praticamente tutto il full frame moderno
- lavorare bene anche a focali wide
- gestire VND migliori
- ridurre vignettatura

Ma ancora abbastanza compatto da:
- restare usabile handheld
- non essere enorme come una matte box cinema completa

Per questo tantissimi filmmaker seri:
- standardizzano 95mm
oppure
- saltano direttamente ai 4x5.65.

---

# Sul tuo setup specifico

Con:
- entity["product","Sony FX6","cinema camera"]
- entity["product","Sony Alpha 1","mirrorless camera"]
- 16-35 GM II
- 24-70 GM II

il 95mm avrebbe avuto molto senso come ecosistema unico.

Specialmente perché:
- entrambe le lenti sono già 82
- quindi lo step-up è minimo
- meccanicamente stabile
- nessun problema ottico reale

---

# Però attenzione

Questo NON significa che il tuo setup attuale sia sbagliato.

Anzi.

82mm Swift è ancora:
- molto pratico
- leggero
- veloce
- travel friendly
- perfetto per run & gun

Ed è probabilmente più coerente col tuo utilizzo reale attuale.

Perché un setup 95:
- cresce rapidamente di peso
- ingombro
- costo
- sbilanciamento

---

# La vera domanda è questa

Vuoi evolverti verso:
- filmmaking agile/documentary/commercial leggero

oppure verso:
- cine rig più completo e modulare?

Perché cambia totalmente il senso dell’investimento.

---

# Secondo me, conoscendo il tipo di lavori che fai

Tu sei in una zona ibrida:
- outdoor
- documentary
- branded
- travel
- run & gun evoluto
- ma con ambizioni visive molto cinematografiche

E lì il sistema Swift 82 è ancora molto intelligente.

Se invece iniziassi a fare:
- narrative
- commercial grossi
- set strutturati
- follow focus
- cine lenses
- matte box serie

allora probabilmente avrebbe più senso:
- 95mm uniforme
oppure direttamente:
- matte box + 4x5.65.

---

# Tradotto brutalmente

Per dove sei oggi:
82 Swift = ancora ottima scelta.

Per dove potresti andare tra qualche anno:
95 o matte box = più lungimiranti.