# Ligne C, étape 1/1 — FENÊTRES ET IMPRESSION — journal

Branche : wip/refonte-c (créée depuis wip/refonte = socle, 7520731).
Copie de travail : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-4
Régions : FENETRES, IMPRESSION (+ HTML/JS : recherche, formulaire, sauvegarde, raccourcis,
cartes signalées, calcul mental, toasts, printChapter).
Outils : scratchpad/refonte/impl/c/ (nd.sh, capt.js…)

## Coordination (lu au départ)
- Ligne A (wip/refonte-a, TERMINÉE) : bannière de mise à jour `.maj-banniere` FAITE (COQUILLE + JS
  sw-update-banner) → je n'y touche pas ; mes toasts reprennent son apparence. Retour Android des
  fenêtres FAIT par A dans urlRouting (liste PAGES : search/formula/backup/flag/drill-overlay ; repose
  sur la classe .open et sur Échap) → garder .open + fermeture par Échap pour chaque fenêtre.
- Ligne B (REVISION, en parallèle) : a modifié la ligne `MathJax.typesetPromise([body])` du module
  Formulaire (→ __apresRendu) : NE PAS toucher cette ligne ni ses voisines immédiates.
  `.flag-list` et `.drill-*` sont rangés en REVISION : je restyle les fenêtres Cartes signalées et
  Calcul mental par des sélecteurs #flag-overlay / #drill-overlay dans FENETRES (et nouvelles classes
  de gabarit .fen*), sans toucher REVISION.

## Plan
1. [ ] Gabarit commun des fenêtres (.fen : voile, boîte, tête titre + ×, plein écran téléphone)
2. [ ] Recherche §5.9 (CSS + JS : index unifié, résultats groupés, pastille de matière, ×)
3. [ ] Formulaire §5.10
4. [ ] Sauvegarde, Cartes signalées, Calcul mental, Raccourcis §5.11 ; toasts §5.1
5. [ ] Impression §5.15 (gabarit printChapter, jetons clairs, page de garde ; formulaire imprimé)
6. [ ] Tests visuel : écrans de mes fenêtres ajoutés ; TOLERES recherche nettoyées
7. [ ] Contrôles : validate, check_js, site, interactions, pwa, regressions, visuel --strict, mobile
8. [ ] Captures clair/sombre ordi/tel comparées (09, esprit de 05)
9. [ ] commit final + git checkout --detach

## Fait
- Commit 6d5258c (travail) : région FENETRES réécrite (c/fenetres.css → remplacer_region), région
  IMPRESSION (c/impression.css), HTML des fenêtres (c/etape_html.py : classes .fen/.fen-boite/
  .fen-tete/.fen-x ; ids gardés), module RECHERCHE réécrit (c/recherche.js, recopié par
  c/maj_recherche.py) + module « AMÉLIORATION 6 » retiré (c/etape_recherche.py, déjà appliqué),
  Formulaire (data-mat, data-nom, impression par l'iframe), printChapter réécrit + imprimerDocument
  (c/impression.js : jetons clairs extraits du grand <style>, page de garde, corrections ouvertes,
  Ctrl+P), raccourcis (c/etape_raccourcis.py), toasts window.__toast, cartes signalées, calcul mental.
- Aperçu fusionné A+B+C : c/apercu.sh → c/apercu/site (0 conflit au 1er essai).
- z-index : .fen = var(--z-overlay) (jetons). Dans MA branche seule, l'ancien #mob-header (z 200)
  recouvre le haut des fenêtres plein écran au téléphone : disparaît à la fusion avec A (vérifié
  sur l'aperçu fusionné). Captures de fidélité : sur l'aperçu fusionné (cap2…).

- Commit 62848ae : écrans visuel formulaire/sauvegarde/signalees/calcul/raccourcis (après 'recherche'
  dans ECRANS, préparateurs après ouvrirRecherche), TOLERES 'recherche' retirées ; drill boutons/titre.
- Commit 2d26b73 : .backup-close gardé (lien « Continuer → » d'Aujourd'hui, #today-close, B), CLAUDE.md
  (paragraphe « Fenêtres » après Sauvegarde ; Template d'impression ; ligne Suites/visuel).
- Impression vérifiée en PDF (c/impr.js + c/pdf2png.py) : rlc cours (lancé en SOMBRE → bien clair),
  rlc exos (corrections ouvertes, filet vert), formulaire (garde compacte).
- t1 : interactions 20/20, pwa 8/8, regressions 29/29 (B5 OK) — TOUT OK.
- tv1 (visuel --strict, avant retouches) : sur mes écrans seulement 2 constats (select du calcul 40 px
  au doigt → corrigé) ; formulaire « non évalué » (dégradé pointillé → filet en tirets, corrigé).

- t2 : site 11/11 OK ; visuel --strict : 0 constat et 0 « non évalué » sur mes 6 écrans (603 constats
  restants hors périmètre : chapitres, tiroir, quiz, Bilan, Aujourd'hui, menu Plus — régions des autres).
- t3 : mobile → seul échec = débordements MathJax connus du socle (13 aggravés + lor-cours, asy-cours,
  int-meth), 6 autres contrôles OK : aucun nouveau débordement dû aux fenêtres.
- c2ae0a5 index de recherche préparé en temps libre (1ʳᵉ recherche ≈ 175 ms = coût de l'ancien à
  l'ouverture ; maintenant ouverture instantanée). 1eaf05b : garde des raccourcis derrière .fen (capture,
  comme B pour Aujourd'hui/Bilan) + tests interactions (n derrière fenêtres, recherche groupée, aide ?).
- Fusion d'essai (c/conflits.sh) : index.html 0 conflit avec A puis B ; CLAUDE.md 0 ; visuel.js 1 conflit
  avec B (listes TOLERES, à résoudre à la main : garder les retraits des deux côtés).
- B (wip/refonte-b) a fini REVISION : il s'attend à ce que FENETRES surcharge .flag-list/#drill-* (fait).

- t5apercu (tests FUSIONNÉS A+B+C sur l'aperçu fusionné) : visuel --strict 0 constat (tous écrans),
  interactions 26/26.
- d70d561 énoncé du calcul mental en bloc (mot coupé au téléphone) ; 0747fe5 Imprimer du Formulaire
  masqué au téléphone (iframe d'impression peu fiable sur Android ; SPEC : Imprimer absent au téléphone).
- t6 (copie) : interactions 21/21, pwa 8/8, regressions 29/29 ; t7 visuel --strict : 0 constat sur mes
  écrans, 0 erreur JS. sw.js inchangé (PRECACHE à jour, aucun fichier ajouté ; CACHE_VERSION non touché).
- regions.md : section « Après la ligne C » ajoutée.

## TERMINÉ — branche wip/refonte-c (6d5258c..0747fe5), puis git checkout --detach
- Écarts à signaler : bannière de mise à jour faite par A (pas refaite) ; z-index des fenêtres = jetons
  (sur C seule, l'ancien #mob-header z 200 recouvre le haut des fenêtres plein écran : disparaît avec A) ;
  Formulaire sans bouton Imprimer au téléphone ; conflit TOLERES dans visuel.js avec B à la fusion.
- relecture finale des captures sur l'aperçu fusionné (c/apercu.sh puis c/capt.js)
- commit final, journal, git checkout --detach
