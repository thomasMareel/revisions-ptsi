# SI de 1ʳᵉ année : corrections et signalements du hors-programme (suite de l'audit du 14/11/2026)

Sources : `docs/audit-2026-11/si-1a.md` (§3, §4), programme `pdf-pt/prog/si.txt` (et `phys.txt` pour la corrosion),
inventaire `docs/programme-pt/sciences-industrielles.md`. Référence pour les liaisons, la mobilité et l'hyperstatisme :
`chaines` (prefix `chs`), §1 et §5 : \(h = m + I_s - E_s\), \(E_s = 6(n-1)\) (3(n−1) en plan), \(h \geq 0\).
Chapitres relus récemment (`sequentiel`, `reseaux`, `transm`, `capteurs`, `usinage`, `trtherm`, `mcc`) : non touchés.

Fichiers produits (tous dans REV2) : 21 panneaux `*.src.html`, 10 fichiers de cartes `*-cartes-corr.json`
(prefix : `cine`, `stat`, `stab`, `prec`, `s2`, `ensi`, `afs`, `cota`, `fad`, `cvs`). Aucune carte ajoutée ni retirée,
ordre inchangé : la progression est conservée (retouches de texte, repli par rang).

## 1. Points de l'audit

| Point de l'audit | Revérification | Fait | Fichier |
|---|---|---|---|
| `cine` §4 « Glissière-rotule (hélicoïdale) » | Vrai : ce nom n'existe pas | Fait : « Hélicoïdale d'axe z » ; tableau renommé « principales liaisons » (7 sur 11, plus « libre ») | `cine-cours` |
| `cine` §6 : schéma cinématique confondu avec le graphe des liaisons | Vrai | Fait : graphe = classes (sommets) et liaisons (arcs) ; schéma = dessin aux symboles normalisés ; \(m = \sum \text{DDL} - r_c\) précisé | `cine-cours` |
| `cine` §6 et carte 23 : \(m = 3(n-1) - \sum(3-\text{DDL}_i)\) | Vrai : c'est \(m - h\) (identique à \(h_{plan} = m + I_s - 3(n-1)\) de `chaines`) | Fait : formule réécrite en \(m - h\), m par observation ; carte 23 réécrite (question gardée) | `cine-cours`, `cine-cartes-corr.json` |
| `statique` §3, méthode 3, cartes 10 et 23 : « h = inconnues − équations », « h < 0 : mécanisme » | Vrai (le cours disait « h < 0 : pas assez de liaisons », la méthode et la carte 10 « mécanisme ») | Fait : \(h = m + I_s - E_s\), toujours \(h \geq 0\) (h < 0 = mobilité oubliée) ; méthode 3 avec une étape « déterminer m » ; carte 23 : question fausse corrigée par `q_nouvelle` (« mécanisme », plus « liaison », isostatique / hyperstatique) | `stat-cours`, `stat-meth`, `stat-cartes-corr.json` |
| `statique` §3, tableau 2D (appui plan, appui ponctuel) | Vrai : appui plan de normale y en plan = Y, M_z (1 DDL) ; ponctuel : 5 DDL en 3D, 2 en plan | Fait : encadré de l'appui plan corrigé (X seulement avec frottement) ; tableau à 4 colonnes DDL (3D), DDL (2D), inconnues | `stat-cours` |
| `statique` §5, équilibre indifférent « au niveau du pivot » | Vrai | Fait : « sur l'axe du pivot » (stable / instable : « à la verticale de l'axe ») | `stat-cours` |
| `energsi` carte 15 (énergie RL « moitié-moitié ») | Vrai : résultat de la charge d'un condensateur | Fait : ½LI² stockée, puis E²/R dissipé en permanence, bilan \(Ei = Ri^2 + \frac{d}{dt}(\tfrac12 Li^2)\) | `ensi-cartes-corr.json` |
| `sys2` carte 13 (ξ ≈ 0,69 « sans dépassement ») | Vrai (calculé : t_r5 % ω₀ ≈ 2,9 pour ξ ≈ 0,69–0,70, D₁ = 5,0 % ; régime critique 4,74) | Fait : `q_nouvelle` « Valeur de z minimisant le temps de réponse à 5 %. » ; réponse avec 5 % de dépassement et rappel du critique (z gardé, comme le reste du paquet) | `s2-cartes-corr.json` |
| `ingsys` EXO 01 Q3 et §3 (fin de course = « boucle de l'asservissement ») | Vrai | Fait : Q3 = système séquentiel (tout ou rien), avec ce qui ferait un asservissement ; §3 : retour d'information asservi / séquentiel distingué ; méthode 2 alignée | `afs-exos`, `afs-cours`, `afs-meth` |
| `ingsys` carte 2 (diagramme de séquence sd) | Vrai : absent du cours et du programme | Fait | `afs-cartes-corr.json` |
| `cotation` concours : « spécification GPS » sans GPS | Vrai, mais c'est la ligne de source (le titre h3 n'en parle pas) | Fait : « (ajustement d'un roulement, chaîne de cotes) » | `cota-exos` |
| `cotation` concours : alésage de bague ∅25 +0,010/0 | Vrai : la norme des roulements place la tolérance sous la cote nominale | Fait : ∅25 0/−0,010 ; A1 recalculé : J_max = −0,002, J_min = −0,025 mm → **serré** (et non plus incertain), cohérent avec A2 | `cota-exos` |
| HP `trsurf`, `cnd` en entier | Vrai (G2 ne cite que les traitements thermiques surfaciques et le contrôle géométrique, S3) | Fait : encadré en tête du §1 ; renvoi aux traitements thermiques (2ᵉ année) et, pour la corrosion, à `electrochimie` (physique-chimie PT, l. 1771-1790 de `phys.txt`) | `tsu-cours`, `cnd-cours` |
| HP `statique` : travaux virtuels | Vrai (aucune des deux années) | Fait : encadré + « (hors programme) » au §4, méthode 4, EXO 05, cartes 20-21 | `stat-cours`, `stat-meth`, `stat-exos`, `stat-cartes-corr.json` |
| HP `cotation` : chaîne de cotes, notation ISO | Vrai (l. 441-442 : seule la nature de l'ajustement) | Fait : encadrés §2 (notation ISO) et §4 ; méthode 3 ; EXO 03 ; partie B du concours ; cartes 11, 12, 13 (ISO) et 19 à 22 (chaîne) | `cota-cours`, `cota-meth`, `cota-exos`, `cota-cartes-corr.json` |
| HP `precision` : PD, PID, Ziegler-Nichols | Vrai (programme : P, PI, avance de phase) | Fait : EXO 06, partie B du concours (PID), lignes PD et PID du tableau du §5, cartes 9, 10, 12, 13, 23 **et 15** (action D) | `prec-exos`, `prec-cours`, `prec-cartes-corr.json` |
| HP `stabilite` : cartes Nyquist, Routh, lieu des pôles | Vrai (l. 910-911) ; cours et EXO 04 déjà signalés | Fait : cartes 9, 14 (Nyquist), 10, 24, 26 (Routh), 15 (lieu des pôles) | `stab-cartes-corr.json` |
| `addfab`, `cvs`, `cine` : ce qui est clairement HP | `addfab` : frittage conventionnel absent de G2 ; `cvs` : gradateur exclu (l. 706-709) ; `cine` : Frenet est au programme de physique PTSI (l. 960), donc rien | Fait : `addfab` §1, méthode 1, EXO 01 et 03, A3 du concours, cartes 0 à 5 ; `cvs` encadré du gradateur, méthodes, cartes 1 (mention) et 3 | `fad-*`, `cvs-*` |

## 2. Erreurs supplémentaires trouvées (corrigées)

- **`cine` EXO 05 (satellite dans une couronne)** : le contact I est du côté opposé à O, donc \(\overrightarrow{CI} = +r\,\vec e_r\) (la correction écrivait −r e_r « vers O »). Le satellite tourne en **sens inverse** du porte-satellite : Ω_S = −6 rad/s, Ω_S/Ω_H = −(R−r)/r = −2. Vitesse de T (0,6 m/s) inchangée.
- `cine` §3 : « connaître la vitesse d'un point et la rotation ne suffit pas » (c'est justement le torseur) ; §1 : « supposée galiléen » ; méthodes, piège RSG : vitesse nulle du point de contact seulement sur un support fixe.
- `statique` EXO 06 : titre « Portique 3D — équilibre spatial » pour un problème plan, « 6 liaisons » ; Q3 faux sur [2, 4] (1600 − 500x ne s'annule pas en B) et signes de T et M_f incohérents : réécrit avec la convention du chapitre `rdm` (M_fz = 500x − 1800 puis 500x − 2000, saut de −200 N·m) et signalé « 2ᵉ année » (torseur de cohésion, S3).
- `statique` EXO 04 (treillis) : longueur AB manquante (le corrigé supposait un triangle équilatéral sans le dire), moments « 2L cos β » sans objet, Q3 contradictoire (« tirent… poussent ») : donnée ajoutée (AB = 1 m), corrigé remis au propre, barre AB tendue (2,89 kN) ajoutée.
- `statique` EXO 05 : « A sous la glissière » contraire à la figure ; EXO 01 Q3, méthode 1 (étape 6), carte 24 : h sans la mobilité ; piège « la normale sort du solide ».
- `ingsys` concours « bilan de puissance », B1 : « quelques watts en améliorant le variateur » faux (le passer de 0,95 à 0,90 dégrade le bilan).
- `ingsys` §2, encadré « Programme PTSI » : il manquait « compléter » (le programme : diagrammes à lire ou à compléter, structure fournie).
- `cvs` §4 : « source de tension réversible si sa tension change de signe » : réversibilités en courant et en tension distinguées (une batterie est réversible en courant).

## 3. Noms de chapitres à changer (proposition)

- `trsurf` « Traitements de surface » → « Traitements de surface (culture, hors programme) ».
- `cnd` « Contrôle non destructif » → « Contrôle non destructif (culture, hors programme) ».
- `addfab` « Frittage & fabrication additive » → « Fabrication additive et frittage » (le procédé au programme en tête).

## 4. Doutes, non faits

- Cartes de `trsurf` (20) et `cnd` (20) **non préfixées** : seul l'encadré en tête du cours a été demandé ; le renommage ci-dessus les signalerait aussi. À préfixer si l'on veut les signaler dans les révisions du jour.
- Laissés (pas clairement hors programme) : composition des accélérations et Coriolis (`cine` §5, déjà « rarement exigée ») ; CIR (`cine` §6, méthode 5 : outil classique, non cité) ; rugosité Ra (`cotation` §3, non citée) ; PI dans `precision` (S3, mais le cours renvoie déjà au chapitre de 2ᵉ année) ; carte `energsi` 16 (RSG : « point de contact immobile » suppose un sol fixe).
- Non faits (hors du mandat « erreurs », pour le lot suivant) : passage de z à ξ dans les cartes de `sys2` et `stabilite` ; vocabulaire « chaîne d'énergie / distribuer » d'`ingsys` (programme : chaîne de puissance, moduler) ; `statique` EXO 02 Q3 inachevé (pas faux).
- Contrôles : `verif_src.py` sans ERREUR (attentions « pas de bloc AU PROGRAMME » et formules en ligne longues : déjà présentes à l'identique dans les panneaux d'origine) ; `corriger_cartes.py --essai` sans erreur pour les 10 fichiers ; aperçus à 390 et 1440 px : voir §5.

## 5. Aperçus (apercu_src.py, 390 et 1440 px)

- 41 aperçus (21 panneaux × 2 largeurs, `cine-cours` à 390 fait au premier essai) : `merr`, `brut` vides et aucune erreur JS partout ; à 1440 px, `larges` vide partout.
- À 390 px, « ATTENTION : la page déborde » pour `cine-exos` (EXO 04), `stat-exos` (EXO 06, Q2), `cota-exos` (corrigés des EXO 02, 03 et du concours), `prec-cours` (démonstration du §2) et `prec-exos` (EXO 03, 05, 06) : **déjà présents à l'identique sur les panneaux d'origine** (mêmes formules, passages non modifiés), et artefacts de l'outil, qui déplie les solutions sans passer par `toggleSol`. Une fois `window.__apresRendu(panneau)` appelé, comme le fait le site au dépliage, les 5 panneaux (mes versions) tombent à `scrollW` = 390 (script `/tmp/claude-0/-home-user/6f48d12f-3f0e-5709-96fa-34955b53c076/scratchpad/si/voir_rendu.js`). Seul écart dû à mes retouches : la formule de Q3 de l'EXO 05 de `cine` (3 signes de plus qu'avant), elle aussi absorbée par le site.
- `afs-exos` à 390 : premier essai expiré (Chromium chargé) ; relancé : OK.
- `diff` panneau d'origine ↔ REV2 relu pour les 21 panneaux : seules les retouches décrites ci-dessus apparaissent.
