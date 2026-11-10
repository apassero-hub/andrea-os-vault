// Genera i file SVG del logo in logo/. Uso: node tools/logo.mjs
import { writeFileSync } from "node:fs";
import { pathToFileURL } from "node:url";
// scrive i file solo se lanciato direttamente, non quando lo importa site/build.mjs
const main = process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href;
const write = (f, t) => main && writeFileSync(f, t);
const out = n => new URL(`../logo/${n}`, import.meta.url);
const N = "#E4E6DA", M = "#1E2119", R = "#B5412A";
const pts = a => a.map(p => p.join(",")).join(" ");
// segno: la V della valle di Cogne con il massiccio del Gran Paradiso dietro (100 x 100)
const SKY = [[0,34],[14,30],[22,24],[32,28],[42,20],[50,14],[58,16],[66,24],[74,22],[80,16],[86,20],[100,18]];
const SNOW = [[50,14],[58,16],[66,24],[74,22],[80,16],[86,20],[94,25],[78,31],[64,35],[56,25]];
export const segno = (m, s, v) => `<polygon points="${pts(SKY)} 100,94 0,94" fill="${m}"/><polygon points="${pts(SNOW)}" fill="${s}" transform="translate(0,3.5)"/><polygon points="0,40 50,94 0,94" fill="${v}"/><polygon points="100,44 50,94 100,94" fill="${v}"/>`;
export const badge = (bg = R, m = N, v = M) => `<rect x="-20" y="-20" width="140" height="140" rx="10" fill="${bg}"/>${segno(m, bg, v)}`;
const font = `<style>@import url("https://fonts.googleapis.com/css2?family=Lexend+Zetta:wght@700&amp;display=swap");</style>`;
const svg = (vb, body, extra = "") => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}">${extra}${body}</svg>\n`;

write(out("segno.svg"), svg("-20 -20 140 140", badge()));
write(out("segno-scuro.svg"), svg("-20 -20 140 140", badge("#D4573D")));
write(out("segno-scritta.svg"), svg("0 0 470 110", `<g transform="translate(0,4)">${segno(R, N, M)}</g><g transform="translate(122,58) skewX(-12)"><text font-family="Lexend Zetta" font-weight="700" font-size="46" letter-spacing="-0.06em" fill="${M}">COGNE</text></g><g transform="translate(124,92) skewX(-12)"><text font-family="Lexend Zetta" font-weight="700" font-size="17" letter-spacing="-0.02em" fill="${R}">TRAIL · GRAN PARADISO</text></g>`, font));

// timbro: la scena ricalcata dalla foto, su 1300 px di larghezza
const S = [[0,395],[90,400],[165,410],[215,370],[265,345],[330,368],[410,378],[470,352],[545,318],[600,284],[640,285],[668,268],[750,262],[810,300],[905,345],[965,330],[995,290],[1030,282],[1065,268],[1100,262],[1125,290],[1200,305],[1270,300],[1300,290]];
const SN = [[668,268],[750,262],[810,300],[905,345],[965,330],[995,290],[1030,282],[1065,268],[1100,262],[1125,290],[1200,305],[1250,325],[1150,352],[1060,398],[960,432],[870,420],[790,372],[720,322]];
const scene = `<polygon points="${pts(S)} 1300,960 0,960" fill="${R}"/><polygon points="${pts(SN)}" fill="${N}" transform="translate(0,26)"/><polygon points="0,410 140,470 330,640 480,760 650,960 0,960" fill="${M}"/><polygon points="1300,470 1200,560 1000,650 850,770 650,960 1300,960" fill="${M}"/>`;
write(out("timbro.svg"), svg("0 0 400 400", `<defs><clipPath id="cv"><circle cx="200" cy="200" r="140"/></clipPath><path id="ring" d="M200,38 a162,162 0 1,1 -0.1,0"/></defs><circle cx="200" cy="200" r="192" fill="${M}"/><circle cx="200" cy="200" r="140" fill="${N}"/><g clip-path="url(#cv)"><g transform="translate(5,52) scale(.3)">${scene}</g></g><text font-family="Lexend Zetta" font-weight="700" font-size="21" letter-spacing="0.02em" fill="${N}"><textPath href="#ring">COGNE TRAIL · PARCO NAZIONALE GRAN PARADISO ·</textPath></text>`, font));
if (main) console.log("logo/: segno.svg, segno-scuro.svg, segno-scritta.svg, timbro.svg");
