---
title: "Funzioni macOS terminale"
created: 2025-09-21
updated: 2025-09-21
model: gpt-5
messages: 2
source: chatgpt-import
tags: []
---

# Funzioni macOS terminale

> Importato da ChatGPT export · 2 messaggi · gpt-5 · 2025-09-21

## 🧑 User

ci sono delle cose interessanti che su mac os possono essere attivate da terminale?

---

## 🤖 Assistant

Sì, su macOS ci sono parecchie funzionalità e preferenze “nascoste” che si possono abilitare o modificare tramite **Terminale**, soprattutto con il comando `defaults write`.
Ti elenco alcune delle più interessanti e utili:

---

### Finder
- **Mostrare i file nascosti**
```bash
defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder
```
(usa `false` per tornare indietro)

- **Mostrare il percorso completo nella barra del titolo**
```bash
defaults write com.apple.finder _FXShowPosixPathInTitle -bool true && killall Finder
```

- **Mostrare sempre la cartella Libreria dell’utente**
```bash
chflags nohidden ~/Library
```

---

### Dock
- **Ridurre il tempo di animazione del Dock**
```bash
defaults write com.apple.dock autohide-time-modifier -float 0.2 && killall Dock
```
(di default è 0.7)

- **Mostrare solo le app aperte nel Dock**
```bash
defaults write com.apple.dock static-only -bool true && killall Dock
```

- **Attivare l’effetto “suck” nel minimizzare le finestre**
```bash
defaults write com.apple.dock mineffect -string suck && killall Dock
```

---

### Screenshot
- **Cambiare il formato predefinito** (es. PNG → JPG)
```bash
defaults write com.apple.screencapture type jpg && killall SystemUIServer
```

- **Cambiare cartella di salvataggio degli screenshot**
```bash
defaults write com.apple.screencapture location ~/Desktop/Screenshots && killall SystemUIServer
```

---

### Safari
- **Mostrare sempre l’indirizzo completo nella barra**
```bash
defaults write com.apple.Safari ShowFullURLInSmartSearchField -bool true
```

- **Abilitare lo sviluppo (menu Sviluppo)**
```bash
defaults write com.apple.Safari IncludeDevelopMenu -bool true
```

---

### Varie
- **Disabilitare l’avviso “Sei sicuro di voler aprire questa app scaricata da Internet?”**
```bash
defaults write com.apple.LaunchServices LSQuarantine -bool false
```

- **Mostrare informazioni dettagliate sull’orologio (secondi, giorno della settimana, ecc.)**
```bash
defaults write com.apple.menuextra.clock DateFormat -string "EEE d MMM HH:mm:ss"
```

- **Velocizzare l’espansione dei pannelli di dialogo (Salva/Apri)**
```bash
defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true
```

---

Vuoi che ti prepari un **file shell con una raccolta di questi comandi pronti** (magari commentati riga per riga), così puoi attivarli o disattivarli a piacere senza doverli ricordare ogni volta?