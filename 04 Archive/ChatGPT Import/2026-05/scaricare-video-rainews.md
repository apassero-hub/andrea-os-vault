---
title: "Scaricare video RaiNews"
created: 2026-05-04
updated: 2026-05-04
model: gpt-5-3
messages: 10
source: chatgpt-import
tags: []
---

# Scaricare video RaiNews

> Importato da ChatGPT export · 10 messaggi · gpt-5-3 · 2026-05-04

## 🧑 User

vorrei scaircare questo video in alta qualità come posso fare? https://www.rainews.it/tgr/vda/video/2025/12/la-traccia-di-toni-e7c40917-fbac-4dd2-8680-42fecb64d413.html?wt_mc=2.www.wzp.rainews

---

## 🤖 Assistant

Qui non serve girarci intorno: i video di entity["organization","RaiNews","portale informativo Rai"] (inclusi quelli TGR come il tuo) **non hanno un pulsante ufficiale per il download in alta qualità**. Sono stream protetti, non file scaricabili direttamente. cite

Detto questo, hai tre strade pratiche.

---

## 1) Metodo migliore (qualità massima reale)
Apri la pagina del video:
👉 link_titleApri il video su RaiNews

Poi:
1. Apri **DevTools** (tasto destro → Ispeziona)
2. Vai su **Network**
3. Filtra per:
- `m3u8` oppure `mp4`
4. Avvia il video
5. Trova il file `.m3u8` (è lo stream HLS)
6. Copia il link

A quel punto usa **ffmpeg** (metodo professionale):

```bash
ffmpeg -i "URL_DEL_FILE_M3U8" -c copy -bsf:a aac_adtstoasc output.mp4
```

👉 Risultato: **video originale, senza perdita**, stessa qualità dello stream Rai.

---

## 2) Metodo semplice (senza sbattimenti)
Usa un downloader compatibile con HLS:

- yt-dlp (consigliato)
```bash
yt-dlp "URL pagina"
```

Oppure incollando direttamente l’URL m3u8 se lo hai trovato.

✔ Funziona bene con Rai
✔ Prende automaticamente la qualità più alta disponibile

---

## 3) Metodo rapido ma meno pulito
- Estensioni browser tipo Video DownloadHelper
- Oppure registrazione schermo (ultima spiaggia)

✘ Qualità inferiore
✘ Compressione
✘ Non è il file originale

---

## Nota importante
- I video Rai sono spesso in **HLS adattivo**, quindi non esiste un “file unico” da scaricare: devi ricostruirlo (ffmpeg/yt-dlp).
- La qualità massima dipende da cosa Rai ha caricato (di solito 720p o 1080p, raramente di più).

---

Se vuoi, passami il link diretto allo stream (m3u8) oppure uno screenshot del Network e ti dico esattamente quale file prendere senza perdere tempo.

---

## 🧑 User

_[contenuto non testuale: image_asset_pointer]_

---

## 🤖 Assistant

Perfetto, sei nel punto giusto.
Quello che stai vedendo (**file `.ts` tipo `seg-6-v1-a1.ts`**) conferma una cosa precisa:

👉 è uno **stream HLS segmentato**, non un file MP4 diretto
👉 quindi così com’è NON lo devi scaricare pezzo per pezzo

---

## Dove stai sbagliando (normale)
Hai filtrato per `mp4`, ma:

- Rai usa **.m3u8 + segmenti.ts**
- il file giusto NON è nei `.ts`
- devi trovare il **manifest `.m3u8`**

---

## Procedura corretta (veloce)

### 1. Cambia filtro
Nel tab Network:
- cancella `mp4`
- cerca:
```
m3u8
```

Oppure:
- filtro “Media”

---

### 2. Ricarica la pagina (IMPORTANTE)
Con Network aperto:
- premi refresh
- fai partire il video

---

### 3. Trova il file giusto
Cerca qualcosa tipo:
```
index.m3u8
master.m3u8
playlist.m3u8
```

👉 quello è il file chiave

---

### 4. Copia URL
Click destro → Copy → Copy link address

---

## 5. Download (metodo serio)

Con **yt-dlp** (più semplice):

```bash
yt-dlp "URL_M3U8"
```

Oppure direttamente pagina (spesso funziona):

```bash
yt-dlp "https://www.rainews.it/..."
```

---

## Alternativa pro (più pulita)

```bash
ffmpeg -i "URL_M3U8" -c copy -bsf:a aac_adtstoasc output.mp4
```

---

## Nota importante
Se non trovi il `.m3u8`:

- togli tutti i filtri
- cerca solo:
```
m3u
```

oppure:
```
playlist
```

---

## Quello che vedo dal tuo screenshot
- Stai vedendo solo segmenti (`.ts`)
- Quindi il `.m3u8` è **più in alto nella lista o filtrato fuori**

---

Se vuoi fare veloce:
mandami uno screen con filtro **vuoto** o con `m3u8` e ti dico esattamente quale link prendere, senza tentativi.

---

## 🧑 User

con m3u8 non trova niente

---

## 🤖 Assistant

Perfetto, situazione chiarissima: Rai spesso **non espone direttamente `.m3u8` con quel nome**, oppure viene caricato in modo “nascosto”.

Quello che vedi (segmenti `.ts`) conferma al 100% che **lo stream esiste**, ma devi intercettarlo nel modo giusto.

Ti dico cosa fare senza perdere tempo.

---

## Metodo più rapido (funziona quasi sempre)
Lascia perdere DevTools.

Usa direttamente:

```bash
yt-dlp "https://www.rainews.it/tgr/vda/video/2025/12/la-traccia-di-toni-e7c40917-fbac-4dd2-8680-42fecb64d413.html"
```

Se vuoi il massimo:

```bash
yt-dlp -f bestvideo+bestaudio "URL"
```

👉 yt-dlp è già ottimizzato per Rai
👉 spesso trova lo stream anche quando tu non lo vedi

---

## Se NON funziona (caso 2)
Allora torniamo su DevTools, ma fatto bene:

### 1. Togli il filtro `mp4`
### 2. Metti:
```
v1
```
oppure:
```
index
```

Oppure guarda nella tab:
👉 **“Media”**

---

## Trick che quasi nessuno usa (ma è quello giusto qui)

Click su uno dei `.ts` (tipo `seg-10-v1-a1.ts`)

Poi:
- vai su **Headers**
- guarda **Request URL**

Vedrai qualcosa tipo:
```
https://.../v1/seg-10-v1-a1.ts
```

👉 Ora fai questo:

1. Cancella la parte finale (`seg-...ts`)
2. Torna indietro di una cartella

Deve diventare qualcosa tipo:
```
https://.../v1/
```

3. Prova ad aggiungere:

```
index.m3u8
```

👉 esempio finale:
```
https://.../v1/index.m3u8
```

---

## Perché funziona
- `.ts` = pezzi video
- `.m3u8` = lista che li unisce
- Rai spesso non mostra il manifest direttamente

---

## Metodo brutale ma efficace
Se vuoi zero sbatti:

```bash
yt-dlp -v "URL"
```

👉 modalità verbose
👉 ti stampa direttamente lo stream `.m3u8` trovato

---

## Conclusione chiara
- Non stai sbagliando: Rai nasconde il manifest
- Hai già tutto quello che serve (i `.ts`)
- Devi solo risalire allo **stream padre**

---

Se vuoi chiuderla in 1 minuto:
mandami lo screenshot del **Request URL completo di uno dei `.ts`**
e ti ricavo io direttamente il link finale pronto da incollare.

---

## 🧑 User

ma da terminale dici?

---

## 🤖 Assistant

Sì, esatto: **da terminale**. È il modo più diretto e pulito.

Vado dritto al punto.

---

## Metodo consigliato (30 secondi)

### 1. Installa entity["software","yt-dlp","video downloader CLI"] (se non lo hai)

Su Mac:
```bash
brew install yt-dlp
```

---

### 2. Scarica il video

```bash
yt-dlp "https://www.rainews.it/tgr/vda/video/2025/12/la-traccia-di-toni-e7c40917-fbac-4dd2-8680-42fecb64d413.html"
```

👉 Fine.
Nella maggior parte dei casi funziona subito e prende la qualità massima disponibile.

---

## Se vuoi controllo totale (qualità massima reale)

```bash
yt-dlp -F "URL"
```

Ti mostra tutte le qualità disponibili.

Poi scegli (esempio):
```bash
yt-dlp -f bestvideo+bestaudio "URL"
```

---

## Dove ti salva il file
Nella cartella in cui sei nel terminale.
Se vuoi specificare:

```bash
yt-dlp -o "~/Desktop/video.mp4" "URL"
```

---

## Quando NON funziona (raro ma possibile)
Allora passi a:
- ffmpeg con m3u8
- oppure debug con `-v`

Ma prima prova così: nel 90% dei casi Rai viene scaricato direttamente senza sbatti.

---

Se vuoi, posso anche dirti:
- come scaricarlo già ottimizzato per editing (codec pulito)
- oppure come evitare ricompressioni inutili per Premiere / DaVinci

Dimmi cosa devi farci e lo adattiamo.

---

## 🧑 User

dammi il comando con link per scaricare miglior qualità sia video sia audio

---

## 🤖 Assistant

Vai diretto così, senza perdere tempo:

```bash
yt-dlp -f "bv*+ba/best" -o "%(title)s.%(ext)s" "https://www.rainews.it/tgr/vda/video/2025/12/la-traccia-di-toni-e7c40917-fbac-4dd2-8680-42fecb64d413.html"
```

### Cosa fa davvero questo comando
- `bv*+ba` → prende **miglior video + miglior audio separati**
- `/best` → fallback se non sono separati
- merge automatico in **MP4** (quando possibile)
- nome file pulito con titolo originale

---

## Se vuoi forzare MP4 (consigliato per editing)

```bash
yt-dlp -f "bv*+ba/best" --merge-output-format mp4 -o "%(title)s.%(ext)s" "https://www.rainews.it/tgr/vda/video/2025/12/la-traccia-di-toni-e7c40917-fbac-4dd2-8680-42fecb64d413.html"
```

---

## Se vuoi il massimo controllo (debug)
```bash
yt-dlp -v -f "bv*+ba/best" "URL"
```

---

Se questo non scarica al primo colpo, non è un problema tuo: è il player Rai. In quel caso si passa direttamente a estrarre lo stream interno, ma prima prova così.