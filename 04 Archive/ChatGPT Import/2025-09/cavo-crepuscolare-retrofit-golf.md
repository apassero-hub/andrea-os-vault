---
title: "Cavo crepuscolare retrofit Golf"
created: 2025-09-25
updated: 2025-09-25
model: gpt-5
messages: 6
source: chatgpt-import
tags: []
---

# Cavo crepuscolare retrofit Golf

> Importato da ChatGPT export · 6 messaggi · gpt-5 · 2025-09-25

## 🧑 User

Sto cercando il devio luci per la golf per il retrofit fari automatici, cosa si intende per cavo crepuscolare? Mi serve?

---

## 🤖 Assistant

Il “cavo crepuscolare” di cui trovi menzione nei kit retrofit per fari automatici della Golf non è altro che il collegamento al **sensore luce/crepuscolare (spesso combinato anche con sensore pioggia)** che permette alla centralina di capire quanta luce ambientale c’è.

Ti spiego la logica:

- **Devio luci**: se prendi quello con la posizione “AUTO”, da solo non fa niente. È solo un selettore con più posizioni.
- **Sensore luce**: rileva l’intensità luminosa (giorno, notte, galleria). È montato dietro lo specchietto retrovisore interno, integrato nello stesso modulo che può includere anche il sensore pioggia.
- **Cavo crepuscolare**: è semplicemente il cablaggio che collega quel sensore alla BCM (Body Control Module), necessario se la tua auto non è già predisposta. Alcuni retrofit includono un piccolo cablaggio “plug&play” da infilare nel connettore sotto il devio luci per portare il segnale alla centralina.

👉 Quindi:
- Se la tua Golf **ha già il sensore pioggia/luci** dietro lo specchietto, il “cavo crepuscolare” non ti serve: basta cambiare il devio con quello con la posizione AUTO e attivare la funzione via OBD.
- Se invece **non hai sensore luce/crepuscolare**, il solo devio luci con AUTO non funziona. Devi montare anche il sensore + il suo cablaggio.

Vuoi che ti cerchi il kit esatto di retrofit per la tua Golf (specificando modello e anno), con devio + sensore + cavo, così ti dico cosa serve davvero alla tua?

---

## 🧑 User

Io ho solo il sensore di umidità del climatronic bizona

---

## 🤖 Assistant

Perfetto, allora la tua Golf **non ha già il sensore luce/crepuscolare**.

Quello che hai sul parabrezza (sensore umidità per il Climatronic bi-zona) serve solo al climatizzatore per evitare appannamenti, ma **non è in grado di leggere la luminosità esterna**.

Quindi:

- Se monti solo il **devio luci con posizione AUTO**, non succede niente: resterà un selettore “morto”.
- Per avere i fari automatici ti serve aggiungere il **sensore luce/crepuscolare** (spesso in kit insieme al sensore pioggia, con supporto specifico sul parabrezza).
- Di conseguenza serve anche il **cavo crepuscolare**, cioè il cablaggio che collega quel sensore alla BCM, perché l’impianto originale della tua macchina non lo prevede.

👉 In sintesi: nel tuo caso ti servono **devio luci con AUTO + sensore luce/crepuscolare + cablaggio dedicato**.
Poi va codificato il tutto via OBD (OBDeleven o VCDS) per attivare la funzione.

Vuoi che ti faccia uno schema con i codici dei componenti OEM (devio, sensore, cablaggio) specifici per Golf 7, così sai cosa comprare senza rischiare di prendere pezzi sbagliati?

---

## 🧑 User

Mi trovi il necessario per questo retrofit al miglior prezzo, usato ma originale

---

## 🤖 Assistant

Ecco l’elenco dei componenti necessari per abilitare i fari automatici sulla tua Golf VII (con Climatronic a doppia zona ma senza sensore luce/pioggia) e i relativi prezzi più convenienti trovati in rete per ricambi usati e originali.

### Comando luci (interruttore fari con posizione “AUTO”)
- Il comando luci sostituisce la manopola originale e introduce la posizione *AUTO*.
- Per le Golf 7 prodotte dal 2012 al 2016 il codice originale è **5G0 941 431 BF WZU** (variante con finitura nera/satinata).
- Trucksitaliana (autodemolitore italiano) propone un esemplare usato a **40 €** (IVA esclusa) con codice 5G0941431BF.
- Sul sito francese GPA si trova lo stesso comando luci usato a circa **35,06 €** IVA inclusa; entrambi sono ricambi originali Volkswagen.

### Sensore luce/pioggia/umidità
- È il modulo che rileva la luminosità esterna e l’umidità/precipitazioni, generalmente montato dietro lo specchietto interno.
- Per la Golf 7 il sensore utilizzato nei kit retrofit è indicato con **5Q0 955 547** o **5Q0 955 547 B**. Oltre a gestire i tergicristalli automatici, misura la luce per decidere quando accendere i fari.
- I ricambi usati non sono molto economici: Autoparts24 riporta sensori pioggia 5Q0 955 547 usati a **circa 183 €** IVA inclusa.
- In assenza di offerte più vantaggiose sull’usato, si può considerare il sensore nuovo: Navistore vende un sensore luce/pioggia originale VAG a **236 €**.

### Cablaggio (cavo crepuscolare)
- È il cablaggio che collega il sensore alla BCM; la tua vettura, avendo solo il sensore di umidità, non è predisposta.
- Naviservice fornisce un **“set cavi sensore luce, pioggia e umidità”** specifico per Golf 7 e altri modelli, codice *cable_set_rainlight*, a **29 € IVA inclusa**.
- Il kit è nuovo (difficile trovare cablaggi usati) e richiede codifica via OBD dopo l’installazione.

### Riepilogo prezzi

| Componente | Codice OEM | Prezzo indicativo (usato) | Fonte |
|---|---|---|---|
| Comando luci con posizione *AUTO* | 5G0 941 431 BF WZU | 35–40 € | Trucksitaliana, GPA |
| Sensore luce/pioggia/umidità | 5Q0 955 547 / 5Q0 955 547 B | ~183 € | Autoparts24 |
| Set cablaggi per sensore luce/pioggia/umidità (cavo crepuscolare) | cable_set_rainlight | 29 € (nuovo) | Naviservice |

### Consigli
1. **Verifica la compatibilità**: confronta i codici OEM con quelli della tua auto per evitare acquisti errati.
2. **Scegli il comando luci più economico**: il ricambio GPA da 35 € è il più conveniente trovato.
3. **Acquista il sensore usato se accetti un costo intorno ai 180 €**; in caso contrario valuta il componente nuovo a 236 €.
4. **Utilizza il cablaggio nuovo**: è economico e garantito.
5. **Codifica via OBD**: dopo il montaggio dei componenti, sarà necessario attivare la funzione fari automatici con un software come OBDeleven o VCDS.

Con questi tre elementi—comando luci con posizione *AUTO*, sensore luce/pioggia e cablaggio crepuscolare—potrai realizzare il retrofit dei fari automatici sulla tua Golf 7, utilizzando ricambi originali e contenendo al massimo il costo.