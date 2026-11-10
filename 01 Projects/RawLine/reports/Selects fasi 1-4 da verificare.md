# RawLine Selects, fasi 1–4: cosa verificare e possibili problemi

10 novembre 2026. Branch in fila, nessuno unito in main, niente push:
`selects/ordine-ora` → `selects/pile-hdr` → `selects/ora-proposta` → `selects/panorami-scartate` (31 commit, 93 file).

Test sulla punta: RawlineKit 598/598, Rename 142/142, Selects 250 (solo `aPhotoIsViewedAfterItsTime`, instabile noto, fallisce in suite e passa da solo).
Revisione indipendente di tutto il diff: nessun difetto critico (nessuna cancellazione definitiva, nessuna sovrascrittura, XMP atomici, parser MakerNote sicuro). Rapporto completo della revisione: scratchpad `revisione-finale.md`.

## Difetti importanti da correggere prima di unire
1. **XMP separato dal RAW** — mentre le scartate si spostano, una scrittura di parole chiave in coda può ricreare un `A.xmp` vuoto al vecchio posto; al ritorno l'XMP vero (con le regolazioni) non rientra.
2. **Foto mai scartate spostate** — lo scarto è legato al percorso: una foto nuova con lo stesso nome nella stessa cartella lo eredita; con "Ricorda per questa cartella" finisce in `_Scartate`/Cestino senza avviso.
3. **"Mostra tutte" rimette in griglia `_Scartate`** — le scartate spostate ricompaiono, contano e entrano nelle pile.
4. **Rename può cancellare gli scarti d'orologio scritti da Selects** — le sue Impostazioni caricano la tabella solo all'apertura e poi la riscrivono intera (verificato nel codice).
5. **⌘Z sulle scartate può bloccare l'app** — sul thread principale rilegge il diario per ogni file; su diari grandi girandola lunga.
6. **Le analisi non si fermano cambiando cartella** — MakerNote e Vision continuano sulla vecchia e si accumulano.

## Minori (14)
Ritorno e ⇧⌘Z non tutto-o-niente per gruppo; riga troncata del diario fa perdere la successiva; messaggio "niente perso" anche a Cestino svuotato; voto sulla pila chiusa tocca anche fotogrammi nascosti dal filtro; file comune rovinato → tabella vuota in Rename; chiavi future della tabella perse; ⌘Z sfasato dopo "Riporta"; pile e orologi rifatti dopo ogni spostamento; immagini Vision liberate a metà dall'altra analisi; calcoli delle scartate sul thread principale; restano "RawLine" e "HDR" come parole chiave piatte; "Togli le parole chiave" usa solo il registro locale; `_Scartate` vuota con `.DS_Store` resta; avvisi doppi chiudendo due volte la scheda.

## Da provare a mano (Andrea)
- **Ordine e orologi:** finestra Orologi (⌥⌘T): Accetta, ⌘Z, Correggi…; poi Rename › Impostazioni mostra lo scarto. Tenerife: la ZV-1 era davvero ~39 min indietro rispetto all'RX100 VII?
- **Pile HDR:** Invio/Esc, Spazio, Dividi/Togli/Unisci, ⌘Z su una pila vera.
- **Panorami:** apertura e chiusura come le HDR.
- **Scartate:** chiudere una scheda con scartate (avviso, `_Scartate`, Cestino, ⌘Z, Foto › Riporta le scartate spostate). Solo su una copia.
- **Lightroom:** accendere l'opzione parole chiave, aprire in Lightroom, filtro per `RawLine|HDR|…`, ⌘G.
- Pulsante rosso della finestra: l'avviso scartate arriva solo all'uscita dell'app (limite noto).

## File di prova che servono
- Bracketing veri A1 / A9 III (3, 5, 7 scatti; M e A; singolo e continuo), un interno a tempi lunghi, foto singole prima e dopo.
- 2–3 panorami a mano (orizzontale e verticale, 4–8 scatti in M) con scatti prima e dopo.
- Una cartella con tele e grandangolo nello stesso momento, meglio con l'orologio del telefono fotografato da ogni corpo.
- Un sidecar Lightroom con parole chiave gerarchiche.

## Altre note
- La fase 4 ha premuto i pulsanti dell'avviso con l'accessibilità di macOS (AXPress), senza mouse né tastiera, sulla build Debug.
- Spec `RawLine Selects.md` aggiornata (§4.4, §4.5, §4.7) ma non committata nel vault.
- Gran Paradiso Trail: online su gran-paradiso-trail.pages.dev; manca la `ADMIN_KEY` (la imposti tu), poi va ripubblicato.
