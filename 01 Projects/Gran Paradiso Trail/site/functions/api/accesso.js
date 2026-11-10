// Cloudflare Pages Function: registra chi entra nell'anteprima (email, data, paese) nel KV "ACCESSI".
// Per leggerli: dashboard Cloudflare > KV > ACCESSI, oppure apri /api/accesso nel browser (export CSV):
// il browser chiede utente e password; l'utente è libero, la password è ADMIN_KEY (come per /api/contatto).
const clean = (v, max) => String(v ?? "").trim().slice(0, max);
// cella CSV sicura: un valore che inizia con = + - @ verrebbe letto da Excel come formula
const cell = v => { const t = String(v ?? "").replace(/[\u0000-\u001f]/g, " "); return (/^[=+\-@]/.test(t) ? "'" + t : t).replaceAll('"', '""'); };

export async function onRequestPost({ request, env }) {
  let d;
  try { d = await request.json(); } catch { return new Response("Richiesta non valida", { status: 400 }); }
  const email = clean(d.email, 160).toLowerCase();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return new Response("Email non valida", { status: 422 });
  if (!env.ACCESSI) return new Response(null, { status: 204 }); // KV non ancora collegato: il sito funziona lo stesso

  const cf = request.cf || {};
  const rec = {
    email,
    data: new Date().toISOString(),
    paese: clean(cf.country, 4),
    citta: clean(cf.city, 80),
    browser: clean(request.headers.get("user-agent"), 200),
  };
  await env.ACCESSI.put(`${rec.data}_${crypto.randomUUID().slice(0, 8)}`, JSON.stringify(rec));
  return new Response(null, { status: 201 });
}

// Confronto a tempo costante sulle impronte SHA-256, come in contatto.js.
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
    try { const d = atob(auth.slice(6)); return d.slice(d.indexOf(":") + 1); } catch { return ""; }
  }
  return "";
}

// /api/accesso → tutti gli accessi; /api/accesso?riepilogo=1 → una riga per email con numero di accessi, primo e ultimo
export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const key = suppliedKey(request);
  if (!env.ADMIN_KEY || !key || !(await sameSecret(key, env.ADMIN_KEY))) {
    return new Response("Non autorizzato", { status: 401, headers: { "WWW-Authenticate": 'Basic realm="Accessi Cogne Trail", charset="UTF-8"' } });
  }
  const recs = [];
  let cursor;
  do {
    const page = await env.ACCESSI.list({ cursor });
    for (const k of page.keys) recs.push(JSON.parse(await env.ACCESSI.get(k.name)));
    cursor = page.list_complete ? null : page.cursor;
  } while (cursor);

  let cols, rows;
  if (url.searchParams.get("riepilogo")) {
    const by = new Map();
    for (const r of recs) {
      const s = by.get(r.email) || { email: r.email, accessi: 0, primo: r.data, ultimo: r.data, paese: r.paese };
      s.accessi++; if (r.data < s.primo) s.primo = r.data; if (r.data > s.ultimo) { s.ultimo = r.data; s.paese = r.paese; }
      by.set(r.email, s);
    }
    cols = ["email", "accessi", "primo", "ultimo", "paese"]; rows = [...by.values()].sort((a, b) => b.ultimo.localeCompare(a.ultimo));
  } else {
    cols = ["data", "email", "paese", "citta", "browser"]; rows = recs.sort((a, b) => b.data.localeCompare(a.data));
  }
  const csv = [cols.join(";"), ...rows.map(r => cols.map(c => `"${cell(r[c])}"`).join(";"))].join("\n");
  return new Response(csv, { headers: { "Content-Type": "text/csv; charset=utf-8", "Content-Disposition": "attachment; filename=accessi.csv", "Cache-Control": "no-store" } });
}
