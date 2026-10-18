(function urlRouting(){
  let lastChap = null;
  /* Pages plein écran du téléphone (page Chapitres, feuille ⋯, Aujourd'hui, recherche,
     quiz, Bilan, fenêtres) : le bouton retour d'Android les FERME au lieu de quitter le
     chapitre. À l'ouverture d'une page (classe .open), une entrée d'historique fictive
     (même URL) est empilée ; « retour » la dépile → popstate → on ferme la page. Fermée
     autrement (×, Échap, voile), l'entrée fictive est retirée (history.back, popstate
     ignoré) ; si un chapitre est choisi depuis la page, elle est REMPLACÉE par ce
     chapitre (syncHash fait alors replaceState au lieu de pushState). */
  const PAGES = ['mob-drawer','mob-more-menu','today-overlay','search-overlay','quiz-overlay','dash-overlay',
    'formula-overlay','backup-overlay','flag-overlay','drill-overlay'];
  const mqTel = window.matchMedia ? window.matchMedia('(max-width:767px)') : { matches:false };
  let pageFictive = null;      // page ouverte qui a empilé l'entrée fictive
  let aRemplacer = false;      // entrée fictive au sommet, à remplacer par la prochaine URL
  let retoursIgnores = 0;      // history.back() lancés par nous : leurs popstate sont ignorés
  let parRetour = false;       // fermeture en cours provoquée par le bouton retour
  const estOuverte = el => !!(el && el.classList.contains('open'));
  function retirerFictive(delai){
    setTimeout(() => {   // laissé à syncHash s'il navigue entre-temps (remplacement)
      if(!aRemplacer || pageFictive) return;
      aRemplacer = false; retoursIgnores++;
      try { history.back(); } catch(e){ retoursIgnores--; }
    }, delai || 0);
  }
  function surMutations(){
    // fermetures d'abord (une page peut en ouvrir une autre dans le même geste)
    if(pageFictive && !estOuverte(pageFictive)){
      pageFictive = null;
      if(parRetour) parRetour = false;
      else { aRemplacer = true; retirerFictive(0); }
    }
    if(!pageFictive && mqTel.matches){
      const el = PAGES.map(id => document.getElementById(id)).find(estOuverte);
      if(el){
        pageFictive = el;
        if(aRemplacer) aRemplacer = false;            // on réutilise l'entrée fictive restée au sommet
        else { try { history.pushState({ pageFictive: el.id }, '', location.href); } catch(e){ pageFictive = null; } }
      }
    }
  }
  const obsPages = new MutationObserver(surMutations);
  PAGES.forEach(id => { const el = document.getElementById(id); if(el) obsPages.observe(el, { attributes:true, attributeFilter:['class'] }); });
  // Un chapitre va être choisi depuis la page ouverte : l'URL du chapitre remplacera
  // l'entrée fictive. avecRelais : une autre page va s'ouvrir aussitôt (tuiles).
  window.__consommerPageFictive = function(avecRelais){
    if(!pageFictive) return;
    pageFictive = null;
    aRemplacer = true;
    if(!avecRelais) retirerFictive(400);   // aucune navigation finalement (même URL) : on retire l'entrée
  };
  function fermerPageParRetour(el){
    parRetour = true;
    if(el.id === 'mob-drawer'){ const b = document.getElementById('mob-drawer-close'); if(b) b.click(); }
    else if(el.id === 'mob-more-menu' && window.__fermerFeuillePlus) window.__fermerFeuillePlus();
    else if(el.id === 'quiz-overlay' && window.quizClose) window.quizClose();
    else document.dispatchEvent(new KeyboardEvent('keydown', { key:'Escape', bubbles:true }));
    if(estOuverte(el)) el.classList.remove('open');   // filet de sécurité
    setTimeout(() => { parRetour = false; }, 0);
  }

  function syncHash(){
    const so = window.__sommaireOuvert ? window.__sommaireOuvert() : null;
    let h, cle;
    if(so){ h = '#sommaire/' + so; cle = 'sommaire/' + so; }
    else {
      const ch = document.querySelector('.chapter.active');
      if(!ch) return;
      const chapId = ch.id.replace('chap-','');
      const p = ch.querySelector('.panel.active');
      const suf = p ? p.id.split('-').pop() : '';
      h = '#' + chapId + (suf ? '/'+suf : '');
      cle = chapId;
    }
    if(location.hash === h) return;            // pas de changement
    if(aRemplacer){ aRemplacer = false; history.replaceState(null,'',h); }   // remplace l'entrée fictive d'une page plein écran
    else if(cle !== lastChap){ history.pushState(null,'',h); }  // nouveau chapitre (ou sommaire) → entrée d'historique
    else { history.replaceState(null,'',h); }                  // même chapitre, onglet différent → pas d'entrée
    lastChap = cle;
  }
  window.__syncHash = syncHash;
  document.addEventListener('click', e=>{
    const t = e.target;
    if(t && t.closest && (t.closest('.chap-btn') || t.closest('.tab') || t.closest('.mob-chap-item')
        || t.closest('.sub-btn') || t.closest('.mat-btn') || t.closest('.mob-mat-btn'))){
      setTimeout(syncHash, 0);   // après les handlers existants (qui mettent à jour .active)
    }
  });
  function navFromHash(){
    const raw = (location.hash || '').replace(/^#/, '');
    if(!raw) return false;
    const parts = raw.split('/');
    // Sommaire de la matière : #sommaire/physique
    if(parts[0] === 'sommaire' && parts[1] && window.__ouvrirSommaire){
      lastChap = 'sommaire/' + parts[1];
      return window.__ouvrirSommaire(parts[1], true);
    }
    const chapId = parts[0], suf = parts[1];
    const c = CHAPTERS_BY_ID[chapId];
    if(!c || !document.getElementById('chap-'+chapId)) return false;
    lastChap = chapId;           // évite de re-empiler une entrée d'historique
    if(window.__sommaireOuvert && window.__sommaireOuvert() && window.__fermerSommaire) window.__fermerSommaire(false);
    navigateTo('chap-'+chapId, suf ? (c.prefix+'-'+suf) : null);
    return true;
  }
  window.addEventListener('popstate', () => {
    if(retoursIgnores > 0){ retoursIgnores--; return; }      // retrait de l'entrée fictive : rien à faire
    if(pageFictive){ const el = pageFictive; pageFictive = null; fermerPageParRetour(el); return; }
    aRemplacer = false;
    navFromHash();
  });
  window.__navFromHash = navFromHash;
})();