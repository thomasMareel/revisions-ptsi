<script>
/* ===== CONTENU : enrichissements d'affichage du cours, des exercices et des simulateurs =====
   (SPEC §7.2, §7.3, §7.14 ; styles : régions CONTENU et SIMU du grand <style>)
   Travail PARESSEUX : un panneau n'est traité qu'à son premier affichage (typesetPanel appelle
   window.__contenuPanneau), le reste après le rendu MathJax (window.__apresRendu, appelé dans la
   promesse de typesetPanel, de toggleSol, du Formulaire et du rendu de démarrage). Tout est
   idempotent (marqueurs) et défensif : une erreur ici ne coupe rien d'autre.
   - .sec-num « §1 · LES BASES » → <span class="sec-n">§1</span><span class="sr"> · </span>
     <span class="sec-t">LES BASES</span> : textContent inchangé (sommaire, recherche, impression) ;
   - .diff « ★ ★ ☆ » → data-niveau="2", 3 barres + « Moyen » (title « Difficulté 2 sur 3 ») ;
   - onglet Exercices : outils en tête (difficulté, Concours PT, effectif), qui masquent des .exo
     par la classe .filtre-masque (pas l'attribut hidden : l'impression garde tout) ;
   - après le rendu : typographie française (espace fine insécable avant ; ! ?, insécable avant :
     et », après «) hors code/pre/kbd/mjx-container, ponctuation collée à sa formule (.mj-colle),
     formule en ligne plus large que sa ligne (.mj-large : défile dans la ligne), schéma SVG dont
     un libellé passerait sous 12 px (largeur minimale + défilement de la figure) ;
   - simulateurs : --p sur chaque curseur (partie remplie de la piste), bouton « Valeurs par défaut »
     (valeurs d'origine du HTML : defaultValue / defaultSelected / defaultChecked). */
(function(){
  'use strict';
  var NIVEAUX = ['', 'Facile', 'Moyen', 'Difficile'];
  var BALISES_EXCLUES = /^(CODE|PRE|KBD|SAMP|VAR|SCRIPT|STYLE|TEXTAREA|INPUT|SELECT|OPTION|BUTTON|SVG|MATH|TEMPLATE|NOSCRIPT)$/;
  var rendus = new WeakSet();          // racines dont le rendu MathJax est terminé
  var raf = window.requestAnimationFrame ? window.requestAnimationFrame.bind(window) : function(f){ return setTimeout(f, 16); };
  function sur(f){ return function(){ try { return f.apply(this, arguments); } catch(e){ /* enrichissement non bloquant */ } }; }
  function visible(el){ return !!(el && el.isConnected && el.getClientRects().length); }

  /* ---------- 1. Surtitre de section (.sec-num, 1er enfant de .course-section) ---------- */
  function couperSecNum(el){
    if(!el || el.__secVu) return;
    el.__secVu = true;
    var t = el.firstChild;
    if(!t || t.nodeType !== 3) return;
    var m = /^\s*(§\s*\d+[a-z]?)\s*·\s*/.exec(t.nodeValue);
    if(!m) return;                     // « MÉTHODES · RLC »… : surtitre simple, inchangé
    var n = document.createElement('span'); n.className = 'sec-n'; n.textContent = m[1].replace(/\s+/g, '');
    var sep = document.createElement('span'); sep.className = 'sr'; sep.textContent = ' · ';
    var titre = document.createElement('span'); titre.className = 'sec-t';
    t.nodeValue = t.nodeValue.slice(m[0].length);
    while(el.firstChild) titre.appendChild(el.firstChild);
    el.appendChild(n); el.appendChild(sep); el.appendChild(titre);
    el.classList.add('coupe');
  }

  /* ---------- 2. Difficulté (.exo > .diff) ---------- */
  function enrichirDiff(d){
    if(!d || d.hasAttribute('data-niveau')) return;
    var n = ((d.textContent || '').match(/★/g) || []).length;
    if(n < 1 || n > 3) return;         // format inattendu : laissé tel quel
    d.setAttribute('data-niveau', String(n));
    d.title = 'Difficulté ' + n + ' sur 3';
    d.innerHTML = '<span class="bars" aria-hidden="true"><i></i><i></i><i></i></span>' + NIVEAUX[n];
  }
  function niveau(exo){
    var d = exo.querySelector(':scope > .diff');
    return d ? d.getAttribute('data-niveau') : null;
  }

  /* ---------- 3. Outils de l'onglet Exercices ---------- */
  function outilsExos(panel){
    if(panel.__outilsExos || !/-exos$/.test(panel.id)) return;
    panel.__outilsExos = true;
    var exos = Array.prototype.slice.call(panel.querySelectorAll('.exo'));
    if(exos.length < 2) return;
    var compte = { 1: 0, 2: 0, 3: 0 }, concours = 0;
    exos.forEach(function(e){
      var n = niveau(e); if(n && compte[n] !== undefined) compte[n]++;
      if(e.classList.contains('concours')) concours++;
    });
    var barre = document.createElement('div');
    barre.className = 'exo-tools';
    var seg = document.createElement('div');
    seg.className = 'seg';
    seg.setAttribute('role', 'group');
    seg.setAttribute('aria-label', 'Filtrer les exercices par difficulté');
    [['tous', 'Tous'], ['1', 'Facile'], ['2', 'Moyen'], ['3', 'Difficile']].forEach(function(o){
      if(o[0] !== 'tous' && !compte[o[0]]) return;      // niveau absent du chapitre : pas de bouton
      var b = document.createElement('button');
      b.type = 'button'; b.dataset.niveau = o[0]; b.textContent = o[1];
      b.setAttribute('aria-pressed', o[0] === 'tous' ? 'true' : 'false');
      if(o[0] !== 'tous') b.title = compte[o[0]] + ' exercice' + (compte[o[0]] > 1 ? 's' : '');
      seg.appendChild(b);
    });
    barre.appendChild(seg);
    var puce = null;
    if(concours){
      puce = document.createElement('button');
      puce.type = 'button'; puce.className = 'chip';
      puce.setAttribute('aria-pressed', 'false');
      puce.textContent = 'Concours PT · ' + concours;
      puce.title = 'Ne garder que les exercices de type concours';
      barre.appendChild(puce);
    }
    var info = document.createElement('span');
    info.className = 'info';
    info.setAttribute('aria-live', 'polite');
    barre.appendChild(info);
    var vide = document.createElement('p');
    vide.className = 'vide';
    vide.hidden = true;
    vide.textContent = 'Aucun exercice ne correspond à ce filtre.';
    barre.appendChild(vide);
    function appliquer(){
      var b = seg.querySelector('button[aria-pressed="true"]');
      var niv = b ? b.dataset.niveau : 'tous';
      var seulsConcours = !!(puce && puce.getAttribute('aria-pressed') === 'true');
      var vus = 0;
      exos.forEach(function(e){
        var ok = (niv === 'tous' || niveau(e) === niv) && (!seulsConcours || e.classList.contains('concours'));
        e.classList.toggle('filtre-masque', !ok);
        if(ok) vus++;
      });
      info.textContent = vus === exos.length ? exos.length + ' exercices corrigés' : vus + ' exercice' + (vus > 1 ? 's' : '') + ' sur ' + exos.length;
      vide.hidden = vus > 0;
    }
    seg.addEventListener('click', function(e){
      var b = e.target.closest('button');
      if(!b) return;
      seg.querySelectorAll('button').forEach(function(x){ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      appliquer();
    });
    if(puce) puce.addEventListener('click', function(){
      puce.setAttribute('aria-pressed', puce.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      appliquer();
    });
    appliquer();
    panel.insertBefore(barre, panel.firstChild);
  }

  /* ---------- 4. Typographie française et ponctuation collée aux formules ---------- */
  function exclu(el){
    return BALISES_EXCLUES.test(el.nodeName.toUpperCase()) || el.nodeName.toUpperCase().indexOf('MJX-') === 0
      || (el.classList && (el.classList.contains('code-inline') || el.classList.contains('codeblock')));
  }
  function typographier(root){
    var a_traiter = [];
    var w = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, { acceptNode: function(n){
      if(n.nodeType === 1) return exclu(n) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_SKIP;
      return /[;:!?«»]/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
    }});
    while(w.nextNode()) a_traiter.push(w.currentNode);
    a_traiter.forEach(function(t){
      var s = t.nodeValue;
      var r = s.replace(/[  ]+([;!?])/g, ' $1')      // espace fine insécable avant ; ! ?
               .replace(/ +([:»])/g, ' $1')                  // espace insécable avant : et »
               .replace(/« +/g, '« ');                        // et après «
      if(r !== s) t.nodeValue = r;
    });
    // Ponctuation collée à sa formule en ligne : « \(x\). » ne se sépare plus en fin de ligne
    root.querySelectorAll('mjx-container:not([display="true"])').forEach(function(m){
      var p = m.parentNode;
      if(!p || (p.classList && p.classList.contains('mj-colle')) || m.closest('pre, code, button, .codeblock')) return;
      var av = m.previousSibling, ap = m.nextSibling;
      var mAv = av && av.nodeType === 3 ? /[(\[«][  ]?$/.exec(av.nodeValue) : null;
      var mAp = ap && ap.nodeType === 3 ? /^[  ]?[.,;:!?…)\]»]+/.exec(ap.nodeValue) : null;
      if(!mAv && !mAp) return;
      var span = document.createElement('span');
      span.className = 'mj-colle';
      p.insertBefore(span, m);
      if(mAv){ av.nodeValue = av.nodeValue.slice(0, mAv.index); span.appendChild(document.createTextNode(mAv[0])); }
      span.appendChild(m);
      if(mAp){ ap.nodeValue = ap.nodeValue.slice(mAp[0].length); span.appendChild(document.createTextNode(mAp[0])); }
    });
  }

  /* ---------- 5. Formules en ligne plus larges que leur ligne (.mj-large) ---------- */
  function blocParent(el, cache){
    for(var e = el; e && e.nodeType === 1; e = e.parentElement){
      var d = cache.get(e);
      if(d === undefined){ d = getComputedStyle(e).display; cache.set(e, d); }
      if(d !== 'inline' && d !== 'contents') return e;
    }
    return null;
  }
  function marquerLarges(root){
    var cacheD = new Map(), cacheL = new Map(), decisions = [];
    root.querySelectorAll('mjx-container:not([display="true"])').forEach(function(m){
      if(!m.getClientRects().length) return;                       // replié (solution, mémo) : plus tard
      var hote = blocParent(m.parentElement, cacheD);
      if(!hote) return;
      var dispo = cacheL.get(hote);
      if(dispo === undefined){
        var cs = getComputedStyle(hote);
        dispo = hote.clientWidth - (parseFloat(cs.paddingLeft) || 0) - (parseFloat(cs.paddingRight) || 0);
        cacheL.set(hote, dispo);
      }
      var large = m.classList.contains('mj-large');
      var l = m.getBoundingClientRect().width;
      var nat = large ? m.scrollWidth : l;
      // ponctuation collée (.mj-colle, insécable) : elle doit tenir sur la même ligne que la formule
      var p = m.parentNode, colle = 0;
      if(p && p.classList && p.classList.contains('mj-colle')) colle = Math.max(0, p.getBoundingClientRect().width - l);
      decisions.push([m, dispo > 0 && nat + colle > dispo + 1]);
    });
    decisions.forEach(function(x){ x[0].classList.toggle('mj-large', x[1]); });
  }

  /* ---------- 6. Schémas SVG : aucun libellé sous 12 px ----------
     Mesure à l'état naturel ; s'il faut agrandir : .lisible (largeur minimale --svg-min, figure
     élargie jusqu'à la colonne, et au téléphone jusque dans la gouttière), puis .defile (la
     figure défile en largeur) seulement si cela ne suffit pas. */
  function schemasLisibles(root){
    var cadres = Array.prototype.slice.call(root.querySelectorAll('figure.schema, .cine-svg-wrap'))
      .filter(function(c){ return c.querySelector('svg text') && visible(c); });
    if(!cadres.length) return;
    cadres.forEach(function(c){ c.classList.remove('lisible', 'defile'); c.style.removeProperty('--svg-min'); });
    var besoins = cadres.map(function(c){
      var svg = c.querySelector('svg');
      var l = svg.getBoundingClientRect().width;
      if(!l) return 0;
      var mini = Infinity;
      svg.querySelectorAll('text, tspan').forEach(function(t){
        if(!t.firstChild || !t.getClientRects().length) return;
        var fs = parseFloat(getComputedStyle(t).fontSize) || 0, m = t.getScreenCTM && t.getScreenCTM();
        if(!fs || !m) return;
        var px = fs * Math.sqrt(Math.abs(m.a * m.d - m.b * m.c));
        if(px > 0 && px < mini) mini = px;
      });
      return (isFinite(mini) && mini < 12) ? Math.ceil(l * 12.1 / mini) : 0;
    });
    cadres.forEach(function(c, i){
      if(!besoins[i]) return;
      c.classList.add('lisible');
      c.style.setProperty('--svg-min', besoins[i] + 'px');
    });
    var trop = cadres.map(function(c, i){ return besoins[i] && besoins[i] > c.clientWidth + 1; });
    cadres.forEach(function(c, i){ if(trop[i]) c.classList.add('defile'); });
  }

  /* ---------- 7. Simulateurs : curseurs (--p) et valeurs par défaut ---------- */
  function majCurseur(inp){
    var min = inp.min === '' ? 0 : parseFloat(inp.min), max = inp.max === '' ? 100 : parseFloat(inp.max), v = parseFloat(inp.value);
    var p = (max > min && isFinite(v)) ? Math.min(100, Math.max(0, (v - min) / (max - min) * 100)) : 50;
    inp.style.setProperty('--p', p.toFixed(2) + '%');
  }
  function curseurs(root){ root.querySelectorAll('input[type="range"]').forEach(majCurseur); }
  function boutonDefaut(wrap){
    var sc = wrap.querySelector(':scope > .sim-controls');
    if(!sc || sc.querySelector('.sim-reset')) return;
    var champs = Array.prototype.slice.call(sc.querySelectorAll('input, select'));
    if(!champs.length) return;
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'sim-reset';
    b.innerHTML = (window.__icon ? window.__icon('refresh') : '↺') + '<span class="ic-lbl">Valeurs par défaut</span>';
    b.addEventListener('click', function(){
      champs.forEach(function(c){
        var change = false;
        if(c.tagName === 'SELECT'){
          var i = Array.prototype.findIndex.call(c.options, function(o){ return o.defaultSelected; });
          if(i < 0) i = 0;
          if(c.selectedIndex !== i){ c.selectedIndex = i; change = true; }
        } else if(c.type === 'checkbox' || c.type === 'radio'){
          if(c.checked !== c.defaultChecked){ c.checked = c.defaultChecked; change = true; }
        } else if(c.value !== c.defaultValue){ c.value = c.defaultValue; change = true; }
        if(change){
          c.dispatchEvent(new Event('input', { bubbles: true }));
          c.dispatchEvent(new Event('change', { bubbles: true }));
        }
      });
      curseurs(sc);
    });
    sc.appendChild(b);
  }
  document.addEventListener('input', sur(function(e){
    var t = e.target;
    if(t && t.type === 'range') majCurseur(t);
  }), true);
  // Un mode de simulateur peut changer des curseurs par programme : resynchroniser après le clic
  document.addEventListener('click', sur(function(e){
    var w = e.target && e.target.closest && e.target.closest('.sim-wrapper, #lor-simu');
    if(w) raf(sur(function(){ curseurs(w); }));
  }));
  document.addEventListener('change', sur(function(e){
    var w = e.target && e.target.closest && e.target.closest('.sim-wrapper, #lor-simu');
    if(w) raf(sur(function(){ curseurs(w); }));
  }));

  /* ---------- Orchestration ---------- */
  function structurer(panel){
    if(!panel || panel.nodeType !== 1) return;
    if(!panel.__structure){
      panel.__structure = true;
      panel.querySelectorAll('.course-section').forEach(function(cs){
        var s = cs.querySelectorAll(':scope > .sec-num');
        if(s.length === 1) couperSecNum(s[0]);   // plusieurs § dans une section (anglais) : surtitres simples
      });
      panel.querySelectorAll('.exo > .diff').forEach(enrichirDiff);
      outilsExos(panel);
      panel.querySelectorAll('.sim-wrapper').forEach(boutonDefaut);
    }
    curseurs(panel);
  }
  function cleMesure(){ return document.documentElement.clientWidth + 'x' + getComputedStyle(document.documentElement).fontSize; }
  function mesurer(root){
    if(!visible(root)) return;                                     // mesures au prochain affichage
    marquerLarges(root);
    schemasLisibles(root);
    root.__cleMesure = cleMesure();
  }
  function finir(root, forcer){
    if(!root || !root.isConnected) return;
    if(root.matches && root.matches('section.panel')) structurer(root);
    if(forcer || !root.__typo){ root.__typo = true; typographier(root); }
    mesurer(root);
  }
  function panneauxVisibles(){
    return Array.prototype.slice.call(document.querySelectorAll('.chapter.active .panel.active')).filter(visible);
  }
  // Appelé (synchrone) par typesetPanel à chaque affichage d'un panneau
  window.__contenuPanneau = sur(function(panel){
    structurer(panel);
    raf(sur(function(){
      if(!panel.isConnected) return;
      // rendu MathJax terminé (ou panneau déjà composé ailleurs, ex. Formulaire) : finitions
      if(rendus.has(panel) || panel.querySelector('mjx-container')){
        if(!panel.__typo) finir(panel);
        else if(panel.__cleMesure !== cleMesure()) mesurer(panel);
      }
    }));
  });
  // Appelé après un rendu MathJax : panneau, solution dépliée, Formulaire (forcer : contenu reconstruit)
  window.__apresRendu = sur(function(root, opts){
    if(!root) return;
    rendus.add(root);
    raf(sur(function(){ finir(root, !!(opts && opts.forcer)); }));
  });
  // Mémo déplié : ses formules deviennent mesurables
  document.addEventListener('click', sur(function(e){
    var r = e.target && e.target.closest && e.target.closest('.reveal');
    if(r && r.classList.contains('open')) raf(sur(function(){ if(visible(r)){ marquerLarges(r); schemasLisibles(r); } }));
  }));
  // Largeur ou taille du texte (A−/A+) changée : nouvelles mesures du panneau affiché
  var minuterie = null;
  function remesurer(){
    clearTimeout(minuterie);
    minuterie = setTimeout(sur(function(){
      panneauxVisibles().forEach(function(p){ if(p.__typo) mesurer(p); });
    }), 250);
  }
  window.addEventListener('resize', remesurer);
  try { new MutationObserver(remesurer).observe(document.documentElement, { attributes: true, attributeFilter: ['style'] }); } catch(e){ /* sans observateur : mesures au redimensionnement seulement */ }
  // Premier affichage : structurer tout de suite les panneaux actifs (pas de saut de mise en page)
  sur(function(){ document.querySelectorAll('.chapter.active .panel.active').forEach(structurer); })();
})();
</script>
