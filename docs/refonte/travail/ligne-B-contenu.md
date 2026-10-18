# Ligne B (contenu) — étape 1/2 : CONTENU + SIMU — journal

Branche : wip/refonte-b (créée depuis wip/refonte 37d0249).
Worktree : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-3
Outils de travail (scratchpad/refonte/impl/ligneB/) :
- contenu.css / simu.css / module.js = SOURCES des régions et du module ; `python3 appliquer.py`
  les réinjecte dans index.html (régions + module remplacé en place) ;
- cap.sh (captures, options |apercu = feuille simulée, |sol, |sel=, |scroll=) ; sims.js (planche
  des 27 simulateurs ; éviter l'option « plein » au téléphone : barres collantes) ; balayage.js
  (mesurerEcran de la suite visuel sur des panneaux) ; deborde.js ; eval.js ; tests.sh (batterie).

## Fait
- 1e2e76c : régions CONTENU et SIMU réécrites (composants §5-7), <style> de #cine-exos en jetons,
  module « CONTENU » + crochets dans typesetPanel, toggleSol (.open, aria-expanded), Formulaire,
  typesetActive (<head>).
- 4206b9a : courbe principale à --chap-vif (__CVchap), estat sombre, train (rayon négatif),
  cases à cocher, modes sur 2 rangées, schémas lisibles (≥ 12 px), MathML d'accessibilité,
  Lorentz (encres, 17 px au tél), sec-num multiples non découpés.
- après 4206b9a (non commité au moment de l'écriture) : retrait « Q1. » (-.265em), tableaux dans
  encadrés défilants, filet d'en-tête des rangées [style*=background].
- 2cb6092 : retrait Q1., ponctuation collée (formule large : max-width 100%-1em), tableaux dans
  encadrés, bandeaux alignés, test B3 (courbe cherchée à la couleur __CVchap). Suites site,
  interactions, pwa, regressions VERTES (t-base + t-reg).
- après 2cb6092 : .fl-amber/.fl-muted-soft/.lab-amber (classes SVG sans règle).
- balayage bal1 (35 panneaux × 2 thèmes × 2 appareils) : 0 constat de contenu hors Lorentz/cine
  (corrigés ensuite) ; restent .toc (région PAGE).

## Reste à faire
- tests : site/interactions/pwa/regressions (t-base en cours), mobile (DEBORDEMENTS_CONNUS),
  visuel --strict ; TOLERES de mon périmètre à nettoyer
- commit final, git checkout --detach

## Reprise (après redémarrage, 2e session)
- t-final interrompu (navigateur fermé par le redémarrage) : relancé en t-final2
  (site, interactions, pwa, regressions, mobile). Puis visuel --strict (t-vis2).
- t-final2 (HEAD b2e77a6) : site, interactions, pwa, regressions, mobile TOUT OK (23 min ;
  mobile : 630 panneaux, 0 débordement).
- En cours : libellés des canvas à 12 px (polices-canvas.py, 74 affectations 8-11 px → 12 px) +
  collisions de libellés corrigées (libelles-canvas.py, 29 remplacements, helper __texteDetoure) ;
  essais dans ligneB/exp (copie), captures de tous les modes : modes.js (modes-avant-o / -apres-o),
  paire.py. #dyn-canvas --h à réduire (dessin ≈ 210 px de haut).
- t-vis2 (visuel --strict, HEAD b2e77a6) : 0 constat dans mon périmètre (contenu, exercices,
  simulateur) ; restent span.num/button.tab/a.toc-item/span.cpg-dir/span.ctb-sub/span.toc-title/
  span.yr2a (PAGE), en-tête/tiroir (COQUILLE), cartes/quiz/Aujourd'hui/Bilan (REVISION),
  recherche/menu Plus (FENETRES).
- 2f4b0a3 : libellés canvas à 12 px + collisions (scripts polices-canvas.py, libelles-canvas.py
  puis -2 … -6 appliqués dans l'ordre ; déjà dans index.html) ; #dyn-canvas 300 px.
  Revue visuelle : modes-fin-o (ordi clair) / modes-fin-t (tél sombre), 97 états chacun.
- Reste : tests site+regressions+interactions sur 2f4b0a3 (t-c1), puis visuel --strict, revue
  finale chapitres (balayage), commit, checkout --detach.
- bal4 (26 panneaux, 5 matières, 2A, info, anglais, tableaux, SVG × clair/sombre × ordi/tél) :
  seul constat de contenu = 3 <p style="background:rgba(255,255,255,0.5)"> (osc-meth, oxr-cours,
  int-meth : 2,53:1 en sombre) → background:var(--sheet) (NON commité au moment d'écrire).
  Les cible44 de bal4 (seg/chip/toggle-sol) = artefact des captures d'éléments (l'émulation
  tactile est perdue) : bal5 sans captures → 44 px, rien.

## Reprise (3e session, 18:50)
- c94200d = fond var(--sheet) des 3 encarts (commité). t-c1 (site, regressions, interactions, pwa) : OK.
- t-c2 (visuel --strict + mobile) : visuel = 0 constat de mon périmètre (tous en COQUILLE/PAGE/
  REVISION/FENETRES) ; mobile interrompu (navigateur fermé par le redémarrage) → relancé en t-mob2.
- t-mob2 (c94200d) : mobile OK (630 panneaux, 0 débordement).
- 1c0621b : figures .lisible à max-width en ligne (88) agrandies (!important), schéma centré à
  sa largeur utile, légende dans la colonne au téléphone ; module CONTENU : rattrapage des
  finitions quand la restauration (+120 ms) précède la lecture du module (bug sous charge,
  4/5 : panneau sans typographie/.mj-large/schémas). Vérifié : parallele.sh (6/6 OK), figs.js
  (figs-t, figs-o : planches), bal6 (20 panneaux à schémas : 0 constat de contenu).
- En cours : t-fin3 = site, interactions, pwa, regressions, mobile, visuel --strict (≈ 25 min).
- Reste : vérifier t-fin3, journal, git checkout --detach.
- t-fin3 (HEAD 1c0621b, 21 min 42 s) : site, interactions, pwa, regressions, mobile OK ;
  visuel --strict : 108 groupes de constats IDENTIQUES à t-c2, aucun dans CONTENU/SIMU
  (span.num = numéros d'onglets « 01–05 », PAGE ; en-tête/kbd/badges = COQUILLE ; cartes/quiz/
  Aujourd'hui/Bilan = REVISION ; recherche/menu Plus = FENETRES).
- TERMINÉ : branche wip/refonte-b à 1c0621b, worktree détaché (git checkout --detach).
