#!/usr/bin/env python3
"""Suite visuel : écrans de la nouvelle coquille ajoutés (mesures EN PLUS, rien de retiré) :
menu Réviser, sélecteur de thème (ordinateur), feuille ⋯ (téléphone), Sommaire de la matière.
Usage : python3 etape_visuel.py tests/suites/visuel.js"""
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

rep("""  { nom: 'menu-plus', chap: 'rlc', onglet: 'meth', racine: '#more-menu', ordinateurSeul: true, preparer: ouvrirMenuPlus },
];""", """  { nom: 'menu-plus', chap: 'rlc', onglet: 'meth', racine: '#more-menu', ordinateurSeul: true, preparer: ouvrirMenuPlus },
  // Coquille de la refonte : menu Réviser, sélecteur de thème, feuille ⋯ du téléphone, Sommaire de la matière
  { nom: 'menu-reviser', chap: 'rlc', onglet: 'meth', racine: '#study-menu', ordinateurSeul: true, preparer: ouvrirMenuReviser },
  { nom: 'theme', chap: 'rlc', onglet: 'meth', racine: '#theme-pop', ordinateurSeul: true, preparer: ouvrirSelecteurTheme },
  { nom: 'feuille-plus', chap: 'rlc', onglet: 'meth', racine: '#mob-more-menu', telephoneSeul: true, preparer: ouvrirFeuillePlus },
  { nom: 'sommaire', chap: 'rlc', onglet: 'meth', preparer: ouvrirSommaire },
];""")
rep("""/* Referme tout ce qui peut rester ouvert entre deux écrans""", """async function ouvrirMenuReviser(page) {
  await cliquer(page, '#study-btn');
  await pause(250);
  return (await estOuvert(page, '#study-menu')) ? [] : ['le menu Réviser ne s\\'ouvre pas'];
}
async function ouvrirSelecteurTheme(page) {
  await cliquer(page, '#theme-btn');
  await pause(300);
  return (await page.evaluate(() => { const p = document.getElementById('theme-pop'); return !!(p && !p.hidden); })) ? [] : ['le sélecteur de thème (#theme-pop) ne s\\'ouvre pas'];
}
async function ouvrirFeuillePlus(page) {
  await cliquer(page, '#mob-more-btn');
  await pause(450);
  return (await estOuvert(page, '#mob-more-menu')) ? [] : ['la feuille ⋯ (#mob-more-menu) ne s\\'ouvre pas'];
}
async function ouvrirSommaire(page) {
  // Lien profond du Sommaire de la matière (comme un favori ou le bouton précédent)
  await page.evaluate(() => { location.hash = '#sommaire/physique'; });
  await pause(500);
  return (await page.evaluate(() => { const s = document.getElementById('sommaire-matiere'); return !!(s && !s.hidden && s.querySelector('.pcard')); }))
    ? [] : ['le Sommaire de la matière (#sommaire/physique) ne s\\'affiche pas'];
}

/* Referme tout ce qui peut rester ouvert entre deux écrans""")
rep("""      const ecrans = ECRANS.filter(e => !(e.ordinateurSeul && app.mobile));""",
    """      const ecrans = ECRANS.filter(e => !(e.ordinateurSeul && app.mobile) && !(e.telephoneSeul && !app.mobile));""")
open(p, 'w', encoding='utf-8').write(s)
print('suite visuel : écrans de la coquille ajoutés')
