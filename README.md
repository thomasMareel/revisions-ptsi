# Révisions PTSI

Site de révisions personnel pour la prépa **PTSI → PT** (Physique–Chimie, Maths, Sciences de l'ingénieur, Informatique, Anglais) : le programme de 1ʳᵉ année (PTSI) et des chapitres de 2ᵉ année (**PT spé**) en maths, physique et SI.

Application web statique, **mono-fichier** (`index.html`) : tout le HTML, le CSS et le JavaScript sont inline. Aucune étape de build, aucune dépendance à installer pour utiliser le site — il suffit d'ouvrir le fichier dans un navigateur.

## Fonctionnalités

- **160 chapitres** en 5 matières (dont 52 de 2ᵉ année), rangés par sous-domaine dans l'ordre pédagogique ; filtre 1ʳᵉ / 2ᵉ année.
- Onglets par chapitre : **Cours**, **Méthodes**, **Simulateur** (27 chapitres, plus le simulateur de la force de Lorentz), **Flashcards**, **Exercices** corrigés (le plus souvent avec un exercice type « CONCOURS PT »).
- **Flashcards** (160 paquets, 3 749 cartes) avec suivi de progression (acquis / hésitant / à revoir), sauvegardé localement. Tu peux ajouter, retirer ou réordonner des cartes sans perdre ta progression.
- **Répétition espacée** (boîtes de Leitner) : menu « Réviser » → « Révisions du jour », avec un badge du nombre de cartes à revoir.
- **Écran « Aujourd'hui »** au lancement : cartes dues, reprendre là où tu t'étais arrêté, chapitres récents.
- **Quiz** global multi-chapitres (filtrable par matière, par mode, par type de carte : formules / grandeurs usuelles) et **calcul mental**.
- **Tableau de bord « Bilan »** : % de cartes acquises global, par matière et par chapitre, chapitres à renforcer en priorité.
- **Sauvegarde / restauration** de la progression (export/import en `.json`) pour la protéger ou la transférer entre appareils.
- **Recherche** globale (cours, formules, encadrés, flashcards), **formulaire** du chapitre (fiche de synthèse imprimable), **impression** d'un chapitre, **cartes signalées**.
- **Lecture audio** des cartes d'anglais.
- **Navigation** : tiroir des chapitres (filtre, épinglés, récents), boutons précédent/suivant (‹ › et Alt+←/→), liens directs du type `#rlc/cours`.
- **Thème clair / sombre**, taille du texte réglable, version **mobile**.
- Formules mathématiques rendues avec **MathJax**.
- **Application installable (PWA)** : depuis le site en ligne (HTTPS), installable sur téléphone/ordinateur, avec mise en cache pour un fonctionnement hors-ligne et un lancement instantané.

## Chapitres présents

Le tiroir « Chapitres » propose un filtre **1ʳᵉ année / 2ᵉ année** ; l'anglais et la fiche des constantes sont visibles les deux années.

### Physique–Chimie (50, dont 13 de 2ᵉ année)
Ondes & signaux (régime continu, 1er ordre, RLC, signaux, filtres, ondes, optique géométrique et ondulatoire), mécanique (cinématique, dynamique, énergie, oscillateurs, moment cinétique, champ central, solide), thermodynamique (introduction, 1er et 2e principes, machines, changements d'état, fluides), électromagnétisme (électrostatique, magnétostatique, induction, Lorentz), chimie (architecture de la matière, molécules, cristaux, cinétique, équilibres, acido-basique, précipitation, oxydoréduction, diagrammes E-pH), fiche des constantes usuelles. Chapitres de 2ᵉ année : voir « PT spé » ci-dessous.

### Maths (48, dont 28 de 2ᵉ année)
Logique ; algèbre (complexes, polynômes) ; analyse (fonctions, suites, continuité, dérivation & DL, asymptotique, primitives, intégrales, équations différentielles, séries ; en 2ᵉ année : fonctions vectorielles, intégrales généralisées, séries entières, intégrales à paramètre, plusieurs variables…) ; algèbre linéaire (matrices, déterminants, espaces vectoriels, applications linéaires ; en 2ᵉ année : projecteurs, éléments propres, réduction, préhilbertiens, isométries) ; géométrie (dont coniques, courbes paramétrées, géométrie 3D, réduction des coniques, surfaces de l'espace) ; probabilités (dénombrement, probabilités, variables aléatoires, tribus, VA discrètes).

### Sciences de l'ingénieur (36, dont 11 de 2ᵉ année)
Analyse fonctionnelle ; mécanique (cinématique, statique, transmission, dynamique du solide, énergétique) ; automatique (schéma-blocs, systèmes 1er/2e ordre, stabilité, précision/PID, SLCI) ; électrotechnique (machine à courant continu, convertisseurs statiques, hacheurs) ; capteurs ; fabrication (cotation, moulage, déformation plastique, usinage, assemblage, fabrication additive, traitements thermiques et de surface, contrôle non destructif). Chapitres de 2ᵉ année : voir « PT spé » ci-dessous.

### Informatique (8)
Python : bases, représentation des nombres, conditions & boucles, fonctions, types construits, tris, récursivité, méthodes numériques.

### Anglais (18)
Colle / oral (usuels, présenter un document, donner son avis, connecteurs, réagir), vocabulaire thématique, grammaire & traduction (faux-amis, temps, modaux, phrasal verbs), civilisation (UK, US, histoire), idiomes & collocations.

### PT spé (2ᵉ année)
52 chapitres avec cours, méthodes, flashcards et exercices corrigés ; les 26 chapitres ajoutés en octobre 2026 ont en plus chacun un exercice type « CONCOURS PT » (comme 7 des chapitres de maths antérieurs). Ils portent le badge « 2ᵉ année » et apparaissent quand « 2ᵉ année » est choisie dans le tiroir ; le Bilan, le quiz et les boutons chapitre précédent / suivant suivent l'année choisie.

- **Physique (13)** : électronique (amplificateur linéaire intégré et rétroaction, oscillateurs électroniques, échantillonnage et traitement numérique du signal) ; optique ondulatoire (ondes lumineuses et interférences, dispositifs de Young et de Michelson) ; thermodynamique et fluides (diffusion thermique, description d'un fluide en écoulement, écoulements visqueux et bilans en conduite, systèmes ouverts et thermodynamique industrielle) ; électromagnétisme (électrostatique approfondie, équations de Maxwell et ARQS, ondes électromagnétiques dans le vide, ondes électromagnétiques et conducteurs).
- **Maths (28)** : suites, intégration, équations différentielles et séries (compléments) ; fonctions vectorielles, intégrales généralisées, séries entières, intégrales à paramètre, fonctions de plusieurs variables ; algèbre linéaire (compléments sur matrices, déterminants, espaces vectoriels et applications linéaires ; projecteurs et symétries, éléments propres, réduction, espaces préhilbertiens, isométries) ; géométrie (coniques, courbes paramétrées, géométrie plane et dans l'espace, réduction des coniques et matrices symétriques, courbes et surfaces de l'espace) ; probabilités (tribus, espaces probabilisés, variables aléatoires discrètes).
- **Sciences de l'ingénieur (11)** : modélisation multiphysique ; mécanique (chaînes de solides : mobilité et hyperstatisme, conception des liaisons : assemblages et guidages, cinétique et dynamique du solide en 3D, résistance des matériaux) ; automatique (réglage des correcteurs, systèmes numériques : acquisition, filtrage et commande) ; électrotechnique (régimes alternatifs et triphasé, redresseurs et onduleurs ; machines synchrone et asynchrone) ; intelligence artificielle (apprentissage automatique) ; fabrication (triptyque produit–procédé–matériau).

> Les contenus de 2ᵉ année sont **rédigés de façon originale** : les manuels de PT spé de l'étudiant n'ont servi qu'à cerner le programme et les notations (aucun texte, exercice ni schéma n'en est repris).

## Lancer le site

- **En ligne** : <https://thomasmareel.github.io/revisions-ptsi/>.
- **En local** : ouvrir `index.html` dans un navigateur (double-clic).

> ✅ **Fonctionne hors-ligne** : MathJax et les polices sont hébergés en local dans `vendor/` (aucune dépendance CDN). Les formules et la mise en page s'affichent correctement même sans connexion.

## Ajouter un nouveau chapitre

👉 **Modèle prêt à copier-coller : [`GABARIT-CHAPITRE.md`](GABARIT-CHAPITRE.md)** (les 5 endroits à modifier, avec des exemples).

Les conventions détaillées sont dans [`CLAUDE.md`](CLAUDE.md). En résumé, un chapitre se déclare à **5 endroits** de `index.html` :

1. **Déclarer le chapitre** dans le tableau `CHAPTERS` (JS) : `id`, `prefix`, `name`, `matiere`, `sub`, `subLabel`, `domain`, `matiereLabel`, `panels`, `drawFn`, `mobLabel`.
2. **Le placer dans l'ordre** : ajouter son `id` dans `CHAP_GROUPS`, dans le bon groupe (c'est ce qui le range dans le tiroir des chapitres).
3. **S'il est de 2ᵉ année** : ajouter aussi son `id` dans `window.__YEAR2A`.
4. **Créer le bloc** `<div class="chapter" id="chap-<id>">` avec sa `<nav class="tabs">` et ses `<section class="panel" id="<prefix>-<panel>">`, dans le bon `<main>` (`#si-content` pour la SI).
5. **Définir les flashcards** : `const <prefix>Cards = [{q:"…", a:"…"}, …]` puis `makeFlash(...)`, après les autres paquets de cartes.

Il n'y a **pas** de bouton de navigation à écrire : le menu des chapitres est construit automatiquement à partir de `CHAPTERS`.

## Vérifier avant de publier

1. **Le validateur** (quelques secondes, sans dépendance) :
   ```
   python tools/validate.py
   ```
   Il vérifie la cohérence `CHAPTERS` ↔ page, l'absence d'IDs dupliqués, les flashcards câblées, les simulateurs déclarés et les formules mal écrites (`<` collé à une lettre).
2. **La syntaxe du JavaScript** (nécessite Node.js) :
   ```
   python tools/check_js.py
   ```
3. **Les tests navigateur** : voir la section « Tests » ci-dessous (`npm run test:rapide` au minimum).
4. **Le numéro de version** : à chaque modification de `index.html` (ou d'un fichier de `vendor/`, `icons/`…), incrémenter `CACHE_VERSION` en haut de `sw.js` (par ex. `ptsi-cache-v81` → `ptsi-cache-v82`), **dans le même commit**. Sans cela, l'application installée ne propose pas la mise à jour et garde d'anciens fichiers.

## Tests

Une batterie de tests ouvre le site dans un vrai navigateur (Chromium, piloté par Playwright) et vérifie automatiquement chaque chapitre, chaque onglet, les formules, les simulateurs, la version mobile, le quiz, la sauvegarde et le mode hors-ligne. Elle ne modifie jamais `index.html`.

```
npm install                    # une seule fois
npx playwright install chromium  # une seule fois
npm run test:rapide            # version courte (≈ 4 min 30 s)
npm test                       # batterie complète (≈ 12 min)
```

👉 Mode d'emploi complet (installation sous Windows, options, lecture des résultats, que faire en cas d'échec) : **[`tests/README.md`](tests/README.md)**.

## Pour aller plus loin

- [`CLAUDE.md`](CLAUDE.md) : conventions techniques du projet (utilisées par Claude à chaque session).
- [`docs/audit-2026-09.md`](docs/audit-2026-09.md) : audit complet du code (carte du fichier, anomalies connues classées par gravité, pistes d'amélioration).
