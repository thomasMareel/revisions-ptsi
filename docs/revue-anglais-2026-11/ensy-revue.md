# Compte rendu : `ensynth` (prefix `ensy`) et cours de `endoc` (prefix `endc`) — 2026-11-26

## 1. Nouveau chapitre `ensynth` « Synthèse de documents : l'épreuve écrite »

Fichiers livrés (dans `AN1/`) :

| Fichier | Contenu |
|---|---|
| `ensy-cours.src.html` | bloc « AU PROGRAMME · PT » (ce qu'on sait de l'épreuve) + 10 sections, 2 figures SVG |
| `ensy-meth.src.html` | 8 méthodes (fiches réflexes) + 2 encadrés « Piège » |
| `ensy-exos.src.html` | 4 exercices dans un seul `.exo-wrapper`, le dernier en `.exo.concours` ; 3 figures SVG |
| `ensy-cartes.js` | `const ensyCards = [ … ];` 30 cartes en texte brut (remplace le paquet provisoire d'une carte) |

Sources de fabrication (à garder pour retoucher) : `ensy_figs.py` → `ensy_figs.json` (figures), `ensy_textes.py`
(tous les textes anglais dont le nombre de mots compte, avec la fonction de comptage), `ensy_construire.py`
(gabarits `ensy-*.tpl.html` → `*.src.html` : figures, textes, nombres de mots calculés, « doc. 2 » et « 61 % » insécables).
Toute retouche d'un texte anglais se fait dans `ensy_textes.py`, puis `python3 ensy_construire.py` : les nombres de
mots affichés suivent.

### Cours (§1 à §10)
AU PROGRAMME · PT (durée 3 h, dossier de 5 documents en 2026, thème géo-ingénierie, 450 à 500 mots d'après le rapport
2026 ; tout le reste renvoyé à la notice et au rapport du jury) · §1 l'épreuve et ce qu'on attend (définition, tableau
résumé / synthèse / essai, ni avis ni connaissances extérieures) · §2 lire un dossier (fiche d'identité, lecture active,
lire un graphique avec figure, points de pourcentage, vocabulaire des évolutions, dessin de presse) · §3 problématique
(méthode, tableau de 5 propositions jugées, formes utiles, question indirecte sans inversion) · §4 plan (tableau de
confrontation, trois plans types, règles) · §5 introduction (4 temps, exemple de 87 mots annoté) · §6 rédiger en
confrontant (paragraphe en 4 temps, exemple de 130 mots, renvois, citations courtes, connecteurs → `enconnect`) ·
§7 conclusion (exemple de 60 mots, ouverture) · §8 anglais de la synthèse (12 verbes introducteurs et leur construction,
comparer / opposer, *on the contrary* ≠ *by contrast*, nuancer, 13 erreurs fréquentes des francophones, UK / US) ·
§9 gérer les 3 h (frise SVG + tableau) et compter les mots (convention, budget, comptage exact, viser 470-490) ·
§10 erreurs classiques (tableau erreur → remède, bloc « avant / après »).
Fil conducteur : un mini-dossier inventé (Norbridge, la voiture en ville), présenté au §2 et repris du §2 au §10.
Renvois : `endoc`, `enconnect`, `enavis`, `engrammod`, `engramfa`.

### Méthodes
1 analyser un document iconographique · 2 formuler une problématique · 3 faire le tableau de confrontation ·
4 rédiger l'introduction (exemple 80 mots) · 5 rédiger une partie · 6 rédiger la conclusion (47 mots) ·
7 relire en 10 minutes (5 passes) · 8 compter les mots. Exemples éclair sur un 2ᵉ mini-dossier fictif (télétravail),
pour ne pas dévoiler les corrigés des exercices.

### Exercices
- **EXO 01** ★ — trouver la problématique (dossier résumé sur la voiture électrique : 5 propositions à juger, une à
  proposer avec un plan, passage au style indirect).
- **EXO 02** ★★ — corriger une introduction maladroite (IA et emploi) : 13 défauts relevés en tableau, introduction
  réécrite (87 mots).
- **EXO 03** ★★ — dossier complet « le dessalement » : 3 articles fictifs (202, 182, 201 mots) + un diagramme en barres
  SVG ; questions guidées (fiches, graphique, tableau, plan) ; **synthèse modèle de 473 mots** (95 + 163 + 163 + 52,
  titre non compté).
- **CONCOURS PT** ★★★ — dossier complet de 5 documents « orbite basse » : 3 textes fictifs (195, 182, 198 mots), une
  courbe SVG, un dessin de presse dessiné en SVG ; parties A (lire), B (construire), C (rédiger) ; **synthèse modèle de
  476 mots** en trois parties (91 + 100 + 124 + 112 + 49, titre non compté). Calculs du graphique vérifiés
  (9 300 / 12 000 ≈ 78 % ; 8 900 / 9 700 ≈ 92 % de la hausse depuis 2019 ; facteur 12 000 / 1 400 ≈ 8,6).
- Comptage des mots par programme (`ensy_textes.py`, convention affichée dans le cours : groupe de caractères entre deux
  espaces, « (doc. 2) » = 2 mots, titre exclu).
- Droit d'auteur : tous les documents, journaux (*The Merrow Coast Herald*, *The Sunday Lantern*, *The Evening Compass*,
  *The Highland Courier*, *The Northern Science Review*, *The Weekend Review*…), auteurs, villes, entreprise (Orbitane)
  et chiffres sont inventés et présentés comme fictifs dans le texte même (« fictional regional daily »,
  « fictional data ») ; le thème 2026 (géo-ingénierie) n'est pas repris.

### Cartes (30, texte brut)
Épreuve (durée, longueur, fautes de méthode, synthèse / résumé / essai) · lire un document (op-ed / editorial, ordre de
lecture d'un graphique, points de pourcentage, verbes d'évolution, prépositions) · problématique et introduction
(to what extent, style indirect, présenter le dossier, annoncer le plan) · développement (renvois, citations, verbes
introducteurs, argue / claim, warn against / call for, suggest, accord / opposition, on the contrary / by contrast) ·
erreurs (indénombrables, *allow to*) · conclusion, comptage des mots. Lecture audio vérifiée en simulant
`__TTS.detectLang` et `cleanForSpeech` (`ensy_tmp/tts.js`) : les réponses en anglais sont lues par la voix anglaise,
gloses françaises entre parenthèses retirées ; aucun `\(` ni `$`.

### Contrôles
- `verif_src.py` sur les trois panneaux : aucune ERREUR ni « attention ».
- `apercu_src.py` (copie `AN1/site/index.html`) à 390 et 1440 px, cours, méthodes, exercices : `merr`, `brut`,
  `larges` vides, aucune erreur JS, `scrollW` = largeur ; captures regardées (figures, tableaux, dessin).
- Cartes : `node -e … ensyCards.length` → 30, questions toutes distinctes ; `ajouter_cartes.py ensy … --essai` sur la
  copie du site → syntaxe valide.

### Points d'attention pour l'intégration
- Remplacer tout le paquet provisoire (`{q:"Chapitre en cours de rédaction ?", …}`) par `ensy-cartes.js` : c'est un
  nouveau chapitre, aucune progression d'élève à préserver.
- Les passages anglais des exercices (documents, synthèses modèles) portent `lang="en"` (césure anglaise, lecteurs
  d'écran) ; c'est nouveau sur le site, sans effet de style.
- Les figures de 520-540 px de large défilent au téléphone (mécanisme `.defile` du site), comme les autres schémas.
- Après intégration : `python3 tools/replier_panneaux.py` (panneaux Cours, Méthodes, Exercices de `ensynth`).

## 2. Cours de `endoc` (prefix `endc`) : l'oral d'anglais de la Banque PT

Livrable : `endc-cours.src.html` = le panneau actuel **inchangé** (§1 à §3, vérifié octet pour octet ; copie dans
`endc_orig_cours.html`) + deux sections ajoutées à la fin (source : `endc-ajout.tpl.html`) :
- **§4 · L'oral d'anglais de la Banque PT** : bloc dépliable « AU PROGRAMME · PT » (≈ 40 min, ≈ 20 min de préparation
  puis ≈ 20 min d'exposé et d'entretien, support enregistré à résumer puis commenter, d'après les rapports 2025-2026 ;
  le reste renvoyé à la notice et au rapport, lien vers `ensynth`), préparer en 20 minutes (5 étapes), prendre des notes
  à l'oreille, piège « tout comprendre ».
- **§5 · Conduire l'exposé et l'entretien** : présentation, résumé, commentaire, entretien (expressions anglaises
  glosées, renvois `enavis` et `enreac`), tableau synthèse écrite / oral (avis et connaissances interdits à l'écrit,
  attendus à l'oral), pièges.
Pas de nouvelle carte pour `endc` (paquets confiés à un autre rédacteur).
Contrôles : `verif_src.py` sans ERREUR ni « attention » ; aperçu 390 et 1440 px : `merr`, `brut`, `larges` vides,
aucune erreur JS.

## Doutes
- `verif_src.py` demande un bloc « AU PROGRAMME » dans tout cours. Pour `endc`, sans toucher au début du panneau, ce
  bloc est un `.reveal` intitulé « AU PROGRAMME · PT » au début du §4 (l'intitulé est de toute façon affiché en
  capitales) ; si l'on préfère la convention « bloc en tête de chapitre », le déplacer en tête lors de l'intégration.
- Détails de l'épreuve non sûrs (titre exigé, décompte des renvois et citations, tolérance, indication du nombre de mots,
  nombre d'écoutes à l'oral, partage du temps exposé / entretien) : jamais affirmés, renvoyés à la notice et au rapport.
- Le lien vers les annales (`https://www.banquept.fr/rubrique38.html`) est celui déjà employé par les exercices
  « Concours PT » du site ; non vérifié d'ici (pas d'accès réseau).
