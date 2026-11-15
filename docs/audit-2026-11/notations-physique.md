# Physique-chimie de 1ʳᵉ année : harmonisation des notations (point 3 de l'audit, 15/11/2026)

Source : `docs/audit-2026-11/physique-1a.md` §4 « Notations incohérentes entre chapitres ». Programme : `pdf-pt/prog/ptsi.txt`
(et `phys.txt`). Panneaux extraits du dépôt actuel (corrections des points 1-2 comprises). Aucune carte ajoutée, retirée ni
déplacée : seules des réponses et, quand la notation y figure, des questions (`q_nouvelle`) sont retouchées, ordre et
nombre inchangés (repli par rang : progression conservée). Numéros de cartes à partir de 0 (comme `cartes.py`).
Cartes en Unicode laissées en Unicode, sauf `eq` n° 0 dont la réponse est écrite en `\( … \)` (voir §4).

Fichiers produits dans `revue3/` (22 panneaux, 10 fichiers de cartes) :
`eme-cours`, `ce-cours`, `ce-meth`, `ce-exos`, `th3-cours`, `th3-meth`, `th3-exos`, `mth-exos`, `eq-cours`, `eq-meth`,
`eq-exos`, `acb-cours`, `acb-exos`, `pre-cours`, `pre-meth`, `pre-exos`, `eph-exos`, `mcin-cours`, `mcin-meth`,
`mcin-exos`, `msol-cours`, `cc-cours` (`.src.html`) ; `eme`, `ce`, `th3`, `mth`, `eq`, `acb`, `pre`, `oxr`, `msol`
(`-cartes-corr.json`). Copies des panneaux d'origine : `revue3/_physique_orig/` (référence des contrôles, à ne pas intégrer).

## 1. Oscillateur amorti : ω₀, Q et τ = 2Q/ω₀

**Cible** : forme canonique ẍ + (ω₀/Q)ẋ + ω₀²x = 0 (le programme ne cite que « pulsation propre et facteur de qualité ») ;
τ = 2Q/ω₀ = 2m/α, enveloppe en e^(−t/τ), comme `rlc` (τ = 2Q/ω₀ = 2L/R) et `oscill` (τ = 2Q/ω₀ = 2m/α).
Vérifié : Q = mω₀/α donc 2Q/ω₀ = 2m/α ; amplitude en e^(−αt/2m) = e^(−t/τ) ; E_m ∝ amplitude² ∝ e^(−2t/τ).

| Panneau | Modifications |
|---|---|
| `eme-cours` §4 | 5 : « amortissement ξ = 1/(2Q) » et les trois ξ des régimes retirés (régimes donnés par Q seul) ; « e^(−t/(2τ)) avec τ = m/α, E_m ∼ e^(−t/τ) » → « e^(−t/τ) avec τ = 2Q/ω₀ = 2m/α (même τ que RLC et oscillateur mécanique), E_m ∼ e^(−2t/τ) » |
| cartes `eme` | n° 19 (« (ξ<1) » retiré), n° 25 (τ = 2Q/ω₀ = 2m/α, enveloppe exp(−t/τ), E_m ∝ exp(−2t/τ)) |

Laissé : `energie` exos (λ = ω₀/(2Q) « taux d'amortissement » = 1/τ, cohérent) ; `mecpt` (τ = m/α y est la constante
de temps d'une chute avec frottement linéaire, 1ᵉʳ ordre : autre grandeur, juste). ξ ne désigne plus l'amortissement dans
aucun chapitre de physique-chimie de 1ʳᵉ année (il reste en SI, `sys2`, `slci`…, hors de ma liste).

## 2. Enthalpie de changement d'état : Δh₁₂

**Cible** : programme PTSI « Δh₁₂(T) = T Δs₁₂(T) », enthalpie de fusion / vaporisation / sublimation → Δh₁₂ = h₂ − h₁
(générique), Δh_fus, Δh_vap pour les transitions nommées ; la mention « (anciennement chaleur latente L) » gardée une fois
dans le cours (§2) et dans la carte de définition (n° 2, où l'élève la cherche). Seul `changement` employait L :
`thermo1`, `thermo2`, `thermo3`, `machines` n'ont aucune chaleur latente (vérifié).

| Panneau | Modifications |
|---|---|
| `ce-cours` | 13 lignes : encadré de tête (« chaleurs latentes » → Δh₁₂), titre h2 et h3 du §2, intro, définition (Q = ΔH = m Δh₁₂, Δh₁₂ = h₂ − h₁), liste fusion/vaporisation/eau, Clausius-Clapeyron (hors programme) et §4 (Q_total = mcΔT₁ + m Δh₁₂ + mc′ΔT₂) |
| `ce-meth` | 4 (méthode 1 Q = m Δh₁₂ ; méthode 3 ; piège Δh_vap ≫ Δh_fus) |
| `ce-exos` | 17 occurrences dans 6 exercices (énoncés et corrigés) ; titre de l'exo 1 « Enthalpie de fusion — fonte de glace » |
| cartes `ce` | n° 2 (q + r), 3 (q + r), 5, 13 (q), 19, 21, 23 (aussi « mCΔT » → m·c·ΔT), 24 |

**Erreur corrigée en passant** : Clausius-Clapeyron (cours §2, méthode 3, exo 2, cartes 5 et 19) mélangeait une enthalpie
massique et des volumes massiques avec R (formule ≈ L_v P/(RT²), donnant en fait des J/mol dans l'exo 2). Écrit
désormais avec Δh_vap massique : dP/dT = Δh_vap/(T(v_g − v_l)) ≈ M Δh_vap P/(RT²), pente −M Δh_vap/R ; l'exo 2 calcule
« l'enthalpie molaire de vaporisation M Δh_vap » (42,3 kJ/mol, puis Δh_vap ≈ 2 350 J/g). Exo 5 Q2 : l'égalité absurde
« x × 334 = (1 − x × 0 + 1) × 4,18 × 10 » remplacée par x Δh_fus = c ΔT (la suite, x ≈ 12,5 %, inchangée).

Laissé : exo 6 garde ΔH_vap pour l'enthalpie molaire (notation de l'énoncé, distincte de Δh_vap massique) ; carte 1
« L/G » et carte 8 « L-V » (L = liquide). **2ᵉ année du site non uniforme** (hors de ma liste, signalé) : `thermodiff`
écrit Δ_{1→2}h (« ou chaleur latente L »), les exercices de `thermoouv` ℓ_v ; à aligner un jour sur Δh₁₂ ou Δ_{1→2}h.

## 3. Entropie échangée et créée : S_éch et S_créée

**Cible** : S_éch et S_créée. Le programme écrit littéralement « ΔS = Sech + Scréé avec Sech = ΣQi/Ti » (sans accent ni
accord) ; la 2ᵉ année du site écrit s_éch, S_créée, Ṡ_créée, et `thermo3` exo « Concours » avait déjà S_créée : j'ai pris
la forme accordée (S_créée), écart purement typographique avec le programme. Dans les formules : `S_{\text{éch}}`,
`S_{\text{créée}}` ; dans le texte hors formule du chapitre (style existant, indice posé par `typographier`) : S_éch,
S_créée, S_{éch,1}, S_{créée,2}.

| Panneau | Modifications |
|---|---|
| `th3-cours` | 26 lignes (S_e, S_c, Se, Sc, δS_e, δS_c ; 2 titres h3), accord « S_créée nulle » |
| `th3-meth` | 14 lignes ; « d'autant plus grande » |
| `th3-exos` | 17 lignes (dont S_{éch,1}, S_{créée,2}) ; « plus S_créée serait petite » |
| `mth-exos` | 4 : ΔS_cr, Ṡ_cr, S_cr ×2 → S_créée, Ṡ_créée (ΔS_univ laissé : c'est bien la variation d'entropie de l'univers) |
| cartes `th3` | 13 : n° 0, 1 (q), 3 (q), 4 (q), 5 (q), 6, 7, 8, 21, 22, 23 (q), 24 (q), 25 |
| carte `mth` | n° 13 (ΔS_cr → S_créée) |

`changement` n'emploie que ΔS_vap (rien à changer).

## 4. Constantes d'équilibre : K° sans dimension, activités a = c/c°

**Cible** (programme : « constante thermodynamique d'équilibre », activités « avec référence à l'état standard ») : K°
partout où la constante était notée K ou K_c en contexte exigible ; K_a, K_s, K_e définies avec c° ; dans les calculs
numériques, un rappel « concentrations en mol/L divisées par c° = 1 mol/L ». K_c et K_p restent dans le seul bloc et
l'exercice 5 déjà signalés hors programme (`equilchim` §1, exo « Kp et Kc »).

| Panneau | Modifications |
|---|---|
| `eq-cours` | 12 lignes : formule de K° en solution diluée écrite avec ([X]/c°) au lieu de K_c dimensionnée + rappel ; K → K° (Van 't Hoff, ΔrG° = −RT ln K°, K° ≫ 1…) ; « Ka/Kb » → K_a ; ICE « substituer dans K° » |
| `eq-meth` | 10 : K_c → K° (concentrations / c°), K → K° partout |
| `eq-exos` | exo 1 K_c = 50 → K° = 50 (Δn_gaz = 0 : rapport de concentrations) ; exos 2-3 (2ᵉ année) K → K° ; exo 4 K_a = x²/((c − x)c°), x = √(K_a c c°), pH = −log([H⁺]/c°) ; exo 6 K → K°, s = c°√K°, s₀ = c°√K_s |
| `acb-cours` | K_e = [H₃O⁺][OH⁻]/(c°)², pH = −log([H₃O⁺]/c°), K_a = [A⁻][H₃O⁺]/([AH] c°) ; formules de pH (hors programme) en log(C/c°) |
| `acb-exos` | 2 formules en log(C/c°) |
| `pre-cours` | K_s = [Ag⁺][Cl⁻]/(c°)², définition par les activités + rappel (même valeur numérique en mol/L) ; s = c°√K_s, s = c°(K_s/4)^{1/3} |
| `pre-meth` | 1 ; `pre-exos` : 4 (Q avec (c°)³, expression de K_s, s = c°√K_s ×2) ; les autres calculs reposent sur le rappel du cours |
| `eph-exos` | 1 : K_s(Fe(OH)₂) = [Fe²⁺][OH⁻]²/(c°)³ |
| cartes `eq` | 19 : n° 0 (q + r : K° avec activités, au lieu de K_c dimensionnée — la contradiction avec n° 28 « K° sans unité » disparaît ; réponse en `\( … \)`, une fraction en Unicode étant mal découpée par `flashPretty`), 1, 7, 8, 12, 13, 14, 15 (q : K → K°), 5, 6, 9, 10, 11, 16, 19, 20, 22 (K_a avec c°), 23, 24 |
| cartes `acb` | 6 : n° 1, 2, 3, 7, 8, 9 ; cartes `pre` : 3 (n° 0, 2, 3) ; carte `oxr` n° 7 ([H⁺]^h → a_(H⁺)^h dans Nernst, écrit avec des activités) |

`oxred` était déjà cohérent (activités, c°, K°) : rien changé dans ses panneaux. **Bogue d'affichage corrigé** : la carte
`eq` n° 6 (Van 't Hoff) s'affichait « ln[K·(T₂/K)(T₁)] » (fraction mal découpée) ; écrite « ln K°(T₂) − ln K°(T₁) = … ».
Même chose pour `pre` n° 2 (« √K s ») : √(Ks).

## 5. Moments : 𝓜

**Cible** : le programme ne fixe aucune notation ; celle de `mvtsolide` : 𝓜_Δ (axe), et donc \vec{𝓜}_O (point), 𝓜 pour
le moment d'un couple.

| Panneau | Modifications |
|---|---|
| `mcin-cours` | \vec{M}_O ×3 → \vec{\mathcal{M}}_O, M_Δ → \mathcal{M}_Δ ; §4 (gyroscope, hors programme) : couple \vec{C} → couple de moment \vec{\mathcal{M}}, Ω_p = 𝓜/L (le C du couple disparaît) |
| `mcin-meth` | 3 ; `mcin-exos` : 3 (𝓜_O, \vec{𝓜}_O, 𝓜_O(\vec{P})) |
| `cc-cours` | 1 (renvoi direct : \vec{M}_O = \vec{0} → \vec{\mathcal{M}}_O) |

**Tableaux de moments d'inertie** : valeurs recalculées (sympy) — anneau / cylindre creux mince mR², disque / cylindre
plein ½mR², sphère pleine ⅖mR², tige au milieu (1/12)mL², tige à une extrémité ⅓mL² : toutes justes dans les deux
chapitres, mais listes et notations différentes (m / M, 5 / 4 cas). Un même encadré (5 cas, masse m) remplace les deux
(`mcin-cours`, et le paragraphe « Quelques valeurs utiles » de `msol-cours`). Carte `msol` n° 9 alignée (m, 5 cas).
Cartes `mcin` (M_O, M_Δ) et `msol` (M_Δ, M) laissées : en Unicode, la lettre M tient lieu de 𝓜 dans les deux decks, déjà
cohérents (𝓜 Unicode n'est employé nulle part et risquerait de manquer dans les polices).

## 6. C dans `chcentral` (facultatif) : rien changé

Dans `chcentral`, C ne désigne que la constante des aires (cours, méthodes, exercices, cartes) : ni couple ni capacité
dans le même chapitre, donc pas de confusion. Le couple noté \vec{C} était dans `mcinc` §4 : réglé au §5.

## Contrôles

- `verif_src.py` : aucune ERREUR. Restent des « attention » déjà présentes dans l'original (« pas de bloc AU PROGRAMME · PT »,
  formules en ligne longues inchangées) ; les formules en ligne que j'avais allongées (c°, 𝓜, S_créée, M Δh_vap) ont été
  coupées aux signes = en plusieurs `\( … \)` successives (rendu identique, coupure de ligne possible).
- `apercu_src.py` 390 et 1440 sur les 22 panneaux : merr et brut vides, aucune erreur JS ; à 1440, larges vide partout.
  À 390, les cours et méthodes sont nets ; sept onglets Exercices gardent un débordement **déjà présent dans l'original**,
  dû uniquement à des formules en ligne que je n'ai pas touchées (liste `larges` relue) : `ce-exos` 736 → 681 px,
  `eq-exos` 588 → 588, `eph-exos` 586 → 586, `mth-exos` 686 → 667, `pre-exos` 489 → 489, `th3-exos` 572 → 572,
  `mcin-exos` 689 (calculs d'orbite et de pendule inchangés) ; `acb-exos` passe de 527 à 390 px (plus de débordement).
- `corriger_cartes.py … --essai` : OK pour les 10 fichiers ; rendu `flashPretty` des cartes retouchées relu (même découpage
  qu'avant, deux bogues corrigés ci-dessus).
- `diff` panneau du dépôt ↔ fichier : seules les modifications listées (plus le saut de ligne final).

## Signalé, non modifié (hors de ma liste)

- `emag` : couple noté \vec{C} = \vec{m} ∧ \vec{B} dans le cours, \vec{Γ} dans les exercices.
- Carte `eq` n° 24 : « étapes élémentaires » (vocabulaire de cinétique) pour une combinaison linéaire de réactions.
- Carte `th3` n° 22 : « Calculer ΔS par l'identité thermo » alors que les identités sont signalées hors programme.
