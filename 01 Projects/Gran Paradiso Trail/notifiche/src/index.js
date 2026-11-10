// Manda una mail di notifica. Riceve dal sito (service binding) un JSON { oggetto, testo, rispondiA? }.
// Il destinatario è fisso nel binding: la casella che riceve organizzazione@cognetrail.com.
// L'inoltro mail di Cloudflare lascia inviare solo verso indirizzi verificati, per questo qui c'è
// la Gmail di Alessandro e non organizzazione@cognetrail.com (che a sua volta inoltra a lui).
const MITTENTE = { email: "notifiche@cognetrail.com", name: "Cogne Trail" };
const EMAIL_OK = /^[^@\s<>"]+@[^@\s<>"]+\.[^@\s<>"]+$/;

export default {
  async fetch(request, env) {
    if (request.method !== "POST") return new Response("Metodo non ammesso", { status: 405 });
    let d;
    try { d = await request.json(); } catch { return new Response("Richiesta non valida", { status: 400 }); }
    const oggetto = String(d.oggetto ?? "").replace(/[\r\n]+/g, " ").slice(0, 200);
    const testo = String(d.testo ?? "").slice(0, 5000);
    if (!oggetto || !testo) return new Response("Dati mancanti", { status: 422 });

    const msg = { from: MITTENTE, to: "abram.alessandro01@gmail.com", subject: oggetto, text: testo };
    if (EMAIL_OK.test(d.rispondiA ?? "")) msg.replyTo = d.rispondiA;
    try {
      const r = await env.EMAIL.send(msg);
      return Response.json({ ok: true, id: r?.messageId ?? null });
    } catch (e) {
      console.error("invio fallito", e.code, e.message);
      return Response.json({ ok: false, code: e.code ?? null, message: e.message }, { status: 502 });
    }
  },
};
