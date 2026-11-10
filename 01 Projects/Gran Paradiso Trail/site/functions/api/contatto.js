// Cloudflare Pages Function: riceve le richieste di contatto dal sito e le salva nel KV "CONTATTI".
// Per leggerle: dashboard Cloudflare > KV > CONTATTI, oppure apri /api/contatto nel browser (export CSV):
// il browser chiede utente e password; l'utente è libero, la password è ADMIN_KEY. La chiave non va più
// nell'indirizzo (resterebbe nella cronologia e nei log).
// Ogni richiesta arriva anche per mail a organizzazione@cognetrail.com, con "Rispondi" verso chi ha scritto.
import { notifica, quando } from "../../lib/notifica.js";
const TIPI = ["brand", "atleta", "media", "cogne"];
const ETICHETTE = { brand: "Brand o partner", atleta: "Atleta o crew", media: "Media o creator", cogne: "Realtà di Cogne", altro: "Altro" };
const clean = (v, max) => String(v ?? "").trim().slice(0, max);

export async function onRequestPost({ request, env, waitUntil }) {
  let d;
  try { d = await request.json(); } catch { return new Response("Richiesta non valida", { status: 400 }); }
  if (d.sito) return new Response(null, { status: 204 }); // campo trappola compilato: bot, ignoriamo in silenzio

  const rec = {
    tipo: TIPI.includes(d.tipo) ? d.tipo : "altro",
    nome: clean(d.nome, 120),
    email: clean(d.email, 160),
    telefono: clean(d.telefono, 40),
    organizzazione: clean(d.organizzazione, 160),
    messaggio: clean(d.messaggio, 2000),
    privacy: d.privacy === "on",
    data: new Date().toISOString(),
  };
  if (!rec.nome || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(rec.email) || !rec.privacy) {
    return new Response("Dati mancanti", { status: 422 });
  }
  await env.CONTATTI.put(`${rec.data}_${crypto.randomUUID().slice(0, 8)}`, JSON.stringify(rec));
  waitUntil(notifica(env, `Richiesta di contatto: ${rec.nome} (${ETICHETTE[rec.tipo]})`,
    `Nuova richiesta dal modulo contatti di Cogne Trail.\n\n` +
    `Chi è: ${ETICHETTE[rec.tipo]}\n` +
    `Nome: ${rec.nome}\n` +
    `Email: ${rec.email}\n` +
    `Telefono: ${rec.telefono || "-"}\n` +
    `Azienda, crew o realtà: ${rec.organizzazione || "-"}\n` +
    `Quando: ${quando(rec.data)}\n\n` +
    `Messaggio:\n${rec.messaggio || "-"}\n\n` +
    `Rispondendo a questa mail scrivi direttamente a ${rec.email}.`, rec.email));
  return new Response(null, { status: 201 });
}

// Confronto a tempo costante: si confrontano le impronte SHA-256, così la durata non dice quanti caratteri tornano.
async function sameSecret(a, b) {
  const enc = new TextEncoder();
  const [x, y] = await Promise.all([a, b].map(v => crypto.subtle.digest("SHA-256", enc.encode(v))));
  const ux = new Uint8Array(x), uy = new Uint8Array(y);
  let diff = 0;
  for (let i = 0; i < ux.length; i++) diff |= ux[i] ^ uy[i];
  return diff === 0;
}

// La password dall'intestazione Authorization: "Basic" (dal browser) oppure "Bearer <chiave>" (da script).
function suppliedKey(request) {
  const auth = request.headers.get("Authorization") || "";
  if (auth.startsWith("Bearer ")) return auth.slice(7);
  if (auth.startsWith("Basic ")) {
    try {
      const decoded = atob(auth.slice(6));
      return decoded.slice(decoded.indexOf(":") + 1);
    } catch { return ""; }
  }
  return "";
}

// Un valore che comincia con = + - @ (o tab, a capo) Excel lo eseguirebbe come formula: lo si rende testo.
const safeCell = s => (/^[=+\-@\t\r]/.test(s) ? "'" + s : s);

export async function onRequestGet({ request, env }) {
  const key = suppliedKey(request);
  if (!env.ADMIN_KEY || !key || !(await sameSecret(key, env.ADMIN_KEY))) {
    return new Response("Non autorizzato", {
      status: 401,
      headers: { "WWW-Authenticate": 'Basic realm="Contatti Gran Paradiso Trail", charset="UTF-8"' },
    });
  }
  const cols = ["data", "tipo", "nome", "email", "telefono", "organizzazione", "messaggio"];
  const rows = [cols.join(";")];
  let cursor;
  do {
    const page = await env.CONTATTI.list({ cursor });
    for (const k of page.keys) {
      const r = JSON.parse(await env.CONTATTI.get(k.name));
      rows.push(cols.map(c => `"${safeCell(String(r[c] ?? "")).replaceAll('"', '""')}"`).join(";"));
    }
    cursor = page.list_complete ? null : page.cursor;
  } while (cursor);
  return new Response(rows.join("\n"), { headers: { "Content-Type": "text/csv; charset=utf-8", "Content-Disposition": "attachment; filename=contatti.csv", "Cache-Control": "no-store" } });
}
