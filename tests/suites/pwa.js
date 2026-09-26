'use strict';
/* ============================================================
   Suite « pwa » — service worker et fonctionnement hors-ligne
   ============================================================
   Contexte AVEC service workers (contrairement aux autres suites) :
   - sw.js : toutes les entrées de PRECACHE existent sur le disque ;
   - manifest.webmanifest valide (nom, icônes présentes, display standalone) ;
   - enregistrement du SW, activation, cache CACHE_VERSION rempli ;
   - rechargement HORS-LIGNE : le site démarre, MathJax rend un cours. */
const fs = require('fs');
const path = require('path');
const { pause, attendreApp, fermerOverlays, naviguer, etatMathJax, lireServiceWorker, listerFichiers } = require('../lib/outils');

module.exports = {
  nom: 'pwa',
  description: 'service worker, précache, hors-ligne',
  delaiMax: () => 5 * 60000,

  async executer(ctx, res) {
    const racine = ctx.options.racine;

    /* ---------- 1) Contrôles statiques de sw.js et du manifeste ---------- */
    const sw = lireServiceWorker(racine);
    res.verifier('sw.js : CACHE_VERSION et PRECACHE lisibles', !!(sw.version && Array.isArray(sw.precache)),
      'impossible de lire ' + (!sw.version ? 'CACHE_VERSION' : 'la liste PRECACHE') + ' dans sw.js');
    if (!Array.isArray(sw.precache)) return;
    res.info('cacheVersion', sw.version);
    const absents = sw.precache.filter(p => p !== './' && !fs.existsSync(path.join(racine, p)));
    res.verifier('PRECACHE : les ' + sw.precache.length + ' fichiers listés existent', !absents.length,
      absents.map(p => 'fichier absent (l\'installation du SW échouerait) : ' + p));
    const horsCache = listerFichiers(racine, 'vendor').concat(listerFichiers(racine, 'icons'))
      .filter(f => !sw.precache.includes(f) && !/\.(md|txt|map)$/i.test(f));
    if (horsCache.length) res.avertir('fichier(s) de vendor/ ou icons/ absents de PRECACHE (non disponibles hors-ligne) : ' + horsCache.slice(0, 6).join(', ') + (horsCache.length > 6 ? '…' : ''));

    let manifeste = null, pbMan = [];
    try { manifeste = JSON.parse(fs.readFileSync(path.join(racine, 'manifest.webmanifest'), 'utf8')); }
    catch (e) { pbMan.push('manifest.webmanifest illisible : ' + e.message); }
    if (manifeste) {
      if (!manifeste.name) pbMan.push('champ « name » absent');
      if (manifeste.display !== 'standalone') pbMan.push('display = ' + manifeste.display + ' (attendu standalone)');
      const icones = (manifeste.icons || []).map(i => i.src);
      if (!icones.length) pbMan.push('aucune icône déclarée');
      icones.filter(s => !fs.existsSync(path.join(racine, s))).forEach(s => pbMan.push('icône absente : ' + s));
    }
    res.verifier('manifest.webmanifest valide (nom, icônes, standalone)', !pbMan.length, pbMan);

    /* ---------- 2) Enregistrement et activation du service worker ---------- */
    const { contexte, page, journal } = await ctx.nouvellePage({ sw: true });
    journal.lieu = '1re visite (SW)';
    let rechargements = 0;
    page.on('load', () => { rechargements++; });
    await page.goto(ctx.url(), { waitUntil: 'load', timeout: 60000 });
    // Attendre que la page soit contrôlée par le SW (1re visite : clients.claim())
    let controle = false;
    const t0 = Date.now();
    while (Date.now() - t0 < 30000) {
      controle = await page.evaluate(() => !!(navigator.serviceWorker && navigator.serviceWorker.controller)).catch(() => false);
      if (controle) break;
      await pause(250);
    }
    await pause(1500);   // un éventuel rechargement automatique a le temps de partir
    await page.waitForLoadState('load').catch(() => {});
    await attendreApp(page);
    const auto = rechargements > 1;
    res.info('rechargementAutomatique1reVisite', auto);
    if (auto) res.avertir('rechargement automatique de la page à la 1re visite — anomalie connue : index.html recharge au 1er controllerchange sans vérifier qu\'un service worker contrôlait déjà la page (voir tests/README.md §5)');

    const reg = await page.evaluate(async () => {
      const r = await Promise.race([navigator.serviceWorker.ready, new Promise(x => setTimeout(() => x(null), 20000))]);
      return r ? { portee: r.scope, etat: r.active && r.active.state, controle: !!navigator.serviceWorker.controller } : null;
    });
    res.verifier('service worker enregistré, activé et contrôlant la page', !!(reg && reg.etat === 'activated' && reg.controle),
      reg ? 'état = ' + reg.etat + ', contrôle = ' + reg.controle : 'navigator.serviceWorker.ready jamais résolu (enregistrement échoué ?)');

    // Précache rempli (cache nommé CACHE_VERSION)
    let cache = null;
    const t1 = Date.now();
    while (Date.now() - t1 < 30000) {
      cache = await page.evaluate(async v => {
        const noms = await caches.keys();
        const c = noms.includes(v) ? await caches.open(v) : null;
        return { noms, entrees: c ? (await c.keys()).length : 0 };
      }, sw.version);
      if (cache.entrees >= sw.precache.length) break;
      await pause(300);
    }
    res.verifier('cache « ' + sw.version + ' » rempli (' + sw.precache.length + ' entrées attendues)',
      cache && cache.noms.includes(sw.version) && cache.entrees >= sw.precache.length,
      cache ? 'caches : ' + cache.noms.join(', ') + ' — ' + cache.entrees + ' entrée(s)' : 'aucun cache');

    /* ---------- 3) Rechargement hors-ligne ---------- */
    journal.lieu = 'hors-ligne';
    const pbHL = [];
    const nbEchecs = journal.echecs.length;
    try {
      await contexte.setOffline(true);
      await page.reload({ waitUntil: 'load', timeout: 30000 });
      await attendreApp(page, 30000);
      await fermerOverlays(page);
      const s = await page.evaluate(() => ({ chapitres: CHAPTERS.length, titre: document.title,
        police: document.fonts ? document.fonts.check('16px "Inter Tight"') : true }));
      if (!s.chapitres) pbHL.push('CHAPTERS vide hors-ligne');
      if (!s.police) pbHL.push('police Inter Tight non disponible hors-ligne');
      const og = await page.evaluate(() => { const c = CHAPTERS.find(x => x.id !== 'rlc' && x.matiere === 'physique'); return c && c.id; });
      await naviguer(page, og, 'cours');
      const pid = await page.evaluate(id => CHAPTERS_BY_ID[id].prefix + '-cours', og);
      const m = await etatMathJax(page, pid, 4000);
      if (!m || !m.mjx) pbHL.push('MathJax n\'a rendu aucune formule hors-ligne dans ' + pid);
      journal.echecs.slice(nbEchecs).forEach(e => pbHL.push('requête échouée hors-ligne : ' + e.url + ' (' + e.erreur + ')'));
    } catch (e) {
      pbHL.push('le site ne démarre pas hors-ligne : ' + String(e.message).split('\n')[0]);
    } finally {
      await contexte.setOffline(false).catch(() => {});
    }
    await ctx.capture(page, 'hors-ligne');
    res.verifier('rechargement hors-ligne : site et MathJax fonctionnels', !pbHL.length, pbHL);

    const js = journal.erreurs.map(e => '[' + e.lieu + '] ' + e.type + ' : ' + e.texte);
    res.verifier('aucune erreur JavaScript (avec service worker)', !js.length, js);
    res.verifier('aucune requête externe (avec service worker)', !journal.externes.length, journal.externes.map(e => e.url));
  },
};
