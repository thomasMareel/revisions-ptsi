# Ligne B, étape 2/2 — RÉVISION (cartes, quiz, Aujourd'hui, Bilan) — journal

Branche : wip/refonte-b (départ 1c0621b, étape « contenu » faite).
Worktree (session 2) : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-6
Périmètre : région CSS REVISION + HTML/JS des cartes (makeFlash), quiz, Aujourd'hui, Bilan.
PAS FENETRES/IMPRESSION (ligne C) : recherche, formulaire, sauvegarde, raccourcis, cartes
signalées, calcul mental, toasts, bannière, impression. Les blocs CSS .flag-list et #drill-*
restent dans REVISION (C les surcharge depuis FENETRES) : ne pas les supprimer.
Outils : scratchpad/refonte/impl/rev/

## Constats (session 2)
- La ligne A (wip/refonte-a, déjà finie) a : ajouté `t` (et `s` = section) à lastPos, modifié
  quizStartDue(prefix), ajouté des symboles au sprite (i-x, i-chev-*, i-clock, i-wave…), déplacé
  #today-btn dans l'en-tête. → Ne PAS retoucher ces lignes (fusion) ; lire lastPos.t « si présent » ;
  icônes manquantes injectées en JS seulement si absentes (pas de doublon d'id après fusion).
- Tests qui contraignent le DOM : interactions (#rlc-flash-content innerText /RÉPONSE/ au verso,
  .flash-controls .easy cliquable après retournement, #rlc-flash-prog contient « Carte 2 / N »,
  #rlc-stats /Acquis\s*:\s*1\//, .flash-course-link toujours dans le DOM, #quiz-reveal-btn,
  #quiz-actions-rate .rate-acq, #quiz-progress-text « 2 / … », #today-date, #today-resume-wrap,
  #today-close ferme, .dash-chap[data-chap], « % » et « acquises » dans le Bilan).

## Fait
- (session 1) lecture SPEC.
- (session 2) lecture SPEC §1, §5.1, §5.4, §5.6–5.8, §5.11, §6, §7, §8, §9 ; composants §1, §10, §11 ;
  DOM/JS de makeFlash, quiz, Aujourd'hui, Bilan ; tests.

## Fait (suite)
- rev/etat-avant.json (+ -mobile) : session de notation scriptée sur 1c0621b (outils/etat.js,
  Date.now figé, hasard à graine ; 26 clés flash:/flashids:, 132 cartes notées ; déterministe).
- b86ebdc (travail) : makeFlash réécrit (rev/makeflash.js, splice1.py) : fiche enrichie au 1er
  affichage (ResizeObserver, rien au chargement), en-tête de badges, rappel de la question au verso,
  pied (Voir dans le cours · §n + Signaler), .review-nav, .fc-reveal, notation icône+échéance+touche,
  progression empilée ; raccourcis tous decks (rev/clavier.js) ; quiz (rev/quiz.html + splice2.py :
  fiche commune, capture clavier, résultats) ; Aujourd'hui (rev/today.html, today.js) ; Bilan (dash.js).

- be8cac1 : région REVISION réécrite (rev/revision.css → socle/remplacer_region.py) ; test
  regressions noter() retourne la carte avant de noter (boutons au verso seulement).
- bc20d11 : formules de réponse ajustées (flashAjusterFormules), résultats du quiz (boutons avant
  la liste des chapitres, 8 au plus), Bilan 3 tuiles. ÉTAT OCTET POUR OCTET : etat-apres(.json,
  -mobile.json) IDENTIQUES à etat-avant (cmp) sur bc20d11.
- Aperçu fusionné A + B : rev/outils/apercu.sh → rev/apercu-site (0 conflit sur index.html) ;
  captures : rev/outils/cap.js (écrans recto, verso, anglais, quiz-config, quiz, quiz-verso, quiz-fin,
  auj, auj-vide, bilan) → rev/c2, c3, c4.

- t1 (bc20d11) : interactions, regressions, pwa OK. 0421795 : test « raccourcis des cartes » ajouté
  (interactions). t2 : interactions OK (21) ; visuel --strict : 0 constat sur quiz, bilan,
  aujourdhui ; sur rlc-flash/anglais-flash, seulement des éléments COQUILLE/PAGE (rev-badge,
  search-btn kbd, span.num, button.tab, cpg-dir, ctb-sub, eyebrow, theme-label, hdr-btn-label).
- 64453c0 : quizGotoChapter (carte affichée + prefix), raccourcis bloqués derrière Aujourd'hui/Bilan
  (capture), CLAUDE.md (paragraphe « Fiche de révision », anomalies 4 et 5), TOLERES de mon périmètre retirées.
- Aperçu fusionné : tests de A copiés dans apercu-site/tests (outils/tests-a.sh), lancés par
  rev/tests-apercu.sh (a1 = visuel --strict + interactions).

- a1 (aperçu fusionné A + B, tests de A) : visuel --strict = 0 constat sur mes écrans (restent 46
  constats « recherche », ligne C) ; interactions (A) OK 24.
- Chargement (téléphone émulé, CPU ×4, outils/perf.js) : 1c0621b DCL ≈ 12,9 s → HEAD ≈ 8,5 s
  (makeFlash paresseux).

- t3 (64453c0) : site 11, mobile 7, regressions 29, pwa 8 : TOUT OK (20 min 49 s).
- État octet pour octet sur 64453c0 : etat-final.json = etat-avant.json (cmp) ; idem sur l'aperçu
  fusionné A + B (etat-apercu.json).
- TERMINÉ : branche wip/refonte-b à 64453c0, worktree détaché (git checkout --detach).

## Écarts connus / hors périmètre
- Sur B seule, l'ancien #mob-header (z 200) recouvre le haut des fenêtres de révision (z 50) au
  téléphone : disparaît à la fusion avec A (vérifié sur l'aperçu fusionné).
- Récents d'Aujourd'hui : « matière · partie » à droite (la clé recents ne garde pas l'onglet).
- visuel --strict sur B seule : constats restants = COQUILLE/PAGE (rev-badge, search-btn kbd,
  span.num, button.tab, cpg-dir, ctb-sub, eyebrow, theme-label, hdr-btn-label, toc-item, yr2a, tiroir)
  et FENETRES (recherche) ; sur l'aperçu fusionné : recherche seulement (ligne C).
- Mode « Ciblé » du quiz inclut toujours les cartes jamais vues (anomalie 5, validation utilisateur).
1. (fait) Référence octet pour octet : session de notation scriptée (Date.now figé, hasard à graine) sur
   1c0621b → dump flash:/flashids: (rev/etat-avant.json).
2. JS makeFlash (§7.9) : en-tête .fc-head, rappel de la question au verso, pied (aide selon pointeur /
   Voir dans le cours + Signaler), .review-nav, bouton « Afficher la réponse », notation icône +
   échéance + touche, progression empilée ; raccourcis 1/2/3/Espace/←→ tous decks + garde.
3. Quiz : même fiche, config en puces/segmentés, résultats.
4. Aujourd'hui (§7.13) et Bilan.
5. CSS REVISION réécrite (composants §10, §11).
6. Captures vs 04a, 04b, 05, 09 ; tests ; journal ; checkout --detach.
