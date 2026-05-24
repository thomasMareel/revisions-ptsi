# Révisions PTSI

Fichier de révisions pour la 1ère année de classe préparatoire PTSI.  
Hébergé sur GitHub Pages : https://thomasmareel04.github.io/revisions-ptsi/

## Ce que contient ce projet

Un fichier HTML monolithique (`index.html`) qui regroupe :
- **56 chapitres** répartis en 3 matières : Physique, Maths, Sciences de l'Ingénieur
- Pour chaque chapitre : onglets Cours / Méthodes / Flashcards / Exercices
- Simulateurs interactifs (canvas) pour certains chapitres
- Recherche plein-texte dans tous les chapitres
- Quiz global multi-chapitres
- Thème clair / sombre
- Version mobile (responsive)
- Mode impression

## Chapitres présents

### Physique (26 chapitres)

**Ondes & signaux :**
- Ondes mécaniques (`chap-ondes`)
- Magnétostatique (`chap-emag`)
- Électrostatique et magnétostatique (`chap-estat`)
- Signaux périodiques et Fourier (`chap-signaux`)
- Circuit RLC série (`chap-rlc`) — avec simulateur
- Filtres du 1er et 2e ordre (`chap-filtres`) — avec simulateur
- Optique géométrique (`chap-optique`) — avec simulateur
- Optique ondulatoire (`chap-optiqued`)
- Oscillateurs harmoniques (`chap-oscill`) — avec simulateur
- Particules chargées — Lorentz (`chap-lorentz`)
- Induction électromagnétique (`chap-induction`)

**Mécanique :**
- Cinématique du point (`chap-cinept`)
- Dynamique et énergétique du point (`chap-mecpt`)
- Moment cinétique (`chap-mcinc`)
- Mouvement dans un champ central (`chap-chcentral`)
- Statique des fluides (`chap-fluides`)
- Dynamique des fluides (`chap-fluiddyn`)

**Thermodynamique :**
- Introduction thermodynamique (`chap-thermo1`)
- 1er principe (`chap-thermo2`) — avec simulateur
- 2e principe (`chap-thermo3`)
- Machines thermiques (`chap-machines`)
- Changements d'état (`chap-changement`)

**Chimie :**
- Cinétique chimique (`chap-cinetique`)
- Équilibres chimiques (`chap-equilchim`)
- Oxydoréduction (`chap-oxred`) — avec simulateur
- Diagrammes E-pH (`chap-eph`)

### Maths (20 chapitres)

Logique · Géométrie · Complexes · Fonctions · Suites · Polynômes · Variables aléatoires · Dénombrement · Probabilités · Analyse asymptotique · Séries numériques · Déterminants · Calcul matriciel · Espaces vectoriels · Applications linéaires · Primitives · Intégrales · Continuité & dérivabilité · Dérivation & DL · Équations différentielles

### Sciences de l'Ingénieur (16 chapitres)

**Électrotechnique :** Machine CC · Convertisseurs statiques · Hacheurs  
**Mécanique :** Capteurs · Cinématique · Statique · Transmission · Dynamique du solide · Énergétique  
**Automatique :** Schéma-blocs · Systèmes 1er ordre · Systèmes 2e ordre · Stabilité · Précision PID · SLCI

## Comment ajouter un nouveau chapitre

1. **Déclarer le chapitre** dans le tableau `CHAPTERS` (vers la ligne 24970 du fichier) :
   ```js
   { id:'mon-chap', prefix:'mc', name:'Mon chapitre',
     matiere:'maths',   // 'physique', 'maths' ou 'si'
     sub:null,          // sous-domaine physique : 'ondes','meca','thermo','chimie' ; null pour maths
     subLabel:'Algèbre',
     domain:'maths',    // domaine pour la couleur : 'ondes','meca','thermo','chimie','maths','elec','auto'
     matiereLabel:'Algèbre',
     panels:['cours','meth','flash','exos'],  // ajouter 'simu' si simulateur
     drawFn:null,       // nom de la fonction de dessin si simulateur, sinon null
     mobLabel:'Mon chap' }
   ```

2. **Ajouter le bouton de navigation** dans la `.chapter-bar` correspondante :
   ```html
   <button class="chap-btn" data-chap="mon-chap">Mon chapitre</button>
   ```

3. **Ajouter le bloc HTML du chapitre** dans le bon `<main>`, en suivant la structure standard (voir CLAUDE.md).

4. **Tester** en ouvrant `index.html` localement ou sur GitHub Pages.

## Stack technique

- HTML / CSS / JS vanilla (zéro dépendance npm)
- MathJax v3 via CDN (formules LaTeX)
- Google Fonts via CDN (Fraunces, Inter Tight, JetBrains Mono)
- GitHub Pages pour l'hébergement

> ⚠ Les formules mathématiques nécessitent une connexion internet (MathJax chargé via CDN).
