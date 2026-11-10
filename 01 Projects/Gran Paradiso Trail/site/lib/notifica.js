// Manda una mail di notifica tramite il Worker cognetrail-notifiche (service binding NOTIFICHE).
// Va passata a waitUntil: la risposta al visitatore parte subito, la mail viaggia dopo.
// Se il binding manca o l'invio fallisce, il sito funziona lo stesso (l'errore resta solo nei log).
export async function notifica(env, oggetto, testo, rispondiA) {
  if (!env.NOTIFICHE) return;
  try {
    const r = await env.NOTIFICHE.fetch("https://notifiche/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ oggetto, testo, rispondiA }),
    });
    if (!r.ok) console.error("notifica non inviata", r.status, await r.text());
  } catch (e) {
    console.error("notifica non inviata", e);
  }
}

// Data e ora italiane, leggibili nella mail.
export const quando = iso => new Date(iso).toLocaleString("it-IT", { timeZone: "Europe/Rome", dateStyle: "full", timeStyle: "short" });
