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
| Bouton Formulaire masqué (`__aFormulaire`), effectifs de l'intercalaire et des onglets | chapitre affiché | inchangé (chapitre affiché, donc chargé ; rien n'est mémorisé pour un chapitre pas encore chargé) |
| Cible « Voir dans le cours · §n » d'une carte (`flashCible`) | Cours du chapitre | inchangé (chapitre affiché, donc chargé) |
| Formulaire, impression, rail, assistant | chapitre affiché | inchangé |

- **Manifeste** `window.__CHAPITRES = { recherche:'…', v:{ rlc:'…', … } }` (empreintes de `recherche.json` et de
  chaque fichier de chapitre) : bloc généré dans le script du `<head>` (≈ 4 Ko, entre deux marqueurs).
- **Extraction par Chromium** (décision du 2026-11-27, au lieu d'une réécriture en Python) : `tools/chapitres.js`
  analyse chaque fichier avec l'analyseur HTML du navigateur et lui applique `tools/extraction-chapitres.js`,
  l'ancien `buildIndex` déplacé tel quel : les entrées sont celles d'avant, à l'identique. Il faut Playwright
  (comme pour les tests) ; `validate.py` (Python) ne fait que comparer les empreintes.
- `recherche.json` pèse ≈ 11 Mo (2,9 Mo compressé), dont 4,3 Mo de texte intégral des exercices : c'est ce que
  la recherche gardait déjà en mémoire. Il n'est chargé qu'à l'ouverture de la recherche (et en arrière-plan
  pour le hors-ligne) ; en attendant, la recherche porte sur les chapitres et les cartes, puis la requête est
  rejouée. Réduire les blancs ne gagnait que 2 %.
- `validate.py` refuse un manifeste ou un index périmé ; `tools/chapitres.js` est idempotent (≈ 7 s).

## 5. Outils et tests

- `node tools/chapitres.js` régénère manifeste et index ; `--verifier` n'écrit rien. La migration (déplacer le
  contenu d'`index.html` vers `chapitres/`, octet pour octet) est faite une fois par un script du scratchpad,
  non versionné. `tools/replier_panneaux.py` disparaît.
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

1. **Chargement asynchrone, encore en un seul fichier** (fait le 2026-11-27) : `__chargerChapitre` (résolue tout de suite tant que le
   contenu est dans `index.html`, avec un délai artificiel réglable pour les tests), clic différé, `navigateTo`
   qui attend, repère de chargement. Batterie verte avec et sans délai artificiel.
2. et 3. (**fusionnés** le 2026-11-27 : l'empreinte des données dérivées se calcule bien plus simplement sur des
   fichiers séparés) **Données dérivées et externalisation** : `tools/chapitres.js`, recherche branchée sur
   `recherche.json` (test : un résultat de chaque nature ouvre et met en évidence le bon élément) ; contenu déplacé
   dans `chapitres/` (RLC compris, 184 fichiers, 514 panneaux, octet pour octet), chargement par `fetch`, préchargement du
   `<head>`, service worker (cache `ptsi-chapitres`, préchargement en arrière-plan, nettoyage), messages d'échec,
   tests `site` et `pwa`, mesures avant / après. Batterie complète, **publication** (point de retour
   `sauvegarde-avant-decoupage`), avec la documentation à jour (`CLAUDE.md`, `docs/interface.md`,
   `GABARIT-CHAPITRE.md`, `tests/README.md`).
4. **Outils des rédacteurs** adaptés (scratchpad).
5. **Piste 1** (fait le 2026-11-28) : formules composées au fil du défilement (RLC, chapitres longs), mesurée à part
   (mesures ci-dessous ; fonctionnement : `docs/interface.md` › « MathJax » › « Composition progressive »).

## 7. Risques

- Synchronisation (focus, défilement, historique) autour du clic différé : lot 1 avec délai artificiel.
- Fidélité de la recherche : même code d'extraction qu'avant (Chromium), même nombre d'entrées (12 219) ; test
  « un résultat de chaque nature » (suite `interactions`).
- Hors ligne : préchargement et suite `pwa` (lot 3).
- Le premier commit du lot 3 ajoute ≈ 20 Mo de fichiers au dépôt (une fois) ; ensuite, une publication n'ajoute
  que la coquille et les chapitres modifiés.

## 8. Suivi

- 2026-11-27 : plan écrit. Lot 1 fait : `navigateTo` ne rend plus l'onglet par défaut d'un chapitre quand il en
  vise un autre (le Cours de RLC était composé pour rien à chaque lien vers ses exercices ou ses cartes) ;
  `window.__navigationEnCours()` attendu par les tests au démarrage ; suites vertes avec `--delai-chapitres=300`.
- 2026-11-27 : lots 2 et 3 faits sur la branche de travail : `index.html` 23,1 → 3,0 Mo ; suites `site`, `pwa`
  (chapitres en cache en arrière-plan, chapitre jamais ouvert lisible hors ligne, version périmée retirée) et
  `interactions` vertes. Corrigé en route : `majPage` (module PAGE) enrichissait l'intercalaire du chapitre affiché
  au départ avant l'arrivée de son contenu (compteurs à zéro, Formulaire masqué).
- 2026-11-27 : mesures après découpage (même machine, en alternance avec la v136 en ligne ; scripts `autre.js`,
  `dcl.js` du scratchpad) :

  | Démarrage (page prête) | v136 (23 Mo) | Découpé (3 Mo + chapitre) |
  |---|---|---|
  | téléphone ×4, reprise d'un chapitre ordinaire (`#pybases/cours`) | 5,8 – 6,3 s | **3,0 – 3,3 s** |
  | téléphone ×4, chapitre RLC (1ʳᵉ visite) | 12,6 – 12,7 s | 10,1 – 11,1 s |
  | ordinateur, chapitre RLC | 2,4 – 2,6 s | **1,3 – 1,4 s** |

  Reste pour RLC et les chapitres longs : la composition des formules (lot 5, piste 1).
- 2026-11-28 : lot 5 fait (composition progressive). Le Cours de RLC composait ses 577 formules d'un seul tenant
  pendant le démarrage (2,5 à 2,8 s d'un bloc au téléphone, rien ne s'affichait avant) ; un panneau est maintenant
  découpé en morceaux : l'écran tout de suite, la suite au repos par lots courts et dès qu'elle approche de l'écran.
  Mesures (même machine, en alternance avec la v137 ; scripts `lot5-mesure.js`, `lot5-trace.js` du scratchpad ;
  « écran prêt » = plus aucun TeX en clair dans l'écran, « bloquant » = somme des tâches longues au-delà de 50 ms) :

  | `#rlc/cours` | v137 | Composition progressive |
  |---|---|---|
  | téléphone ×4 : écran prêt | 8,7 – 10,3 s | **2,3 – 2,9 s** |
  | téléphone ×4 : plus longue tâche | 2,6 – 2,9 s | 0,6 – 0,7 s (démarrage ; lots : 50 – 250 ms) |
  | téléphone ×4 : temps bloquant jusqu'à la fin | 5,7 – 6,7 s | 4,6 – 5,3 s |
  | téléphone ×4 : tout composé | 8,7 – 10,3 s | 15 – 16 s (au repos, pendant la lecture) |
  | ordinateur : écran prêt | 1,8 – 2,2 s | **0,6 s** |

  Chapitre sans formule au démarrage (`#pybases/cours`) : inchangé (2,6 – 3,2 s). Appris en route : le coût d'un lot
  est surtout le **dessin** de la page sous l'écran (tout ce qui a bougé) ; les lots trop petits (une formule) coûtaient
  4 s de dessin sur 6 s, d'où des lots d'environ 80 ms avec leurs finitions dans la même tâche. Un dernier balayage
  MathJax du panneau entier, par sécurité, coûtait 0,6 s au téléphone pour ne rien trouver : seulement s'il y a une
  formule hors morceaux. Corrigé en route (comparaison du HTML final avec la v137, 23 panneaux identiques) : mesures
  d'un morceau qui est lui-même un bloc de code ou un tableau défilant, typographie appliquée à du code (« figure : »
  dans un programme Python), libellé de section pris sur le TeX en clair (titres désormais composés d'emblée).
