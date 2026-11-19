/* Jetons d'accès de l'assistant : « v1.<charge>.<signature> », charge = JSON { exp, portee }
   en base64url, signature = HMAC-SHA-256 de « v1.<charge> » avec le secret JETON_CLE.
   Changer JETON_CLE (secret du Worker) révoque tous les jetons. */
const enc = new TextEncoder();

function b64url(octets) {
  let s = '';
  const t = new Uint8Array(octets);
  for (let i = 0; i < t.length; i++) s += String.fromCharCode(t[i]);
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}
function deB64url(texte) {
  const s = texte.replace(/-/g, '+').replace(/_/g, '/') + '==='.slice((texte.length + 3) % 4);
  const bin = atob(s);
  const t = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) t[i] = bin.charCodeAt(i);
  return t;
}
function cle(secret, usages) {
  return crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, usages);
}

export async function signer(charge, secret) {
  const corps = 'v1.' + b64url(enc.encode(JSON.stringify(charge)));
  const sig = await crypto.subtle.sign('HMAC', await cle(secret, ['sign']), enc.encode(corps));
  return corps + '.' + b64url(sig);
}

/* Charge du jeton s'il est bien signé et non expiré, sinon null */
export async function verifier(jeton, secret, maintenant = Date.now()) {
  if (typeof jeton !== 'string' || jeton.length > 2000) return null;
  const parts = jeton.split('.');
  if (parts.length !== 3 || parts[0] !== 'v1') return null;
  let ok = false;
  try {
    ok = await crypto.subtle.verify('HMAC', await cle(secret, ['verify']), deB64url(parts[2]), enc.encode(parts[0] + '.' + parts[1]));
  } catch (e) { return null; }
  if (!ok) return null;
  let charge;
  try { charge = JSON.parse(new TextDecoder().decode(deB64url(parts[1]))); } catch (e) { return null; }
  if (!charge || typeof charge.exp !== 'number' || charge.exp <= maintenant) return null;
  return charge;
}

/* Comparaison de deux chaînes en temps constant (empreintes HMAC de même longueur) */
export async function egal(a, b) {
  const k = await crypto.subtle.importKey('raw', crypto.getRandomValues(new Uint8Array(32)), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const [x, y] = await Promise.all([crypto.subtle.sign('HMAC', k, enc.encode(String(a))), crypto.subtle.sign('HMAC', k, enc.encode(String(b)))]);
  const u = new Uint8Array(x), v = new Uint8Array(y);
  let d = 0;
  for (let i = 0; i < u.length; i++) d |= u[i] ^ v[i];
  return d === 0;
}
