# Revue : `cvs` (prefix `cvs`) « Convertisseurs statiques » — 2026-11-21

Point 4 de l'audit (`docs/audit-2026-11/si-1a.md` §2 point 5, §5 point 7) : cellule de commutation non formalisée,
démarche de synthèse absente, onduleur et redresseur absents en 1ʳᵉ année, aucune figure. Programme :
`pdf-pt/prog/si.txt` l. 692-714, B2 « Modéliser les convertisseurs statiques d'énergie », **S2** ; chaîne de
puissance (A3, S1, l. 260-268). Chapitres voisins lus : `hacheurs`, `mcc` (1ʳᵉ année, S4 anticipé), `triphase` et
`machalt` (2ᵉ année), dont les notations sont reprises (voir plus bas).

## Fichiers produits (dans `AN1/`)
- `cvs-cours.src.html` (131 Ko dont ≈ 85 Ko de SVG ; ≈ 46 700 signes de texte contre ≈ 9 800), `cvs-meth.src.html`,
  `cvs-exos.src.html` : 1ʳᵉ ligne identique au panneau actuel.
- `cvs-cartes-corr.json` (2 cartes, réponse seule), `cvs-cartes-ajout.js` (15 cartes, à la fin) : 25 → 40 cartes.
- Scripts : `cvs_calculs.py` (exemples du cours), `cvs_calculs_exos.py` (exercices, exemples éclairs des méthodes,
  simulations de contrôle), `cvs_svg.py` (symboles normalisés : sources de tension / courant / alternative,
  résistance, bobine, condensateur, diode, transistor (symbole IGBT), transistor + diode, interrupteur, flèches de
  tension et de courant, repère de chronogramme), `cvs_figs.py` + `cvs_figs2.py` → `cvs_figs.json` (14 figures),
  gabarits `cvs-cours.tpl.html`, `cvs-exos.tpl.html` assemblés par `cvs_construire.py` ; contrôles `cvs_voir.py`
  (rendu clair / sombre + détection de chevauchements, traits sur texte, texte hors cadre ou sous 12 px),
  `cvs_figsite.js` (captures des figures dans la copie du site), `cvs_cartes_rendu.js` (cartes passées par
  `flashPretty` puis MathJax). Anciens panneaux : `cvs_orig_{cours,meth,exos}.html`.

## Erreurs et faiblesses de l'ancien chapitre (corrigées)
**Cours**
1. Aucune figure ; cellule de commutation non définie ; aucune démarche de synthèse ; ni onduleur ni redresseur
   (seulement cités dans la liste des quatre familles) ; aucun exemple chiffré.
2. §2 : MOS « faible puissance (< 1 kW) », « jusqu'à plusieurs milliers de kHz » : inexact (les MOS SiC équipent des
   onduleurs de traction de centaines de kW ; le découpage usuel va de quelques dizaines à quelques centaines de kHz).
   Aligné sur `triphase` §1 et §9 (tensions modestes, découpage rapide ; IGBT 600 V à quelques kV, ≈ 20 kHz).
3. §2 : interrupteur bidirectionnel en courant, « la diode conduit quand v devient négative » : faux. Fermé,
   l'interrupteur impose \(v_K = 0\) ; c'est le **signe du courant** qui décide entre transistor et diode. Corrigé
   (§4, notice « Erreur classique ») ; même correction sur la carte 12.
4. §3 : « Convention récepteur : le courant entre par la borne +. Le dipôle reçoit de l'énergie » confond une
   convention d'orientation et un fonctionnement. Remplacé par l'orientation des interrupteurs en convention
   récepteur (§4) et le plan \((u, i)\) de la charge avec \(p = ui\) (§3).
5. §4 : « l'induit d'une MCC est une source de courant réversible car le moteur peut fonctionner en récepteur ou en
   générateur » : la réversibilité dépend des signes (en courant ou en tension), pas du seul sens de l'énergie.
   Remplacé par les quadrants et l'exemple du monte-charge (réversible en tension, pas en courant).
6. Commande des transistors « \(v_{GS} > 0\) → passant » : un seuil existe ; écrit « ≈ 15 V pour fermer, 0 ou
   négative pour ouvrir ».
7. Les rappels de dipôles (§3 ancien) sont réduits à ce qui sert : continuité de \(i_L\) et \(u_C\), critère
   \(T \ll \tau\), et le résultat clé absent \(\langle u_L\rangle = 0\), \(\langle i_C\rangle = 0\) en régime périodique.

**Exercices**
8. Ancien EXO 02 (monoalternance), Q3 : « la source fournit \(V_{\text{eff}}I_{\text{eff}} = 2{,}83\ \text{W}\) » : faux.
   La diode idéale ne dissipe rien, la source fournit 2 W ; 2,83 VA est la puissance apparente (2ᵉ année). Corrigé
   (nouvel EXO 07, vérifié par intégration numérique).
9. Ancien EXO 04 (transistor en commutation), Q3 : rendement avec résistance série « ≈ 53 % » faux (61 % avec ses
   propres chiffres) ; « ≈ 95 % » pour le découpage faux (99 %) ; \(R_s = 6{,}4\ \Omega\) ne donne pas la même tension
   moyenne (29,3 V et non 28,8 V) ; surtout, sur une charge **résistive**, comparer à tension moyenne égale n'a pas de
   sens (le découpage donne 135,5 W, la résistance série 82,9 W). Refait à puissance de chauffe égale :
   \(R_s = 3{,}04\ \Omega\), 77 % contre 98,8 % (nouvel EXO 10, pertes de commutation ajoutées).
10. Ancien EXO 03 (pont de Graetz), Q3 : l'effet du condensateur était donné sans dire que la tension moyenne monte
    vers la crête (≈ 309 V, et non 207 V) ni que l'estimation \(\Delta V \approx V_{\max}/(2fRC)\) est un majorant
    (32,5 V estimés, 27 V simulés). Précisé, marqué « 2ᵉ année : filtrage » ; contraintes sur les diodes ajoutées.
11. Ancien EXO 01, Q2 : « Quel composant limite les dommages ? » sans réponse dans la correction : reformulée
    (tension inverse maximale \(V_{RRM}\)) ; démarche « hypothèse puis vérification » rédigée.
12. Ancien EXO 06 (redresseur à thyristor) : hors programme non signalé (le programme limite la synthèse aux
    convertisseurs à interrupteurs deux ou trois segments ; `triphase` classe les thyristors en culture). Titre
    « (hors programme, pour aller plus loin) », modèle du thyristor donné dans l'énoncé, validité « charge
    résistive » précisée (nouvel EXO 11).
13. Ancien « Concours PT » (trois questions de cours, ★★☆) : gardé et étendu en EXO 05 (cellule chiffrée, choix des
    interrupteurs, temps mort) ; nouveau sujet Concours en quatre parties.

**Méthodes** : ancienne méthode 3 et pièges reprenant l'erreur 2 (MOS « basse puissance, très haute fréquence ») ;
réécrites. Méthodes anciennes gardées (état d'une diode, règles d'association, comportement des L et C), fondues
dans les nouvelles.

**Cartes** (25 relues ; 2 fausses, corrigées par leur réponse, question inchangée)
- carte 9 (MOS / IGBT) : « MOS < 1 kW, jusqu'à plusieurs milliers de kHz » (erreur 2) ;
- carte 12 (interrupteur bidirectionnel en courant) : « la diode conduit quand v est négative » (erreur 3). Sa
  question parle de « diode de roue libre » : appellation admise pour une diode antiparallèle (les modules IGBT la
  nomment ainsi), question gardée ; la nouvelle réponse explique ce rôle.
- Gardées : carte 6 (« V_A > V_K → passante », simplification classique), cartes 15-16 (juste en continu établi),
  carte 3 (gradateur déjà préfixé « Hors programme (pour aller plus loin) : », juste : il est hors de tout programme).

## Couverture du programme : avant → après

| Capacité (B2, S2 sauf mention) | Avant | Après |
|---|---|---|
| Chaînes fonctionnelles : fonction moduler (A3, S1) | une phrase | ✅ §1 (figure de la chaîne d'un vélo, définition, familles, rhéostat contre découpage chiffré) ; M10 ; Concours A1 ; cartes 0, 38 |
| Nature des grandeurs d'entrée-sortie, sources de tension et de courant | 🔶 §4 (texte) | ✅ §2 (définitions, figure des caractéristiques, L et C comme sources, \(T \ll \tau\), \(\langle u_L\rangle = 0\)) ; M1 ; EXO 03 ; Concours A2 ; cartes 36 |
| Réversibilité des sources et des convertisseurs | 🔶 une ligne | ✅ §3 (définitions, figure des quadrants du plan \((u,i)\), monte-charge chiffré, mise en garde sur les plans) ; M1, M10 ; EXO 03, 06 ; Concours A3 ; carte 39 |
| Modèles des interrupteurs parfaits, deux ou trois segments | 🔶 §2 (texte, erreur 3) | ✅ §4 (définition, figure symboles + caractéristiques, tableau, MOS / IGBT) ; M4 ; EXO 04 ; cartes 28 |
| Commutations spontanée et commandée | 🔶 diode seulement | ✅ §5 (figure des trajectoires, règle des signes, exemple du hacheur série) ; M5 ; EXO 04, 05 ; carte 27 |
| Règles d'association des sources ; cellule élémentaire de commutation | 🔶 règles seules | ✅ §6 (règles, figure de la cellule, complémentarité, temps mort, \(\langle u\rangle = \alpha E\), \(\langle i_e\rangle = \alpha I\), \(U = E\sqrt\alpha\), conservation de la puissance) ; M2 ; EXO 02, 05 ; cartes 25, 26, 30 |
| Synthèse des convertisseurs (nature et réversibilité des sources, bidirectionnalité des interrupteurs) | ❌ | ✅ §7 (méthode en six étapes, tableau des cinq cas, synthèse du pont asymétrique avec figure) ; M6 ; EXO 06 ; Concours B ; carte 29 |
| Hacheur (continu-continu) | renvoi | ✅ §8 résumé + figure calculée (schéma, \(u\), \(i\), qui conduit), exemple chiffré ; détail renvoyé à « Les hacheurs » ; EXO 05, 06 ; Concours C |
| Onduleur (continu-alternatif) ; convertisseurs à deux ou trois cellules | ❌ | ✅ §9 (synthèse, figure du pont, pleine onde, \(U = E\), courant R-L calculé avec \(I_0 = (E/R)\tanh(T/4\tau)\), rôle des diodes, figure des chronogrammes, idée de la MLI avec figure, trois cellules) ; M7 ; EXO 09 ; cartes 31, 32, 33 |
| Redresseur (alternatif-continu) | ❌ (exercices seuls) | ✅ §10 (synthèse → diodes, règle de conduction, figure du PD2 et des chronogrammes, \(\langle u_s\rangle = 2V\sqrt2/\pi\), contraintes des diodes, monoalternance, PD3 structurel) ; M8 ; EXO 07, 08 ; cartes 34, 35 |
| Pertes, rendement (ordres de grandeur) | une phrase | ✅ §11 (conduction, commutation avec figure, \(P_{\text{com}}\), bilan chiffré d'un hacheur, redressement synchrone) ; M9 ; EXO 10 ; Concours D ; cartes 37, 38 |
| Hors programme | gradateur cité, thyristor non signalé | « Pour aller plus loin » : gradateur, thyristor et pont commandé, interrupteurs à quatre segments, convertisseurs indirects, SiC / GaN ; EXO 11 signalé |
| 2ᵉ année (S3, S4) | — | renvois : ondulation et filtrage, puissances et facteur de puissance, harmoniques et MLI détaillée, triphasé, calibres (`triphase`, `chfonc`) |

(Les numéros de cartes de la colonne « Après » sont les index du deck après ajout : 25 à 39 pour les nouvelles.)

## Cours (bloc « Au programme · PTSI » + 11 sections + « Pour aller plus loin »)
§1 Le convertisseur dans la chaîne de puissance · §2 Sources de tension et de courant · §3 Réversibilité et quadrants ·
§4 Interrupteurs parfaits et caractéristiques statiques · §5 Commutations spontanées et commandées · §6 Cellule de
commutation · §7 Synthèse d'un convertisseur · §8 Hacheurs · §9 Onduleur monophasé en pont · §10 Redresseur à diodes ·
§11 Pertes et rendement. Douze exemples traités chiffrés (au moins un par section, deux au §9), une erreur classique
par section, neuf formules nommées (`data-nom`) pour le Formulaire, trois démonstrations dépliables
(\(\langle u_L\rangle = 0\), \(I_0\) de l'onduleur, \(\langle u_s\rangle\) du PD2).

Figures (13 dans le cours, toutes calculées ou tracées par script, classes du site, vérifiées en clair et en sombre à
360 px puis dans la copie du site à 390 et 1440 px) : chaîne de puissance ; caractéristiques des sources ; quadrants ;
interrupteurs (symboles + caractéristiques) ; trajectoires de commutation ; cellule ; pont asymétrique ; hacheur série
(régime périodique exact : 4,44 → 6,75 A) ; onduleur en pont ; chronogrammes pleine onde sur R-L (exponentielles
exactes, zones de conduction des diodes, \(i_e\) négatif) ; MLI (porteuse, modulante, moyenne par période) ; PD2
(losange + \(u_s\), \(i_e\)) ; pertes par commutation. Une 14ᵉ figure (pont en H avec induit) illustre le Concours.

## Méthodes (10, contre 5)
1 nature et réversibilité d'une source · 2 règles d'interconnexion · 3 état d'une diode · 4 caractéristique statique ·
5 commutation spontanée ou commandée (+ piège d'orientation) · 6 synthèse · 7 chronogrammes d'une cellule ou d'un
pont · 8 valeurs moyenne et efficace · 9 bilan de puissance et pertes (+ piège \(\langle u\rangle\langle i\rangle\)) ·
10 choix du convertisseur et de la technologie (+ piège du plan des quadrants). Chaque méthode a un exemple éclair
chiffré, vérifié dans `cvs_calculs_exos.py`.

## Exercices (12, contre 7)
01 diode (ancien 01, Q2 reformulée) · 02 associations de sources (ancien 05, + surtension de 20 kV) · 03 nature et
réversibilité des sources (nouveau) · 04 caractéristiques statiques et choix des interrupteurs (nouveau) · 05 cellule
chiffrée (ancien Concours étendu) · 06 synthèse d'un hacheur réversible en courant (nouveau) · 07 monoalternance
(ancien 02, Q3 corrigée) · 08 pont de Graetz (ancien 03, précisé) · 09 onduleur pleine onde sur R-L (nouveau, bilan
d'énergie vérifié deux fois : 4,16 J par demi-période = \(RI_{\text{eff}}^2\), 416 W) · 10 transistor en commutation
et rendement (ancien 04, refait) · 11 thyristor (ancien 06, signalé hors programme) · **Concours PT** « Navette
autonome d'entrepôt » (nouveau, quatre parties : chaîne et sources, synthèse du pont en H, commande bipolaire en
traction et en freinage récupératif, pertes et choix de \(f_{\text{déc}}\)).

## Cartes ajoutées (15)
Cellule ; valeurs moyennes de la cellule ; règle des signes ; segment ; étapes de la synthèse ; temps mort ; onduleur
pleine onde ; diodes de l'onduleur ; idée de la MLI ; PD2 ; redresseur sans commande ; \(\langle u_L\rangle = 0\) ;
pertes par commutation ; rendement (`val`) ; monte-charge (réversibilité en tension). Formules en `\\( … \\)`,
`cat:'form'` sur les cinq cartes de formule. Rendu contrôlé (flashPretty puis MathJax : aucune erreur).

## Notations (alignées sur `triphase`, 2ᵉ année)
\(E\) source de tension continue, \(I\) source de courant ; \(K\), \(K'\) interrupteurs d'une cellule, \(v_K\),
\(i_K\) en convention récepteur ; \(u\) tension appliquée à la charge, \(i\) son courant, \(i_e\) courant de la source ;
\(\alpha\), \(T\), \(f_{\text{déc}}\) ; \(\langle x\rangle\) moyenne, \(U\) efficace ; pont : bras \(K_1, K_1'\)
(point A) et \(K_2, K_2'\) (point B), \(u = v_A - v_B\), \(T_1\), \(D_1\)… ; redresseur : \(v = V\sqrt2\sin\theta\),
\(u_s\), \(D_1, D_2\) à cathodes communes, \(D_1', D_2'\) à anodes communes ; quadrants dans le plan \((u, i)\) de la
charge, comme `triphase` §1. f.é.m. de la machine : \(E_m = k\Omega\).

**Divergences signalées (autres chapitres, non modifiés)** : `mcc` note \(E\) la f.é.m. (ici \(E_m\), pour garder \(E\)
à la source comme en 2ᵉ année ; dit dans le texte au §3) ; `hacheurs` note \(U_e\), \(U_s\), \(\langle U_C\rangle\)
et numérote le pont \(T_1\) à \(T_4\) (\(T_1\), \(T_3\) en haut) au lieu des bras \(K_1, K_1'\) / \(K_2, K_2'\) de
`triphase` (signalé dans une notice du §8). `hacheurs` §3 appelle « cellule de commutation réversible en courant »
un transistor avec sa diode antiparallèle, qui est un **interrupteur** (la cellule en compte deux) : à corriger lors
d'une reprise de ce chapitre.

## Doutes
- Durées de commutation notées \(t_f\) (fermeture) et \(t_o\) (ouverture) plutôt que \(t_{on}\), \(t_{off}\), pour ne
  pas les confondre avec \(t_{on} = \alpha T\) du chapitre « Les hacheurs ». Le modèle \(\tfrac12 EI(t_f + t_o)f\)
  (charge inductive) est donné comme ordre de grandeur ; l'exercice 10 (charge résistive) le présente comme majorant.
- « Étude structurelle des convertisseurs à deux ou trois cellules » : interprétée comme pont monophasé (deux
  cellules) et triphasé (onduleur à trois bras, PD3) ; le triphasé n'est donné que par sa structure, ses formes
  d'onde restant en 2ᵉ année.
- La MLI est donnée comme idée (moyenne glissante \((2\alpha - 1)E\)) ; le fondamental \(mE/\sqrt2\) n'est cité
  qu'en ordre de grandeur, marqué 2ᵉ année.
- Le gradateur reste dans le tableau des familles (marqué hors programme), comme dans `triphase`.
