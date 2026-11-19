/* Tests du relais (node --test) : l'API Claude est SIMULÉE (fetch remplacé), aucune vraie clé. */
import { test } from 'node:test';
import assert from 'node:assert/strict';
import worker, { coutUsd, valider, construireRequete } from '../src/index.js';
import { signer, verifier } from '../src/jeton.js';
import { REGLES_ECRIT, messageUtilisateur } from '../src/prompts.js';

const SITE = 'https://thomasmareel.github.io';
class KV { constructor() { this.m = new Map(); } async get(k) { return this.m.has(k) ? this.m.get(k) : null; } async put(k, v) { this.m.set(k, String(v)); } }
const nouvelEnv = () => ({
  ORIGINES: SITE + ',http://localhost:8765', MODELE: 'claude-sonnet-5-5', MODELE_APPROFONDI: 'claude-opus-5-5',
  BUDGET_JOUR_USD: '1.50', DUREE_JETON_JOURS: '30', DEBIT_MINUTE: '20',
  ANTHROPIC_API_KEY: 'cle-factice-pour-test', ASSISTANT_CODE: 'mon-code-de-test-42', JETON_CLE: 'cle-de-signature-de-test', COMPTEURS: new KV(),
});
const ctx = () => ({ taches: [], waitUntil(p) { this.taches.push(p); } });
const req = (chemin, o = {}) => new Request('https://relais.test' + chemin, {
  method: o.method || 'GET', headers: Object.assign({ Origin: SITE, 'Content-Type': 'application/json' }, o.headers || {}),
  body: o.body ? JSON.stringify(o.body) : undefined,
});

/* API Claude simulée : flux SSE d'une réponse en trois morceaux */
let derniereRequete = null;
function sse(evts) { return evts.map(e => 'event: ' + e.type + '\ndata: ' + JSON.stringify(e) + '\n\n').join(''); }
function simulerApi(o = {}) {
  globalThis.fetch = async (url, init) => {
    const u = String(url instanceof Request ? url.url : url);
    if (!u.startsWith('https://api.anthropic.com/')) throw new Error('requête inattendue : ' + u);
    const h = new Headers(init && init.headers);
    derniereRequete = { url: u, headers: h, corps: JSON.parse(init.body) };
    if (o.statut) return new Response(JSON.stringify({ type: 'error', error: { type: 'authentication_error', message: 'x' } }), { status: o.statut, headers: { 'content-type': 'application/json' } });
    const morceaux = ['La loi ', 'de Faraday ', '\\(e=-\\dfrac{\\mathrm d\\Phi}{\\mathrm dt}\\).'];
    const corps = sse([
      { type: 'message_start', message: { id: 'msg_test', type: 'message', role: 'assistant', model: 'claude-sonnet-5-5', content: [], stop_reason: null, stop_sequence: null,
        usage: { input_tokens: 120, output_tokens: 1, cache_creation_input_tokens: 9000, cache_read_input_tokens: 0 } } },
      { type: 'content_block_start', index: 0, content_block: { type: 'text', text: '' } },
      ...morceaux.map(t => ({ type: 'content_block_delta', index: 0, delta: { type: 'text_delta', text: t } })),
      { type: 'content_block_stop', index: 0 },
      { type: 'message_delta', delta: { stop_reason: o.arret || 'end_turn', stop_sequence: null }, usage: { output_tokens: 40 } },
      { type: 'message_stop' },
    ]);
    return new Response(corps, { status: 200, headers: { 'content-type': 'text/event-stream', 'request-id': 'req_test' } });
  };
}
const lireSSE = texte => texte.split('\n\n').filter(Boolean).map(b => {
  const ev = /event: (.*)/.exec(b), d = /data: (.*)/.exec(b);
  return { ev: ev && ev[1], data: d ? JSON.parse(d[1]) : null };
});
async function jeton(env) { return (await (await worker.fetch(req('/auth', { method: 'POST', body: { code: env.ASSISTANT_CODE } }), env, ctx())).json()).jeton; }
const demande = (o = {}) => Object.assign({
  chapitre: { id: 'induction', nom: 'Induction', matiere: 'Physique', partie: 'Électromagnétisme', annee: 1 },
  contenu: { empreinte: 'fnv1a:00000000', texte: '# Cours\n§1 · LOI DE FARADAY\n' + 'x'.repeat(5000) },
  contexte: { onglet: 'cours', section: { num: '§1', titre: 'Loi de Faraday' } },
  historique: [], question: 'Que dit la loi de Faraday ?',
}, o);

test('santé, CORS : origine autorisée servie, origine étrangère refusée', async () => {
  const env = nouvelEnv();
  const r = await worker.fetch(req('/sante'), env, ctx());
  assert.equal(r.status, 200);
  assert.equal(r.headers.get('Access-Control-Allow-Origin'), SITE);
  const r2 = await worker.fetch(req('/sante', { headers: { Origin: 'https://exemple.com' } }), env, ctx());
  assert.equal(r2.status, 403);
  const r3 = await worker.fetch(req('/chat', { method: 'OPTIONS' }), env, ctx());
  assert.equal(r3.status, 204);
});

test('auth : mauvais code refusé, bon code → jeton valide 30 jours, 10 essais par heure', async () => {
  const env = nouvelEnv();
  const mauvais = await worker.fetch(req('/auth', { method: 'POST', body: { code: 'faux' } }), env, ctx());
  assert.equal(mauvais.status, 401);
  const bon = await (await worker.fetch(req('/auth', { method: 'POST', body: { code: env.ASSISTANT_CODE } }), env, ctx())).json();
  const charge = await verifier(bon.jeton, env.JETON_CLE);
  assert.ok(charge && charge.portee.includes('chat'));
  assert.ok(Math.abs(charge.exp - Date.now() - 30 * 86400000) < 60000);
  for (let i = 0; i < 9; i++) await worker.fetch(req('/auth', { method: 'POST', body: { code: 'faux' } }), env, ctx());
  const bloque = await worker.fetch(req('/auth', { method: 'POST', body: { code: env.ASSISTANT_CODE } }), env, ctx());
  assert.equal(bloque.status, 429);
});

test('jetons : falsifié, expiré ou signé avec une autre clé → refusé', async () => {
  const j = await signer({ exp: Date.now() + 1000, portee: ['chat'] }, 'k1');
  assert.ok(await verifier(j, 'k1'));
  assert.equal(await verifier(j, 'k2'), null);
  assert.equal(await verifier(j.slice(0, -2) + 'AA', 'k1'), null);
  assert.equal(await verifier(await signer({ exp: Date.now() - 1, portee: ['chat'] }, 'k1'), 'k1'), null);
  assert.equal(await verifier('n.importe.quoi', 'k1'), null);
});

test('chat : sans jeton → 401 ; demande invalide → 400', async () => {
  const env = nouvelEnv();
  simulerApi();
  const r = await worker.fetch(req('/chat', { method: 'POST', body: demande() }), env, ctx());
  assert.equal(r.status, 401);
  const j = await jeton(env);
  const r2 = await worker.fetch(req('/chat', { method: 'POST', headers: { Authorization: 'Bearer ' + j }, body: demande({ historique: [{ role: 'assistant', texte: 'x' }] }) }), env, ctx());
  assert.equal(r2.status, 400);
  assert.equal(valider(demande({ question: '' })), 'question');
  assert.equal(valider(demande({ historique: [{ role: 'user', texte: 'a' }] })), 'historique');
  assert.equal(valider(demande({ historique: [{ role: 'user', texte: 'a' }, { role: 'assistant', texte: 'b' }] })), null);
});

test('chat : flux SSE relayé, coût compté, requête conforme (cache, modèle, repli, réflexion)', async () => {
  const env = nouvelEnv();
  simulerApi();
  const j = await jeton(env);
  const c = ctx();
  const r = await worker.fetch(req('/chat', { method: 'POST', headers: { Authorization: 'Bearer ' + j },
    body: demande({ historique: [{ role: 'user', texte: 'Bonjour', contexte: { onglet: 'cours' } }, { role: 'assistant', texte: 'Salut !' }] }) }), env, c);
  assert.equal(r.status, 200);
  assert.match(r.headers.get('Content-Type'), /text\/event-stream/);
  const evts = lireSSE(await r.text());
  await Promise.all(c.taches);
  const texte = evts.filter(e => e.ev === 'texte').map(e => e.data.t).join('');
  assert.equal(texte, 'La loi de Faraday \\(e=-\\dfrac{\\mathrm d\\Phi}{\\mathrm dt}\\).');
  const fin = evts.find(e => e.ev === 'fin');
  assert.ok(fin, 'événement fin attendu : ' + JSON.stringify(evts.slice(-2)));
  assert.equal(fin.data.arret, 'end_turn');
  const attendu = coutUsd('claude-sonnet-5-5', { input_tokens: 120, output_tokens: 40, cache_creation_input_tokens: 9000, cache_read_input_tokens: 0 });
  assert.ok(Math.abs(fin.data.cout - attendu) < 1e-4);
  const jour = 'depense:' + new Date().toISOString().slice(0, 10);
  assert.equal(+(await env.COMPTEURS.get(jour)), Math.round(attendu * 1e6));
  // requête envoyée à l'API
  const q = derniereRequete;
  // clé transmise par en-tête seulement (x-api-key, ou Authorization: Bearer selon la version du SDK)
  assert.ok(q.headers.get('x-api-key') === env.ANTHROPIC_API_KEY || q.headers.get('authorization') === 'Bearer ' + env.ANTHROPIC_API_KEY);
  assert.match(q.headers.get('anthropic-beta') || '', /server-side-fallback-2026-07-01/);
  assert.equal(q.corps.model, 'claude-sonnet-5-5');
  assert.equal(q.corps.fallbacks, 'default');
  assert.deepEqual(q.corps.thinking, { type: 'between_tools' });
  assert.deepEqual(q.corps.output_config, { effort: 'low' });
  assert.equal(q.corps.stream, true);
  assert.equal(q.corps.system[0].text, REGLES_ECRIT);
  assert.ok(q.corps.system.every(b => b.cache_control && b.cache_control.type === 'ephemeral'));
  assert.match(q.corps.system[1].text, /<chapitre>\n# Cours/);
  assert.equal(q.corps.messages.length, 3);
  assert.equal(q.corps.messages[0].content, messageUtilisateur({ onglet: 'cours' }, 'Bonjour'));
  const dernier = q.corps.messages[2].content[0];
  assert.ok(dernier.cache_control);
  assert.match(dernier.text, /<contexte>\nOnglet : Cours ; section : §1 « Loi de Faraday »\n<\/contexte>\n\nQue dit la loi de Faraday \?/);
  assert.ok(!JSON.stringify(q.corps).includes(env.ANTHROPIC_API_KEY), 'la clé ne doit jamais être dans le corps');
});

test('approfondir : Opus 5.5, effort moyen, réflexion adaptative (sans paramètre thinking)', () => {
  const p = construireRequete(demande({ approfondir: true }), nouvelEnv());
  assert.equal(p.model, 'claude-opus-5-5');
  assert.deepEqual(p.output_config, { effort: 'medium' });
  assert.equal(p.thinking, undefined);
  assert.equal(p.max_tokens, 16000);
});

test('budget du jour atteint → 429 ; débit par minute plafonné', async () => {
  const env = nouvelEnv();
  simulerApi();
  const j = await jeton(env);
  await env.COMPTEURS.put('depense:' + new Date().toISOString().slice(0, 10), String(1.5e6));
  const r = await worker.fetch(req('/chat', { method: 'POST', headers: { Authorization: 'Bearer ' + j }, body: demande() }), env, ctx());
  assert.equal(r.status, 429);
  assert.equal((await r.json()).erreur, 'budget');
  const env2 = nouvelEnv(); env2.DEBIT_MINUTE = '1';
  const j2 = await jeton(env2);
  const c = ctx();
  const ok = await worker.fetch(req('/chat', { method: 'POST', headers: { Authorization: 'Bearer ' + j2 }, body: demande() }), env2, c);
  await ok.text(); await Promise.all(c.taches);
  const trop = await worker.fetch(req('/chat', { method: 'POST', headers: { Authorization: 'Bearer ' + j2 }, body: demande() }), env2, ctx());
  assert.equal(trop.status, 429);
});

test('erreur de l\'API (clé refusée) → événement erreur « configuration », sans détail interne', async () => {
  const env = nouvelEnv();
  simulerApi({ statut: 401 });
  const j = await jeton(env);
  const c = ctx();
  const r = await worker.fetch(req('/chat', { method: 'POST', headers: { Authorization: 'Bearer ' + j }, body: demande() }), env, c);
  const evts = lireSSE(await r.text());
  await Promise.all(c.taches);
  assert.deepEqual(evts.map(e => e.ev), ['erreur']);
  assert.equal(evts[0].data.code, 'configuration');
});

test('relais mal configuré (secret manquant) → 503', async () => {
  const env = nouvelEnv(); delete env.ANTHROPIC_API_KEY;
  const r = await worker.fetch(req('/chat', { method: 'POST', body: demande() }), env, ctx());
  assert.equal(r.status, 503);
});
