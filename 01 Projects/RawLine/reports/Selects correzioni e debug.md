# RawLine Selects: correzioni e 3 passaggi di debug

10 novembre 2026. Segue [[Selects fasi 1-4 da verificare]].

**Branch:** `selects/correzioni` (sopra `selects/panorami-scartate`), 50 commit da main, niente unito, niente push.
**Test sulla punta (7050779):** RawlineKit 613/613, Rename 143/143, Selects 278: nella suite intera falliscono 4 test a tempo (`aPhotoIsViewedAfterItsTime`, `aPhotoPassedQuicklyIsNotViewed`, `autoAdvanceWaitsThenMoves`, `holdingTheArrowReadsOnlyTheLast`); rilanciati da soli passano tutti (CullControllerTests 12/12 due volte, InspectorModelTests 9/9).

## Corretto (ogni difetto con un test visto fallire prima)
**I 6 importanti della revisione:** XMP che restava separato dal RAW; scarto ereditato da una foto nuova con lo stesso nome (ora conta l'identità del file); `_Scartate` in "Mostra tutte"; Rename che cancellava gli scarti d'orologio di Selects (ora lettura-modifica-scrittura sotto blocco, da tutte e due le app); ⌘Z/Riporta fuori dal thread principale; analisi fermate cambiando cartella.

**Passaggio 1 (integrità dei file):** "Riporta" non prende più dal Cestino un file di un'altra cartella con lo stesso nome; al ritorno XMP e JPEG non finiscono accanto a una foto nuova con lo stesso nome; una scartata ripresa in Lightroom (XMP cambiato) non va più nel Cestino alla chiusura; ⌘Q aspetta lo spostamento in corso.

**Passaggio 2 (concorrenza e prestazioni):** tornando su una scheda da 1.500 RAW non si rileggono più tutte le intestazioni (~20 s → 0,5 s). Verificato che cambi di scheda e chiusure fermano le analisi in 1–2 s, memoria stabile.

**Passaggio 3 (peso sul Mac e decisioni):** analisi di 1.503 ARW da **329 s di CPU a 17,7 s**, picco memoria da 659 a 498 MB, stessi risultati; miniature di Vision non più tutte in memoria; ricerca delle pile che riprende invece di ripartire, interruttori pile/panorami che la fermano davvero; foto dell'ora saltata dall'ora legale (fotocamera rimasta all'ora solare) che perdevano l'ora di scatto.

## Possibili problemi rimasti (minori, non corretti)
- **I 4 test a tempo** ormai falliscono spesso insieme sotto carico: vanno resi deterministici (orologio finto), altrimenti nascondono un difetto vero il giorno che c'è.
- **Proposta d'orologio, testo:** la scomposizione fuso/orologio a volte perde il verso o scrive "0 h 30 min"; lo scarto applicato è giusto.
- **Ora legale:** al ritorno all'ora solare (ottobre) una pila a cavallo delle 02:00 si spezza; telefono + fotocamera a cavallo del cambio danno due proposte a un'ora di distanza.
- **Panorami:** una raffica che segue uno sciatore può passare per panorama (si potrebbe escludere con la MakerNote "continuo").
- **Parole chiave:** dividendo una pila il numero va alla prima per nome, non alla più grande; unire e annullare dà un numero nuovo (mai collisioni).
- **Memoria:** dopo orologi + pile l'app può restare a ~865 MB a riposo (memoria liberata e non restituita, probabile Vision); una volta 2,47 GB dopo una sessione lunga, non riprodotto.
- **Scartate:** un gruppo spostato a metà con disco staccato o crash non è nel registro (Riporta non lo conosce); i sidecar `.dop`/`.pp3`/`.acr` non viaggiano col gruppo; con il pulsante rosso l'avviso arriva solo all'uscita; un ritorno rifiutato dice ancora "nothing was lost"; ⇧⌘Z dopo un ritorno vuoto può rifare un lotto più vecchio.
- **Cartelle recenti** sparite restano nell'elenco (dal triage): da decidere se cancellarle o mostrarle in grigio.
- **File › Chiudi scheda** non fa niente se Selects non è l'app attiva.

Dettagli con file:riga: rapporti `debug-passaggio-1/2/3.md` e `revisione-finale.md` nella scratchpad della sessione.

## Da provare a mano (Andrea)
- ⌘Z e Foto › Riporta sulle scartate con la finestra in primo piano, su una copia.
- Finestra Orologi (⌥⌘T): Accetta, ⌘Z, Correggi…, poi Rename › Impostazioni con Selects aperta insieme.
- Pile HDR e panorami: Invio/Esc, Dividi/Togli/Unisci.
- Lightroom: opzione parole chiave accesa, filtro `RawLine|HDR|…`, ⌘G.
- Tenerife: la ZV-1 era davvero ~39 min indietro rispetto all'RX100 VII?

## File di prova che servono
Bracketing veri A1/A9 III; 2–3 panorami a mano; tele + grandangolo nello stesso momento; un XMP di Lightroom con parole chiave gerarchiche. Misure in Release ancora da fare.

## Note
- Passaggio 2: un avvio di prova in primo piano ha ricevuto un tuo tasto (scheda di prova chiusa, app uscita normalmente, niente toccato). Da lì sempre `open -g`.
- Preferenze di Selects: tolte le 3 cartelle di prova dalle recenti (backup `selects-prefs-prima-pulizia.plist` in scratchpad).
- Spec `RawLine Selects.md` aggiornata solo fino alle correzioni; non committata nel vault.
