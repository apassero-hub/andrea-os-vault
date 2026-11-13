#!/bin/zsh
# Prova col cavo staccato davvero: copia dal G-SPEED (sola lettura) verso il BigDisk.
P="${0:A:h}"; T="/Volumes/RAID BigDisk 2025 4TB/RawLine Space - Prove/Cavo"
rm -f "$P/cavo.jsonl"
"$P/copia" "/Volumes/G-SPEED Shuttle XL TB3/2025/Noli Home - Gillio" "$T/Noli Home - Gillio" "$P/cavo.jsonl" > "$P/cavo.log" 2>&1
echo "uscita $?" >> "$P/cavo.log"
