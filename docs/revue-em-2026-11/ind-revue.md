# Revue `induction` (prefix `ind`) — Induction électromagnétique (PTSI, 1ʳᵉ année)

Fichiers produits (dans `EM/`) : `ind-cours.src.html`, `ind-meth.src.html`, `ind-exos.src.html`,
`ind-cartes-corr.json` (3 cartes), `ind-cartes-ajout.js` (14 cartes), ce compte rendu.
Sources et scripts : gabarit relu `ind-cours.v2.tpl.html` (copie du brouillon `ind-cours.tpl.html`, laissé intact,
corrigée par `_edit_ind_cours.py`), figures `figs_ind.py` → `figs_ind.json` (copies d'origine : `figs_ind.orig.*`),
assemblage `construire_ind.py` (le brouillon utilisait des marques `<!--FIG:nom-->` que `construire.py`, qui attend
`@@FIG:nom@@`, ne remplaçait pas), vérifications numériques et symboliques de tous les exemples, méthodes et
exercices : `verif_ind.py` (sympy, numpy). Le panneau `ind-flash` n'est pas touché.

Contrôles (lancés un par un) : `verif_src.py` sur les trois fichiers, sans ERREUR ni « attention » ; `apercu_src.py`
à 390 et 1440 px pour le cours, les méthodes et les exercices : `merr`, `brut`, `larges` vides, aucune erreur JS,
`scrollW` égal à la largeur ; figures regardées en capture (1440 px) ; `corriger_cartes.py --essai` : 3 réponses
corrigées ; `ajouter_cartes.py --essai` : 25 → 39 cartes.

## Cours : 4 sections courtes → 11 sections §n + bloc « AU PROGRAMME · PTSI » + « POUR ALLER PLUS LOIN »
Point de départ : le brouillon d'une session précédente (11 sections, 8 figures), relu d'un œil critique, puis
corrigé et complété. Tous les exemples ont été recalculés (`verif_ind.py`, partie COURS). Sections :
§1 flux (orientation, main droite, N spires) · §2 loi de Faraday (expériences, convention générateur, schéma électrique
équivalent) · §3 loi de Lenz · §4 auto-induction (flux propre/extérieur, L d'une bobine longue, continuité, bilan
d'énergie, mesure de L) · §5 inductance mutuelle (bobines longues coaxiales en influence totale, applications) ·
§6 circuits couplés en régime sinusoïdal forcé (système, impédance d'entrée, bilan, |M| ≤ √(L₁L₂)) · §7 transformateur
(loi des tensions démontrée, bilan, très haute tension) · §8 rails de Laplace (équations électrique et mécanique avec
conventions, P_L + e i = 0, générateur et moteur) · §9 spire en rotation (alternateur, couple résistant) · §10 courants
de Foucault (origine, mise en évidence, freinage, chauffage, tôles feuilletées) · §11 moteur à courant continu à
entrefer plan (+ haut-parleur). 14 exemples traités chiffrés (au moins un par section), 8 figures calculées
(2 à 5 Ko chacune), erreurs classiques, ordres de grandeur, liens vers `emag` et `maxwell`.

### Erreurs de l'ancien panneau du site (corrigées par la réécriture)
1. §4 : « Un transformateur abaisseur a m  1 » (le « < » avait disparu : phrase vide de sens).
2. §5 : rails traités avec une normale opposée à B sans figure qui le montre ; f.é.m. « de Lorentz » e = Blv sans
   convention, alors que le programme exige les conventions d'algébrisation (audit 2026-11, point 12) et exclut
   le champ électromoteur.
3. Absences (audit, lignes 37-38 et 67) : inductance mutuelle de bobines coaxiales, circuits couplés, bilan du
   transformateur, spire tournante, courants de Foucault, moteur à courant continu, expériences, mesure de L.

### Erreurs ou faiblesses du brouillon (corrigées)
1. **Figures** : les vecteurs étaient notés avec la flèche combinante U+20D7, absente de la police des figures du site
   (rendue par un carré « n⊠ », vu en capture) → lettres en gras italique, comme les figures de 2ᵉ année.
2. **Figure des rails** : courbe étiquetée x/(v₀τ) alors qu'elle part de 0 → (x − x₀)/(v₀τ), légende précisée.
3. **§10, pertes par courants de Foucault dans un disque** : l'hypothèse « champ des courants induits négligeable »
   n'était pas satisfaite (≈ 18 % de B₀ au centre pour h = 1 mm) → disque de 0,5 mm (≈ 9 %), P ≈ 0,9 W au lieu de
   1,8 W, et contrôle de l'hypothèse écrit dans l'exemple.
4. **§7** : « on retrouve ce résultat [conservation de la puissance] comme limite de deux circuits couplés en influence
   totale » : seule la loi des tensions découle de M² = L₁L₂ sans résistance (u₂ = (M/L₁)u₁) ; la relation des courants
   demande en plus L₁ très grande. Reformulé.
5. **§11** : « en SI, on la note k » → « en sciences industrielles, on la note K » (`E = KΩ`, `C_m = K i` dans les
   chapitres de SI du site ; « SI » était ambigu avec le Système international).
6. §3 sans exemple chiffré → ajout « quel courant dans l'anneau ? » (R = 2,1 mΩ, e = −0,57 mV, i = −0,27 A, champ
   induit 8 µT : la loi de Lenz donne le sens, pas l'importance ; flux propre négligeable, τ = L/R ≈ 40 µs).
7. §1 : erreur classique et ordres de grandeur mélangés dans un même encadré → séparés, IRM ajoutée, flux à travers
   10 cm² (Terre 5·10⁻⁸ Wb, aimant 5·10⁻⁴ Wb).
8. §4 : « L ne dépend que de la géométrie » → précisé (sans matériau magnétique) ; surtension de rupture chiffrée
   (0,30 A coupés en 10 µs dans 0,20 H : ≈ 6 kV).
9. Énergie magnétique notée `\mathcal E_m` → `U_m`, notation du chapitre `maxwell` (2ᵉ année).
10. Quatre formules en ligne trop longues pour le téléphone passées en bloc ; quatre `data-nom` renommés (mot coupé
    dans la marge à 1440 px : « Alternateu r ») ; figure du moteur : axe en tirets qui barrait les libellés.

Vérifié et conservé (exact) : orientation et sens de toutes les figures (main droite, ⊙, sens des flèches de i, F,
dF⃗ = iB dr e⃗_θ, ω), f.é.m. et couple de la spire tournante (sympy : Γω + ei = 0), rails (F⃗ = iℓB e⃗_x,
P_L + ei = 0), recharge sans fil (Z_e = 0,89 + 10,8 j Ω, P₂ = 0,29 W), M² = L₁L₂, transformateur 230 V → 12 V,
très haute tension (0,13 % contre 50 % de pertes), moteur (Φ₀ = 6,0·10⁻⁴ Wb par tige, 333 rad·s⁻¹, 83 %).

### Couverture du programme (PTSI 1.7.3 à 1.7.5) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Flux d'un champ uniforme, contour orienté plan | §1 ✅ | §1, méthode 1, exo 01, carte |
| Expériences illustrant les lois de Faraday et de Lenz | ❌ | §2 (trois expériences), exo 02 |
| Loi de Lenz : prédire, interpréter | §2 🔶 | §3 (+ exemple chiffré), méthode 3, exo 02, exo 10 |
| Loi de Faraday avec conventions d'algébrisation | 🔶 | §2 (schéma équivalent), méthode 2, tous les exercices |
| Flux propre / flux extérieurs | 🔶 | §4, méthode 4 |
| Ordre de grandeur de L d'une bobine longue | ✅ | §4, méthode 5, carte |
| Mesurer une inductance | ❌ | §4, exo 03 Q5, carte |
| Bilan de puissance et d'énergie (auto-induction) | 🔶 (faux dans l'exo 02) | §4, exo 03 |
| M de deux bobines longues de même axe en influence totale | ❌ | §5, méthode 5, exo 04, carte |
| Applications du couplage par mutuelle | ❌ | §5 |
| Circuits couplés en RSF : système d'équations | ❌ | §6, méthode 6, exo 06, carte |
| Transformateur : loi des tensions, bilan | 🔶 (énoncée) | §7 (démonstration dépliable), méthode 7, exo 05 |
| Rails : équations électrique et mécanique, conventions, bilan | 🔶 | §8, méthodes 8 et 9, exos 07, 08 |
| Spire rectangulaire en rotation uniforme | ❌ (exercice seul) | §9, méthode 10, exo 09, carte |
| Freinage par induction, courants de Foucault | ❌ | §10, exo 10, 2 cartes |
| Moteur à courant continu à entrefer plan | ❌ | §11, méthode 10, exo 11, carte |
| Citer des applications | partiel | dans chaque section |

Hors programme regroupé en fin de cours : champ électromoteur, Maxwell-Faraday, formule de Neumann, densité
d'énergie B²/(2μ₀). Rien de hors programme n'est présenté comme exigible.

## Méthodes : 1 algorithme + 3 méthodes + pièges → 10 méthodes (étapes, exemple éclair chiffré, piège)
1 orienter et calculer un flux (bobine plate, 1,1·10⁻² Wb) · 2 loi de Faraday et schéma équivalent (+20 mV, +0,20 A)
· 3 loi de Lenz et contrôle de signe (aimant qui traverse une bobine : −0,20 V puis +0,33 V, aires égales) ·
4 flux propre / extérieur, continuité (tension de bobine +2 V → −8 V) · 5 L et M de bobines longues (0,25 mH, 7,5 µH)
· 6 circuits couplés en RSF (|I₂/I₁| = 0,27, impédance ramenée 0,71 − 0,44 j Ω) · 7 transformateur idéal
(adaptateur 230 V → 5 V, 5,3 kΩ ramenés) · 8 circuit mobile (τ = 1,6 s) · 9 bilan électromécanique (8,0 m·s⁻¹,
0,80 W) · 10 machine tournante et moteur à courant continu (300 / 200 rad·s⁻¹).
Erreurs de l'ancien panneau corrigées : « la force de Laplace est TOUJOURS opposée au mouvement » (faux en moteur :
rails alimentés, moteur à courant continu) ; signes contradictoires entre méthode 1 (e = −Blv) et méthode 3 (e = Blv).

## Exercices : 7 → 12 (11 numérotés + Concours PT), solutions raisonnées, valeurs recalculées
| n° | Titre | Niveau | Origine |
|---|---|---|---|
| 01 | Flux et f.é.m. : spire dans un champ sinusoïdal | ★☆☆ | ancien 01 (orientation, Lenz, inclinaison) |
| 02 | **Prévoir le sens du courant induit : trois expériences** | ★☆☆ | nouveau |
| 03 | Établissement du courant dans une bobine : énergie et mesure de L | ★★☆ | ancien 02, **Q3 refaite** |
| 04 | **Deux bobines longues de même axe** (M, créneau, série ±, sonde inclinée) | ★★☆ | nouveau |
| 05 | Transformateur d'alimentation (+ démonstration, R/m², rendement) | ★★☆ | ancien 05 |
| 06 | **Recharge sans fil : circuits couplés et accordés** (η = 96 %, puis 61 %) | ★★★ | nouveau |
| 07 | Rails de Laplace : freinage d'une tige lancée | ★★☆ | ancien 03 + ancien « concours » (doublon) |
| 08 | Rails verticaux : vitesse limite et bilan de puissance | ★★☆ | ancien 06 |
| 09 | Alternateur : f.é.m., puissance et couple résistant | ★★☆ | ancien 04 (+ couple) |
| 10 | **Courants de Foucault : aimant dans un tube de cuivre** | ★★☆ | nouveau |
| 11 | **Moteur à courant continu à entrefer plan** (démarrage, charge, caractéristique, récupération) | ★★★ | nouveau |
| CPT | **Le haut-parleur électrodynamique** (force, f.c.é.m., équations couplées, bilan, impédance motionnelle, microphone) | ★★★ | nouveau |

- **Ancien 02, Q3 (faux)** : « W_E = ∫₀^∞ E i dt = E·(E/R)·τ » (intégrale divergente, i → E/R) et « l'énergie se
  répartit à parts égales entre l'inductance et la résistance (résultat général) » : c'est le résultat du condensateur.
  Refait sur [0, 5τ] : W_E ≈ 2,9 mJ, U_m ≈ 0,36 mJ, W_R ≈ 2,5 mJ (identité W_E − W_R = ½Li² vérifiée avec sympy).
- **Ancien « Concours PT »** : même situation que l'ancien 03 (rails horizontaux, tige lancée) ; son apport (sens par
  Lenz, P_L + ei = 0) est fondu dans l'exo 07, et un vrai problème en quatre parties le remplace.
- Anciens 01, 03, 04, 06 : f.é.m. « en valeur absolue » → orientation, normale, signes et contrôle par la loi de Lenz.
- Exo 08 : la vitesse limite (19 m·s⁻¹) suppose environ 150 m de rails : signalé dans la solution.

## Cartes : 25 → 39
Corrigées (`ind-cartes-corr.json`, question inchangée) : n° 15 (« e = Blv » sans convention → valeur absolue,
signe selon l'orientation, e = −Bℓv pour Φ = Bℓx), n° 16 (« règle de la main gauche » → F⃗ = i ℓ⃗ ∧ B⃗, ℓ⃗ dans le
sens du courant), n° 19 (Φ = BS cos ωt pour N spires, incohérent avec e = NBSω sin ωt → Φ = NBS cos ωt).
Ajoutées (14) : orienter la normale ; schéma équivalent ; mesurer L ; ordre de grandeur de L (`val`) ; M de bobines
coaxiales (`form`) ; équations couplées en RSF (`form`) ; énergie de deux circuits couplés (`form`) ; très haute
tension ; P_L + ei = 0 (`form`) ; vitesse limite des rails en moteur ; f.é.m. maximale de la spire tournante ;
équations du moteur à courant continu (`form`) ; origine des courants de Foucault ; utilisations et inconvénient.
La carte n° 21 (bilan RL) avait déjà été corrigée sur le site (audit, point 7) : conservée.

## Notations choisies (alignées sur `mgs`, `mxw` et le nouveau `emag`)
Orientation → \(\vec n\) par la main droite ; \(\Phi\) (Wb), \(e=-\mathrm d\Phi/\mathrm dt\) en convention générateur,
schéma équivalent \(e = Ri\) ; \(i\) minuscule pour les courants variables ; \(L\), \(M\) (algébrique),
\(U_m = \tfrac12Li^2\) (comme `mxw`) ; \(\vec F = i\,\vec\ell\wedge\vec B\), \(\vec\ell\) orienté comme le circuit ;
\(P_L + e\,i = 0\) ; \(\vec{\mathcal M} = NiS\,\vec n\), \(\vec\Gamma = \vec{\mathcal M}\wedge\vec B\) ; moteur :
\(\Phi_0\) (\(E = \Phi_0\omega\), \(\Gamma = \Phi_0 i\)), avec renvoi à la notation \(K\) des sciences industrielles ;
complexes soulignés \(\underline I\).

## Doutes et points à signaler
- Divergence de notation : le chapitre d'électrocinétique de 1ʳᵉ année du site note l'énergie d'une bobine
  \(\mathcal E_L\) ; ce chapitre suit `maxwell` (\(U_m\)).
- §10 : le calcul des pertes dans un disque dépasse le « qualitatif » du programme, mais n'utilise que la loi de Faraday
  et l'effet Joule ; présenté comme un ordre de grandeur, avec son hypothèse contrôlée.
- Haut-parleur (§11 et Concours) : la f.é.m. y est obtenue par \(P_L + e\,i = 0\) (admis), seul chemin compatible avec
  l'exclusion du champ électromoteur ; le cours `emag` (autre rédacteur) cite aussi le haut-parleur et renvoie ici.
- Cours long (≈ 84 000 caractères HTML dont ≈ 49 000 de texte) : 11 sections, toutes demandées par le programme.
- Pas de renommage du chapitre proposé (« Induction électromagnétique » convient).
