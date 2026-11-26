# Historique des chantiers de contenu

Ce fichier reçoit l'historique détaillé des chantiers de contenu, retiré de `CLAUDE.md` le 2026-11-26 : ce qui a été écrit, corrigé, créé ou renommé, avec les dates et les comptes rendus. Les règles qui en sont issues (format des cours, hors-programme, notations communes) sont dans `CLAUDE.md` › « Rédaction des contenus » : elles y font foi. Les comptes cités (chapitres, cartes, sections) sont ceux de la date indiquée. Un nouveau chantier ajoute ici sa section (dates, chapitres, comptes rendus) ; sa règle, s'il en crée une, va dans `CLAUDE.md`.

Sommaire :
- Cours vidéo
- Chapitres, groupes et tags
- Automatique (SI, 2026-11-12)
- Cours de 2ᵉ année (2026-11-13 → 2026-11-16)
- Électromagnétisme de 1ʳᵉ année (2026-11-19)
- 1ʳᵉ année : audit de novembre 2026 (points 1 à 4, lots 1 à 8)
- Point 7 de l'audit : format de la 2ᵉ année pour la 1ʳᵉ année (lots 9 et 10)
- Informatique (point 5 de l'audit)
- Anglais (point 8 de l'audit)
- Comptes rendus et consignes

## Cours vidéo

Depuis novembre 2026, le dépôt porte aussi la fabrication des **cours vidéo « prof au tableau »** (tableau noir Manim, voix de synthèse Camille de Mistral, sous-titres) et les sources LaTeX des cours PDF associés. **Mode d'emploi complet : `video/README.md`** (choix validés par l'utilisateur, étapes, règles d'écriture, contrôles) ; mise en ligne : `video/YOUTUBE.md`. Depuis le chapitre 4 (demande de l'utilisateur du 2026-11-11) : voix plus dynamique (`"expressivite": 3.0`, `"tempo": 1.0` dans `chapitre.json`, texte écrit sur un ton vivant). **Format de toutes les vidéos à venir (demande de l'utilisateur du 2026-11-16, à partir du cours de RdM)** : cours **condensé** (≈ 25-30 %, 3 min environ) puis **une vraie partie de résolution d'exercices** (≈ 70 % : 2 ou 3 exercices inventés de difficulté croissante, énoncé, « À vous » avec pause, étapes justifiées à l'oral, vérification), « Ce qu'il faut retenir » = la méthode ; 10 à 13 min (détail : `video/README.md` › « Format »).

- Indépendant du site : rien dans `video/` n'est chargé par `index.html` ni mis en cache par `sw.js` (pas de bump de `CACHE_VERSION` pour un changement limité à `video/`).
- **Environnement cloud dédié « revisions-ptsi »** (créé le 2026-11-11) : il porte le secret réseau Mistral et les variables YouTube ; une session vidéo doit tourner dessus (« Default » n'a aucun de ces secrets).
- Avant tout travail vidéo : `bash video/installer.sh` (outils + contrôle de l'accès à la voix).

- En ligne : thermochimie complète, chapitres 1 à 8 ; matrices, chapitre 1 (1ʳᵉ année) et chapitres 2 à 4 (2ᵉ année) ; automatique (`video/slci/`, une vidéo par chapitre du groupe Automatique sauf `sysnum`), chapitres 1 à 8 : automatique complète ; résistance des matériaux (`video/rdm/`, 3 vidéos au nouveau format, 2026-11-16) ; électromagnétisme de 2ᵉ année (`video/em/`, une vidéo par chapitre, 2026-11-16) (tableau « Vidéos livrées » de `video/README.md`, onglet « Vidéos » des chapitres `thermochimie`, `matrices`, `matrices2a`, `slci`, `schblocs`, `sys1`, `sys2`, `bode`, `stabilite`, `precision`, `correcteurs`, `rdm`, `estat2a`, `magnetostat`, `maxwell`, `oemvide`, `oemcond`).
- **Intégration au site : onglet « Vidéos »** des chapitres (depuis le 2026-11-11 : `thermochimie` et `matrices` ; le 2026-11-12 : `matrices2a` et les sept chapitres d'automatique de 1ʳᵉ année ; le 2026-11-13 : `correcteurs` ; le 2026-11-16 : `rdm` et les chapitres d'électromagnétisme de 2ᵉ année ; entre Cours et Méthodes).
- Tableau tenu à jour : `video/README.md` › « Vidéos livrées ». Fonctionnement de l'onglet : `docs/interface.md` › « Onglet Vidéos ».

## Chapitres, groupes et tags

Juste après `CHAPTERS`, l'IIFE `reorderChapters` déclare **`CHAP_GROUPS`** (`grep -n 'const CHAP_GROUPS'`) = `[ [subCode, subLabel, [ids…]] , … ]` (30 groupes, dont `['capteurs', 'Chaîne d\'information', ['capteurs','reseaux']]` — groupe renommé le 2026-11-14 à la création de `reseaux` « Réseaux de communication », prefix `rsx`, 1ʳᵉ année — puis `['ia', 'Intelligence artificielle', ['ia']]` en SI) : **source unique** de l'ordre pédagogique, des **sous-domaines** (`c.sub`) et de leurs **libellés** (`c.subLabel`), qu'il réécrit en réordonnant `CHAPTERS` en place. `subCode` à `null` = pas de code de sous-domaine (maths ; le `subLabel` groupe quand même le tiroir). Un `id` absent est rejeté en fin de liste. **Pour changer l'ordre ou le sous-domaine : éditer `CHAP_GROUPS`**. ⚠️ `matiereLabel` (tag) et `domain` (`data-domain`, alias de compatibilité) ne sont **pas** réécrits : les tenir à la main en cohérence (ex. `lorentz` porte encore le tag « Mécanique » dans le groupe Électromagnétisme). Tags ajoutés avec la PT spé : « Électronique » (ali, oscelec, signum, groupe Ondes & signaux), « Thermochimie » (thermochimie, fin du groupe Chimie, 2ᵉ année), « Résistance des matériaux » et « Conception » (SI Mécanique), « Intelligence artificielle » (ia) ; le chapitre SI `ia` a `domain:'info'`. Le code `'meca'` sert en physique ET en SI. Les couleurs ne dépendent plus de `domain` mais de `matiere` (`data-mat`).

Les 26 chapitres de PT spé ajoutés le 2026-10-04 sont listés en fin de `CHAPTERS`, de `__YEAR2A` et des decks (voir `docs/interface.md` › « Années »).

## Automatique (SI, 2026-11-12)

- **Automatique (SI, réorganisée le 2026-11-12)** : groupe `auto` = `slci` (« SLCI : modélisation et transformée de Laplace », chapitre d'entrée), `schblocs`, `sys1`, `sys2`, `bode` (« Réponse fréquentielle et diagrammes de Bode », créé ce jour-là), `stabilite`, `precision` (« Performances : précision et rapidité »), `sequentiel` (« Systèmes séquentiels : diagrammes d'états et programmation », prefix `seq`, 1ʳᵉ année, créé le 2026-11-14), puis en 2ᵉ année `correcteurs`, `sysnum` et `resnum` (résolution numérique, créé le 2026-11-13).
- Cours de 1ʳᵉ année réécrits (figures SVG calculées : réponses, abaque du temps de réponse, Bode, marges) ; notations communes : ξ (amortissement), ω₀, ω_c0 (coupure à 0 dB de la FTBO), Mφ, M_G, écart ε.
- Le deck `slci` reste un deck de synthèse (cartes d'origine conservées, cartes de Laplace ajoutées).

## Cours de 2ᵉ année (2026-11-13 → 2026-11-16)

### Format et inventaires

- **Cours de 2ᵉ année (réécriture commencée le 2026-11-13)** : chaque cours réécrit commence par un bloc « AU PROGRAMME · PT » (sec-num sans §, `.reveal` « Programme officiel » listant les capacités exigibles du programme 2021, renvoyant aux §) ; le hors-programme est regroupé en fin de cours (« POUR ALLER PLUS LOIN · … »).
- Inventaire programme ↔ chapitres et état d'avancement : `docs/programme-pt/physique-chimie.md` (physique-chimie, terminée), `docs/programme-pt/mathematiques.md` (maths, terminée), `docs/programme-pt/sciences-industrielles.md` (SI, terminée), `docs/programme-pt/informatique.md` (informatique commune, terminée le 2026-11-21).

### Physique-chimie (terminée le 2026-11-13)

- Chapitres créés à cette occasion (physique-chimie, réécriture terminée le 2026-11-13) : `magnetostat` (« Magnétostatique : théorème d'Ampère », prefix `mgs`, après `emag`), `fluidstat` (« Statique des fluides : pression et poussée d'Archimède », `fst`, après `fluides`), `thermodiff` (« Thermodynamique différentielle et fluides réels », `tdf`, après `changement` ; diagrammes calculés avec CoolProp), `electrochimie` (« Électrochimie : courbes courant-potentiel, électrolyse, corrosion », `ech`, après `thermochimie`) ; `estat2a` renommé « Électrostatique : champ, potentiel, théorème de Gauss ».
- Les chapitres courts de 1ʳᵉ année d'avant la réforme 2021 sont gardés : `estat` et `fluides` en « aperçu » de la 2ᵉ année ; `emag` (« Champ magnétique et actions de Laplace ») et `changement` (« Corps pur diphasé et changements d'état ») renommés le 2026-11-15, leur encadré disant ce qui est exigible en PTSI.

### Maths (terminée le 2026-11-13)

- **Maths** (réécriture terminée le 2026-11-13) : les 25 cours courts de 2ᵉ année réécrits au même format (rédigés par des sous-agents d'après `p2a/maths/CONSIGNES.md` et `PERIMETRES.md` du scratchpad, non versionnés) ; `matrices2a`, `conred` et `surfaces` complétés ; `coniques` renommé « Courbes du plan et coniques » (courbes d'équation f(x, y) = 0 en tête), `geoplane` renommé « Propriétés métriques des courbes planes » (enveloppes, développée) ; `suites2a` et `integ2a` = outils de 1ʳᵉ année réinvestis (pas de section propre au programme de PT) ; `geo3d` « Géométrie dans l'espace » est passé en **1ʳᵉ année** le 2026-11-21 (partie B du programme de PTSI, après `geometrie` devenu « Géométrie du plan »).
- Méthodes, exercices et cartes des 42 chapitres de maths et de SI de 2ᵉ année relus et harmonisés le 2026-11-14 (6 à 10 méthodes, 7 à 10 exercices dont un « Concours PT », cartes ajoutées, hors-programme signalé : en tête de la réponse d'une carte, « Hors programme en PT (pour aller plus loin) : », question inchangée).

### SI (2026-11-13)

- **SI** (2026-11-13) : les 11 cours de 2ᵉ année complétés (encadré « Au programme », manques comblés, hors-programme en fin de chapitre : `correcteurs` « anticipation et PID », démonstrations de Ferraris et de Park dans `machalt`, compléments d'`ia`) ; trois chapitres créés : `energ2a` « Énergétique des systèmes de solides » (prefix `en2`, après `dyn2a`), `resnum` « Résolution numérique en sciences de l'ingénieur » (`rnum`, groupe Automatique après `sysnum`, tag « Ingénierie numérique »), `chfonc` « Chaînes fonctionnelles : choisir et dimensionner les composants » (`chf`, groupe Analyse système après `multiphy`).
- Figures calculées en Python (scripts dans le scratchpad de la session, non versionnés).

### Électromagnétisme de 2ᵉ année (2026-11-16)

- **Électromagnétisme de 2ᵉ année revu le 2026-11-16** (demande de l'utilisateur : « au top de la qualité ») : `estat2a`, `magnetostat`, `maxwell`, `oemvide`, `oemcond` relus et corrigés, 10 méthodes et 10 à 12 exercices (dont un « Concours PT ») par chapitre, cartes complétées ; modèle de Drude, plasma et polarisation circulaire hors programme (fin de chapitre ou signalés) ; guide d'onde à deux plans : cité par le préambule du programme, sans capacité détaillée ; notations \(I_{\text{enlacé}}\), σ (conductivité), 𝓜 (moment magnétique) ; comptes rendus dans `docs/revue-em-2026-11/`.

## Électromagnétisme de 1ʳᵉ année (2026-11-19)

- **Électromagnétisme de 1ʳᵉ année revu le 2026-11-19**, au même niveau : `emag` (12 sections, 11 figures, champ tournant et boussole, couple sur un cadre ; Biot et Savart, Ampère, H et réluctance en « Pour aller plus loin »), `induction` (11 sections, 8 figures : Faraday en convention générateur, Lenz, L, M, circuits couplés, transformateur, rails, spire tournante, Foucault, moteur à courant continu, haut-parleur), `lorentz` (8 sections, 7 figures : champ E, champ B, miroir électrostatique, cyclotron, filtre de Wien ; hélice hors programme), chacun avec le bloc « AU PROGRAMME · PTSI », 10 méthodes, 12 exercices dont un « Concours PT », 39 à 40 cartes ; `estat` reste un **aperçu** de la 2ᵉ année (encadré « non exigible en PTSI », 5 sections, 6 méthodes, 8 exercices, sans bloc programme).
- Notations alignées sur la 2ᵉ année (\(\vec{\mathcal M}\), \(\vec\Gamma\), \(U_m\) pour l'énergie magnétique).
- Comptes rendus : `docs/revue-em-2026-11/{emag,ind,lor,es}-revue.md`.
- Règle retenue pour les figures (vecteurs en gras dans les SVG) : `CLAUDE.md` › « Rédaction des contenus ».

## 1ʳᵉ année : audit de novembre 2026 (points 1 à 4, lots 1 à 8)

Plan d'action et annexes : `docs/audit-2026-11.md`, `docs/audit-2026-11/` (corrections et notations par matière).

### Points 1 à 3 (2026-11-15)

- **1ʳᵉ année corrigée le 2026-11-15** (points 1-2 de `docs/audit-2026-11.md`) : hors-programme signalé sur place, par un encadré « Hors programme en PTSI (vu en 2ᵉ année) » ou « (pour aller plus loin) », par le titre de la méthode ou de l'exercice, ou par le préfixe de la réponse d'une carte.
- Point 3 : notations communes harmonisées le 2026-11-15 ; liste en vigueur dans `CLAUDE.md` › « Rédaction des contenus ».

### Point 4 : grands manques comblés (lots 1 à 8, 2026-11-21 → 2026-11-22)

- **Grands manques de la 1ʳᵉ année comblés, lot 1 (2026-11-21, point 4 de `docs/audit-2026-11.md`)** : chapitres créés `incertitudes` « Mesures et incertitudes » (physique, prefix `inc`, partie Référence avant `constantes` ; types A et B, composition, Monte-Carlo en Python, écart normalisé, régression) et `liaisons` « Liaisons, graphe et schéma cinématique » (SI, prefix `lia`, Mécanique entre `cine` et `statique` ; 11 liaisons, symboles, torseurs cinématiques et transmissibles 3D, graphe, schéma, liaisons équivalentes, mobilité, hyperstatisme \(h = m - I_c + 6\gamma\) comme `chaines`) ; `geometrie` réécrit en « Géométrie du plan » ; `changement` réécrit (diagramme (P, v) calculé, titre et règle des moments, \(\Delta s_{12} = \Delta h_{12}/T\), sans renvoi à tort en 2ᵉ année) ; `thermo1` complété (gaz réels, Amagat).
- Comptes rendus : `docs/revue-1a-2026-11/`.
- Rédacteurs : consignes `p2a/an1/CONSIGNES-1A.md` du scratchpad (non versionnées).
- **Lot 2 (2026-11-21)** : `cotation` réécrite sur la spécification GPS 2021 (principes, modèles, zones, références, ajustements ; chaîne de cotes et ISO 286 hors programme) ; `applin` et `matrices` complétés (rang, base adaptée, théorème du rang géométrique, équations linéaires, symétries, matrices élémentaires, changement de base \(P_{\mathcal B\to\mathcal B'}\) comme `matrices2a`, matrices semblables ; Cramer hors programme) ; `integrales` (définition par les fonctions en escalier, rectangles et trapèzes, Taylor-Lagrange, valeurs complexes) et `series` (comparaison série-intégrale ; d'Alembert, séries alternées, semi-convergence en « Pour aller plus loin ») ; probabilités restructurées sans recouvrement — `denombrmt` (dénombrement seul), `proba` (univers fini, conditionnement, indépendance mutuelle, coalitions), `va` renommé « Variables aléatoires sur un univers fini » (lois U, B, binomiale, conditionnelles, couples, E(X), V(X), Bienaymé-Tchebychev) ; σ-additivité, lois géométrique, de Poisson et hypergéométrique en « Pour aller plus loin ».
- **Lot 3 (2026-11-21)** : `ingsys` réécrit et renommé « Ingénierie système : besoin, exigences, architecture » (diagrammes SysML uc, req, bdd, ibd, stm dessinés, exigences quantifiées, cycle de vie et ACV, chaînes de puissance et d'information ; vocabulaire APTE hors programme) ; `statique` complétée (modèle local, passage au global, glisseur et couple, torseurs transmissibles 3D, modèle plan, frottement visqueux, roulement, pivotement, arc-boutement ; PFS énoncé sans « si et seulement si » ; travaux virtuels hors programme) et `cine` alignée sur `liaisons` (\(n_c\), pas \(p_h\)) ; `ondes` renommé « Propagation d'un signal et interférences » (partie 1.6 : interférences à deux ondes ; d'Alembert, ondes stationnaires et Doppler en « Pour aller plus loin ») et `optiqued` (Young au programme) ; `contderiv`, `asympt`, `dl` sans recouvrement, dans cet ordre (`dl` renommé « Développements limités » ; limite de la dérivée, \(\mathcal C^k\), Leibniz, Taylor ; convexité, Jensen, Heine en « Pour aller plus loin »).
- **Lot 4 (2026-11-21)** : `calculs` « Calculs algébriques et arithmétique » créé (maths, prefix `calc`, après `logique` dans la partie renommée « Logique et calculs » ; Σ, Π, inégalités, partie entière, arithmétique dans ℕ ; Bézout, Gauss, congruences en « Pour aller plus loin ») ; `fonctions` réécrit (th, Argsh, Argch hors programme) ; `regimecontinu` (ARQS, mesures ; Norton, Millman hors programme), `premierordre` (RC, RL, énergie, Euler) ; `acidobase` (réaction prépondérante, titrages ; formules de pH en « Pour aller plus loin ») et `precipitation` (pS = f(pH), complexation hors programme) ; `cvs` (cellule de commutation, onduleur, redresseur ; redresseur commandé hors programme).
- **Lot 5 (2026-11-22)** : `cinept` et `mecpt` (renommé « Principes de la dynamique : lois de Newton » ; composition des vitesses et Coulomb vues en SI, en « Pour aller plus loin » ; Euler avec la même fonction `euler` que `pynum` et `premierordre`) ; `machines` (une seule convention : énergies reçues par le fluide, \(T_C\), \(T_F\), \(Q_C\), \(Q_F\), \(\eta_C\), \(e_{PAC}\) ; cycles calculés avec CoolProp ; simulateur et deux exercices de `thermo2`/`thermo3` alignés) et `cristallin` (maille primitive ou conventionnelle, sites de la CFC, figures 3D) ; `ev` et `det` (caractérisation du déterminant ; comatrice, Cramer, formes multilinéaires en « Pour aller plus loin » ; partie Algèbre linéaire réordonnée : `matrices`, `ev`, `applin`, `det`) ; `moulage` renommé « Moulage : fonderie, injection plastique et composites » et `addfab` « Fabrication additive » (règles de conception ; frittage hors programme).
- Dans la marge, les noms de formule (`data-nom`) sont coupés à la syllabe (`hyphens:auto`).
- **Lot 6 (2026-11-22)** : `mcinc` (point et systèmes discrets), `mvtsolide` (solide en rotation, seul tableau des moments d'inertie, Huygens-Steiner en « Pour aller plus loin », non-isochronisme du pendule pesant en Python) et `chcentral` (Kepler, satellites, trajectoires calculées avec `odeint`) sans recouvrement ; notations \(\mathcal M\), \(\Gamma\), \(L_z = mC\) ; `energie` (pendule aux grandes amplitudes, portrait de phase) et `oscill`, exposé de référence de l'oscillateur amorti (Q, ω₀, τ = 2Q/ω₀, résonance) ; `atome` recentré sur le tableau périodique (nombres quantiques, Klechkowski en « Pour aller plus loin ») et `equilchim` (état final en Python ; Le Chatelier, Van 't Hoff, K_c/K_p hors programme ; placé avant `cinetique`) ; `logique` (𝒫(E), partitions, applications, analyse-synthèse ; relations d'équivalence et d'ordre en « Pour aller plus loin ») et `polynomes` (Horner, Taylor ; PGCD, Bézout, Lagrange hors programme).
- **Lot 7 (2026-11-22)** : `signaux` renommé « Signaux périodiques et spectres » (calcul des coefficients de Fourier hors programme) et `filtres` « Régime sinusoïdal forcé et filtrage linéaire » (socle des impédances, associations et diviseurs en un seul endroit, §1 à §3 ; simulation d'un filtre en Python ; `rlc` y renvoie) ; `cinetique` (méthodes différentielle et intégrale en Python, Arrhenius ; mécanismes hors programme) et `molecules` (géométrie donnée par l'énoncé, VSEPR et mésomérie en « Pour aller plus loin ») ; `primitives` et `edo` (cadre complexe, stabilité, Euler ; Lagrange, wronskien en « Pour aller plus loin ») ; `deform` renommé « Mise en forme par déformation et découpage » et `assemblage` « Assemblages : soudage, rivetage, collage, vissage » (règles de conception, encadré « Vu en avance (2ᵉ année) »).
- **Lot 8 (2026-11-22)** : `optgeo` et `optique` (renommé « Optique géométrique — Lentilles minces, œil et appareil photographique » ; microscope non afocal ; lunette et microscope = exemples non exigibles ; prisme en « Pour aller plus loin ») ; `rlc` (impédances et notation complexe renvoyées à `filtres` §1-§3, notations de `oscill` : \(\omega_p\), τ = 2Q/ω₀ ; simulation `odeint`/Euler ; ses panneaux restent dépliés) et `thermo3` renommé « Deuxième principe : bilans d'entropie » (expressions de S fournies, identités thermodynamiques en « Pour aller plus loin ») ; `complexes` (similitudes hors programme, trigonométrie renvoyée à `fonctions`) et `suites` (sommes renvoyées à `calculs`, seuil et vitesse de convergence en Python) ; `dynsolide` et `energsi`, introductions « Vues en avance (2ᵉ année) » sans recouvrement, placées avant `dyn2a` et `energ2a`.

## Point 7 de l'audit : format de la 2ᵉ année pour la 1ʳᵉ année (lots 9 et 10)

- **Point 7 de l'audit (format de la 2ᵉ année pour les chapitres de 1ʳᵉ année déjà corrects), lot 9 (2026-11-26)** : `thermo2` renommé « Premier principe : bilans d'énergie » (§1-§6 gardés, bilans sur un chemin, calorimétrie, premier principe en puissance ; Joule-Thomson et polytropiques en « Pour aller plus loin ») ; `sys1`, `sys2`, `bode`, `stabilite`, `precision` (bloc « AU PROGRAMME · PTSI », § existants gardés pour les vidéos, nouvelles sections à la suite ; identification, réponses impulsionnelle et à une rampe, Euler ; facteur de résonance \(Q_r\), \(Q\) restant le facteur de qualité ; temps de réponse \(t_{r5\%}\) ; Routh complet, Nyquist et Black hors programme).
- Consignes des rédacteurs : `p2a/an1/CONSIGNES-POINT7.md` du scratchpad (non versionnées).
- **Lot 10 (2026-11-26, fin du point 7)** : `slci` et `schblocs` (§1-§5 gardés, §6-§8 ajoutés ; linéarisation, transformée inverse, pôle dominant signalés hors programme ; effet de charge, perturbation), `oxred` (électrodes de référence, prédominance, état final, dismutation, titrages ; électrolyse et ΔrG° en fin de chapitre) et `eph` (construction du diagramme du fer, dismutation du chlore, Winkler), `mcc` et `hacheurs` (modèle électromécanique et commande « vus en avance », programme de SI S4 ; ondulation, MLI, association hacheur-moteur ; `hacheurs` garde \(T_1\) à \(T_4\), source \(E\), f.é.m. \(E_m\)).
- Les aperçus `fluides`, `fluiddyn`, `estat` étaient déjà au format (encadré « non exigible en PTSI »).

## Informatique (point 5 de l'audit)

**Contenu (programme d'informatique commune 2021, chantier du 2026-11-19 au 2026-11-21, point 5 de l'audit)** : 17 chapitres (14 de 1ʳᵉ année ; `sql`, `progdyn`, `iajeux` en 2ᵉ année) en cinq parties de `CHAP_GROUPS` — `prog` Programmation (`pybases`, `pyctrl`, `pyfonc`, `pytypes`), `algo` Algorithmique (`pyanalyse` « Spécification, correction et complexité », chapitre de référence de ces notions, `pydicho`, `pyrec`, `pytri`, `pyglouton`, `progdyn`), `numinfo` Nombres et calcul numérique (`pyrepr`, `pynum`, recentré sur le programme d'informatique avec renvois aux capacités numériques de physique, de maths et de SI), `donnees` Données (`pyfichiers`, `pyimages`, `sql`), `graphia` Graphes et IA (`graphes`, `iajeux`) ; chaque cours commence par un bloc « AU PROGRAMME · INFORMATIQUE », tout le code affiché a été exécuté et testé, et l'annexe Python du programme est limitative (ce qui en sort est documenté sur place).

Inventaire et répartition des notions : `docs/programme-pt/informatique.md` ; comptes rendus : `docs/revue-info-2026-11/`.

Rendu des cartes d'informatique (`flashInfoHTML`) : `CLAUDE.md` › « Pilotage data-driven » ; correctif de `flashPretty` du 2026-11-19 : `docs/interface.md` › « Cartes d'anglais et d'informatique ».

## Anglais (point 8 de l'audit)

**Point 8 de l'audit (2026-11-26)** : les 18 paquets étoffés (≈ 270 → 552 cartes, réponses fausses corrigées, comptes rendus `docs/revue-anglais-2026-11/`) ; chapitre `ensynth` « Synthèse de documents : l'épreuve écrite » (prefix `ensy`, partie « Épreuve écrite » de `CHAP_GROUPS`, onglets Cours, Méthodes, Cartes, Exercices : méthode de la synthèse de la Banque PT, deux dossiers inventés avec synthèse modèle de 450 à 500 mots, passages anglais en `lang="en"`) ; `endoc` §4-§5 : l'oral d'anglais de la Banque PT.

Le site de la Banque PT n'est pas joignable depuis le conteneur : les détails incertains de l'épreuve renvoient à sa notice et au dernier rapport du jury.

## Comptes rendus et consignes

Comptes rendus versionnés (un fichier par chapitre, `<prefix>-revue.md` en général) :
- `docs/revue-em-2026-11/` : électromagnétisme de 2ᵉ année (2026-11-16) et de 1ʳᵉ année (`emag`, `ind`, `lor`, `es`, 2026-11-19) ;
- `docs/revue-1a-2026-11/` : lots 1 à 10 de la 1ʳᵉ année (2026-11-21 → 2026-11-26) ;
- `docs/revue-info-2026-11/` : informatique (2026-11-19 → 2026-11-21) ;
- `docs/revue-anglais-2026-11/` : anglais (point 8, 2026-11-26).

Inventaires programme ↔ chapitres : `docs/programme-pt/physique-chimie.md`, `mathematiques.md`, `sciences-industrielles.md`, `informatique.md`.

Consignes des rédacteurs (sous-agents), dans le scratchpad des sessions, non versionnées : `p2a/maths/CONSIGNES.md` et `PERIMETRES.md` (maths de 2ᵉ année), `p2a/an1/CONSIGNES-1A.md` (lots 1 à 8), `p2a/an1/CONSIGNES-POINT7.md` (lots 9 et 10). Les scripts Python des figures calculées sont eux aussi restés dans les scratchpads.
