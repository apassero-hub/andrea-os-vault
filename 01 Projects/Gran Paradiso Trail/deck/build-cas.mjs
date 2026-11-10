// Uso: node deck/build-cas.mjs  → genera deck/cas.html e lo stampa in deck/Cogne-Trail-Proposta-CAS.pdf
// Proposta di main partnership per Cogne Acciai Speciali. Usa lo stesso stile della presentazione:
// il CSS viene letto da build-deck.mjs, così le due restano allineate.
import { writeFileSync, readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const dir = new URL(".", import.meta.url);
const img = n => "data:image/jpeg;base64," + readFileSync(new URL(`../site/src/img/${n}.jpg`, dir)).toString("base64");
const deckSrc = readFileSync(new URL("build-deck.mjs", dir), "utf8");
const css = deckSrc.match(/<style>([\s\S]*?)<\/style>/)[1];

const R28 = [[0,1543,"Cogne"],[2,1708,"Montroz"],[4,2050],[7,2425,"Miniere"],[10.5,2450],[13,2330],[16,2416,"Brolliot"],[19,2200],[22.8,1841,"Goilles"],[24,1727,"Lillaz"],[25,1600],[28,1543,"Arrivo"]];

// stesso profilo della presentazione
function dense(pts, step = 0.25) {
  const out = []; let seed = 7;
  const rnd = () => (seed = (seed * 9301 + 49297) % 233280) / 233280 - 0.5;
  for (let i = 0; i < pts.length - 1; i++) {
    const [k0, a0] = pts[i], [k1, a1] = pts[i + 1];
    for (let k = k0; k < k1; k += step) {
      const t = (k - k0) / (k1 - k0), e = t * t * (3 - 2 * t), edge = Math.min(t, 1 - t) * 2;
      out.push([k, a0 + (a1 - a0) * e + rnd() * 26 * edge]);
    }
  }
  out.push(pts.at(-1).slice(0, 2));
  return out;
}
const fmt = a => String(a).replace(/\B(?=(\d{3})+$)/, ".");
function profile(pts, { w, h, min, max, pad = 50, labels = true, axis = true, band }) {
  const km = pts.at(-1)[0];
  const x = k => (k / km) * w, y = a => pad + (1 - (a - min) / (max - min)) * (h - pad * 2);
  const d = dense(pts).map(([k, a], i) => `${i ? "L" : "M"}${x(k).toFixed(1)},${y(a).toFixed(1)}`).join("");
  const end = x(km);
  let s = `<svg viewBox="0 0 ${w} ${h + (axis ? 30 : 0)}">`;
  if (band) s += `<rect class="band-km" x="${x(band[0])}" y="0" width="${x(band[1]) - x(band[0])}" height="${h}"/>`;
  s += `<path class="ground" d="${d}L${end},${h}L0,${h}Z"/><path class="ridge" d="${d}"/>`;
  if (band) s += `<text class="band-lbl" x="${(x(band[0]) + x(band[1])) / 2}" y="${h - 24}" text-anchor="middle">${band[2]}</text>`;
  const top = Math.max(...pts.map(p => p[1]));
  if (labels) for (const [k, a, label] of pts) {
    if (!label) continue;
    const cx = x(k), cy = y(a), anchor = k === 0 ? "start" : k === km ? "end" : "middle";
    const hot = label === "Miniere";
    s += `<circle class="pt${hot ? " top" : ""}" cx="${cx}" cy="${cy}" r="${hot ? 9 : 6}"/>`;
    s += `<text class="lbl" x="${cx}" y="${cy - 40}" text-anchor="${anchor}">${label}</text><text class="lbl-q" x="${cx}" y="${cy - 18}" text-anchor="${anchor}">${fmt(a)} m</text>`;
  }
  if (axis) for (let k = 0; k <= km; k += 5) s += `<text class="axis" x="${x(k)}" y="${h + 26}" text-anchor="${k ? "middle" : "start"}">${k} km</text>`;
  return s + "</svg>";
}

const slides = [];
const S = (cls, body) => slides.push(`<section class="slide ${cls}">${body}<footer class="sf"><span class="mk">Cogne Trail</span><span class="pg"></span></footer></section>`);

// 1 copertina
S("dark cover", `
  <img class="bgimg" src="${img("miniere")}" alt="">
  <div class="cover-in">
    <p class="kicker">Cogne Trail × Cogne Acciai Speciali</p>
    <h1 class="cas-h1">Dal ferro<br>di Cogne</h1>
    <p class="sub">Proposta di partnership · prima edizione, sabato 12 giugno 2027</p>
  </div>
  <div class="cover-prof">${profile(R28, { w: 1920, h: 300, min: 1300, max: 3100, pad: 20, labels: false, axis: false })}</div>
  <p class="cover-note">Documento riservato · bozza</p>`);

// 2 la storia comune
S("split rev", `
  <div class="col photo-col"><img src="${img("miniere")}" alt=""></div>
  <div class="col">
    <p class="alt-big">Cogne</p>
    <h2 class="t">Un nome, una storia</h2>
    <p class="body">L'acciaieria di Aosta è nata per trasformare la magnetite estratta a Cogne. Le miniere hanno chiuso nel 1979, il nome è rimasto: oggi Cogne si legge nel mondo attraverso il vostro acciaio.</p>
    <p class="body">Il 12 giugno 2027 la Miniere 28 riporta centinaia di persone sui sentieri dei minatori, fino agli edifici di Colonna a 2.425 metri. Nessun'altra azienda ha un legame così diretto con questa gara.</p>
  </div>`);

// 3 la gara delle miniere
S("race", `
  <div class="race-top">
    <div><h2 class="rn">Miniere <em>28</em></h2><p class="body">La gara che sale da Cogne alle miniere di Colonna e scende per villaggi e boschi di larice fino a Lillaz. Il primo tratto è quello dei minatori.</p></div>
    <dl class="stats"><div><dt>Distanza</dt><dd>28 km</dd></div><div><dt>Dislivello</dt><dd>1.340 m+</dd></div><div><dt>Quota max</dt><dd>2.425 m</dd></div><div><dt>Partenza</dt><dd>08:30</dd></div></dl>
  </div>
  <div class="prof">${profile(R28, { w: 1728, h: 360, min: 1350, max: 3050, pad: 70, band: [0, 7, "Il Tratto del Ferro"] })}</div>
  <p class="route">Cogne, Montroz, Miniere di Colonna, Brolliot, Goilles, Lillaz, Cogne · insieme alla Invergneux 47, 400–500 atleti attesi</p>`);

// 4 la proposta
S("partners", `
  <h2 class="t">La proposta</h2>
  <p class="lead small">Title partner della prima edizione, con un progetto costruito sulla storia che ci lega.</p>
  <div class="tiers">
    <article class="hl"><h3>Title partner</h3><p>Il vostro nome nel titolo dell'evento: arco d'arrivo, pettorali, village, sito e materiali.</p></article>
    <article class="hl"><h3>Il Tratto del Ferro</h3><p>La salita da Cogne alle miniere di Colonna, cronometrata a parte, con classifica e premio a vostro nome.</p></article>
    <article class="hl"><h3>Acciaio al traguardo</h3><p>Ogni finisher riceve un oggetto in acciaio Cogne, medaglia o placchetta, da disegnare insieme.</p></article>
    <article><h3>Squadra Cogne</h3><p>Pettorali gratuiti per i dipendenti che corrono, con uscite di preparazione sui percorsi nei mesi prima.</p></article>
    <article><h3>Corsa dei bambini</h3><p>La corsa della domenica sul prato di Sant'Orso porta il vostro nome.</p></article>
    <article><h3>Dal ferro all'acciaio</h3><p>Un racconto foto e video tra miniere, gara e stabilimento, per i vostri canali e il bilancio di sostenibilità.</p></article>
  </div>`);

// 5 squadra cogne
S("squad", `
  <div class="wc">
    <div>
      <h2 class="t">Squadra Cogne</h2>
      <p class="lead">La gara aperta a chi l'acciaio lo fa ogni giorno.</p>
    </div>
    <div>
      <p class="body">Tra le oltre 1.100 persone che lavorano in Cogne Acciai Speciali c'è chi sui sentieri della valle ci corre già. La Squadra Cogne è per loro: pettorali gratuiti o scontati, una maglia dedicata e tre uscite di preparazione sui percorsi con gli organizzatori, da marzo a maggio.</p>
      <p class="body">Il giorno della gara la squadra ha la sua classifica e la sua premiazione. Le famiglie corrono la domenica, con i bambini sul prato di Sant'Orso.</p>
    </div>
  </div>
  <div class="nums squad-nums">
    <div><b>50</b><span>pettorali gratuiti con la partnership principale</span></div>
    <div><b>3</b><span>uscite di preparazione sui percorsi</span></div>
    <div><b>−30%</b><span>sull'iscrizione per tutti gli altri dipendenti</span></div>
  </div>`);

// 6 cosa riceve
S("org", `
  <div><h2 class="t">Cosa riceve Cogne Acciai Speciali</h2><p class="lead small">Alla prima edizione il valore non sono i numeri: è essere il nome che fa nascere la gara.</p></div>
  <div class="areas"><ul>
    <li><b>Visibilità</b>Arco d'arrivo, pettorali, village, sito, social e comunicati, a partire dall'annuncio delle iscrizioni.</li>
    <li><b>Contenuti</b>Servizio fotografico e video professionale, con diritti d'uso sui vostri canali.</li>
    <li><b>Persone</b>Pettorali per la Squadra Cogne, ospitalità al village, premiazione del Tratto del Ferro.</li>
    <li><b>Esclusiva</b>Unico title partner, primo partner annunciato, prelazione sulle edizioni successive.</li>
    <li><b>Territorio</b>Il vostro nome legato a Cogne e al Parco Nazionale Gran Paradiso fin dalla prima edizione.</li>
  </ul></div>`);

// 7 tre livelli
S("levels", `
  <h2 class="t">Tre modi di esserci</h2>
  <div class="lv">
    <article class="hl">
      <p class="lv-tag">La proposta che vi facciamo</p>
      <h3>Title partner</h3>
      <p class="lv-price">15.000 €</p>
      <ul>
        <li>Il vostro nome nel titolo: Cogne Trail presentata da Cogne Acciai Speciali</li>
        <li>Arco d'arrivo, pettorali, village, sito e comunicazione</li>
        <li>Il Tratto del Ferro e l'oggetto in acciaio per i finisher</li>
        <li>Squadra Cogne: 50 pettorali gratuiti, −30% per gli altri dipendenti</li>
        <li>Corsa dei bambini a vostro nome</li>
        <li>Racconto foto e video completo, prelazione sulle edizioni successive</li>
      </ul>
    </article>
    <article>
      <p class="lv-tag">&nbsp;</p>
      <h3>Partner del Ferro</h3>
      <p class="lv-price">7.000 €</p>
      <ul>
        <li>Il Tratto del Ferro a vostro nome, con premio dedicato</li>
        <li>Logo su pettorali, village e sito</li>
        <li>Squadra Cogne: 20 pettorali gratuiti, −30% per gli altri dipendenti</li>
        <li>Foto della gara per i vostri canali</li>
      </ul>
    </article>
    <article>
      <p class="lv-tag">&nbsp;</p>
      <h3>Amici della gara</h3>
      <p class="lv-price">3.000 €</p>
      <ul>
        <li>Logo al village e sul sito</li>
        <li>−30% sull'iscrizione per tutti i dipendenti</li>
        <li>Una selezione di foto della gara</li>
      </ul>
    </article>
  </div>
  <p class="note">Importi annui, IVA esclusa. Una parte del contributo può essere in materiali, come l'acciaio per gli oggetti dei finisher.</p>`);

// 8 cosa sostiene
S("offer", `
  <h2 class="t">Cosa rende possibile</h2>
  <p class="lead small">Il contributo dei partner va dove si vede la qualità di una gara.</p>
  <ul class="offer-list">
    <li><h3>Sicurezza</h3><p>Soccorso sul percorso, controlli, gestione dei punti in quota.</p></li>
    <li><h3>Cronometraggio</h3><p>Chip, classifiche in tempo reale, il rilevamento del Tratto del Ferro.</p></li>
    <li><h3>Ristori</h3><p>Rifugi e punti ristoro con i prodotti del territorio.</p></li>
    <li><h3>Sentieri</h3><p>Tracciatura, segnaletica e ripristino dopo la gara.</p></li>
    <li><h3>Racconto</h3><p>Foto e video della gara, prima, durante e dopo.</p></li>
  </ul>
  <p class="note-in">Le iscrizioni coprono meno della metà dei costi di una gara in quota: il resto arriva da partner e territorio.</p>
  <img class="band" src="${img("sentiero")}" alt="">`);

// 7 tempi
S("timeline", `
  <h2 class="t">I tempi</h2>
  <ol class="tl tl5">
    <li><span>Dicembre 2026</span><h3>Incontro</h3><p>Presentazione del progetto e scelta delle attivazioni.</p></li>
    <li><span>Gennaio 2027</span><h3>Accordo</h3><p>Contributo, visibilità e oggetto in acciaio definiti.</p></li>
    <li><span>Inizio 2027</span><h3>Annuncio</h3><p>Il partner presentato insieme all'apertura delle iscrizioni.</p></li>
    <li class="race-day"><span>12 giugno 2027</span><h3>Si corre</h3><p>Tre giorni di evento a Cogne, il Tratto del Ferro, la corsa dei bambini.</p></li>
    <li><span>Luglio 2027</span><h3>Resoconto</h3><p>Consegna di foto, video e numeri dell'edizione.</p></li>
  </ol>
  <div class="tl-prof">${profile(R28, { w: 1920, h: 260, min: 1300, max: 3100, pad: 20, labels: false, axis: false })}</div>`);

// 8 chiusura
S("dark end", `
  <img class="bgimg" src="${img("lago")}" alt="">
  <div class="end-in">
    <p class="big-end">Dal ferro di Cogne, di corsa.</p>
    <p class="contact">Organizzazione Cogne Trail<br>cognetrail.com</p>
  </div>`);

const extra = `
.cas-h1{font-size:190px!important}
.tl5{grid-template-columns:repeat(5,1fr)!important;gap:40px!important}
.tl5 h3{font-size:34px}.tl5 p{font-size:25px}
svg .band-km{fill:rgba(181,65,42,.10)}svg .band-lbl{font:700 22px var(--d);letter-spacing:-.06em;text-transform:uppercase;fill:var(--red)}
.org .t{max-width:16ch}
.squad-nums{margin-top:90px}.squad-nums div:nth-child(1) b{color:var(--red)}.squad-nums div:nth-child(3) b{color:var(--ink)}
.lv{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:56px}
.lv article{border-top:2px solid var(--line);padding-top:26px}.lv article.hl{border-top:6px solid var(--red);padding-top:22px}
.lv-tag{height:30px;font:600 20px var(--t);color:var(--red);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.lv h3{font:600 38px var(--t);letter-spacing:-.02em}
.lv-price{font:700 64px/1.1 var(--d);letter-spacing:-.05em;margin:14px 0 26px}.lv .hl .lv-price{color:var(--red)}
.lv ul{list-style:none}.lv li{font-size:24px;line-height:1.35;color:#3f4440;padding:10px 0;border-bottom:1px solid var(--line)}
.note-in{margin-top:44px;font-size:24px;color:var(--lich)}
.offer .band{height:300px}
.tl-prof{position:absolute;left:0;right:0;bottom:0}.tl-prof .ground{fill:var(--ink)}
.timeline .sf .mk,.timeline .sf .pg{color:var(--neve)}
.offer .sf{bottom:auto;top:44px}
`;

const html = `<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Cogne Trail · Proposta Cogne Acciai Speciali</title>
<link href="https://fonts.googleapis.com/css2?family=Lexend+Zetta:wght@400;600;700;800&family=Inter+Tight:wght@400;500;600&display=swap" rel="stylesheet">
<style>${css}${extra}</style></head><body>${slides.join("\n")}</body></html>`;

const out = new URL("cas.html", dir);
writeFileSync(out, html);
const pdf = fileURLToPath(new URL("Cogne-Trail-Proposta-CAS.pdf", dir));
execFileSync("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", [
  "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
  `--print-to-pdf=${pdf}`, out.href,
], { stdio: "inherit" });
console.log("PDF pronto:", pdf, "·", slides.length, "pagine");
