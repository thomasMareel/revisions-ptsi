# Revue — `maxwell` (prefix `mxw`), « Équations de Maxwell et ARQS » (2ᵉ année, programme PT 4.3 et 4.4)

Fichiers produits (dans `EM/`) : `mxw-cours.src.html`, `mxw-meth.src.html`, `mxw-exos.src.html`,
`mxw-cartes-corr.json` (5 corrections), `mxw-cartes-ajout.js` (10 cartes). Fichiers de travail :
`mxw-exos-nouveaux.html` (exercices ajoutés avant assemblage), `oem3_rep.py`, `oem3_exos.py`,
`oem3_verif_sympy.py` (communs aux trois chapitres), `orig/` (panneaux et cartes d'origine).

Contrôles : `verif_src.py` sans erreur ni « attention » sur les trois panneaux ; `apercu_src.py` à 390 et
1440 px : `merr`, `brut`, `larges` vides, aucune erreur JS ; `corriger_cartes.py --essai` (5 réponses) et
`ajouter_cartes.py --essai` (39 → 49) sans erreur.

## 1. Relecture du cours : ce qui a été corrigé

Tous les calculs et ordres de grandeur du cours ont été refaits (Python) : **aucune erreur numérique ni de
signe** (Poynting du fil, solénoïde, condensateur, relations de passage, table de l'ARQS, τ de Drude,
ε₀/σ, rapport j_D/j…). Les corrections portent sur la conformité au programme et la pédagogie :

| Où | Problème | Correction |
|---|---|---|
| §6 | La loi d'Ohm **exigible** n'était présentée que comme conséquence du modèle de Drude (hors programme), sous la forme `j = σ₀E`, `σ₀ = ne²τ/m`, dans un §« Loi d'Ohm locale et modèle de Drude ». | Sous-section « Loi d'Ohm locale et effet Joule » (exigible, notation `σ`, `R = ℓ/(σS)`, ordres de grandeur, domaine de validité, application chiffrée), puis sous-section « Modèle de Drude (hors programme, pour aller plus loin) » qui garde σ₀ (conductivité statique) et la conductivité complexe. |
| §6, §8 | Neutralité (`ε₀/σ₀`) et rapport `ε₀ω/σ₀` écrits avec la notation de Drude. | `σ` (notation du programme et des chapitres voisins). |
| Bloc « Au programme » | Hors-programme mal délimité ; capacité « div j = 0 en ARQS » et §10 non cités. | Liste mise à jour, hors-programme nommé (Drude, conductivité complexe, ARQS électrique) et renvoyé aux §. |
| §5 | Équation de Poisson donnée sans démonstration ni exemple. | Démonstration en une ligne (rot E = 0 → E = −grad V → MG), formule nommée (`data-nom`), **exemple chiffré** : potentiel dans un faisceau d'électrons (Poisson en cylindriques, contrôle par Gauss, ΔV ≈ 0,9 V). |
| §7 | Exemple du fil sans valeurs ; interprétation des termes du bilan non explicitée (capacité « interpréter chaque terme »). | Valeurs (Π ≈ 84 W·m⁻², RI² = 0,53 W) ; encadré « Lire le bilan terme à terme » et orientation d'une surface pour une puissance rayonnée. |
| §9 | La simplification de la conservation de la charge en ARQS (capacité du programme) n'était qu'implicite (§8). | Encadré : divergence de `rot B = μ₀j` ⇒ `div j = 0`, interprétation. |
| §10 | Pas d'exemple chiffré. | Exemple « d'où vient l'énergie du condensateur » : Π radial entrant, flux = u·i (0,10 W). |
| §1, §4, §7 | Cinq formules en ligne trop longues pour le téléphone. | Passées en bloc ou coupées. |

## 2. Couverture du programme (4.3, 4.4) avant → après

| Capacité exigible | Avant | Après |
|---|---|---|
| Conservation de la charge à 1 D (établir), forme générale | cours §2, carte | + méthode 2, exercice 2 |
| Déduire la conservation de la charge des équations de Maxwell | cours §3, carte | inchangé (déjà complet) |
| Associer MF à la loi de Faraday | cours §9, exercice 3 (bétatron) | + méthode 3 |
| Citer, utiliser, interpréter les équations sous forme intégrale | cours §3, méthodes 1-2, exercices | + cartes (Gauss, flux), exercices 4, 9 |
| Relier le couplage E/B à la propagation | cours §3-§4 | + méthode 5 (piège du courant de déplacement) |
| Établir les équations de propagation | cours §4 | + méthode 5 |
| ARQS magnétique : simplifier Maxwell et la conservation de la charge | cours §8-§9, méthode 5 | + encadré §9, méthode 9, carte |
| Lois locales des champs statiques, Poisson, Laplace | cours §5 (sans démonstration ni exemple) | + démonstration, exemple, méthode 6, exercices 5 et 8, 3 cartes |
| Puissance volumique cédée aux porteurs | cours §6, carte | inchangé |
| Milieu ohmique : aspects énergétiques | cours §6-§7 (via Drude) | loi d'Ohm exigible séparée, exercices 1, 11, concours C |
| Flux du vecteur de Poynting, puissance rayonnée | cours §7, concours | + notice d'orientation, méthode 8, exercice 9 |
| Bilan d'énergie local et intégral ; interpréter chaque terme | cours §7, méthode 4 | + notice terme à terme, méthode 7, exercice 9, carte |
| Relations de passage (fournies) : les exploiter | cours §5, méthode 7 | + méthode 10 chiffrée, exercice 4 |

## 3. Méthodes (7 → 10, toutes avec exemple éclair chiffré)

1 local ↔ intégral · 2 bilan de conservation à 1 D · 3 champ en régime variable (Faraday, Ampère généralisé) ·
4 Maxwell-flux près d'un axe · 5 équation de propagation ou de diffusion · 6 Poisson et Laplace ·
7 bilan d'énergie local et intégral · 8 puissance par le flux de Poynting · 9 valider l'ARQS magnétique ·
10 relations de passage. L'ancienne méthode « conductivité complexe » (hors programme) devient une notice
« Hors programme, souvent guidé » ; la liste des pièges est conservée.

## 4. Exercices (7 → 12, dont le Concours PT)

Tous les corrigés existants ont été recalculés (Python) : **justes**, conservés. Les nouveaux corrigés ont
été vérifiés avec sympy (`oem3_verif_sympy.py`) et numériquement.

| N° | Titre | Statut |
|---|---|---|
| 01 ★ | Pourquoi un conducteur est-il neutre ? | ancien 01 |
| 02 ★ | Bilan de charge dans un faisceau d'ions | **nouveau** (bilan 1 D, régime stationnaire) |
| 03 ★ | L'ARQS est-elle justifiée ? | ancien 02 |
| 04 ★ | Courants surfaciques : solénoïde et câble coaxial | **nouveau** (relations de passage) |
| 05 ★★ | Ce champ est-il possible ? | **nouveau** (4 équations, champ induit, Poisson/Laplace, Ampère local) |
| 06 ★★ | Le bétatron | ancien 03 |
| 07 ★★ | Lentille magnétique | ancien 04 |
| 08 ★★ | Faisceau d'électrons : charge d'espace et force magnétique | **nouveau** (Poisson, Gauss, Ampère, rapport v²/c²) |
| 09 ★★ | Charge d'un condensateur : courant de déplacement et bilan d'énergie | **nouveau** (Ampère généralisé, Poynting, U_m/U_e) |
| 10 ★★ | Conductivité de l'aluminium (modèle de Drude, **hors programme**) | ancien 05, titre signalé |
| 11 ★★★ | Courants de Foucault dans un noyau cylindrique | ancien 06 |
| Concours | Câble coaxial : des champs aux grandeurs de circuit | inchangé |

Renvois vérifiés : cours §6 → « exercice 1 » ; méthodes → « exercice 10 » (Drude) ; exercice 8 → « exercice 7 ».

## 5. Cartes

- Corrigées (question inchangée) : **21** (loi d'Ohm exigible avec σ, Drude signalé hors programme),
  **22** (σ du cuivre ; τ signalé hors programme), **23**, **24** (conductivité complexe), **34** (ARQS
  électrique) : préfixe « Hors programme en PT (pour aller plus loin) : ».
- Ajoutées (10) : Poisson/Laplace (form), démonstration de Poisson, équations locales de la statique (form),
  Gauss et flux sous forme intégrale (form), E n'est plus un gradient en régime variable, div j = 0 en ARQS,
  flux du courant de déplacement d'un condensateur, B entre les armatures (form), interprétation des termes
  du bilan de Poynting, densité d'énergie magnétique de 1 T (val).

## 6. Notations et cohérence du groupe

- Choisies : `σ` conductivité (exigible), `σ₀` réservée à la conductivité statique de Drude ; complexes
  soulignés, convention `e^{i(ωt−kz)}` (identique dans `oev` et `oec`) ; `Π` pour Poynting ; (MG), (MΦ),
  (MF), (MA) ; `e = −dΦ/dt`.
- **Divergences signalées (non modifiées)** : la charge surfacique est notée `σ` ici (§5, « dans ce
  paragraphe seulement ») et dans `estat2a`, mais `σ_s` dans `oemcond` ; le courant enlacé est `I_{enl}` ici
  et `I_{\text{enlacé}}` dans `magnetostat` ; le contour est `Γ` ici, `𝒞` dans `magnetostat` ; la normale de
  passage est `n⃗₁₂` ici et dans `oemcond`, `n⃗_{1→2}` dans `estat2a`. À harmoniser d'un seul geste si
  l'utilisateur le souhaite (cartes 17-18 comprises).

## 7. Doutes

- Le programme place la loi d'Ohm locale au programme « sans modèle » : le §6 garde le modèle de Drude,
  signalé hors programme sur place (plutôt que déplacé en fin de chapitre, car il éclaire immédiatement la
  validité de la loi). À déplacer en section « Pour aller plus loin » si l'on veut une règle uniforme.
- Exercice 8, Q5 : estimation volontairement grossière (force supposée constante), dite comme telle.
- Pas de renommage du chapitre proposé.
