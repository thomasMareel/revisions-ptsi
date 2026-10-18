# Journal — tâche SOCLE de la refonte (branche wip/refonte)

Copie de travail : /home/user/revisions-ptsi/.claude/worktrees/wf_34f13d39-955-1
Branche : wip/refonte (créée depuis claude/repo-analysis-vjplbu @ 346cfa9)

## Plan
1. [ ] Rangement du CSS en régions (sur le CSS d'origine) + contrôle d'équivalence de cascade
2. [ ] Jetons (tokens.css) dans RÉGION JETONS + script de thème du <head> (data-theme-pref) + meta theme-color + CLAUDE.md
3. [ ] BASE = composants.css §0 et §1
4. [ ] Polices (vendor/fonts, polices.css, <link>, impression, mentions nominatives, PRECACHE)
5. [ ] MathJax chtml.scale 1.07 (page + impression)
6. [ ] data-mat (.chapter, rangées du tiroir, .chap-title-banner)
7. [ ] getCanvasColors/__CV : muted/grid depuis les jetons
8. [ ] regions.md
9. [ ] Tests : validate, check_js, site, interactions, pwa, regressions (+ visuel/mobile notés)
10. [ ] git checkout --detach

## Fait
- [x] 1. Régions : commit 8129080. Outils dans scratchpad/refonte/impl/socle/ (regions.py = classement +
  écriture ; conflits.py + conflits-dom.js = contrôle de cascade ; compare-styles.js = styles calculés
  avant/après ; remplacer_region.py = remplace le contenu d'une région). 0 conflit, styles identiques.
  Petits autres blocs <style> laissés en place : (a) <style> dans #cine-exos (schémas SVG des exos de
  cinématique, .cine-svg-wrap / .svg-*) → propriétaire CONTENU ; (b) <style id="sr-badge-style">
  injecté par le module « RECHERCHE AMÉLIORÉE » (.sr-badge, .sr-b-*, .search-group-label…) →
  propriétaire FENETRES ; (c) CSS du gabarit d'impression (const CSS dans printChapter) → IMPRESSION.
- [x] 2/3. Jetons + BASE (composants §0/§1) + script du <head> (data-theme-pref) + metas theme-color
  (applyTheme les aligne) + manifeste : commit b50c71d. CLAUDE.md : À FAIRE en fin de tâche (section
  « Variables CSS de thème » → jetons + régions + filet de sécurité ; Polices ; PRECACHE 45).
- [x] 4/5. Polices + MathJax 1,07 : commit 4bf2712 (pwa.js : contrôle Source Sans 3 + Source Serif 4).
- [x] 6/7. data-mat + getCanvasColors (muted=--text-3, grid=encre 8/12 %) + B4 mis à jour : commit 2b6d7b9.
- [x] CLAUDE.md : commit b99facc. regions.md écrit (scratchpad/refonte/impl/regions.md).
- [x] Tests : validate OK, check_js 0 erreur ; regressions 29/29 + pwa 8/8 OK ; site 11/11 OK
  (27 simulateurs clair+sombre, 0 erreur JS, 0 requête externe) ; interactions 20/20 OK.
  Matrice thème (theme-check.js) : 8/8 ok (« Clair » sur appareil sombre reste clair dès le <head>).
- [x] mobile + visuel : l'original passait les deux ; maintenant mobile 1 échec (formules +7 % à 1,07 :
  rlc-cours 415→441 et 11 autres aggravés, 3 nouveaux) ; visuel 2 échecs (compteurs rouges blanc sur
  --accent=#ff9085 en sombre 2,19:1, ic-lbl Signaler 2,21:1, kbd opacifiés ; débordement rlc-cours).
  Notés dans regions.md (« Dette de transition »). TOLERES : 38 constats disparus retirés (commit 37d0249).
- [x] git checkout --detach (fin de tâche) — voir dernière étape.

## TERMINÉ (branche wip/refonte, 7 commits 8129080..37d0249)
