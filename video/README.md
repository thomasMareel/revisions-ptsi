# Cours vidéo « prof au tableau »

Ce dossier contient tout ce qu'il faut pour fabriquer les cours vidéo du site : un tableau noir animé
(Manim), une narration en voix de synthèse (Voxtral, Mistral) et des sous-titres. Les vidéos sont
hébergées sur **YouTube en non répertorié** ; le site ne contient que leurs liens.

Rien de ce dossier n'est chargé par `index.html`. Les fichiers produits (audio, images, vidéos) ne
sont **jamais** versionnés (voir `.gitignore`) : le dépôt ne garde que les sources.

## Choix validés par Thomas (ne pas les changer sans lui demander)

- **Voix** : Camille, voix prédéfinie de Mistral (`voice_3141`), modèle `voxtral-mini-tts-3`,
  ralentie de 5 % (`atempo` 0,95, hauteur inchangée), volume normalisé à −16 LUFS.
- **Tableau** : fond `#1F2A24`, craie `#EDEBE4`, titres jaunes `#F2D16B`, rouge `#F08A7E`,
  bleu `#8EC5F2`, vert `#9BD49A`, orange `#F2B36B`, gris `#8FA097`, police Palatino (`mathpazo`), 1080p, 30 images/s.
- **Écriture** : `Ecrire(mob)` (apparition nette, glyphe par glyphe). Pas l'animation `Write` de
  Manim, jugée « trop brouillon ». `Create` pour les axes, cadres et traits.
- **Sous-titres** : texte exact avec les symboles (ξ, νᵢ, ΔrG°), 2 lignes de 42 caractères au plus,
  désactivables. La forme prononcée (« ksi », « delta-r-G standard ») ne sert qu'à la voix.
- **Format** : une vidéo de 7 à 9 minutes par chapitre, une dizaine de scènes, tableau effacé entre
  deux scènes, un exercice « À vous » avec minuteur, un bilan numéroté « À retenir » à la fin.
- **Ton** : cours dynamique et complet, appuyé sur le programme officiel de PT ; tous les objets définis.

## Arborescence

```
video/
  installer.sh          installation des outils (à relancer sans risque)
  MISE-EN-PLACE.md      à faire une fois : clé Mistral et autorisation YouTube (guide pas à pas)
  YOUTUBE.md            mise en ligne des vidéos
  commun/               scripts partagés par tous les cours
    mistral_client.py   accès à la voix (secret réseau ou variable MISTRAL_API_KEY)
    test_voix.py        essai réel de la voix, une phrase
    audio.py            voix : synthèse, contrôle, régénération, timeline.json
    base.py             classes Manim : Cours, Ecrire, T(), M(), couleurs
    ancres.py           contrôle des points de synchronisation avant le rendu
    rendu.sh            rendu des scènes (2 en parallèle)
    planche.py          planche d'images de contrôle
    assemble.py         vidéo finale, sous-titres, fiche YouTube
    youtube.py          envoi sur YouTube (non répertorié), sous-titres compris
  thermochimie/
    pdf/                sources LaTeX du cours PDF (51 pages) : contenu de référence des vidéos
    ch1/ ch2/ ch3/      un dossier par chapitre vidéo
      chapitre.json     cours, numéro, titre, nom de fichier, voix
      segments.py       le script : scènes et phrases (texte écrit, texte prononcé, pause)
      scenes.py         une classe Manim par scène, calée sur la voix
      timeline.json     début et fin de chaque phrase dans la vidéo livrée
      youtube.json      identifiant et lien de la vidéo en ligne (écrit par youtube.py)
```

Un nouveau cours = un nouveau dossier à côté de `thermochimie/` ; un nouveau chapitre = une copie
du dossier du chapitre précédent, dont on réécrit `chapitre.json`, `segments.py` et `scenes.py`.

## Mise en route d'une session

```
bash video/installer.sh
```

Le script installe ce qui manque (LaTeX, ffmpeg, Manim, client Mistral) et termine par un contrôle,
dont l'accès à la voix. Il n'a été essayé que sur une machine où LaTeX et ffmpeg étaient déjà
présents : sur une machine neuve, lire sa sortie et corriger au besoin.

**Clé Mistral et autorisation YouTube : jamais dans le dépôt** (il est public), ni dans un fichier,
ni dans un message de commit, ni dans une sortie affichée. Elles vivent dans l'environnement cloud
de Claude Code. Leur mise en place, à faire une fois, est décrite pas à pas dans
**`MISE-EN-PLACE.md`** ; `python3 video/commun/test_voix.py` et `python3 video/commun/youtube.py test`
disent si tout est branché.

⚠️ Après l'installation de LaTeX, les polices Latin Modern peuvent fausser les suites `mobile` et
`visuel` des tests du site : voir « Conteneur Claude Code » dans `CLAUDE.md` (`FONTCONFIG_FILE`).

## Fabriquer un chapitre

Toutes les commandes se lancent **depuis le dossier du chapitre** (ex. `video/thermochimie/ch4`).

1. **Écrire le script** dans `segments.py`, à partir du chapitre correspondant du PDF
   (`pdf/chN.tex`, données dans `pdf/data/`) :
   `SCENES = [(id_scène, titre, [(id_phrase, écrit, dit_ou_None, pause_en_s), ...]), ...]`.
   `écrit` est le texte des sous-titres ; `dit` la forme prononcée quand elle diffère.
2. **Voix** : `python3 ../../commun/audio.py` (`-v` pour tout voir). Chaque phrase est synthétisée,
   retranscrite et mesurée ; une phrase douteuse est régénérée jusqu'à 6 fois. Lire la liste des
   défauts restants : **reformuler** la phrase dans `segments.py` plutôt que d'insister. Produit
   `narration.wav` et `timeline.json`. Le cache `audio/` évite de repayer les phrases inchangées.
3. **Scènes** dans `scenes.py` : une classe par scène (`class S3(Cours): sid = "S3"`), animations
   placées avec `self.t("id")` (début d'une phrase) et `self.a("id", "fragment")` (instant où le
   fragment est prononcé). Finir chaque scène par `self.fin()`.
4. **Contrôle des ancres** : `python3 ../../commun/ancres.py` (doit afficher 0 erreur).
5. **Rendu** : `bash ../../commun/rendu.sh` (ou `... S2 S5` pour quelques scènes). Une ligne
   `RETARD` signale une animation qui déborde sur la suivante : raccourcir ou déplacer.
6. **Planche** : `python3 ../../commun/planche.py`, puis **regarder** `out/planche.jpg` : aucun
   chevauchement, rien hors cadre, rien d'illisible. Corriger et ne re-rendre que les scènes touchées.
7. **Assemblage** : `python3 ../../commun/assemble.py` → `out/<fichier>.mp4` (sous-titres
   désactivables, chapitres), `out/<fichier>.srt`, `out/youtube.txt` (titre, description, chapitres).
8. **Mise en ligne** : `python3 ../../commun/youtube.py envoi` (vidéo non répertoriée, description,
   sous-titres), puis versionner `youtube.json`, reporter le lien dans le tableau ci-dessous et
   l'ajouter au site. Tant que YouTube n'est pas branché : à la main, voir `YOUTUBE.md`.

Ordre de grandeur pour un chapitre de 8 minutes : 70 phrases, environ 0,15 $ de voix
(0,016 $ pour 1 000 caractères, plus la transcription de contrôle et les régénérations),
20 à 40 minutes de travail machine.

## Règles d'écriture du script (leçons des chapitres 1 à 3)

- Dans `dit` : nombres **en toutes lettres** ; « ksi » pour ξ, « nu i » pour νᵢ, « delta-r-G standard »
  pour ΔrG° ; différentielles « dé G », « P dé V ».
- **Pas de points de suspension** (mots parasites) ni de suites de signes épelés du type
  « x, plus quatre fois moins deux » (mots inventés) : faire une vraie phrase.
- Énumérations : « Règle numéro un », « Premièrement » ; « Un : » est parfois mal lu.
- Une phrase = une idée, 25 mots au plus ; la pause (0,3 à 1 s) donne le rythme.
- Une formule épelée est détectée automatiquement et sort du contrôle de débit.
- Personne n'écoute la voix pendant la fabrication : le contrôle est indirect (transcription, débit,
  silences). Signaler à Thomas les phrases restées douteuses avec leur minutage, il les écoute.

## Corriger une vidéo déjà en ligne

L'audio d'origine n'est pas dans le dépôt. Pour corriger un chapitre livré, relancer `audio.py`
(la voix est régénérée, quelques centimes), puis toutes les scènes : elles se recalent seules sur la
nouvelle `timeline.json`. YouTube ne remplace pas une vidéo : la correction a une nouvelle adresse,
à reporter dans le site.

## Intégration au site (à concevoir avec Thomas, rien n'est encore fait)

Contraintes du site à respecter (détail dans `CLAUDE.md`) :

- **aucune requête externe au chargement** (suites `site` et `pwa`) et fonctionnement hors ligne :
  le lecteur YouTube ne peut donc être inséré **qu'au clic** (bouton « Voir le cours en vidéo » qui
  crée l'`<iframe>` `https://www.youtube-nocookie.com/embed/<id>`), avec un message clair hors ligne ;
  `sw.js` laisse déjà passer les requêtes externes ;
- le lecteur YouTube fournit la vitesse (×0,25 à ×2), les sous-titres et les chapitres : ne pas les recoder ;
- pas de refonte non demandée : proposer une maquette (emplacement dans la page chapitre, téléphone
  d'abord) avant de toucher à `index.html` ; puis tests, bump de `CACHE_VERSION`, publication ;
- les liens vivent dans une table de données (identifiant du chapitre du site → vidéos), pas dans le HTML des chapitres ;
- vérifier d'abord qu'un chapitre du site correspond au cours (pour la thermochimie de PT, il est
  peut-être à créer : `GABARIT-CHAPITRE.md`).

## Vidéos livrées

| Cours | Chapitre | Durée | Lien YouTube |
|---|---|---|---|
| Thermochimie | 1 — Rappels de première année | 8 min 18 | à ajouter |
| Thermochimie | 2 — Enthalpie libre et potentiel chimique | 7 min 27 | à ajouter |
| Thermochimie | 3 — Grandeurs de réaction et grandeurs standard | 8 min 30 | à ajouter |

Suite prévue : chapitre 4, « Effets thermiques des réactions » (chaleur de réaction, température de
flamme, simulation du réacteur adiabatique : `pdf/ch4.tex`, `pdf/data/adiab.dat`,
`pdf/code/reacteur_adiabatique.py`), puis les chapitres 5 à 8 du PDF.

Remarque de Thomas sur le chapitre 3 : l'explication des νᵢ (coefficients stœchiométriques
**algébriques** : négatifs pour les réactifs, positifs pour les produits) n'était pas assez claire.
Prévoir un rappel explicite d'une quinzaine de secondes dans la suite.

## Le PDF du cours

`thermochimie/pdf/` : `pdflatex main.tex` (deux passes). Les valeurs numériques et les courbes
viennent de `scripts/calculs.py`, qui réécrit `data/*.dat`.

## Droits et voix

- Camille est une voix fournie par Mistral ; l'usage passe par l'API payante. Mentionner « voix de
  synthèse » dans la description de chaque vidéo (`assemble.py` l'écrit dans `out/youtube.txt`).
- **Ne jamais cloner la voix de quelqu'un sans son accord écrit.**
- Contenu : rédaction originale à partir du programme officiel ; ne recopier ni manuel ni poly.
