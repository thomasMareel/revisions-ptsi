# Un fichier par chapitre — plan (point 6 de l'audit, pistes 3 et 4)

Plan validé par l'utilisateur le 2026-11-27. Document de travail, à tenir à jour à chaque lot.

## 1. Pourquoi

Le contenu des chapitres a doublé entre le 19 et le 26 novembre (points 4, 5, 7 et 8 de l'audit) : `index.html`
est passé de 12 à 23 Mo, dont 20 Mo de contenu replié dans des `<template class="pan-tpl">`. Le repli évite de
construire les éléments, mais le navigateur doit quand même **lire** ces 20 Mo à chaque lancement.

Mesures du 2026-11-27 (téléphone simulé 390 px, processeur ×4, machine du conteneur, plus lente que celle du
19 novembre : seuls les rapports comptent ; scripts dans le scratchpad de la session, `dcl.js`, `autre.js`) :

| Démarrage (page analysée) | Version du 19 nov. (12 Mo) | Actuelle (23 Mo) | Coquille seule (3,1 Mo) |
|---|---|---|---|
| reprise d'un chapitre ordinaire (`#pybases/cours`) | 4,5 – 5,4 s | 7,8 – 9,4 s | **3,6 – 4,2 s** |
| chapitre RLC (1ʳᵉ visite) | 8,7 – 9,3 s | 15,5 – 19,4 s | 12,7 – 15,1 s |

- Le découpage divise par deux le démarrage dans le cas habituel (le site rouvre le dernier chapitre) et
  l'empêche de grossir avec le contenu. Fichier lu au démarrage : 23 → 3,1 Mo (6,3 → 0,85 Mo compressé).
- Il ne règle pas le cas de RLC (577 formules composées au démarrage, contre 216 avant sa réécriture du lot 8) ni
  l'ouverture d'un chapitre long : c'est la piste 1 (formules composées au fil du défilement), lot 5 ci-dessous.

## 2. Principe

- `index.html` garde **tout sauf** le contenu des onglets Cours, Méthodes et Exercices : coquille, scripts,
  paquets de cartes, `CHAPTERS`, chaque `div.chapter` avec ses onglets et ses panneaux (`<section class="panel"
  id="<prefix>-<onglet>">` **vide** pour Cours, Méthodes, Exercices ; Cartes, Simulateur et Vidéos inchangés).
- Le contenu de ces trois onglets vit dans **`chapitres/<id>.html`** (un fichier par chapitre, nommé par l'`id`
  du chapitre, pas par son `prefix`), sous la forme exacte qu'il a aujourd'hui dans `index.html` :

  ```html
  <template class="pan-tpl" data-panneau="rlc-cours"> … </template>
  <template class="pan-tpl" data-panneau="rlc-meth"> … </template>
  <template class="pan-tpl" data-panneau="rlc-exos"> … </template>
  ```

  Ce fichier devient la **source** du contenu : on l'édite directement (il se lit en entier, contrairement à
  `index.html`), puis on lance `python3 tools/chapitres.py` (données dérivées, voir §4).
- **Un chapitre visible a toujours son contenu.** Le clic sur un `.chap-btn` d'un chapitre pas encore chargé est
  différé (écouteur en phase de capture) : chargement du fichier, mise en place des `<template>` dans leurs
  panneaux, puis le clic est rejoué et tout le code existant (onglets, rendu MathJax, module CONTENU, PAGE,
  rail, recherche dans la page, assistant, impression) voit le contenu comme aujourd'hui. Depuis le cache du
  service worker, le chargement prend quelques dizaines de millisecondes ; un repère discret s'affiche s'il dure.
- `window.__chargerChapitre(id)` → promesse (une seule requête par chapitre) ; `navigateTo` l'attend avant sa
  séquence actuelle (donc ses rappels : recherche, Bilan, quiz, « Reprendre », liens profonds, restauration de
  `lastPos`, tests via `naviguer()`). `__deplierChapitre` et `__racinePanneau` restent (chapitre chargé).
- **Démarrage** : le petit script du `<head>` devine le chapitre à afficher (`#id/onglet`, sinon `lastPos`,
  sinon `rlc`) et lance tout de suite son chargement, en parallèle de l'analyse de la page.
- Échec (hors ligne et pas en cache, ou ouverture en `file://`) : le clic n'aboutit pas, un toast l'explique
  (« Chapitre pas encore disponible hors ligne », « Ouvre le site en ligne ou avec un petit serveur local »).
  **L'ouverture de `index.html` par double-clic ne marchera plus** (accepté par l'utilisateur le 2026-11-27) :
  `python -m http.server` dans le dossier, puis `http://localhost:8000`.

## 3. Hors ligne et mises à jour (service worker)

- Fichiers de chapitre appelés avec leur empreinte : `chapitres/<id>.html?v=<empreinte>` (8 caractères, calculée
  sur le contenu, fins de ligne normalisées pour que Windows et Linux donnent la même). Une correction ne change
  que l'empreinte du chapitre touché : le téléphone ne retélécharge que ce chapitre et la coquille.
- Cache à part, **`ptsi-chapitres`**, épargné par la purge du changement de `CACHE_VERSION` (la coquille reste
  purgée et rechargée comme aujourd'hui). Les requêtes vers `chapitres/` ne passent jamais par la branche HTML
  du service worker (elle répond `index.html` à toute requête qui accepte du HTML).
- **Préchargement en arrière-plan** : après le démarrage, au repos, la page télécharge un à un les chapitres
  absents du cache (et l'index de recherche), pas en mode « économie de données » ni hors ligne. Hors ligne, tout
  reste donc disponible comme aujourd'hui une fois ce préchargement fait.
- **Nettoyage** : la page retire de `ptsi-chapitres` les versions qui ne figurent plus dans son manifeste.
- Le HTML reste en stale-while-revalidate : une page ancienne demande d'anciennes empreintes, servies par le cache
  (ou, à défaut, par le réseau, qui donne la version récente : sans gravité).

## 4. Données dérivées (générées par `tools/chapitres.py`)

Certaines fonctions lisent aujourd'hui le contenu de **tous** les chapitres (ou d'un chapitre avant son
affichage) par `__racinePanneau` ou dans le DOM :

| Usage | Aujourd'hui | Après |
|---|---|---|
| Recherche (sections, définitions/propriétés, méthodes, formules, exercices) | `buildIndex` parcourt les 184 chapitres | **`chapitres/recherche.json`**, chargé à l'ouverture de la recherche ; chaque résultat porte un repère (`panneau`, nature, rang) résolu après le chargement du chapitre ; cartes et chapitres restent calculés dans la page |
| Bouton Formulaire masqué (`__aFormulaire`) | lecture des sections | manifeste (`f`) |
| Effectifs de l'intercalaire et des onglets (sections, méthodes, exercices) | `querySelectorAll` | manifeste (`s`, `m`, `e`) |
| Cible « Voir dans le cours · §n » d'une carte (`flashCible`) | Cours du chapitre | inchangé (chapitre affiché, donc chargé) |
| Formulaire, impression, rail, assistant | chapitre affiché | inchangé |

- **Manifeste** `window.__CHAPITRES = { rlc:{ v:'…', f:1, s:9, m:10, e:12 }, … }` : bloc généré en tête de page
  (≈ 10 Ko, entre deux marqueurs), lu par le script du `<head>`, le chargement, l'intercalaire.
- L'extraction de l'index de recherche est réécrite en Python (stdlib) **à l'identique** de `buildIndex` ; un test
  compare, sur des chapitres chargés dans la page, les entrées de `recherche.json` à celles que calcule l'ancien
  code (gardé dans le test).
- `validate.py` refuse un manifeste ou un index périmé ; `tools/chapitres.py` est idempotent.

## 5. Outils et tests

- `tools/chapitres.py` : `extraire` (une fois : déplace le contenu replié de `index.html` vers `chapitres/`),
  puis par défaut régénère manifeste et index ; `--verifier` n'écrit rien. Remplace `tools/replier_panneaux.py`.
- `validate.py` : IDs uniques sur `index.html` **et** tous les chapitres, « < » collé et `\[ … \]` cherchés dans
  les chapitres, aucun `<script>`, `<style>`, `</template>` parasite dans un chapitre, panneaux vides dans
  `index.html`, un fichier par chapitre listant Cours, Méthodes ou Exercices, données dérivées à jour.
- Tests : `naviguer()` passe par `navigateTo` (attend le chargement) ; les navigations par `location.hash`
  attendent le chapitre chargé ; suite `site` : panneaux vides dans `index.html`, éléments au démarrage ; suite
  `pwa` : chapitre jamais ouvert disponible hors ligne après le préchargement, cache `ptsi-chapitres` gardé au
  changement de version, versions périmées retirées ; option de test « délai de chargement » pour faire
  apparaître les erreurs de synchronisation.
- Outils des rédacteurs (scratchpad, non versionnés : `panneau.py`, `appliquer.py`, `chapitres.py`…) : à faire
  lire et écrire dans `chapitres/<id>.html`.

## 6. Lots

Chaque lot laisse le site fonctionnel, testé, commité et poussé sur la branche de travail.

1. **Chargement asynchrone, encore en un seul fichier** : `__chargerChapitre` (résolue tout de suite tant que le
   contenu est dans `index.html`, avec un délai artificiel réglable pour les tests), clic différé, `navigateTo`
   qui attend, repère de chargement. Batterie verte avec et sans délai artificiel.
2. **Données dérivées** : `tools/chapitres.py` (manifeste, `recherche.json`), recherche, intercalaire et
   `__aFormulaire` branchés dessus ; test d'équivalence de la recherche ; `validate.py`.
3. **Externalisation** : contenu déplacé dans `chapitres/` (RLC compris), chargement par `fetch`, préchargement du
   `<head>`, service worker (cache `ptsi-chapitres`, préchargement en arrière-plan, nettoyage), messages d'échec,
   tests `site` et `pwa`, mesures avant / après. Batterie complète, **publication** (point de retour
   `sauvegarde-avant-decoupage`), avec la documentation à jour (`CLAUDE.md`, `docs/interface.md`,
   `GABARIT-CHAPITRE.md`, `tests/README.md`).
4. **Outils des rédacteurs** adaptés (scratchpad).
5. **Piste 1, ensuite** : formules composées au fil du défilement (RLC, chapitres longs), mesurée à part.

## 7. Risques

- Synchronisation (focus, défilement, historique) autour du clic différé : lot 1 avec délai artificiel.
- Fidélité de la recherche : test d'équivalence (lot 2).
- Hors ligne : préchargement et suite `pwa` (lot 3).
- Le premier commit du lot 3 ajoute ≈ 20 Mo de fichiers au dépôt (une fois) ; ensuite, une publication n'ajoute
  que la coquille et les chapitres modifiés.

## 8. Suivi

- 2026-11-27 : plan écrit.
