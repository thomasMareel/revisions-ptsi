# Revue du chapitre `ondes` (prefix `ond`) — « Ondes mécaniques » — 2026-11-21

Objet (audit 2026-11-14, `docs/audit-2026-11/physique-1a.md` §2 point 5, §4 point 9, §5 point 5) : recentrer le chapitre sur la
partie 1.6 « Propagation d'un signal » du programme de PTSI. Avant : 4 sections dont 3 consacrées à du hors-programme
(d'Alembert en tête, ondes stationnaires, décibels, Doppler), aucune section sur f(t − x/c), les milieux dispersifs ou les
interférences de deux ondes ; 4 méthodes (dont 2 hors programme), 8 exercices (dont 5 hors programme et 2 « Concours PT »).

## Fichiers produits (dans `AN1/`)
- `ond-cours.src.html` (115,7 ko, dont ≈ 75 ko de figures) — assemblé par `ond_construire.py` à partir de `ond-cours.tpl.html`
  et `ond_figs.json` ;
- `ond-meth.src.html` (10 méthodes), `ond-exos.src.html` (12 exercices dont 1 « Concours PT ») ;
- `ond-cartes-corr.json` (3 corrections de réponse), `ond-cartes-ajout.js` (13 cartes) ;
- scripts : `ond_figs.py` (figures), `ond_calculs.py` (exemples du cours), `ond_calculs_exos.py` (exercices anciens et
  nouveaux), `ond_cartes.py` (cartes), `ond_construire.py` (assemblage), `ond_voir.py` (aperçu des figures, sert aussi à `od`).

## Erreurs trouvées et corrigées
| Où | Erreur | Correction |
|---|---|---|
| Cours §1 (ancien) | d'Alembert présenté en tête, et « toute onde se propageant à la célérité c satisfait l'équation de d'Alembert » (faux hors milieu non dispersif, non absorbant, 1D) | d'Alembert déplacé en « Pour aller plus loin », avec son domaine de validité explicite ; le programme exclut toute équation d'onde |
| Cours (ancien) | ondes stationnaires et modes propres présentés comme partie du cours | regroupés en « Pour aller plus loin » (vus en 2ᵉ année sur les OEM ; modes de corde hors des deux programmes) |
| Carte 7 « Deux sources identiques en phase : niveau sonore résultant ? » | réponse « +3 dB » : vrai pour des sources incohérentes, faux pour des sources en phase (cohérentes : +6 dB, interférences) | réponse corrigée (question inchangée) : cohérentes en phase → ×4, +6 dB, ailleurs interférences ; incohérentes → +3 dB |
| Cartes 19 et 20 (conditions constructive / destructive) | « Δφ = 2nπ ⟺ différence de chemin multiple de λ » sans l'hypothèse « sources en phase » (faux pour des haut-parleurs en opposition) | hypothèse ajoutée dans la réponse, cas des sources en opposition indiqué |
| Exercice 6 (ancien, devenu EXO 05) | titre « ondes stationnaires » pour deux ondes de même sens ; valeurs arrondies trop tôt (Δφ = 5,91 rad, intensité 3,84 A²) | titre corrigé ; Δφ = 5,93 rad, A ≈ 1,97 A, intensité 3,88 A² ; remarque sur l'égalité supposée des amplitudes |
| Exercice 3 (ancien, devenu EXO 08) | f₃ = 223,5 Hz | 224 Hz (3 × 74,54) |
| Exercice 4 (ancien, devenu EXO 09) | « environ 2 demi-tons vers le haut puis 2 vers le bas » | environ 1,5 demi-ton de chaque côté, 3 demi-tons au total (12 log₂(482,6/404,3) = 3,06) |
| Concours (sonar) | coefficient d'absorption noté a, comme l'écart entre sources de la nouvelle partie | noté α |
| Concours Melde | présenté comme second « Concours PT » | devenu EXO 11 (hors programme, pour aller plus loin) : un seul « Concours PT » par chapitre |

## Couverture du programme (partie 1.6, ondes mécaniques et acoustiques) : avant → après
| Capacité exigible | Avant | Après |
|---|---|---|
| Grandeurs physiques des signaux acoustiques, électriques, électromagnétiques | absent | §1 (tableau), carte |
| Ordres de grandeur de fréquences (acoustique, mécanique, EM) | célérités seulement | §1 (tableau), carte `val` |
| Écrire f(x − ct), g(x + ct), f(t − x/c), g(t + x/c) ; célérité, retard | f(x − ct) dans d'Alembert seulement | §2, méthode 1, EXO 02, carte |
| Prévoir l'évolution temporelle en un point et le profil à différents instants | absent | §2 (figure calculée, exemple), méthode 2, EXO 02, carte |
| Onde progressive sinusoïdale : vitesse de phase, double périodicité, λ = v_φ/f | formule seule | §3 (figure, démonstration, exemples), méthode 3, EXO 01, cartes |
| Déphasage dû à la propagation, relié au retard | formule seule | §4 (figure oscilloscope + XY), méthode 4, EXO 03, concours A3 |
| Mesurer vitesse de phase, longueur d'onde, déphasage | absent | §4 (protocole, exemple), méthode 5, EXO 03, carte |
| Milieux dispersifs : définition, exemples | un « piège » de méthode (« la célérité ne dépend pas de la fréquence ») | §5 (figure calculée, tableau, 2 exemples), méthode 6, EXO 04, 2 cartes |
| Interférences de deux ondes de même fréquence : conditions constructives / destructives | exercice seulement | §7, méthode 8, EXO 05-06, concours B, cartes |
| Amplitude résultante en fonction du déphasage | exercice seulement | §6 (démonstration, construction de Fresnel), méthode 7, EXO 05, carte |
| Mettre en œuvre un dispositif (cuve à ondes, haut-parleurs, ultrasons) | absent | §8 (figure calculée de cuve à ondes, applications : antibruit, sonorisation, réseaux d'émetteurs), méthode 9, EXO 06, concours B |

## Contenu
**Cours** (bloc « AU PROGRAMME · PTSI » + 8 sections + 2 « Pour aller plus loin ») : §1 Signaux et ondes ; §2 Onde progressive
à une dimension ; §3 Onde progressive sinusoïdale ; §4 Déphasage dû à la propagation (mesures) ; §5 Milieux dispersifs ;
§6 Somme de deux signaux sinusoïdaux ; §7 Interférences de deux ondes ; §8 Figures d'interférences et applications ;
PAPL « Équation d'onde et ondes stationnaires » (d'Alembert, ondes stationnaires, modes de corde, vitesse de groupe) ;
PAPL « Décibels et effet Doppler » (+3 / +6 dB, Doppler, cône de Mach). 12 exemples traités chiffrés, 7 notices « Erreur
classique », 7 figures SVG calculées : impulsion (profil à deux instants et signal en deux points), double périodicité,
oscilloscope et mode XY, impulsion en milieu non dispersif / dispersif (superposition de 900 composantes), construction de
Fresnel et amplitude en fonction de Δφ, cuve à ondes (crêtes et hyperboles calculées), onde stationnaire (PAPL).

**Méthodes** (10) : reconnaître une onde progressive ; passer du signal en un point au profil ; exploiter une onde
sinusoïdale ; retard et déphasage ; mesurer λ et c à l'oscilloscope (avec incertitude) ; reconnaître un milieu dispersif ;
additionner deux sinusoïdes ; nature des interférences en un point ; localiser et compter maxima et minima ; modes propres
(hors programme). Les anciennes méthodes 1 à 3 sont reprises (1 → 3, 2 → 10, dB → notice « Piège (hors programme) »).

**Exercices** (12) : 6 nouveaux ou repris au programme en tête (EXO 01 ancien, EXO 02 impulsion trapézoïdale, EXO 03
célérité du son et température, EXO 04 houle et tsunami, EXO 05 ancien 06 corrigé, EXO 06 zones de silence devant deux
haut-parleurs, avec comparaison approximation / résolution exacte) ; puis les 5 anciens exercices hors programme gardés et
signalés (EXO 07 dB, 08 corde, 09 Doppler, 10 tuyau, 11 Melde) ; « Concours PT » sonar restructuré : A propagation (inchangé),
**B nouvelle partie au programme** (deux transducteurs : directions d'interférences constructives et destructives, pilotage
du faisceau par un retard de 5,2 µs), C atténuation et D Doppler (anciennes B et C, hors programme, signalées).

**Cartes** : 25 → 38 (3 réponses corrigées, 13 ajoutées à la fin : forme f(t − x/c), passage signal → profil, double
périodicité, vitesse de phase, ordres de grandeur de fréquences, mesure de λ, milieu dispersif (définition, exemples),
amplitude de la somme, déphasage en M, conditions de stabilité, lignes d'interférences, antibruit).

## Notations
s(x, t), A, ω, k (« norme du vecteur d'onde, souvent appelée nombre d'onde »), v_φ = ω/k, λ, T, f ; retard de phase
φ_j(M) = φ_{S_j} + 2π r_j/λ et s_j = A_j cos(ωt − φ_j), différence de marche δ = S₂M − S₁M, Δφ = φ₂ − φ₁ = 2πδ/λ + (φ_{S₂} − φ_{S₁}),
p ordre, i = λD/a : mêmes conventions que les chapitres de 2ᵉ année `interf` / `dispinterf` (retard de phase, δ = (S₂M) − (S₁M))
et que le chapitre `optiqued` réécrit en même temps. Les anciens exercices gardent leurs notations (Δr dans l'EXO 05).

## Doutes et remarques pour l'intégration
- **Renommage suggéré** : le chapitre couvre désormais toute la partie 1.6 côté ondes mécaniques ; « Propagation d'un signal et
  interférences » (mobLabel « Propagation & interférences ») décrirait mieux son contenu que « Ondes mécaniques ». Le cours
  d'`optiqued` renvoie au chapitre sous son nom actuel « Ondes mécaniques » (4 occurrences ; `ond-cours` renvoie 2 fois à « Optique ondulatoire ») : à mettre à jour si l'on renomme.
- Le simulateur (onglet « Simulateur », non modifié) montre aussi l'onde stationnaire (hors programme) ; le cours y renvoie
  seulement pour l'onde progressive.
- Le §8 renvoie au calcul δ ≈ ax/D fait dans `optiqued` (§5) plutôt que de le refaire.
- Exemple de la houle : la vitesse de groupe (hors programme) gouverne les temps d'arrivée ; le cours ne fait que l'ordre
  d'arrivée et le signale explicitement, pour ne pas affirmer un temps d'arrivée faux.
- Les cartes hors programme gardent leur préfixe d'origine « Hors programme (pour aller plus loin) : » (non modifiées).
