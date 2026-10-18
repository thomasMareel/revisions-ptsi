# Refonte « Cahier de prépa » — note de reprise

*Mise à jour le 2026-10-18 au soir, après la fusion des trois lignes de travail.*
**Le site en ligne n'a pas changé** : `main` = `346cfa9` (cache `ptsi-cache-v88`). La refonte vit sur la branche `wip/refonte` (les branches `wip/refonte-a`, `-b`, `-c` y sont fusionnées).

## 1. Où trouver quoi

| Dossier | Contenu |
|---|---|
| `docs/refonte/conception/` | **Système de design final validé** : `SPEC.md` (spécification complète, 9 parties), `tokens.css`, `composants.css` (CSS de référence sur les classes du site), `maquettes/*.html` + `captures/*.png` (**cible visuelle** : 01 chapitre ordinateur, 02/02b téléphone, 03a/b/c navigation, 04a/b carte, 05 Aujourd'hui, 06a/b sombre, 07a/b thème, 08a/b/c exercices et simulateur, 09 spécimen, planches), `outils/` (contrôles de contraste, cibles, captures), `controles/` (résultats chiffrés). Pour rouvrir une maquette, recréer à côté de `maquettes/` les dossiers `../mathjax/` (copie de `vendor/mathjax/`) et `../polices/` (copie de `vendor/fonts/`). |
| `docs/refonte/travail/` | Journaux de chaque étape (`socle.md`, `ligne-A-coquille.md`, `ligne-A-page.md`, `ligne-B-contenu.md`, `ligne-B-revision.md`, `ligne-C-fenetres.md`, `fusion.md`), **`regions.md`** (régions du CSS et leurs propriétaires), outils des agents (`a/`, `ligneB/`, `socle/`), `couverture.py` (couverture CSS). |
| `docs/refonte/workflow/implementation-refonte.js` | Script du workflow d'implémentation (socle → lignes → fusion → relecture ×3 → vérification finale). |
| `CLAUDE.md` | **Réécrit à la fusion** : il décrit l'état du site refondu (coquille, navigation, page chapitre, contenu, simulateurs, fiche de révision, fenêtres, impression, régions CSS, jetons, règles « ne pas faire »). |

## 2. État des branches

| Branche | État |
|---|---|
| `wip/refonte` | **Socle + lignes A, B, C FUSIONNÉS, puis remis en cohérence** : en-tête `.hdr`, barre latérale / tiroir / page Chapitres, Sommaire de la matière, barre du téléphone qui s'efface, feuille ⋯, sélecteur de thème (ligne A, coquille) ; intercalaire, onglets, rail, pied (ligne A, page) ; contenu, exercices, simulateurs (ligne B, contenu) ; fiche de révision, quiz, Aujourd'hui, Bilan (ligne B, révision) ; fenêtres `.fen`, recherche, formulaire, toasts, impression (ligne C). Batterie complète verte, **`visuel --strict` : 0 constat** (82 écrans × thèmes × appareils), `TOLERES` et `DEBORDEMENTS_CONNUS` vides, état des flashcards identique à `main` octet pour octet. |
| `wip/refonte-a`, `-b`, `-c` | Historique des lignes (déjà fusionnées dans `wip/refonte`). |

Notes à garder en tête :
- Taille du texte : segmenté « A / A+ / A++ » (100/110/120 %) au lieu de « A− / A / A+ » (plancher de 13 px ; clé `readScale` inchangée). Écart volontaire.
- En 2ᵉ année, ouvrir un chapitre de 1ʳᵉ année garde la 2ᵉ année (sa partie se déplie).
- Colonne de lecture enveloppée dans `<article id="app-main" role="none">` (pas div/section : `</div>` orphelins du contenu).
- `CACHE_VERSION` volontairement **non** incrémenté sur `wip/refonte` : bump unique à la publication (`v89`).

## 3. Ce qui reste à faire, dans l'ordre

1. **Relecture adversariale** sous 4 angles (ordinateur, téléphone, fonctionnel/régressions dont l'état des flashcards identique à `main`, accessibilité/`visuel --strict`) + corrections, jusqu'à 3 tours.
2. **Vérification finale** : batterie complète verte, `visuel --strict` vert, planche avant/après pour l'utilisateur.
3. **Publication** (règle du CLAUDE.md) : branche `sauvegarde-avant-refonte` sur `main` actuel, bump de `CACHE_VERSION` (v89), fusion dans `main`, push, run Actions `completed success`, message à l'utilisateur.

## 4. Comment reprendre

1. `git fetch origin && git branch -a | grep wip/refonte`.
2. Copier `docs/refonte/workflow/implementation-refonte.js` et l'adapter : `F` (conception) → `<copie>/docs/refonte/conception` si le scratchpad d'origine n'existe plus ; `I` (journaux) → un dossier du scratchpad où l'on recopie `docs/refonte/travail/*.md` ; ne garder que les étapes restantes (relecture, vérification finale), en remplaçant les étapes faites par leur résumé (§2 ci-dessus et `travail/fusion.md`).
3. Lancer le workflow ; chaque agent relit son journal et reprend depuis `wip/refonte`.
