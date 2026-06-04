---
title: "Problema telecomando Golf 7"
created: 2025-10-03
updated: 2025-10-03
model: gpt-5
messages: 10
source: chatgpt-import
tags: []
---

# Problema telecomando Golf 7

> Importato da ChatGPT export · 10 messaggi · gpt-5 · 2025-10-03

## 🧑 User

Mi è capitata una cosa strana con la Golf di mio padre ovvero che abbiamo cambiato la batteria e adesso non apre più la macchina cioè la chiave funziona perfettamente la macchina si accende se la apro nel lottolino la macchina si apre tutto a posto, anche la sua Golf 7 anzi la 7.5 del 2017 però dal telecomandino della macchina c'è la chiave, non apre più la macchina e non la chiude

---

## 🤖 Assistant

Quello che descrivi è piuttosto tipico dopo un cambio batteria sulla Golf 7/7.5. Non riguarda la chiave in sé, ma la **sincronizzazione del telecomando con la centralina comfort** (Kessy o modulo chiusura). In pratica:

- L’auto si avvia perché il transponder RFID della chiave viene comunque letto dall’antenna nell’accensione.
- Ma la parte radiocomando (apri/chiudi a distanza) si è “persa” durante il distacco della batteria.

### Cosa puoi provare subito
1. **Resincronizzazione manuale**
- Entra in auto con la chiave.
- Chiudi manualmente le portiere.
- Metti la chiave nel quadro e gira su “ON” senza avviare.
- Premi un tasto del telecomando (apri/chiudi) per 5–10 secondi.
- Spegni e prova a usare la chiave dall’esterno.

2. **Reset semplice**
- Premi il pulsante di apertura/chiusura sul telecomando mentre apri o chiudi manualmente con la chiave nella serratura. Spesso basta per far riprendere la comunicazione.

3. **Controlla la batteria interna del telecomando**
- A volte, dopo lo stacco della batteria auto, la pila del telecomando già un po’ scarica non regge più bene. Vale la pena sostituirla (CR2032).

### Se non funziona
- Va fatta una **nuova codifica del telecomando via OBD** con strumenti tipo VCDS o OBDeleven.
- In rari casi, se c’è stata una caduta di tensione brusca, la centralina comfort può aver registrato errori che bloccano il radiocomando: si risolve cancellando i DTC e ripetendo la sincronizzazione.

Vuoi che ti scriva passo passo la procedura per ricodificare il telecomando con OBDeleven, così te la fai da solo senza andare in concessionaria?

---

## 🧑 User

Guarda che la Golf non ha un tasto a caso, che sia o l'apri o il chiudi. Ovviamente sono due tasti separati.

---

## 🤖 Assistant

Hai ragione, mi sono espresso male: sulla Golf 7/7.5 ci sono **due tasti distinti** (apri e chiudi), più eventualmente il tasto bagagliaio.
Il concetto è che per la resincronizzazione puoi usare **uno qualsiasi dei due principali (apri o chiudi)**, l’importante è che venga inviato un segnale mentre la centralina è in “ascolto” (quadro acceso).

Quindi la sequenza corretta è:

1. Entra in auto con la chiave.
2. Chiudi manualmente le porte.
3. Gira la chiave su quadro acceso (posizione ON, senza avviare).
4. Premi e tieni premuto per alcuni secondi **il tasto di apertura o quello di chiusura** sul telecomando.
5. Spegni, togli la chiave e prova di nuovo ad aprire/chiudere da fuori.

Se non riprende così, la sincronizzazione “rapida” non basta e serve fare l’adattamento con OBD.

Vuoi che ti scriva la procedura completa passo-passo con OBDeleven per associare di nuovo il telecomando alla centralina comfort?

---

## 🧑 User

Comunque questa cosa non lo sapevo. La mia, non so, la batteria l'avrò cambiata tre o quattro volte. Mai avuto questo problema.

---

## 🤖 Assistant

Esatto, ed è proprio questo il punto: non sempre succede.

Ti spiego perché:
- Quando stacchi e riattacchi la batteria, se la centralina **perde completamente alimentazione** (specialmente se resta senza tensione per un po’ o se la batteria nuova viene collegata con un piccolo “arco”), può cancellare le associazioni temporanee con i telecomandi.
- In altri casi, se la sostituzione è rapida o se usi un mantenitore di memoria (tipo un piccolo alimentatore a 12V messo in OBD o sull’accendisigari), la centralina non perde i dati e tutto continua a funzionare.
- Per questo sulla tua Golf non ti è mai capitato: probabilmente la batteria non è mai stata staccata abbastanza a lungo da far “dimenticare” la chiave, oppure la centralina della tua (più vecchia) è leggermente meno sensibile.

Sulla 7.5 (dal 2017 in poi) invece i moduli comfort/Kessy sono un po’ più “delicati” a questi reset, e capita più spesso che il telecomando perda la sincronizzazione.

Vuoi che ti spieghi come fare in modo che la prossima volta non capiti (trucchetto del mantenitore memoria)?

---

## 🧑 User

No, no, no. Fammi spiegar meglio. La macchina in cui ho cambiato la batteria dell'auto, quindi la batteria per l'accensione del veicolo, è la mia. E sulla mia non mi ha dato mai nessun tipo di problema. Anzi, anche oggi che ho messo la batteria nuova, batteria dell'auto, il telecomandino ha sempre continuato a funzionare, sia prima, sia dopo. Su quella di mio padre, invece, in cui la batteria dell'auto non è stata sostituita, ma ha soltanto cambiato, diciamo, le due CR2025, che sono all'interno dei due telecomandini. Uno l'ho ancora provato, ma l'altro, che è quello che mio padre lo usava di solito, non apre più la macchina. Ma, appunto, le centraline non hanno subito un reset, le centraline dell'auto, perché la batteria non è stata toccata, non è stata staccata, non è stato modificato niente. Solo cambiato due piccole pile dei telecomandi, perché erano scarichi.

---

## 🤖 Assistant

Ah, chiaro adesso. Quindi:

- La tua Golf → batteria auto cambiata più volte → nessun problema coi telecomandi.
- Quella di tuo padre (Golf 7.5, 2017) → **non è stata toccata la batteria dell’auto**, avete cambiato solo le pile CR2025 dei telecomandi → uno funziona, l’altro no.

In questo caso la logica cambia: non c’entra la centralina che ha perso memoria, ma solo **il telecomando** che dopo il cambio pila non si è più risincronizzato correttamente. Capita se:
- durante il cambio pila il telecomando è rimasto troppo tempo senza alimentazione,
- i contatti metallici non sono perfettamente appoggiati,
- oppure la scheda interna del telecomando si è leggermente “spostata” e non trasmette più correttamente.

### Cose da provare subito
1. **Resincronizzazione manuale** (vale anche qui):
- Apri l’auto manualmente con la chiave meccanica.
- Metti il quadro su ON.
- Premi uno dei tasti (apri o chiudi) per qualche secondo.
- Spegni e riprova dall’esterno.

2. **Verifica la pila**
- Sicuro CR2025 e non CR2032? Su alcune Golf 7.5 i telecomandi montano CR2032. Se metti la 2025 funziona lo stesso ma con meno contatto e meno autonomia → a volte fa falso contatto.
- Controlla che la pila sia messa dal lato giusto (polo + verso il basso, nella maggior parte dei modelli).

3. **Pulizia contatti**
- Se i lamellini che toccano la pila si sono piegati, il telecomando non prende alimentazione → basta alzarli leggermente con un cacciavitino.

4. **Test incrociato**
- Quello che funziona → conferma che la macchina e la centralina ricevono.
- Quello che non va → è solo questione del telecomando.

Se dopo questi tentativi non funziona, probabilmente bisogna **ricodificarlo alla macchina via OBD** (VCDS/OBDeleven).

Vuoi che ti scriva la procedura OBD passo-passo così verifichi se riesci a farlo ripartire senza andare in concessionaria?

---

## 🧑 User

Ah, posso rifarlo anche quella parte lì con lo BD11.

---

## 🤖 Assistant

Esatto. Se il telecomando non riparte con la procedura manuale, con **OBDeleven** puoi forzare l’adattamento e ricollegarlo alla centralina comfort.

Su Golf 7/7.5 la procedura è questa:

---

### 🔧 Procedura ricodifica telecomando con OBDeleven
1. **Collega OBDeleven** e accendi il quadro (senza avviare).
2. Vai su **Centralina 09 – Cent. elettrica (Central Electrics / BCM)**.
3. Entra in **Adattamenti (Adaptation)**.
4. Cerca la voce **Remote control adaptation** o **Key adaptation** (dipende dalla traduzione della tua app).
- In alcuni casi si trova sotto *“Remote control key → add key”*.
5. Avvia la funzione “Aggiungi telecomando”.
- OBDeleven ti chiederà di premere un tasto del telecomando che vuoi associare.
- Premi il **tasto apri o chiudi** sul telecomando da programmare.
6. Conferma. La centralina dovrebbe memorizzarlo subito.
7. Esci, spegni il quadro, prova il telecomando dall’esterno.

---

### Nota importante
- Se hai più chiavi, conviene **ricodificarle tutte insieme** nella stessa sessione, perché alcune centraline sovrascrivono la lista.
- Se non lo aggiungi, rischi che resti memorizzata solo quella funzionante.
- Se la procedura non va a buon fine, prova a cancellare errori (DTC) e ripetere.

---

Vuoi che ti scriva la sequenza di menu **così come compare passo passo su OBDeleven in italiano**, così la trovi subito senza perderti nei sottomenù?