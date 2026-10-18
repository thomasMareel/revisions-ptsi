# Journal — ligne A, étape 1/2 : COQUILLE ET NAVIGATION (branche wip/refonte-a)

Copie de travail : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-2
Branche : wip/refonte-a (créée depuis wip/refonte)

## Plan
1. [ ] Lecture : région COQUILLE actuelle, HTML en-tête / tiroir / barre téléphone, JS tiroir (buildDrawerList…), thème
2. [ ] En-tête ordinateur .hdr (§5.12) : nav-toggle, marque §, champ recherche visible, Aujourd'hui, Bilan, Réviser+compteur ▾, thème, Plus
3. [ ] Barre latérale ≥1200 (#mob-drawer permanent), tiroir 1024–1199 / 768–1023, page Chapitres téléphone (§4.3/§5.13), navCollapsed
4. [ ] Navigation : segmenté année, filtre groupé par matière <mark>, épinglés/récents (puces/lignes), intercalaires .mat-tab avec effectif, parties repliables, « + N chapitres de 1ʳᵉ année », .nav-item
5. [ ] Sommaire de la matière (#sommaire/<matière>)
6. [ ] Barre téléphone .mbar (titre 2 lignes, s'efface, section courante), feuille ⋯ qui monte du bas, retour Android
7. [ ] Sélecteur de thème : popover ordinateur + segmenté feuille ⋯ (actuellement : … via matchMedia)
8. [ ] Tests mis à jour (#today-btn dans l'en-tête, thème par popover)
9. [ ] Contrôles : validate, check_js, site, interactions, pwa, regressions, visuel --strict, mobile
10. [ ] Comparaison visuelle aux captures 01, 02, 02b, 03a, 03b, 03c, 07a, 07b (clair + sombre)
11. [ ] git checkout --detach

## Fait
- Commit e9140de (travail) : HTML coquille (scripts dans scratchpad/refonte/impl/a/ : etape_html.py +
  coquille.html, coquille.css → remplacer_region COQUILLE, nav.js (module navigation), routage.js +
  etape_routage.py, theme.js + menus.js + etape_js2.py, etape_tests.py). Colonne de lecture enveloppée
  dans <article id="app-main" role="none"> (PAS div/section : </div> et </section> orphelins du contenu).
- Outils : a/capt.js (captures site réel, scénarios = maquettes), a/sonde.js (évaluer une expression).
- Commits 9dd05df, 90f4cd7 : tests (choisirTheme dans tests/lib/outils.js ; interactions : today-btn
  dans l'en-tête, thème par popover, + 3 étapes : barre latérale/navCollapsed, sommaire, filtre ;
  mobile : thème par feuille ⋯, + retour Android ; visuel : écrans menu-reviser, theme, feuille-plus,
  sommaire ; ouvrirTiroir = barre latérale ≥1200 ; TOLERES de la coquille retirés), CLAUDE.md.
- Résultats : interactions 23/23, regressions OK, pwa OK, visuel --strict : 0 constat dans le périmètre
  (restent REVISION/FENETRES/CONTENU/SIMU/PAGE) ; mobile : seul échec = débordements MathJax aggravés
  (dette du socle, CONTENU).

- Commits 796c71d, 2639f87 : finitions. Batterie finale (t6) : interactions 23/23, regressions OK,
  pwa OK, site 11/11 (t5), visuel --strict : 0 constat sur les écrans/éléments de la coquille
  (64 écrans mesurés) ; mobile complet : seul échec = débordements MathJax (13 connus aggravés + 3
  nouveaux lor-cours/asy-cours/int-meth = EXACTEMENT ceux signalés par le socle).
- regions.md complété (section « Après la ligne A, étape 1 »).

## TERMINÉ — branche wip/refonte-a (e9140de..2639f87), puis git checkout --detach

## Notes
- Taille du texte : segmenté « A / A+ / A++ » (100/110/120 %) au lieu de « A− / A / A+ » (le plancher
  13 px interdit < 100 % ; clé readScale inchangée). Écart volontaire à noter.
- En 2ᵉ année, ouvrir un chapitre de 1ʳᵉ année GARDE la 2ᵉ année (sa partie se déplie).
- Récents : incluent le chapitre courant (maquette), épinglés/récents non filtrés par année.
- Débordement 441 px de rlc-cours au téléphone (MathJax, CONTENU) : le viewport de mise en page
  s'élargit, donc les éléments fixes plein écran aussi → captures téléphone des pages sur rlc-meth.
