/* Extraction des données dérivées d'un chapitre (docs/chargement-chapitres.md, §4).

   Fonction exécutée DANS le navigateur (tools/chapitres.js la passe à Chromium, la suite de tests
   `site` la rejoue sur les chapitres affichés pour vérifier que les données générées sont à jour).
   Elle reprend à l'identique l'ancienne construction de l'index de la recherche (`buildIndex` du
   module RECHERCHE GLOBALE d'index.html, avant le 2026-11-27) pour les sections, définitions et
   propriétés, méthodes, formules et exercices.

   Entrée : panneaux = [{ id: 'rlc-cours', racine }] dans l'ordre du chapitre (racine : contenu
   d'un <template> ou panneau déplié, jamais rendu par MathJax).
   Sortie : [{ k nature, t titre, p panneau, o provenance, x texte, n nom de formule?, r rang }],
     r = rang de l'élément visé parmi ceux du même sélecteur dans son panneau (CIBLES ci-dessous, les
     mêmes que dans le module RECHERCHE GLOBALE) : le site le retrouve une fois le chapitre chargé. */
function extraireChapitre(panneaux) {
  const CIBLES = { sec: '.course-section', boite: '.def-box, .prop-box', meth: '.method-box', form: '.formula', exo: '.exo' };
  const ongletDe = pid => /-meth$/.test(pid) ? 'Méthodes' : /-exos$/.test(pid) ? 'Exercices' : /-flash$/.test(pid) ? 'Cartes' : 'Cours';
  // « §3 » d'une section (le .sec-num peut être découpé en spans : son texte reste « §3 · TITRE »)
  function paragraphe(el, pid) {
    const sec = el && el.closest ? el.closest('.course-section') : null;
    const sn = sec ? sec.querySelector('.sec-num') : null;
    const t = sn ? sn.textContent.replace(/\s+/g, ' ').trim().split(/\s*·\s*/)[0] : '';
    return /^§/.test(t) ? t : ongletDe(pid);
  }
  // Texte d'un bloc (contenu source : aucune formule rendue) ; sansEntete : après le titre h2
  function texte(el, sansEntete) {
    const tc = el.textContent;
    if (!sansEntete) return tc;
    const h = el.querySelector('h2'), k = h ? tc.indexOf(h.textContent) : -1;
    return k >= 0 ? tc.slice(k + h.textContent.length) : tc;
  }
  /* Titre d'une boîte sans gras d'ouverture : son début, formules en TeX (formule en bloc ramenée
     en ligne), coupé entre deux mots et JAMAIS dans une formule. Une formule compte pour la moitié
     de son TeX. */
  function titreBoite(b) {
    const s = texte(b).replace(/\$\$([\s\S]*?)\$\$/g, ' \\($1\\) ').replace(/\\\[([\s\S]*?)\\\]/g, ' \\($1\\) ').replace(/\s+/g, ' ').trim();
    const parts = s.split(/(\\\([\s\S]*?\\\))/);
    const fin = t => t.replace(/[\s,;:.(—–-]+$/, '') + ' …';
    let out = '', vu = 0;
    for (let k = 0; k < parts.length; k++) {
      const p = parts[k];
      if (k % 2) {
        if (/\\begin|\\\\/.test(p)) { if (vu >= 30) return fin(out); out += ' … '; vu += 2; continue; }
        const l = Math.ceil(p.length / 2);
        if (vu + l > 100 && vu >= 30) return fin(out);
        out += p; vu += l;
      } else if (vu + p.length > 90) {
        let c = p.slice(0, Math.max(0, 90 - vu));
        const e = c.lastIndexOf(' ');
        if (e > 0 || out) c = c.slice(0, Math.max(0, e));
        return fin(out + c);
      } else { out += p; vu += p.length; }
    }
    return out;
  }
  const entrees = [];
  let rangs = null;
  const rang = (kind, el) => rangs[kind].indexOf(el);
  const add = (kind, title, el, extra) => {
    title = String(title || '').replace(/\s+/g, ' ').trim();
    if (title) entrees.push(Object.assign({ k: kind, t: title }, extra, { r: rang(kind, el) }));
  };
  for (const { id: pid, racine } of panneaux) {
    rangs = {};
    for (const k in CIBLES) rangs[k] = Array.from(racine.querySelectorAll(CIBLES[k]));
    if (/-(cours|meth)$/.test(pid)) {
      racine.querySelectorAll('.course-section').forEach(sec => {
        const h2 = sec.querySelector('h2');
        if (h2) add('sec', h2.textContent, sec, { p: pid, o: paragraphe(sec, pid), x: texte(sec, true).slice(0, 900) });
      });
      racine.querySelectorAll('.def-box, .prop-box').forEach(b => {
        const fort = b.querySelector(':scope > strong:first-child, :scope > p:first-child > strong:first-child');
        const t = (fort ? fort.textContent : titreBoite(b)).replace(/^(DÉFINITION|PROPRIÉTÉ)\s*/i, '');
        if (t.trim().length < 4) return;
        add('boite', t, b, { p: pid, o: paragraphe(b, pid), x: texte(b).slice(0, 600) });
      });
      racine.querySelectorAll('.method-box > strong:first-child').forEach(st => {
        add('meth', st.textContent, st.parentElement, { p: pid, o: ongletDe(pid), x: texte(st.parentElement).slice(0, 600) });
      });
      racine.querySelectorAll('.formula').forEach(fo => {
        const src = fo.textContent.replace(/\s+/g, ' ').trim();
        if (src.length < 4) return;
        const sec = fo.closest('.course-section'), h2 = sec ? sec.querySelector('h2') : null;
        const nom = fo.getAttribute('data-nom') || '';
        const extra = { p: pid, o: paragraphe(fo, pid), x: src };
        if (nom) extra.n = nom;
        add('form', nom || (h2 ? h2.textContent : 'Formule'), fo, extra);
      });
    } else if (/-exos$/.test(pid)) {
      racine.querySelectorAll('.exo').forEach(exo => {
        const h3 = exo.querySelector('h3'), num = exo.querySelector('.num');
        if (!h3) return;
        const n = num ? num.textContent.replace(/\s+/g, ' ').trim() : '';
        // texte INTÉGRAL : un mot-clé de la partie C d'un long exercice reste trouvable
        add('exo', h3.textContent, exo, { p: pid, o: n ? n.charAt(0) + n.slice(1).toLowerCase() : 'Exercices', x: texte(exo) });
      });
    }
  }
  return entrees;
}

if (typeof module !== 'undefined') module.exports = { extraireChapitre };
