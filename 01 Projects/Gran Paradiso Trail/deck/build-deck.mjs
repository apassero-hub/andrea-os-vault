// Uso: node deck/build-deck.mjs  → genera deck/deck.html, poi Chrome headless lo stampa in deck/Cogne-Trail-Presentazione.pdf
import { writeFileSync, readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const dir = new URL(".", import.meta.url);
const img = n => "data:image/jpeg;base64," + readFileSync(new URL(`../site/src/img/${n}.jpg`, dir)).toString("base64");

const R47 = [[0,1542,"Cogne"],[2.5,1500],[6.8,2310,"Arpisson"],[8.5,2050],[10.5,1809,"Gimillan"],[13,2000],[17,2517,"Rif. Grauson"],[18,2440],[20.5,2620],[23,2895,"Passo Invergneux"],[24.5,2760],[27,2700],[30,2525,"Rif. Sogno"],[34.5,2330],[37,2380],[39.5,2346,"Lago delle Loie"],[42,1700],[43,1615,"Lillaz"],[46.5,1542,"Arrivo"]];
const R28 = [[0,1543,"Cogne"],[2,1708,"Montroz"],[4,2050],[7,2425,"Miniere"],[10.5,2450],[13,2330],[16,2416,"Brolliot"],[19,2200],[22.8,1841,"Goilles"],[24,1727,"Lillaz"],[25,1600],[28,1543,"Arrivo"]];

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
function profile(pts, { w, h, min, max, pad = 50, labels = true, axis = true, kmMax }) {
  const km = kmMax ?? pts.at(-1)[0];
  const x = k => (k / km) * w, y = a => pad + (1 - (a - min) / (max - min)) * (h - pad * 2);
  const d = dense(pts).map(([k, a], i) => `${i ? "L" : "M"}${x(k).toFixed(1)},${y(a).toFixed(1)}`).join("");
  const end = x(pts.at(-1)[0]);
  let s = `<svg viewBox="0 0 ${w} ${h + (axis ? 30 : 0)}">`;
  s += `<path class="ground" d="${d}L${end},${h}L0,${h}Z"/><path class="ridge" d="${d}"/>`;
  const top = Math.max(...pts.map(p => p[1]));
  if (labels) for (const [k, a, label] of pts) {
    if (!label) continue;
    const cx = x(k), cy = y(a), anchor = k === 0 ? "start" : k === pts.at(-1)[0] ? "end" : "middle";
    s += `<circle class="pt${a === top ? " top" : ""}" cx="${cx}" cy="${cy}" r="${a === top ? 9 : 6}"/>`;
    s += `<text class="lbl" x="${cx}" y="${cy - 40}" text-anchor="${anchor}">${label}</text><text class="lbl-q" x="${cx}" y="${cy - 18}" text-anchor="${anchor}">${fmt(a)} m</text>`;
  }
  if (axis) for (let k = 0; k <= pts.at(-1)[0]; k += 5) s += `<text class="axis" x="${x(k)}" y="${h + 26}" text-anchor="${k ? "middle" : "start"}">${k} km</text>`;
  return s + "</svg>";
}

const slides = [];
const S = (cls, body) => slides.push(`<section class="slide ${cls}">${body}<footer class="sf"><span class="mk">Cogne Trail</span><span class="pg"></span></footer></section>`);

// 1 copertina
S("dark cover", `
  <img class="bgimg" src="${img("lago")}" alt="">
  <div class="cover-in">
    <p class="kicker">Cogne, Parco Nazionale Gran Paradiso</p>
    <h1>Cogne<br>Trail</h1>
    <p class="sub">Prima edizione · sabato 4 settembre 2027</p>
  </div>
  <div class="cover-prof">${profile(R47, { w: 1920, h: 300, min: 1300, max: 3100, pad: 20, labels: false, axis: false })}</div>
  <p class="cover-note">Presentazione del progetto per partner e istituzioni · bozza riservata</p>`);

// 2 perché Cogne
S("why-cogne", `
  <div class="wc">
    <div><h2 class="t">Perché Cogne</h2><p class="lead">A Cogne il trail esiste già. Manca ancora la sua gara.</p></div>
    <div>
      <p class="body">Sempre più persone corrono sui sentieri della valle e intorno a questo sport sta crescendo una comunità locale. L'idea nasce da qui: un evento che riunisca chi queste montagne le vive ogni giorno e chi arriva da fuori per scoprirle.</p>
      <p class="body">Nel mondo il trail running sta cambiando volto: più cultura, più stile, più comunità. In Valle d'Aosta questa scena è arrivata solo in parte. Cogne può essere il posto dove le due cose si incontrano.</p>
    </div>
  </div>
  <img class="band" src="${img("sentiero")}" alt="">`);

// 3 numeri
S("numbers", `
  <h2 class="t">Il progetto in breve</h2>
  <div class="nums">
    <div><b>2</b><span>gare, una sola piazza di partenza e arrivo</span></div>
    <div><b>47 + 28</b><span>chilometri, tra colli, alpeggi e miniere</span></div>
    <div><b>2.895 m</b><span>la quota più alta, il Passo Invergneux</span></div>
    <div><b>400–500</b><span>atleti alla prima edizione, per crescere con cura</span></div>
    <div><b>3</b><span>giorni di evento in paese, da venerdì a domenica</span></div>
    <div><b>4.9.27</b><span>sabato 4 settembre 2027, data proposta</span></div>
  </div>`);

// 4 Invergneux 47
S("race", `
  <div class="race-top">
    <div><h2 class="rn">Invergneux <em>47</em></h2><p class="body">Alpeggi, laghi, rifugi e il colle più alto della gara. La gara regina, per chi cerca una giornata intera in quota.</p></div>
    <dl class="stats"><div><dt>Distanza</dt><dd>46,5 km</dd></div><div><dt>Dislivello</dt><dd>2.730 m+</dd></div><div><dt>Quota max</dt><dd>2.895 m</dd></div><div><dt>Partenza</dt><dd>06:30</dd></div></dl>
  </div>
  <div class="prof">${profile(R47, { w: 1728, h: 360, min: 1350, max: 3050, pad: 70 })}</div>
  <p class="route">Cogne, Arpisson, Gimillan, Rifugio Grauson, Passo Invergneux, Rifugio Sogno, Lago delle Loie, Lillaz, Cogne</p>`);

// 5 foto lago
S("full", `<img class="bgimg" src="${img("lago")}" alt=""><p class="cap">Sul percorso della 47 km</p>`);

// 6 Miniere 28
S("race", `
  <div class="race-top">
    <div><h2 class="rn">Miniere <em>28</em></h2><p class="body">Villaggi, gallerie, boschi di larice e balconi sulla valle. Accessibile, veloce, piena di storia.</p></div>
    <dl class="stats"><div><dt>Distanza</dt><dd>28 km</dd></div><div><dt>Dislivello</dt><dd>1.340 m+</dd></div><div><dt>Quota max</dt><dd>2.425 m</dd></div><div><dt>Partenza</dt><dd>08:30</dd></div></dl>
  </div>
  <div class="prof">${profile(R28, { w: 1728, h: 360, min: 1350, max: 3050, pad: 70 })}</div>
  <p class="route">Cogne, Montroz, Miniere di Colonna, Brolliot, Goilles, Lillaz, Cogne</p>`);

// 7 miniere storia
S("split rev", `
  <div class="col photo-col"><img src="${img("miniere")}" alt=""></div>
  <div class="col">
    <p class="alt-big">2.425 m</p>
    <h2 class="t">Le miniere di Colonna</h2>
    <p class="body">Per oltre un secolo da qui è uscito il ferro magnetite che ha fatto la storia di Cogne. Chiuse nel 1979, oggi sono il cuore della 28 km: si corre tra gli edifici dei minatori, sopra il paese.</p>
    <p class="body">Un luogo della gara e un luogo da raccontare: è la storia che rende questa gara diversa da tutte le altre.</p>
  </div>`);

// 8 luoghi
S("places", `
  <h2 class="t">Dove si corre</h2>
  <div class="pl">
    <article><span>2.895 m</span><h3>Passo Invergneux</h3><p>Il punto più alto della 47 km, tra il vallone del Grauson e quello dell'Urtier, con vista aperta sul Gran Paradiso.</p></article>
    <article><span>2.425 m</span><h3>Miniere di Colonna</h3><p>Il villaggio minerario sopra Cogne, simbolo del paese e della 28 km.</p></article>
    <article><span>1.615 m</span><h3>Lillaz</h3><p>L'ultimo villaggio prima dell'arrivo, con le sue cascate. Entrambe le gare ci passano.</p></article>
    <article><span>1.542 m</span><h3>La piazza di Cogne</h3><p>Partenza, arrivo, village e ristoro finale davanti al prato di Sant'Orso.</p></article>
  </div>`);

// 9 weekend
S("weekend", `
  <h2 class="t">Il weekend</h2>
  <ol class="days">
    <li><h3>Venerdì 3 settembre</h3><ul><li><time>16:00</time>Apertura village e ritiro pettorali</li><li><time>18:30</time>Briefing e presentazione percorsi</li><li><time>20:00</time>Cena del paese con i produttori</li></ul></li>
    <li class="main"><h3>Sabato 4 settembre</h3><ul><li><time>06:30</time>Partenza Invergneux 47</li><li><time>08:30</time>Partenza Miniere 28</li><li><time>11:30</time>Primi arrivi della 28 km</li><li><time>13:00</time>Primi arrivi della 47 km</li><li><time>17:30</time>Premiazioni</li><li><time>20:00</time>Festa finale</li></ul></li>
    <li><h3>Domenica 5 settembre</h3><ul><li><time>09:30</time>Corsa dei bambini e shake-out run</li><li><time>11:00</time>Brunch di chiusura</li></ul></li>
  </ol>
  <p class="note">Gara di sabato: chi corre si ferma a dormire, il paese lavora tutto il weekend.</p>`);

// 10 perché settembre
S("why", `
  <h2 class="t">Perché settembre</h2>
  <div class="why3">
    <article><h3>Percorsi puliti</h3><p>A giugno il Passo Invergneux, quasi a 2.900 m, rischia ancora neve. A inizio settembre i sentieri sono aperti e sicuri.</p></article>
    <article><h3>Un vuoto in calendario</h3><p>Una settimana dopo l'UTMB di Chamonix e una prima del Tor des Géants: nessuna sovrapposizione con le grandi gare dell'area.</p></article>
    <article><h3>Il paese è pronto</h3><p>Dopo agosto gli alberghi tornano disponibili, la luce è perfetta e i larici iniziano a cambiare colore.</p></article>
  </div>
  <p class="note">Data proposta, da definire con il Comune e i soggetti coinvolti.</p>`);

// 11 comunità
S("community", `
  <h2 class="t">Una gara vissuta dal paese</h2>
  <p class="lead">Dalla piazza ai rifugi, con chi Cogne la vive ogni giorno.</p>
  <div class="prof thin">${profile(R28, { w: 1728, h: 200, min: 1400, max: 2600, pad: 20, labels: false, axis: false })}</div>
  <div class="cm">
    <article><h3>Piazza</h3><p>Partenza, arrivo, village, food and beverage</p></article>
    <article><h3>Paese</h3><p>Alberghi, ristoranti, bar e attività locali</p></article>
    <article><h3>Comunità</h3><p>Pro Loco, Sci Club Gran Paradiso, volontari</p></article>
    <article><h3>Territorio</h3><p>Rifugi, ristori e prodotti locali</p></article>
    <article><h3>Miniere</h3><p>Un luogo della gara, un luogo da raccontare</p></article>
  </div>`);

// 12 principi
S("principles", `
  <h2 class="t">Crescere, rimanendo Cogne</h2>
  <div class="pr">
    <article><h3>Qualità prima dei numeri</h3><p>Una prima edizione da 400–500 partecipanti, per costruire la gara con cura e crescere un passo alla volta.</p></article>
    <article><h3>Un'esperienza curata</h3><p>Percorsi, ristori, accoglienza e servizi pensati bene, dall'inizio alla fine.</p></article>
    <article><h3>Cogne dentro la gara</h3><p>Prodotti locali, rifugi, volontari e realtà del paese come parte dell'identità dell'evento.</p></article>
    <article><h3>Una gara che resta</h3><p>Una gara riconoscibile e desiderata, profondamente legata a Cogne, anno dopo anno.</p></article>
  </div>
  <p class="big-line">Ambizione alta, scala umana.</p>`);

// 13 a chi parliamo
S("audience", `
  <h2 class="t">A chi parla la gara</h2>
  <div class="why3">
    <article><h3>La nuova scena del trail</h3><p>Crew e community urbane di Milano, Torino e del nord Italia: runner giovani, attenti a stile, contenuti ed esperienza.</p></article>
    <article><h3>Chi corre in montagna</h3><p>Trail runner esperti che cercano gare tecniche, curate e fuori dai circuiti più affollati.</p></article>
    <article><h3>La valle</h3><p>Atleti, famiglie e appassionati valdostani, insieme ai turisti che a settembre scelgono Cogne e il Parco.</p></article>
  </div>`);

// 14 partner
S("partners", `
  <h2 class="t">Diventare partner</h2>
  <p class="lead small">Pochi partner, scelti, e uno solo per categoria.</p>
  <div class="tiers">
    <article class="hl"><h3>Main partner</h3><p>Uno solo. Nome accanto all'evento, arco d'arrivo, pettorali, village, contenuti.</p></article>
    <article><h3>Partner di categoria</h3><p>Uno per settore: abbigliamento, nutrizione, orologi e tracking, occhiali, bevande.</p></article>
    <article><h3>Partner di tratto</h3><p>Un rifugio, un ristoro o la salita cronometrata al Passo Invergneux con premio dedicato.</p></article>
    <article><h3>Community partner</h3><p>Crew e negozi running: iscrizioni di gruppo e uscite di avvicinamento in città.</p></article>
    <article><h3>Media partner</h3><p>Testate e creator della scena per il racconto prima, durante e dopo.</p></article>
    <article><h3>Amici di Cogne</h3><p>Alberghi, ristoranti e produttori del paese dentro la gara e dentro il racconto.</p></article>
  </div>`);

// 15 cosa offriamo
S("offer", `
  <div class="col">
    <h2 class="t">Cosa offriamo</h2>
    <p class="lead small">Alla prima edizione il valore non sono i numeri: sono i contenuti e la scena.</p>
  </div>
  <ul class="offer-list">
    <li><h3>Contenuti foto e video</h3><p>Servizio fotografico e video professionale della gara, con il vostro prodotto in azione, utilizzabile sui vostri canali.</p></li>
    <li><h3>Presenza in gara</h3><p>Visibilità su percorso, village, pettorali e materiali, calibrata sul livello di partnership.</p></li>
    <li><h3>Prodotto in prova</h3><p>Test sui percorsi nei mesi prima della gara con atleti e community.</p></li>
    <li><h3>Esclusiva di categoria</h3><p>Nel vostro settore ci siete solo voi.</p></li>
    <li><h3>Un territorio unico</h3><p>Il nome legato a Cogne e al Parco Nazionale Gran Paradiso fin dalla prima edizione.</p></li>
  </ul>`);

// 16 organizzazione
S("org", `
  <h2 class="t">Costruirla insieme</h2>
  <div class="org">
    <div class="who">
      <article><h3>Comune di Cogne</h3><p>Supporto e coordinamento</p></article>
      <article><h3>Parco Nazionale Gran Paradiso</h3><p>Percorsi, territorio, autorizzazioni</p></article>
      <article><h3>Realtà locali</h3><p>Sci Club Gran Paradiso, Pro Loco, rifugi, operatori, volontari</p></article>
    </div>
    <div class="areas">
      <h3>Cinque ambiti di lavoro</h3>
      <ul><li><b>Organizzazione</b> Sci Club Gran Paradiso e comitato organizzatore</li><li><b>Percorsi</b> sopralluoghi, tracciatura, ristori, controlli</li><li><b>Comunicazione</b> identità, sito, foto e video, promozione</li><li><b>Gara</b> iscrizioni, cronometraggio, classifiche</li><li><b>Sicurezza</b> piano di sicurezza, soccorso, gestione percorso</li></ul>
    </div>
  </div>`);

// 17 timeline
S("timeline", `
  <h2 class="t">Verso la prima edizione</h2>
  <ol class="tl">
    <li><span>Inverno 2026</span><h3>Partner e autorizzazioni</h3><p>Accordi con Comune e Parco, ricerca partner, identità e sito.</p></li>
    <li><span>Primavera 2027</span><h3>Iscrizioni aperte</h3><p>Lancio pubblico, apertura iscrizioni, attivazioni con le crew.</p></li>
    <li><span>Estate 2027</span><h3>Sopralluoghi e tracciatura</h3><p>Percorsi definitivi, ristori, piano di sicurezza, volontari.</p></li>
    <li class="race-day"><span>4 settembre 2027</span><h3>Si corre</h3><p>Tre giorni di evento a Cogne.</p></li>
  </ol>`);

// 18 chiusura
S("dark end", `
  <img class="bgimg" src="${img("sentiero")}" alt="">
  <div class="end-in">
    <p class="big-end">Si parte da Cogne.</p>
    <p class="contact">Organizzazione Cogne Trail<br>cognetrail.com</p>
  </div>`);

const html = `<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Cogne Trail · Presentazione</title>
<link href="https://fonts.googleapis.com/css2?family=Lexend+Zetta:wght@400;600;700;800&family=Inter+Tight:wght@400;500;600&display=swap" rel="stylesheet">
<style>
@page{size:1920px 1080px;margin:0}
:root{--neve:#E4E6DA;--ink:#1E2119;--red:#B5412A;--red2:#D4573D;--lich:#6B7258;--rock:#8D917F;--line:#C8CBBC;--d:"Lexend Zetta",sans-serif;--t:"Inter Tight",sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#777}
body{font:400 30px/1.45 var(--t);color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact;counter-reset:pg}
.slide:last-child{break-after:auto;page-break-after:auto}
.slide{width:1920px;height:1080px;position:relative;overflow:hidden;background:var(--neve);padding:110px 96px 120px;page-break-after:always;break-after:page;counter-increment:pg}
.sf{position:absolute;left:96px;right:96px;bottom:44px;display:flex;justify-content:space-between;font-size:20px;color:var(--rock)}
.sf .mk{font:700 20px var(--d);letter-spacing:-.09em;transform:skewX(-12deg);display:inline-block;color:var(--ink)}
.sf .pg::after{content:counter(pg,decimal-leading-zero)}
.dark{background:var(--ink);color:var(--neve)}.dark .sf .mk{color:var(--neve)}
.t{font:700 64px/1.1 var(--d);letter-spacing:-.03em;text-transform:uppercase;margin-bottom:48px}
.lead{font:500 58px/1.1 var(--t);letter-spacing:-.025em;max-width:22ch;margin-bottom:44px}
.lead.small{font-size:44px;max-width:30ch}
.body{max-width:40ch;color:#3f4440;margin-bottom:26px}
.note{position:absolute;left:96px;bottom:110px;font-size:24px;color:var(--rock)}
img{display:block}
.bgimg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
/* svg */
svg{width:100%;height:auto;display:block;overflow:visible}
svg .ground{fill:#D3D6C8}svg .ridge{fill:none;stroke:var(--red);stroke-width:4;stroke-linejoin:round}
svg .pt{fill:var(--neve);stroke:var(--red);stroke-width:3.5}svg .pt.top{fill:var(--red)}
svg .lbl{font:600 22px var(--t);fill:var(--ink)}svg .lbl-q{font:400 19px var(--t);fill:var(--rock)}svg .axis{font:400 18px var(--t);fill:var(--rock)}
/* cover */
.cover .bgimg{opacity:.32;mix-blend-mode:luminosity}
.cover-in{position:relative;z-index:2}
.kicker{font:500 30px var(--t);color:#B9BDAE}
.cover h1{font:700 230px/1 var(--d);letter-spacing:-.04em;text-transform:uppercase;margin:30px 0 40px}
.cover .sub{font:600 36px var(--t)}
.cover-prof{position:absolute;left:0;right:0;bottom:0;z-index:1}
.cover-prof .ground{fill:var(--ink)}.cover-prof .ridge{stroke:var(--red2)}
.cover-note{position:absolute;right:96px;top:120px;font-size:22px;color:#B9BDAE;z-index:2}
.cover .sf{z-index:3}
/* split */
.split{display:grid;grid-template-columns:1fr 1fr;gap:96px;padding-right:0}
.split.rev{padding-right:96px;padding-left:0}
.photo-col{margin:-110px 0 -120px;position:relative}
.photo-col img{width:100%;height:100%;object-fit:cover;mix-blend-mode:multiply}
.alt-big{font:700 150px/1 var(--d);letter-spacing:-.05em;color:var(--red);margin-bottom:30px}
.wc{display:grid;grid-template-columns:1fr 1fr;gap:96px}.wc .body{font-size:27px}
.band{position:absolute;left:0;right:0;bottom:0;width:100%;height:330px;object-fit:cover;object-position:50% 58%;mix-blend-mode:multiply}
.why-cogne .sf{bottom:auto;top:44px}
/* numbers */
.nums{display:grid;grid-template-columns:repeat(3,1fr);gap:64px 80px;margin-top:20px}
.nums div{border-top:4px solid var(--ink);padding-top:22px}
.nums b{display:block;font:700 86px/1.05 var(--d);letter-spacing:-.05em;margin-bottom:14px}
.nums div:nth-child(3) b{color:var(--red)}
.nums span{font-size:28px;color:#3f4440}
/* race */
.race-top{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:56px;align-items:end}
.rn{white-space:nowrap;font:700 80px/1 var(--d);letter-spacing:-.04em;text-transform:uppercase;margin-bottom:24px}.rn em{font-style:normal;color:var(--red)}
.stats{display:grid;grid-template-columns:repeat(4,auto);gap:40px}
.stats dt{font-size:22px;color:var(--rock)}.stats dd{font:600 34px/1.2 var(--d);letter-spacing:-.04em;white-space:nowrap}
.prof{margin-top:40px}
.route{position:absolute;left:96px;bottom:96px;font-size:24px;color:#3f4440}
/* full */
.full{padding:0}.full .bgimg{mix-blend-mode:multiply}
.cap{position:absolute;left:96px;bottom:110px;font-size:22px;color:var(--neve);background:var(--ink);padding:8px 16px}
/* places */
.pl{display:grid;grid-template-columns:repeat(4,1fr);gap:56px}
.pl span{display:block;font:700 54px/1 var(--d);letter-spacing:-.05em;color:var(--red);margin-bottom:30px}
.pl h3{font:600 34px/1.2 var(--t);margin-bottom:14px}.pl p{font-size:26px;color:#3f4440}
.pl article{border-top:2px solid var(--line);padding-top:30px}
/* weekend */
.days{list-style:none;display:grid;grid-template-columns:repeat(3,1fr);gap:64px}
.days>li{border-top:5px solid var(--ink);padding-top:26px}.days>li.main{border-color:var(--red)}
.days h3{font:600 32px/1.2 var(--d);letter-spacing:-.04em;margin-bottom:24px}
.days ul{list-style:none}.days ul li{display:grid;grid-template-columns:110px 1fr;padding:12px 0;border-bottom:1px solid var(--line);font-size:26px}
.days time{font-weight:600}
/* why */
.why3{display:grid;grid-template-columns:repeat(3,1fr);gap:72px}
.why3 article{border-top:5px solid var(--ink);padding-top:30px}.why3 article:first-child{border-color:var(--red)}
.why3 h3{font:600 40px/1.2 var(--t);letter-spacing:-.02em;margin-bottom:20px}.why3 p{color:#3f4440}
/* community */
.prof.thin{margin:0 0 50px}.prof.thin .ground{fill:var(--ink)}
.cm{display:grid;grid-template-columns:repeat(5,1fr);gap:40px}
.cm h3{font:600 28px var(--d);letter-spacing:-.04em;text-transform:uppercase;margin-bottom:12px}.cm p{font-size:25px;color:#3f4440}
/* principles */
.pr{display:grid;grid-template-columns:repeat(4,1fr);gap:56px}
.pr article{border-left:2px solid var(--line);padding-left:30px}
.pr h3{font:600 36px/1.15 var(--t);margin-bottom:18px}.pr p{font-size:26px;color:#3f4440}
.big-line{position:absolute;left:96px;bottom:130px;font:700 60px var(--d);letter-spacing:-.04em;text-transform:uppercase;color:var(--red)}
/* audience reuse why3 */
/* partners */
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:44px 64px}
.tiers article{border-top:2px solid var(--line);padding-top:22px}.tiers article.hl{border-top:5px solid var(--red)}
.tiers h3{font:600 34px var(--t);margin-bottom:10px}.tiers p{font-size:25px;color:#3f4440}
/* offer */
.offer-list{display:grid;grid-template-columns:repeat(5,1fr);gap:40px;list-style:none;margin-top:30px}
.offer-list li{border-top:5px solid var(--ink);padding-top:24px}.offer-list li:first-child{border-color:var(--red)}
.offer-list h3{font:600 30px/1.2 var(--t);margin-bottom:14px}.offer-list p{font-size:24px;color:#3f4440}
/* org */
.org{display:grid;grid-template-columns:1fr 1.1fr;gap:110px}
.who article{border-top:2px solid var(--line);padding:22px 0 26px}.who h3{font:600 36px var(--t)}.who p{font-size:26px;color:#3f4440}
.areas h3{font:600 30px var(--d);letter-spacing:-.04em;text-transform:uppercase;margin-bottom:24px}
.areas ul{list-style:none}.areas li{padding:16px 0;border-bottom:1px solid var(--line);font-size:26px;color:#3f4440}.areas b{display:block;color:var(--ink);font-size:30px}
/* timeline */
.tl{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:48px;position:relative;margin-top:40px}
.tl li{border-top:5px solid var(--ink);padding-top:26px}.tl li.race-day{border-color:var(--red)}
.tl span{display:block;font:600 26px var(--d);letter-spacing:-.04em;color:var(--lich);margin-bottom:24px}.tl li.race-day span{color:var(--red)}
.tl h3{font:600 36px/1.15 var(--t);margin-bottom:14px}.tl p{font-size:26px;color:#3f4440}
/* end */
.end .bgimg{opacity:.35;mix-blend-mode:luminosity}
.end-in{position:absolute;left:96px;bottom:150px}
.big-end{font:700 128px/1.05 var(--d);letter-spacing:-.04em;text-transform:uppercase;color:var(--red2);margin-bottom:56px;max-width:14ch}
.contact{font-size:34px;line-height:1.5}
</style></head><body>${slides.join("\n")}</body></html>`;

const out = new URL("deck.html", dir);
writeFileSync(out, html);
const pdf = fileURLToPath(new URL("Cogne-Trail-Presentazione.pdf", dir));
execFileSync("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", [
  "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
  `--print-to-pdf=${pdf}`, out.href,
], { stdio: "inherit" });
console.log("PDF pronto:", pdf, "·", slides.length, "pagine");
