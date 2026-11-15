# Mathématiques de 1ʳᵉ année : notations harmonisées (point 3 de l'audit du 14/11/2026)

Sources : `docs/audit-2026-11/maths-1a.md` §4 (tableau « Notations incohérentes »), programme `ptsi_maths.txt` (PTSI) et `maths.txt` (PT), 2ᵉ année du site.
Les panneaux de départ sont ceux du dépôt actuel, qui contient déjà les corrections des points 1 et 2. Ils sont copiés dans `REV3/_maths_orig/` (`<p>-<onglet>.html`, plus les cartes numérotées `<p>-cartes.txt`).
Le dépôt n'a pas été modifié : `corriger_cartes.py` n'a été lancé qu'avec `--essai`.

## Fichiers produits (dans `REV3`)

| Chapitre (prefix) | Panneaux | Cartes |
|---|---|---|
| proba (`prb`) | `prb-cours`, `prb-meth`, `prb-exos` | `prb-cartes-corr.json` (11, dont 7 questions retouchées) |
| va (`va`) | — | `va-cartes-corr.json` (3, rendu de V(X) cassé, voir plus bas) |
| polynomes (`pol`) | — | `pol-cartes-corr.json` (1) |
| fonctions (`fn`) | `fn-cours`, `fn-meth`, `fn-exos` | `fn-cartes-corr.json` (5, dont 2 questions) |
| dl (`dl`) | `dl-cours` | — |
| primitives (`prim`) | `prim-cours` | — |
| integrales (`int`) | `int-meth` | — |
| det (`det`) | `det-cours`, `det-exos` | `det-cartes-corr.json` (2, dont 1 question) |
| matrices (`mat`) | `mat-exos` | `mat-cartes-corr.json` (6, dont 2 questions) |
| ev (`ev`) | `ev-cours`, `ev-meth`, `ev-exos` | `ev-cartes-corr.json` (1) |
| contderiv (`cd`) | `cd-cours` | `cd-cartes-corr.json` (3, dont 1 question) |
| edo (`edo`) | `edo-cours` | `edo-cartes-corr.json` (2, dont 1 question) |

Chaque panneau est dans `REV3/<p>-<onglet>.src.html`, 17 panneaux et 34 cartes en tout.
Aucune carte n'est ajoutée, retirée ni déplacée. 14 questions sont retouchées, toujours à rang inchangé et sans question en double dans le paquet (le script le vérifie) : la progression des élèves est conservée par le repli par rang.

Contrôles :
- `verif_src.py` : aucune ERREUR. Les « attention » restantes existaient déjà : formules en ligne longues de `cd-cours`, et « pas de bloc AU PROGRAMME » sur les cours de 1ʳᵉ année. Celle de `ev-cours` a disparu, la formule raccourcie avec les flèches retirées.
- `apercu_src.py` à 390 et à 1440 px : aucune régression. Les débordements qui restent à 390 px existaient déjà ; le détail est dans la dernière section.
- `corriger_cartes.py --essai` : sans erreur pour les 9 fichiers.
- `diff` contre le panneau du dépôt : seules les modifications ci-dessous apparaissent.

## Notation par notation

### 1. Espérance et variance → E(X), V(X), σ(X)
La cible est fixée par le programme (« E(X) », « V(aX + b) = a²V(X) », « σ(X) »). `va` et la 2ᵉ année l'utilisent déjà.

Modifications :
- **`prb-cours`** : 15 𝔼[·] et 11 Var. Toutes les formules de §3 et §4 sont reprises. Le crochet ne sert plus qu'au regroupement extérieur, V(X) = E[(X − E(X))²], comme dans `va`.
- **`prb-meth`** : 7 𝔼 et 5 Var (méthode 4, Markov, Bienaymé-Tchebychev, pièges). On écrit V(X) = E(X²) − E(X)², forme du programme.
- **`prb-exos`** : 5 𝔼 et 3 Var.
- **Cartes `prb`** :
  - n° 12, 15, 16, 17, 18, 19 et 21 : question et réponse ;
  - n° 13, 14, 24 et 25 : réponse seule.
- σ(X) était déjà écrit ainsi partout.

Laissé tel quel : aucune autre occurrence en 1ʳᵉ année. `denombrmt` et `va` écrivaient déjà E(X) et V(X).

### 2. Coefficient binomial → \(\binom{n}{p}\) ; formule du binôme
Le programme écrit le coefficient binomial \(\binom{n}{k}\), mais ne donne pas de forme explicite pour la formule du binôme. J'ai retenu \((a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}\). C'est la forme de `denombrmt` (cours et carte n° 6), de `matrices` (\(A^k B^{n-k}\)) et de la 2ᵉ année (`series2a`, produit de Cauchy).

Modifications :
- `prb-cours` : « = C_n^p » supprimé de la définition (1 occurrence, la seule de la 1ʳᵉ année). La formule du binôme passe de \(a^{n-k}b^k\) à \(a^k b^{n-k}\).
- Carte `pol` n° 18 : même changement d'ordre.

Laissé tel quel :
- **« C(n,k) » dans 20 cartes en Unicode** : `denombrmt` (12 cartes), `pol` (4), `prb` (3), `va` (1). C'est la transcription Unicode du coefficient binomial, et non la notation C_n^p : on ne peut pas écrire \(\binom{n}{k}\) sans TeX, et une carte en Unicode doit rester en Unicode. Si l'on veut \(\binom{n}{k}\) partout, il faut réécrire ces 20 cartes en `\\( … \\)`. C'est à décider.
- Les arrangements A_n^p ne font pas partie de la liste.

### 3. Fonctions hyperboliques → ch, sh (TeX : `\operatorname{ch}`, `\operatorname{sh}`)
Cible : programme (« sh, ch ») et forme TeX de la 2ᵉ année du site (`\operatorname{ch}` : 104 occurrences, `\operatorname{sh}` : 74, dans `con`, `gpl`, `sen`, `ed2`…).

Modifications :
- `dl-cours` : 6 (tableau des dérivées et DL de ch et sh).
- `fn-exos` : 28 (EXO sur f_p et f_i, EXO « fonctions hyperboliques », dont \(\operatorname{sh}^{-1}\)).
- `fn-meth` : 17 `\text{ch|sh|th|Argsh|Argch}` → `\operatorname{…}`. Le rendu ne change pas : la méthode écrivait déjà ch et sh, seule l'écriture TeX est alignée.
- `prim-cours` : 4 `\mathrm{ch|sh}`.
- `int-meth` : 1 `\mathrm{sh}`.
- **Cartes `fn`** :
  - n° 17 (question et réponse) et n° 18 : cosh, sinh → ch, sh ;
  - n° 19 : la question devient « Réciproque de sh » et la réponse « Argsh x = … », comme dans `fn-meth`.

La carte `dl` n° 31 écrivait déjà ch et sh.

### 4. Transposée → A^⊤
La cible est fixée par le programme (« Notation A^⊤ »). `matrices` et la 2ᵉ année l'utilisent déjà (`^\top`, 346 occurrences).

Modifications :
- `det-cours` : 2.
- `det-exos` : 2.
- Carte `det` n° 5 : la question devient « det(A^⊤) = ? ».
- Carte `det` n° 11 : réponse « com(A)^⊤ ». J'y ai aussi corrigé un rendu fautif : « (1/det A) » s'affichait comme \(\frac{1}{\det}A\). La carte s'écrit maintenant « (1/(det A)) ».

Aucune autre occurrence de A^T en 1ʳᵉ année.

### 5. Rang → rg
La cible est fixée par le programme (« Notation rg(x₁, …, xₙ) », « rg(u) »). `applin` et la 2ᵉ année l'utilisent déjà.

Modifications :
- `det-cours` : 1 (`\mathrm{rang}(A)` → `\operatorname{rg}(A)`).
- Carte `ev` n° 14 : rang(A) → rg(A).
- `matrices` est ajouté à la liste parce que le chapitre se contredisait : son cours écrit \(\operatorname{rg} f\), alors que ses cartes et un corrigé écrivaient « rang ».
  - `mat-exos` : `\dim\ker + \text{rang}` → `\dim\ker f + \operatorname{rg} f`.
  - Cartes `mat` n° 3, 16, 22 et 28 : réponse.
  - Cartes `mat` n° 4 et 5 : question.

Laissé tel quel :
- le mot « rang » dans la prose (« calculer le rang de A », « théorème du rang », « rang-nullité ») ;
- `prb-meth`, « X = rang » du premier succès, qui n'est pas un rang de matrice.

**À savoir** : `flashPretty` met « rang » en romain (`\operatorname{rang}`) mais pas « rg ». Dans les cartes Unicode, « rg(A) » s'affiche donc en italique, comme le font déjà les cartes `lin` n° 12 et 13. Même chose pour « ch », « sh » (cartes `fn` n° 17-18 et `dl` n° 31).

Correctif proposé, une ligne dans `flashPretty` : remplacer `/\b(rang|Vect|pgcd|ppcm|Card|Ker|diag|sgn)\b/g` par `/\b(rang|rg|ch|sh|Vect|pgcd|ppcm|Card|Ker|diag|sgn)\b/g`. Cette regex ne porte que sur les fragments déjà reconnus comme mathématiques. À valider par la suite `site` : je n'ai pas modifié le JavaScript.

### 6. Vecteurs d'un espace vectoriel abstrait → lettres nues (`ev`)
La cible est celle d'`applin` et d'`ev2a`. Chaque occurrence a été relue.

Modifications :
- `ev-cours` : 68 (63 vecteurs u, v, f, g, e_i, v_i et 5 vecteurs nuls → \(0_E\), notation d'`applin`).
- `ev-meth` : 9 (dont 3 \(0_E\)).
- `ev-exos` : 21. Les vecteurs nuls y deviennent :
  - \(0_{\mathbb{R}^3} = (0,0,0)\) ;
  - \(\{0\}\) deux fois, comme dans les cartes et en 2ᵉ année ;
  - « la fonction nulle \(0\) est paire » au lieu de « \(\vec 0\) pair ».

Une espace est insérée après une commande TeX (`\lambda u`, `1\cdot u`). Les cartes `ev` n'avaient pas de flèche.

Laissé tel quel :
- `lin-simu`, qui écrit \(\vec{e_1}, \vec{e_2}\) : flèches dessinées dans le plan, donc géométrie ;
- les flèches de `geometrie`.

### 7. Bornes atteintes → « théorème des bornes atteintes »
La cible est fixée par le programme (« Théorème des bornes atteintes »). `fpv` l'utilise déjà.

Modifications :
- `cd-cours` :
  - h2 « TVI, bornes atteintes, image d'un intervalle » ;
  - h3 « Théorème des bornes atteintes » ;
  - énoncé « Théorème (parfois appelé théorème de Weierstrass) », seule mention gardée.
- `fn-cours` : h2 « Fonctions monotones — Théorème des bornes atteintes ».
- Carte `cd` n° 4 : la question devient « Énoncer le théorème des bornes atteintes. ».
- Carte `fn` n° 21 : « — théorème des bornes atteintes ».

La carte `cd` n° 18 était déjà correcte.

### 8. Intervalles ouverts → ]a, b[
Le programme et tout le reste du site écrivent ]a, b[.

Modifications :
- `fn-cours` : arctan : \(\mathbb{R}\to\, ]-\pi/2,\pi/2[\).
- `fn-exos` : « valeurs \(\in\, ]0,1/e[\) ».
- Carte `fn` n° 14 : « ℝ → ]−π/2, π/2 [ ». L'espace avant « [ » est voulue : collée, `flashPretty` lit « π/2[ » comme \(\frac{\pi}{2[}\). Avec l'espace, la carte s'affiche bien ]−π/2, π/2[ (vérifié).

Aucune autre parenthèse d'intervalle ouvert en 1ʳᵉ année : les autres « (a, b) » sont des couples ou des coordonnées.

### 9. Amortissement → ξ (`edo` §3)
L'équation y est bien écrite sous forme canonique \(\ddot y + 2\xi\omega_0\dot y + \omega_0^2 y = 0\). La cible est celle des sciences de l'ingénieur du site.

Modifications :
- `edo-cours` : 6 ζ → ξ.
- Carte `edo` n° 24 : question et réponse.
- Carte `edo` n° 25 : réponse.

Pas d'autre ζ en 1ʳᵉ année.

### 10. Définition des limites → inégalités larges (`contderiv`)
La cible est fixée par le programme (« Les définitions sont énoncées avec des inégalités larges »). `suites` l'utilise déjà. ε > 0 et η > 0 restent stricts.

Modifications :
- `cd-cours` : 3 formules, soit 6 inégalités (limite, continuité, et continuité uniforme, qui est hors programme mais gardée cohérente).
- Carte `cd` n° 0 (continuité) et n° 19 (continuité uniforme).

Laissé tel quel : `logique`, EXO Q3 et carte n° 21. C'est un exercice de négation sur une phrase donnée avec des inégalités strictes. Ce n'est pas un renvoi direct, et le changer obligerait à refaire la négation.

## Correction liée : V(X) mal rendu dans les cartes
Dans une carte en Unicode, `flashFrac` prend seulement « (X) » comme numérateur. « V(X)/ε² » s'affichait donc \(V\frac{X}{\varepsilon^2}\), et « √V(X) » s'affichait \(\sqrt{V}(X)\). Ce défaut existait déjà dans `va` et serait apparu dans `prb` avec la nouvelle notation.

La correction met des parenthèses de regroupement, que `flashPretty` retire à l'affichage, par exemple « (V(X))/ε² » et « √(V(X)) ». Elle touche :
- les cartes `va` n° 16, 23 et 24 ;
- les cartes `prb` n° 24 et 25.

Le rendu a été vérifié avec le vrai `flashPretty` du site.

## Défauts vus en passant (hors mission, non corrigés)
- `fn-exos`, EXO « injectivité » Q2 : le corrigé contient un brouillon, « par exemple \(f(0)=f(2e^{-2}\cdot e^{?})\)... Plus précisément ». L'exemple est faux de surcroît : f(0) = 0 n'est atteint qu'en 0.
- `geo-exos`, EXO moments, corrigé : brouillon « Hmm: … ✓... Ah : formule de transport ».
- `ev-exos`, EXO somme directe Q2 : « \(\{(0,0,0,t):t\in\mathbb{R}\}...\) mais \(t=0\) aussi ».
- Carte `fn` n° 17 : « e⁻ˣ » s'affiche e^{-}ˣ, avec l'exposant mal formé.
- Hors liste, mais le programme les fixe : il écrit Arcsin, Arccos, Arctan, alors que le site écrit arcsin, arccos, arctan.

## Aperçus (`apercu_src.py`, 34 passages : 17 panneaux à 390 et 1440 px)
- Résultat global : `merr` et `brut` vides partout, et aucune erreur JS.
- À 1440 px : `larges` est vide partout.
- À 390 px, cinq panneaux débordent : `prb-exos` (811 px), `fn-exos` (742 px), `det-exos` (862 px), `mat-exos` (567 px) et `ev-exos` (638 px).
  - Ce débordement existait déjà : les panneaux d'origine du dépôt, passés au même outil, donnent les mêmes largeurs et les mêmes formules.
  - Il vient de longues formules en ligne de corrigés, collées à leur ponctuation (`SPAN.mj-colle`). Aucune n'a été introduite par ce lot.
  - Il reste à traiter dans un lot de mise en forme : passer ces formules en `$$`.
