/* Menus déroulants de l'en-tête (Réviser ▾, Plus ⋯) — gabarit .menu (SPEC §5.1) :
   clic, Échap, clic dehors ; flèches ↑ ↓ (Début / Fin) entre les éléments ; ouverture au
   clavier = focus sur le 1ᵉʳ élément. Chaque élément garde son id et son propre handler.
   Le menu Plus reçoit « Dans ce chapitre » entre 1200 et 1359 px (pas de place pour le
   rail du sommaire à cette largeur). */
(function(){
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  function menuDeroulant(btnId, menuId, avantOuverture){
    const btn = document.getElementById(btnId), menu = document.getElementById(menuId);
    if(!btn || !menu) return;
    const items = () => Array.from(menu.querySelectorAll('.menu-item')).filter(x => !x.disabled && x.getClientRects().length);
    const estOuvert = () => menu.classList.contains('open');
    function close(rendre){
      if(!estOuvert()) return;
      menu.classList.remove('open'); btn.classList.remove('open'); btn.setAttribute('aria-expanded', 'false');
      if(rendre) btn.focus();
    }
    function open(clavier){
      if(avantOuverture) try { avantOuverture(menu); } catch(e){}
      menu.classList.add('open'); btn.classList.add('open'); btn.setAttribute('aria-expanded', 'true');
      if(clavier){ const f = items()[0]; if(f) f.focus(); }
    }
    btn.addEventListener('click', e => { e.stopPropagation(); if(estOuvert()) close(); else open(e.detail === 0); });
    btn.addEventListener('keydown', e => {
      if((e.key === 'ArrowDown' || e.key === 'ArrowUp') && !estOuvert()){ e.preventDefault(); open(true); }
    });
    // chaque élément ferme le menu (son action reste gérée par son propre handler)
    menu.addEventListener('click', e => { if(e.target.closest && e.target.closest('.menu-item')) close(); });
    menu.addEventListener('keydown', e => {
      const l = items(), n = l.length, i = l.indexOf(document.activeElement);
      if(!n) return;
      if(e.key === 'ArrowDown'){ e.preventDefault(); l[(i + 1) % n].focus(); }
      else if(e.key === 'ArrowUp'){ e.preventDefault(); l[(i <= 0 ? n : i) - 1].focus(); }
      else if(e.key === 'Home'){ e.preventDefault(); l[0].focus(); }
      else if(e.key === 'End'){ e.preventDefault(); l[n - 1].focus(); }
      else if(e.key === 'Escape'){ e.stopPropagation(); close(true); }
      else if(e.key === 'Tab'){ close(); }
    });
    document.addEventListener('click', e => { if(!menu.contains(e.target) && !btn.contains(e.target)) close(); });
    document.addEventListener('keydown', e => { if(e.key === 'Escape') close(); });
  }
  /* « Dans ce chapitre » : sections du panneau affiché (1200–1359 px seulement) */
  function dansCeChapitre(){
    const box = document.getElementById('more-toc');
    const list = box && box.querySelector('.more-toc-list');
    if(!list) return;
    const w = window.innerWidth;
    const ch = Array.from(document.querySelectorAll('.chapter.active')).find(x => x.offsetParent !== null);
    const p = ch && ch.querySelector('.panel.active');
    const secs = (w >= 1200 && w < 1360 && p) ? Array.from(p.querySelectorAll('.course-section')).filter(s => s.querySelector('h2')) : [];
    list.innerHTML = '';
    if(secs.length < 2){ box.hidden = true; return; }
    secs.forEach((s, k) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'menu-item hdr-more-item';
      b.setAttribute('role', 'menuitem');
      const lab = s.dataset.tocLabel || ((s.querySelector('.sec-num') || {}).textContent || '');
      const m = lab.match(/^\s*(§\s*\d+)/);
      b.innerHTML = '<span class="n">' + esc(m ? m[1].replace(/\s+/g, '') : '§' + (k + 1)) + '</span><span>' + esc(s.querySelector('h2').textContent.trim()) + '</span>';
      b.addEventListener('click', () => s.scrollIntoView({ behavior:'smooth', block:'start' }));
      list.appendChild(b);
    });
    box.hidden = false;
  }
  menuDeroulant('more-btn', 'more-menu', dansCeChapitre);
  menuDeroulant('study-btn', 'study-menu');
})();