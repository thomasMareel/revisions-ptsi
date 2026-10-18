#!/usr/bin/env python3
"""Ligne A : met à jour les tests pour la nouvelle coquille (vérifications CONSERVÉES) :
- thème : le sélecteur (popover de #theme-btn / segmenté de la feuille ⋯) remplace le
  bouton cyclique ; on vérifie toujours data-theme ET la clé theme du Store ;
- « Aujourd'hui » : #today-btn est dans l'en-tête (plus dans le menu Plus) ;
- suite visuel : barre latérale permanente à 1440 px (écran « tiroir »).
Usage : python3 etape_tests.py <racine du dépôt>"""
import sys, os
R = sys.argv[1]

def maj(rel, paires):
    p = os.path.join(R, rel)
    s = open(p, encoding='utf-8').read()
    for a, b in paires:
        assert s.count(a) == 1, (rel, a[:70], s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)
    print('mis à jour :', rel)

# ---------- interactions ----------
maj('tests/suites/interactions.js', [
    ("const { pause, attendreApp, fermerOverlays, naviguer, marqueJournal, problemesJournal } = require('../lib/outils');",
     "const { pause, attendreApp, fermerOverlays, naviguer, choisirTheme, marqueJournal, problemesJournal } = require('../lib/outils');"),
    ('''    await etape("écran « Aujourd'hui » (menu Plus)", async () => {
      await page.click('#more-btn');
      await pause(200);
      await page.click('#today-btn');''',
     '''    await etape("écran « Aujourd'hui » (bouton de l'en-tête)", async () => {
      await page.click('#today-btn');'''),
    ('''    await etape('thème sombre puis clair (#theme-btn, mémorisé)', async () => {
      await page.click('#theme-btn');
      await pause(250);
      const a = await page.evaluate(() => ({ t: document.documentElement.getAttribute('data-theme'), s: Store.get('theme') }));
      await page.click('#theme-btn');
      await pause(250);
      const b = await page.evaluate(() => ({ t: document.documentElement.getAttribute('data-theme'), s: Store.get('theme') }));
      return [(a.t !== 'dark' || a.s !== 'dark') && '1er clic : data-theme=' + a.t + ', Store=' + a.s,
        (b.t === 'dark' || b.s === 'dark') && '2e clic : data-theme=' + b.t + ', Store=' + b.s];
    });''',
     '''    await etape('thème sombre puis clair (sélecteur de #theme-btn, mémorisé)', async () => {
      const a = await choisirTheme(page, 'dark');
      const b = await choisirTheme(page, 'light');
      return [(a.attr !== 'dark' || a.store !== 'dark') && 'choix « Sombre » : data-theme=' + a.attr + ', Store=' + a.store,
        a.pop && 'le sélecteur reste ouvert après le choix « Sombre »',
        (b.attr === 'dark' || b.store !== 'light') && 'choix « Clair » : data-theme=' + b.attr + ', Store=' + b.store];
    });'''),
])

# ---------- site ----------
maj('tests/suites/site.js', [
    ("const { pause, attendreApp, fermerOverlays, naviguer, etatMathJax, problemesJournal } = require('../lib/outils');",
     "const { pause, attendreApp, fermerOverlays, naviguer, choisirTheme, etatMathJax, problemesJournal } = require('../lib/outils');"),
    ('''        await page.click('#theme-btn');
        await pause(300);
        const t = await page.evaluate(() => ({ attr: document.documentElement.getAttribute('data-theme'), stocke: Store.get('theme') }));
        res.verifier('bascule en thème sombre (#theme-btn)', t.attr === 'dark' && t.stocke === 'dark',
          'data-theme = ' + t.attr + ', Store theme = ' + t.stocke);''',
     '''        const t = await choisirTheme(page, 'dark');
        res.verifier('bascule en thème sombre (sélecteur de #theme-btn)', t.attr === 'dark' && t.store === 'dark',
          'data-theme = ' + t.attr + ', Store theme = ' + t.store);'''),
    ("    if (themes.includes('sombre')) { await page.click('#theme-btn'); await pause(200); }",
     "    if (themes.includes('sombre')) await choisirTheme(page, 'light');"),
])

# ---------- regressions (B4) ----------
maj('tests/suites/regressions.js', [
    ("const { pause, attendreApp, fermerOverlays, naviguer, extraireDeck, remplacerDeck, suivreErreurs } = require('../lib/outils');",
     "const { pause, attendreApp, fermerOverlays, naviguer, choisirTheme, extraireDeck, remplacerDeck, suivreErreurs } = require('../lib/outils');"),
    ('''        await page.click('#theme-btn');
        await pause(300);
        const v2 = await lire();
        if (v2.theme !== 'dark') throw new Error('préparation : #theme-btn n\\'a pas activé le thème sombre');
        controler('thème sombre', v2, attendu.sombre);
        await page.click('#theme-btn');
        await pause(300);
        controler('retour au clair', await lire(), attendu.clair);''',
     '''        await choisirTheme(page, 'dark');
        const v2 = await lire();
        if (v2.theme !== 'dark') throw new Error('préparation : le sélecteur de thème (#theme-btn) n\\'a pas activé le thème sombre');
        controler('thème sombre', v2, attendu.sombre);
        await choisirTheme(page, 'light');
        controler('retour au clair', await lire(), attendu.clair);'''),
])

# ---------- mobile ----------
maj('tests/suites/mobile.js', [
    ("const { pause, attendreApp, fermerOverlays, naviguer, etatMathJax } = require('../lib/outils');",
     "const { pause, attendreApp, fermerOverlays, naviguer, choisirTheme, etatMathJax } = require('../lib/outils');"),
    ('''    /* ---------- 3) Thème via le bouton mobile ---------- */
    journal.lieu = 'thème mobile';
    await page.tap('#mob-theme-btn');
    await pause(300);
    const th = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
    await page.tap('#mob-theme-btn');
    await pause(200);
    const th2 = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
    res.verifier('bouton thème mobile (sombre puis clair)', th === 'dark' && th2 !== 'dark', 'data-theme après 1 clic = ' + th + ', après 2 clics = ' + th2);''',
     '''    /* ---------- 3) Thème via la feuille ⋯ du téléphone (segmenté Clair / Sombre / Auto) ---------- */
    journal.lieu = 'thème mobile';
    let th = {}, th2 = {};
    try {
      th = await choisirTheme(page, 'dark', true);
      th2 = await choisirTheme(page, 'light', true);
    } catch (e) { th.erreur = String(e.message).split('\\n')[0]; }
    res.verifier('thème au téléphone par la feuille ⋯ (sombre puis clair, mémorisé)',
      th.attr === 'dark' && th.store === 'dark' && th2.attr !== 'dark' && th2.store === 'light' && !th2.feuille,
      th.erreur || ('« Sombre » : data-theme = ' + th.attr + ', Store = ' + th.store + ' ; « Clair » : data-theme = ' + th2.attr
        + ', Store = ' + th2.store + (th2.feuille ? ' ; la feuille ⋯ reste ouverte après Échap' : '')));'''),
])

# ---------- visuel ----------
maj('tests/suites/visuel.js', [
    ("const { pause, attendreApp, naviguer, etatMathJax } = require('../lib/outils');",
     "const { pause, attendreApp, naviguer, choisirTheme, etatMathJax } = require('../lib/outils');"),
    ('''async function ouvrirTiroir(page, app) {
  await cliquer(page, app.mobile ? '#mob-menu-btn' : '#nav-toggle-btn');
  await pause(450);
  return (await estOuvert(page, '#mob-drawer')) ? [] : ['le tiroir ne s\\'ouvre pas'];
}''',
     '''async function ouvrirTiroir(page, app) {
  // À partir de 1200 px, la navigation est une barre latérale PERMANENTE (#nav-toggle-btn la
  // replie ou l'affiche) : on vérifie qu'elle est affichée ; en dessous, c'est un tiroir
  // (page « Chapitres » plein écran au téléphone) qu'on ouvre.
  const laterale = await page.evaluate(() => matchMedia('(min-width:1200px)').matches);
  if (laterale) {
    if (await page.evaluate(() => document.documentElement.classList.contains('nav-replie'))) await cliquer(page, '#nav-toggle-btn');
    await pause(300);
    const vis = await page.evaluate(() => { const d = document.getElementById('mob-drawer'); const r = d.getBoundingClientRect();
      return d.checkVisibility() && r.width > 200 && r.left >= 0 && document.querySelectorAll('#mob-chap-list .mob-chap-row').length > 0; });
    return vis ? [] : ['la barre latérale des chapitres n\\'est pas affichée'];
  }
  await cliquer(page, app.mobile ? '#mob-menu-btn' : '#nav-toggle-btn');
  await pause(450);
  return (await estOuvert(page, '#mob-drawer')) ? [] : ['le tiroir ne s\\'ouvre pas'];
}'''),
    ('''        if (theme === 'sombre') {
          await cliquer(page, app.mobile ? '#mob-theme-btn' : '#theme-btn');
          await pause(350);
        }''',
     '''        if (theme === 'sombre') {
          // Sélecteur de thème : popover de #theme-btn (ordinateur), feuille ⋯ (téléphone)
          await choisirTheme(page, 'dark', app.mobile).catch(e => pbPreparation.push(app.nom + ' : sélecteur de thème : ' + String(e.message).split('\\n')[0]));
          await pause(150);
        }'''),
])
print('tests à jour')
