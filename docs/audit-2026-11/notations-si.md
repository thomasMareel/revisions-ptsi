# SI : harmonisation des notations (point 3 de l'audit du 14/11/2026)

Sources : `docs/audit-2026-11/si-1a.md` §4 « Notations incohérentes », programme `pdf-pt/prog/si.txt`
(l. 261-266 : « chaine de puissance », « fonctions alimenter, moduler, convertir, transmettre et agir »), chapitres de
2ᵉ année du site pour les références (`chaines`, `dyn2a`, `energ2a`, `multiphy`). Panneaux extraits du dépôt actuel
(points 1 et 2 déjà intégrés), copies d'origine dans `REV3/_si_orig/`.

Fichiers produits (tous dans REV3) : 10 panneaux `*.src.html` (`s2-exos`, `corr-cours`, `corr-meth`, `corr-exos`,
`afs-cours`, `afs-meth`, `afs-exos`, `cine-cours`, `stat-cours`, `tr-exos`) et 10 fichiers de cartes
`*-cartes-corr.json` (`s2`, `stab`, `slci`, `corr`, `afs`, `sb`, `tsu`, `cnd`, `cine`, `stat`). Aucune carte ajoutée,
retirée ni déplacée ; aucune question en double dans ces paquets (vérifié) : retouches de texte à longueur et ordre
inchangés, progression conservée (repli par rang de `flashLoadState`).

## 1. Amortissement : ξ partout (cible : ξ, notation des cours de 1ʳᵉ année, de la 2ᵉ année et des vidéos)

| Où | Occurrences modifiées |
|---|---|
| `sys2` exercices (`s2-exos`) | 37 : EXO 01 à 06, énoncés et corrigés (36 `z` → `\xi` dans les formules ; « Relier Q et z » → « Relier Q et ξ ») |
| `sys2` cartes (`s2`) | 22 cartes : 0, 1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 (questions retouchées : 1, 3, 5, 10, 12, 13, 15, 16, 18, 19, 20, 21, 23, 24). Cartes en Unicode restées en Unicode (ξ) ; carte 13 (TeX) : `\xi` |
| `stabilite` cartes (`stab`) | 1 carte : 16 (« Mφ ≈ 100ξ », « ξ = 0,45 ») — l'audit disait « stabilite (16) » : c'est la **carte 16**, la seule du paquet en z |
| `slci` cartes (`slci`) | 6 cartes écrites en **ζ** (non signalées par l'audit) : 8, 9 (question), 10, 11, 19, 21 (question) → ξ / `\xi` |

Rien d'autre à changer : les cours, méthodes, exercices et simulateurs de `slci`, `schblocs`, `sys1`, `sys2`, `bode`,
`stabilite`, `precision`, `correcteurs`, `sysnum` écrivent déjà ξ. Laissés : les identifiants HTML `slci-z`,
`slci-z-ctrl`, `slci-z-val` et la variable `z` du code des simulateurs (invisibles, libellé déjà « Amortissement ξ ») ;
« transformée en z » de `sysnum` (autre sens). Rendu des cartes vérifié avec le `flashPretty` du site : même découpage
texte / formules qu'avant, à la lettre près.

## 2. Constante d'intégration du PI : T_i (cible : T_i, notation de `precision`, `sysnum`, `slci` et de la vidéo)

| Où | Occurrences modifiées |
|---|---|
| `correcteurs` cours | 34 `T_I` → `T_i` ; libellé SVG du Bode du PI (`1/T` indice I → i), légende (`1/T<sub>i</sub>`) et `aria-label` (« 1/Ti ») ; et, pour garder la formule cohérente, `K_I = K_p/T_I` → `K_i = K_p/T_i` (2 `K_I` ; les exercices du chapitre écrivaient déjà `K_i`, comme `schblocs`) |
| `correcteurs` méthodes | 4 |
| `correcteurs` exercices | 11 |
| `correcteurs` cartes (`corr`) | 6 cartes : 13, 14, 15 (question : « T_i·ω = 10 »), 16, 32, 41 |

Vérifiés sans changement : `resnum`, `chfonc`, `multiphy` (aucun T_I ni T_i), `precision` et `sysnum` (déjà T_i).
Laissé : `TI` nom de variable dans le code Python de `sysnum` (exos, `KP, TI, TE = …`), identifiant de code.

## 3. Chaîne de puissance (cible : vocabulaire du programme 2021 et de la 2ᵉ année)

| Où | Modifications |
|---|---|
| `ingsys` cours | surtitre du §3 « CHAÎNES DE PUISSANCE ET D'INFORMATION » ; figure : titre « Chaîne de puissance », boîte « Moduler », `aria-label` ; légende ; intertitre « Chaîne de puissance » ; encadré « Alimenter → Moduler → Convertir → Transmettre → Agir » avec **une seule** mention « (anciennement « chaîne d'énergie », avec « distribuer » au lieu de « moduler ») » ; « Moduler : le pré-actionneur, ou modulateur de puissance (relais, hacheur, variateur, distributeur) » ; couplage des deux chaînes (8 retouches) |
| `ingsys` méthodes | titre de la méthode 2 (1) |
| `ingsys` exercices | EXO 01 Q1 et corrigé (« Moduler : variateur/relais ») ; concours « portail » : titre, partie B, B1 et corrigé (« Moduler », ordres vers « Moduler ») ; concours « treuil » : titre « Bilan de puissance le long d'une chaîne de puissance », ligne de source, énoncé (10 retouches) |
| `ingsys` carte 7 | question « … de la chaîne de puissance ? » ; réponse « Alimenter → Moduler → … (source, pré-actionneur ou modulateur, actionneur, transmetteur, effecteur) » |
| `schblocs` carte 9 | « Chaîne de puissance : les 5 fonctions. » / « Alimenter → Moduler → Convertir → Transmettre → Agir. » (le cours de `schblocs` disait déjà « chaîne de puissance … moduler ») |

Gardés : « pré-actionneur » (le programme dit « préactionneurs », l. 280) ; « flux d'énergie » de la méthode 2 et
« matière, énergie et information » (flux, pas le nom de la chaîne).
**Hors de ma liste, à signaler** : `cvs` écrit encore « chaîne d'énergie » (intro du cours, et carte 0 « … son rôle dans
une chaîne d'énergie ? »).

## 4. Cartes de `trsurf` (`tsu`, 20) et `cnd` (20)

Fait : les 40 réponses commencent par « Hors programme (culture technologique) : » (questions inchangées).

## 5. Cinématique et statique (référence : `chaines`, 2ᵉ année)

Fait (changements simples et locaux) :
- `cine` cours (5 retouches) : torseur cinématique `\{V(S/\mathcal{R})\}_A` → `\{\mathcal{V}(S/\mathcal{R})\}_A` ;
  §4 : « (DDL), noté \(n_c\), » ; §6 : \(m = I_c - r_c\) avec \(I_c = \sum n_c\) (nombre d'inconnues cinématiques),
  décompte \(m - h = 3(n-1) - \sum(3 - n_{c,i})\) et la phrase qui suit ; carte 23 alignée (\(I_c\), \(n_{c,i}\)).
- `statique` cours : torseurs `\{T(…)\}` → `\{\mathcal{T}(…)\}` (§1 et actions mutuelles, 3) et torseurs des liaisons
  `\{\mathcal{T}_{\text{enc}}\}`, `pivot`, `glis`, `appui` (4) : cela lève aussi l'ambiguïté avec la composante
  tangentielle T de Coulomb ; cartes 5 et 7. \(I_s\), \(E_s\), \(h = m + I_s - E_s\) : déjà en place (point 2).

Non fait (demanderait de réécrire les formules de tout le chapitre, à faire avec le futur chapitre « Liaisons et schéma
cinématique ») : les **vitesses** de `cine` (≈ 70 `\vec{v}` dans le cours, les méthodes, les exercices et les cartes,
le plus souvent abrégées en \(\vec{v}(A)\) sans le mouvement ; §2 de cinématique du point, où v minuscule est la
notation de physique) contre \(\vec{V}(P, j/i)\) de `chaines`. Le sigle « DDL » est gardé dans le texte de `cine` et
`statique` (`chaines` n'emploie aucun sigle, seulement « degrés de liberté » et \(n_c\), désormais introduit en 1ʳᵉ année).

## 6. Facultatif

- **J_Δ (`dynsolide`) / I_Δ (`dyn2a`)** : non fait. La 2ᵉ année n'est pas homogène : `dyn2a` écrit \(I_\Delta\) pour
  l'opérateur d'inertie, mais \(J_\Delta\) en rappelant le résultat de 1ʳᵉ année et dans \(E_c = \frac12 J_\Delta\omega^2\) ;
  `energ2a` et `energsi` écrivent \(J_{eq}\), \(J_m\), \(J_p\). Passer `dynsolide` à I_Δ le rendrait incohérent avec
  ses propres \(J_G\), \(J_O\) et avec \(J_{eq}\). Plus gênant qu'utile.
- **Rapport de transmission** : la 2ᵉ année n'écrit pas i mais **k** (`energ2a`, `multiphy` : \(k = \omega_s/\omega_m\)) ;
  `transm` écrit i (\(i_{12}\), \(i_{global} = \prod i_k\)…), `energsi` r. Trois notations : le choix est à arbitrer
  (k partout obligerait à réécrire `transm`, où k sert d'indice), donc **`energsi` non modifié**. Fait seulement : dans
  `transm`, l'exercice « Concours PT » « Train d'engrenages » écrivait r alors que tout le chapitre écrit i → i (4).
- **Frottement visqueux f (`energsi`) / f_v (2ᵉ année)** : non fait. En 2ᵉ année, \(f_v\) est le coefficient **en
  rotation** (N·m·s/rad) et le coefficient en translation s'écrit **c** (`energ2a`, carte 34 de `multiphy`) ; `energsi`
  emploie f pour un amortisseur en translation (N·s/m), comme `sys2` (carte 12, EXO 05). Changer energsi seul ne
  rétablirait pas la cohérence.

## 7. Repéré hors de ma liste (non modifié)

- `stabilite` carte 18 : retard pur « e^(−Lp) » (audit §4) alors que `slci` et la carte 27 écrivent T.
- `cvs` : « chaîne d'énergie » (voir §3).
- `sys2` carte 12 et EXO 05 : f pour l'amortisseur et \(f_0\) pour la fréquence propre dans le même exercice.

## 8. Contrôles

- `verif_src.py` sur les 10 panneaux : aucune ERREUR ; attentions déjà présentes à l'identique dans les panneaux
  d'origine (« pas de bloc AU PROGRAMME · PT » pour `afs-cours`, `cine-cours`, `stat-cours` ; 10 formules en ligne
  longues dans `s2-exos`, deux signes de plus chacune à cause de `\xi`).
- `corriger_cartes.py … --essai` : sans erreur pour les 10 fichiers de cartes.
- `diff` panneau du dépôt ↔ REV3 relu pour les 10 panneaux : seules les retouches décrites (et l'absence de saut de
  ligne final, comme à l'extraction).
- Aperçus (`apercu_src.py`, 390 et 1440 px) : voir ci-dessous.
- Aperçus (`apercu_src.py`, 390 et 1440 px, 20 aperçus pour 10 panneaux) : `merr`, `brut`, `larges` vides et aucune
  erreur JS partout, sauf `s2-exos` à 390 px : « ATTENTION : la page déborde (577 px) » sur 8 formules en ligne des
  corrigés (EXO 01, 02, 03, 05). **Déjà présent à l'identique sur le panneau d'origine** (même aperçu : 577 px, mêmes
  formules) : artefact de l'outil, qui déplie les solutions sans passer par `toggleSol`. Une fois `window.__apresRendu`
  appelé comme le fait le site au dépliage, origine et version modifiée tombent toutes deux à `scrollW` = 390
  (script `/tmp/claude-0/-home-user/6f48d12f-3f0e-5709-96fa-34955b53c076/scratchpad/si3/rendu.py`, avec le
  `voir_rendu.js` de la revue 2).
