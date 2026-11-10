# Genera budget/Cogne_Trail_2027_Budget_v2.xlsx: un solo file con parametri, dettaglio costi,
# ricavi, sponsor e quadro dei tre scenari. Parte dai due file di Ale (v1) e applica le correzioni
# descritte in BUDGET.md. Uso: python3 tools/budget_v2.py  (serve openpyxl)
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).resolve().parent.parent / "budget" / "Cogne_Trail_2027_Budget_v2.xlsx"

F = "Arial"
BLUE = "0000FF"; GREEN = "008000"
INK = "1E2119"; NEVE = "E4E6DA"; RED = "B5412A"
f_title = Font(name=F, size=14, bold=True, color=INK)
f_sub = Font(name=F, size=10, italic=True, color="6B7258")
f_head = Font(name=F, size=10, bold=True, color="FFFFFF")
f_txt = Font(name=F, size=10)
f_bold = Font(name=F, size=10, bold=True)
f_in = Font(name=F, size=10, color=BLUE)
f_link = Font(name=F, size=10, color=GREEN)
f_new = Font(name=F, size=10, bold=True, color=RED)
fill_head = PatternFill("solid", fgColor=INK)
fill_in = PatternFill("solid", fgColor="FFF6C8")   # ipotesi chiave da confermare
fill_tot = PatternFill("solid", fgColor=NEVE)
thin = Side(style="thin", color="C8CBBC")
b_top = Border(top=Side(style="thin", color=INK))
EUR = '#,##0 €;-#,##0 €;"-"'
EUR2 = '#,##0.00 €;-#,##0.00 €;"-"'
PCT = '0%;-0%;"-"'
NUM = '#,##0;-#,##0;"-"'
SC = ["B", "C", "D"]          # colonne scenario in Parametri, Ricavi, Quadro
NOTE = "Ipotesi v1 di Ale, non preventivo"

wb = Workbook()

def sheet(name, title, sub):
    ws = wb.create_sheet(name)
    ws["A1"] = title; ws["A1"].font = f_title
    ws["A2"] = sub; ws["A2"].font = f_sub
    ws.sheet_view.showGridLines = False
    return ws

def head(ws, row, labels):
    for i, l in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=l)
        c.font = f_head; c.fill = fill_head
        c.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 28

def put(ws, ref, value, font=f_txt, fmt=None, fill=None, comment=None):
    c = ws[ref]; c.value = value; c.font = font
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    if comment: c.comment = Comment(comment, "Cogne Trail")
    return c

def widths(ws, w):
    for col, v in w.items(): ws.column_dimensions[col].width = v

# ---------------------------------------------------------------- Leggimi
ws = wb.active; ws.title = "Leggimi"
ws.sheet_view.showGridLines = False
rows = [
    ("COGNE TRAIL 2027 | Budget v2", f_title),
    ("Versione 2 del 10 novembre 2026, costruita sui due file di Ale (v1). Stime di pianificazione, non preventivi.", f_sub),
    ("", None),
    ("COME SI USA", f_bold),
    ("Si modificano solo le celle con il testo blu: i parametri nel foglio Parametri, le voci in Dettaglio costi, gli importi in Sponsor e contributi.", f_txt),
    ("Le celle con fondo giallo sono ipotesi chiave ancora da confermare.", f_txt),
    ("Il testo nero è calcolato, il testo verde è un collegamento a un altro foglio: non va sovrascritto.", f_txt),
    ("Per aggiungere una voce di costo: inserire una riga dentro la tabella di Dettaglio costi (sopra la riga dei totali) e scegliere il Tipo dal menu.", f_txt),
    ("Il Tipo decide come la voce cambia tra gli scenari: Fisso, Per atleta, Per atleta 28 / 47, Proporzionale 28 / 47, Per volontario, Piano B. In natura, Escluso, Opzionale e Promemoria non entrano nei totali.", f_txt),
    ("", None),
    ("COSA CAMBIA RISPETTO ALLA V1", f_bold),
    ("1. Un solo file: gli scenari sommano direttamente dal dettaglio, quindi una modifica a una voce aggiorna tutto.", f_txt),
    ("2. Costi variabili come costo unitario × iscritti (maglia 12 €, pasto 10 €, medaglia 6 €), invece della proporzione sullo scenario da 500.", f_txt),
    ("3. Nuove voci: bagni chimici, rientro dei ritirati e trasporti in quota, corsa dei bambini, SIAE, tasse FIDAL. Sono segnate \"Nuova v2\" in Dettaglio costi.", f_txt),
    ("4. Commissioni della piattaforma d'iscrizione al 4% (nella v1 erano zero).", f_txt),
    ("5. Fondo imprevisti al 15% (nella v1 era il 10%), per i molti costi a zero non ancora confermati.", f_txt),
    ("6. Volontari da 60 a 80 (cestini) e da 40 a 60 (pasto finale).", f_txt),
    ("7. Sito: il sito esiste già (Cloudflare), restano traduzioni FR/EN e dominio, 500 € invece di 1.950 €.", f_txt),
    ("8. Punto acqua della 47 km come costo fisso (nella v1 scalava con gli iscritti).", f_txt),
    ("9. Nuovo foglio Sponsor e contributi, con importi obiettivo e confermati tenuti separati. Nel quadro il saldo resta calcolato sui soli confermati.", f_txt),
    ("10. Pettorali gratuiti per gli sponsor (Parametri, riga 10): occupano posti e riducono gli iscritti paganti. Il loro costo resta nei costi per atleta.", f_txt),
    ("11. Il foglio Quadro scenari mostra il fabbisogno v1 accanto a quello v2, per confronto.", f_txt),
    ("", None),
    ("DA DECIDERE CON ALE", f_bold),
    ("Giorno di gara: nella v1 le gare sono domenica 13 giugno, mentre sito, presentazione e proposta CAS dicono sabato 12 giugno. Il budget non cambia, il programma sì.", f_txt),
    ("Nomi: Gran Paradiso Trail / Colonna 28K (v1) oppure Cogne Trail / Miniere 28 (sito e PDF). In questo file si usano \"28 km\" e \"47 km\".", f_txt),
    ("Rifugio Sogno: è l'unico cancello orario della 47 km, ma LoveVdA lo dà come temporaneamente chiuso. Va verificato.", f_txt),
    ("Soccorso sanitario e cronometraggio: le cifre v1 sono probabilmente basse. Sono i primi preventivi da chiedere.", f_txt),
    ("Fiscalità ASD: IVA sulle sponsorizzazioni e natura commerciale o meno delle iscrizioni, da chiedere al commercialista.", f_txt),
]
for i, (t, font) in enumerate(rows, 1):
    c = ws.cell(row=i, column=1, value=t)
    if font: c.font = font
    c.alignment = Alignment(wrap_text=True, vertical="top")
ws.column_dimensions["A"].width = 130

# ---------------------------------------------------------------- Parametri
P = sheet("Parametri", "PARAMETRI | Ipotesi dei tre scenari", "Testo blu = da modificare · fondo giallo = ipotesi chiave da confermare")
head(P, 4, ["PARAMETRO", "300 iscritti", "400 iscritti", "500 iscritti", "NOTE"])
par = [
    # riga, etichetta, valori o formula (con {c} = colonna), formato, input?, giallo?, nota
    (5, "Iscritti totali", [300, 400, 500], NUM, True, True, "Scenari v1"),
    (6, "Quota 28 km", [0.6, 0.6, 0.6], PCT, True, False, "Ripartizione v1"),
    (7, "Quota 47 km", "=1-{c}6", PCT, False, False, "Complementare"),
    (8, "Iscritti 28 km", "=ROUND({c}5*{c}6,0)", NUM, False, False, "Calcolato"),
    (9, "Iscritti 47 km", "={c}5-{c}8", NUM, False, False, "Calcolato"),
    (10, "Pettorali gratuiti per sponsor", [0, 0, 0], NUM, True, True, "Nuovo v2. Es. 50 con CAS title partner. Occupano posti e riducono i paganti"),
    (11, "Iscritti paganti", "={c}5-{c}10", NUM, False, False, "Calcolato"),
    (12, "Primi iscritti agevolati (early)", [100, 100, 100], NUM, True, False, "Totale sulle due gare (v1)"),
    (13, "Quota standard tra i paganti dopo l'early", [0.7, 0.7, 0.75], PCT, True, False, "v1: a 500 iscritti il 75%, negli altri il 70%"),
    (14, "28 km · prezzo early", [40, 40, 40], EUR, True, False, "Tariffa v1"),
    (15, "28 km · prezzo standard", [45, 45, 45], EUR, True, False, "Tariffa v1"),
    (16, "28 km · prezzo finale", [50, 50, 50], EUR, True, False, "Tariffa v1"),
    (17, "47 km · prezzo early", [60, 60, 60], EUR, True, False, "Tariffa v1"),
    (18, "47 km · prezzo standard", [70, 70, 70], EUR, True, False, "Tariffa v1"),
    (19, "47 km · prezzo finale", [80, 80, 80], EUR, True, False, "Tariffa v1"),
    (20, "Commissioni piattaforma iscrizioni", [0.04, 0.04, 0.04], PCT, True, True, "Nuovo v2. Stima, da verificare con Wedosport o con la piattaforma scelta"),
    (21, "Fondo imprevisti", [0.15, 0.15, 0.15], PCT, True, True, "v1: 10%. v2: 15% per la prima edizione"),
    (22, "Pubblicità Piano B (€)", [600, 600, 600], EUR, True, False, "v1"),
    (23, "Attivare Piano B? (0 = no, 1 = sì)", [0, 0, 0], NUM, True, False, "Disattivato come nella v1"),
    (24, "Volontari (cestino pranzo)", [80, 80, 80], NUM, True, True, "v1: 60. Da contare ristoro per ristoro"),
    (25, "Volontari al pasto finale", [60, 60, 60], NUM, True, True, "v1: 40"),
]
for r, label, val, fmt, is_in, yellow, note in par:
    put(P, f"A{r}", label)
    for i, col in enumerate(SC):
        v = val[i] if isinstance(val, list) else val.format(c=col)
        put(P, f"{col}{r}", v, f_in if is_in else f_txt, fmt, fill_in if yellow else None)
    put(P, f"E{r}", note, f_sub)
widths(P, {"A": 42, "B": 14, "C": 14, "D": 14, "E": 70})
P.freeze_panes = "B5"

# ---------------------------------------------------------------- Dettaglio costi
D = sheet("Dettaglio costi", "COSTI | Dettaglio voce per voce e valore nei tre scenari",
          "Il Tipo decide come la voce scala. Righe \"Nuova v2\" in rosso. Inserire nuove righe sopra la riga dei totali.")
head(D, 4, ["CAPITOLO", "SOTTOVOCE", "TIPO", "€/UNITÀ", "Q.TÀ (fissi)", "300 (€)", "400 (€)", "500 (€)", "STATO", "NOTE / ASSUNZIONI", "V2"])
FIX, PA, P28, P47, PR28, PR47, PV, PVP = "Fisso", "Per atleta", "Per atleta 28", "Per atleta 47", "Proporzionale 28", "Proporzionale 47", "Per volontario", "Per volontario al pasto"
items = [
    ("Sicurezza e percorsi", "Coordinamento sicurezza", FIX, 800, 1, "Stima", "Piano sicurezza da validare", ""),
    ("Sicurezza e percorsi", "Soccorso / assistenza sanitaria", FIX, 3000, 1, "Stima", "Probabilmente bassa per due gare in quota: primo preventivo da chiedere", "Da verificare"),
    ("Sicurezza e percorsi", "Presidi alpini, comunicazioni e logistica", FIX, 2500, 1, "Stima", "Verificare fabbisogno sul percorso", ""),
    ("Sicurezza e percorsi", "Materiali tracciatura e segnalazione", FIX, 800, 1, "Stima", "Posa e rimozione con volontari", ""),
    ("Sicurezza e percorsi", "Rientro ritirati e trasporti in quota", FIX, 500, 1, "Stima", "Discesa di chi si ritira a Grauson o al Sogno, materiali ai ristori lontani dalle strade", "Nuova v2"),
    ("Cronometraggio", "Servizio cronometraggio Wedosport", FIX, 1500, 1, "Stima", "Preventivo da richiedere, con i rilevamenti intermedi in quota", "Da verificare"),
    ("Cronometraggio", "Controlli / checkpoint", FIX, 500, 1, "Stima", "Verificare numero postazioni", ""),
    ("Cronometraggio", "Pettorali personalizzati", FIX, 300, 1, "Stima", "Esclusa fee piattaforma (ora nei ricavi)", ""),
    ("Cronometraggio", "Rilevamento a Colonna per il Tratto del Ferro", "Opzionale", 300, 1, "Solo con CAS", "Da attivare (Tipo = Fisso) se CAS accetta il Tratto del Ferro", "Nuova v2"),
    ("Ristori 47 km", "R1 Gimillan km 10,77", "Promemoria", 0, 1, "Ripartizione da definire", "Quota compresa negli alimenti 47 km", ""),
    ("Ristori 47 km", "R2 Rifugio Grauson km 17,24", "Promemoria", 0, 1, "Ripartizione da definire", "Quota compresa negli alimenti 47 km", ""),
    ("Ristori 47 km", "R3 Rifugio Sogno km 30,36", "Promemoria", 0, 1, "Da verificare", "Unico cancello orario. Rifugio forse chiuso (LoveVdA)", ""),
    ("Ristori 47 km", "R4 Bardoney km 38,04", "Promemoria", 0, 1, "Ripartizione da definire", "Quota compresa negli alimenti 47 km", ""),
    ("Ristori 47 km", "Alimenti e bevande per i 4 ristori", PR47, 1400, 1, "Stima", "1.400 € a 200 iscritti, scala con gli iscritti alla 47 km", ""),
    ("Ristori 47 km", "Punto acqua aggiuntivo", FIX, 150, 1, "Stima opzionale inclusa", "Tra Grauson e Sogno. v2: fisso, non scala", ""),
    ("Ristori 28 km", "R1 Miniera di Colonna km 6,88", PR28, 350, 1, "Stima", "Ristoro leggero, 350 € a 300 iscritti", ""),
    ("Ristori 28 km", "R2 Brolliot km 15,01", PR28, 500, 1, "Stima", "Ristoro principale, 500 € a 300 iscritti", ""),
    ("Ristori 28 km", "R3 Les Goilles km 22,37", PR28, 300, 1, "Stima", "Ristoro leggero, 300 € a 300 iscritti", ""),
    ("Logistica 28 km", "Trasporto materiali Colonna", FIX, 150, 1, "Stima", "La strada termina prima del ristoro", ""),
    ("Pasto finale", "Pasto finale atleti", PA, 10, None, "Stima", "Piatto locale; possibile Pro Loco non confermata", ""),
    ("Maglie", "Maglia tecnica ufficiale", PA, 12, None, "Stima", "A tutti gli iscritti al ritiro pettorale. Attenzione ai minimi d'ordine", ""),
    ("Medaglie", "Medaglie 28 km", P28, 6, None, "Stima", "Ipotesi prudente: tutti finisher. Con l'acciaio CAS resta la lavorazione", ""),
    ("Medaglie", "Medaglie 47 km", P47, 6, None, "Stima", "Due artigiani distinti (v1)", ""),
    ("Village", "Portale partenza/arrivo legno e ferro", FIX, 2000, 1, "Stima", "Da verificare ancoraggi e sicurezza", ""),
    ("Village", "Banner e grafiche stampate", FIX, 400, 1, "Stima", "", ""),
    ("Village", "Segnaletica village e materiali pettorali", FIX, 200, 1, "Stima", "", ""),
    ("Village", "Noleggio impianto audio e supporto", FIX, 500, 1, "Stima", "Il Comune non ha un impianto; 2 giorni da verificare", ""),
    ("Village", "Speaker / presentatore", FIX, 400, 1, "Stima", "Nessun accordo", ""),
    ("Village", "Podio premiazioni", FIX, 250, 1, "Stima", "", ""),
    ("Village", "Pulizie e materiali festa", FIX, 350, 1, "Stima", "Due giorni", ""),
    ("Village", "Elettricità e materiali area partner", FIX, 300, 1, "Stima", "I partner portano idealmente i propri stand", ""),
    ("Village", "Bagni chimici", FIX, 800, 1, "Stima", "Circa 6 bagni per due giorni", "Nuova v2"),
    ("Village", "SIAE e musica per la festa", FIX, 300, 1, "Stima", "Solo se c'è musica", "Nuova v2"),
    ("Programma", "Corsa dei bambini", FIX, 300, 1, "Stima", "Nel programma di sito e PDF: pettorali, gadget, ristoro", "Nuova v2"),
    ("Sito web", "Traduzioni FR/EN e adattamento del sito esistente", FIX, 350, 1, "Stima", "v1: 1.800 € per un sito nuovo. Il sito c'è già", "Modificata v2"),
    ("Sito web", "Dominio e hosting annuale", FIX, 150, 1, "Stima", "", ""),
    ("Foto/video pre-gara", "Riprese video territorio e percorsi", FIX, 800, 1, "Stima-obiettivo", "Da decidere se lavoro pagato o contributo in natura", ""),
    ("Foto/video pre-gara", "Montaggio teaser, video e clip", FIX, 600, 1, "Stima-obiettivo", "", ""),
    ("Foto/video pre-gara", "Fotografia promozionale", FIX, 400, 1, "Stima-obiettivo", "", ""),
    ("Foto/video weekend", "Copertura editoriale ufficiale", FIX, 1500, 1, "Stima-obiettivo", "Promessa anche nella proposta CAS", ""),
    ("Foto atleti", "Servizio foto a vendita diretta", "Escluso", 0, 1, "Non concordato", "Costo zero per l'organizzazione (v1)", ""),
    ("Grafica/social", "Gestione grafica e social interna", "In natura", 0, 1, "Confermato", "Lavoro non monetizzato (v1)", ""),
    ("Assicurazioni", "Polizza manifestazione", FIX, 1500, 1, "Accantonamento", "Verificare RC, infortuni, volontari, due giorni", ""),
    ("Permessi", "Tasse FIDAL / approvazione gara", FIX, 300, 1, "Stima", "Da verificare con FIDAL VdA", "Nuova v2"),
    ("Permessi", "Piazza, sala, tavoli e transenne", "In natura", 0, 1, "Atteso, non confermato", "Comune di Cogne", ""),
    ("Permessi", "Permessi e nulla osta", "In natura", 0, 1, "Non quantificato", "Zero non significa gratuito", ""),
    ("Volontari", "Cestini pranzo", PV, 12, None, "Stima", "Numero volontari in Parametri", "Modificata v2"),
    ("Volontari", "Accesso ristoro finale", PVP, 10, None, "Stima", "Numero in Parametri", "Modificata v2"),
    ("Volontari", "Cena ringraziamento", "Escluso", 0, 1, "Esclusa", "Offerta personalmente, non a carico dell'organizzazione (v1)", ""),
    ("Pubblicità", "Campagne sponsorizzate Piano B", "Piano B", 600, 1, "Riserva", "Entra solo se attivata in Parametri", ""),
]
first = 5
last = first + len(items) - 1
types = [FIX, PA, P28, P47, PR28, PR47, PV, PVP, "Piano B", "Opzionale", "In natura", "Escluso", "Promemoria"]
dv = DataValidation(type="list", formula1='"' + ",".join(types) + '"', allow_blank=False)
D.add_data_validation(dv)
for k, (cap, sub, tipo, unit, qty, stato, note, v2) in enumerate(items):
    r = first + k
    put(D, f"A{r}", cap); put(D, f"B{r}", sub)
    put(D, f"C{r}", tipo, f_in); dv.add(f"C{r}")
    put(D, f"D{r}", unit, f_in, EUR)
    if tipo == "Piano B":
        put(D, f"D{r}", "=Parametri!D22", f_link, EUR)
    if qty is None:
        put(D, f"E{r}", "per scenario", f_sub)
    else:
        put(D, f"E{r}", qty, f_in, NUM)
    for col, pc in zip(["F", "G", "H"], SC):
        f = (f'=IF($C{r}="{FIX}",$D{r}*$E{r},'
             f'IF($C{r}="{PA}",Parametri!{pc}$5*$D{r},'
             f'IF($C{r}="{P28}",Parametri!{pc}$8*$D{r},'
             f'IF($C{r}="{P47}",Parametri!{pc}$9*$D{r},'
             f'IF($C{r}="{PR28}",$D{r}*$E{r}*Parametri!{pc}$8/Parametri!$D$8,'
             f'IF($C{r}="{PR47}",$D{r}*$E{r}*Parametri!{pc}$9/Parametri!$D$9,'
             f'IF($C{r}="{PV}",Parametri!{pc}$24*$D{r},'
             f'IF($C{r}="{PVP}",Parametri!{pc}$25*$D{r},'
             f'IF($C{r}="Piano B",$D{r}*$E{r}*Parametri!{pc}$23,0)))))))))')
        put(D, f"{col}{r}", f, f_txt, EUR)
    put(D, f"I{r}", stato, f_sub); put(D, f"J{r}", note, f_sub)
    if v2: put(D, f"K{r}", v2, f_new)
    if "Da verificare" in v2:
        D[f"D{r}"].fill = fill_in
tr = last + 2
put(D, f"B{tr}", "TOTALE COSTI OPERATIVI (escluso Piano B)", f_bold)
put(D, f"B{tr+1}", "Piano B (se attivo)", f_txt)
for col in ["F", "G", "H"]:
    put(D, f"{col}{tr}", f'=SUMIF($C${first}:$C${last},"<>Piano B",{col}{first}:{col}{last})', f_bold, EUR, fill_tot)
    put(D, f"{col}{tr+1}", f'=SUMIF($C${first}:$C${last},"Piano B",{col}{first}:{col}{last})', f_txt, EUR)
    D[f"{col}{tr}"].border = b_top
D[f"B{tr}"].fill = fill_tot
widths(D, {"A": 20, "B": 44, "C": 20, "D": 11, "E": 12, "F": 12, "G": 12, "H": 12, "I": 22, "J": 64, "K": 14})
D.freeze_panes = "C5"
D.auto_filter.ref = f"A4:K{last}"
DTOT = {"B": f"'Dettaglio costi'!F{tr}", "C": f"'Dettaglio costi'!G{tr}", "D": f"'Dettaglio costi'!H{tr}"}
DPB = {"B": f"'Dettaglio costi'!F{tr+1}", "C": f"'Dettaglio costi'!G{tr+1}", "D": f"'Dettaglio costi'!H{tr+1}"}
DCOL = {"B": "F", "C": "G", "D": "H"}

# ---------------------------------------------------------------- Ricavi
R = sheet("Ricavi iscrizioni", "RICAVI | Iscrizioni per fascia di prezzo", "Le fasce si applicano ai soli paganti. Commissioni sottratte")
head(R, 4, ["VOCE", "300 (€)", "400 (€)", "500 (€)"])
def early(c): return f"MIN(Parametri!{c}11,Parametri!{c}12)"
def std(c): return f"ROUND((Parametri!{c}11-{early(c)})*Parametri!{c}13,0)"
rv = [
    (5, "Iscritti paganti", lambda c: f"=Parametri!{c}11", NUM, f_link),
    (6, "Early · 28 km", lambda c: f"={early(c)}*Parametri!{c}6*Parametri!{c}14", EUR, f_txt),
    (7, "Early · 47 km", lambda c: f"={early(c)}*Parametri!{c}7*Parametri!{c}17", EUR, f_txt),
    (8, "Standard · 28 km", lambda c: f"={std(c)}*Parametri!{c}6*Parametri!{c}15", EUR, f_txt),
    (9, "Standard · 47 km", lambda c: f"={std(c)}*Parametri!{c}7*Parametri!{c}18", EUR, f_txt),
    (10, "Ultima fascia · 28 km", lambda c: f"=(Parametri!{c}11-{early(c)}-{std(c)})*Parametri!{c}6*Parametri!{c}16", EUR, f_txt),
    (11, "Ultima fascia · 47 km", lambda c: f"=(Parametri!{c}11-{early(c)}-{std(c)})*Parametri!{c}7*Parametri!{c}19", EUR, f_txt),
    (12, "INCASSI LORDI", lambda c: f"=SUM({c}6:{c}11)", EUR, f_bold),
    (13, "Commissioni piattaforma", lambda c: f"=-{c}12*Parametri!{c}20", EUR, f_txt),
    (14, "INCASSI NETTI", lambda c: f"={c}12+{c}13", EUR, f_bold),
    (15, "Quota media per pagante (lorda)", lambda c: f"=IFERROR({c}12/{c}5,0)", EUR2, f_txt),
]
for r, label, fn, fmt, font in rv:
    put(R, f"A{r}", label, f_bold if font is f_bold else f_txt)
    for c in SC:
        put(R, f"{c}{r}", fn(c), font, fmt, fill_tot if r in (12, 14) else None)
put(R, "A17", "Nota: incassi simulati. La fiscalità delle quote (ASD, IVA) è da verificare con il commercialista.", f_sub)
widths(R, {"A": 40, "B": 14, "C": 14, "D": 14})

# ---------------------------------------------------------------- Sponsor
S = sheet("Sponsor e contributi", "SPONSOR E CONTRIBUTI | Obiettivi e confermati",
          "Nel saldo entrano solo i confermati. Gli obiettivi servono a vedere quanto chiudere. Importi IVA esclusa")
head(S, 4, ["FONTE", "TIPO", "OBIETTIVO €", "CONFERMATO €", "STATO", "NOTE"])
sp = [
    ("Cogne Acciai Speciali", "Title partner", 15000, 0, "Proposta pronta, non inviata", "Livelli in proposta: 15.000 / 7.000 / 3.000 €. Con il title: 50 pettorali gratuiti (Parametri, riga 10)"),
    ("Partner tecnico", "Materiali", 0, 0, "Da cercare", "Di solito in natura (maglie, materiale staff): ridurre le voci di costo invece di indicarlo qui"),
    ("Partner di tratto / rifugi", "Ristori", 0, 0, "Da cercare", "Rifugio Grauson primo candidato"),
    ("Amici di Cogne", "Attività locali", 0, 0, "Da cercare", "Tramite il Consorzio Operatori Turistici"),
    ("Regione Valle d'Aosta", "Contributo L.R. 3/2004", 0, 0, "Bando 2027 non ancora uscito", "Verificare scadenze e soggetto richiedente"),
    ("Comune di Cogne", "Contributo in denaro", 0, 0, "Da chiedere", "I servizi in natura sono in Dettaglio costi"),
    ("Altro", "", 0, 0, "", ""),
]
for k, (src, tipo, ob, conf, stato, note) in enumerate(sp):
    r = 5 + k
    put(S, f"A{r}", src); put(S, f"B{r}", tipo)
    put(S, f"C{r}", ob, f_in, EUR, fill_in if ob else None)
    put(S, f"D{r}", conf, f_in, EUR)
    put(S, f"E{r}", stato, f_sub); put(S, f"F{r}", note, f_sub)
sl = 5 + len(sp) - 1
put(S, f"A{sl+2}", "TOTALE", f_bold, fill=fill_tot)
put(S, f"C{sl+2}", f"=SUM(C5:C{sl})", f_bold, EUR, fill_tot)
put(S, f"D{sl+2}", f"=SUM(D5:D{sl})", f_bold, EUR, fill_tot)
S_OB, S_CONF = f"'Sponsor e contributi'!C{sl+2}", f"'Sponsor e contributi'!D{sl+2}"
widths(S, {"A": 28, "B": 24, "C": 14, "D": 14, "E": 28, "F": 80})

# ---------------------------------------------------------------- Quadro
Q = sheet("Quadro scenari", "COGNE TRAIL 2027 | Quadro economico", "Saldo calcolato sui soli sponsor confermati · stime modificabili in Parametri e Dettaglio costi")
head(Q, 4, ["INDICATORE", "300 iscritti", "400 iscritti", "500 iscritti"])
var_types = [PA, P28, P47, PR28, PR47]
qv = [
    (5, "Iscritti complessivi", lambda c: f"=Parametri!{c}5", NUM, f_link),
    (6, "  di cui 28 km", lambda c: f"=Parametri!{c}8", NUM, f_link),
    (7, "  di cui 47 km", lambda c: f"=Parametri!{c}9", NUM, f_link),
    (8, "  di cui pettorali gratuiti", lambda c: f"=Parametri!{c}10", NUM, f_link),
    (10, "Incassi lordi da iscrizioni", lambda c: f"='Ricavi iscrizioni'!{c}12", EUR, f_link),
    (11, "Commissioni piattaforma", lambda c: f"='Ricavi iscrizioni'!{c}13", EUR, f_link),
    (12, "INCASSI NETTI", lambda c: f"='Ricavi iscrizioni'!{c}14", EUR, f_bold),
    (14, "Costi operativi", lambda c: f"={DTOT[c]}", EUR, f_link),
    (15, "Fondo imprevisti", lambda c: f"={c}14*Parametri!{c}21", EUR, f_txt),
    (16, "Pubblicità Piano B (se attiva)", lambda c: f"={DPB[c]}", EUR, f_link),
    (17, "TOTALE COSTI PREVISTI", lambda c: f"=SUM({c}14:{c}16)", EUR, f_bold),
    (19, "SALDO SENZA SPONSOR", lambda c: f"={c}12-{c}17", EUR, f_bold),
    (20, "FABBISOGNO PER IL PAREGGIO", lambda c: f"=MAX(0,-{c}19)", EUR, f_bold),
    (22, "Sponsor e contributi confermati", lambda c: f"={S_CONF}", EUR, f_link),
    (23, "SALDO CON I CONFERMATI", lambda c: f"={c}19+{c}22", EUR, f_bold),
    (24, "Sponsor e contributi obiettivo", lambda c: f"={S_OB}", EUR, f_link),
    (25, "SALDO SE ARRIVANO GLI OBIETTIVI", lambda c: f"={c}19+{c}24", EUR, f_bold),
    (27, "Costo totale per atleta", lambda c: f"=IFERROR({c}17/{c}5,0)", EUR2, f_txt),
    (28, "Costo variabile per atleta (maglia, pasto, medaglia, ristori)", lambda c: "=IFERROR((" + "+".join(
        f"SUMIF('Dettaglio costi'!$C${first}:$C${last},\"{t}\",'Dettaglio costi'!{DCOL[c]}${first}:{DCOL[c]}${last})" for t in var_types) + f")/{c}5,0)", EUR2, f_txt),
    (29, "Costo di un pettorale gratuito in più (variabile, senza imprevisti)", lambda c: f"={c}28", EUR2, f_txt),
    (31, "Fabbisogno nella v1 di Ale (per confronto)", None, EUR, f_in),
    (32, "Differenza v2 − v1", lambda c: f"={c}20-{c}31", EUR, f_txt),
]
v1 = {"B": 18804, "C": 16768, "D": 14872}
for r, label, fn, fmt, font in qv:
    put(Q, f"A{r}", label, f_bold if font is f_bold else f_txt)
    for c in SC:
        if fn is None:
            put(Q, f"{c}{r}", v1[c], f_in, fmt, comment="Valore della riga 15 del file v1 di Ale (Budget_3_Scenari.xlsx), scritto a mano per confronto")
        else:
            put(Q, f"{c}{r}", fn(c), font, fmt, fill_tot if r in (12, 17, 20, 23, 25) else None)
put(Q, "A34", "Nota: budget provvisorio, da completare con preventivi, autorizzazioni e parere del commercialista.", f_sub)
widths(Q, {"A": 62, "B": 16, "C": 16, "D": 16})
Q.freeze_panes = "B5"

# ---------------------------------------------------------------- Riepilogo per capitolo
RP = sheet("Riepilogo capitoli", "RIEPILOGO | Costi per capitolo", "Somma automatica dal Dettaglio costi")
head(RP, 4, ["CAPITOLO", "300 (€)", "400 (€)", "500 (€)", "PESO A 500"])
caps = list(dict.fromkeys(i[0] for i in items))
for k, cap in enumerate(caps):
    r = 5 + k
    put(RP, f"A{r}", cap)
    for c in SC:
        put(RP, f"{c}{r}", f"=SUMIF('Dettaglio costi'!$A${first}:$A${last},$A{r},'Dettaglio costi'!{DCOL[c]}${first}:{DCOL[c]}${last})", f_link, EUR)
    put(RP, f"E{r}", f"=IFERROR(D{r}/D${5+len(caps)+1},0)", f_txt, '0.0%;-0.0%;"-"')
rt = 5 + len(caps) + 1
put(RP, f"A{rt}", "TOTALE (incluso Piano B se attivo)", f_bold, fill=fill_tot)
for c in SC:
    put(RP, f"{c}{rt}", f"=SUM({c}5:{c}{rt-2})", f_bold, EUR, fill_tot)
widths(RP, {"A": 28, "B": 14, "C": 14, "D": 14, "E": 12})

wb.move_sheet("Quadro scenari", offset=1 - wb.sheetnames.index("Quadro scenari"))
wb.active = 1
wb.calculation.fullCalcOnLoad = True
OUT.parent.mkdir(exist_ok=True)
wb.save(OUT)
print("Salvato:", OUT)
