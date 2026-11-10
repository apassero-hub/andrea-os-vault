// Uso: node build.mjs "password"   → genera dist/index.html con il contenuto cifrato (AES-GCM + PBKDF2)
import { readFileSync, writeFileSync } from "node:fs";
import { webcrypto as crypto } from "node:crypto";

const password = process.argv[2];
if (!password) { console.error('Uso: node build.mjs "password"'); process.exit(1); }
const dir = new URL(".", import.meta.url);

// Punti chiave dal deck di Alessandro: [km, quota, etichetta]
const R47 = [[0,1542,"Cogne"],[2.5,1500],[6.8,2310,"Arpisson"],[8.5,2050],[10.5,1809,"Gimillan"],[13,2000],[17,2517,"Rif. Grauson"],[18,2440],[20.5,2620],[23,2895,"Passo Invergneux"],[24.5,2760],[27,2700],[30,2525,"Rif. Sogno"],[34.5,2330],[37,2380],[39.5,2346,"Lago delle Loie"],[42,1700],[43,1615,"Lillaz"],[46.5,1542,"Arrivo"]];
const R28 = [[0,1543,"Cogne"],[2,1708,"Montroz"],[4,2050],[7,2425,"Miniere"],[10.5,2450],[13,2330],[16,2416,"Brolliot"],[19,2200],[22.8,1841,"Goilles"],[24,1727,"Lillaz"],[25,1600],[28,1543,"Arrivo"]];

// interpolazione con piccole irregolarità deterministiche, per un profilo che sembri sentiero
function dense(pts, step = 0.25) {
  const out = []; let seed = 7;
  const rnd = () => (seed = (seed * 9301 + 49297) % 233280) / 233280 - 0.5;
  for (let i = 0; i < pts.length - 1; i++) {
    const [k0, a0] = pts[i], [k1, a1] = pts[i + 1];
    for (let k = k0; k < k1; k += step) {
      const t = (k - k0) / (k1 - k0), e = t * t * (3 - 2 * t);
      const edge = Math.min(t, 1 - t) * 2;
      out.push([k, a0 + (a1 - a0) * e + rnd() * 26 * edge]);
    }
  }
  out.push(pts.at(-1).slice(0, 2));
  return out;
}

function profile(pts, { w, h, min, max, pad = 40, hero = false }) {
  const km = pts.at(-1)[0];
  const x = k => (k / km) * w, y = a => pad + (1 - (a - min) / (max - min)) * (h - pad * 2);
  const d = dense(pts).map(([k, a], i) => `${i ? "L" : "M"}${x(k).toFixed(1)},${y(a).toFixed(1)}`).join("");
  let s = `<svg viewBox="0 0 ${w} ${h}" role="img">`;
  s += `<path class="ground" d="${d}L${w},${h}L0,${h}Z"/><path class="ridge" d="${d}"/>`;
  for (const [k, a, label] of pts) {
    if (!label) continue;
    const cx = x(k), cy = y(a), top = a === Math.max(...pts.map(p => p[1]));
    const anchor = k === 0 ? "start" : k === km ? "end" : hero ? (k < km * .35 ? "start" : k > km * .65 ? "end" : "middle") : "middle";
    const lx = cx + (hero && anchor === "start" && k ? 8 : hero && anchor === "end" && k !== km ? -8 : 0);
    s += `<circle class="pt" cx="${cx}" cy="${cy}" r="${top ? 6 : 4.5}"/>`;
    const ty = hero && !top ? cy + 30 : cy - 22;
    s += `<text class="lbl${top ? " keep top" : ""}" x="${lx}" y="${ty}" text-anchor="${anchor}">${label}</text>`;
    s += `<text class="lbl-q${top ? " top" : ""}" x="${lx}" y="${ty + 15}" text-anchor="${anchor}">${String(a).replace(/\B(?=(\d{3})+$)/, ".")} m</text>`;
  }
  if (!hero) for (let k = 0; k <= km; k += 5) s += `<text class="axis" x="${x(k)}" y="${h + 16}" text-anchor="${k === 0 ? "start" : "middle"}">${k} km</text>`;
  return s + "</svg>";
}

let content = readFileSync(new URL("src/content.html", dir), "utf8")
  .replace("{{PROFILE_HERO}}", profile(R47, { w: 1200, h: 360, min: 1350, max: 3050, pad: 20, hero: true }))
  .replace("{{PROFILE_47}}", profile(R47, { w: 1000, h: 230, min: 1400, max: 3000 }))
  .replace("{{PROFILE_28}}", profile(R28, { w: 1000, h: 230, min: 1400, max: 3000 }));

content = content.replace(/\{\{IMG_(\w+)\}\}/g, (_, n) => "data:image/jpeg;base64," + readFileSync(new URL(`src/img/${n}.jpg`, dir)).toString("base64"))
  .replace(/\{\{PNG_(\w+)\}\}/g, (_, n) => "data:image/png;base64," + readFileSync(new URL(`src/img/${n}.png`, dir)).toString("base64")); // PNG per i loghi con trasparenza
const enc = new TextEncoder();
const salt = crypto.getRandomValues(new Uint8Array(16)), iv = crypto.getRandomValues(new Uint8Array(12));
const base = await crypto.subtle.importKey("raw", enc.encode(password), "PBKDF2", false, ["deriveKey"]);
const key = await crypto.subtle.deriveKey({ name: "PBKDF2", salt, iterations: 250000, hash: "SHA-256" }, base, { name: "AES-GCM", length: 256 }, false, ["encrypt"]);
const data = new Uint8Array(await crypto.subtle.encrypt({ name: "AES-GCM", iv }, key, enc.encode(content)));
const payload = Buffer.concat([salt, iv, data]).toString("base64");

const html = readFileSync(new URL("src/template.html", dir), "utf8").replace("{{PAYLOAD}}", payload);
writeFileSync(new URL("dist/index.html", dir), html);
console.log("dist/index.html pronto,", (html.length / 1024).toFixed(0), "KB");
