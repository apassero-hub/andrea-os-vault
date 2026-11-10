# Riconoscere bracketing e panoramiche dai metadati RAW (senza soglia di tempo chiesta all'utente)

Note di ricerca per RawLine Selects (Swift, macOS, ImageIO + parser propri). Nomi dei tag in inglese come in ExifTool; spiegazioni in italiano. Ricerca del 10 nov 2026; le tabelle ExifTool sono state lette direttamente da exiftool.org (alcune pagine solo in parte, lo segnalo).

## 1. Segnali EXIF standard: quanto valgono

### Takeaway
L'EXIF standard da solo basta a riconoscere un AEB "di macchina" solo quando la fotocamera scrive `ExposureMode = 2 (Auto bracket)`; per tutto il resto (posizione nel gruppo, dimensione del gruppo) serve la MakerNote o una ricostruzione da EV + tempo. `ExposureBiasValue`, i tempi/diaframmi/ISO e `SubSecTimeOriginal` sono i mattoni per l'euristica generica che funziona con ogni marca.

### Cited Findings
- `ExposureMode` (EXIF 0xA402): 0 = Auto, 1 = Manual, 2 = Auto bracket — [ExifTool EXIF Tags](https://exiftool.org/TagNames/EXIF.html) (valori standard EXIF; pagina non riletta in questa sessione, ma il valore 2 è confermato indirettamente dal progetto bracketed-image-finder che filtra proprio "exposure mode of (2) auto bracketed") — [dsoprea/bracketed-image-finder](https://github.com/dsoprea/bracketed-image-finder)
- ImageIO espone le chiavi EXIF standard (`kCGImagePropertyExifExposureMode`, `kCGImagePropertyExifExposureBiasValue`, `kCGImagePropertyExifSubsecTimeOriginal`, `kCGImagePropertyExifExposureTime`, `FNumber`, `ISOSpeedRatings`, `FocalLength`, `ExposureProgram`, `WhiteBalance`) — [Apple, EXIF Dictionary Keys](https://developer.apple.com/documentation/imageio/exif-dictionary-keys)
- PTGui calcola un EV per immagine da tempo, diaframma e ISO e cerca una sequenza di EV che si ripete; con AEB in Av/Tv (dove i tempi cambiano da un gruppo all'altro) ripiega sul campo EXIF "Exposure Bias" — [PTGui KB 101](https://ptgui.com/kb/101)
- Hugin, nel rilevamento automatico delle pile, confronta l'esposizione di base con una tolleranza "fuzzy" di 0,3 EV; in priorità di diaframma la deriva dell'esposimetro può spezzare un gruppo in due — [Hugin bug 679998 / mailing list](https://bugs.launchpad.net/hugin/+bug/679998), [hugin-devs](https://lists.launchpad.net/hugin-devs/msg05130.html)
- Uno sviluppatore Hugin suggerisce di usare DateTimeOriginal e tempo di posa come criterio di raggruppamento più affidabile — [hugin-devs](https://lists.launchpad.net/hugin-devs/msg05524.html)

### Inferences
- Affidabilità decrescente: (a) MakerNote con dimensione/posizione del gruppo (Sony SequenceLength, Panasonic BracketSettings, Canon BracketMode+BracketShotNumber, Olympus DriveMode "Shot N") > (b) `ExposureMode = 2` > (c) EV calcolato + `ExposureBiasValue` + vicinanza temporale. `ExposureMode=2` dice "questo scatto è parte di un AEB" ma non dice quanti né quale; molte marche lo scrivono, ma non ho trovato una tabella che garantisca che tutte le marche lo facciano su tutti i modelli (vedi Gaps).
- `ExposureProgram` è utile come discriminante: in M (1) l'AEB varia il tempo, in A (3) varia il tempo, in S (4) varia il diaframma (sconsigliato per HDR) — quindi l'EV va calcolato da tutti e tre i parametri, non solo dal tempo.
- `SubSecTimeOriginal` serve sempre: senza decimi di secondo, scatti a raffica cadono nello stesso secondo e l'ordine si perde; come fallback ordinare per contatore/nome file (bracketed-image-finder assume che l'ordine del nome file sia cronologico — [GitHub](https://github.com/dsoprea/bracketed-image-finder)).
- Formula EV pratica: EV100 = log2(N²/t) − log2(ISO/100). Differenze tra scatti adiacenti multipli di 1/3 EV (0,3/0,5/0,7/1/2/3) sono la firma di un bracket.

### Gaps
- Non ho una fonte che dica quali marche/modelli scrivono `ExposureMode=2` nei RAW e quali lasciano 0/1 durante l'AEB: va verificato sui file di prova di ogni marca.
- `kCGImagePropertyExifAuxImageNumber` (Exif Aux, "ImageNumber") esiste in ImageIO, ma non ho verificato in questa sessione quali marche lo popolano né se contenga il numero nella sequenza.

## 2. Campi MakerNote per marca (posizione e dimensione del gruppo) e cosa espone ImageIO

### Takeaway
ImageIO espone pochissimo delle MakerNote: per Canon solo `ContinuousDrive`, per Nikon `ShootingMode` (bitmask con il bit "Exposure Bracketing") e `ShutterCount`; i campi di posizione/dimensione del bracket vanno letti con un parser proprio della MakerNote. I segnali più ricchi: Sony (ReleaseMode/ReleaseMode2 + SequenceImageNumber + SequenceLength), Canon (FileInfo BracketMode/BracketValue/BracketShotNumber), Panasonic/Leica (BurstMode=2 + BracketSettings con numero di scatti + SequenceNumber), Olympus/OM (DriveMode con "AE Bracketing, Shot N"), Fujifilm (AutoBracketing + SequenceNumber), Nikon (ShootingMode bit 4 + ExposureBracketValue; dimensione nel MenuSettings dei soli Z recenti).

### Cited Findings

**Apple ImageIO (cosa arriva "gratis")**
- Dizionario Canon: solo `FlashExposureComp`, `ContinuousDrive`, `AspectRatioInfo`, `OwnerName`, `CameraSerialNumber`, `ImageSerialNumber`, `LensModel`, `Firmware` — nessuna chiave di bracketing — [Apple, Canon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/canon-camera-dictionary-keys)
- Dizionario Nikon: `ISOSetting`, `ISOSelection`, `ColorMode`, `Quality`, `WhiteBalanceMode`, `SharpenMode`, `FocusMode`, `FlashSetting`, `ImageAdjustment`, **`ShootingMode`**, `DigitalZoom`, **`ShutterCount`**, `FlashExposureComp`, `FocusDistance`, lens/serial — [Apple, Nikon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/nikon-camera-dictionary-keys)
- Non esistono dizionari ImageIO per Sony, Panasonic, Leica: per queste marche ImageIO dà solo EXIF standard (inferenza dall'assenza nella documentazione; Apple documenta dizionari maker per Apple, Canon, Nikon, Fuji, Olympus, Pentax, Minolta — elenco non riverificato voce per voce in questa sessione).

**Sony** (MakerNote, tag 0x9050/0x9400/0x2010 sono cifrati/"enciphered" in ExifTool; offset variano per modello)
- `ReleaseMode` 0xB049 (tabella principale): 0 Normal, 2 Continuous, **5 Exposure Bracketing**, 6 White Balance Bracketing, 8 DRO Bracketing, 65535 n/a — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- `SequenceNumber` 0xB04A: "shot number in continuous burst", 0 = Single, 65535 n/a — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- `ReleaseMode2` (in Tag9050a/b/c/d, Tag9400a/b/c, Tag9405b, Tag2010b–i): 0 Normal, 1 Continuous, **2 Continuous - Exposure Bracketing**, 3 DRO or WB Bracketing, 5 Continuous - Burst, 7 Continuous - Sweep Panorama, 9 Continuous - HDR, 13 3D Sweep Panorama, 15 High Resolution Sweep Panorama, 17 Burst 2, 19 Speed/Advance Priority, 20 Multi Frame NR, **23 Single-frame - Exposure Bracketing**, 26 Continuous Low… Offset: Tag9400c idx 9; Tag9400a/b idx 16; Tag9050b idx 75/107/109/115 (ILCE-6100…ILCE-9M2, ILCA-99M2); Tag9050c idx 75/107 (ILCE-1, 7SM3, FX3); Tag9050d idx 31 (ILCE-6700/7CM2/7CR/ZV-E1, anche ILCE-1M2/7M5/7RM6 con otturatore meccanico) — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- `ReleaseMode3` (Tag2010a–i): 0 Normal, 1 Continuous, **2 Bracketing**, 4 Burst, 5 Speed Priority, 6 Self-timer, 9 Single Burst Shooting. Offset Tag2010i (ILCE-7M3/7RM3/7RM4/9/9M2/6100/6400/6600/7C): 516 — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- **`SequenceImageNumber`** (posizione nel gruppo, int32u): Tag9400a/b idx 8, Tag9400c idx 18, Tag2010b–e idx 0, Tag9405b idx 36; **`SequenceFileNumber`**: Tag9400a/b idx 12, Tag9400c idx 26 — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- **`SequenceLength`** (dimensione del gruppo): Tag9400c idx 22: 0 Continuous, 1,2,3,4,5,6,7,9,10,12,16 shots, 100 iSweep Panorama, 200 Sweep Panorama; Tag9400a idx 34 / Tag9400b idx 30 (fino a 10 shots). Secondo campo "file" in Tag9400c idx 30 (1,2,3,5,7,9,10 files); nota ExifTool: per ILCE-7M5 gli offset successivi slittano di −1 — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- `ShotNumberSincePowerUp` (Tag9400a idx 26, 9400b idx 22, 9400c idx 10): include tutti gli scatti di modalità multi-shot — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- Modelli vecchi (A200…A900, A230…A390): `DriveMode` in CameraSettings (0x6 Single-frame Bracketing, 0x7 Continuous Bracketing, 0x18/0x28 WB, 0x19/0x29 DRO) e `ExposureBracketShotNumber` in FocusInfo idx 47; NEX/SLT 2010: DriveMode2 0x71/0x75 Continuous Bracketing 0.3/0.7 EV; CameraSettings3 `SweepPanoramaDirection` idx 51 — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- Panorama Sony (JPEG Sweep): sotto-tabella Panorama 0x1003 (PanoramaFullWidth/Height, Direction, Crop…) — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)

**Canon**
- **FileInfo** (tag 0x0093): idx 3 **`BracketMode`** 0 Off, 1 AEB, 2 FEB, 3 ISO, 4 WB; idx 4 **`BracketValue`**; idx 5 **`BracketShotNumber`**; idx 1 FileNumber/ShutterCount; idx 23 ShutterMode — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)
- ShotInfo (0x0004): idx 16 `AutoExposureBracketing` −1 On, 0 Off, 1/2/3 = On (shot 1/2/3); idx 17 `AEBBracketValue`; idx 9 `SequenceNumber` ("valid only for some models") — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)
- CameraSettings (0x0001): idx 5 `ContinuousDrive` 0 Single, 1 Continuous, 3 Speed Priority, 4 Low, 5 High, 6 Silent Single, 8 High+, 10 Silent; idx 50 `FocusBracketing` — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)
- CameraInfo 5D Mark II: idx 184 `AEBSequence` (0 = 0,-,+; 1 = -,0,+), idx 183 `AEBAutoCancel` (model-specific) — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)
- `BurstShotNumber` (CameraInfoR5m2 idx 3952): 1 per scatto singolo e primo della raffica, poi +1; ExifTool nota che su quei modelli SequenceNumber vale sempre 0 — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)
- Panorama (compatte Stitch Assist): tag 0x0005 PanoramaFrameNumber, PanoramaDirection (0 L→R, 1 R→L, 2 B→T, 3 T→B, 4 2x2) — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)

**Nikon**
- **`ShootingMode`** 0x0089 (bitmask): bit 4 = Exposure Bracketing, bit 6 = WB Bracketing, bit 8 = D-Lighting Bracketing. Esposto anche da ImageIO come `kCGImagePropertyMakerNikonShootingMode` — [ExifTool Nikon](https://exiftool.org/TagNames/Nikon.html), [Apple](https://developer.apple.com/documentation/imageio/nikon-camera-dictionary-keys)
- `ExposureBracketValue` 0x0019 (rational64s) e `FlashExposureBracketValue` 0x0018 — [ExifTool Nikon](https://exiftool.org/TagNames/Nikon.html)
- ShotInfo cifrato (0x0091, per modello): D810/D500 → BracketingInfo idx 15 `AEBracketingSteps` (codici tipo 0x85 = "3F0.3", fino a 0xd6 = "5F3": contiene numero fotogrammi e passo); D4S idx 5964; D500 ADLBracketingType; D800 `SequenceNumber` idx 1308 — [ExifTool Nikon](https://exiftool.org/TagNames/Nikon.html)
- Z6III (MenuSettings idx 838/840/842) e Z8 (554/556/558): `BracketSet` (0 AE/Flash, 1 AE…), **`BracketProgram`** (0 Disabled, 2/3/4/5/7/9 F = numero scatti), **`BracketIncrement`** (0.3…3.0) — [ExifTool Nikon](https://exiftool.org/TagNames/Nikon.html)
- MakerNotes0x56: `BurstShotNumber` idx 8, BurstStartImageNumber — [ExifTool Nikon](https://exiftool.org/TagNames/Nikon.html)
- `ShutterCount` 0xA7 (usato anche come chiave di decifratura di ShotInfo) e `ImageCount` 0xA5 — [ExifTool Nikon](https://exiftool.org/TagNames/Nikon.html)

**Fujifilm**
- `AutoBracketing` 0x1100: 0 Off, 1 On, 2 No flash & flash, 6 Pixel Shift (X-T3: 2 = Pre-shot); `SequenceNumber` 0x1101; `WhiteBalanceBracketing` 0x1102 — [ExifTool FujiFilm](https://exiftool.org/TagNames/FujiFilm.html)
- `DriveSettings` 0x1103: DriveMode (val & 0xff) 0 Single, 1 CL, 2 CH; DriveSpeed — [ExifTool FujiFilm](https://exiftool.org/TagNames/FujiFilm.html)
- `CompositeImageMode` 0x1150 (32 Panorama, 128 HDR, 1024 Multi-exposure), CompositeImageCount1/2; `PanoramaAngle` 0x1153, `PanoramaDirection` 0x1154; `ExposureCount` 0x1032; `ImageCount` 0x1438 — [ExifTool FujiFilm](https://exiftool.org/TagNames/FujiFilm.html)
- Apple ImageIO ha un dizionario Fuji (`kCGImagePropertyMakerFujiDictionary`) ma la documentazione Apple non elenca chiavi utili per il bracketing (non verificato voce per voce).

**Panasonic / Leica (Leica L e molte compatte usano la MakerNote Panasonic)**
- `BurstMode` 0x002A: 0 Off, 1 On, **2 Auto Exposure Bracketing**, 3 Focus Bracketing, 4 Unlimited, 8 WB Bracketing, 18 Aperture Bracketing ("decoding may vary by model") — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html)
- `SequenceNumber` 0x002B (posizione) — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html)
- **`BracketSettings`** 0x0045: 0 No Bracket, 1 "3 Images, 0/-/+", 2 "3 Images, -/0/+", 3 "5 Images, 0/-/+", 4 "5 Images, -/0/+", 5 "7 Images, 0/-/+", 6 "7 Images, -/0/+" → dà sia **dimensione** sia **ordine** — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html)
- `ShootingMode` 0x001F: 28 Panorama Assist, 62 Panorama; `SweepPanoramaDirection` 0x0093; `TimerRecording` 0x0096 (3 = Focus Bracketing); `HDR` 0x009E; `BurstSpeed` 0x0077 — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html)
- Le tabelle ExifTool "Panasonic Tags" valgono per Panasonic e Leica; le sezioni Leica2…Leica9 (M8, M9, M Typ 240, M10, S, X…) non definiscono campi di bracketing/sequenza — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html)

**Olympus / OM System**
- CameraSettings (0x2020) **`DriveMode` 0x0600** (int16u[n]): valori = modo, numero scatto, bit di modo, otturatore, (da E-M1 II) shooting mode. ExifTool: modo 0 Single Shot, 1 Continuous Shooting, 2 Exposure Bracketing, 3 WB Bracketing, 4 Exposure+WB; se il modo è 5 il bitmask decodifica 0 AE, 1 WB, 2 FL, 3 MF, 4 ISO, 5 AE Auto, 6 Focus "Bracketing"; se c'è il numero scatto aggiunge ", Shot N" — [ExifTool Olympus](https://exiftool.org/TagNames/Olympus.html), [Olympus.pm](https://raw.githubusercontent.com/exiftool/exiftool/master/lib/Image/ExifTool/Olympus.pm)
- `PanoramaMode` 0x0601: direzione (1 L→R, 2 R→L, 3 B→T, 4 T→B) + numero scatto — [Olympus.pm](https://raw.githubusercontent.com/exiftool/exiftool/master/lib/Image/ExifTool/Olympus.pm)
- `StackedImage` 0x0804: 5 4 = HDR1, 6 4 = HDR2, 8 8 = Tripod Hi-Res, 9 * = Focus-stacked, ND/GND live; `SpecialMode` 0x0200 (tabella principale): [modo (3 = Panorama), sequence number, direzione panorama] — [ExifTool Olympus](https://exiftool.org/TagNames/Olympus.html)

### Inferences
- Gerarchia di lettura per Selects: 1) segnale "è bracket" + "posizione" + "dimensione" dalla MakerNote se il parser lo copre; 2) se manca la dimensione (Canon, Fuji, Olympus, Nikon pre-Z), dedurla: il gruppo finisce quando la posizione torna a 1 (Canon BracketShotNumber, Olympus "Shot N", Sony SequenceImageNumber, Panasonic SequenceNumber); 3) fallback EXIF+EV+tempo.
- La posizione che "riparte da 1" è il segnale di confine più robusto di tutti e non richiede alcuna soglia di tempo.
- Nikon e Sony nuove hanno i campi utili in blocchi cifrati (ShotInfo Nikon, Tag9050/9400/2010 Sony): costo di implementazione alto, offset per modello. Il segnale Nikon gratuito via ImageIO è il bit 4 di ShootingMode; per Sony il segnale gratuito non cifrato è `ReleaseMode` 0xB049 + `SequenceNumber` 0xB04A nella tabella principale (da verificare che i modelli recenti li scrivano ancora).

### Gaps
- Le pagine ExifTool Canon e Nikon sono state lette solo in parte (troncamento): mancano ShotInfoZ9/ShotInfo02xx Nikon (i Z9/Z8 hanno probabilmente bracket in SeqInfo/ShotInfo) e RawBurstInfo Canon.
- `AEBracketCompensation`, `BracketShotNumber`, `ExposureBracketShotNumber` Nikon non compaiono nelle parti lette: non posso confermarne esistenza/ID.
- Leica M/Q/SL con MakerNote propria: nessun campo di bracketing documentato → per Leica affidarsi all'euristica EV+tempo (o a `ExposureMode=2` se presente).
- Sony: non verificato se `ReleaseMode` 0xB049 sia ancora popolato da ILCE-7M4/7RV/A1 II.

## 3. Bracket a mano (compensazione cambiata a mano, o solo tempo in M)

### Takeaway
Senza MakerNote il bracket manuale si riconosce come una corsa di scatti consecutivi con focale, diaframma, ISO, bilanciamento del bianco e obiettivo identici, EV che cambia a passi regolari (monotono o 0/−/+), e intervalli brevi *relativi al tempo di posa*; nessuno degli strumenti studiati lo fa senza soglia, ma la soglia si può derivare dai dati stessi.

### Cited Findings
- PTGui richiede una sequenza EV che si ripete con stesso numero di scatti per gruppo; per bracket irregolari serve il collegamento manuale ("Link Selected Images") o, da PTGui 13, "Link HDR Bracketed Exposures" con il numero di immagini per gruppo — [PTGui KB 101](https://ptgui.com/kb/101)
- bracketed-image-finder riconosce due schemi: "periodic" (0, −, +, −−, ++ … con ampiezza crescente a coppie) e "sequential" (da negativo a positivo, estremi simmetrici attorno a 0); gruppi validi di 3, 5 o 7 — [GitHub dsoprea](https://github.com/dsoprea/bracketed-image-finder)
- Una richiesta su Adobe Community propone di confrontare l'intervallo tra scatti con la durata del primo scatto invece di una soglia fissa — [Adobe Community, better auto-stacking](https://community.adobe.com/t5/idea-lightroom-classic/p-better-auto-stacking-for-bracketing-hdr-focus-stacking-and-panoramas/idi-p/12250005)
- Gli utenti segnalano che "Auto-Stack by Capture Time" fallisce con bracket a lunga esposizione (es. −3/0/+3 EV): nessun intervallo fisso funziona — [Adobe Community](https://community.adobe.com/questions-675/auto-stacking-doesn-t-group-bracketed-photos-965830)

### Inferences
- Soglia di tempo "auto-adattiva" (niente input utente): gap ammesso tra scatto i e i+1 = durata di posa dello scatto i + tempo di elaborazione/scrittura stimato (es. 0,5–2 s) + margine; oppure, meglio, stimare il "ritmo" della cartella: calcolare la distribuzione dei gap fra scatti consecutivi e cercare una valle (bimodale: gap da raffica/bracket di frazioni di secondo vs gap "umani" di secondi/minuti). Il taglio va messo nella valle (es. con Otsu o k-means a 2 cluster sul log del gap).
- Vincoli per un candidato bracket manuale: stesso corpo (serial), stesso obiettivo, stessa focale (±0,5 mm), stesso diaframma (in M/A), stesso ISO (salvo bracket ISO), stesso WB, stesso orientamento; EV con almeno 3 valori distinti, differenze multiple di 1/3 EV, escursione ≥ 1 EV; sequenza monotona o 0/−/+.
- Variante "solo tempo in M": `ExposureBiasValue` resta 0; l'EV va calcolato dal tempo → la regola deve basarsi su EV calcolato, non sul bias.
- Variante "compensazione a mano in A": il tempo cambia e cambia anche `ExposureBiasValue`; il bias è il segnale più pulito (passi esatti), l'EV calcolato fa da conferma.
- Confine del gruppo: ripetizione del valore EV di partenza (inizio di un nuovo ciclo 0/−/+) o ritorno a un EV già visto nel gruppo.

### Gaps
- Nessuna fonte con tassi di errore misurati per queste euristiche; vanno tarate su cartelle reali (Andrea: neve/montagna, Sony).

## 4. Panoramiche

### Takeaway
I metadati riconoscono con certezza solo le panoramiche "in camera" (Sweep Panorama Sony, Panorama Assist Panasonic, Olympus PanoramaMode, Fuji, Canon Stitch Assist), che spesso producono JPEG già cuciti. Le panoramiche fatte a mano in RAW si riconoscono solo per esclusione (esposizione, focale, WB costanti; tempi di qualche secondo) più un controllo di sovrapposizione delle immagini.

### Cited Findings
- Sony: ReleaseMode2 7/13/15 (Sweep / 3D / High-Res Sweep), SequenceLength 100/200, AspectRatio 5 = Panorama; sotto-tabella Panorama con dimensioni e direzione — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- Panasonic `ShootingMode` 28/62 e `SweepPanoramaDirection` 0x0093; Fuji `CompositeImageMode` 32 + `PanoramaDirection`; Olympus `PanoramaMode` 0x0601 con numero scatto e `SpecialMode` 3; Canon `PanoramaFrameNumber`/`PanoramaDirection` — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html), [FujiFilm](https://exiftool.org/TagNames/FujiFilm.html), [Olympus](https://exiftool.org/TagNames/Olympus.html), [Canon](https://exiftool.org/TagNames/Canon.html)
- Per i panorami Lightroom il raggruppamento per tempo "è un po' diverso ma vale la pena provarci" (commento community, non documentazione Adobe) — [Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/braketed-processing/m-p/12094405/highlight/true)
- Hugin raggruppa esposizioni diverse in "stack" e poi cerca punti di controllo tra le immagini per allinearle (align_image_stack) — [pixls.us, Aligning images with Hugin](https://pixls.us/articles/aligning-images-with-hugin)

### Inferences
- Segnale metadati per pano a mano: N ≥ 2 scatti consecutivi con tempo, diaframma, ISO, focale, WB *identici* (tipico di chi blocca l'esposizione in M per il pano), intervalli di 1–10 s, nessun flag di raffica/bracket. Il dato GPS/bussola (GPSImgDirection) quando presente aiuta: direzione che cambia in modo monotono = rotazione.
- Questo profilo coincide con "stessa scena scattata più volte" (scatti ripetuti): serve una verifica visiva leggera. Approccio economico: miniature 256–512 px (o il JPEG incorporato), calcolo di feature (Vision `VNGenerateImageFeaturePrintRequest` per similarità globale; `VNTranslationalImageRegistrationRequest` / `VNHomographicImageRegistrationRequest` per lo spostamento). Pano = alta similarità *parziale* con traslazione orizzontale/verticale importante (es. 20–70 % del lato) tra scatti adiacenti; scatti ripetuti = traslazione ~0; bracket = traslazione ~0 ma luminanza diversa.
- Combinazioni pano+bracket (HDR pano): gruppi bracket in successione con traslazione tra un gruppo e l'altro → trattare a due livelli (prima bracket, poi catena di bracket).

### Gaps
- Non ho trovato documentazione ufficiale di come Lightroom/PTGui/Hugin rilevino automaticamente che un insieme è un panorama prima di cucirlo: in genere l'utente lo seleziona. Le soglie di sovrapposizione indicate sopra sono una mia proposta, non tratte da fonti.
- Le API Vision citate sono note dalla documentazione Apple ma non riverificate in questa sessione.

## 5. Raffica vs bracket vs panorama

### Takeaway
La distinzione si fa su tre assi: varia l'esposizione? (bracket sì, raffica e pano no), varia l'inquadratura? (pano sì, raffica poco, bracket no), quanto sono vicini gli scatti? (raffica/bracket frazioni di secondo, pano secondi). I flag MakerNote (Sony ReleaseMode2 1/5 vs 2/23, Panasonic BurstMode 1 vs 2, Canon ContinuousDrive vs BracketMode, Fuji DriveMode vs AutoBracketing, Olympus DriveMode modo 1 vs 2/5) separano raffica e bracket in modo diretto.

### Cited Findings
- Sony distingue Continuous (1), Burst (5), Exposure Bracketing continuo (2) e single-frame (23), Sweep Panorama (7) in un solo campo ReleaseMode2; `SequenceLength` 0 = Continuous (raffica senza lunghezza fissa) vs 3/5/7/9 shots — [ExifTool Sony](https://exiftool.org/TagNames/Sony.html)
- Panasonic BurstMode 1 On vs 2 AEB vs 3 Focus Bracketing — [ExifTool Panasonic](https://exiftool.org/TagNames/Panasonic.html)
- Canon: ContinuousDrive descrive la cadenza; il bracket è in FileInfo BracketMode — i due coesistono (AEB scattato in raffica) — [ExifTool Canon](https://exiftool.org/TagNames/Canon.html)
- Fuji: DriveMode (CL/CH) separato da AutoBracketing — [ExifTool FujiFilm](https://exiftool.org/TagNames/FujiFilm.html)

### Inferences
- Regola: drive continuo + EV costante = raffica; EV a passi regolari (con o senza drive continuo) = bracket; EV costante + gap di secondi + traslazione dell'inquadratura = pano candidato. Il focus bracketing (Panasonic BurstMode 3, Olympus bit "Focus", Canon FocusBracketing, Nikon FocusShiftShooting) è un quarto tipo da tenere separato: EV costante, focale costante, distanza di messa a fuoco che varia.
- Una raffica lunga a esposizione automatica può avere piccole variazioni di EV (±0,3): richiedere passi ≥ 0,3 EV *e* escursione totale ≥ 1 EV evita falsi bracket.

### Gaps
- Nessuna fonte confronta quantitativamente questi criteri.

## 6. Come fanno gli altri strumenti

### Takeaway
Nessuno strumento noto raggruppa senza soglia: Photomatix usa i metadati con uno slider "tempo massimo tra due fotogrammi" (0,5–64 s), Lightroom usa solo il tempo (Auto-Stack by Capture Time, soglia scelta dall'utente), PTGui cerca una sequenza EV ripetuta con numero fisso per gruppo, Hugin usa l'EV con tolleranza 0,3. Usare la MakerNote + una soglia derivata dai dati sarebbe un vantaggio concreto di RawLine.

### Cited Findings
- Photomatix Pro, batch "Automatically detect number of bracketed frames": usa i metadati, si può limitare il numero di fotogrammi e regolare "Maximum time between two bracketed frames" (min ½ s, max 64 s); pensato per cartelle con gruppi di dimensione variabile o altri file — [Photomatix Pro 7 manual, batch](https://www.hdrsoft.com/support/doc/photomatix-pro/v7/batch-processing.html), [HDRsoft real-estate tutorial](https://www.hdrsoft.com/real-estate/hdr-interior-tutorial-part3.html)
- PhotomatixCL (riga di comando) non ha il rilevamento automatico: richiede gruppi di uguale numero — [PhotomatixCL](https://hdrsoft.com/download/photomatixcl.html)
- Il plugin HDR Batch di Photomatix per Lightroom si basa sulle pile di Lightroom; il tutorial suggerisce Auto-Stack by Capture Time con circa 2 s — [HDRsoft Lightroom plugin tutorial](https://www.hdrsoft.com/resources/hdr-batch-plugin-for-lightroom-tutorial.html)
- Lightroom: Auto-Stack by Capture Time solo su tempo; utenti chiedono da anni lo stacking per numero di immagini o per bracket — [Adobe Community feature request](https://community.adobe.com/feature-requests-681/p-auto-stacking-by-capture-time-661611); fallimenti con lunghe esposizioni — [Adobe Community](https://community.adobe.com/questions-675/auto-stacking-doesn-t-group-bracketed-photos-965830)
- PTGui: sequenza EV ripetuta, uguale numero per gruppo; fallback su Exposure Bias in Av/Tv (PTGui Pro 12+) — [PTGui KB 101](https://ptgui.com/kb/101)
- Hugin: rilevamento automatico delle pile introdotto con 2015.0beta1, tolleranza 0,3 EV sull'esposizione di base — [Launchpad bug 679998](https://bugs.launchpad.net/hugin/+bug/679998), [hugin-devs](https://lists.launchpad.net/hugin-devs/msg05130.html)
- HDR-Merge (Blender/align_image_stack): il primo gruppo determina il numero di immagini per gruppo; dimensioni miste non supportate — [GitHub gregzaal/HDR-Merge](https://github.com/gregzaal/HDR-Merge)
- bracketed-image-finder: ExposureMode = 2 + schemi EV, ordine per nome file — [GitHub dsoprea](https://github.com/dsoprea/bracketed-image-finder)

### Inferences
- Algoritmo proposto per Selects, senza soglia utente:
  1. Ordina per DateTimeOriginal+SubSecTimeOriginal (fallback contatore/nome file), separa per seriale camera.
  2. Passo "certo": se la MakerNote dà posizione (e dimensione) → chiudi il gruppo quando la posizione torna a 1 o raggiunge la dimensione. Tipi: bracket / raffica / pano in-camera / focus.
  3. Passo "probabile": corse di scatti con `ExposureMode=2` o con EV a passi regolari (≥3 valori, passi multipli di 1/3, escursione ≥1 EV), parametri fissi uguali, gap ≤ soglia adattiva (durata posa + valle della distribuzione dei gap della cartella).
  4. Passo "pano candidato": corse con esposizione identica e gap di secondi, confermate da registrazione delle miniature (traslazione significativa).
  5. Mostra i gruppi trovati con livello di confidenza (certo/probabile) e lascia correggere, invece di chiedere la soglia prima.
- Vantaggio rispetto alla concorrenza: Photomatix e Lightroom chiedono comunque una soglia temporale; la MakerNote (soprattutto Sony, il corredo di Andrea) permette confini esatti.

### Gaps
- Aurora HDR, darktable, digiKam e RawTherapee: non ho trovato in questa sessione documentazione sul raggruppamento automatico dei bracket (per limiti di tempo/ricerca); da quanto risulta in generale nessuno dei tre open source ha un raggruppamento automatico documentato, ma non è verificato. Aurora HDR è stato dismesso da Skylum (non verificato in questa sessione).
- GroupForHDR (GitHub) dichiara di raggruppare bracket per EXIF per il real estate, ma il codice non è stato esaminato.
