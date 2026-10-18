/* ============================================================ */
/* ===== NAVIGATION DES CHAPITRES : #mob-drawer ================ */
/* ============================================================ */
/* Même structure partout (SPEC §4.3) : barre latérale permanente à partir de 1200 px
   (repliable par #nav-toggle-btn, clé navCollapsed), tiroir de 768 à 1199 px, page plein
   écran « Chapitres » au téléphone (☰). Contenu : année (clé year) · filtre (toutes
   matières, les deux années, résultats groupés par matière) · Épinglés / Récents (jamais
   filtrés) · intercalaires de matière avec effectif · parties repliables (CHAP_GROUPS,
   clé drawerCollapsed) · rangées = bouton du chapitre + épingle (frères).
   Choisir un chapitre clique TOUJOURS le .chap-btn caché (couche de commande).
   Aussi dans ce module : barre du téléphone (titre, section courante, effacement au
   défilement), feuille ⋯ du téléphone et Sommaire de la matière (#sommaire/<matière>).
   Construction paresseuse : la liste n'est bâtie que si la navigation est visible
   (barre latérale) ou à l'ouverture du tiroir — rien de lourd au chargement du téléphone. */
(function(){
  const MATS = ['physique','maths','si','info','anglais'];
  const MAT_NOMS = { physique:'Physique', maths:'Maths', si:'SI', info:'Info', anglais:'Anglais' };
  const ONGLETS = { cours:'Cours', meth:'Méthodes', simu:'Simulateur', flash:'Cartes', exos:'Exercices' };
  const $ = id => document.getElementById(id);
  const ic = n => (window.__icon ? window.__icon(n) : '');
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const root = document.documentElement;
  const mm = q => (window.matchMedia ? window.matchMedia(q) : { matches:false, addEventListener(){} });
  const mqSide = mm('(min-width:1200px)'), mqTel = mm('(max-width:767px)');

  /* ── Données chapitres (dérivées de CHAPTERS, ordre et parties de CHAP_GROUPS) ── */
  const CHAP_DATA = (function buildChapData(){
    const out = { physique: [], maths: [], si: [], info: [], anglais: [] };
    MATS.forEach(mat => {
      const groups = {};   // subLabel → liste (préserve l'ordre d'apparition)
      const order = [];
      CHAPTERS.filter(c => c.matiere === mat).forEach(c => {
        const key = c.subLabel || '';
        if(!(key in groups)){ groups[key] = []; order.push(key); }
        groups[key].push({ id: 'chap-' + c.id, label: c.mobLabel || c.name, c,
          // year 0 = visible dans les DEUX années (langues + fiches de référence) ;
          // sinon 2 si chapitre de 2ᵉ année (__YEAR2A), 1 par défaut.
          year: (c.matiere === 'anglais' || c.id === 'constantes') ? 0
              : (window.__YEAR2A && window.__YEAR2A.has(c.id)) ? 2 : 1 });
      });
      order.forEach(sub => out[mat].push({ sub, items: groups[sub] }));
    });
    return out;
  })();
  /* 'chap-x' → {item, mat} */
  const CHAP_ITEM_BY_ID = {};
  Object.keys(CHAP_DATA).forEach(m => CHAP_DATA[m].forEach(g => g.items.forEach(it => {
    CHAP_ITEM_BY_ID[it.id] = { item: it, mat: m, sub: g.sub };
  })));

  let currentMat = 'physique';
  let currentYear = (parseInt(Store.get('year')) === 2) ? 2 : 1;
  let drawerOpen = false;
  let aConstruire = true;             // liste à (re)construire à la prochaine apparition
  const deplies1A = new Set();        // parties (mat|partie) où les chapitres de 1ʳᵉ année sont dépliés (2ᵉ année)
  const okYear = it => it.year === currentYear || it.year === 0;

  /* Chapitre affiché (deux .chapter.active au chargement, un par <main> : le visible) */
  function activeChapEl(){
    const l = Array.from(document.querySelectorAll('.chapter.active'));
    return l.find(x => x.offsetParent !== null) || l[0] || null;
  }
  const activeChapId = () => (activeChapEl() || {}).id || '';

  /* ── Année / matières ── */
  function chaptersInYear(mat, year){
    return (CHAP_DATA[mat] || []).some(g => g.items.some(it => it.year === year || it.year === 0));
  }
  function matieresForYear(year){ return MATS.filter(m => chaptersInYear(m, year)); }
  function firstChapInYear(mat, year){
    for(const g of (CHAP_DATA[mat] || [])){
      const it = g.items.find(x => x.year === year || x.year === 0);
      if(it) return it.id;
    }
    return null;
  }
  function effectif(mat){
    let n = 0;
    (CHAP_DATA[mat] || []).forEach(g => g.items.forEach(it => { if(okYear(it)) n++; }));
    return n;
  }
  function refreshYearButtons(){
    document.querySelectorAll('.mob-year-btn').forEach(b => {
      const on = parseInt(b.dataset.year) === currentYear;
      b.classList.toggle('active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }
  function refreshMatButtons(){
    const avail = matieresForYear(currentYear);
    if(!avail.includes(currentMat)) currentMat = avail[0] || currentMat;
    document.querySelectorAll('.mob-mat-btn').forEach(b => {
      const m = b.dataset.mat, on = m === currentMat;
      b.style.display = avail.includes(m) ? '' : 'none';
      b.classList.toggle('active', on);
      b.setAttribute('aria-selected', on ? 'true' : 'false');
      b.tabIndex = on ? 0 : -1;
      const n = b.querySelector('.n');
      if(n) n.textContent = effectif(m);
      b.title = on ? 'Ouvrir le sommaire : ' + MAT_NOMS[m] : MAT_NOMS[m];
    });
    const bar = $('mob-mat-bar');
    if(bar) bar.setAttribute('data-mat', currentMat);
  }

  /* ══ Récents, épinglés, repli des parties ══════════════════════════════
     - Récents (clé 'recents') : 8 derniers chapitres consultés (MRU).
     - Épinglés (clé 'pinned') : 8 favoris ★ au plus.
     - Repli des parties (clé 'drawerCollapsed') : accordéon mémorisé.
     - Anneau de progression (ringSVG) : % de cartes « acquises » (flash:<prefix>) ;
       rendu dans le Bilan seulement (window.__ringSVG), jamais dans la navigation. */
  function getRecents(){ return Store.getJSON('recents', []) || []; }
  function recordRecent(chapId){
    if(!CHAP_ITEM_BY_ID[chapId]) return;
    const r = getRecents().filter(x => x !== chapId);
    r.unshift(chapId);
    Store.setJSON('recents', r.slice(0, 8));
  }
  window.__recordRecent = recordRecent;   // utilisé par l'écran « Aujourd'hui »
  function getPinned(){ return Store.getJSON('pinned', []) || []; }
  function isPinned(id){ return getPinned().includes(id); }
  function togglePin(id){
    const p = getPinned(); const i = p.indexOf(id);
    if(i >= 0) p.splice(i, 1); else p.unshift(id);
    Store.setJSON('pinned', p.slice(0, 8));
  }
  /* API pour les autres modules (intercalaire du chapitre, feuille ⋯) : id 'chap-x' ou 'x' */
  const idChap = id => (String(id || '').indexOf('chap-') === 0 ? String(id) : 'chap-' + id);
  window.__isPinned = id => isPinned(idChap(id));
  window.__togglePin = id => { togglePin(idChap(id)); reconstruire(); return isPinned(idChap(id)); };
  function getCollapsed(){ return Store.getJSON('drawerCollapsed', {}) || {}; }
  function setCollapsed(key, val){
    const c = getCollapsed();
    if(val) c[key] = 1; else delete c[key];
    Store.setJSON('drawerCollapsed', c);
  }
  /* Anneau SVG de progression (% de cartes acquises) — utilisé par le Bilan */
  function ringSVG(pct){
    if(pct === null) return '<span class="mob-ring mob-ring-empty" aria-hidden="true"></span>';
    const r = 6, c = 2 * Math.PI * r;
    const off = (c * (1 - pct / 100)).toFixed(1);
    const cls = pct >= 80 ? 'ok' : pct >= 40 ? 'mid' : pct > 0 ? 'low' : 'zero';
    return `<svg class="mob-ring ${cls}" viewBox="0 0 16 16" aria-hidden="true"><circle class="ring-bg" cx="8" cy="8" r="${r}"/><circle class="ring-fg" cx="8" cy="8" r="${r}" stroke-dasharray="${c.toFixed(1)}" stroke-dashoffset="${off}"/></svg>`;
  }
  window.__ringSVG = ringSVG;

  /* ── Cartes d'un deck : dues (même règle que srsCountDue) et acquises ── */
  function etatDeck(prefix){
    const cards = (window.FLASH_REGISTRY || {})[prefix];
    const r = { tot: Array.isArray(cards) ? cards.length : 0, dues: 0, acq: 0 };
    if(!r.tot) return r;
    const arr = Store.getJSON('flash:' + prefix, null);
    if(!Array.isArray(arr)) return r;
    for(let i = 0; i < r.tot; i++){
      const s = arr[i];
      if(!s || s.last === null || s.last === undefined) continue;
      if(s.last === 2) r.acq++;
      if(typeof srsIsDue === 'function' && srsIsDue(s)) r.dues++;
    }
    return r;
  }
  let cacheEtats = null;   // valable le temps d'une construction
  const etat = prefix => { if(!cacheEtats) cacheEtats = {}; return cacheEtats[prefix] || (cacheEtats[prefix] = etatDeck(prefix)); };
  const libDues = n => n + ' carte' + (n > 1 ? 's' : '') + ' due' + (n > 1 ? 's' : '');
  const libAnnee = y => y === 2 ? '2ᵉ année' : y === 1 ? '1ʳᵉ année' : 'les deux années';

  /* ── Choisir un chapitre : ferme le tiroir / la page, clique le .chap-btn caché ── */
  function ouvrirChapitre(id){
    const chapId = id.replace('chap-', '');
    const cible = idChap(chapId);
    // Page plein écran ouverte : l'entrée d'historique fictive sera REMPLACÉE par le
    // chapitre choisi (au lieu d'être retirée), sauf si l'on reste sur le même chapitre
    if(cible !== activeChapId() && window.__consommerPageFictive) window.__consommerPageFictive();
    fermerSommaire(false);
    const f = $('mob-filter');
    if(f && f.value){ f.value = ''; const cl = $('mob-filter-clear'); if(cl) cl.hidden = true; }
    if(drawerOpen) closeDrawer(true);
    const chapBtn = document.querySelector('.chap-btn[data-chap="' + chapId + '"]');
    if(chapBtn) chapBtn.click();
    updateMobTitle();
    queueSync();
  }

  /* ── Rangée de chapitre : bouton de navigation + bouton épingle (frères, jamais imbriqués) ── */
  function makeChapRow(item, opts){
    opts = opts || {};
    const c = item.c;
    const row = document.createElement('li');
    row.className = 'mob-chap-row';
    row.dataset.id = item.id;
    row.setAttribute('data-mat', c.matiere);   // encre de la matière (jetons --chap*)
    const cur = item.id === opts.actif;
    if(cur) row.classList.add('cur');
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'mob-chap-item' + (cur ? ' active' : '');
    if(cur) btn.setAttribute('aria-current', 'page');
    let html = '<span class="mob-chap-label">' + (opts.labelHtml || esc(item.label)) + '</span>';
    let end = '';
    if(opts.resultat){
      if(item.year === 2) end += '<span class="badge badge-2a" title="2ᵉ année">2ᵉ</span>';
      end += ic('chev-right');
    } else {
      if(item.year === 2 && currentYear === 1) end += '<span class="tag2a" title="2ᵉ année">2A</span>';
      const n = etat(c.prefix).dues;
      if(n) end += '<span class="count count-soft" title="' + libDues(n) + '"><span class="sr">' + libDues(n) + ' : </span>' + n + '</span>';
    }
    if(end) html += '<span class="end">' + end + '</span>';
    if(opts.sub) html += '<span class="sub">' + esc(opts.sub) + '</span>';
    btn.innerHTML = html;
    btn.title = c.name;
    btn.addEventListener('click', () => ouvrirChapitre(item.id));
    row.appendChild(btn);
    if(!opts.resultat){
      const p = isPinned(item.id);
      const pin = document.createElement('button');
      pin.type = 'button';
      pin.className = 'mob-pin' + (p ? ' pinned' : '');
      pin.setAttribute('aria-pressed', p ? 'true' : 'false');
      pin.setAttribute('aria-label', (p ? 'Désépingler ' : 'Épingler ') + item.label);
      pin.title = p ? 'Désépingler' : 'Épingler en tête de la navigation';
      pin.innerHTML = ic(p ? 'star-fill' : 'star');
      pin.addEventListener('click', e => {
        e.stopPropagation();
        togglePin(item.id);
        reconstruire();
        const n = document.querySelector('#mob-chap-list .mob-chap-row[data-id="' + item.id + '"] .mob-pin');
        if(n) n.focus();
      });
      row.appendChild(pin);
    }
    return row;
  }

  /* ── Épinglés et Récents (jamais filtrés ; puces + lignes sur ordinateur, une rangée de puces au téléphone) ── */
  function panneauNom(panelId){ const s = String(panelId || '').split('-').pop(); return ONGLETS[s] || ''; }
  function construireRapides(actif){
    const box = $('mob-quick');
    if(!box) return;
    box.innerHTML = '';
    const pinned = getPinned().map(id => CHAP_ITEM_BY_ID[id]).filter(Boolean);
    const pinIds = getPinned();
    const rec = getRecents().filter(id => !pinIds.includes(id)).map(id => CHAP_ITEM_BY_ID[id]).filter(Boolean).slice(0, 3);
    if(!pinned.length && !rec.length) return;
    const tel = mqTel.matches;
    const puce = (x, icone) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'chip';
      b.setAttribute('data-mat', x.mat);
      b.title = x.item.c.name;
      b.innerHTML = (icone ? icone : '<span class="dot" aria-hidden="true"></span>')
        + '<span class="chip-lbl">' + esc(x.item.label) + '</span>'
        + (x.item.year === 2 && currentYear === 1 ? '<span class="tag2a">2A</span>' : '');
      b.addEventListener('click', () => ouvrirChapitre(x.item.id));
      return b;
    };
    const bloc = titre => {
      const d = document.createElement('div');
      d.className = 'nav-block';
      d.innerHTML = '<div class="kicker">' + titre + '</div>';
      box.appendChild(d);
      return d;
    };
    if(tel){
      const d = bloc(pinned.length && rec.length ? 'Épinglés · Récents' : pinned.length ? 'Épinglés' : 'Récents');
      const ch = document.createElement('div'); ch.className = 'chips';
      pinned.forEach(x => ch.appendChild(puce(x, '<svg class="ic on" aria-hidden="true"><use href="#i-star-fill"></use></svg>')));
      rec.forEach(x => ch.appendChild(puce(x, '<svg class="ic" aria-hidden="true"><use href="#i-clock"></use></svg>')));
      d.appendChild(ch);
      return;
    }
    if(pinned.length){
      const d = bloc('Épinglés');
      const ch = document.createElement('div'); ch.className = 'chips';
      pinned.forEach(x => ch.appendChild(puce(x)));
      d.appendChild(ch);
    }
    if(rec.length){
      const d = bloc('Récents');
      const pos = Store.getJSON('lastPos', null);
      rec.forEach((x, i) => {
        let ou = x.sub || '';
        if(i === 0 && pos && pos.chap === x.item.id && pos.panel){
          ou = panneauNom(pos.panel) + (pos.s ? ' · ' + String(pos.s).split(' ')[0] : '');
        }
        const b = document.createElement('button');
        b.type = 'button';
        b.className = 'recent-row';
        b.setAttribute('data-mat', x.mat);
        b.title = x.item.c.name;
        b.innerHTML = '<span class="dot" aria-hidden="true"></span><span class="nm">' + esc(x.item.label) + '</span>'
          + (ou ? '<span class="where">' + esc(ou) + '</span>' : '');
        b.addEventListener('click', () => ouvrirChapitre(x.item.id));
        d.appendChild(b);
      });
    }
  }

  /* ── Filtre : toutes matières, les deux années, accents ignorés ; résultats groupés
     par matière, correspondance surlignée par <mark> (dans la teinte de la matière) ── */
  const sansAccent = s => String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  function surligner(texte, nq){
    // repère nq (normalisé) dans texte en gardant la correspondance des positions
    let norm = '', pos = [];
    for(let i = 0; i < texte.length; i++){
      const n = sansAccent(texte[i]);
      for(let k = 0; k < n.length; k++){ norm += n[k]; pos.push(i); }
    }
    const j = norm.indexOf(nq);
    if(j < 0) return null;
    const a = pos[j], b = pos[j + nq.length - 1] + 1;
    return esc(texte.slice(0, a)) + '<mark>' + esc(texte.slice(a, b)) + '</mark>' + esc(texte.slice(b));
  }
  function buildFilteredList(list, q){
    const nq = sansAccent(q);
    const groupes = [];
    let total = 0;
    MATS.forEach(m => {
      const lignes = [];
      CHAP_DATA[m].forEach(g => g.items.forEach(it => {
        const hn = surligner(it.c.name, nq);
        const hl = hn ? null : surligner(it.label, nq);
        if(!hn && !hl) return;
        lignes.push({ it, html: hn || hl, sub: (g.sub ? g.sub + ' · ' : '') + libAnnee(it.year) });
      }));
      if(lignes.length){ groupes.push({ m, lignes }); total += lignes.length; }
    });
    list.classList.add('nav-results');
    if(!total){
      const e = document.createElement('div');
      e.className = 'mob-filter-empty';
      e.textContent = 'Aucun chapitre ne correspond à « ' + q + ' ».';
      list.appendChild(e);
      return;
    }
    const k = document.createElement('div');
    k.className = 'kicker';
    k.textContent = total + ' chapitre' + (total > 1 ? 's' : '') + ' · toutes matières, les deux années';
    list.appendChild(k);
    groupes.forEach(gr => {
      const d = document.createElement('div');
      d.className = 'grp';
      d.setAttribute('data-mat', gr.m);
      d.innerHTML = '<div class="grp-h"><span class="dot" aria-hidden="true"></span>' + MAT_NOMS[gr.m] + '<span class="n">' + gr.lignes.length + '</span></div>';
      const ul = document.createElement('ul');
      ul.className = 'nav-list';
      gr.lignes.forEach(l => ul.appendChild(makeChapRow(l.it, { resultat: true, labelHtml: l.html, sub: l.sub })));
      d.appendChild(ul);
      list.appendChild(d);
    });
  }

  /* ── Construire la navigation (si visible ; sinon à la prochaine ouverture) ── */
  const navVisible = () => drawerOpen || (mqSide.matches && !root.classList.contains('nav-replie'));
  function buildDrawerList(mat){
    if(mat) currentMat = mat;
    if(!navVisible()){ aConstruire = true; return; }
    aConstruire = false;
    cacheEtats = null;
    const drawer = $('mob-drawer'), list = $('mob-chap-list');
    if(!list) return;
    list.innerHTML = '';
    list.classList.remove('nav-results');
    const q = ($('mob-filter') || {}).value ? $('mob-filter').value.trim() : '';
    if(drawer) drawer.classList.toggle('filtre-actif', !!q);
    if(q){ buildFilteredList(list, q); cacheEtats = null; return; }
    const actif = activeChapId();
    construireRapides(actif);
    refreshMatButtons();
    const m = currentMat;
    (CHAP_DATA[m] || []).forEach(group => {
      const items = group.items.filter(okYear);
      const autres = currentYear === 2 ? group.items.filter(it => it.year === 1) : [];
      if(!items.length && !autres.length) return;     // partie sans chapitre dans l'année courante
      const collKey = m + '|' + (group.sub || '');
      const collapsed = !!getCollapsed()[collKey];
      const part = document.createElement('div');
      part.className = 'nav-part';
      const h = document.createElement('button');
      h.type = 'button';
      h.className = 'nav-part-h mob-sub-toggle' + (collapsed ? ' collapsed' : '');
      h.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
      h.innerHTML = ic('chev-down') + '<span>' + esc(group.sub || 'Chapitres') + '</span>'
        + (items.length ? '<span class="n">' + items.length + '</span>' : '');
      h.addEventListener('click', () => { setCollapsed(collKey, !collapsed); buildDrawerList(m); });
      part.appendChild(h);
      if(!collapsed){
        const ul = document.createElement('ul');
        ul.className = 'nav-list';
        const deplie = deplies1A.has(collKey) || autres.some(it => it.id === actif);
        group.items.forEach(it => {
          if(okYear(it) || (deplie && it.year === 1 && currentYear === 2)) ul.appendChild(makeChapRow(it, { actif }));
        });
        if(autres.length){
          const li = document.createElement('li');
          const more = document.createElement('button');
          more.type = 'button';
          more.className = 'nav-more';
          more.setAttribute('aria-expanded', deplie ? 'true' : 'false');
          more.innerHTML = deplie ? ic('chev-down') + 'Masquer les chapitres de 1ʳᵉ année'
            : ic('chev-right') + '+ ' + autres.length + ' chapitre' + (autres.length > 1 ? 's' : '') + ' de 1ʳᵉ année';
          more.addEventListener('click', () => {
            if(deplie) deplies1A.delete(collKey); else deplies1A.add(collKey);
            buildDrawerList(m);
          });
          li.appendChild(more);
          ul.appendChild(li);
        }
        part.appendChild(ul);
      }
      list.appendChild(part);
    });
    cacheEtats = null;
    // Chapitre actif au milieu de la zone visible (utile avec plus de cent chapitres)
    const act = list.querySelector('.mob-chap-row.cur');
    const sc = $('mob-drawer-scroll');
    if(act && sc){
      const r = act.getBoundingClientRect(), s = sc.getBoundingClientRect();
      if(r.top < s.top + 40 || r.bottom > s.bottom - 40) sc.scrollTop += (r.top - s.top) - sc.clientHeight / 2;
    }
  }
  function reconstruire(){ aConstruire = true; buildDrawerList(currentMat); }
  window.__majNav = reconstruire;

  /* ── Tuiles de la page Chapitres (téléphone) : Aujourd'hui · Bilan ── */
  function majTuiles(){
    if(!mqTel.matches) return;
    const due = (typeof srsCountDue === 'function') ? srsCountDue() : 0;
    const sub = $('dr-today-sub');
    if(sub) sub.textContent = due ? libDues(due) + ' · ≈ ' + Math.max(1, Math.round(due * 20 / 60)) + ' min' : 'Aucune carte due';
    const b = $('rev-badge-tile');
    if(b){ b.textContent = due > 99 ? '99+' : String(due); b.hidden = !due; }
    let acq = 0, tot = 0;
    const y = window.__currentYear ? window.__currentYear() : 1;
    CHAPTERS.forEach(c => {
      if(!c.panels.includes('flash')) return;
      if(window.__inRevision && !window.__inRevision(c, y)) return;
      const e = etatDeck(c.prefix); acq += e.acq; tot += e.tot;
    });
    const d = $('dr-dash-sub');
    if(d) d.textContent = tot ? Math.round(acq / tot * 100) + ' % des cartes acquises' : 'Progression des cartes';
  }

  /* ── Filtre instantané ── */
  (function(){
    const input = $('mob-filter');
    const clear = $('mob-filter-clear');
    if(!input) return;
    input.placeholder = 'Filtrer les ' + CHAPTERS.length + ' chapitres';
    input.addEventListener('input', () => {
      if(clear) clear.hidden = !input.value;
      buildDrawerList(currentMat);
    });
    input.addEventListener('keydown', e => {
      if(e.key === 'Escape' && input.value){
        e.stopPropagation();
        input.value = '';
        if(clear) clear.hidden = true;
        buildDrawerList(currentMat);
      } else if(e.key === 'Enter'){
        const first = document.querySelector('#mob-chap-list .mob-chap-item');
        if(first) first.click();
      }
    });
    if(clear) clear.addEventListener('click', () => {
      input.value = '';
      clear.hidden = true;
      buildDrawerList(currentMat);
      input.focus();
    });
  })();

  /* ── Ouvrir / fermer le tiroir (ou la page Chapitres) ; replier la barre latérale ── */
  const navToggle = $('nav-toggle-btn');
  function majBoutons(){
    const lat = mqSide.matches, replie = root.classList.contains('nav-replie');
    if(navToggle){
      const ouvert = lat ? !replie : drawerOpen;
      navToggle.setAttribute('aria-expanded', ouvert ? 'true' : 'false');
      const t = lat ? (replie ? 'Afficher la navigation des chapitres' : 'Masquer la navigation des chapitres') : 'Chapitres';
      navToggle.title = t; navToggle.setAttribute('aria-label', t);
    }
    const mb = $('mob-menu-btn');
    if(mb) mb.setAttribute('aria-expanded', drawerOpen ? 'true' : 'false');
  }
  function currentToggle(){ return window.innerWidth >= 768 ? navToggle : $('mob-menu-btn'); }
  function openDrawer(){
    if(mqSide.matches){ setReplie(false); return; }
    drawerOpen = true;
    const drawer = $('mob-drawer');
    drawer.classList.add('open');
    $('mob-drawer-overlay').classList.add('open');
    buildDrawerList(currentMat);
    majTuiles();
    majBoutons();
    const sc = $('mob-drawer-scroll');
    if(sc && mqTel.matches && !$('mob-filter').value) sc.scrollTop = 0;
    // Focus dans le tiroir (sur le bouton fermer)
    const closeBtn = $('mob-drawer-close');
    if(closeBtn) setTimeout(() => { try{ closeBtn.focus({ preventScroll:true }); }catch(e){ closeBtn.focus(); } }, 30);
  }
  function closeDrawer(sansFocus){
    if(!drawerOpen) return;
    drawerOpen = false;
    $('mob-drawer').classList.remove('open');
    $('mob-drawer-overlay').classList.remove('open');
    majBoutons();
    // Rendre le focus au bouton d'ouverture (différé pour passer après le clic)
    const opener = currentToggle();
    if(opener && !sansFocus) setTimeout(() => opener.focus(), 0);
  }
  function setReplie(v){
    root.classList.toggle('nav-replie', !!v);
    Store.set('navCollapsed', v ? '1' : '0');
    majBoutons();
    if(!v) buildDrawerList(currentMat);
  }
  /* Piège de focus : tant que le tiroir est ouvert, Tab boucle à l'intérieur */
  $('mob-drawer').addEventListener('keydown', e => {
    if(e.key !== 'Tab' || !drawerOpen) return;
    const focusables = Array.from($('mob-drawer')
      .querySelectorAll('button:not([disabled]), input, [href], [tabindex]:not([tabindex="-1"])'))
      .filter(x => x.getClientRects().length);
    if(!focusables.length) return;
    const first = focusables[0], last = focusables[focusables.length - 1];
    if(e.shiftKey && document.activeElement === first){ e.preventDefault(); last.focus(); }
    else if(!e.shiftKey && document.activeElement === last){ e.preventDefault(); first.focus(); }
  });
  $('mob-menu-btn').addEventListener('click', openDrawer);
  if(navToggle) navToggle.addEventListener('click', () => {
    if(mqSide.matches) setReplie(!root.classList.contains('nav-replie'));
    else if(drawerOpen) closeDrawer(); else openDrawer();
  });
  $('mob-drawer-close').addEventListener('click', () => closeDrawer());
  $('mob-drawer-overlay').addEventListener('click', () => closeDrawer());
  document.addEventListener('keydown', e => { if(e.key === 'Escape' && drawerOpen) closeDrawer(); });
  const surChangementLargeur = () => {
    if(mqSide.matches && drawerOpen) closeDrawer(true);
    majBoutons();
    if(navVisible()) buildDrawerList(currentMat);
    rendreBarre(true);
  };
  if(mqSide.addEventListener) mqSide.addEventListener('change', surChangementLargeur);
  if(mqTel.addEventListener) mqTel.addEventListener('change', surChangementLargeur);

  /* Tuiles */
  $('dr-today-tile') && $('dr-today-tile').addEventListener('click', () => {
    if(window.__consommerPageFictive) window.__consommerPageFictive(true);
    closeDrawer(true);
    if(window.todayOpen) window.todayOpen();
  });
  $('dr-dash-tile') && $('dr-dash-tile').addEventListener('click', () => {
    if(window.__consommerPageFictive) window.__consommerPageFictive(true);
    closeDrawer(true);
    const b = $('dash-btn') || $('mob-dash-btn');
    if(b) b.click();
  });

  /* ── Swipe pour ouvrir le tiroir depuis le bord gauche ── */
  let swipeStartX = 0, swipeStartY = 0, swipeBlocked = false;
  // Le swipe ne doit PAS se déclencher quand on manipule un curseur, un
  // sélecteur, un bouton ou un simulateur (sinon glisser un slider au doigt
  // ferait changer de page). On neutralise le geste dans ces zones.
  const SWIPE_IGNORE = 'input,select,button,textarea,canvas,.sim-controls,.sim-wrapper,.control,a';
  document.addEventListener('touchstart', e => {
    swipeStartX = e.touches[0].clientX;
    swipeStartY = e.touches[0].clientY;
    swipeBlocked = !!(e.target && e.target.closest && e.target.closest(SWIPE_IGNORE));
  }, {passive:true});
  document.addEventListener('touchend', e => {
    if(swipeBlocked){ swipeBlocked = false; return; }
    if(mqSide.matches) return;
    const dx = e.changedTouches[0].clientX - swipeStartX;
    const dy = Math.abs(e.changedTouches[0].clientY - swipeStartY);
    // Swipe droit depuis bord gauche → ouvrir ; swipe gauche → fermer
    if(!drawerOpen && swipeStartX < 28 && dx > 55 && dy < 60) openDrawer();
    if(drawerOpen && dx < -55 && dy < 60) closeDrawer();
  }, {passive:true});

  /* ── Année : 1ʳᵉ / 2ᵉ (ouvre le 1ᵉʳ chapitre de l'année dans la matière courante) ── */
  function setYear(y){
    currentYear = (y === 2) ? 2 : 1;
    Store.set('year', String(currentYear));
    refreshYearButtons();
    refreshMatButtons();
  }
  document.querySelectorAll('.mob-year-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const y = (parseInt(btn.dataset.year) === 2) ? 2 : 1;
      if(y === currentYear && !sommaireOuvert) return;
      setYear(y);
      if(sommaireOuvert){ rendreSommaire(currentMat); buildDrawerList(currentMat); return; }
      buildDrawerList(currentMat);
      const id = firstChapInYear(currentMat, currentYear);
      if(id){
        const cb = document.querySelector('.chap-btn[data-chap="' + id.replace('chap-', '') + '"]');
        if(cb) cb.click();
        updateMobTitle();
      }
    });
  });

  /* ── Intercalaires de matière : parcourir sans naviguer ; un 2ᵉ clic sur l'actif
     ouvre le Sommaire de la matière ── */
  document.querySelectorAll('.mob-mat-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const m = btn.dataset.mat;
      if(m === currentMat && btn.classList.contains('active')){ ouvrirSommaire(m); return; }
      currentMat = m;
      buildDrawerList(currentMat);
    });
  });
  // Clavier : ← → entre les intercalaires (role=tablist)
  $('mob-mat-bar') && $('mob-mat-bar').addEventListener('keydown', e => {
    if(e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    const tabs = Array.from(document.querySelectorAll('.mob-mat-btn')).filter(b => b.style.display !== 'none');
    const i = tabs.indexOf(document.activeElement);
    if(i < 0) return;
    e.preventDefault();
    const t = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
    t.click(); t.focus();
  });

  /* ══ Barre du téléphone (SPEC §4.2) ══════════════════════════════════════
     Au repos (haut de page) : « ● Matière · partie · année » + titre complet (2 lignes).
     Au défilement : la barre s'efface quand on descend (> 8 px, au-delà de 120 px) et
     revient au moindre geste vers le haut avec « Chapitre · onglet » + la section
     courante (scroll-spy du sommaire : window.__surSection). Un seul écouteur scroll
     passif, regroupé par requestAnimationFrame. */
  const barre = $('mob-header');
  const etatBarre = { c: null, section: null, cle: '' };
  function casPhrase(t, sec){
    t = String(t || '').replace(/\s+/g, ' ').trim();
    if(!t || /[a-zà-öø-ÿ]/.test(t)) return t;            // déjà en casse normale
    const ref = sec ? ((sec.querySelector('h2') || {}).textContent || '') : '';
    const sigles = new Set(ref.split(/[^A-Za-zÀ-ÖØ-Ý0-9]+/).filter(w => w.length > 1 && /[A-Z]/.test(w) && w === w.toUpperCase()));
    const s = t.split(' ').map(w => { const k = w.replace(/[^A-Za-zÀ-ÖØ-Ý0-9]/g, ''); return sigles.has(k) ? w : w.toLowerCase(); }).join(' ');
    return s.charAt(0).toUpperCase() + s.slice(1);
  }
  function rendreBarre(force){
    if(!barre) return;
    const k = $('mob-bar-k'), h = $('mob-chapter-title');
    if(!k || !h) return;
    let cle, kh, hh, mat;
    if(sommaireOuvert){
      mat = sommaireOuvert;
      cle = 'S|' + mat + '|' + currentYear;
      kh = '<span class="dot" aria-hidden="true"></span><b>' + MAT_NOMS[mat] + '</b><span>·</span><span>' + (currentYear === 2 ? '2ᵉ' : '1ʳᵉ') + ' année</span>';
      hh = 'Sommaire de la matière';
    } else {
      const c = etatBarre.c;
      if(!c) return;
      mat = c.matiere;
      const sec = etatBarre.section;
      const enSection = !!(sec && (window.scrollY || 0) > 120);
      const ch = activeChapEl(), p = ch && ch.querySelector('.panel.active');
      const ong = p ? panneauNom(p.id) : '';
      if(enSection){
        cle = 'C|' + c.id + '|' + ong + '|' + sec.id;
        kh = '<span class="dot" aria-hidden="true"></span><span class="chap">' + esc(c.mobLabel || c.name) + '</span>' + (ong ? '<span>·</span><span>' + ong + '</span>' : '');
        hh = (sec.n ? '<span class="sn">' + esc(sec.n) + '</span>' : '') + esc(sec.t);
      } else {
        const yr = window.__chapYear ? window.__chapYear(c) : 1;
        cle = 'R|' + c.id;
        kh = '<span class="dot" aria-hidden="true"></span><b>' + MAT_NOMS[mat] + '</b>'
          + (c.subLabel ? '<span>·</span><span class="part">' + esc(c.subLabel) + '</span>' : '')
          + (yr ? '<span>·</span><span>' + (yr === 2 ? '2ᵉ' : '1ʳᵉ') + '</span>' : '');
        hh = esc(c.name);
      }
    }
    if(cle === etatBarre.cle && !force) return;
    etatBarre.cle = cle;
    barre.setAttribute('data-mat', mat);
    k.innerHTML = kh;
    h.innerHTML = hh;
  }
  /* ── Titre dynamique de la barre du téléphone (chapitre affiché) ── */
  function updateMobTitle(){
    const ch = activeChapEl();
    if(!ch) return;
    const c = CHAPTERS_BY_ID[ch.id.replace('chap-', '')];
    if(!c) return;
    if(etatBarre.c !== c) etatBarre.section = null;
    etatBarre.c = c;
    rendreBarre();
  }
  // Section courante (appelé par le scroll-spy du sommaire interne) → barre + lastPos.s
  window.__surSection = function(sec){
    try {
      const ch = sec && sec.closest('.chapter');
      if(!ch || ch !== activeChapEl()) return;
      const lab = sec.dataset.tocLabel || '';
      const m = lab.match(/^(§\s*\d+[a-z]?)\s*[·:\-–—.]?\s*(.*)$/i);
      const s = { id: sec.id, n: m ? m[1].replace(/\s+/g, '') : '', t: casPhrase(m ? m[2] : lab, sec) };
      if(etatBarre.section && etatBarre.section.id === s.id) return;
      etatBarre.section = s;
      rendreBarre();
      // « Reprendre · Cours · §3 Régime libre » (Récents, Sommaire) : section dans lastPos
      const pos = Store.getJSON('lastPos', null);
      const p = sec.closest('.panel');
      if(pos && pos.chap === ch.id && p && pos.panel === p.id){
        const lib = (s.n ? s.n + ' ' : '') + s.t;
        if(pos.s !== lib){ pos.s = lib; pos.t = Date.now(); Store.setJSON('lastPos', pos); }
      }
    } catch(e){}
  };
  // Effacement au défilement (téléphone)
  let dernierY = window.scrollY || 0, tic = false;
  function majDefilement(){
    tic = false;
    if(!barre) return;
    const y = Math.max(0, window.scrollY || 0);
    let cachee = barre.classList.contains('cachee');
    if(!mqTel.matches || y <= 120){ cachee = false; dernierY = y; }
    else if(y - dernierY > 8){ cachee = true; dernierY = y; }
    else if(y < dernierY){ cachee = false; dernierY = y; }
    if(cachee !== barre.classList.contains('cachee')){
      barre.classList.toggle('cachee', cachee);
      root.classList.toggle('mbar-cachee', cachee);
    }
    if(mqTel.matches) rendreBarre();
  }
  window.addEventListener('scroll', () => { if(!tic){ tic = true; requestAnimationFrame(majDefilement); } }, { passive:true });
  // Changement d'onglet : la section courante sera redonnée par le scroll-spy
  document.addEventListener('click', e => {
    if(e.target && e.target.closest && e.target.closest('.tab')){ etatBarre.section = null; setTimeout(() => rendreBarre(), 0); }
  });

  /* ══ Sommaire de la matière (SPEC §4.3 point 8) : table des matières d'un livre ══
     Rendu dans la zone de la feuille (#sommaire-matiere), lien profond #sommaire/<matière>
     (urlRouting). Ouvert par un 2ᵉ clic sur l'intercalaire actif, ou window.__ouvrirSommaire
     (nom de la matière du fil d'Ariane). Fermé par tout changement de chapitre (.chap-btn). */
  let sommaireOuvert = null;
  function quand(t){
    if(!t) return '';
    const d = new Date(t), j = new Date(); j.setHours(0, 0, 0, 0);
    const h = d.getHours() + ' h ' + String(d.getMinutes()).padStart(2, '0');
    const jour = new Date(d); jour.setHours(0, 0, 0, 0);
    const ecart = Math.round((j - jour) / 86400000);
    if(ecart === 0) return 'aujourd\'hui, ' + h;
    if(ecart === 1) return 'hier, ' + h;
    try { return d.toLocaleDateString('fr-FR', { weekday:'long', day:'numeric', month:'short' }) + ', ' + h; }
    catch(e){ return d.toLocaleDateString() + ', ' + h; }
  }
  function rendreSommaire(mat){
    const box = $('sommaire-matiere');
    if(!box) return;
    cacheEtats = null;
    const actif = activeChapId();
    const parties = [];
    let nChap = 0, dues = 0, acq = 0, tot = 0, autreAnnee = 0;
    (CHAP_DATA[mat] || []).forEach(g => {
      const items = g.items.filter(okYear);
      autreAnnee += g.items.length - items.length;
      if(!items.length) return;
      let pd = 0, pa = 0, pt = 0;
      items.forEach(it => { const e = etat(it.c.prefix); pd += e.dues; pa += e.acq; pt += e.tot; });
      parties.push({ g, items, pd, pa, pt });
      nChap += items.length; dues += pd; acq += pa; tot += pt;
    });
    const pct = (a, t) => t ? Math.round(a / t * 100) : 0;
    let html = '<div class="sommaire-feuille" data-mat="' + mat + '"><div class="ov-head">'
      + '<div class="ov-crumb"><span class="dot" aria-hidden="true"></span><b>Sommaire de la matière</b><span>·</span><span>' + libAnnee(currentYear) + '</span></div>'
      + '<h2 class="ov-h">' + MAT_NOMS[mat] + '</h2>'
      + '<div class="ov-meta">' + parties.length + ' partie' + (parties.length > 1 ? 's' : '') + ' · ' + nChap + ' chapitre' + (nChap > 1 ? 's' : '')
      + (dues ? ' · <b>' + libDues(dues) + '</b>' : '') + (tot ? ' · ' + pct(acq, tot) + ' % des cartes acquises' : '') + '</div>';
    const pos = Store.getJSON('lastPos', null);
    const rp = pos && pos.chap && CHAP_ITEM_BY_ID[pos.chap];
    if(rp && rp.mat === mat){
      const sn = pos.s ? String(pos.s).split(' ')[0] : '';
      const s = [panneauNom(pos.panel), pos.s || '', quand(pos.t)].filter(Boolean).join(' · ');
      html += '<button type="button" class="ov-resume" data-chap="' + esc(pos.chap) + '" data-panel="' + esc(pos.panel || '') + '">'
        + '<span class="pic" aria-hidden="true">' + esc(/^§\d/.test(sn) ? sn : '§') + '</span>'
        + '<span class="tx"><span class="t">Reprendre : ' + esc(rp.item.c.name) + '</span>' + (s ? '<span class="s">' + esc(s) + '</span>' : '') + '</span>'
        + ic('chev-right') + '</button>';
    }
    html += '</div><div class="ov-grid">';
    parties.forEach(p => {
      html += '<section class="pcard"><div class="pcard-h"><h3>' + esc(p.g.sub || 'Chapitres') + '</h3><span class="pcard-n">' + p.items.length + ' chapitre' + (p.items.length > 1 ? 's' : '') + '</span></div>';
      if(p.pt) html += '<div class="pcard-p"><div class="stack" role="img" aria-label="' + pct(p.pa, p.pt) + ' % des cartes acquises"><i class="s2" style="width:' + pct(p.pa, p.pt) + '%"></i></div>'
        + '<span>' + pct(p.pa, p.pt) + ' % acquis' + (p.pd ? ' · <b>' + p.pd + ' due' + (p.pd > 1 ? 's' : '') + '</b>' : '') + '</span></div>';
      html += '<ol class="pcard-list">';
      p.items.forEach(it => {
        const e = etat(it.c.prefix);
        html += '<li><button type="button" data-chap="' + it.id + '"' + (it.id === actif ? ' class="cur" aria-current="page"' : '') + '>' + esc(it.c.name) + '</button>'
          + (it.c.drawFn ? '<span class="simu" title="Simulateur">' + ic('wave') + '<span class="sr">simulateur</span></span>' : '')
          + (e.dues ? '<span class="count count-soft" title="' + libDues(e.dues) + '">' + e.dues + '</span>' : '') + '</li>';
      });
      html += '</ol></section>';
    });
    html += '</div>';
    if(autreAnnee){
      const autre = currentYear === 1 ? 2 : 1;
      html += '<div class="ov-2a"><span>' + autreAnnee + ' chapitre' + (autreAnnee > 1 ? 's' : '') + ' de ' + libAnnee(autre) + ' en ' + MAT_NOMS[mat].toLowerCase()
        + (autre === 2 ? ' (PT) : ils s\'ajoutent en 2ᵉ année.' : ' : révisés aussi en 2ᵉ année.') + '</span>'
        + '<button type="button" class="btn" data-annee="' + autre + '">Voir la ' + libAnnee(autre) + '</button></div>';
    }
    html += '</div>';
    box.innerHTML = html;
    cacheEtats = null;
    box.querySelectorAll('.pcard-list button[data-chap]').forEach(b => b.addEventListener('click', () => ouvrirChapitre(b.dataset.chap)));
    const rs = box.querySelector('.ov-resume');
    if(rs) rs.addEventListener('click', () => {
      const ch = rs.dataset.chap, pa = rs.dataset.panel;
      fermerSommaire(false);
      if(typeof navigateTo === 'function') navigateTo(ch, pa || null);
    });
    const an = box.querySelector('.ov-2a .btn');
    if(an) an.addEventListener('click', () => { setYear(parseInt(an.dataset.annee)); rendreSommaire(mat); buildDrawerList(currentMat); rendreBarre(true); });
  }
  function ouvrirSommaire(mat, depuisUrl){
    if(!CHAP_DATA[mat]) return false;
    if(!chaptersInYear(mat, currentYear)) setYear(currentYear === 1 ? 2 : 1);
    if(drawerOpen){
      if(window.__consommerPageFictive) window.__consommerPageFictive();
      closeDrawer(true);
    }
    sommaireOuvert = mat;
    currentMat = mat;
    rendreSommaire(mat);
    $('sommaire-matiere').hidden = false;
    root.classList.add('sommaire-ouvert');
    if(typeof scrollPageTop === 'function') scrollPageTop();
    buildDrawerList(currentMat);
    rendreBarre(true);
    if(!depuisUrl && window.__syncHash) window.__syncHash();
    return true;
  }
  function fermerSommaire(majUrl){
    if(!sommaireOuvert) return;
    sommaireOuvert = null;
    const box = $('sommaire-matiere');
    if(box){ box.hidden = true; box.innerHTML = ''; }
    root.classList.remove('sommaire-ouvert');
    etatBarre.cle = '';
    updateMobTitle();
    if(majUrl !== false && window.__syncHash) window.__syncHash();
  }
  window.__ouvrirSommaire = ouvrirSommaire;
  window.__fermerSommaire = fermerSommaire;
  window.__sommaireOuvert = () => sommaireOuvert;
  // Tout changement de chapitre (clic réel ou programmatique sur .chap-btn) ferme le sommaire
  document.addEventListener('click', e => {
    if(sommaireOuvert && e.target && e.target.closest && e.target.closest('.chap-btn')) fermerSommaire(false);
  }, true);

  /* ── Synchroniser la navigation avec le chapitre actif ── */
  function syncSidebar(){
    const activeChap = activeChapEl();
    if(activeChap){
      const c = CHAPTERS_BY_ID[activeChap.id.replace('chap-', '')];
      if(c){
        // Chapitres des deux années (anglais, constantes) : l'année courante reste. Un
        // chapitre de 2ᵉ année ouvert en 1ʳᵉ année fait passer en 2ᵉ année ; un chapitre
        // de 1ʳᵉ année ouvert en 2ᵉ année y reste (sa partie se déplie : « + N chapitres
        // de 1ʳᵉ année »), car la 2ᵉ année révise tout le programme.
        const bothYears = (c.matiere === 'anglais' || c.id === 'constantes');
        const y = (window.__YEAR2A && window.__YEAR2A.has(c.id)) ? 2 : 1;
        if(!bothYears && y === 2 && currentYear !== 2){ currentYear = 2; Store.set('year', '2'); refreshYearButtons(); }
        if(c.matiere !== currentMat) currentMat = c.matiere;
        recordRecent(activeChap.id);   // historique « Récents » + écran Aujourd'hui
      }
    }
    refreshMatButtons();
    buildDrawerList(currentMat);
    updateMobTitle();
  }
  let syncQueued = false;
  function queueSync(){
    if(syncQueued) return;
    syncQueued = true;
    // setTimeout plutôt que requestAnimationFrame : rAF se met en pause dans les
    // onglets en arrière-plan, ce qui désynchroniserait la navigation.
    setTimeout(() => { syncQueued = false; syncSidebar(); }, 0);
  }

  /* ── Boutons de la barre du téléphone → fonctions de l'en-tête ── */
  $('mob-search-btn').addEventListener('click', () => { $('search-btn').click(); });
  $('mob-quiz-btn').addEventListener('click', () => { $('quiz-btn').click(); });

  /* ── Feuille « ⋯ » du téléphone : monte du bas, à la demande (une modale) ── */
  (function(){
    const btn = $('mob-more-btn'), menu = $('mob-more-menu'), voile = $('mob-more-scrim');
    if(!btn || !menu) return;
    let opener = null;
    const majEpingle = () => {
      const b = $('mob-pin-btn'); if(!b) return;
      const id = activeChapId(), p = id && isPinned(id);
      b.setAttribute('aria-pressed', p ? 'true' : 'false');
      const l = b.querySelector('.ic-lbl'); if(l) l.textContent = p ? 'Désépingler ce chapitre' : 'Épingler ce chapitre';
      const u = b.querySelector('use'); if(u) u.setAttribute('href', p ? '#i-star-fill' : '#i-star');
    };
    function open(){
      majEpingle();
      opener = document.activeElement;
      menu.classList.add('open');
      if(voile){ voile.hidden = false; requestAnimationFrame(() => voile.classList.add('open')); }
      btn.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
      const f = menu.querySelector('.menu-item');
      if(f) setTimeout(() => { try{ f.focus({ preventScroll:true }); }catch(e){ f.focus(); } }, 60);
    }
    function close(rendre){
      if(!menu.classList.contains('open')) return;
      menu.classList.remove('open');
      if(voile){ voile.classList.remove('open'); voile.hidden = true; }
      btn.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      if(rendre !== false && opener && opener.getClientRects && opener.getClientRects().length) try{ opener.focus({ preventScroll:true }); }catch(e){}
    }
    btn.addEventListener('click', e => {
      e.stopPropagation();
      if(menu.classList.contains('open')) close(); else open();
    });
    // Les actions ferment la feuille ; les segmentés (thème, taille du texte) la laissent ouverte
    menu.querySelectorAll('.menu-item').forEach(it => it.addEventListener('click', () => close(false)));
    const pinB = $('mob-pin-btn');
    if(pinB) pinB.addEventListener('click', () => { const id = activeChapId(); if(id){ togglePin(id); reconstruire(); } });
    if(voile) voile.addEventListener('click', () => close());
    document.addEventListener('keydown', e => { if(e.key === 'Escape') close(); });
    // Piège du focus dans la feuille
    menu.addEventListener('keydown', e => {
      if(e.key !== 'Tab') return;
      const f = Array.from(menu.querySelectorAll('button:not([disabled])')).filter(x => x.getClientRects().length);
      if(!f.length) return;
      const a = f[0], z = f[f.length - 1];
      if(e.shiftKey && document.activeElement === a){ e.preventDefault(); z.focus(); }
      else if(!e.shiftKey && document.activeElement === z){ e.preventDefault(); a.focus(); }
    });
    window.__fermerFeuillePlus = close;
  })();

  /* ── Init ── */
  refreshYearButtons();
  refreshMatButtons();
  majBoutons();
  syncSidebar();

  // Observer les changements de chapitre actif pour resynchroniser la navigation
  const chapObs = new MutationObserver(() => queueSync());
  document.querySelectorAll('.chapter').forEach(ch => {
    chapObs.observe(ch, {attributes:true, attributeFilter:['class']});
  });
  // Les compteurs des rangées suivent les révisions (appelé par __updateReviseBadge)
  window.__majNavCompteurs = () => { if(navVisible()) reconstruire(); else aConstruire = true; };
})();
