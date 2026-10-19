'use strict';
/* ============================================================
   Suite « interactions » — parcours d'un utilisateur sur ordinateur
   ============================================================
   Deep-link #hash, routage (précédent / suivant du navigateur), boutons
   ‹ › de chapitre, bascule vers la SI, recherche, flashcards + Leitner, quiz,
   « Réviser », Bilan, Aujourd'hui, formulaire, cartes signalées, calcul
   mental, impression, thème, sauvegarde (export PUIS import, qui recharge). */
const fs = require('fs');
const { pause, attendreApp, fermerOverlays, naviguer, choisirTheme, marqueJournal, problemesJournal } = require('../lib/outils');

/* Chapitre réellement affiché (deux .chapter.active coexistent au chargement :
   un dans chaque <main> ; on garde celui qui est visible) */
const CHAP_VISIBLE = () => {
  const v = Array.from(document.querySelectorAll('.chapter.active')).find(c => c.offsetParent !== null);
  return v ? v.id : null;
};

module.exports = {
  nom: 'interactions',
  description: "quiz, recherche, Bilan, Aujourd'hui, sauvegarde, navigation, #hash",
  delaiMax: () => 8 * 60000,

  async executer(ctx, res) {
    const { page, journal } = await ctx.nouvellePage();

    /* Chaque étape : exceptions et erreurs JS de l'étape → échec de l'étape */
    async function etape(nom, fn) {
      journal.lieu = nom;
      const m = marqueJournal(journal);
      let pb = [];
      try { pb = (await fn()) || []; }
      catch (e) { pb = ['exception du test : ' + String(e.message).split('\n')[0]]; }
      pb = pb.filter(Boolean).concat(problemesJournal(journal, m));
      res.verifier(nom, !pb.length, pb);
      await fermerOverlays(page).catch(() => {});
    }
    const visible = () => page.evaluate(CHAP_VISIBLE);
    const ouvert = id => page.evaluate(id => { const o = document.getElementById(id); return !!(o && o.classList.contains('open')); }, id);

    /* ---------- Deep-link ---------- */
    await etape('deep-link #rlc/simu (sans écran Aujourd\'hui)', async () => {
      await page.goto(ctx.url('#rlc/simu'), { waitUntil: 'load', timeout: 60000 });
      await attendreApp(page);
      await pause(400);
      const s = await page.evaluate(() => ({
        aujourdhui: document.getElementById('today-overlay').classList.contains('open'),
        panneau: (document.querySelector('#chap-rlc .panel.active') || {}).id,
        hash: location.hash,
      }));
      s.chap = await visible();
      return [
        s.aujourdhui && "l'écran Aujourd'hui s'ouvre alors qu'un #hash est fourni",
        s.chap !== 'chap-rlc' && 'chapitre affiché : ' + s.chap + ' au lieu de chap-rlc',
        s.panneau !== 'rlc-simu' && 'onglet actif : ' + s.panneau + ' au lieu de rlc-simu',
        s.hash !== '#rlc/simu' && 'hash : ' + s.hash,
      ];
    });

    // Chapitre dont l'id diffère du prefix (cas le plus fréquent, source de bugs)
    const autre = await page.evaluate(() => {
      const c = CHAPTERS.find(x => x.id !== 'rlc' && x.id !== x.prefix && x.matiere !== 'si' && x.panels.includes('flash'));
      return { id: c.id, prefix: c.prefix };
    });

    /* ---------- Routage : hash, pushState / replaceState, précédent ---------- */
    await etape('routage #hash + bouton précédent/suivant du navigateur (' + autre.id + ')', async () => {
      const pb = [];
      await naviguer(page, autre.id, 'cours');
      let h = await page.evaluate(() => location.hash);
      if (h !== '#' + autre.id + '/cours') pb.push('après navigation : hash ' + h + ' au lieu de #' + autre.id + '/cours');
      const lg = await page.evaluate(() => history.length);
      await page.evaluate(pid => document.querySelector('.tab[data-panel="' + pid + '"]').click(), autre.prefix + '-flash');
      await pause(150);
      h = await page.evaluate(() => location.hash);
      if (h !== '#' + autre.id + '/flash') pb.push('après clic sur l\'onglet Flashcards : hash ' + h);
      if (await page.evaluate(() => history.length) !== lg) pb.push("un changement d'onglet ne doit pas créer d'entrée d'historique (replaceState)");
      await page.goBack();
      await pause(500);
      if (await visible() !== 'chap-rlc') pb.push('« précédent » : chapitre affiché ' + (await visible()) + ' au lieu de chap-rlc');
      h = await page.evaluate(() => location.hash);
      if (!h.startsWith('#rlc/')) pb.push('« précédent » : hash ' + h);
      await page.goForward();
      await pause(500);
      if (await visible() !== 'chap-' + autre.id) pb.push('« suivant » : chapitre affiché ' + (await visible()));
      return pb;
    });

    /* ---------- Bascule vers un chapitre SI (<main id="si-content">) ---------- */
    await etape('navigation vers un chapitre SI (bascule de <main>)', async () => {
      const si = await page.evaluate(() => CHAPTERS.find(c => c.matiere === 'si').id);
      await naviguer(page, si, 'cours');
      const s = await page.evaluate(id => ({
        siAffiche: getComputedStyle(document.getElementById('si-content')).display !== 'none',
        principalMasque: getComputedStyle(document.querySelector('main:not(#si-content)')).display === 'none',
        visible: !!document.getElementById('chap-' + id).offsetParent,
      }), si);
      const pb = [!s.siAffiche && '#si-content reste masqué', !s.principalMasque && 'le <main> principal reste affiché',
        !s.visible && 'chap-' + si + ' invisible'];
      await naviguer(page, 'rlc', 'cours');
      if (await visible() !== 'chap-rlc') pb.push('retour vers rlc impossible (chapitre affiché : ' + (await visible()) + ')');
      return pb;
    });

    /* ---------- Boutons ‹ › (chapitre précédent / suivant) ---------- */
    await etape('boutons chapitre précédent / suivant', async () => {
      const pb = [];
      const ids = await page.evaluate(() => CHAPTERS.map(c => c.id));
      const k = Math.min(5, ids.length - 2);
      await naviguer(page, ids[k], 'cours');
      await page.evaluate(() => document.getElementById('next-chap-btn').click());
      await pause(400);
      if (await visible() !== 'chap-' + ids[k + 1]) pb.push('› : chapitre affiché ' + (await visible()) + ' au lieu de chap-' + ids[k + 1]);
      await page.evaluate(() => document.getElementById('prev-chap-btn').click());
      await pause(400);
      if (await visible() !== 'chap-' + ids[k]) pb.push('‹ : chapitre affiché ' + (await visible()) + ' au lieu de chap-' + ids[k]);
      await naviguer(page, ids[0], 'cours');
      await pause(100);
      if (!(await page.evaluate(() => document.getElementById('prev-chap-btn').disabled))) pb.push('‹ devrait être désactivé sur le premier chapitre');
      return pb;
    });

    /* ---------- Page chapitre : intercalaire, onglets, rail droit, pied (SPEC §4.4) ---------- */
    await etape('page chapitre : intercalaire, onglets (ARIA, compteurs, clavier), rail droit, pied dans la feuille', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      await pause(300);
      const s = await page.evaluate(() => {
        const ch = document.getElementById('chap-rlc'), c = CHAPTERS_BY_ID.rlc;
        const b = ch.querySelector(':scope > .chap-title-banner');
        const nav = ch.querySelector(':scope > nav.tabs');
        const flash = nav && nav.querySelector('.tab[data-panel="rlc-flash"]');
        const rail = document.getElementById('chap-rail');
        const secs = document.querySelectorAll('#rlc-cours .course-section').length;
        return {
          fil: b ? (b.querySelector('.ctb-crumb') || {}).textContent || '' : '',
          titre: b ? (b.querySelector('.ctb-title') || {}).textContent || '' : '', nom: c.name,
          actions: b ? b.querySelectorAll('.ctb-actions [data-ctb]').length : 0,
          meta: b ? (b.querySelector('.ctb-meta') || {}).textContent || '' : '',
          role: nav && nav.getAttribute('role'),
          selection: Array.from(nav.querySelectorAll('.tab')).map(t => t.getAttribute('aria-selected')).join(','),
          cartes: flash ? parseInt((flash.querySelector('.cnt') || {}).textContent, 10) : NaN, deck: FLASH_REGISTRY.rlc.length,
          railOn: document.documentElement.classList.contains('rail-on') && rail.getBoundingClientRect().width > 150,
          liens: rail.querySelectorAll('.toc-list a').length, secs,
          actif: (rail.querySelector('.toc-list a.on .t') || {}).textContent || '',
          mesCartes: !!rail.querySelector('.rail-cartes .big'),
          pied: document.getElementById('chap-pager').parentNode === ch,
          suivant: document.getElementById('next-chap-name').textContent,
        };
      });
      if (!/Physique/.test(s.fil) || !/Ondes/.test(s.fil)) pb.push('fil d\'Ariane : « ' + s.fil + ' »');
      if (s.titre !== s.nom) pb.push('titre de l\'intercalaire : « ' + s.titre + ' » au lieu de « ' + s.nom + ' »');
      if (s.actions !== 3) pb.push(s.actions + ' actions dans l\'intercalaire (Formulaire, Imprimer, Épingler attendus)');
      if (!/année/.test(s.meta) || !/cartes/.test(s.meta)) pb.push('méta de l\'intercalaire : « ' + s.meta + ' »');
      if (s.role !== 'tablist' || !/^true(,false)+$/.test(s.selection)) pb.push('onglets : role=' + s.role + ', aria-selected=' + s.selection);
      if (s.cartes !== s.deck) pb.push('effectif de l\'onglet Cartes : ' + s.cartes + ' au lieu de ' + s.deck);
      if (!s.railOn) pb.push('rail droit absent à 1 400 px');
      if (s.liens !== s.secs || s.secs < 2) pb.push('sommaire du rail : ' + s.liens + ' lignes pour ' + s.secs + ' sections');
      if (!s.actif) pb.push('aucune section active dans le sommaire du rail en haut de page');
      if (!s.mesCartes) pb.push('« Mes cartes » absent du rail');
      if (!s.pied) pb.push('#chap-pager n\'est pas en bas de la feuille du chapitre affiché');
      if (!s.suivant) pb.push('nom du chapitre suivant vide');
      // Sommaire du rail : clic sur la 3ᵉ section → défilement jusqu'à elle, ligne active
      await page.evaluate(() => document.querySelectorAll('#chap-rail .toc-list a')[2].click());
      await pause(1400);
      const d = await page.evaluate(() => {
        const a = document.querySelectorAll('#chap-rail .toc-list a')[2], sec = document.getElementById(a.dataset.targetId);
        return { haut: Math.round(sec.getBoundingClientRect().top), on: a.classList.contains('on') };
      });
      if (d.haut < 0 || d.haut > 300) pb.push('clic sur le sommaire du rail : la section est à ' + d.haut + ' px du haut');
      if (!d.on) pb.push('clic sur le sommaire du rail : la ligne n\'est pas marquée active');
      // Clavier : → sur l'onglet actif active l'onglet suivant
      await page.evaluate(() => { scrollPageTop(); document.querySelector('#chap-rlc .tab.active').focus(); });
      await page.keyboard.press('ArrowRight');
      await pause(300);
      const k = await page.evaluate(() => ({ p: (document.querySelector('#chap-rlc .panel.active') || {}).id,
        f: document.activeElement && document.activeElement.getAttribute('data-panel') }));
      if (k.p !== 'rlc-meth' || k.f !== 'rlc-meth') pb.push('→ sur les onglets : panneau ' + k.p + ', focus ' + k.f + ' (rlc-meth attendu)');
      // Onglet Exercices : liste des exercices dans le rail ; Simulateur : pas de rail
      await naviguer(page, 'rlc', 'exos');
      await pause(300);
      const e = await page.evaluate(() => ({ liens: document.querySelectorAll('#chap-rail .exo-list a').length,
        exos: document.querySelectorAll('#rlc-exos .exo').length, onglet: document.getElementById('chap-rlc').dataset.onglet }));
      if (!e.exos || e.liens !== e.exos) pb.push('rail de l\'onglet Exercices : ' + e.liens + ' lignes pour ' + e.exos + ' exercices');
      if (e.onglet !== 'exos') pb.push('data-onglet de la feuille : ' + e.onglet);
      await naviguer(page, 'rlc', 'simu');
      await pause(300);
      if (await page.evaluate(() => document.documentElement.classList.contains('rail-on'))) pb.push('rail affiché sur l\'onglet Simulateur');
      // Épingler depuis l'intercalaire (puis rétablir)
      await naviguer(page, 'rlc', 'cours');
      const avant = await page.evaluate(() => (Store.getJSON('pinned', []) || []).includes('chap-rlc'));
      await page.click('#chap-rlc .ctb-actions [data-ctb="epingler"]');
      const ep = await page.evaluate(() => ({ st: (Store.getJSON('pinned', []) || []).includes('chap-rlc'),
        aria: document.querySelector('#chap-rlc [data-ctb="epingler"]').getAttribute('aria-pressed') }));
      if (ep.st === avant || ep.aria !== String(!avant)) pb.push('Épingler (intercalaire) : épinglé=' + ep.st + ', aria-pressed=' + ep.aria);
      await page.click('#chap-rlc .ctb-actions [data-ctb="epingler"]');
      // Formulaire depuis l'intercalaire
      await page.click('#chap-rlc .ctb-actions [data-ctb="formulaire"]');
      await pause(400);
      if (!(await ouvert('formula-overlay'))) pb.push('le bouton Formulaire de l\'intercalaire n\'ouvre pas le formulaire');
      await page.keyboard.press('Escape');
      return pb;
    });

    /* ---------- Navigation des chapitres (coquille) ---------- */
    await etape('barre latérale des chapitres (≥ 1200 px) : affichée, repliable, mémorisée (navCollapsed)', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      const etat = () => page.evaluate(() => {
        const d = document.getElementById('mob-drawer'), r = d.getBoundingClientRect();
        return { vis: d.checkVisibility() && r.width > 200, replie: document.documentElement.classList.contains('nav-replie'),
          cle: Store.get('navCollapsed'), aria: document.getElementById('nav-toggle-btn').getAttribute('aria-expanded'),
          rangees: document.querySelectorAll('#mob-chap-list .mob-chap-row').length,
          cur: (document.querySelector('#mob-chap-list .mob-chap-row.cur .mob-chap-item[aria-current="page"]') || {}).textContent || '',
          marge: Math.round(document.getElementById('app-main').getBoundingClientRect().left) };
      });
      let s = await etat();
      if (!s.vis || s.replie) pb.push('au départ, la barre latérale n\'est pas affichée');
      if (!s.rangees) pb.push('aucune rangée de chapitre dans la barre latérale');
      if (!/RLC/.test(s.cur)) pb.push('rangée du chapitre affiché (aria-current) : « ' + s.cur + ' »');
      if (s.marge < 280) pb.push('la colonne de lecture n\'est pas décalée par la barre latérale (bord gauche ' + s.marge + ' px)');
      await page.click('#nav-toggle-btn');
      await pause(250);
      s = await etat();
      if (s.vis || !s.replie || s.cle !== '1' || s.aria !== 'false') pb.push('après repli : visible=' + s.vis + ', classe nav-replie=' + s.replie + ', navCollapsed=' + s.cle + ', aria-expanded=' + s.aria);
      if (s.marge > 10) pb.push('barre repliée : la colonne de lecture reste décalée (' + s.marge + ' px)');
      await page.reload({ waitUntil: 'load' });
      await attendreApp(page);
      await pause(300);
      s = await etat();
      if (!s.replie || s.vis) pb.push('après rechargement, le repli n\'est pas conservé');
      await page.click('#nav-toggle-btn');
      await pause(300);
      s = await etat();
      if (!s.vis || s.replie || s.cle !== '0' || !s.rangees) pb.push('après réaffichage : visible=' + s.vis + ', navCollapsed=' + s.cle + ', rangées=' + s.rangees);
      return pb;
    });

    await etape('Sommaire de la matière : 2ᵉ clic sur l\'intercalaire actif, #sommaire/…, précédent', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      await page.click('#mob-mat-bar .mob-mat-btn[data-mat="physique"]');   // intercalaire actif → sommaire
      await pause(400);
      const lire = () => page.evaluate(() => {
        const s = document.getElementById('sommaire-matiere');
        return { ouvert: !!(s && !s.hidden), parties: s ? s.querySelectorAll('.pcard').length : 0,
          titre: s && s.querySelector('.ov-h') ? s.querySelector('.ov-h').textContent : '', hash: location.hash,
          mainMasque: getComputedStyle(document.querySelector('#app-main > main')).display === 'none' };
      });
      let s = await lire();
      if (!s.ouvert || !s.parties) pb.push('le sommaire ne s\'ouvre pas (' + s.parties + ' partie(s))');
      if (s.titre !== 'Physique') pb.push('titre du sommaire : « ' + s.titre + ' »');
      if (s.hash !== '#sommaire/physique') pb.push('hash du sommaire : ' + s.hash);
      if (!s.mainMasque) pb.push('le chapitre reste affiché sous le sommaire');
      const cible = await page.evaluate(() => { const b = document.querySelector('#sommaire-matiere .pcard-list button[data-chap]:not(.cur)'); const id = b.dataset.chap; b.click(); return id; });
      await pause(600);
      s = await lire();
      if (s.ouvert) pb.push('le sommaire reste ouvert après le choix d\'un chapitre');
      if (await visible() !== cible) pb.push('chapitre affiché : ' + (await visible()) + ' au lieu de ' + cible);
      await page.goBack();
      await pause(600);
      s = await lire();
      if (!s.ouvert || s.hash !== '#sommaire/physique') pb.push('« précédent » ne rouvre pas le sommaire (hash ' + s.hash + ')');
      await page.goBack();
      await pause(600);
      s = await lire();
      if (s.ouvert) pb.push('2ᵉ « précédent » : le sommaire reste ouvert');
      if (await visible() !== 'chap-rlc') pb.push('2ᵉ « précédent » : chapitre affiché ' + (await visible()) + ' au lieu de chap-rlc');
      return pb;
    });

    await etape('filtre de la navigation : résultats groupés par matière, <mark>, Entrée', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      await page.fill('#mob-filter', 'onde');
      await pause(300);
      const r = await page.evaluate(() => ({
        groupes: Array.from(document.querySelectorAll('#mob-chap-list .grp')).map(g => g.getAttribute('data-mat')),
        marques: document.querySelectorAll('#mob-chap-list mark').length,
        lignes: document.querySelectorAll('#mob-chap-list .mob-chap-item').length,
        mat: getComputedStyle(document.getElementById('mob-mat-bar')).display,
      }));
      if (r.groupes.length < 2 || !r.groupes.includes('physique')) pb.push('groupes par matière : ' + r.groupes.join(', '));
      if (!r.marques || r.marques < r.lignes) pb.push(r.marques + ' <mark> pour ' + r.lignes + ' résultat(s)');
      if (r.mat !== 'none') pb.push('les intercalaires restent affichés pendant le filtrage');
      await page.fill('#mob-filter', 'rlc');
      await pause(300);
      await page.press('#mob-filter', 'Enter');
      await pause(700);
      if (await visible() !== 'chap-rlc') pb.push('Entrée : chapitre affiché ' + (await visible()));
      const vide = await page.evaluate(() => document.getElementById('mob-filter').value);
      if (vide) pb.push('le filtre n\'est pas vidé après le choix d\'un chapitre (« ' + vide + ' »)');
      return pb;
    });

    /* ---------- Recherche ---------- */
    await etape('recherche (Ctrl K / bouton) : résultats puis Entrée', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      const avant = await page.evaluate(() => location.hash);
      await page.click('#search-btn');
      await pause(250);
      if (!(await ouvert('search-overlay'))) return ['la fenêtre de recherche ne s\'ouvre pas'];
      await page.fill('#search-input', 'fourier');
      await pause(500);
      const n = await page.evaluate(() => document.querySelectorAll('#search-results .search-result').length);
      if (!n) pb.push('aucun résultat pour « fourier »');
      await page.keyboard.press('Enter');
      await pause(500);
      if (await ouvert('search-overlay')) pb.push('la recherche reste ouverte après Entrée');
      const apres = await page.evaluate(() => location.hash);
      if (n && apres === avant) pb.push('Entrée n\'a pas navigué vers le 1er résultat (hash inchangé : ' + apres + ')');
      await page.keyboard.press('Control+k');
      await pause(200);
      if (!(await ouvert('search-overlay'))) pb.push('Ctrl+K n\'ouvre pas la recherche');
      await page.keyboard.press('Escape');
      await pause(150);
      if (await ouvert('search-overlay')) pb.push('Échap ne ferme pas la recherche');
      return pb;
    });

    /* ---------- Flashcards + répétition espacée ---------- */
    await etape('flashcards : retourner, noter, progression et Leitner', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'flash');
      const q = await page.evaluate(() => document.getElementById('rlc-flash-content').innerText);
      await page.click('#rlc-flash .flash-card');
      await pause(600);
      const a = await page.evaluate(() => document.getElementById('rlc-flash-content').innerText);
      if (a === q || !/R[ÉE]PONSE/i.test(a)) pb.push('la carte ne se retourne pas (face : ' + a.slice(0, 40) + ')');
      await page.click('#rlc-flash .flash-controls .easy');
      await pause(400);
      const s = await page.evaluate(() => {
        const st = Store.getJSON('flash:rlc', []) || [];
        const notees = st.filter(x => x && x.last !== null && x.last !== undefined);
        return { notees, n: FLASH_REGISTRY.rlc.length, prog: document.getElementById('rlc-flash-prog').textContent,
          stats: document.getElementById('rlc-stats').textContent };
      });
      if (s.notees.length !== 1) pb.push(s.notees.length + ' carte(s) notée(s) dans le Store au lieu de 1');
      else {
        const c = s.notees[0];
        if (c.last !== 2 || c.e !== 1) pb.push('état enregistré inattendu : ' + JSON.stringify(c));
        if (c.box !== 1 || !(c.due > Date.now() + 12 * 3600e3)) pb.push('Leitner : box=' + c.box + ', due=' + c.due + ' (attendu box 1, révision dans ~1 jour)');
      }
      if (!new RegExp('Carte 2 / ' + s.n).test(s.prog)) pb.push('progression : « ' + s.prog + ' »');
      if (!/Acquis\s*:\s*1\//.test(s.stats)) pb.push('statistiques : « ' + s.stats + ' »');
      // « Voir le cours » bascule sur l'onglet Cours
      await page.evaluate(() => document.querySelector('#rlc-flash .flash-course-link').click());
      await pause(500);
      const actif = await page.evaluate(() => (document.querySelector('#chap-rlc .panel.active') || {}).id);
      if (actif !== 'rlc-cours') pb.push('« Voir le cours » : onglet actif ' + actif);
      return pb;
    });

    /* ---------- Quiz global ---------- */
    await etape('quiz global : configuration, question, notation, fermeture', async () => {
      const pb = [];
      const compte = () => page.evaluate(() => Object.keys(FLASH_REGISTRY).reduce((n, p) =>
        n + ((Store.getJSON('flash:' + p, []) || []).filter(s => s && s.last !== null && s.last !== undefined).length), 0));
      const avant = await compte();
      await page.click('#study-btn');
      await pause(200);
      await page.click('#quiz-btn');
      await pause(500);
      if (!(await ouvert('quiz-overlay'))) return ['le quiz ne s\'ouvre pas'];
      const info = await page.evaluate(() => document.getElementById('quiz-config-info').textContent);
      if (!/carte/.test(info)) pb.push('configuration : « ' + info + ' »');
      await page.click('#quiz-start-btn');
      await pause(400);
      const q = await page.evaluate(() => ({
        ecran: getComputedStyle(document.getElementById('quiz-screen-question')).display !== 'none',
        texte: document.getElementById('quiz-question-text').textContent.trim(),
        prog: document.getElementById('quiz-progress-text').textContent,
      }));
      if (!q.ecran || !q.texte) return pb.concat(['l\'écran question ne s\'affiche pas']);
      await page.click('#quiz-reveal-btn');
      await pause(250);
      await page.click('#quiz-actions-rate .rate-acq');
      await pause(300);
      const prog2 = await page.evaluate(() => document.getElementById('quiz-progress-text').textContent);
      if (prog2.split('/')[0].trim() !== '2') pb.push('progression après notation : « ' + prog2 + ' » (avant : « ' + q.prog + ' »)');
      const apres = await compte();
      if (apres !== avant + 1) pb.push('cartes notées dans le Store : ' + avant + ' → ' + apres + ' (attendu +1)');
      await page.keyboard.press('Escape');
      await pause(200);
      if (await ouvert('quiz-overlay')) pb.push('Échap ne ferme pas le quiz');
      return pb;
    });

    /* ---------- « Révisions du jour » ---------- */
    await etape('« Réviser » (révisions du jour) sans carte due', async () => {
      await page.click('#study-btn');
      await pause(200);
      await page.click('#revise-btn');
      await pause(400);
      const s = await page.evaluate(() => ({
        ouvert: document.getElementById('quiz-overlay').classList.contains('open'),
        info: document.getElementById('quiz-config-info').textContent,
      }));
      await page.keyboard.press('Escape');
      return [!s.ouvert && 'la fenêtre du quiz ne s\'ouvre pas',
        s.ouvert && !/Aucune carte à réviser/.test(s.info) && 'message attendu « Aucune carte à réviser… », obtenu « ' + s.info + ' »'];
    });

    /* ---------- Bilan ---------- */
    await etape('Bilan : statistiques et clic vers un chapitre', async () => {
      const pb = [];
      await page.click('#dash-btn');
      await pause(400);
      if (!(await ouvert('dash-overlay'))) return ['le Bilan ne s\'ouvre pas'];
      const s = await page.evaluate(() => ({
        texte: document.getElementById('dash-overlay').innerText,
        rlc: !!document.querySelector('#dash-overlay .dash-chap[data-chap="rlc"]'),
      }));
      if (!/%/.test(s.texte) || !/acquises/.test(s.texte)) pb.push('contenu inattendu : ' + s.texte.slice(0, 80).replace(/\s+/g, ' '));
      // liste défilée jusqu'en bas : le titre « Bilan » et le × restent à l'écran (seule la liste défile)
      const fin = await page.evaluate(async () => {
        const ov = document.getElementById('dash-overlay');
        [ov].concat(Array.from(ov.querySelectorAll('*'))).forEach(e => { if (e.scrollHeight > e.clientHeight) e.scrollTop = e.scrollHeight; });
        await new Promise(r => setTimeout(r, 250));
        const x = ov.querySelector('.dash-close').getBoundingClientRect(), t = ov.querySelector('.dash-head h2').getBoundingClientRect();
        const rl = document.querySelector('#dash-overlay .dash-chap[data-chap="rlc"]');
        const v = r => r.top >= 0 && r.bottom <= innerHeight;
        const res = { x: v(x), titre: v(t) };
        if (rl) rl.scrollIntoView({ block: 'center' });
        return res;
      });
      if (!fin.x || !fin.titre) pb.push('Bilan défilé jusqu\'en bas : ' + (!fin.titre ? 'titre ' : '') + (!fin.x ? '× ' : '') + 'hors de l\'écran');
      if (!s.rlc) pb.push('la ligne du chapitre rlc (noté plus haut) est absente');
      else {
        await page.click('#dash-overlay .dash-chap[data-chap="rlc"]');
        await pause(500);
        const actif = await page.evaluate(() => (document.querySelector('#chap-rlc .panel.active') || {}).id);
        if (await ouvert('dash-overlay')) pb.push('le Bilan reste ouvert après le clic');
        if (actif !== 'rlc-flash') pb.push('clic sur rlc : onglet actif ' + actif + ' au lieu de rlc-flash');
      }
      return pb;
    });

    /* ---------- Aujourd'hui ---------- */
    await etape("écran « Aujourd'hui » (bouton de l'en-tête)", async () => {
      await page.click('#today-btn');
      await pause(400);
      const s = await page.evaluate(() => ({
        ouvert: document.getElementById('today-overlay').classList.contains('open'),
        date: document.getElementById('today-date').textContent,
        reprendre: !document.getElementById('today-resume-wrap').hidden,
      }));
      const pb = [!s.ouvert && "l'écran ne s'ouvre pas", s.ouvert && (s.date === '—' || !s.date) && 'date non renseignée',
        s.ouvert && !s.reprendre && 'section « Reprendre » absente alors qu\'un chapitre a été consulté'];
      await page.click('#today-close').catch(() => {});
      await pause(200);
      if (await ouvert('today-overlay')) pb.push('« Continuer » ne ferme pas l\'écran');
      return pb;
    });

    /* ---------- Relance : dernier chapitre consulté, sans « Aujourd'hui » ---------- */
    await etape('relance sans #hash : dernier chapitre consulté, « Aujourd\'hui » fermé', async () => {
      await naviguer(page, autre.id, 'flash');
      await page.goto(ctx.url(), { waitUntil: 'load', timeout: 60000 });
      await attendreApp(page);
      await pause(400);
      const s = await page.evaluate(id => ({
        aujourdhui: document.getElementById('today-overlay').classList.contains('open'),
        panneau: (document.querySelector('#chap-' + id + ' .panel.active') || {}).id,
      }), autre.id);
      s.chap = await visible();
      return [
        s.aujourdhui && "l'écran Aujourd'hui s'ouvre au lancement",
        s.chap !== 'chap-' + autre.id && 'chapitre affiché : ' + s.chap + ' au lieu de chap-' + autre.id,
        s.panneau !== autre.prefix + '-flash' && 'onglet actif : ' + s.panneau + ' au lieu de ' + autre.prefix + '-flash',
      ];
    });

    /* ---------- Fenêtres secondaires ---------- */
    for (const [nom, menu, bouton, fenetre] of [
      ['formulaire du chapitre', '#more-btn', '#formula-btn', 'formula-overlay'],
      ['cartes signalées', '#more-btn', '#flag-btn', 'flag-overlay'],
      ['calcul mental', '#study-btn', '#drill-btn', 'drill-overlay'],
    ]) {
      await etape('fenêtre « ' + nom + ' » : ouverture, raccourcis de la page inactifs derrière, Échap', async () => {
        await naviguer(page, 'rlc', 'cours');
        await page.click(menu);
        await pause(200);
        await page.click(bouton);
        await pause(500);
        const s = await page.evaluate(id => { const o = document.getElementById(id); return o ? { ouvert: o.classList.contains('open'), n: o.innerText.trim().length } : null; }, fenetre);
        if (!s) return ['#' + fenetre + ' absent'];
        const avant = await visible();
        await page.keyboard.press('n');            // « chapitre suivant » : sans effet derrière une fenêtre
        await pause(400);
        const apres = await visible();
        await page.keyboard.press('Escape');
        await pause(200);
        return [!s.ouvert && 'la fenêtre ne s\'ouvre pas', s.ouvert && s.n < 20 && 'fenêtre vide',
          apres !== avant && 'la touche n change de chapitre derrière la fenêtre (' + apres + ')',
          (await ouvert(fenetre)) && 'Échap ne ferme pas la fenêtre'];
      });
    }

    /* ---------- Formulaire : jamais d'entrée vers une fenêtre vide ----------
       43 chapitres (anglais, info, une partie des maths et de la SI) n'ont aucune formule à
       regrouper : l'action « Formulaire » de l'intercalaire, du menu Plus et d'Aujourd'hui y est
       masquée ; ailleurs (rlc), elle est affichée et la fenêtre contient des formules. */
    await etape('Formulaire : entrées masquées sans formule à regrouper (fonctions, anglais), affichées et fenêtre remplie sinon (rlc)', async () => {
      const pb = [];
      const ang = await page.evaluate(() => (CHAPTERS.find(x => x.matiere === 'anglais') || {}).id);
      for (const [id, attendu] of [['rlc', true], ['fonctions', false], [ang, false]]) {
        if (!id) continue;
        await naviguer(page, id, 'cours');
        const ctb = await page.evaluate(i => { const b = document.querySelector('#chap-' + i + ' .chap-title-banner [data-ctb="formulaire"]'); return !!(b && b.getClientRects().length); }, id);
        await page.click('#more-btn'); await pause(250);
        const menu = await page.evaluate(() => !!document.getElementById('formula-btn').getClientRects().length);
        await page.keyboard.press('Escape'); await pause(200);
        await page.evaluate(() => window.todayOpen()); await pause(300);
        const auj = await page.evaluate(() => !!document.getElementById('today-formula').getClientRects().length);
        await page.keyboard.press('Escape'); await pause(200);
        if (ctb !== attendu || menu !== attendu || auj !== attendu) pb.push(id + ' : « Formulaire » ' + (attendu ? 'masqué' : 'affiché') + ' (intercalaire ' + ctb + ', menu Plus ' + menu + ', Aujourd\'hui ' + auj + ')');
        if (attendu) {
          await page.click('#chap-' + id + ' .chap-title-banner [data-ctb="formulaire"]');
          await page.waitForFunction(() => !/Préparation/.test(document.getElementById('formula-body').textContent), null, { timeout: 15000 }).catch(() => {});
          const n = await page.evaluate(() => document.querySelectorAll('#formula-body .fsheet-f').length);
          if (!n) pb.push(id + ' : fenêtre Formulaire sans formule');
          await page.keyboard.press('Escape'); await pause(200);
        }
      }
      return pb;
    });

    /* ---------- Focus des fenêtres (relecture accessibilité, tour 1) ----------
       Tab depuis le dernier élément et Maj+Tab depuis le premier restent dans la fenêtre ;
       Échap rend le focus au bouton qui l'a ouverte (ou au bouton du menu d'origine). Les
       éléments atteignables sont calculés ici, indépendamment du site (sans les <use href>). */
    await etape('fenêtres : focus piégé (Tab, Maj+Tab) et rendu au bouton d\'origine (Échap)', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      const bord = (id, dernier) => page.evaluate(([id, dernier]) => {
        const ov = document.getElementById(id);
        const f = Array.from(ov.querySelectorAll('a[href], button, input, select, textarea, [tabindex]'))
          .filter(e => e.tabIndex >= 0 && !e.disabled && e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden');
        const e = dernier ? f[f.length - 1] : f[0];
        if (e) e.focus();
        return !!e && document.activeElement === e;
      }, [id, dernier]);
      const dedans = id => page.evaluate(id => document.getElementById(id).contains(document.activeElement), id);
      for (const [nom, menu, bouton, fenetre, retour] of [
        ['Aujourd\'hui', null, '#today-btn', 'today-overlay', 'today-btn'],
        ['Bilan', null, '#dash-btn', 'dash-overlay', 'dash-btn'],
        ['quiz (configuration)', '#study-btn', '#quiz-btn', 'quiz-overlay', 'study-btn'],
        ['formulaire', '#more-btn', '#formula-btn', 'formula-overlay', 'more-btn'],
      ]) {
        if (menu) { await page.focus(menu); await page.keyboard.press('Enter'); await pause(300); }
        await page.focus(bouton); await page.keyboard.press('Enter'); await pause(600);
        if (!(await ouvert(fenetre))) { pb.push(nom + ' : la fenêtre ne s\'ouvre pas'); await fermerOverlays(page).catch(() => {}); continue; }
        // juste après l'ouverture, le focus est sur la boîte (tabindex=-1) : Maj+Tab natif sortait derrière
        await page.keyboard.press('Shift+Tab'); await pause(80);
        if (!(await dedans(fenetre))) pb.push(nom + ' : Maj+Tab juste après l\'ouverture (focus sur la boîte) sort de la fenêtre');
        if (!(await bord(fenetre, true))) pb.push(nom + ' : dernier élément non focalisable');
        await page.keyboard.press('Tab'); await pause(80);
        if (!(await dedans(fenetre))) pb.push(nom + ' : Tab depuis le dernier élément sort de la fenêtre');
        await bord(fenetre, false);
        await page.keyboard.press('Shift+Tab'); await pause(80);
        if (!(await dedans(fenetre))) pb.push(nom + ' : Maj+Tab depuis le premier élément sort de la fenêtre');
        await page.keyboard.press('Escape'); await pause(500);
        const a = await page.evaluate(() => document.activeElement && document.activeElement !== document.body ? document.activeElement.id || document.activeElement.className : 'BODY');
        if (a !== retour) pb.push(nom + ' : focus rendu à ' + a + ' au lieu de #' + retour);
      }
      return pb;
    });

    /* ---------- Année : passage automatique réversible (relecture fonctionnelle, tour 1) ---------- */
    await etape('année : un chapitre de 2ᵉ année ouvert en passant ne laisse pas la 2ᵉ année acquise ; un choix manuel reste', async () => {
      const annee = () => page.evaluate(() => ({ store: Store.get('year'), courante: window.__currentYear() }));
      const choisir = y => page.evaluate(y => { const b = document.querySelector('.mob-year-btn[data-year="' + y + '"]'); if (b) b.click(); return !!b; }, y);
      await naviguer(page, 'rlc', 'cours');
      await choisir(1); await pause(200);
      await naviguer(page, 'fpv', 'cours');                // chapitre de 2ᵉ année : passage automatique
      const a = await annee();
      await naviguer(page, 'rlc', 'cours');                // retour à la 1ʳᵉ année
      const b = await annee();
      await choisir(2); await pause(200);                   // 2ᵉ année choisie à la main
      const chap = await visible();
      await naviguer(page, 'signaux', 'cours');
      const c = await annee();
      await choisir(1); await pause(200);
      return [
        a.courante !== 2 && 'chapitre de 2ᵉ année : année courante ' + a.courante + ' au lieu de 2',
        b.courante !== 1 && 'retour à un chapitre de 1ʳᵉ année : année courante ' + b.courante + ' (Store ' + b.store + ') au lieu de 1',
        chap !== 'chap-rlc' && 'la bascule d\'année change le chapitre affiché (' + chap + ')',
        c.courante !== 2 && '2ᵉ année choisie à la main puis chapitre de 1ʳᵉ année : année ' + c.courante + ' au lieu de 2',
      ];
    });

    /* ---------- « Dans ce chapitre » sans rail (1100 px) ---------- */
    await etape('« Dans ce chapitre » dans le menu Plus à 1100 px (pas de rail)', async () => {
      const taille = page.viewportSize();
      await page.setViewportSize({ width: 1100, height: 850 });
      await pause(400);
      await naviguer(page, 'rlc', 'cours');
      await page.click('#more-btn'); await pause(300);
      const s = await page.evaluate(() => {
        const t = document.getElementById('more-toc');
        return { visible: !!(t && !t.hidden && t.getClientRects().length), n: t ? t.querySelectorAll('.more-toc-list > *').length : 0, rail: !!document.querySelector('#chap-rail .toc-item, #chap-rail .rail-bloc') && !!(document.getElementById('chap-rail') || {}).offsetParent };
      });
      await page.keyboard.press('Escape'); await pause(200);
      await page.setViewportSize(taille); await pause(400);
      return [!s.visible && !s.rail && 'ni rail ni « Dans ce chapitre » dans le menu Plus à 1100 px',
        s.visible && s.n < 3 && '« Dans ce chapitre » ne liste que ' + s.n + ' section(s)'];
    });

    /* ---------- Bilan : « Réviser mes points faibles » = cartes faibles seulement ---------- */
    await etape('Bilan : « Réviser mes points faibles » lance autant de cartes que son compteur (jamais vues exclues)', async () => {
      await naviguer(page, 'rlc', 'flash');
      await page.evaluate(() => { const f = window.FLASH_INSTANCES.rlc; f.rate(0); f.rate(1); f.rate(2); });
      await pause(200);
      await page.click('#dash-btn'); await pause(700);
      const n = await page.evaluate(() => { const b = document.getElementById('dash-revise-btn'); return b ? parseInt(b.querySelector('.count').textContent, 10) : null; });
      if (n === null) return ['bouton « Réviser mes points faibles » absent après deux cartes faibles'];
      await page.click('#dash-revise-btn'); await pause(700);
      const p = await page.evaluate(() => (document.getElementById('quiz-progress-text') || {}).textContent || '');
      const total = parseInt((p.split('/')[1] || '').trim(), 10);
      return [total !== n && 'le quiz lancé compte ' + total + ' carte(s) pour un compteur de ' + n + ' (« ' + p + ' »)'];
    });


    /* ---------- Onglet Cartes (ordinateur) : notation au-dessus du pli, quel que soit le titre ---------- */
    await etape('onglet Cartes à 1280 × 800 : « Afficher la réponse » et la notation au-dessus du pli (titres de 1, 2 et 3 lignes)', async () => {
      const pb = [];
      const taille = page.viewportSize();
      await page.setViewportSize({ width: 1280, height: 800 }); await pause(400);
      for (const id of ['rlc', 'thermoouv', 'signum']) {
        await naviguer(page, id, 'flash');
        await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, 0); });
        await pause(500);
        const m = await page.evaluate(id => {
          const p = document.getElementById(CHAPTERS_BY_ID[id].prefix + '-flash');
          const r = p && Array.from(p.querySelectorAll('.fc-reveal')).find(b => b.getClientRects().length);
          const t = document.querySelector('#chap-' + id + ' > .chap-title-banner .ctb-title');
          return { bas: r ? Math.round(r.getBoundingClientRect().bottom) : null, vh: innerHeight,
            lignes: t ? Math.round(t.getBoundingClientRect().height / (parseFloat(getComputedStyle(t).lineHeight) || 1)) : 0 };
        }, id);
        if (m.bas === null) { pb.push(id + ' : « Afficher la réponse » introuvable'); continue; }
        if (m.bas > m.vh) pb.push(id + ' (titre sur ' + m.lignes + ' ligne(s)) : « Afficher la réponse » finit à ' + m.bas + ' px pour ' + m.vh);
        await page.evaluate(id => window.FLASH_INSTANCES[CHAPTERS_BY_ID[id].prefix].flip(), id); await pause(500);
        const n = await page.evaluate(id => {
          const c = document.querySelector('#' + CHAPTERS_BY_ID[id].prefix + '-flash .flash-controls');
          return c && c.getClientRects().length ? Math.round(c.getBoundingClientRect().bottom) : null;
        }, id);
        if (n === null || n > m.vh) pb.push(id + ' : notation ' + (n === null ? 'absente' : 'finit à ' + n + ' px') + ' pour ' + m.vh);
        await page.evaluate(id => window.FLASH_INSTANCES[CHAPTERS_BY_ID[id].prefix].flip(), id); await pause(400);
      }
      await page.setViewportSize(taille); await pause(400);
      return pb;
    });

    /* ---------- Clavier : focus après le choix d'un chapitre, parcours d'une fiche et du quiz ---------- */
    await etape('clavier : focus après le choix d\'un chapitre (barre latérale), parcours d\'une fiche et du quiz sans chute sur <body>', async () => {
      const pb = [];
      const actif = () => page.evaluate(() => { const a = document.activeElement; return !a || a === document.body ? 'BODY' : (a.id ? '#' + a.id : '') + '.' + String(a.className || '').split(' ').join('.'); });
      await naviguer(page, 'rlc', 'cours');
      const ok = await page.evaluate(() => { const b = document.querySelector('#mob-chap-list .mob-chap-row[data-id="chap-signaux"] .mob-chap-item'); if (b) b.focus(); return !!b && document.activeElement === b; });
      if (!ok) pb.push('rangée « Signaux » introuvable dans la barre latérale');
      else {
        await page.keyboard.press('Enter'); await pause(700);
        const a = await actif();
        const ch = await visible();
        if (ch !== 'chap-signaux') pb.push('Entrée sur la rangée n\'ouvre pas le chapitre (' + ch + ')');
        if (a === 'BODY') pb.push('après le choix d\'un chapitre au clavier, le focus tombe sur <body>');
        const titre = await page.evaluate(() => document.title);
        if (!/Signaux/.test(titre)) pb.push('titre du document non mis à jour : « ' + titre + ' »');
      }
      // fiche : Afficher la réponse → 1re note ; note → Afficher la réponse
      await naviguer(page, 'rlc', 'flash');
      const rev = await page.evaluate(() => { const b = Array.from(document.querySelectorAll('#rlc-flash .fc-reveal')).find(x => x.getClientRects().length); if (b) b.focus(); return !!b && document.activeElement === b; });
      if (!rev) pb.push('« Afficher la réponse » non focalisable');
      else {
        await page.keyboard.press('Enter'); await pause(600);
        const a1 = await actif();
        if (!/flash-controls|hard|ok|easy/.test(a1) && !(await page.evaluate(() => !!(document.activeElement && document.activeElement.closest && document.activeElement.closest('.flash-controls'))))) pb.push('fiche : après « Afficher la réponse », focus sur ' + a1 + ' au lieu d\'une note');
        await page.keyboard.press('Enter'); await pause(600);
        const a2 = await page.evaluate(() => !!(document.activeElement && document.activeElement.classList && document.activeElement.classList.contains('fc-reveal')));
        if (!a2) pb.push('fiche : après la note, focus sur ' + (await actif()) + ' au lieu de « Afficher la réponse »');
      }
      // quiz : Commencer → Afficher la réponse → note → Afficher la réponse
      await page.evaluate(() => window.quizOpen()); await pause(500);
      await page.focus('#quiz-start-btn'); await page.keyboard.press('Enter'); await pause(600);
      if ((await actif()).indexOf('#quiz-reveal-btn') !== 0) pb.push('quiz : après « Commencer », focus sur ' + (await actif()));
      await page.keyboard.press('Enter'); await pause(600);
      if (!/quiz-rate-btn/.test(await actif())) pb.push('quiz : après « Afficher la réponse », focus sur ' + (await actif()));
      await page.keyboard.press('Enter'); await pause(600);
      if (!/quiz-reveal-btn|quiz-results/.test(await actif()) && (await actif()) === 'BODY') pb.push('quiz : après la note, le focus tombe sur <body>');
      const nom = await page.evaluate(() => { const b = document.getElementById('quiz-reveal-btn'); return b ? [b.getAttribute('aria-keyshortcuts'), (b.querySelector('.kbd-hint') || {}).getAttribute && b.querySelector('.kbd-hint').getAttribute('aria-hidden')] : []; });
      if (nom[0] !== 'Space' || nom[1] !== 'true') pb.push('« Afficher la réponse » : aria-keyshortcuts=' + nom[0] + ', aide clavier aria-hidden=' + nom[1]);
      return pb;
    });

    /* ---------- Focus jamais caché sous l'en-tête et les onglets collants (WCAG 2.4.11) ----------
       Maj+Tab en remontant les Exercices : le navigateur alignait l'élément focalisé sur le bord
       haut de la fenêtre, sous 103 px de barres (scroll-padding-top sur html). */
    await etape('Maj+Tab sur #rlc/exos : l\'élément focalisé n\'est jamais caché sous l\'en-tête et les onglets collants', async () => {
      const pb = [];
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await naviguer(page, 'rlc', 'exos');
      await page.evaluate(() => document.getElementById('next-chap-btn').focus());
      await pause(200);
      let vus = 0;
      for (let i = 0; i < 18; i++) {
        await page.keyboard.press('Shift+Tab'); await pause(120);
        const r = await page.evaluate(() => {
          const a = document.activeElement, p = document.getElementById('rlc-exos');
          if (!a || !p || !p.contains(a)) return null;
          const t = document.querySelector('#chap-rlc > nav.tabs').getBoundingClientRect(), b = a.getBoundingClientRect();
          return { el: (a.className || a.tagName).toString().split(' ')[0] + ' «' + (a.textContent || '').trim().slice(0, 20) + '»', haut: Math.round(b.top), onglets: Math.round(t.bottom) };
        });
        if (!r) continue;
        vus++;
        if (r.haut < r.onglets - 1) pb.push(r.el + ' : haut à ' + r.haut + ' px, sous les onglets collés (bas à ' + r.onglets + ' px)');
      }
      if (!vus) pb.push('aucun élément du panneau Exercices atteint par Maj+Tab');
      await page.emulateMedia({ reducedMotion: null });
      return pb.slice(0, 5);
    });

    /* ---------- Blocs dépliables : intitulé = vrai bouton, contenu HORS du bouton ; solutions ----------
       Un .reveal entier en role=button faisait de tout son contenu déplié (texte, formules) le nom
       d'un seul bouton ; « Voir la solution » n'avait aucun état avant le 1er clic, puis changeait de
       libellé EN PLUS d'aria-expanded (état annoncé deux fois). */
    await etape('blocs dépliables (.reveal, « Voir la solution ») : bouton d\'intitulé, aria-expanded dès l\'affichage, libellé fixe, Entrée / Espace', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      const src = await page.evaluate(() => {
        const rs = Array.from(document.querySelectorAll('.chapter .reveal'));
        return { n: rs.length,
          role: rs.filter(r => r.hasAttribute('role') || r.hasAttribute('tabindex')).length,
          sansBouton: rs.filter(r => { const b = r.querySelector(':scope > .reveal-btn'); return !b || !b.getAttribute('aria-controls') || !document.getElementById(b.getAttribute('aria-controls')); }).length,
          // (une formule EN LIGNE dans la question de l'intitulé est permise : « Calculer ω0 et Q pour R = 10 Ω »)
          contenuDansBouton: rs.filter(r => r.querySelector('.reveal-btn .content, .reveal-btn p, .reveal-btn mjx-container[display="true"]')).length };
      });
      if (!src.n) pb.push('aucun .reveal dans les chapitres');
      if (src.role) pb.push(src.role + ' .reveal encore en role=button / tabindex (tout le contenu devient le nom du bouton)');
      if (src.sansBouton) pb.push(src.sansBouton + ' .reveal sans bouton d\'intitulé relié à son contenu (aria-controls)');
      if (src.contenuDansBouton) pb.push(src.contenuDansBouton + ' .reveal dont le contenu est DANS le bouton');
      const sel = '#rlc-cours .reveal';
      await page.evaluate(s => { const b = document.querySelector(s + ' > .reveal-btn'); b.scrollIntoView({ block: 'center' }); b.focus(); }, sel);
      await page.keyboard.press('Enter'); await pause(300);
      const ouvert = await page.evaluate(s => { const r = document.querySelector(s), b = r.querySelector(':scope > .reveal-btn'); return [r.classList.contains('open'), b.getAttribute('aria-expanded'), b.textContent.length < 200]; }, sel);
      if (!ouvert[0] || ouvert[1] !== 'true') pb.push('Entrée sur l\'intitulé du 1er mémo : open=' + ouvert[0] + ', aria-expanded=' + ouvert[1]);
      if (!ouvert[2]) pb.push('nom du bouton du mémo déplié trop long (contenu inclus ?)');
      await page.keyboard.press(' '); await pause(300);
      const ferme = await page.evaluate(s => { const r = document.querySelector(s); return [r.classList.contains('open'), r.querySelector(':scope > .reveal-btn').getAttribute('aria-expanded')]; }, sel);
      if (ferme[0] || ferme[1] !== 'false') pb.push('Espace sur l\'intitulé du mémo déplié : open=' + ferme[0] + ', aria-expanded=' + ferme[1]);
      await naviguer(page, 'rlc', 'exos');
      const sols = await page.evaluate(() => Array.from(document.querySelectorAll('#rlc-exos .toggle-sol')).map(b => [b.getAttribute('aria-expanded'), !!document.getElementById(b.getAttribute('aria-controls') || '-')]));
      if (!sols.length) pb.push('aucun « Voir la solution » dans rlc-exos');
      const sansEtat = sols.filter(s => s[0] !== 'false' || !s[1]).length;
      if (sansEtat) pb.push(sansEtat + ' « Voir la solution » sans aria-expanded="false" ni aria-controls avant le 1er clic');
      const ts = '#rlc-exos .toggle-sol';
      const avant = await page.evaluate(s => { const b = document.querySelector(s); b.scrollIntoView({ block: 'center' }); b.focus(); return b.textContent.trim(); }, ts);
      await page.keyboard.press('Enter'); await pause(400);
      const apres = await page.evaluate(s => { const b = document.querySelector(s); return [b.textContent.trim(), b.getAttribute('aria-expanded'), b.nextElementSibling.classList.contains('shown')]; }, ts);
      if (apres[1] !== 'true' || !apres[2]) pb.push('Entrée sur « ' + avant + ' » : aria-expanded=' + apres[1] + ', solution affichée=' + apres[2]);
      if (apres[0] !== avant) pb.push('libellé changé au dépliage (« ' + avant + ' » → « ' + apres[0] + ' ») en plus d\'aria-expanded');
      await page.keyboard.press('Enter'); await pause(300);
      return pb;
    });

    /* ---------- Tiroir modal et menu ouvert à la souris : raccourcis muets derrière ---------- */
    await etape('tiroir modal (1024 px) et menu Plus ouvert à la souris : role=dialog, arrière-plan inerte, « n » sans effet', async () => {
      const pb = [];
      const taille = page.viewportSize();
      await page.setViewportSize({ width: 1024, height: 800 }); await pause(400);
      await naviguer(page, 'rlc', 'cours');
      const h0 = await page.evaluate(() => location.hash);
      await page.click('#nav-toggle-btn'); await pause(600);
      // arrière-plan : #app-main (le chapitre, très lourd) hors de l'arbre d'accessibilité par
      // aria-hidden (inert y recalculait le style de tout le chapitre : ≈ 0,8 s au téléphone),
      // le reste (en-têtes, « haut de page », lien d'évitement) inerte ; focus jamais dans le chapitre
      const arr = () => page.evaluate(() => { const am = document.getElementById('app-main'); return { cache: am.getAttribute('aria-hidden'), inertAm: !!am.inert,
        inert: ['site-header', 'mob-header', 'back-to-top', 'skip-link'].filter(id => { const e = document.getElementById(id); return e && e.inert; }).length }; });
      const t = await page.evaluate(() => { const d = document.getElementById('mob-drawer'); return { open: d.classList.contains('open'), role: d.getAttribute('role'), modal: d.getAttribute('aria-modal') }; });
      const ta = await arr();
      if (!t.open) pb.push('le tiroir ne s\'ouvre pas à 1024 px');
      if (t.role !== 'dialog' || t.modal !== 'true') pb.push('tiroir ouvert : role=' + t.role + ', aria-modal=' + t.modal);
      if (ta.cache !== 'true') pb.push('tiroir ouvert : #app-main sans aria-hidden="true" (arrière-plan lu par les lecteurs d\'écran)');
      if (ta.inertAm) pb.push('tiroir ouvert : #app-main rendu inerte (recalcul du style de tout le chapitre)');
      if (ta.inert < 2) pb.push('tiroir ouvert : en-têtes non inertes (' + ta.inert + ')');
      const fuite = await page.evaluate(() => { const b = document.querySelector('#app-main .tab'); if (b) b.focus(); const a = document.activeElement; return !!(a && document.getElementById('app-main').contains(a)); });
      if (fuite) pb.push('tiroir ouvert : le focus peut entrer dans le chapitre caché derrière');
      for (const k of ['n', '3', 'g']) { await page.keyboard.press(k); await pause(250); }
      const h1 = await page.evaluate(() => location.hash);
      if (h1 !== h0) pb.push('touches n / 3 / g derrière le tiroir : ' + h0 + ' → ' + h1);
      await page.keyboard.press('Escape'); await pause(500);
      const f = await page.evaluate(() => document.getElementById('mob-drawer').getAttribute('role'));
      const fa = await arr();
      if (f || fa.cache !== null || fa.inert) pb.push('tiroir refermé : role=' + f + ', aria-hidden sur #app-main=' + fa.cache + ', éléments inertes=' + fa.inert);
      await page.setViewportSize(taille); await pause(400);
      await naviguer(page, 'rlc', 'cours');
      await page.click('#more-btn'); await pause(300);
      await page.keyboard.press('n'); await pause(400);
      const h2 = await page.evaluate(() => location.hash);
      if (h2 !== h0) pb.push('« n » avec le menu Plus ouvert à la souris : ' + h0 + ' → ' + h2);
      await page.keyboard.press('Escape'); await pause(200);
      return pb;
    });

    /* ---------- Contraste élevé : appliqué dans les deux thèmes ---------- */
    await etape('contraste élevé (prefers-contrast: more) : encre 3 = encre 2 et filets = --field, en clair ET en sombre', async () => {
      const pb = [];
      await page.emulateMedia({ contrast: 'more' }); await pause(200);
      for (const th of ['light', 'dark']) {
        await page.evaluate(t => window.__setTheme(t), th); await pause(300);
        const v = await page.evaluate(() => { const c = getComputedStyle(document.documentElement); const g = n => c.getPropertyValue(n).trim(); return { t3: g('--text-3'), t2: g('--text-2'), line: g('--line'), field: g('--field') }; });
        if (v.t3 !== v.t2) pb.push(th + ' : --text-3 ' + v.t3 + ' ≠ --text-2 ' + v.t2);
        if (v.line !== v.field) pb.push(th + ' : --line ' + v.line + ' ≠ --field ' + v.field);
      }
      await page.emulateMedia({ contrast: null }); await page.evaluate(() => window.__setTheme('light')); await pause(300);
      return pb;
    });

    /* ---------- Couleurs forcées (contraste élevé de Windows) : repères d'état conservés ---------- */
    await etape('couleurs forcées (forced-colors: active) : soulignement de l\'onglet actif, intercalaire et rangée courante visibles', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'flash');
      await page.emulateMedia({ forcedColors: 'active' }); await pause(300);
      const r = await page.evaluate(() => {
        const sys = document.createElement('span'); sys.style.cssText = 'position:absolute;forced-color-adjust:none;color:Highlight'; document.body.appendChild(sys);
        const hl = getComputedStyle(sys).color; sys.remove();
        const t = document.querySelector('#chap-rlc > nav.tabs .tab.active'), m = document.querySelector('.mat-tab.active'), row = document.querySelector('#mob-chap-list .mob-chap-row.cur');
        return { hl, souligne: t ? getComputedStyle(t, '::after').backgroundColor : '', inter: m ? getComputedStyle(m).outlineStyle : 'absent', rail: row ? getComputedStyle(row, '::before').backgroundColor : null };
      });
      if (r.souligne !== r.hl) pb.push('onglet actif : soulignement ' + r.souligne + ' (Highlight = ' + r.hl + ')');
      if (r.inter !== 'solid') pb.push('intercalaire de matière actif sans contour (' + r.inter + ')');
      if (r.rail !== null && r.rail !== r.hl) pb.push('rangée courante de la navigation : rail ' + r.rail);
      await page.emulateMedia({ forcedColors: 'none' }); await pause(200);
      return pb;
    });

    /* ---------- Recherche : frappe légère (composition à la pause), liste MathJax stable ---------- */
    await etape('recherche : aucune composition MathJax pendant la frappe, composition à la pause, liste interne de MathJax stable', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      await page.click('#search-btn'); await pause(500);
      await page.keyboard.type('pulsation propre', { delay: 40 });
      await pause(120);
      const pendant = await page.evaluate(() => document.querySelectorAll('#search-results mjx-container').length);
      if (pendant) pb.push(pendant + ' formule(s) composée(s) 120 ms après la dernière touche (composition à chaque frappe)');
      await pause(2500);
      const apres = await page.evaluate(() => document.querySelectorAll('#search-results mjx-container').length);
      if (!apres) pb.push('aucune formule composée dans les résultats après la pause');
      const n = () => page.evaluate(() => { try { return Array.from(MathJax.startup.document.math).length; } catch (e) { return -1; } });
      const avant = await n();
      for (let i = 0; i < 10; i++) { await page.fill('#search-input', ['champ électrique', 'impédance', 'énergie cinétique'][i % 3] + ' '.repeat(i % 2)); await pause(700); }
      await page.fill('#search-input', 'pulsation propre'); await pause(2500);
      const fin = await n();
      if (avant >= 0 && fin - avant > 50) pb.push('liste interne de MathJax : ' + avant + ' → ' + fin + ' après 10 recherches (formules des anciens résultats jamais retirées)');
      await page.keyboard.press('Escape'); await pause(200);
      return pb;
    });

    /* ---------- Impression de l'onglet Exercices filtré ---------- */
    await etape('impression de l\'onglet Exercices filtré : exercices affichés seulement, sélection indiquée en page de garde', async () => {
      await naviguer(page, 'rlc', 'exos'); await pause(300);
      const ok = await page.evaluate(() => { const b = document.querySelector('#rlc-exos .exo-tools button[data-niveau="3"]'); if (b) b.click(); return !!b; });
      if (!ok) return ['filtre de difficulté absent de rlc-exos'];
      await pause(300);
      const vus = await page.evaluate(() => Array.from(document.querySelectorAll('#rlc-exos .exo')).filter(e => !e.classList.contains('filtre-masque')).length);
      await page.evaluate(() => { window.print = () => {}; printChapter(); });
      await pause(2500);
      const s = await page.evaluate(() => {
        const f = document.getElementById('print-iframe'); const d = f && f.contentDocument;
        return d ? { blocs: d.querySelectorAll('.sec-block').length, sel: (d.querySelector('.cover-selection') || {}).textContent || '' } : null;
      });
      await page.evaluate(() => { const b = document.querySelector('#rlc-exos .exo-tools button[data-niveau="tous"]'); if (b) b.click(); });
      if (!s) return ['aucune iframe d\'impression générée'];
      return [s.blocs !== vus && s.blocs + ' exercice(s) imprimé(s) pour ' + vus + ' affiché(s)', !/Difficile/.test(s.sel) && 'sélection absente de la page de garde (« ' + s.sel + ' »)'];
    });

    /* ---------- Recherche groupée et aide clavier ---------- */
    await etape('recherche groupée par nature (matière de chaque ligne, ↓) ; aide clavier (« ? » et menu Plus › Raccourcis) et Échap', async () => {
      const pb = [];
      await naviguer(page, 'rlc', 'cours');
      await page.keyboard.press('Control+k');
      await pause(250);
      await page.fill('#search-input', 'bobine');
      await pause(500);
      const r = await page.evaluate(() => {
        const lignes = Array.from(document.querySelectorAll('#search-results .search-result'));
        return { groupes: Array.from(document.querySelectorAll('#search-results .sr-groupe-titre > span:first-child'), e => e.textContent),
          n: lignes.length, sansMat: lignes.filter(e => !e.dataset.mat).length, sel: lignes.filter(e => e.classList.contains('sel')).length };
      });
      if (r.groupes.length < 2) pb.push('résultats de « bobine » non groupés par nature (' + r.groupes.join(', ') + ')');
      if (r.sansMat) pb.push(r.sansMat + ' résultat(s) sans matière (data-mat)');
      if (r.sel !== 1) pb.push(r.sel + ' ligne(s) active(s) au lieu de 1');
      await page.keyboard.press('ArrowDown');
      const i = await page.evaluate(() => { const s = document.querySelector('#search-results .search-result.sel'); return s ? +s.dataset.i : -1; });
      if (r.n > 1 && i !== 1) pb.push('↓ ne choisit pas la 2ᵉ ligne (ligne ' + i + ')');
      await page.keyboard.press('Escape');
      await pause(200);
      if (await ouvert('search-overlay')) pb.push('Échap ne ferme pas la recherche');
      await page.keyboard.press('?');
      await pause(300);
      if (!(await ouvert('key-help-modal'))) pb.push('« ? » n\'ouvre pas l\'aide clavier');
      else {
        await page.keyboard.press('Escape');
        await pause(200);
        if (await ouvert('key-help-modal')) pb.push('Échap ne ferme pas l\'aide clavier');
      }
      // Entrée « Raccourcis » du menu Plus (souris, puis clavier) : ouvre l'aide ; Échap rend le focus à ⋯
      for (const mode of ['souris', 'clavier']) {
        if (mode === 'souris') { await page.click('#more-btn'); await pause(300); await page.click('#keys-btn'); }
        else { await page.focus('#more-btn'); await page.keyboard.press('Enter'); await pause(300); await page.focus('#keys-btn'); await page.keyboard.press('Enter'); }
        await pause(400);
        if (!(await ouvert('key-help-modal'))) { pb.push('menu Plus › Raccourcis (' + mode + ') n\'ouvre pas l\'aide clavier'); continue; }
        if (await ouvert('more-menu')) pb.push('menu Plus › Raccourcis (' + mode + ') : le menu reste ouvert');
        await page.keyboard.press('Escape'); await pause(300);
        const f = await page.evaluate(() => (document.activeElement || {}).id || 'BODY');
        if (f !== 'more-btn') pb.push('menu Plus › Raccourcis (' + mode + ') puis Échap : focus sur ' + f + ' au lieu de #more-btn');
      }
      return pb;
    });

    /* ---------- Impression (génération de l'iframe seulement) ---------- */
    await etape('impression du chapitre (document généré)', async () => {
      await naviguer(page, 'rlc', 'cours');
      await page.evaluate(() => { window.print = () => {}; printChapter(); });
      await pause(2500);
      const s = await page.evaluate(() => {
        const f = document.getElementById('print-iframe') || Array.from(document.querySelectorAll('iframe')).pop();
        try { const d = f && f.contentDocument; return d ? { titre: d.title, texte: d.body ? d.body.innerText.length : 0, base: !!d.querySelector('base') } : null; }
        catch (e) { return { erreur: e.message }; }
      });
      if (!s) return ['aucune iframe d\'impression générée'];
      return [s.erreur && s.erreur, !s.erreur && s.texte < 200 && 'document d\'impression quasi vide (' + s.texte + ' caractères)',
        !s.erreur && !s.base && 'balise <base> absente (les chemins vendor/… ne résoudraient pas)'];
    });

    /* ---------- Lecture audio des cartes d'anglais (présence du bouton) ---------- */
    await etape('bouton de lecture audio sur une flashcard d\'anglais', async () => {
      const ang = await page.evaluate(() => { const c = CHAPTERS.find(x => x.matiere === 'anglais' && x.panels.includes('flash')); return c && c.id; });
      if (!ang) return [];
      await naviguer(page, ang, 'flash');
      const s = await page.evaluate(id => ({ ok: !!(window.__TTS && window.__TTS.ok), btn: !!document.querySelector('#chap-' + id + ' .flash-tts-btn') }), ang);
      return [s.ok && !s.btn && 'bouton .flash-tts-btn absent alors que la synthèse vocale est disponible'];
    });

    /* ---------- Raccourcis des cartes : tous les decks, garde de saisie, rien derrière le quiz ---------- */
    await etape('raccourcis des cartes (Espace, 1/2/3, flèches) sur un deck quelconque, garde de saisie et quiz', async () => {
      const pb = [];
      await naviguer(page, autre.id, 'flash');
      await pause(300);
      const lire = () => page.evaluate(p => ({
        verso: !!(FLASH_INSTANCES[p] && FLASH_INSTANCES[p].isFlipped && FLASH_INSTANCES[p].isFlipped()),
        panneau: (Array.from(document.querySelectorAll('.chapter.active .panel.active')).find(x => x.offsetParent) || {}).id,
        chap: (Array.from(document.querySelectorAll('.chapter.active')).find(x => x.offsetParent) || {}).id,
        notees: (Store.getJSON('flash:' + p, []) || []).filter(s => s && s.last !== null && s.last !== undefined).length,
        prog: (document.getElementById(p + '-flash-prog') || {}).textContent || '',
      }), autre.prefix);
      await page.evaluate(() => { if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); });
      const s0 = await lire();
      await page.keyboard.press('2'); await pause(250);
      const s1 = await lire();
      if (s1.panneau !== autre.prefix + '-flash') pb.push('« 2 » au recto a changé d\'onglet (' + s1.panneau + ')');
      if (s1.notees !== s0.notees) pb.push('« 2 » au recto a noté une carte');
      await page.keyboard.press(' '); await pause(500);
      const s2 = await lire();
      if (!s2.verso) pb.push('Espace ne retourne pas la carte (' + autre.prefix + ')');
      await page.keyboard.press('3'); await pause(400);
      const s3 = await lire();
      if (s3.notees !== s0.notees + 1) pb.push('« 3 » au verso : ' + (s3.notees - s0.notees) + ' carte(s) notée(s) au lieu de 1');
      if (s3.verso) pb.push('après « 3 », la carte suivante est restée au verso');
      await page.keyboard.press('ArrowRight'); await pause(250);
      const s4 = await lire();
      if (s4.prog === s3.prog) pb.push('→ ne passe pas à la carte suivante (« ' + s4.prog + ' »)');
      // Garde de saisie : Espace dans un champ ne retourne rien
      await page.evaluate(() => { const i = document.createElement('input'); i.id = 'zz-saisie'; document.body.appendChild(i); i.focus(); });
      await page.keyboard.press(' '); await pause(300);
      if ((await lire()).verso) pb.push('Espace dans un champ de saisie a retourné la carte');
      await page.evaluate(() => { const i = document.getElementById('zz-saisie'); if (i) i.remove(); });
      // Quiz ouvert : les touches ne vont pas à la page derrière
      await page.evaluate(() => window.quizOpen());
      await pause(400);
      await page.keyboard.press('n'); await pause(400);
      await page.keyboard.press('3'); await pause(250);
      const s5 = await lire();
      if (s5.chap !== 'chap-' + autre.id) pb.push('« n » derrière le quiz a changé de chapitre (' + s5.chap + ')');
      if (s5.notees !== s3.notees) pb.push('« 3 » derrière le quiz a noté une carte du chapitre');
      await page.keyboard.press('Escape'); await pause(250);
      if (await ouvert('quiz-overlay')) pb.push('Échap ne ferme pas le quiz');
      return pb;
    });

    /* ---------- Espace sur les commandes de la fiche : retourne / relit, ne note jamais ----------
       Le focus est posé sur la 1re note (« À revoir ») après un retournement, et Chrome le met sur
       le bouton cliqué : Espace y gardait l'activation native et notait « À revoir » en silence. */
    await etape('Espace sur « Afficher la réponse » ou une note focalisée (cartes, quiz) : retourne la carte, ne note pas', async () => {
      const pb = [];
      const etatFlash = () => page.evaluate(() => { const o = {}; for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (/^flash:/.test(k)) o[k] = localStorage.getItem(k); } return JSON.stringify(o); });
      const fiche = () => page.evaluate(() => ({ verso: FLASH_INSTANCES.rlc.isFlipped(), prog: (document.getElementById('rlc-flash-prog') || {}).textContent || '' }));
      await naviguer(page, 'rlc', 'flash');
      const e0 = await etatFlash(), f0 = await fiche();
      if (f0.verso) { await page.keyboard.press('ArrowRight'); await pause(300); }
      await page.click('#rlc-flash .fc-reveal'); await pause(600);
      const f1 = await fiche();
      if (!f1.verso) pb.push('clic sur « Afficher la réponse » : la carte n\'est pas retournée');
      await page.keyboard.press(' '); await pause(600);
      const f2 = await fiche(), e2 = await etatFlash();
      if (f2.verso) pb.push('cartes : Espace après le clic sur « Afficher la réponse » ne retourne pas la carte (verso resté affiché)');
      if (f2.prog !== f1.prog) pb.push('cartes : Espace a changé de carte (« ' + f1.prog + ' » → « ' + f2.prog + ' »)');
      if (e2 !== e0) pb.push('cartes : Espace sur la note focalisée a écrit flash:rlc (carte notée « À revoir »)');
      // Entrée sur une note focalisée : activation native (note la carte)
      await page.keyboard.press(' '); await pause(600);
      await page.focus('#rlc-flash .flash-controls .ok'); await page.keyboard.press('Enter'); await pause(600);
      if ((await etatFlash()) === e0) pb.push('cartes : Entrée sur « Hésitant » focalisé ne note pas la carte');
      // Quiz : Espace (révéler), Espace (relire la question) → progression inchangée, rien d'écrit
      await page.evaluate(() => window.quizOpen()); await pause(500);
      await page.evaluate(() => {
        ['physique', 'maths', 'si', 'info', 'anglais'].forEach(m => { const c = document.getElementById('qc-' + m); if (c && c.checked !== (m === 'physique')) c.click(); });
        const a = document.querySelector('input[name="quiz-mode"][value="all"]'); if (a) a.click();
        const n = document.querySelector('input[name="quiz-nb"][value="10"]'); if (n) n.click();
      });
      await page.click('#quiz-start-btn'); await pause(600);
      const prog = () => page.evaluate(() => ((document.getElementById('quiz-progress-text') || {}).textContent || '').trim());
      const q0 = await prog(), s0 = await etatFlash();
      await page.evaluate(() => { if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); });
      await page.keyboard.press(' '); await pause(500);
      const rev = await page.evaluate(() => getComputedStyle(document.getElementById('quiz-actions-rate')).display !== 'none');
      if (!rev) pb.push('quiz : Espace ne révèle pas la réponse');
      await page.keyboard.press(' '); await pause(500);
      const q1 = await prog(), s1 = await etatFlash();
      if (q1 !== q0) pb.push('quiz : Espace, Espace a fait avancer le quiz (« ' + q0 + ' » → « ' + q1 + ' »)');
      if (s1 !== s0) pb.push('quiz : Espace, Espace a écrit une clé flash: (carte notée « À revoir »)');
      await page.keyboard.press('Escape'); await pause(250);
      return pb;
    });

    /* ---------- Thème ---------- */
    await etape('thème Auto : suit le réglage de l\'appareil en continu, pas un choix explicite', async () => {
      const lire = () => page.evaluate(() => ({ t: document.documentElement.getAttribute('data-theme'), pref: document.documentElement.getAttribute('data-theme-pref') }));
      const attendre = async attendu => {   // l'événement « change » de matchMedia est asynchrone
        for (let i = 0; i < 30; i++) { const s = await lire(); if (s.t === attendu) return s; await pause(100); }
        return lire();
      };
      const pb = [];
      await page.evaluate(() => window.__setTheme('auto'));
      await page.emulateMedia({ colorScheme: 'dark' });
      let s = await attendre('dark');
      if (s.t !== 'dark' || s.pref !== 'auto') pb.push('Auto + appareil en sombre : data-theme=' + s.t + ', préférence=' + s.pref);
      await page.emulateMedia({ colorScheme: 'light' });
      s = await attendre(null);
      if (s.t === 'dark') pb.push('Auto + appareil repassé en clair : le site reste sombre');
      await page.evaluate(() => window.__setTheme('light'));
      await page.emulateMedia({ colorScheme: 'dark' });
      await pause(600);
      s = await lire();
      if (s.t === 'dark') pb.push('préférence Clair : le site suit quand même l\'appareil en sombre');
      await page.emulateMedia({ colorScheme: 'light' });
      await page.evaluate(() => window.__setTheme('auto'));
      return pb;
    });

    await etape('thème sombre puis clair (sélecteur de #theme-btn, mémorisé)', async () => {
      const a = await choisirTheme(page, 'dark');
      const b = await choisirTheme(page, 'light');
      return [(a.attr !== 'dark' || a.store !== 'dark') && 'choix « Sombre » : data-theme=' + a.attr + ', Store=' + a.store,
        a.pop && 'le sélecteur reste ouvert après le choix « Sombre »',
        (b.attr === 'dark' || b.store !== 'light') && 'choix « Clair » : data-theme=' + b.attr + ', Store=' + b.store];
    });

    /* ---------- Sauvegarde : export ---------- */
    let exporte = null;
    await etape('sauvegarde : export JSON (téléchargement)', async () => {
      await page.click('#more-btn');
      await pause(200);
      await page.click('#backup-btn');
      await pause(300);
      if (!(await ouvert('backup-overlay'))) return ['la fenêtre Sauvegarde ne s\'ouvre pas'];
      const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 8000 }), page.click('#backup-export-btn')]);
      const f = ctx.fichierSortie('sauvegarde-exportee.json');
      await dl.saveAs(f);
      exporte = JSON.parse(fs.readFileSync(f, 'utf8'));
      const fb = await page.evaluate(() => document.getElementById('backup-feedback').textContent);
      return [exporte.app !== 'revisions-ptsi' && 'champ app = ' + exporte.app, exporte.version !== 1 && 'champ version = ' + exporte.version,
        !(exporte.data && exporte.data['flash:rlc']) && 'la progression flash:rlc est absente de l\'export',
        !/Export réussi/.test(fb) && 'message de confirmation absent (« ' + fb + ' »)'];
    });

    /* ---------- Sauvegarde : import (recharge la page) ---------- */
    await etape('sauvegarde : import JSON puis rechargement', async () => {
      const n = await page.evaluate(p => FLASH_REGISTRY[p].length, autre.prefix);
      const etat = Array.from({ length: n }, (_, i) => i < 3
        ? { h: 0, o: 0, e: 1, last: 2, box: 1, due: Date.now() + 86400000 } : { h: 0, o: 0, e: 0, last: null });
      const donnees = { app: 'revisions-ptsi', version: 1, exportedAt: new Date().toISOString(),
        data: Object.assign({}, exporte ? exporte.data : {}, { ['flash:' + autre.prefix]: JSON.stringify(etat) }) };
      const f = ctx.fichierSortie('sauvegarde-a-importer.json');
      fs.writeFileSync(f, JSON.stringify(donnees, null, 1));
      let confirme = null;
      journal.dialogue = d => { confirme = d.message(); d.accept(); };
      const recharge = page.waitForEvent('load', { timeout: 15000 });
      await page.setInputFiles('#backup-file-input', f);
      await recharge;
      await attendreApp(page);
      const lu = await page.evaluate(p => Store.getJSON('flash:' + p, null), autre.prefix);
      await naviguer(page, autre.id, 'flash');
      const stats = await page.evaluate(p => document.getElementById(p + '-stats').textContent, autre.prefix);
      return [!confirme && 'aucune demande de confirmation avant l\'import',
        JSON.stringify(lu) !== JSON.stringify(etat) && 'la progression importée n\'a pas été réécrite dans le Store',
        !/Acquis\s*:\s*3\//.test(stats) && 'statistiques du chapitre après import : « ' + stats + ' »'];
    });

    if (journal.dialogues.length) res.avertir('boîte(s) de dialogue inattendue(s) : ' + journal.dialogues.map(d => d.type + ' « ' + d.message + ' »').join(' ; '));
  },
};
