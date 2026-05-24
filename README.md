# Révisions PTSI

Site de révisions personnel pour la prépa **PTSI** (Physique–Chimie, Maths, Sciences de l'ingénieur).

Application web statique, **mono-fichier** (`index.html`) : tout le HTML, le CSS et le JavaScript sont inline. Aucune étape de build, aucune dépendance à installer — il suffit d'ouvrir le fichier dans un navigateur.

## Fonctionnalités

- **61 chapitres** organisés par matière et sous-domaine.
- Onglets par chapitre : **Cours**, **Méthodes**, **Simulateur** (12 chapitres), **Flashcards**, **Exercices**.
- **Flashcards** avec suivi de progression (acquis / hésitant / à revoir), sauvegardé localement (`localStorage`).
- **Simulateurs** interactifs en Canvas (RLC, filtres, optique, oscillateurs, MCC, hacheurs, intégrales, etc.).
- **Recherche** globale (cours + formules + encadrés).
- **Quiz** global multi-chapitres.
- **Thème clair / sombre**.
- **Version mobile** (menu tiroir) et **mode impression** par chapitre.
- Formules mathématiques rendues avec **MathJax**.

## Chapitres présents

### Physique–Chimie (26)
Ondes & signaux, électrocinétique (RLC, filtres), optique géométrique & ondulatoire, mécanique du point (cinématique, dynamique, énergétique, moment cinétique, champ central, Lorentz), oscillateurs, thermodynamique (introduction, 1er et 2e principes, machines, changements d'état), fluides (statique, dynamique), induction, électromagnétisme, chimie (cinétique, équilibres, oxydoréduction, équilibres acido-basiques).

### Maths (20)
Logique & ensembles, géométrie de l'espace, nombres complexes, fonctions réelles, suites, polynômes, dénombrement, variables aléatoires, probabilités, analyse asymptotique, séries numériques, déterminants, matrices, espaces vectoriels, applications linéaires, primitives, intégrales, continuité & dérivabilité, dérivation & DL, équations différentielles.

### Sciences de l'ingénieur (15)
Électrotechnique (MCC, convertisseurs statiques, hacheurs), capteurs, mécanique (cinématique, statique, transmission de puissance, dynamique du solide, énergétique), automatique (schéma-blocs, systèmes 1er/2e ordre, stabilité, précision/PID, SLCI).

## Lancer le site

- **En ligne** : voir GitHub Pages (lien dans les paramètres du dépôt).
- **En local** : ouvrir `index.html` dans un navigateur (double-clic).

> ⚠️ **Hors-ligne** : MathJax et les polices sont chargés depuis un CDN. Sans connexion, les formules du cours s'affichent en texte brut et les polices retombent sur une police système. Les flashcards (caractères Unicode) restent lisibles.

## Ajouter un nouveau chapitre

Les conventions détaillées sont dans [`CLAUDE.md`](CLAUDE.md). En résumé :

1. **Déclarer le chapitre** dans le tableau `CHAPTERS` (JS) : `id`, `prefix`, `name`, `matiere`, `sub`, `subLabel`, `domain`, `matiereLabel`, `panels`, `drawFn`, `mobLabel`.
2. **Ajouter le bouton** de navigation `.chap-btn` (avec `data-chap="<id>"`) dans la bonne `.chapter-bar`.
3. **Créer le bloc** `<div class="chapter" id="chap-<id>">` avec sa `<nav class="tabs">` et ses `<section class="panel" id="<prefix>-<panel>">`.
4. **Définir les flashcards** : `const <prefix>Cards = [{q:"…", a:"…"}, …]` puis `makeFlash(...)`.
5. La fonction `validateChaptersCoherence()` signale dans la console toute incohérence entre `CHAPTERS` et le DOM au chargement.
