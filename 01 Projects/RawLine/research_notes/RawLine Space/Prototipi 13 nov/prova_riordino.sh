#!/bin/zsh
# Prova di riordino → quarantena → modifiche esterne → "Ripristina schema precedente".
# Lavora SOLO sulla cartella indicata, che è una copia di prova.
P="${0:A:h}"; R="$1"; REF="$2"; L="$P/riordino"
rm -rf "$L"; mkdir -p "$L"; cd "$L"

echo "=== 1. istantanea prima di tutto"
"$P/riordina" istantanea "$R" S0.tsv

echo "=== 2. piano di riordino (modello approvato: RAW/ e Export/Alta, Export/Web)"
python3 -I - "$R" > piano1.tsv <<'EOF'
import os, sys
r = sys.argv[1]
for n in sorted(os.listdir(r)):
    if os.path.isfile(os.path.join(r, n)) and os.path.splitext(n)[1].lower() in (".arw", ".xmp", ".dng"):
        print(f"{n}\tRAW/{n}")
for sotto, nuovo in (("Gillio Export/Alta", "Export/Alta"), ("Gillio Export/Web", "Export/Web")):
    d = os.path.join(r, sotto)
    for n in sorted(os.listdir(d)):
        if n != ".DS_Store": print(f"{sotto}/{n}\t{nuovo}/{n}")
EOF
echo "passi nel piano: $(wc -l < piano1.tsv | tr -d ' ')"

echo "=== 2b. piano sbagliato apposta: due file verso lo stesso nome → deve essere rifiutato"
head -2 piano1.tsv | awk -F'\t' '{print $1 "\tRAW/stesso_nome.ARW"}' > piano_errato.tsv
"$P/riordina" applica "$R" piano_errato.tsv reg.jsonl; echo "(uscita $?)"

echo "=== 3. riordino con interruzione brutale a metà, poi ripresa"
"$P/riordina" applica "$R" piano1.tsv reg.jsonl > /dev/null & pid=$!
sleep 0.4; kill -9 $pid 2>/dev/null; wait $pid 2>/dev/null
echo "dopo l'interruzione: passi fatti nel registro = $(grep -c FATTA reg.jsonl)"
"$P/riordina" applica "$R" piano1.tsv reg.jsonl
"$P/riordina" istantanea "$R" S1.tsv

echo "=== 4. quarantena: 100 RAW con il loro XMP (spostamento, nessuna eliminazione)"
grep -i '\.arw	' piano1.tsv | head -100 | awk -F'\t' '{print $2}' | while read f; do
  b="${f%.*}"; echo "$f\t.RawLineSpace/Quarantena/lotto-1/$f"; echo "$b.xmp\t.RawLineSpace/Quarantena/lotto-1/$b.xmp"
done > piano2.tsv
"$P/riordina" applica "$R" piano2.tsv reg.jsonl

echo "=== 5. modifiche fatte da fuori nel frattempo"
echo "nuovo" > "$R/Export/Web/arrivato_dopo.jpg"
X1=$(ls "$R/RAW" | grep -i '\.xmp$' | tail -1); echo "<!-- modificato -->" >> "$R/RAW/$X1"; echo "XMP modificato sul posto: $X1"
X2=$(ls "$R/RAW" | grep -i '\.xmp$' | tail -2 | head -1); cp "$R/RAW/$X2" "$R/RAW/.salva"; echo "<!-- salvato alla Lightroom -->" >> "$R/RAW/.salva"; mv -f "$R/RAW/.salva" "$R/RAW/$X2"; echo "XMP risalvato con un file nuovo (cambia l'identificativo): $X2"

echo "=== 6. Ripristina schema precedente (istantanea S0)"
"$P/riordina" ripristina "$R" S0.tsv reg.jsonl

echo "=== 7. confronto con la copia di riferimento"
python3 -I "$P/verifica.py" "$REF" "$R"
echo "registro: $(wc -l < reg.jsonl | tr -d ' ') righe"
