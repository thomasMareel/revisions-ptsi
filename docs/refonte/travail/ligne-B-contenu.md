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
