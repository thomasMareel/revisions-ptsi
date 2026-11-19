/* ===== Relais de l'assistant IA (Cloudflare Worker) — docs/assistant-ia.md, phase 1 =====
   Le site est public et statique : AUCUNE clé n'y figure. Ce relais garde la clé de l'API
   Claude (secret ANTHROPIC_API_KEY), vérifie l'accès (code personnel → jeton signé),
   plafonne le débit et la dépense du jour, puis relaie la réponse de Claude en flux SSE.

   Routes : GET /sante · POST /auth { code } → { jeton, exp } ·
            POST /chat (Authorization: Bearer <jeton>) { chapitre, contenu, contexte,
                 historique:[{ role, texte, contexte? }], question, approfondir } → flux SSE :
                 event texte { t } … puis event fin { arret, modele, cout, usage } ou event erreur { code }.
   Secrets (tableau de bord Cloudflare ou « npx wrangler secret put ») : ANTHROPIC_API_KEY,
   ASSISTANT_CODE (le code personnel de Thomas), JETON_CLE (longue chaîne aléatoire).
   Variables et espace KV « COMPTEURS » : wrangler.toml. */
import Anthropic from '@anthropic-ai/sdk';
import { REGLES_ECRIT, blocChapitre, messageUtilisateur } from './prompts.js';
import { signer, verifier, egal } from './jeton.js';

// Tarifs publics, dollars par million de jetons (relevés le 2026-11-19) : entrée, sortie,
// écriture du cache (5 min), lecture du cache. Modèle inconnu : tarif le plus cher (prudence).
const PRIX = {
  'claude-sonnet-5-5': [2, 10, 2.5, 0.1],
  'claude-sonnet-5': [2, 10, 2.5, 0.2],
  'claude-opus-5-5': [4, 20, 5, 0.2],
  'claude-haiku-5-5': [0.1, 0.5, 0.125, 0.01],
};
const PRIX_DEFAUT = [8, 40, 10, 0.4];
const LIMITES = { question: 4000, contenu: 230000, historique: 30, message: 20000 };

export function coutUsd(modele, u) {
  const p = PRIX[String(modele || '').replace(/-\d{8}$/, '')] || PRIX_DEFAUT;
  const n = k => (typeof u[k] === 'number' ? u[k] : 0);
  return (n('input_tokens') * p[0] + n('output_tokens') * p[1]
    + n('cache_creation_input_tokens') * p[2] + n('cache_read_input_tokens') * p[3]) / 1e6;
}

const json = (obj, statut, entetes) => new Response(JSON.stringify(obj), {
  status: statut, headers: Object.assign({ 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' }, entetes),
});

function enTetesCors(req, env) {
  const origine = req.headers.get('Origin') || '';
  const autorisees = String(env.ORIGINES || '').split(',').map(s => s.trim()).filter(Boolean);
  const ok = !!origine && autorisees.includes(origine);
  const h = { Vary: 'Origin' };
  if (ok) Object.assign(h, {
    'Access-Control-Allow-Origin': origine,
    'Access-Control-Allow-Headers': 'Authorization, Content-Type',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Max-Age': '86400',
  });
  return { h, interdit: !!origine && !ok };
}

async function compteur(env, cle) { return +((await env.COMPTEURS.get(cle)) || 0); }

/* ---------- /auth : code personnel → jeton ---------- */
async function auth(req, env, cors) {
  if (!env.ASSISTANT_CODE || !env.JETON_CLE) return json({ erreur: 'configuration' }, 503, cors);
  const ip = req.headers.get('CF-Connecting-IP') || 'inconnue';
  const cle = 'auth:' + ip + ':' + Math.floor(Date.now() / 3600000);
  const n = await compteur(env, cle);
  if (n >= 10) return json({ erreur: 'trop_de_tentatives' }, 429, cors);
  let corps;
  try { corps = await req.json(); } catch (e) { return json({ erreur: 'requete' }, 400, cors); }
  const code = corps && typeof corps.code === 'string' ? corps.code.slice(0, 500) : '';
  if (!code || !(await egal(code, env.ASSISTANT_CODE))) {
    await env.COMPTEURS.put(cle, String(n + 1), { expirationTtl: 3700 });
    return json({ erreur: 'code' }, 401, cors);
  }
  const exp = Date.now() + (+env.DUREE_JETON_JOURS || 30) * 86400000;
  return json({ jeton: await signer({ exp, portee: ['chat'] }, env.JETON_CLE), exp }, 200, cors);
}

/* ---------- Validation de la demande ---------- */
export function valider(c) {
  if (!c || typeof c !== 'object') return 'corps';
  if (typeof c.question !== 'string' || !c.question.trim() || c.question.length > LIMITES.question) return 'question';
  if (c.contenu != null && (typeof c.contenu !== 'object' || typeof c.contenu.texte !== 'string' || c.contenu.texte.length > LIMITES.contenu)) return 'contenu';
  const h = c.historique == null ? [] : c.historique;
  if (!Array.isArray(h) || h.length > LIMITES.historique) return 'historique';
  for (let i = 0; i < h.length; i++) {
    const m = h[i];
    if (!m || typeof m.texte !== 'string' || m.texte.length > LIMITES.message) return 'historique';
    if (m.role !== (i % 2 === 0 ? 'user' : 'assistant')) return 'historique';   // alterné, commence par l'élève
  }
  if (h.length % 2) return 'historique';                                        // finit par une réponse
  return null;
}

/* ---------- Requête à l'API Messages ---------- */
export function construireRequete(c, env) {
  const approfondir = !!c.approfondir;
  const modele = approfondir ? (env.MODELE_APPROFONDI || 'claude-opus-5-5') : (env.MODELE || 'claude-sonnet-5-5');
  const system = [{ type: 'text', text: REGLES_ECRIT, cache_control: { type: 'ephemeral' } }];
  if (c.contenu && c.contenu.texte) system.push({ type: 'text', text: blocChapitre(c.chapitre, c.contenu.texte), cache_control: { type: 'ephemeral' } });
  const messages = (c.historique || []).map(m => ({
    role: m.role,
    content: m.role === 'user' ? messageUtilisateur(m.contexte, m.texte) : m.texte,
  }));
  // Dernier message : contexte volatil + question ; point de cache pour le tour suivant
  messages.push({ role: 'user', content: [{ type: 'text', text: messageUtilisateur(c.contexte, c.question), cache_control: { type: 'ephemeral' } }] });
  const p = {
    model: modele, max_tokens: approfondir ? 16000 : 4000, system, messages,
    // Refus d'un classifieur de sécurité : repli côté serveur sur le modèle prévu par l'API
    betas: ['server-side-fallback-2026-07-01'], fallbacks: 'default',
  };
  if (approfondir) p.output_config = { effort: 'medium' };   // Opus 5.5 : réflexion adaptative
  else {
    p.output_config = { effort: 'low' };                       // réponse rapide
    if (/sonnet-5-5/.test(modele)) p.thinking = { type: 'between_tools' };   // pas de temps de réflexion
  }
  return p;
}

function codeErreur(e) {
  if (e instanceof Anthropic.APIUserAbortError || (e && e.name === 'AbortError')) return 'annule';
  if (e instanceof Anthropic.RateLimitError) return 'surcharge';
  if (e instanceof Anthropic.AuthenticationError || e instanceof Anthropic.PermissionDeniedError) return 'configuration';
  if (e instanceof Anthropic.BadRequestError) return 'requete_api';
  if (e instanceof Anthropic.APIConnectionError) return 'reseau';
  if (e instanceof Anthropic.APIError) return 'service';
  return 'interne';
}

/* ---------- /chat : réponse de Claude en flux SSE ---------- */
async function chat(req, env, ctx, cors) {
  if (!env.ANTHROPIC_API_KEY || !env.JETON_CLE) return json({ erreur: 'configuration' }, 503, cors);
  const charge = await verifier((req.headers.get('Authorization') || '').replace(/^Bearer\s+/i, ''), env.JETON_CLE);
  if (!charge || !Array.isArray(charge.portee) || !charge.portee.includes('chat')) return json({ erreur: 'jeton' }, 401, cors);
  const minute = 'debit:' + Math.floor(Date.now() / 60000);
  const n = await compteur(env, minute);
  if (n >= (+env.DEBIT_MINUTE || 20)) return json({ erreur: 'debit' }, 429, cors);
  await env.COMPTEURS.put(minute, String(n + 1), { expirationTtl: 120 });
  const jour = 'depense:' + new Date().toISOString().slice(0, 10);
  const budget = Math.round((+env.BUDGET_JOUR_USD || 1.5) * 1e6);   // micro-dollars
  if ((await compteur(env, jour)) >= budget) return json({ erreur: 'budget' }, 429, cors);
  let corps;
  try { corps = await req.json(); } catch (e) { return json({ erreur: 'requete' }, 400, cors); }
  const pb = valider(corps);
  if (pb) return json({ erreur: 'requete', detail: pb }, 400, cors);

  const params = construireRequete(corps, env);
  const client = new Anthropic({ apiKey: env.ANTHROPIC_API_KEY, maxRetries: 1 });
  const { readable, writable } = new TransformStream();
  const ecrivain = writable.getWriter();
  const enc = new TextEncoder();
  const envoyer = (ev, data) => ecrivain.write(enc.encode('event: ' + ev + '\ndata: ' + JSON.stringify(data) + '\n\n'));
  const tache = (async () => {
    try {
      const flux = client.beta.messages.stream(params, { signal: req.signal });
      for await (const e of flux) {
        if (e.type === 'content_block_delta' && e.delta && e.delta.type === 'text_delta') await envoyer('texte', { t: e.delta.text });
      }
      const fin = await flux.finalMessage();
      const u = fin.usage || {};
      const cout = coutUsd(fin.model || params.model, u);
      await env.COMPTEURS.put(jour, String((await compteur(env, jour)) + Math.round(cout * 1e6)), { expirationTtl: 3 * 86400 });
      await envoyer('fin', {
        arret: fin.stop_reason, modele: fin.model || params.model, cout: Math.round(cout * 1e5) / 1e5,
        usage: { entree: u.input_tokens || 0, sortie: u.output_tokens || 0, cache_ecrit: u.cache_creation_input_tokens || 0, cache_lu: u.cache_read_input_tokens || 0 },
      });
    } catch (e) {
      try { await envoyer('erreur', { code: codeErreur(e) }); } catch (_) { /* client parti */ }
    } finally {
      try { await ecrivain.close(); } catch (_) { /* déjà fermé */ }
    }
  })();
  if (ctx && ctx.waitUntil) ctx.waitUntil(tache);
  return new Response(readable, { headers: Object.assign({}, cors, {
    'Content-Type': 'text/event-stream; charset=utf-8', 'Cache-Control': 'no-store', 'X-Accel-Buffering': 'no',
  }) });
}

export default {
  async fetch(req, env, ctx) {
    const { h: cors, interdit } = enTetesCors(req, env);
    if (interdit) return json({ erreur: 'origine' }, 403, cors);
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    const chemin = new URL(req.url).pathname;
    try {
      if (chemin === '/sante' && req.method === 'GET') return json({ ok: true, service: 'revisions-assistant', version: 1 }, 200, cors);
      if (chemin === '/auth' && req.method === 'POST') return await auth(req, env, cors);
      if (chemin === '/chat' && req.method === 'POST') return await chat(req, env, ctx, cors);
      return json({ erreur: 'introuvable' }, 404, cors);
    } catch (e) {
      return json({ erreur: 'interne' }, 500, cors);
    }
  },
};
