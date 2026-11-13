#!/bin/zsh
# Prova d'interruzione: la copia viene uccisa di colpo (kill -9) a tempi casuali, poi ripresa.
# uso: interrompi.sh <sorgente> <destinazione> <registro> <numero di interruzioni>
P="${0:A:h}"; SRC="$1"; DST="$2"; REG="$3"; N="$4"
rm -f "$REG"
for i in $(seq 1 $N); do
  "$P/copia" "$SRC" "$DST" "$REG" > "$P/interr_$i.log" 2>&1 &
  pid=$!
  attesa=$(( (RANDOM % 25) + 3 ))
  sleep $attesa
  if kill -0 $pid 2>/dev/null; then
    kill -9 $pid; wait $pid 2>/dev/null
    tmp=$(find "$DST" -name '.rawline-tmp-*' 2>/dev/null | wc -l | tr -d ' ')
    echo "interruzione $i dopo ${attesa}s: temporanei rimasti a metà=$tmp, file verificati nel registro=$(grep -c VERIFICATA "$REG")"
  else
    wait $pid; echo "interruzione $i: la copia era già finita"; break
  fi
done
echo "--- ripresa finale senza interruzioni"
"$P/copia" "$SRC" "$DST" "$REG" | tail -3
echo "temporanei rimasti: $(find "$DST" -name '.rawline-tmp-*' | wc -l | tr -d ' ')"
