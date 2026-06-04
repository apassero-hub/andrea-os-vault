---
title: "Script Photoshop sRGB Batch"
created: 2026-04-24
updated: 2026-04-24
model: gpt-5-3
messages: 2
source: chatgpt-import
tags: []
---

# Script Photoshop sRGB Batch

> Importato da ChatGPT export · 2 messaggi · gpt-5-3 · 2026-04-24

## 🧑 User

mi crei uno script photoshop che mi applichi profilo colore srgb a una cartella di files psd con sottocartelle e che salvi il file poi col profilo aggiornato all'interno delle cartelle stesse aggiornando appunto il file preesistente?

---

## 🤖 Assistant

Sì, si fa in modo pulito con ExtendScript (JavaScript per Photoshop), senza passaggi manuali e senza cambiare naming o struttura.

Questo script:
- scansiona ricorsivamente tutte le sottocartelle
- apre ogni PSD
- converte il profilo in sRGB IEC61966-2.1
- salva sovrascrivendo il file originale
- mantiene livelli e struttura

### Script completo (copialo così com’è)

```javascript
#target photoshop

app.displayDialogs = DialogModes.NO;

// === SCEGLI LA CARTELLA PRINCIPALE ===
var inputFolder = Folder.selectDialog("Seleziona la cartella con i PSD");
if (!inputFolder) {
alert("Nessuna cartella selezionata.");
exit();
}

// === PROFILO DESTINAZIONE ===
var targetProfile = "sRGB IEC61966-2.1";

// === FUNZIONE RICORSIVA ===
function processFolder(folder) {
var files = folder.getFiles();

for (var i = 0; i < files.length; i++) {
var file = files[i];

if (file instanceof Folder) {
processFolder(file); // ricorsione sottocartelle
} else if (file instanceof File && file.name.match(/\.psd$/i)) {
processPSD(file);
}
}
}

// === PROCESSO PSD ===
function processPSD(file) {
try {
var doc = app.open(file);

// Se NON è già sRGB → converte
if (doc.colorProfileName!== targetProfile) {
doc.convertProfile(targetProfile, Intent.RELATIVECOLORIMETRIC, true, true);
}

// Opzioni salvataggio PSD
var psdSaveOptions = new PhotoshopSaveOptions();
psdSaveOptions.embedColorProfile = true;
psdSaveOptions.alphaChannels = true;
psdSaveOptions.layers = true;

// Salva sovrascrivendo
doc.saveAs(file, psdSaveOptions, true);

doc.close(SaveOptions.DONOTSAVECHANGES);

} catch (e) {
alert("Errore su file: " + file.fsName + "\n" + e);
}
}

// === AVVIO ===
processFolder(inputFolder);

alert("Operazione completata.");
```

---

### Note operative (importanti)

- **È una conversione, non un’assegnazione**
Usa `convertProfile`, quindi mantiene l’aspetto visivo coerente. È quello che vuoi nel 99% dei casi.

- Se invece vuoi **forzare il profilo senza conversione** (più rischioso), va cambiato approccio. Dimmi e ti preparo la variante.

- **Sovrascrive i file originali**
Non c’è backup. Se hai dubbi, fai una copia prima.

- Funziona anche con PSD molto pesanti, ma:
- niente ottimizzazione batch parallelo
- tempi dipendono da dimensione e numero file

---

### Come usarlo

1. Apri Photoshop
2. File → Scripts → Browse
3. Seleziona il file `.jsx` che hai salvato
4. Scegli la cartella principale
5. Fine, lavora da solo

---

Se vuoi spingerlo a livello pro:
- log errori su file.txt
- skip file già sRGB senza aprirli (più veloce)
- gestione PSB
- conversione + export automatico PNG/JPG

Te lo preparo su misura.