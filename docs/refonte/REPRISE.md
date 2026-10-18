# Refonte « Cahier de prépa » — note de reprise

*Travail interrompu proprement le 2026-10-18 à ≈ 15 h 15 (UTC), à la demande de l'utilisateur (économie de quota).*
**Le site en ligne n'a pas changé** : `main` = `346cfa9` (cache `ptsi-cache-v88`). La refonte vit uniquement sur les branches `wip/refonte*`.

## 1. Où trouver quoi

| Dossier | Contenu |
|---|---|
| `docs/refonte/conception/` | **Système de design final validé** : `SPEC.md` (spécification complète, 9 parties), `tokens.css`, `composants.css` (CSS de référence sur les classes du site), `maquettes/*.html` + `captures/*.png` (**cible visuelle** : 01 chapitre ordinateur, 02/02b téléphone, 03a/b/c navigation, 04a/b carte, 05 Aujourd'hui, 06a/b sombre, 07a/b thème, 08a/b/c exercices et simulateur, 09 spécimen, planches), `outils/` (contrôles de contraste, cibles, captures), `controles/` (résultats chiffrés). Les polices sont déjà dans `vendor/fonts/` (socle). Pour rouvrir une maquette, recréer à côté de `maquettes/` les dossiers `../mathjax/` (copie de `vendor/mathjax/`) et `../polices/` (copie de `vendor/fonts/`). |
| `docs/refonte/travail/` | Journaux de chaque étape (`socle.md`, `ligne-A-coquille.md`, `ligne-B-contenu.md`, `ligne-A-page.md`), **`regions.md`** (régions du CSS et leurs propriétaires), outils des agents (`a/`, `ligneB/`, `socle/` : scripts d'injection, captures, balayages). `ligneB/appliquer.py` réinjecte `contenu.css`/`simu.css`/`module.js` dans `index.html` (chemins à adapter). |
| `docs/refonte/workflow/implementation-refonte.js` | Script du workflow d'implémentation (socle → 2 lignes → fusion → relecture ×3 → vérification finale). |

## 2. État des branches

| Branche | Base | État |
|---|---|---|
| `wip/refonte` | `346cfa9` (main) | **Socle TERMINÉ** (`8129080`…`37d0249`) : grand `<style>` rangé en régions balisées (JETONS, BASE, COQUILLE, PAGE, CONTENU, SIMU, REVISION, FENETRES, IMPRESSION), jetons définitifs + base des composants, polices Source Serif 4 / Source Sans 3 / JetBrains Mono (PRECACHE à jour), MathJax `chtml.scale` 1,07, `data-mat`, couleurs canvas lues dans les jetons, CLAUDE.md mis à jour. Plus ce dossier `docs/refonte/`. |
| `wip/refonte-a` | `wip/refonte` (`37d0249`) | **Ligne A, étape 1 « coquille » TERMINÉE** (`e9140de`…`2639f87`) : en-tête `.hdr`, barre latérale / tiroir / page Chapitres, barre du téléphone qui s'efface, feuille ⋯, sélecteur de thème (popover + segmenté), Sommaire de la matière `#sommaire/<matière>`, retour Android, tests mis à jour (interactions 23/23, regressions, pwa, site verts ; visuel `--strict` : 0 constat dans son périmètre). **Étape 2 « page chapitre » : PAS COMMENCÉE** (juste planifiée, voir `ligne-A-page.md`). |
| `wip/refonte-b` | `wip/refonte` (`37d0249`) | **Ligne B, étape 1 « contenu + simulateurs » PRESQUE TERMINÉE** (`1e2e76c`…`b2e77a6`) : régions CONTENU et SIMU réécrites, module d'enrichissement du contenu (`.sec-num` découpé, `.diff` en barres, typographie française, `.mj-large`), courbes à l'encre du chapitre, Lorentz lisible, débordements à 390 px corrigés. **Reste** : relancer les suites (mobile, visuel `--strict`), nettoyer les `TOLERES` de son périmètre, commit final. **Étape 2 « révision et fenêtres » : PAS COMMENCÉE.** |

Notes des agents à garder en tête :
- Taille du texte : segmenté « A / A+ / A++ » (100/110/120 %) au lieu de « A− / A / A+ » (plancher de 13 px ; clé `readScale` inchangée). Écart volontaire.
- En 2ᵉ année, ouvrir un chapitre de 1ʳᵉ année garde la 2ᵉ année (sa partie se déplie).
- Colonne de lecture enveloppée dans `<article id="app-main" role="none">` (pas div/section : `</div>` orphelins du contenu).

## 3. Ce qui reste à faire, dans l'ordre

1. **Ligne B, fin de l'étape 1** (sur `wip/refonte-b`) : tests + `TOLERES` + commit.
2. **En parallèle** : ligne A étape 2 « page chapitre » (`wip/refonte-a` ; SPEC §4.4, §5.1, §7.4/5/10/11 ; composants §4, §8) et ligne B étape 2 « révision et fenêtres » (`wip/refonte-b` ; SPEC §5.4, §5.6–5.11, §5.15, §7.9, §7.13 ; composants §10, §11). Consignes exactes : tableau `LIGNES` du script.
3. **Fusion** de `wip/refonte-a` puis `wip/refonte-b` dans `wip/refonte`, batterie complète, documentation (CLAUDE.md, README, GABARIT).
4. **Relecture adversariale** sous 4 angles (ordinateur, téléphone, fonctionnel/régressions dont l'état des flashcards identique à `main`, accessibilité/`visuel --strict`) + corrections, jusqu'à 3 tours.
5. **Vérification finale** : batterie complète verte, `visuel --strict` vert, planche avant/après pour l'utilisateur.
6. **Publication** (règle du CLAUDE.md) : branche `sauvegarde-avant-refonte` sur `main` actuel, bump de `CACHE_VERSION` (v89), fusion dans `main`, push, run Actions `completed success`, message à l'utilisateur.

## 4. Comment reprendre

1. `git fetch origin && git branch -a | grep wip/refonte` (les trois branches doivent exister).
2. Copier `docs/refonte/workflow/implementation-refonte.js` et l'adapter :
   - `F` (dossier de la conception) → `<copie>/docs/refonte/conception` si le scratchpad d'origine n'existe plus ;
   - `I` (journaux) → un dossier du scratchpad où l'on recopie `docs/refonte/travail/*.md` ;
   - **sauter les étapes faites** : remplacer l'appel `socle` par son résumé (§2 ci-dessus), retirer l'étape « coquille » de la ligne A, et remplacer l'étape « contenu » de la ligne B par « finir l'étape contenu (tests, TOLERES, commit) » ;
   - garder ensuite les étapes « page », « revision », la fusion, la relecture et la vérification finale.
3. Lancer le workflow ; chaque agent relit son journal et reprend depuis sa branche.
