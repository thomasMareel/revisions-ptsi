# Journal — ligne A, étape 2/2 : PAGE CHAPITRE (branche wip/refonte-a)

Copie de travail : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-4
Branche : wip/refonte-a (depuis 2639f87, fin de la coquille)
Scripts/captures de travail : scratchpad/refonte/impl/p/ (nd.sh = node + Playwright + polices ; capt.js
= captures du site aux tailles des maquettes ; apercu.sh = fusion à 3 voies avec wip/refonte-b dans p/apercu/site)

## Décisions d'architecture (2e session)
- Feuille = `.chapter` (fond --sheet, rayon, ombre, liseré 4 px --chap-vif) ; panneau = `.panel` (padding,
  filet rouge ::before à margin-col − 20 px sur cours/meth, prolongé le long du pied). Simu : feuille
  66rem, pas de rail. Exos et Simu : tête et panneau alignés à 2,5rem (comme 08a/08b). État posé par JS :
  `data-onglet` sur la feuille et `html.rail-on` (colonne du rail).
- Rail = UN `<aside id="chap-rail" class="rail">` dans #app-main, `position:fixed` à droite (≥ 1360 px),
  `#app-main` reçoit `padding-right:var(--rail-w)`. Contenu reconstruit pour le chapitre affiché :
  sommaire (cours ; items enregistrés dans le scroll-spy), « Mes cartes », liste des exos (onglet Exos).
- SOMMAIRE INTERNE : plus de `.toc-wrapper`/`.toc-content` dans les panneaux (gain au chargement) ; ids
  + data-toc-label gardés ; IntersectionObserver n'observe que les sections du chapitre affiché.
- Intercalaire : injectChapterTitleBanners crée seulement le h2 ; enrichissement PARESSEUX au 1er
  affichage (fil d'Ariane, actions, méta). Onglets : libellés (Cartes, Simu/Exos au téléphone),
  `.cnt`, `.count` posés paresseusement ; compteur dû mis à jour via __updateReviseBadge.
- Module JS « PAGE CHAPITRE » : `<script>` séparé, juste avant l'enregistrement du service worker.
- quizStartDue(prefix) : argument facultatif (bouton « Réviser les N cartes dues » du rail).

## Plan
1. [x] Lecture SPEC §1, §4.4, §5.1, §6, §7 (4,5,10,11), §9 ; composants §4, §8, §9 ; région PAGE actuelle
2. [x] CSS PAGE réécrite (feuille, intercalaire, onglets, rail, pager, onglets téléphone)
3. [x] JS : intercalaire (§7.4), onglets compteurs (§7.5), rail (§7.10), pager (§7.11)
4. [x] Captures comparées 01, 06a, 08a, 08b, 02, 06b (sur l'aperçu fusionné avec B : capB1, capB2) — très proches
5. [x] Tests : validate, check_js, site, interactions, pwa, regressions, visuel --strict, mobile
6. [x] commit + checkout --detach

## Fait
- c1c2cd2 : région PAGE + module PAGE CHAPITRE + HTML (rail, pied, i-chev-left) + sommaire interne retiré
- 12daaa9 : pied le long du filet rouge, onglets téléphone (top:0 quand la barre s'efface : bogue de
  spécificité corrigé), casPhrase (noms propres et sigles gardés : « Maxwell », « ARQS »), cache
- interactions/pwa/regressions OK (t1)
- ce160c4 : scroll-spy sur une ligne de lecture (bande de 2 px sous les barres collantes : la section
  sous la ligne est active ; l'ancienne bande 10–30 % marquait la section précédente), test interactions
  « page chapitre » (vert, t2), CLAUDE.md (page chapitre, sommaire, régions), TOLERES de la page retirées
  (cpg-dir, ctb-sub, button.tab tel, yr2a, toc-title)
- 116443e : ligne de lecture recalculée au redimensionnement
- visuel --strict (tv1, copie seule) : 0 constat sur les éléments page/coquille ; restent hors périmètre :
  quiz, recherche, Bilan, Aujourd'hui, cartes, contenu (notice sombre, ::before, débordement rlc-cours tel
  dû à une formule de liste : contenu, ligne B)
- en cours : t3 = site + mobile ; ensuite visuel --strict sur l'aperçu fusionné (--racine=p/apercu/site)

## 3e session (reprise après redémarrage)
- t3 (site OK ; mobile : seul échec = débordements MathJax ; suit-cours 394 px NOUVEAU par rapport à la
  coquille : gouttière 16 px (SPEC §4.2) au lieu de 12 ; la ligne B corrige par .formula défilante → à
  vérifier sur l'aperçu fusionné)
- captures cap3 (copie) / capB3 (aperçu fusionné) relues : 01, 06a, 08a, 02, 06b, pieds, 1280, tablette = fidèles
- retouche : titres de la liste d'exercices du rail coupés à 2 lignes (titre complet en title)
- c263af1 : titres du rail coupés à 2 lignes
- t4 (copie, --strict) : interactions 24/24, pwa 8/8, regressions 29/29, site 11/11 OK ; visuel --strict : 0 constat
  sur la page (intercalaire, onglets, rail, pied) ; mobile : seul échec = débordements de formules (socle +
  suit-cours 394 px dû à la gouttière 16 px) ; sonde contrastes intercalaire 7 matières × 2 thèmes : tout ≥ 4,8:1
- t5apercu (aperçu fusionné A+B, --strict) : mobile OK, 0 débordement sur 630 panneaux (13 « ne déborde plus ») ;
  visuel : 0 constat sur les écrans de chapitre ; restent quiz, recherche, Bilan, Aujourd'hui, cartes (REVISION/FENETRES)
- regions.md complété (section « Après la ligne A, étape 2 »)

## TERMINÉ — branche wip/refonte-a (c1c2cd2..c263af1), puis git checkout --detach

## 4e session (relance de l'étape, 19 h 52 UTC) — vérification seule
- Branche intacte (c263af1), arbre propre ; validate.py OK, check_js.py 0 bloc en erreur ; PAGE sans couleur
  codée en dur ; sw.js inchangé (CACHE_VERSION non incrémenté). Captures capB3 relues (01, 08a, 06b) : fidèles.
- Rien à refaire. git checkout --detach.
