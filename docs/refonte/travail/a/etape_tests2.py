#!/usr/bin/env python3
"""Nouvelles vérifications de la coquille (s'AJOUTENT aux existantes) :
- interactions : barre latérale repliable (navCollapsed), Sommaire de la matière (#sommaire/…,
  précédent), filtre groupé par matière avec <mark> ;
- mobile : le bouton retour (Android) ferme la page Chapitres et la feuille ⋯ sans quitter le chapitre.
Usage : python3 etape_tests2.py <racine du dépôt>"""
import sys, os
R = sys.argv[1]

def maj(rel, a, b):
    p = os.path.join(R, rel)
    s = open(p, encoding='utf-8').read()
    assert s.count(a) == 1, (rel, a[:60], s.count(a))
    s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)
    print('mis à jour :', rel)

maj('tests/suites/interactions.js', "    /* ---------- Recherche ---------- */", r"""    /* ---------- Navigation des chapitres (coquille) ---------- */
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

    /* ---------- Recherche ---------- */""")

maj('tests/suites/mobile.js', "    res.verifier('tiroir : ouverture, matières, filtre, Entrée', !pbTiroir.length, pbTiroir);", r"""    res.verifier('tiroir : ouverture, matières, filtre, Entrée', !pbTiroir.length, pbTiroir);

    /* ---------- 2b) Bouton retour (Android) : ferme la page Chapitres / la feuille ⋯ ---------- */
    journal.lieu = 'retour Android';
    const pbRetour = [];
    try {
      const avant = await page.evaluate(() => location.hash);
      for (const [nom, bouton, page_] of [['page Chapitres', '#mob-menu-btn', 'mob-drawer'], ['feuille ⋯', '#mob-more-btn', 'mob-more-menu']]) {
        await page.tap(bouton);
        await pause(500);
        if (!(await page.evaluate(id => document.getElementById(id).classList.contains('open'), page_))) { pbRetour.push(nom + ' : ne s\'ouvre pas'); continue; }
        await page.goBack();
        await pause(500);
        const s = await page.evaluate(id => ({ ouvert: document.getElementById(id).classList.contains('open'), hash: location.hash }), page_);
        if (s.ouvert) pbRetour.push(nom + ' : le bouton retour ne la ferme pas');
        if (s.hash !== avant) pbRetour.push(nom + ' : le bouton retour a quitté le chapitre (hash ' + s.hash + ' au lieu de ' + avant + ')');
      }
      // fermée par ×, puis retour : on revient bien au chapitre PRÉCÉDENT (l'entrée fictive a été retirée)
      await page.tap('#mob-menu-btn');
      await pause(500);
      await page.tap('#mob-drawer-close');
      await pause(500);
      const s2 = await page.evaluate(() => ({ ouvert: document.getElementById('mob-drawer').classList.contains('open'), hash: location.hash }));
      if (s2.ouvert) pbRetour.push('× ne ferme pas la page Chapitres');
      if (s2.hash !== avant) pbRetour.push('après ×, hash ' + s2.hash + ' au lieu de ' + avant);
    } catch (e) { pbRetour.push('interaction impossible : ' + String(e.message).split('\n')[0]); }
    res.verifier('bouton retour (Android) : ferme la page Chapitres et la feuille ⋯ sans quitter le chapitre', !pbRetour.length, pbRetour);""")
print('tests ajoutés')
