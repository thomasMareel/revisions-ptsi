# `cine` (prefix `cine`) — alignement sur le chapitre `liaisons` (SI, 1ʳᵉ année), 2026-11-21

Alignement seulement (pas de réécriture générale) : liste « À aligner dans `cine` » de `AN1/lia-revue.md` traitée en
entier, plus les passages incomplets ou faux rencontrés. Script unique : `cine_aligner.py` (retouches ciblées des panneaux
actuels, copiés dans `_tmp/cine_orig_*.html`).

## Fichiers produits (dans `AN1/`)

| Fichier | Contenu |
|---|---|
| `cine-cours.src.html` | cours aligné (≈ 27 000 signes) : bloc « AU PROGRAMME · PTSI » ajouté, §3 complété, §4 réduit à un rappel, §5 complété, §6 aligné |
| `cine-meth.src.html` | méthode 4 renvoyée à `liaisons` (méthodes 4, 5, 6, 7) ; formule trop longue de la méthode 2 passée en bloc |
| `cine-cartes-corr.json` | 6 cartes corrigées (réponse seule) |
| `cine-cartes-ajout.js` | 2 cartes ajoutées (25 → 27) |

`cine-exos` n'est pas modifié (aucune notation à aligner ; ses corrigés sont cohérents avec le cours corrigé).

## Liste de `lia-revue.md` : ce qui a été fait

1. **§4** (7 liaisons sur 11, une ligne « Libre », aucun domaine de validité) : réduit à un rappel — définition de \(n_c\),
   torseur cinématique d'une liaison, formes de la pivot (« en tout point de l'axe »), de la glissière (« en tout point »),
   de la sphérique (« au centre seulement ») et de l'hélicoïdale (pas \(p_h\)), exemple chiffré d'une vis, tableau des
   onze liaisons avec \(n_c\) et mouvements permis ; renvois à `liaisons` §2, §3, §4, §6, §7, §8, §10.
2. **« DDL »** (14 occurrences) → \(n_c\) / « degrés de liberté » ; « Pivot-glissant » → « pivot glissant » ; hélicoïdale
   \(\dot\lambda = \frac{p}{2\pi}\dot\theta\) → pas \(p_h\). Cartes 14 à 17 : réponses seules retouchées (\(n_c\), domaine de
   validité), questions inchangées.
3. **§6, graphe et mobilité** : paragraphe réduit, renvoi à `liaisons` §7, §8, §10 ; formule plane écrite
   \(m - h = 3(n-1) - I_s\), \(I_s = \sum n_s\), \(n_s = 3 - n_c\), avec la forme \(h_{\text{plan}} = m - I_c + 3\gamma\) et
   des renvois à `liaisons` §10, §12 et `statique` §6, §8 ; carte 23 alignée.
4. **§6, fermeture** : renvoi à `liaisons` §8 (pompe traitée) et §10 (fermeture cinématique) ; **roulement sans
   glissement** : vitesse de glissement \(\vec V_g\) et renvoi à `liaisons` §5.
5. **Méthode 4, étape 1** : renvoi aux méthodes 4 et 5 de `liaisons` (et 6, 7 en exemple).
6. Cartes 14 à 17 : traitées (point 2).

## Erreurs et manques corrigés en plus

- **Signe de la vitesse du centre d'une roue** (§6 : « \(v_C = R\dot\theta\) ») : avec l'orientation usuelle (\(\vec z\)
  sortant, roue avançant selon \(+\vec x\) sur un sol de normale \(\vec y\)), \(v_C = -R\dot\theta\), comme le corrige l'EXO 03.
  Calcul écrit dans le cours ; carte 22 (« sans valeur absolue en algébrique ») corrigée.
- **Figure du CIR** : « v⃗(A) » écrit avec la flèche combinante U+20D7, affichée en carré → **v** en gras.
- **Bloc « AU PROGRAMME · PTSI »** absent → ajouté (capacités B2/C1/C2 du S1-S2 ; Frenet signalé comme relevant du
  programme de physique, Coriolis hors programme).
- **Mouvements simples** (translation, rotation autour d'un axe fixe ; programme S1) absents → définition et exemple de la
  grande roue (§3) ; carte ajoutée.
- **Composition des torseurs cinématiques** \(\{\mathcal V(2/0)\} = \{\mathcal V(2/1)\} + \{\mathcal V(1/0)\}\) (base de la
  fermeture cinématique de `liaisons` §10) absente → ajoutée au §5 avec un exemple (chariot d'une grue à tour) ; carte ajoutée.
- Notations : phrase reliant \(\vec v(A\in S/\mathcal R)\) à \(\vec V(A, S/\mathcal R)\) et \(\{\mathcal V(2/1)\}\) de `liaisons`.
- Coriolis : « rarement exigée en PTSI » → « hors programme (pour aller plus loin) », titre de la sous-section signalé.
- « Si m = 1 : mécanisme à un degré de liberté » (confusion mobilité / degré de liberté) → reformulé.

Les numéros de section (§1 à §6) sont inchangés : `liaisons` renvoie à « Cinématique », §6 (CIR) et méthode 4.

## Vérifications

- Exemples ajoutés recalculés : grande roue (\(2\pi/600 \times 20 \approx 0{,}21\) m/s), vis (\(p_h N/60 = 20\) mm/s,
  \(62{,}8\times0{,}005 \approx 0{,}31\) m/s), grue (\(0{,}2\times10 = 2\) m/s, norme 2,06 m/s), signe de \(v_C\).
- `verif_src.py` : aucune erreur ni « attention » ; `apercu_src.py` à 390 et 1 440 px : `merr`, `brut`, `larges` vides,
  aucune erreur JS ; figure du CIR regardée en clair et en sombre.
- Cartes : `corriger_cartes.py cine … --essai` (6) et `ajouter_cartes.py cine … --essai` (25 → 27) sans erreur ; textes
  rendus sans erreur MathJax.

## Doutes et points signalés (non traités ici)

1. `cine-exos` : libellés SVG à 10-11 px ; surtout, son `<style>` (classes `.svg-*`) est le seul endroit où ces classes
   sont définies, alors qu'il est replié dans un `<template>` : `sb-exos`, `s2-exos` et `bode-exos` les emploient aussi et
   s'affichent sans style tant que `cine-exos` n'a pas été ouvert (texte noir par défaut, illisible en sombre). Correctif
   conseillé : déplacer ces règles dans la région CONTENU du grand `<style>`. (`stat-exos` n'en dépend plus.)
2. Un tiers du chapitre reste de la cinématique du point (Frenet, cylindrique), au programme de physique : conservé.
