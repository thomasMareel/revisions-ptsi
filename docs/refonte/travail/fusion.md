# Journal — étape FUSION (wip/refonte ← A, B, C)

Worktree : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-7
Base wip/refonte = 7520731 (socle + dossier docs/refonte) ; A = c263af1, B = 64453c0, C = 0747fe5.
Outils : scratchpad/refonte/impl/fusion/ (tol.py + poser_tol.py : fusion sémantique des TOLERES ;
jonction.js : debord / impression / sp8 / retour ; capt.js : captures aux tailles des maquettes ;
sonde.js : évaluer une expression ; gabarit.py, testsreadme.py : retouches de docs).

## Fait
- 49737a2 merge A (sans conflit) ; d1a26b6 merge B (conflit TOLERES de tests/suites/visuel.js résolu
  par fusion sémantique : retraits de A et de B gardés) ; 5abe554 merge C (même conflit, même méthode).
  index.html, CLAUDE.md, interactions.js, mobile.js, regressions.js : fusion automatique.
- validate OK, check_js 18 blocs 0 erreur.
- f039e0a docs : CLAUDE.md réécrit en entier, README (Fonctionnalités), GABARIT-CHAPITRE.md, tests/README.md.
- Batterie t1 (--strict, toutes suites) sur 5abe554 : TOUT EST OK en 23 min 07 s
  (site 11, mobile 8 dont 0 débordement sur 630 panneaux, interactions 26, pwa 8 (+ avertissement connu),
  regressions 29, visuel 8 : 0 constat contraste/taille/débordement/cible24/cible44, 82 écrans).
- Contrôles de jonction (jonction.js) :
  - retour Android sur les 8 pages plein écran (Aujourd'hui, recherche, quiz, Bilan, formulaire,
    sauvegarde, signalées, calcul) : toutes refermées, chapitre et URL inchangés ;
  - impression rlc exos / cours, slci exos (PDF rastérisé relu) : tous les exercices imprimés même avec
    le filtre « Difficile » actif, corrections ouvertes, pas d'.exo-tools, formules dessinées ;
  - 141 onglets Exercices à 390 px, toutes solutions dépliées : 0 débordement ;
  - REVISION sous-partie 8 (.flag-list/#drill-*) : seul effet = rembourrage du corps du Calcul mental.
- 8d76e47 remise en cohérence : sous-partie 8 retirée (sauf .is-flagged), .mob-filter-tag et
  .backup-close (règles mortes) retirées, icônes undo/skip/flip/play dans le sprite statique (injection
  JS supprimée), onglet Cartes au téléphone à .75rem des onglets + hauteur de fiche (maquette 04a),
  TOLERES vide.
- État des flashcards : session scriptée (rev/outils/etat.js) identique octet pour octet à main
  (346cfa9) et à la référence de la ligne B, ordinateur et téléphone.
- Captures (cap1, cap2) comparées à 01, 02, 04a, 04b, 05, 08b : fidèles.

- 70dbfbb docs : REPRISE.md mis à jour, journaux copiés dans docs/refonte/travail, durées des tests.
- Batterie t2 (--strict, toutes suites) sur 8d76e47 (index.html final) : TOUT EST OK en 23 min 43 s
  (site 11, mobile 8, interactions 26, pwa 8 + avertissement connu, regressions 29, visuel 8 : 0 constat).
- Chargement téléphone émulé, processeur ×4, sans SW (perf.js, 3 essais) : main = DCL 12,5 s / prêt
  13,2 s ; wip/refonte = DCL 9,1 s / prêt 9,5 s (makeFlash paresseux, sommaire interne supprimé).

## TERMINÉ — wip/refonte, puis checkout --detach
