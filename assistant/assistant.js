/* ===== ASSISTANT IA — module chargé à la demande (docs/assistant-ia.md) =====
   Chargé par l'amorce d'index.html au premier usage (bouton, touche « a », bulle de
   sélection). Phase 0 : collecte du contexte et panneau ; la discussion arrive en phase 1
   (relais authentifié). AUCUNE CLÉ ICI, JAMAIS : ce fichier est public.

   API :
   - window.__contexteAssistant({ contenu:true|false, selection }) → objet au schéma 1
     (voir docs/assistant-ia.md › « Collecte du contexte ») ;
   - window.__assistant.ouvrir({ selection, opener, source }) / fermer() / estOuvert() ;
   - window.__assistant.fiche(demande) → texte de la « fiche de demande » (étape 3a).

   Contrat de compatibilité (CLAUDE.md › Assistant IA) : ce module ne lit que des
   conventions stables du site (CHAPTERS, #chap-<id>, <prefix>-<onglet>, .sec-num « §n · »,
   .exo, .method-box, .flash-side, .sim-wrapper, __VIDEOS + timeline.json). */
(function(){
  'use strict';
  if(window.__assistant) return;

  const SCHEMA = 1;
  const ONGLETS = { cours:'Cours', video:'Vidéos', meth:'Méthodes', simu:'Simulateur', flash:'Cartes', exos:'Exercices' };
  const MATIERES = { physique:'Physique', maths:'Maths', si:'SI', info:'Info', anglais:'Anglais' };
  const $ = id => document.getElementById(id);
  const chapitres = () => (typeof CHAPTERS_BY_ID !== 'undefined' ? CHAPTERS_BY_ID : {});
  const estTelephone = () => !!(window.matchMedia && window.matchMedia('(max-width:767px)').matches);
  const mmss = t => { t = Math.max(0, Math.floor(t || 0)); return Math.floor(t / 60) + ':' + String(t % 60).padStart(2, '0'); };
  const nb = n => (window.__nb ? window.__nb(n, 0) : String(n));
  const coupe = (t, n) => (t.length > n ? t.slice(0, n - 1).replace(/\s+\S*$/, '') + '…' : t);

  /* ─────────────── 1. Lecture de la page ─────────────── */

  function chapitreVisible(){
    if(window.__sommaireOuvert && window.__sommaireOuvert()) return null;
    const els = document.querySelectorAll('.chapter.active');
    for(const el of els) if(el.offsetParent !== null) return el;
    return null;
  }
  function panneauActif(chap){ return chap ? chap.querySelector(':scope > .panel.active') || chap.querySelector('.panel.active') : null; }
  /* Boîte d'un repère : les surtitres .sec-num sont en display:contents (marge du cours) et
     n'ont pas de boîte propre ; on prend alors leur premier enfant mesurable, à défaut leur section. */
  function rectDe(el){
    const r = el.getBoundingClientRect();
    if(r.width || r.height) return r;
    for(const ch of el.children){ const q = ch.getBoundingClientRect(); if(q.width || q.height) return q; }
    const sec = el.closest('.course-section');
    return sec ? sec.getBoundingClientRect() : r;
  }
  function visible(el){ const r = rectDe(el); return r.width > 0 || r.height > 0; }

  // Ligne de lecture : sous l'en-tête (ou la barre du téléphone) et les onglets collés, un peu plus bas
  function ligneLecture(chap){
    let y = 0;
    for(const id of ['site-header', 'mob-header']){
      const h = $(id);
      if(h && h.offsetParent !== null){ const r = h.getBoundingClientRect(); if(r.bottom > 0) y = Math.max(y, r.bottom); }
    }
    const t = chap && chap.querySelector('nav.tabs');
    if(t){ const r = t.getBoundingClientRect(); if(r.top <= y + 4) y = Math.max(y, r.bottom); }
    return y + Math.min(160, (window.innerHeight || 800) * 0.22);
  }
  // Dernier élément dont le haut a passé la ligne ; à défaut le premier visible
  function courant(els, y){
    let c = null, premier = null;
    for(const el of els){
      if(!visible(el)) continue;
      if(!premier) premier = el;
      if(rectDe(el).top <= y) c = el; else break;
    }
    return c || premier;
  }

  /* TeX des formules déjà composées : MathJax garde, pour chaque formule, son conteneur et
     son TeX d'origine (même lecture que la recherche). */
  function carteTeX(){
    const m = new Map();
    try { for(const it of MathJax.startup.document.math){ if(it && it.typesetRoot) m.set(it.typesetRoot, { tex:it.math, display:!!it.display }); } } catch(e){}
    return m;
  }

  /* Texte d'un morceau de page, formules en TeX (\( … \) en ligne, $$ … $$ en bloc),
     blocs séparés par des retours à la ligne, solutions marquées. Lecture seule. */
  const BLOCS = new Set(['P','DIV','SECTION','ARTICLE','H1','H2','H3','H4','H5','H6','UL','OL','TABLE','TR','THEAD','TBODY',
    'BLOCKQUOTE','PRE','FIGURE','FIGCAPTION','DETAILS','SUMMARY','HR','DL','DT','DD','HEADER','FOOTER','ASIDE','NAV','FORM']);
  const IGNORER = 'svg, script, style, template, canvas, input, select, textarea, button.toggle-sol, .exo-tools, .kbd-hint, '
    + '.vid-cadre, .sim-controls, .flash-controls, .review-nav, .fc-reveal, mjx-assistive-mml, [data-assistant-ignorer]';
  function serialiser(racine, texDe){
    const out = [];
    (function marcher(n){
      if(n.nodeType === 3){ out.push(n.nodeValue); return; }
      if(n.nodeType !== 1 && n.nodeType !== 11) return;
      if(n.nodeType === 1){
        const tag = n.tagName;
        if(tag === 'MJX-CONTAINER'){
          const m = texDe(n);
          if(m) out.push(m.display ? '\n$$' + m.tex + '$$\n' : '\\(' + m.tex + '\\)');
          return;
        }
        if(n.matches(IGNORER)) return;
        if(tag === 'BR'){ out.push('\n'); return; }
        if(tag === 'SUB' || tag === 'SUP'){
          const t = n.textContent || '';
          out.push((tag === 'SUB' ? '_' : '^') + (t.length > 1 ? '{' + t + '}' : t));
          return;
        }
        const bloc = BLOCS.has(tag) || tag === 'LI';
        if(tag === 'LI') out.push('\n- ');
        else if(bloc) out.push('\n');
        if(tag === 'TD' || tag === 'TH') out.push(' | ');
        if(n.classList.contains('solution')) out.push('[Solution' + (n.classList.contains('shown') ? '' : ' (non ouverte par l’élève)') + ']\n');
        for(const c of n.childNodes) marcher(c);
        if(bloc) out.push('\n');
        return;
      }
      for(const c of n.childNodes) marcher(c);
    })(racine);
    return out.join('')
      .replace(/[ \t   ]+/g, ' ')
      .split('\n').map(l => l.trim()).join('\n')
      .replace(/\n{3,}/g, '\n\n').trim();
  }
  const texDeCarte = carte => n => carte.get(n) || null;

  // Texte d'une sélection (Range), formules comprises
  function texteSelection(range){
    if(!range) return '';
    const anc = range.commonAncestorContainer;
    const ancEl = anc.nodeType === 1 ? anc : anc.parentElement;
    const carte = carteTeX();
    const dansFormule = ancEl && ancEl.closest ? ancEl.closest('mjx-container') : null;
    if(dansFormule){
      const m = carte.get(dansFormule);
      return m ? (m.display ? '$$' + m.tex + '$$' : '\\(' + m.tex + '\\)') : '';
    }
    // conteneurs touchés par la sélection, dans l'ordre du document ↔ ceux du fragment cloné
    const originaux = ancEl ? Array.from(ancEl.querySelectorAll('mjx-container')).filter(c => range.intersectsNode(c)) : [];
    const frag = range.cloneContents();
    const clones = Array.from(frag.querySelectorAll('mjx-container'));
    const parClone = new Map();
    if(clones.length === originaux.length) clones.forEach((c, i) => { const m = carte.get(originaux[i]); if(m) parClone.set(c, m); });
    return serialiser(frag, n => parClone.get(n) || null);
  }

  function infoSection(el){
    if(!el) return null;
    const brut = (el.textContent || '').replace(/\s+/g, ' ').trim();
    const m = brut.match(/^(§\s*\d+[a-z]?)\s*·\s*(.*)$/i);
    const sec = el.closest('.course-section');
    let titre = m ? m[2] : brut;
    try { if(window.__casPhrase) titre = window.__casPhrase(titre, sec) || titre; } catch(e){}
    return { num: m ? m[1].replace(/\s+/g, '') : null, titre, id: (sec && sec.id) || el.id || null };
  }

  function infoExercice(exo, carte){
    if(!exo) return null;
    const num = exo.querySelector(':scope > .num');
    const h = exo.querySelector(':scope > h3');
    const diff = exo.querySelector(':scope > .diff');
    let niveau = diff ? +diff.getAttribute('data-niveau') || null : null;
    if(!niveau && diff) niveau = ((diff.textContent || '').match(/★/g) || []).length || null;
    const sol = exo.querySelector(':scope > .solution');
    const st = exo.querySelector(':scope > .statement');
    return {
      num: num ? num.textContent.replace(/\s+/g, ' ').trim() : null,
      titre: h ? serialiser(h, texDeCarte(carte)) : null,
      niveau, concours: exo.classList.contains('concours'),
      solutionOuverte: !!(sol && sol.classList.contains('shown')),
      enonce: st ? coupe(serialiser(st, texDeCarte(carte)), 1500) : null,
    };
  }

  function infoCarte(panneau, prefix, carte){
    const face = panneau.querySelector('.flash-side');
    if(!face) return null;
    const q = face.querySelector('.fc-q'), a = face.querySelector('.fc-a');
    const pos = panneau.querySelector('.fp-n');
    const mm = pos ? (pos.textContent || '').match(/(\d+)\s*\/\s*(\d+)/) : null;
    return {
      deck: prefix, rang: mm ? +mm[1] : null, total: mm ? +mm[2] : null,
      face: face.classList.contains('verso') ? 'verso' : 'recto',
      question: q ? serialiser(q, texDeCarte(carte)) : null,
      reponse: a ? serialiser(a, texDeCarte(carte)) : null,
    };
  }

  function infoSimulateur(panneau){
    const w = panneau.querySelector('.sim-wrapper');
    if(!w) return null;
    const txt = el => (el && el.textContent || '').replace(/\s+/g, ' ').trim();
    const mode = w.querySelector('.mode-switch button.active, .mode-switch [aria-pressed="true"]');
    const reglages = {}, mesures = {};
    w.querySelectorAll('.sim-controls .control').forEach(c => {
      if(!visible(c)) return;
      const l = c.querySelector('label'), v = c.querySelector('.value'), chk = c.querySelector('input[type="checkbox"]');
      const k = txt(l); if(!k) return;
      reglages[k] = chk ? (chk.checked ? 'oui' : 'non') : txt(v);
    });
    w.querySelectorAll('.sim-info > div').forEach(d => {
      const l = d.querySelector('.lbl'); const k = txt(l);
      const v = txt(d).replace(k, '').trim();
      if(k && v && v !== '—') mesures[k] = v;
    });
    return { titre: txt(w.querySelector('h2')), mode: mode ? txt(mode) : null, reglages, mesures };
  }

  /* Vidéo lancée : instant de lecture (module Vidéos) → partie, scène, phrase (timeline.json) */
  const timelines = new Map();   // src → objet | 'chargement' | 'absent'
  function chargerTimeline(src){
    if(timelines.has(src)) return;
    timelines.set(src, 'chargement');
    fetch(src + '/timeline.json').then(r => r.ok ? r.json() : Promise.reject())
      .then(j => { timelines.set(src, j); }).catch(() => { timelines.set(src, 'absent'); });
  }
  function infoVideo(chapId){
    const v = window.__instantVideo ? window.__instantVideo() : null;
    if(!v || (chapId && v.chap && v.chap !== chapId)) return null;
    const res = { yt:v.yt, titre:v.titre, t:v.t, temps:mmss(v.t), estime:!!v.estime, src:v.src || null };
    const p = (v.parties || []).filter(x => x[0] <= v.t + 0.5).pop();
    if(p) res.partie = p[1];
    if(v.src){
      const tl = timelines.get(v.src);
      if(!tl) chargerTimeline(v.src);
      else if(typeof tl === 'object'){
        for(const id of tl.ordre || Object.keys(tl.scenes || {})){
          const sc = tl.scenes[id];
          if(!sc || v.t < sc.t0 || v.t >= sc.t0 + sc.duree) continue;
          res.scene = { id, titre: sc.titre || null };
          const rel = v.t - sc.t0;
          const ph = (sc.phrases || []).filter(x => x.debut <= rel + 0.3).pop();
          if(ph) res.phrase = { id: ph.id, ecrit: ph.ecrit || ph.dit || '' };
          break;
        }
      }
    }
    return res;
  }

  /* Contenu du chapitre : texte canonique (Cours, Méthodes, Exercices, Cartes), calculé une
     fois par chapitre et par session de l'assistant (réutilisé octet pour octet : condition
     du cache de prompt en phase 1). */
  const contenus = new Map();
  function fnv(t){ let h = 0x811c9dc5; for(let i = 0; i < t.length; i++){ h ^= t.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; } return ('0000000' + h.toString(16)).slice(-8); }
  function contenuChapitre(c){
    if(contenus.has(c.id)) return contenus.get(c.id);
    // Panneaux repliés dans un <template class="pan-tpl"> (performance) : mis en place avant lecture.
    const chapEl = $('chap-' + c.id);
    if(chapEl && window.__deplierChapitre) window.__deplierChapitre(chapEl);
    const carte = carteTeX(), parties = [];
    for(const p of c.panels || []){
      if(p === 'simu' || p === 'video') continue;
      if(p === 'flash'){
        const cartes = (window.FLASH_REGISTRY && window.FLASH_REGISTRY[c.prefix]) || [];
        if(!cartes.length) continue;
        const nu = h => String(h || '').replace(/<br\s*\/?>/gi, '\n').replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
        parties.push('# Cartes\n' + cartes.map((k, i) => 'Q' + (i + 1) + '. ' + nu(k.q) + '\nR. ' + nu(k.a)).join('\n'));
        continue;
      }
      const el = $(c.prefix + '-' + p);
      if(!el) continue;
      const t = serialiser(el, texDeCarte(carte));
      if(t) parties.push('# ' + (ONGLETS[p] || p) + '\n' + t);
    }
    const texte = parties.join('\n\n');
    const r = { empreinte: 'fnv1a:' + fnv(texte), signes: texte.length, jetons: Math.round(texte.length / 3.4), texte };
    contenus.set(c.id, r);
    return r;
  }

  /* ─────────────── 2. Collecteur (schéma 1) ─────────────── */
  function contexte(o){
    o = o || {};
    const carte = carteTeX();
    const chap = chapitreVisible();
    const c = chap ? chapitres()[chap.id.replace(/^chap-/, '')] : null;
    const so = window.__sommaireOuvert ? window.__sommaireOuvert() : null;
    const ctx = {
      schema: SCHEMA,
      url: location.href,
      page: c ? 'chapitre' : (so ? 'sommaire' : 'accueil'),
      annee: window.__currentYear ? window.__currentYear() : null,
      matiere: null, chapitre: null, onglet: null, section: null, methode: null,
      exercice: null, carte: null, simulateur: null, video: null, selection: null, contenu: null,
    };
    if(so && !c) ctx.matiere = { code: so, nom: MATIERES[so] || so };
    if(c){
      ctx.matiere = { code: c.matiere, nom: MATIERES[c.matiere] || c.matiere };
      const an = window.__chapYear ? window.__chapYear(c) : null;
      ctx.chapitre = { id: c.id, prefix: c.prefix, nom: c.name, partie: c.subLabel || null, tag: c.matiereLabel || null,
                       annee: an === 0 ? 'les deux' : an };
      const pan = panneauActif(chap);
      const onglet = pan ? pan.id.slice(c.prefix.length + 1) : null;
      ctx.onglet = onglet;
      const y = ligneLecture(chap);
      if(pan && (onglet === 'cours' || onglet === 'meth')){
        const secs = Array.from(pan.querySelectorAll('.sec-num')).filter(s => !s.closest('.exo'));
        ctx.section = infoSection(courant(secs, y));
        if(onglet === 'meth'){
          const box = courant(Array.from(pan.querySelectorAll('.method-box')), y);
          const t = box && box.querySelector('strong, b, h3, h4');
          if(t) ctx.methode = { titre: serialiser(t, texDeCarte(carte)) };
        }
      }
      if(pan && onglet === 'exos'){
        const exos = Array.from(pan.querySelectorAll('.exo')).filter(e => !e.classList.contains('filtre-masque'));
        ctx.exercice = infoExercice(courant(exos, y), carte);
      }
      if(pan && onglet === 'flash') ctx.carte = infoCarte(pan, c.prefix, carte);
      if(pan && onglet === 'simu') ctx.simulateur = infoSimulateur(pan);
      ctx.video = infoVideo(c.id);
      if(o.contenu) ctx.contenu = contenuChapitre(c);
    }
    const sel = o.selection === undefined ? selectionCourante : o.selection;
    if(sel && sel.range){
      const t = texteSelection(sel.range);
      if(t){
        const n = sel.range.startContainer;
        const el = n.nodeType === 1 ? n : n.parentElement;
        const s = el && el.closest ? el.closest('.course-section') : null;
        const sn = s && s.querySelector('.sec-num');
        ctx.selection = { texte: coupe(t, 4000), section: sn ? (infoSection(sn) || {}).num : null };
      }
    }
    return ctx;
  }

  /* ─────────────── 3. Fiche de demande (étape 3a, sans agent) ─────────────── */
  function fiche(demande){
    const x = contexte({ contenu:false });
    const L = ['# Demande de modification (assistant du site de révisions)', '', '**Demande** : ' + (demande || '').trim(), '', '**Où**'];
    L.push('- Page : ' + x.url);
    if(x.chapitre){
      const c = x.chapitre;
      L.push('- Chapitre : ' + c.nom + ' (id `' + c.id + '`, préfixe `' + c.prefix + '`, ' + (x.matiere ? x.matiere.nom : '') + ' › ' + (c.partie || '') + ', année : ' + c.annee + ')');
      if(x.onglet) L.push('- Onglet : ' + (ONGLETS[x.onglet] || x.onglet) + ' (panneau `' + c.prefix + '-' + x.onglet + '`)');
    }
    if(x.section) L.push('- Section : ' + (x.section.num ? x.section.num + ' ' : '') + '« ' + x.section.titre + ' »');
    if(x.methode) L.push('- Méthode : « ' + x.methode.titre + ' »');
    if(x.exercice) L.push('- Exercice : ' + (x.exercice.num || '') + ' « ' + (x.exercice.titre || '') + ' »' + (x.exercice.concours ? ' (Concours PT)' : ''));
    if(x.carte) L.push('- Carte : ' + (x.carte.rang ? x.carte.rang + '/' + x.carte.total + ' ' : '') + 'du paquet `' + x.carte.deck + '` — Q : « ' + coupe(x.carte.question || '', 300) + ' »');
    if(x.simulateur) L.push('- Simulateur : ' + x.simulateur.titre + (x.simulateur.mode ? ' (mode ' + x.simulateur.mode + ')' : ''));
    if(x.video){
      const v = x.video;
      let l = '- Vidéo : « ' + v.titre + ' » (YouTube `' + v.yt + '`' + (v.src ? ', sources `' + v.src + '`' : '') + '), à ' + v.temps + (v.estime ? ' (environ)' : '');
      if(v.partie) l += ', partie « ' + v.partie + ' »';
      if(v.scene) l += ', scène ' + v.scene.id + (v.scene.titre ? ' « ' + v.scene.titre + ' »' : '');
      L.push(l);
      if(v.phrase) L.push('  - Phrase `' + v.phrase.id + '` : « ' + v.phrase.ecrit + ' »');
    }
    if(x.selection){ L.push('- Passage sélectionné :'); x.selection.texte.split('\n').forEach(s => L.push('  > ' + s)); }
    L.push('', '**Consignes** : suivre `CLAUDE.md` (ancres grep, rédaction originale, notations du site ; `validate.py`, `check_js.py`, tests concernés ; bump de `CACHE_VERSION` si un fichier mis en cache change) ; pour une vidéo, `video/README.md`.');
    return L.join('\n');
  }

  /* ─────────────── 4. Panneau ─────────────── */
  const panel = $('assistant-panel');
  let construit = false, ouvert = false, opener = null, minuterie = 0, mode = 'question';
  let selectionCourante = null, dernierResume = '';
  const icone = n => (window.__icon ? window.__icon(n) : '');

  function construire(){
    if(construit || !panel) return;
    construit = true;
    panel.innerHTML = ''
      + '<div class="assist-tete">'
      +   '<h2 class="assist-titre" id="assistant-titre">Assistant</h2>'
      +   '<span class="assist-etat" title="La discussion sera reliée à l’étape suivante (relais)">bientôt relié</span>'
      +   '<button type="button" class="btn btn-ghost btn-icon assist-x" aria-label="Fermer l’assistant">' + icone('x') + '</button>'
      + '</div>'
      + '<div class="assist-corps">'
      +   '<section class="assist-ctx" aria-labelledby="assist-ctx-t">'
      +     '<h3 class="assist-kicker" id="assist-ctx-t">Ce que l’assistant voit</h3>'
      +     '<p class="assist-lieu"><span class="pastille" aria-hidden="true"></span><span class="assist-lieu-t"></span></p>'
      +     '<p class="assist-chap"></p>'
      +     '<ul class="assist-faits"></ul>'
      +     '<details class="assist-detail"><summary>Détail de l’envoi</summary>'
      +       '<pre class="assist-json" tabindex="0" aria-label="Contexte envoyé, au format JSON"></pre>'
      +       '<button type="button" class="btn btn-ghost assist-copier">' + icone('copy') + '<span class="ic-lbl">Copier le contexte</span></button>'
      +     '</details>'
      +   '</section>'
      +   '<div class="assist-fil" role="log" aria-live="polite" aria-relevant="additions">'
      +     '<p class="assist-accueil">Pose une question sur ce que tu lis : l’assistant reçoit tout seul la page, la section visible, '
      +     'ta sélection et l’instant de la vidéo. '
      +     (relais() ? '' : '<strong>Pas encore relié</strong> : les réponses arriveront avec la mise en service du relais. ')
      +     'Le mode <strong>Modification</strong> prépare une demande à coller dans Claude Code.</p>'
      +   '</div>'
      + '</div>'
      + '<form class="assist-saisie" novalidate>'
      +   '<div class="seg assist-mode" role="radiogroup" aria-label="Type de demande">'
      +     '<button type="button" role="radio" aria-checked="true" tabindex="0" data-mode="question">Question</button>'
      +     '<button type="button" role="radio" aria-checked="false" tabindex="-1" data-mode="modif">Modification</button>'
      +   '</div>'
      +   '<label class="sr" for="assistant-question">Ta demande</label>'
      +   '<textarea id="assistant-question" class="assist-champ" rows="2"></textarea>'
      +   '<div class="assist-actions">'
      +     '<button type="button" class="btn btn-ghost assist-nouvelle" hidden>Nouvelle conversation</button>'
      +     '<p class="assist-aide" aria-hidden="true">Entrée : envoyer · Maj+Entrée : à la ligne</p>'
      +     '<button type="submit" class="btn btn-primary assist-envoyer">' + icone('send') + '<span class="ic-lbl">Envoyer</span></button>'
      +   '</div>'
      + '</form>';

    panel.querySelector('.assist-x').addEventListener('click', () => fermer());
    panel.addEventListener('keydown', e => {
      if(e.key === 'Escape'){ e.stopPropagation(); fermer(); return; }
      if(e.key === 'Tab' && estTelephone() && window.__focusables){   // page plein écran : focus piégé
        const f = window.__focusables(panel);
        if(!f.length) return;
        const i = f.indexOf(document.activeElement);
        if(e.shiftKey && (i <= 0)){ e.preventDefault(); f[f.length - 1].focus(); }
        else if(!e.shiftKey && i === f.length - 1){ e.preventDefault(); f[0].focus(); }
      }
    });
    const det = panel.querySelector('.assist-detail');
    det.addEventListener('toggle', () => { if(det.open) majJSON(); });
    panel.querySelector('.assist-copier').addEventListener('click', () => {
      copier(JSON.stringify(contexte({ contenu:true }), null, 2), 'Contexte copié');
    });
    // Type de demande : groupe radio (flèches, tabindex itinérant)
    const radios = Array.from(panel.querySelectorAll('.assist-mode [role="radio"]'));
    const choisir = (b, focus) => {
      radios.forEach(r => { const on = r === b; r.setAttribute('aria-checked', on ? 'true' : 'false'); r.tabIndex = on ? 0 : -1; });
      mode = b.getAttribute('data-mode');
      majChamp();
      if(focus) b.focus();
    };
    radios.forEach((b, i) => {
      b.addEventListener('click', () => choisir(b));
      b.addEventListener('keydown', e => {
        if(e.key === 'ArrowRight' || e.key === 'ArrowDown'){ e.preventDefault(); choisir(radios[(i + 1) % radios.length], true); }
        if(e.key === 'ArrowLeft' || e.key === 'ArrowUp'){ e.preventDefault(); choisir(radios[(i - 1 + radios.length) % radios.length], true); }
      });
    });
    const champ = $('assistant-question');
    champ.addEventListener('input', ajusterChamp);
    champ.addEventListener('keydown', e => {
      if(e.key === 'Enter' && !e.shiftKey && !e.isComposing){ e.preventDefault(); envoyer(); }
    });
    panel.querySelector('.assist-saisie').addEventListener('submit', e => { e.preventDefault(); envoyer(); });
    panel.querySelector('.assist-nouvelle').addEventListener('click', () => {
      conversations.delete(cleConversation());
      panel.querySelectorAll('.assist-fil > .assist-msg, .assist-fil > .assist-code').forEach(m => m.remove());
      majEnvoi();
      const c = $('assistant-question'); if(c) c.focus();
    });
    panel.addEventListener('click', e => {
      const b = e.target && e.target.closest ? e.target.closest('.assist-lien-sec') : null;
      if(b){ e.preventDefault(); allerSection(b.getAttribute('data-sec')); }
    });
    majChamp();
    typo(panel);
    // Fermeture par le bouton retour d'Android (urlRouting envoie Échap au document)
    document.addEventListener('keydown', e => {
      if(e.key === 'Escape' && ouvert && estTelephone() && !panel.contains(e.target)) fermer();
    });
  }

  // Typographie du site (espaces fines insécables avant ; ! ?, insécables dans « »…) : idempotente
  function typo(el){ try { if(window.__typographier) window.__typographier(el); } catch(e){} }
  function majChamp(){
    const champ = $('assistant-question');
    if(!champ) return;
    champ.placeholder = mode === 'modif'
      ? 'Décris la modification\u00a0: «\u00a0corrige cette démonstration\u00a0», «\u00a0reformule ce passage\u00a0»…'
      : 'Ta question sur cette page…';
    const b = panel.querySelector('.assist-envoyer .ic-lbl');
    if(b) b.textContent = mode === 'modif' ? 'Préparer la fiche' : 'Envoyer';
  }
  function ajusterChamp(){
    const c = $('assistant-question');
    if(!c) return;
    c.style.height = 'auto';
    c.style.height = Math.min(c.scrollHeight + 2, Math.round((window.innerHeight || 800) * 0.4)) + 'px';
  }

  function ajouterMessage(type, titre, corps, pre){
    const fil = panel.querySelector('.assist-fil');
    const d = document.createElement('div');
    d.className = 'assist-msg ' + type;
    if(titre){ const t = document.createElement('span'); t.className = 'assist-msg-t'; t.textContent = titre; d.appendChild(t); }
    if(corps){ const p = document.createElement('p'); p.textContent = corps; d.appendChild(p); }
    if(pre){ const p = document.createElement('pre'); p.textContent = pre; p.tabIndex = 0; d.appendChild(p); }
    fil.appendChild(d);
    typo(d);
    const corpsEl = panel.querySelector('.assist-corps');
    try { d.scrollIntoView({ block:'nearest', behavior: window.__reduceMotion ? 'auto' : 'smooth' }); } catch(e){ corpsEl.scrollTop = corpsEl.scrollHeight; }
    return d;
  }

  function envoyer(){
    const champ = $('assistant-question');
    if(enCours){ enCours.ctrl.abort(); return; }   // le bouton sert alors à arrêter la réponse
    const texte = (champ.value || '').trim();
    if(!texte){ champ.focus(); return; }
    ajouterMessage('moi', null, texte);
    champ.value = ''; ajusterChamp();
    if(mode === 'modif'){
      const f = fiche(texte);
      copier(f, null).then(ok => {
        ajouterMessage('note', ok ? 'Fiche copiée' : 'Fiche prête',
          (ok ? 'Colle-la dans une session Claude Code (environnement « revisions-ptsi ») : ' : 'Copie-la (sélectionne le texte) et colle-la dans une session Claude Code : ')
          + 'elle dit exactement où modifier.', f);
      });
      return;
    }
    if(!relais()){
      ajouterMessage('note', 'Pas encore relié',
        'Question notée avec son contexte, mais l’assistant n’est pas encore relié : les réponses arriveront avec la mise en service du relais (assistant/MISE-EN-SERVICE.md).');
      return;
    }
    demander(texte, false);
  }

  function copier(texte, toast){
    const fin = ok => { if(ok && toast && window.__toast) window.__toast(toast, { icone:'copy' }); return ok; };
    if(navigator.clipboard && navigator.clipboard.writeText){
      return navigator.clipboard.writeText(texte).then(() => fin(true), () => fin(copierVieux(texte)));
    }
    return Promise.resolve(fin(copierVieux(texte)));
  }
  function copierVieux(texte){
    const avant = document.activeElement;   // la copie de secours déplace le focus : on le rend ensuite
    try {
      const t = document.createElement('textarea');
      t.value = texte; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
      panel.appendChild(t); t.select();
      const ok = document.execCommand('copy'); t.remove();
      if(avant && avant.focus) try { avant.focus({ preventScroll:true }); } catch(e){}
      return ok;
    } catch(e){ if(avant && avant.focus) try { avant.focus({ preventScroll:true }); } catch(_){} return false; }
  }

  // Résumé « Ce que l'assistant voit » (tenu à jour tant que le panneau est ouvert)
  function majResume(){
    if(!construit) return;
    const x = contexte({ contenu:false });
    const faits = [];
    if(x.chapitre){
      let o = ONGLETS[x.onglet] || x.onglet || '';
      if(x.section) o += ' · ' + (x.section.num ? x.section.num + ' ' : '') + x.section.titre;
      if(x.methode) o += ' · ' + x.methode.titre;
      if(x.exercice) o += ' · ' + (x.exercice.num || '') + (x.exercice.titre ? ' ' + x.exercice.titre : '');
      if(x.carte) o += ' · carte ' + (x.carte.rang || '?') + '/' + (x.carte.total || '?') + ' (' + x.carte.face + ')';
      if(x.simulateur && x.simulateur.mode) o += ' · mode ' + x.simulateur.mode;
      faits.push(['Où', o]);
    } else {
      faits.push(['Où', x.page === 'sommaire' ? 'Sommaire de la matière' : 'Aucun chapitre affiché']);
    }
    if(x.selection) faits.push(['Sélection', '« ' + coupe(x.selection.texte.replace(/\s+/g, ' '), 180) + ' »', 'sel']);
    if(x.video) faits.push(['Vidéo', x.video.titre + ', à ' + x.video.temps + (x.video.estime ? ' (environ)' : '') + (x.video.partie ? ' — ' + x.video.partie : '')]);
    if(x.chapitre){
      const cc = contenus.get(x.chapitre.id);
      faits.push(['Contenu', cc ? 'le chapitre entier, ' + nb(cc.signes) + ' signes (≈ ' + nb(cc.jetons) + ' jetons)' : 'le chapitre entier (mesure en cours…)']);
    }
    const cle = JSON.stringify([x.matiere, x.chapitre && x.chapitre.id, faits]);
    if(cle === dernierResume) return;
    dernierResume = cle;
    const ctxEl = panel.querySelector('.assist-ctx');
    if(x.matiere) ctxEl.setAttribute('data-mat', x.matiere.code); else ctxEl.removeAttribute('data-mat');
    panel.querySelector('.assist-lieu-t').textContent = x.chapitre
      ? [x.matiere && x.matiere.nom, x.chapitre.partie, x.chapitre.annee === 2 ? '2ᵉ année' : (x.chapitre.annee === 1 ? '1ʳᵉ année' : null)].filter(Boolean).join(' · ')
      : (x.matiere ? x.matiere.nom : 'Site de révisions');
    panel.querySelector('.assist-chap').textContent = x.chapitre ? x.chapitre.nom : '';
    const ul = panel.querySelector('.assist-faits');
    ul.innerHTML = '';
    faits.forEach(([l, v, cls]) => {
      const li = document.createElement('li');
      if(cls) li.className = 'assist-' + cls;
      const a = document.createElement('span'); a.className = 'lbl'; a.textContent = l;
      const b = document.createElement('span'); b.className = 'val'; b.textContent = v;
      li.append(a, b);
      if(cls === 'sel'){
        const r = document.createElement('button');
        r.type = 'button'; r.className = 'btn btn-ghost btn-icon assist-retirer';
        r.setAttribute('aria-label', 'Ne pas envoyer la sélection');
        r.innerHTML = icone('x');
        r.addEventListener('click', () => { selectionCourante = null; majResume(); const ch = $('assistant-question'); if(ch) ch.focus(); });
        li.appendChild(r);
      }
      ul.appendChild(li);
    });
    typo(ctxEl);
    const det = panel.querySelector('.assist-detail');
    if(det && det.open) majJSON();
  }
  function majJSON(){
    const x = contexte({ contenu:true });
    if(x.contenu) x.contenu = Object.assign({}, x.contenu, { texte: coupe(x.contenu.texte, 700) + ' [… ' + nb(x.contenu.signes) + ' signes au total]' });
    panel.querySelector('.assist-json').textContent = JSON.stringify(x, null, 2);
  }
  // Mesure du contenu au repos (le résumé l'affiche dès qu'elle est prête)
  function mesurerContenu(){
    const chap = chapitreVisible();
    const c = chap ? chapitres()[chap.id.replace(/^chap-/, '')] : null;
    if(!c || contenus.has(c.id)) return;
    const f = () => { try { contenuChapitre(c); dernierResume = ''; majResume(); } catch(e){} };
    if(window.requestIdleCallback) requestIdleCallback(f, { timeout:1200 }); else setTimeout(f, 200);
  }

  function ouvrir(o){
    o = o || {};
    construire();
    if(o.selection) selectionCourante = o.selection;
    else if(window.__assistantSelection){ const s = window.__assistantSelection(); if(s && Date.now() - s.t < 60000) selectionCourante = s; }
    opener = o.opener || opener || $('assistant-btn');
    const tel = estTelephone();
    panel.setAttribute('aria-modal', tel ? 'true' : 'false');
    if(!ouvert){
      ouvert = true;
      panel.classList.add('open');
      document.documentElement.classList.add('assistant-ouvert');
      document.querySelectorAll('#assistant-btn').forEach(b => b.setAttribute('aria-expanded', 'true'));
    }
    dernierResume = '';
    majResume();
    mesurerContenu();
    majEtat();
    majEnvoi();
    clearInterval(minuterie);
    minuterie = setInterval(() => { if(!document.hidden){ majResume(); mesurerContenu(); } }, 1500);
    const champ = $('assistant-question');
    if(o.mode === 'modif'){ const b = panel.querySelector('[data-mode="modif"]'); if(b) b.click(); }
    // Téléphone : focus sur le panneau (le clavier virtuel ne surgit pas d'office)
    try { (tel ? panel : champ).focus({ preventScroll:true }); } catch(e){}
  }
  function fermer(){
    if(!ouvert) return;
    ouvert = false;
    clearInterval(minuterie);
    const avaitFocus = panel.contains(document.activeElement);
    panel.classList.remove('open');
    document.documentElement.classList.remove('assistant-ouvert');
    document.querySelectorAll('#assistant-btn').forEach(b => b.setAttribute('aria-expanded', 'false'));
    if(avaitFocus && window.__rendreFocus){
      const repli = $('assistant-btn');
      window.__rendreFocus(opener && opener.getClientRects().length ? opener : null, repli && repli.getClientRects().length ? repli : (document.querySelector('.chapter.active .tab.active') || null));
    }
  }

  /* ─────────────── 5. Discussion par le relais (phase 1) ───────────────
     Le relais (assistant/relais/, Cloudflare Worker) garde la clé de l'API Claude ; le site ne
     connaît que son adresse (rien de secret) et un JETON d'appareil, obtenu une fois avec le code
     d'accès de Thomas et rangé dans IndexedDB : jamais dans Store ni dans le localStorage
     exporté par la Sauvegarde. Sans adresse de relais, l'assistant reste « pas encore relié ». */
  const RELAIS = '';   // ex. 'https://revisions-assistant.<sous-domaine>.workers.dev' (assistant/MISE-EN-SERVICE.md, étape 5)
  const relais = () => (window.__RELAIS_ASSISTANT || RELAIS || '').replace(/\/+$/, '');
  let memJeton = null;
  function base(){
    return new Promise((ok, ko) => {
      if(!window.indexedDB){ ko(new Error('indexedDB')); return; }
      const r = indexedDB.open('assistant-ia', 1);
      r.onupgradeneeded = () => r.result.createObjectStore('cles');
      r.onsuccess = () => ok(r.result);
      r.onerror = () => ko(r.error);
    });
  }
  async function jetonLire(){
    if(memJeton && memJeton.exp > Date.now()) return memJeton;
    try {
      const db = await base();
      const v = await new Promise(ok => { const q = db.transaction('cles').objectStore('cles').get('jeton'); q.onsuccess = () => ok(q.result || null); q.onerror = () => ok(null); });
      memJeton = v && v.exp > Date.now() ? v : null;
    } catch(e){ /* stockage indisponible : jeton en mémoire seulement */ }
    return memJeton;
  }
  async function jetonEcrire(v){
    memJeton = v;
    try {
      const db = await base();
      await new Promise(ok => { const tx = db.transaction('cles', 'readwrite'); const s = tx.objectStore('cles'); if(v) s.put(v, 'jeton'); else s.delete('jeton'); tx.oncomplete = ok; tx.onerror = ok; });
    } catch(e){}
  }

  // Conversation du chapitre affiché : [{ role:'user', texte, contexte } | { role:'assistant', texte }]
  const conversations = new Map();
  let enCours = null;   // { ctrl } pendant une réponse
  const cleConversation = () => { const c = chapitreVisible(); return c ? c.id : 'hors-chapitre'; };
  function contexteVolatil(x){
    const v = {};
    ['page', 'onglet', 'section', 'methode', 'exercice', 'carte', 'simulateur', 'video', 'selection'].forEach(k => { if(x[k] != null) v[k] = x[k]; });
    return v;
  }

  /* Rendu d'une réponse : paragraphes, listes, **gras**, `code`, renvois « §n » cliquables ;
     formules laissées en TeX puis composées par MathJax. Jamais d'innerHTML du modèle. */
  function enLigne(parent, t){
    const re = /(\*\*[^*\n]+\*\*|`[^`\n]+`|§\s?\d+)/g;
    let i = 0, m;
    while((m = re.exec(t))){
      if(m.index > i) parent.appendChild(document.createTextNode(t.slice(i, m.index)));
      const s = m[0];
      if(s.startsWith('**')){ const b = document.createElement('strong'); b.textContent = s.slice(2, -2); parent.appendChild(b); }
      else if(s.startsWith('`')){ const c = document.createElement('code'); c.textContent = s.slice(1, -1); parent.appendChild(c); }
      else {   // renvoi « §n » : un vrai lien dans la phrase (navigation vers la section du cours)
        const a = document.createElement('a'); a.className = 'assist-lien-sec'; a.textContent = s;
        const id = cleConversation();
        a.href = id !== 'hors-chapitre' ? '#' + id + '/cours' : '#';
        a.setAttribute('data-sec', s.replace(/\s+/g, '')); parent.appendChild(a);
      }
      i = re.lastIndex;
    }
    if(i < t.length) parent.appendChild(document.createTextNode(t.slice(i)));
  }
  function blocDOM(b){
    const t = b.replace(/^\n+|\n+$/g, '');
    if(/^\s*\$\$[\s\S]*\$\$\s*$/.test(t)){ const d = document.createElement('div'); d.className = 'assist-formule'; d.textContent = t.trim(); return d; }
    const lignes = t.split('\n');
    if(lignes.every(l => /^\s*([-*•]|\d+[.)])\s+/.test(l) || /^\s{2,}\S/.test(l))){
      const liste = document.createElement(/^\s*\d/.test(lignes[0]) ? 'ol' : 'ul');
      lignes.forEach(l => {
        const m = l.match(/^\s*(?:[-*•]|\d+[.)])\s+(.*)$/);
        if(m){ const li = document.createElement('li'); enLigne(li, m[1]); liste.appendChild(li); }
        else if(liste.lastChild) enLigne(liste.lastChild, ' ' + l.trim());
      });
      return liste;
    }
    const p = document.createElement('p');
    lignes.forEach((l, k) => { if(k) p.appendChild(document.createElement('br')); enLigne(p, l); });
    return p;
  }
  function composer(el){
    if(window.MathJax && MathJax.typesetPromise) return MathJax.typesetPromise([el]).catch(() => {});
    return Promise.resolve();
  }
  // Réponse en cours : les paragraphes terminés sont rendus et composés, le dernier reste brut
  function rendeurFlux(boite){
    const corps = boite.querySelector('.assist-rep');
    const brut = document.createElement('p'); brut.className = 'assist-encours';
    corps.appendChild(brut);
    let texte = '', faits = 0;
    return {
      ajouter(t){
        texte += t;
        const blocs = texte.split(/\n{2,}/);
        for(; faits < blocs.length - 1; faits++){
          if(!blocs[faits].trim()) continue;
          const d = blocDOM(blocs[faits]);
          corps.insertBefore(d, brut);
          composer(d);
        }
        brut.textContent = blocs[blocs.length - 1];
      },
      finir(){
        const blocs = texte.split(/\n{2,}/);
        const der = blocs[blocs.length - 1];
        brut.remove();
        if(der && der.trim()){ const d = blocDOM(der); corps.appendChild(d); composer(d); }
        return texte;
      },
      texte: () => texte,
    };
  }
  function allerSection(num){
    const chap = chapitreVisible();
    const c = chap ? chapitres()[chap.id.replace(/^chap-/, '')] : null;
    if(!c) return;
    const cible = () => {
      const sec = Array.from(document.querySelectorAll('#' + c.prefix + '-cours .sec-num')).find(s => new RegExp('^' + num.replace('§', '§\\s*') + '\\b').test((s.textContent || '').trim()));
      const bloc = sec && (sec.closest('.course-section') || sec);
      if(bloc) bloc.scrollIntoView({ block:'start', behavior: window.__reduceMotion ? 'auto' : 'smooth' });
    };
    if(estTelephone()) fermer();
    const onglet = panneauActif(chap);
    if(onglet && onglet.id === c.prefix + '-cours') cible();
    else if(window.navigateTo) navigateTo('chap-' + c.id, c.prefix + '-cours', cible);
  }

  function reponseBoite(){
    const fil = panel.querySelector('.assist-fil');
    const d = document.createElement('div');
    d.className = 'assist-msg ia';
    d.setAttribute('aria-busy', 'true');
    const t = document.createElement('span'); t.className = 'assist-msg-t'; t.textContent = 'Assistant';
    const r = document.createElement('div'); r.className = 'assist-rep';
    d.append(t, r);
    fil.appendChild(d);
    return d;
  }
  function piedReponse(boite, fin){
    const pied = document.createElement('div');
    pied.className = 'assist-pied';
    const m = document.createElement('span');
    m.className = 'assist-meta';
    const nom = /opus/.test(fin.modele || '') ? 'Opus' : /haiku/.test(fin.modele || '') ? 'Haiku' : 'Sonnet';
    m.textContent = nom + (typeof fin.cout === 'number' ? ' · ' + (fin.cout < 0.01 ? '< 1 centime' : '≈ ' + nb(Math.round(fin.cout * 100)) + ' centime' + (fin.cout >= 0.015 ? 's' : '')) : '');
    pied.appendChild(m);
    if(!/opus/.test(fin.modele || '')){
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'btn btn-ghost assist-approfondir';
      b.textContent = 'Approfondir';
      b.title = 'Redemander avec un modèle plus puissant (plus lent, plus cher)';
      b.addEventListener('click', () => { b.disabled = true; demander('Approfondis ta réponse précédente : plus de rigueur et de détails.', true); });
      pied.appendChild(b);
    }
    boite.appendChild(pied);
  }
  const MESSAGES_ERREUR = {
    budget: 'Budget du jour atteint : l’assistant reprend demain (plafond réglé dans le relais).',
    debit: 'Trop de questions en une minute : réessaie dans un instant.',
    surcharge: 'Le service de Claude est surchargé : réessaie dans un instant.',
    configuration: 'Le relais est mal configuré (clé de l’API ?) : voir assistant/MISE-EN-SERVICE.md.',
    reseau: 'Le relais n’a pas pu joindre Claude : réessaie dans un instant.',
    service: 'Le service de Claude a renvoyé une erreur : réessaie dans un instant.',
    requete_api: 'La demande a été refusée par l’API (trop longue ?).',
    requete: 'La demande a été refusée par le relais (trop longue ?).',
    annule: 'Réponse arrêtée.',
    interne: 'Erreur du relais : réessaie dans un instant.',
  };

  async function demanderCode(question, approfondir){
    ajouterMessage('note', 'Code d’accès', 'Cet appareil n’est pas encore autorisé : tape ton code d’accès (une fois, valable 30 jours).');
    const fil = panel.querySelector('.assist-fil');
    const f = document.createElement('form');
    f.className = 'assist-code';
    f.innerHTML = '<label class="sr" for="assistant-code">Code d’accès</label>'
      + '<input id="assistant-code" class="assist-champ" type="password" autocomplete="current-password" placeholder="Code d’accès">'
      + '<button type="submit" class="btn btn-primary">Valider</button>';
    fil.appendChild(f);
    const champ = f.querySelector('input');
    try { champ.focus({ preventScroll:true }); } catch(e){}
    f.addEventListener('submit', async e => {
      e.preventDefault();
      const code = champ.value;
      if(!code) return;
      const b = f.querySelector('button'); b.disabled = true;
      try {
        const r = await fetch(relais() + '/auth', { method:'POST', headers:{ 'Content-Type':'application/json' }, body: JSON.stringify({ code }) });
        const j = await r.json().catch(() => ({}));
        if(r.ok && j.jeton){
          await jetonEcrire({ jeton:j.jeton, exp:j.exp });
          f.remove(); majEtat();
          ajouterMessage('note', 'Appareil autorisé', 'C’est fait : l’assistant répond désormais sur cet appareil.');
          if(question) demander(question, approfondir);
          else { const c = $('assistant-question'); if(c) c.focus(); }
        } else {
          b.disabled = false; champ.value = ''; champ.focus();
          ajouterMessage('note', 'Code refusé', j.erreur === 'trop_de_tentatives' ? 'Trop d’essais : réessaie dans une heure.' : 'Ce code n’est pas le bon.');
        }
      } catch(err){
        b.disabled = false;
        ajouterMessage('note', 'Relais injoignable', navigator.onLine === false ? 'Hors connexion.' : 'Le relais ne répond pas : réessaie dans un instant.');
      }
    });
  }

  async function demander(question, approfondir){
    const jt = await jetonLire();
    if(!jt){ demanderCode(question, approfondir); return; }
    const x = contexte({ contenu:true });
    const cle = cleConversation();
    const hist = conversations.get(cle) || [];
    const vol = contexteVolatil(x);
    const corps = {
      chapitre: x.chapitre ? { id:x.chapitre.id, nom:x.chapitre.nom, matiere: x.matiere ? x.matiere.nom : '', partie:x.chapitre.partie, annee:x.chapitre.annee } : null,
      contenu: x.contenu ? { empreinte:x.contenu.empreinte, texte:x.contenu.texte } : null,
      contexte: vol, historique: hist.slice(-28), question, approfondir: !!approfondir,
    };
    const boite = reponseBoite();
    const flux = rendeurFlux(boite);
    const ctrl = new AbortController();
    enCours = { ctrl };
    majEnvoi();
    let fin = null, erreur = null;
    try {
      const r = await fetch(relais() + '/chat', { method:'POST', signal: ctrl.signal,
        headers:{ 'Content-Type':'application/json', Authorization:'Bearer ' + jt.jeton }, body: JSON.stringify(corps) });
      if(r.status === 401){ await jetonEcrire(null); boite.remove(); enCours = null; majEnvoi(); majEtat(); demanderCode(question, approfondir); return; }
      if(!r.ok || !r.body){ const j = await r.json().catch(() => ({})); erreur = j.erreur || 'interne'; }
      else {
        const lecteur = r.body.getReader(), dec = new TextDecoder();
        let tampon = '';
        for(;;){
          const { value, done } = await lecteur.read();
          if(done) break;
          tampon += dec.decode(value, { stream:true });
          let k;
          while((k = tampon.indexOf('\n\n')) >= 0){
            const bloc = tampon.slice(0, k); tampon = tampon.slice(k + 2);
            const ev = (/^event: (.*)$/m.exec(bloc) || [])[1], d = (/^data: (.*)$/m.exec(bloc) || [])[1];
            let data = null; try { data = d ? JSON.parse(d) : null; } catch(e){}
            if(ev === 'texte' && data) flux.ajouter(data.t || '');
            else if(ev === 'fin') fin = data || {};
            else if(ev === 'erreur') erreur = (data && data.code) || 'interne';
          }
        }
      }
    } catch(e){
      erreur = e && e.name === 'AbortError' ? 'annule' : (navigator.onLine === false ? 'hors' : 'injoignable');
    }
    const texte = flux.finir();
    boite.removeAttribute('aria-busy');
    enCours = null; majEnvoi();
    if(fin && fin.arret === 'refusal'){
      ajouterMessage('note', 'Pas de réponse', 'L’assistant n’a pas pu répondre à cette demande. Reformule-la autrement.');
    } else if(fin && texte.trim()){
      piedReponse(boite, fin);
      hist.push({ role:'user', texte:question, contexte:vol }, { role:'assistant', texte });
      while(hist.length > 28) hist.splice(0, 2);
      conversations.set(cle, hist);
      majEnvoi();
    }
    if(erreur){
      if(!texte.trim()) boite.remove();
      ajouterMessage('note', 'Pas de réponse', erreur === 'hors' ? 'Hors connexion : l’assistant a besoin d’Internet.'
        : erreur === 'injoignable' ? 'Le relais ne répond pas : réessaie dans un instant.' : (MESSAGES_ERREUR[erreur] || MESSAGES_ERREUR.interne));
    }
  }

  async function majEtat(){
    const p = panel && panel.querySelector('.assist-etat');
    if(!p) return;
    if(!relais()){ p.textContent = 'bientôt relié'; p.title = 'La discussion sera reliée à la mise en service du relais'; return; }
    const j = await jetonLire();
    p.textContent = j ? 'relié' : 'code requis';
    p.title = j ? 'Cet appareil est autorisé jusqu’au ' + new Date(j.exp).toLocaleDateString('fr-FR') : 'Ton code d’accès sera demandé à la première question';
  }
  function majEnvoi(){
    const b = panel && panel.querySelector('.assist-envoyer');
    if(!b) return;
    if(enCours){ b.classList.add('arret'); b.querySelector('.ic-lbl').textContent = 'Arrêter'; }
    else { b.classList.remove('arret'); majChamp(); }
    const n = panel.querySelector('.assist-nouvelle');
    if(n) n.hidden = !(conversations.get(cleConversation()) || []).length || !!enCours;
  }

  window.__contexteAssistant = contexte;
  window.__assistant = { ouvrir, fermer, estOuvert: () => ouvert, contexte, fiche, version: SCHEMA };
})();
