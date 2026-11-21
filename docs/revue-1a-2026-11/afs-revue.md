# Revue : `ingsys` (prefix `afs`) « Analyse fonctionnelle & ingénierie système » — 2026-11-21

Point 4 de l'audit (`docs/audit-2026-11/si-1a.md` §2 point 4, §5 point 4). Chapitre réécrit : cours, méthodes et exercices
entièrement refaits, cartes relues (1 corrigée) et complétées (19 ajoutées). Programme : `pdf-pt/prog/si.txt`
(A1, A2, A3, B3, A4 ; semestres relus sur le PDF : A1 S1, A2 S2, A3 S1 sauf « justifier le choix des constituants » S4
et diagramme d'états S2, B3 « vérifier la cohérence du modèle » S2, **A4 entier en S4**).

## Fichiers produits (dans `AN1/`)
- `afs-cours.src.html` (103 Ko, dont ≈ 45 Ko de SVG ; ≈ 46 800 signes de texte contre ≈ 4 200), `afs-meth.src.html`,
  `afs-exos.src.html` : 1ʳᵉ ligne identique au panneau actuel (`<section class="panel active" id="afs-cours">`,
  `<section class="panel" id="afs-meth">`, `<section class="panel" id="afs-exos">`).
- `afs-cartes-corr.json` (1 carte), `afs-cartes-ajout.js` (19 cartes, à la fin).
- Scripts : `afs_calculs.py` (exemples du cours), `afs_calculs_exos.py` (exercices et exemples éclairs des méthodes),
  `afs_svg.py` (aides SysML : cadre à onglet, bloc, exigence, contenance ⊕, dépendances pointillées, acteur, cas,
  ports, puces de flux), `afs_figs.py` + `afs_figs_exos.py` → `afs_figs.json` (17 figures), `afs-cours.tpl.html` et
  `afs-exos.tpl.html` (gabarits `@@FIG:nom@@`) assemblés par `afs_construire.py` ; contrôles : `afs_voir.py`
  (rendu clair/sombre + détection automatique des chevauchements, traits sur texte, texte < 12 px),
  `afs_figsite.js` (captures des figures dans la copie du site), `afs_deborde.js`, `afs_cartes_rendu.js`
  (cartes passées par `flashPretty` puis MathJax). Copies des anciens panneaux : `afs_orig_{cours,meth,exos}.html`.

## Erreurs et faiblesses de l'ancien chapitre (corrigées)
1. **Figure des chaînes en 8 à 9 px** (`style="font-size:9px"`, sous la règle des 12 px) : redessinée (§8), avec le
   vocabulaire 2021 et les liens ordres / mesures.
2. §3 intitulé « L'architecture fonctionnelle d'un système **asservi** » : les deux chaînes valent pour tout système
   commandé (l'exemple du portail est séquentiel). Le lien asservi / séquentiel a maintenant sa section (§9).
3. §1 : « fonction principale / fonctions de service / fonctions contraintes » présentées comme trois catégories
   disjointes et comme exigibles. En analyse fonctionnelle (APTE), les fonctions de service **comprennent** les
   principales et les contraintes ; ce vocabulaire n'est plus au programme 2021 (qui parle d'exigences) : déplacé en
   « Pour aller plus loin », carte 0 corrigée (réponse préfixée « Hors programme en PTSI : »).
4. Exercice 02, Q1 : la « flexibilité » confondue avec le sens de la borne (≥) : corrigé (niveau minimal, flexibilité
   F0 si l'exigence est impérative).
5. Deux exercices marqués « CONCOURS PT » (le format en veut un) : le bilan de puissance du treuil devient l'EXO 08
   (inchangé, juste ; ajout du cas « variateur à 0,90 → 278 W ») ; l'ancien « Concours » du portail est fusionné
   dans l'EXO 01 (besoin, exigences chiffrées, capteurs).
6. Aucune figure SysML, aucune exigence chiffrée reliée à une solution, aucune ligne d'ACV, frontière et flux en deux
   phrases, A4 (S4) présenté sans le signaler : tout cela est traité ci-dessous.
   (L'erreur de l'audit sur l'exo 01 Q3, fin de course présenté comme boucle d'asservissement, était déjà corrigée
   dans le dépôt : réponse gardée.)

## Couverture du programme : avant → après

| Capacité (semestre) | Avant | Après |
|---|---|---|
| A1 Décrire le besoin et les exigences, ingénierie système, cahier des charges (S1) | 🔶 §1, §2 en texte | ✅ §1 (besoin, matière d'œuvre, démarche, vérifier/valider, panorama SysML), §3 uc dessiné, §4 ; M2–M4 ; EXO 02–04 ; cartes |
| A1 Traduire en exigences, critères et niveaux (S1) | 🔶 critère/niveau/flexibilité | ✅ §4 (bonne exigence, F0–F3, tableau de 7 exigences, req dessiné avec contenance, deriveReqt, refine, satisfy, verify) ; M3, M4 ; EXO 02, 04, concours A |
| A1 Impact environnemental et sociétal, ACV (S1) | ❌ | ✅ §5 (phases, unité fonctionnelle, indicateurs, ordres de grandeur, ACV chiffrée robot / tondeuse, sociétal) ; M5 ; EXO 05 ; cartes |
| A2 Frontière, milieu extérieur, éléments influents (S2) | 🔶 une phrase | ✅ §2 (figure, isoler et justifier selon la question) ; M1 ; EXO 01 Q5, concours B1 |
| A2 Nature et codage des flux (S2) | 🔶 | ✅ §2 (tableau, \(P = UI, Fv, C\omega, pQ_v\), nombre de bits, Gray, hexadécimal) ; EXO 07, 11 ; cartes |
| A3 Associer fonctions et constituants, bdd, ibd (S1) | 🔶 quatre lignes | ✅ §6 (bdd dessiné, multiplicités, bilan de masse), §7 (ibd dessiné, ports, 9 flux, compatibilité d'interface) ; M6, M7 ; EXO 06, 07, concours B |
| A3 Chaînes fonctionnelles, alimenter… agir, acquérir… communiquer (S1) | 🔶 vocabulaire 2021 mais figure illisible | ✅ §8 (figure, constituants, rendements, puissance en montée) ; M8 ; EXO 01, 07, 08, concours B3, C |
| A3 Liens entre chaînes : asservi / séquentiel (S1) | 🔶 | ✅ §9 (stm du robot, régulation de la lame calculée et simulée, pièges fin de course et thermostat) ; M9 ; EXO 09, concours E1 |
| A3 Diagramme d'états (S2) | renvoi | renvoi à « Systèmes séquentiels », stm du robot en §9 |
| B3 Confronter modèle et mesures (S2) ; A4 écarts (S4, introduit) | 🔶 trois lignes | ✅ §10 (trois systèmes, trois écarts, écart relatif, causes, exemple chiffré) ; M10 ; EXO 10, concours E2–E3 ; le recalage (S4) est signalé « 2ᵉ année » |
| Hors programme | — | « Pour aller plus loin » : sd, act, par ; APTE (bête à cornes, pieuvre, FAST) ; ACV normalisée ; MBSE |

## Cours (10 sections + « Au programme · PTSI » + « Pour aller plus loin »)
§1 Système, besoin et ingénierie système · §2 Frontière, milieu extérieur et flux · §3 Cas d'utilisation · §4 Exigences ·
§5 Cycle de vie et impact environnemental · §6 Architecture et bdd · §7 ibd · §8 Chaînes de puissance et d'information ·
§9 Systèmes asservis et séquentiels · §10 Performances et écarts. Un exemple traité chiffré par section (10), une
erreur classique par section, 11 figures calculées (frontière et flux ; uc ; req ; cycle de vie ; ACV en barres
empilées ; bdd ; ibd + tableau des flux ; chaînes ; stm ; régulation de la lame simulée en Python : chute de 11 % en
boucle ouverte, retour à la consigne en moins d'une seconde en boucle fermée ; triangle des écarts). Fil rouge : un
robot de tonte inventé (données cohérentes d'une section à l'autre : 8,0 kg, batterie 18 V 3,0 A·h = 54 W·h, 40 W en
tonte, 0,30 m/s, autonomie simulée 70 min, mesurée 58 min). Formules du Formulaire (`data-nom`) : puissance d'un flux
d'énergie, nombre de bits, énergie d'une batterie, rendement d'une chaîne, écart relatif.

## Méthodes (10)
1 Isoler un système et inventorier les flux · 2 Lire un uc · 3 Traduire un besoin en exigences quantifiées · 4 Lire un
diagramme d'exigences · 5 Exploiter une ACV · 6 Lire un bdd · 7 Compléter un ibd · 8 Identifier les chaînes de
puissance et d'information · 9 Distinguer asservi et séquentiel · 10 Caractériser les écarts. Chacune : étapes,
exemple éclair chiffré vérifié, 3 encadrés « Piège ».

## Exercices (11 + Concours PT), tous inventés, valeurs vérifiées (`afs_calculs_exos.py`)
01 ★ Portail : besoin, chaînes, frontière (ancien EXO 01 + ancien « Concours » portail) · 02 ★★ Drone : exigences,
deriveReqt et conflit autonomie / masse (ancien, complété) · 03 ★ Consigne à colis : uc dessiné · 04 ★★ Monte-escalier :
req dessiné, exigence dérivée calculée · 05 ★★ Trottinette personnelle / libre-service : ACV par km · 06 ★★ Fauteuil
roulant : bdd dessiné, bilan de masse, série de batteries · 07 ★★ Arrosage automatique : ibd à compléter (port non relié),
interface 0–5 V / 0–3,3 V · 08 ★★ Bilan de puissance (ancien, gardé) · 09 ★ Asservi ou séquentiel (six systèmes, piège
de l'imprimante 3D en boucle ouverte) · 10 ★★★ Halage d'un bateau : performances attendues, simulées, mesurées, modèle
enrichi (recalage signalé « 2ᵉ année ») · 11 ★★ Station météo : Gray, impulsions, trame en hexadécimal ·
CONCOURS PT ★★★ Plateforme élévatrice PMR en 5 parties (exigences, frontière et ibd, dimensionnement, autonomie,
comportement et écarts), 2 figures.

## Cartes
- Relues : 10 cartes. **Corrigée** : carte 0 (fonctions principale / de service / contrainte), réponse seule, préfixée
  « Hors programme en PTSI : ». Les autres sont justes. La carte 2 cite le diagramme de séquence (« le programme ne le
  cite pas ») : désormais cohérente avec le cours (« Pour aller plus loin »). La carte 7 écrit « pré-actionneur », le
  cours « préactionneur » (graphie du programme) : laissée telle quelle (variante, pas une erreur).
- **Ajoutées : 19** (10 → 29) : matière d'œuvre, vérifier/valider, frontière et élément influent, natures de flux,
  puissance (form), nombre de bits (form), Gray, acteur et cas, include/extend, bonne exigence, relations du req,
  énergie d'une batterie (form), cycle de vie, unité fonctionnelle, ordres de grandeur CO₂ (val), bdd, ibd, rendement
  global (form), asservi / séquentiel. Les cartes avec unités sont écrites en `\\( … \\)` pour que `flashPretty` ne
  mette pas « V », « mm » en italique (contrôlé par `afs_cartes_rendu.js` : aucune erreur MathJax).
- `corriger_cartes.py afs … --essai` : 1 réponse corrigée ; `ajouter_cartes.py afs … --essai` : 10 → 29 cartes.

## Contrôles
`verif_src.py` : aucune erreur ni « attention » sur les trois fichiers. `apercu_src.py` à 390 et 1440 : `merr`,
`brut`, `larges` vides, aucune erreur JS, aucune ligne ATTENTION (deux formules en ligne trop longues à 390 px
passées en bloc ou raccourcies). Figures : `afs_voir.py tout` sans chevauchement ni trait sur texte, captures claires
et sombres regardées (aplats des barres de l'ACV lisibles dans les deux thèmes), captures dans la copie du site à
390 px (les diagrammes SysML, de 540 unités de large, défilent horizontalement au téléphone avec le fondu du site,
comme prévu par `.lisible` / `.defile`) et à 1440 px en sombre.

## Notations et vocabulaire
Chaîne de puissance (alimenter, moduler, convertir, transmettre, agir) et chaîne d'information (acquérir, traiter,
communiquer) comme `schblocs`, `chfonc`, `mph` ; préactionneur, actionneur, transmetteur, effecteur ; \(\eta\),
\(P = C\,\omega\), \(C_m\), \(\omega_m\) ; énergie en W·h, capacité en A·h ; poursuite / régulation (programme et
`schblocs`) ; trois systèmes souhaité (attendu) / simulé / réel (mesuré) comme `mph` §1 ; relations SysML écrites avec
leurs mots-clés anglais («deriveReqt», «satisfy», «verify», «refine», «include», «extend»), comme dans les sujets.

## Points pour l'intégrateur et doutes
1. **Performance au démarrage** : `chap-ingsys` est l'un des deux chapitres non repliés. Ses panneaux passent de
   ≈ 290 à ≈ 2 400 éléments (cours 1 305, exercices 953, méthodes 163), surtout des éléments SVG : ≈ + 2 100
   éléments au chargement (le site en compte ≈ 19 000). À peser : laisser tel quel, ou replier aussi les panneaux de
   `chap-ingsys` (il est dans `#si-content`, masqué au départ) en adaptant `replier_panneaux.py` et `validate.py`.
2. **Renvoi à mettre à jour** dans `seq-cours` (bloc « Au programme ») : « le panorama des diagrammes SysML
   d'« Analyse fonctionnelle & ingénierie système » (§2) » → le panorama est maintenant en §1 (tableau), les diagrammes
   en §3 à §7.
3. **Nom du chapitre** (non modifié) : le programme 2021 ne parle plus d'« analyse fonctionnelle ». Proposition, à
   valider : « Ingénierie système : besoin, exigences, architecture » (mobLabel « Ingénierie système ») ; `chf-cours`
   cite l'ancien nom entre guillemets.
4. Valeurs d'ACV (§5, EXO 05) : ordres de grandeur réalistes mais **fictifs** (présentés comme « étude simplifiée,
   valeurs arrondies ») ; seuls les facteurs d'émission (électricité ≈ 0,05–0,06 kg CO₂e/kWh en France, ≈ 0,25 en
   Europe, ≈ 1 au charbon ; essence ≈ 2,3 kg CO₂/L brûlé, ≈ 2,8 avec l'amont ; batterie ≈ 100 kg CO₂e/kWh) sont donnés
   comme repères.
5. Classes de flexibilité F0 à F3 (norme d'analyse fonctionnelle) citées comme vocabulaire usuel du cahier des charges,
   sans en faire une exigence du programme.
6. Le programme ne cite pas le diagramme de cas d'utilisation nommément (« ingénierie système et diagrammes
   associés ») ; il est traité parce qu'il ouvre la plupart des dossiers SysML des sujets.
7. Droit d'auteur : aucun manuel utilisé ; tous les systèmes, exigences, données et exercices sont inventés.
