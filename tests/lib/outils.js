'use strict';
/* ============================================================
   Outils partagés par les suites de tests
   ============================================================
   Rappels sur le site (voir CLAUDE.md) :
   - CHAPTERS, CHAPTERS_BY_ID, Store, navigateTo, getCanvasColors, flashPretty…
     sont des globales « lexicales » : dans page.evaluate on écrit CHAPTERS.length,
     PAS window.CHAPTERS.
   - applyTheme n'est pas accessible : pour changer de thème, cliquer #theme-btn.
   - Au 1er chargement, le service worker recharge la page : les suites
     travaillent donc dans des contextes où les service workers sont BLOQUÉS
     (sauf la suite pwa). */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const pause = ms => new Promise(r => setTimeout(r, ms));

/* Messages de console à ignorer (bruit propre à l'outil de test, pas au site) */
const CONSOLE_IGNOREE = [
  /Service Worker registration blocked by Playwright/i,
  /willReadFrequently/i,   // provoqué par nos propres lectures de pixels (getImageData)
];

/* Branche des écouteurs sur une page et renvoie un « journal » :
   erreurs (console.error / console.warning / exceptions), requêtes externes,
   requêtes échouées et réponses HTTP ≥ 400. `journal.lieu` indique l'étape en
   cours (utile pour savoir OÙ une erreur est apparue). */
function suivreErreurs(page, base) {
  const origine = new URL(base).origin;
  const j = { lieu: 'chargement', erreurs: [], externes: [], echecs: [], http: [], dialogues: [], dialogue: null };
  page.on('console', m => {
    const t = m.type();
    if (t !== 'error' && t !== 'warning') return;
    const texte = m.text();
    if (CONSOLE_IGNOREE.some(re => re.test(texte))) return;
    const loc = m.location() || {};
    j.erreurs.push({ lieu: j.lieu, type: 'console.' + t, texte: texte.slice(0, 400),
      source: (loc.url || '').replace(origine, '') + (loc.lineNumber != null ? ':' + loc.lineNumber : '') });
  });
  page.on('pageerror', e => {
    j.erreurs.push({ lieu: j.lieu, type: 'exception', texte: String(e.message).slice(0, 400),
      source: String(e.stack || '').split('\n').slice(1, 3).join(' / ').replace(new RegExp(origine, 'g'), '').slice(0, 300) });
  });
  page.on('request', r => {
    const u = r.url();
    if (!u.startsWith(origine) && !/^(data|blob|about|chrome-extension|chrome):/.test(u)) j.externes.push({ lieu: j.lieu, url: u });
  });
  page.on('requestfailed', r => {
    const err = (r.failure() && r.failure().errorText) || '';
    if (/ERR_ABORTED/.test(err)) return;   // navigation interrompue : normal pendant un rechargement
    if (!r.url().startsWith(origine)) return;   // requête externe (bloquée) : déjà signalée ci-dessus
    j.echecs.push({ lieu: j.lieu, url: r.url().replace(origine, ''), erreur: err });
  });
  page.on('response', r => {
    if (r.status() >= 400) j.http.push({ lieu: j.lieu, url: r.url().replace(origine, ''), statut: r.status() });
  });
  // Boîtes de dialogue (alert/confirm) : refusées et notées, sauf si une suite
  // a prévu une réponse via journal.dialogue = d => d.accept()
  page.on('dialog', d => {
    if (j.dialogue) { const f = j.dialogue; j.dialogue = null; f(d); return; }
    j.dialogues.push({ lieu: j.lieu, type: d.type(), message: d.message().slice(0, 200) });
    d.dismiss().catch(() => {});
  });
  return j;
}

/* Résume les problèmes d'un journal (depuis l'indice `depuis` de chaque liste) */
function problemesJournal(j, depuis) {
  const d = depuis || { erreurs: 0, externes: 0, echecs: 0, http: 0 };
  const out = [];
  j.erreurs.slice(d.erreurs).forEach(e => out.push('[' + e.lieu + '] ' + e.type + ' : ' + e.texte + (e.source ? ' (' + e.source + ')' : '')));
  j.externes.slice(d.externes).forEach(e => out.push('[' + e.lieu + '] requête EXTERNE : ' + e.url));
  j.echecs.slice(d.echecs).forEach(e => out.push('[' + e.lieu + '] requête échouée : ' + e.url + ' (' + e.erreur + ')'));
  j.http.slice(d.http).forEach(e => out.push('[' + e.lieu + '] HTTP ' + e.statut + ' : ' + e.url));
  return out;
}
function marqueJournal(j) {
  return { erreurs: j.erreurs.length, externes: j.externes.length, echecs: j.echecs.length, http: j.http.length };
}

/* Attend que le site soit initialisé : grand script exécuté (CHAPTERS, decks),
   MathJax prêt, puis laisse passer la restauration de position (+120 ms,
   puis navigateTo +80 ms). */
async function attendreApp(page, delai) {
  const max = delai || 60000, t0 = Date.now();
  let etat = null, planteDepuis = 0;
  while (Date.now() - t0 < max) {
    etat = await page.evaluate(() => ({
      chapters: typeof CHAPTERS !== 'undefined',
      decks: !!window.FLASH_INSTANCES,
      charge: document.readyState === 'complete',
      mathjax: !!(window.MathJax && MathJax.startup && MathJax.startup.document && typeof MathJax.typesetPromise === 'function'),
    })).catch(() => null);   // contexte détruit pendant une navigation : on réessaie
    if (etat && etat.chapters && etat.decks && etat.charge && etat.mathjax) { await pause(500); return; }
    // Page chargée mais CHAPTERS absent depuis 3 s : le grand script a planté, inutile d'attendre
    if (etat && etat.charge && !etat.chapters) { planteDepuis = planteDepuis || Date.now(); if (Date.now() - planteDepuis > 3000) break; }
    await pause(200);
  }
  const manque = !etat ? ['page inaccessible'] : [
    !etat.chapters && 'CHAPTERS non défini (le grand script a planté ?)',
    !etat.decks && 'aucune flashcard initialisée (makeFlash jamais appelé ?)',
    !etat.charge && 'page pas entièrement chargée',
    !etat.mathjax && 'MathJax pas prêt',
  ].filter(Boolean);
  throw new Error("le site ne s'est pas initialisé (" + Math.round((Date.now() - t0) / 1000) + ' s) : ' + manque.join(' ; '));
}

/* Ferme les fenêtres superposées (Aujourd'hui, Bilan…) ouvertes au lancement */
async function fermerOverlays(page) {
  await page.evaluate(() => {
    document.querySelectorAll('.dash-overlay.open').forEach(o => o.classList.remove('open'));
    const q = document.getElementById('quiz-overlay');
    if (q && q.classList.contains('open') && window.quizClose) window.quizClose();
  });
}

/* Navigue vers un chapitre (et un onglet : 'cours', 'flash'…) via navigateTo,
   exactement comme le fait le site, puis attend la fin de la navigation. */
async function naviguer(page, id, onglet) {
  const ok = await page.evaluate(([id, onglet]) => new Promise(resolve => {
    const c = CHAPTERS_BY_ID[id];
    if (!c || !document.querySelector('.chap-btn[data-chap="' + id + '"]')) { resolve(false); return; }
    const t = setTimeout(() => resolve(true), 1500);   // garde-fou si le rappel n'arrive jamais
    navigateTo('chap-' + id, onglet ? c.prefix + '-' + onglet : null, () => { clearTimeout(t); resolve(true); });
  }), [id, onglet || null]);
  if (!ok) throw new Error('chapitre introuvable pour la navigation : ' + id);
  await pause(120);
}

/* Code exécuté DANS la page : délimiteurs TeX restés en clair et erreurs
   MathJax (mjx-merror) d'un élément. Attend jusqu'à `attenteMs` que le rendu
   paresseux (typesetPanel) ait fait son travail. */
async function etatMathJax(page, idElement, attenteMs) {
  return page.evaluate(async ([id, attente]) => {
    const el = document.getElementById(id);
    if (!el) return null;
    const EXCLUS = 'script,style,code,pre,textarea,mjx-container,.no-mathjax,.tex2jax_ignore';
    const DELIM = /\\\(|\\\)|\\\[|\\\]|\$\$/;
    const restes = () => {
      const out = [];
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = w.nextNode())) {
        const p = n.parentElement;
        if (!p || p.closest(EXCLUS)) continue;
        if (DELIM.test(n.nodeValue)) out.push(n.nodeValue.trim().slice(0, 120));
      }
      return out;
    };
    const t0 = Date.now();
    let r = restes();
    while (r.length && Date.now() - t0 < attente) { await new Promise(x => setTimeout(x, 100)); r = restes(); }
    const merror = Array.from(el.querySelectorAll('mjx-merror'))
      .map(m => (m.getAttribute('data-mjx-error') || m.textContent || '').slice(0, 120));
    return { restes: r, merror, mjx: el.querySelectorAll('mjx-container').length, texte: el.textContent.trim().length };
  }, [idElement, attenteMs == null ? 2500 : attenteMs]);
}

/* ---------- Decks de flashcards dans le HTML (côté node) ----------
   Repère `const <nom> = [ … ];` et renvoie { debut, fin, cartes } où debut/fin
   délimitent le littéral de tableau (crochets inclus). Les chaînes sont
   parcourues correctement (un « ] » dans une question ne gêne pas). */
function extraireDeck(html, nomConst) {
  const re = new RegExp('const\\s+' + nomConst + '\\s*=\\s*\\[');
  const m = re.exec(html);
  if (!m) throw new Error('deck introuvable dans index.html : const ' + nomConst);
  const debut = m.index + m[0].length - 1;
  let prof = 0, i = debut, chaine = null;
  for (; i < html.length; i++) {
    const c = html[i];
    if (chaine) {
      if (c === '\\') { i++; continue; }
      if (c === chaine) chaine = null;
      continue;
    }
    if (c === '"' || c === "'" || c === '`') { chaine = c; continue; }
    if (c === '/' && html[i + 1] === '/') { i = html.indexOf('\n', i); if (i < 0) break; continue; }
    if (c === '/' && html[i + 1] === '*') { i = html.indexOf('*/', i + 2) + 1; if (i <= 0) break; continue; }
    if (c === '[') prof++;
    else if (c === ']') { prof--; if (prof === 0) break; }
  }
  if (prof !== 0) throw new Error('fin du deck ' + nomConst + ' introuvable');
  const fin = i + 1;
  const cartes = vm.runInNewContext('(' + html.slice(debut, fin) + ')', {}, { timeout: 2000 });
  if (!Array.isArray(cartes)) throw new Error('le deck ' + nomConst + " n'est pas un tableau");
  return { debut, fin, cartes };
}
/* Remplace le contenu d'un deck par `cartes` (sérialisées en JSON, valide en JS) */
function remplacerDeck(html, nomConst, cartes) {
  const d = extraireDeck(html, nomConst);
  return html.slice(0, d.debut) + JSON.stringify(cartes) + html.slice(d.fin);
}

/* ---------- Service worker (côté node) ----------
   Lit CACHE_VERSION et la liste PRECACHE de sw.js. */
function lireServiceWorker(racine) {
  const src = fs.readFileSync(path.join(racine, 'sw.js'), 'utf8');
  const v = /CACHE_VERSION\s*=\s*['"]([^'"]+)['"]/.exec(src);
  const p = /PRECACHE\s*=\s*(\[[\s\S]*?\])\s*;/.exec(src);
  let precache = null;
  if (p) { try { precache = vm.runInNewContext('(' + p[1] + ')', {}, { timeout: 1000 }); } catch (e) { precache = null; } }
  return { version: v ? v[1] : null, precache };
}

/* Liste récursive des fichiers d'un dossier (chemins relatifs, séparateur « / ») */
function listerFichiers(racine, sousDossier) {
  const out = [];
  const base = path.join(racine, sousDossier);
  if (!fs.existsSync(base)) return out;
  (function parcourir(dossier) {
    for (const e of fs.readdirSync(dossier, { withFileTypes: true })) {
      const p = path.join(dossier, e.name);
      if (e.isDirectory()) parcourir(p);
      else out.push(path.relative(racine, p).split(path.sep).join('/'));
    }
  })(base);
  return out;
}

module.exports = {
  pause, suivreErreurs, problemesJournal, marqueJournal, attendreApp, fermerOverlays,
  naviguer, etatMathJax, extraireDeck, remplacerDeck, lireServiceWorker, listerFichiers,
};
