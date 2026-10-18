/* Préférence (clé 'theme') : 'light' | 'dark' | 'auto' (défaut, et ancienne
   valeur absente) = suit le réglage clair/sombre de l'appareil, EN CONTINU.
   Le thème effectif reste exprimé par data-theme="dark" sur <html> (seul
   sélecteur du CSS sombre, lu par getCanvasColors/__CV) ; data-theme-pref
   porte la préférence. Déjà posé avant l'affichage par le script du <head>.
   Sélecteur explicite (SPEC §4.6) : sur ordinateur, #theme-btn ouvre le popover
   #theme-pop (3 cartes Clair / Sombre / Auto + taille du texte) ; au téléphone,
   segmenté en bas de la feuille ⋯. Tout bouton [data-theme-set] appelle setTheme ;
   la mention « actuellement : … » suit le réglage de l'appareil (même matchMedia).
   API : window.__themePref(), window.__setTheme(pref). */
(function(){
  const root = document.documentElement;
  const btn = document.getElementById('theme-btn');
  const pop = document.getElementById('theme-pop');
  const mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  const NOMS = { light:'Clair', dark:'Sombre', auto:'Auto' };
  const themePref = () => { const t = Store.get('theme'); return (t === 'light' || t === 'dark') ? t : 'auto'; };
  const estSombre = pref => pref === 'dark' || (pref === 'auto' && !!(mq && mq.matches));
  /* Barre du navigateur : les deux <meta name="theme-color"> du <head> portent la
     couleur de la feuille (--sheet) en clair et en sombre, chacune pour son
     media système. Préférence explicite : les deux prennent la couleur du thème
     choisi ; Auto : chacune retrouve la sienne. (Valeurs relues dans le HTML,
     sans getComputedStyle au chargement.) */
  const metasTheme = Array.from(document.querySelectorAll('meta[name="theme-color"]'));
  const couleurMeta = new Map(metasTheme.map(m => [m, m.getAttribute('content')]));
  const metaDe = sch => metasTheme.find(m => (m.getAttribute('media') || '').indexOf(sch) >= 0);
  function majThemeColor(pref){
    if(!metasTheme.length) return;
    const ref = pref === 'auto' ? null : metaDe(pref === 'dark' ? 'dark' : 'light');
    metasTheme.forEach(m => {
      const c = ref ? couleurMeta.get(ref) : couleurMeta.get(m);
      if(c && m.getAttribute('content') !== c) m.setAttribute('content', c);
    });
  }
  /* Choix coché (cartes du popover, segmenté de la feuille ⋯) et « actuellement » */
  function majControles(pref){
    document.querySelectorAll('[data-theme-set]').forEach(b =>
      b.setAttribute('aria-checked', b.getAttribute('data-theme-set') === pref ? 'true' : 'false'));
    const appareil = (mq && mq.matches) ? 'sombre' : 'clair';
    document.querySelectorAll('.theme-actuel').forEach(e => { if(e.textContent !== appareil) e.textContent = appareil; });
    const t = 'Thème : ' + NOMS[pref] + (pref === 'auto' ? ' (actuellement ' + appareil + ')' : '');
    if(btn){ btn.title = t; btn.setAttribute('aria-label', t); }
  }
  function applyTheme(pref){
    const avant = root.getAttribute('data-theme') === 'dark';
    const sombre = estSombre(pref);
    if(sombre) root.setAttribute('data-theme','dark'); else root.removeAttribute('data-theme');
    root.setAttribute('data-theme-pref', pref);
    try{ majThemeColor(pref); }catch(e){}
    majControles(pref);
    // redessiner les canvas (couleurs dépendantes du thème) si l'écran a changé
    if(avant !== sombre) setTimeout(()=>{ try{
      const a = Array.from(document.querySelectorAll('.chapter.active')).find(x => x.offsetParent !== null);
      if(a) redrawChapter(a.id.replace('chap-',''));
    }catch(e){} }, 50);
  }
  function setTheme(pref){
    if(pref !== 'light' && pref !== 'dark') pref = 'auto';
    Store.set('theme', pref);
    applyTheme(pref);
  }
  applyTheme(themePref());
  if(mq){
    const surChangement = () => { const p = themePref(); if(p === 'auto') applyTheme('auto'); else majControles(p); };
    if(mq.addEventListener) mq.addEventListener('change', surChangement);
    else if(mq.addListener) mq.addListener(surChangement);
  }

  /* Popover de l'en-tête : Échap, clic dehors ou choix d'un thème le ferment */
  const ouvert = () => !!(pop && !pop.hidden);
  function ouvrirPop(){
    if(!pop || !btn) return;
    pop.hidden = false;
    btn.setAttribute('aria-expanded', 'true');
    const c = pop.querySelector('.theme-opt[aria-checked="true"]') || pop.querySelector('.theme-opt');
    if(c) setTimeout(() => { try{ c.focus({ preventScroll:true }); }catch(e){ c.focus(); } }, 30);
  }
  function fermerPop(rendreFocus){
    if(!ouvert()) return;
    pop.hidden = true;
    btn.setAttribute('aria-expanded', 'false');
    if(rendreFocus) btn.focus();
  }
  if(btn) btn.addEventListener('click', e => { e.stopPropagation(); if(ouvert()) fermerPop(); else ouvrirPop(); });
  document.addEventListener('click', e => {
    const b = e.target && e.target.closest ? e.target.closest('[data-theme-set]') : null;
    if(b){ setTheme(b.getAttribute('data-theme-set')); if(pop && pop.contains(b)) fermerPop(true); return; }
    if(ouvert() && !pop.contains(e.target) && e.target !== btn) fermerPop();
  });
  if(pop) pop.addEventListener('keydown', e => {
    if(e.key === 'Escape'){ e.stopPropagation(); fermerPop(true); return; }
    // Flèches : d'une carte à l'autre (groupe radio), puis Entrée / Espace pour choisir
    const opts = Array.from(pop.querySelectorAll('.theme-opt'));
    const i = opts.indexOf(document.activeElement);
    if(i < 0 || !/^Arrow(Left|Right|Up|Down)$/.test(e.key)) return;
    e.preventDefault();
    opts[(i + (/Right|Down/.test(e.key) ? 1 : opts.length - 1)) % opts.length].focus();
  });
  document.addEventListener('keydown', e => { if(e.key === 'Escape' && ouvert()) fermerPop(true); });
  window.__themePref = themePref;
  window.__setTheme = setTheme;
})();