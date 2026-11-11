# Cours vidéo « prof au tableau »

Ce dossier contient tout ce qu'il faut pour fabriquer les cours vidéo du site : un tableau noir animé
(Manim), une narration en voix de synthèse (Voxtral, Mistral) et des sous-titres. Les vidéos sont
hébergées sur **YouTube en non répertorié** ; le site ne contient que leurs liens.

Rien de ce dossier n'est chargé par `index.html`. Les fichiers produits (audio, images, vidéos) ne
sont **jamais** versionnés (voir `.gitignore`) : le dépôt ne garde que les sources.

## Choix validés par Thomas (ne pas les changer sans lui demander)

- **Voix** : Camille, voix prédéfinie de Mistral (`voice_3141`), modèle `voxtral-mini-tts-3`, volume
  normalisé à −16 LUFS. **Depuis le chapitre 4 (demande de Thomas du 2026-11-11 : « plus dynamique »)** :
  `"expressivite": 3.0` et `"tempo": 1.0` dans `chapitre.json` (paramètre `expressiveness` de l'API :
  ≈ 30 % d'intonation en plus, mesuré sur 6 tirages ; au-delà de 3, presque rien de plus ; plus de
  ralentissement, l'expressivité ralentissant déjà un peu le débit). Chapitres 1 à 3 : réglage d'origine
  (pas d'expressivité, ralentie de 5 %), qui reste la valeur par défaut d'`audio.py`.
- **Tableau** : fond `#1F2A24`, craie `#EDEBE4`, titres jaunes `#F2D16B`, rouge `#F08A7E`,
  bleu `#8EC5F2`, vert `#9BD49A`, orange `#F2B36B`, gris `#8FA097`, police Palatino (`mathpazo`), 1080p, 30 images/s.
- **Écriture** : `Ecrire(mob)` (apparition nette, glyphe par glyphe). Pas l'animation `Write` de
  Manim, jugée « trop brouillon ». `Create` pour les axes, cadres et traits.
- **Sous-titres** : texte exact avec les symboles (ξ, νᵢ, ΔrG°), 2 lignes de 42 caractères au plus,
  désactivables. La forme prononcée (« ksi », « delta-r-G standard ») ne sert qu'à la voix.
- **Format** : une vidéo de 8 à 10 minutes par chapitre, une dizaine de scènes, tableau effacé entre
  deux scènes, un exercice « À vous » avec minuteur, un bilan numéroté « À retenir », puis **un exercice
  résolu de bout en bout** (demande de Thomas du 2026-11-11, dès que le chapitre s'y prête) : une scène
  d'énoncé (données au tableau, question encadrée, « réfléchissons » : quel outil du chapitre ?) et une
  scène de résolution par étapes numérotées, chaque étape **justifiée à l'oral** (pourquoi on fait ce
  calcul), résultat encadré, vérification (signe, ordre de grandeur, comparaison aux tables). La phrase
  « Dans le prochain chapitre… » clôt la vidéo, après l'exercice.
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
dont l'accès à la voix. Essayé sur une machine neuve le 2026-11-11 (≈ 10 minutes : LaTeX, ffmpeg,
Manim) ; si une ligne ABSENT ou !! reste, lire sa sortie et corriger au besoin.

**Clé Mistral et autorisation YouTube : jamais dans le dépôt** (il est public), ni dans un fichier,
ni dans un message de commit, ni dans une sortie affichée. Elles vivent dans l'environnement cloud
de Claude Code (environnement « revisions-ptsi »). Leur mise en place, **faite le 2026-11-11**, est
décrite pas à pas dans **`MISE-EN-PLACE.md`** (à refaire seulement si une clé est révoquée) ; `python3 video/commun/test_voix.py` et `python3 video/commun/youtube.py test`
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
   l'ajouter au site. Envoi automatique branché et essayé (2026-11-11) ; repli à la main : `YOUTUBE.md`.

Ordre de grandeur pour un chapitre de 8 minutes : 70 phrases, environ 0,15 $ de voix
(0,016 $ pour 1 000 caractères, plus la transcription de contrôle et les régénérations),
20 à 40 minutes de travail machine.

## Règles d'écriture du script (leçons des chapitres 1 à 4)

- **Ton vivant** (depuis le chapitre 4) : interpeller (« Regardez ! », « Attention au piège ! »,
  « Et voilà ! », « À vous de jouer ! »), poser la question avant la réponse (« Réaction exothermique ?
  Alors… »), des exclamations sur les résultats clés, des phrases courtes. La voix suit la ponctuation :
  un texte enjoué donne une voix plus haute et plus vivante (mesuré : + 25 à 45 Hz).

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

## Intégration au site (faite le 2026-11-11)

Les vidéos sont rangées dans un onglet **« Vidéos »** du chapitre du site correspondant, entre Cours
et Méthodes (choix de Thomas) : grands lecteurs empilés dans l'ordre, titre et durée au-dessus, liste
repliable des parties dessous (un clic lance la vidéo à ce moment). Thermochimie : chapitre
`thermochimie` du site (« Thermodynamique de la transformation chimique », physique › Chimie,
2ᵉ année), rédigé à partir de `thermochimie/pdf/`.

- **Rien n'est chargé depuis YouTube avant un clic** : chaque vidéo montre d'abord une image
  d'aperçu rangée dans le site (`media/videos/`) ; le lecteur `youtube-nocookie` n'est créé qu'au clic
  sur « Lire » ou sur une partie. Hors ligne, un message le dit. Une seule vidéo tourne à la fois.
- La vitesse, les sous-titres et le plein écran sont ceux du lecteur YouTube.
- À l'impression, l'onglet donne la liste des vidéos avec leurs liens et leurs parties.

**Ajouter une vidéo** (chapitre qui a déjà l'onglet, par exemple le chapitre 4 de thermochimie),
une fois `youtube.py envoi` fait :

1. Image d'aperçu : une image de l'introduction (titre et plan au tableau, juste avant l'effacement
   final de la scène S0, après toute surbrillance), depuis le dossier du chapitre vidéo :
   ```
   ffmpeg -ss <durée de S0 - 0,6 s> -i out/<fichier>.mp4 -frames:v 1 \
     -vf scale=1280:720 -c:v libwebp -quality 80 ../../../media/videos/thermochimie-4.webp
   ```
2. Une entrée dans la table `window.__VIDEOS` d'`index.html` (`grep -n 'window.__VIDEOS = {'`) :
   `{ yt:'<id de youtube.json>', titre:'…', duree:<s>, apercu:'media/videos/thermochimie-4.webp',
   parties:[[0,'Introduction'], [<t0 entier de chaque scène>, '<titre de la scène>'], …] }`
   (les mêmes parties que dans `out/youtube.txt`).
3. Publication comme pour toute modification du site : `validate.py`, `check_js.py`, tests
   (`interactions` contient le test de l'onglet Vidéos), bump de `CACHE_VERSION` dans `sw.js`.

**Donner l'onglet à un autre chapitre du site** : dans `CHAPTERS`, ajouter `'video'` à `panels`
(après `'cours'`) ; dans le bloc du chapitre, ajouter l'onglet
`<button class="tab" data-panel="<prefix>-video"><span class="num">02</span>Vidéos</button>` après
Cours et le panneau `<section class="panel" id="<prefix>-video"><div class="vid-liste"
data-videos="<id du chapitre>"></div></section>` après celui du Cours ; puis l'entrée de la table.
Vérifier d'abord qu'un chapitre du site correspond au cours (sinon le créer : `GABARIT-CHAPITRE.md`).

## Vidéos livrées

Toutes en **non répertorié**, sous-titres français compris, envoyées le 2026-11-11 par `youtube.py`
(identifiants dans `thermochimie/chN/youtube.json`). Sur le site : onglet « Vidéos » du chapitre
`thermochimie` (table `window.__VIDEOS`).

| Cours | Chapitre | Durée | Lien YouTube |
|---|---|---|---|
| Thermochimie | 1 — Rappels de première année | 8 min 18 | <https://youtu.be/YtisR2_KXQ0> |
| Thermochimie | 2 — Enthalpie libre et potentiel chimique | 7 min 27 | <https://youtu.be/l9C4IiB3gVA> |
| Thermochimie | 3 — Grandeurs de réaction et grandeurs standard | 8 min 30 | <https://youtu.be/tbJv-uT1Uyw> |
| Thermochimie | 4 — Premier principe : effets thermiques des réactions | 8 min 48 | <https://youtu.be/L5z0oicvuOI> |
| Thermochimie | 5 — Deuxième principe : évolution et équilibre | 9 min 15 | <https://youtu.be/IxOhQ0SkXQ0> |
| Thermochimie | 6 — Influence des paramètres et optimisation | 9 min 40 | <https://youtu.be/A9G7gfQWMk8> |

Suite prévue : les chapitres 7 et 8 du PDF, `pdf/ch7.tex` et `ch8.tex` (le chapitre 9 du PDF est le
recueil d'exercices, le 10 le formulaire : pas de vidéo prévue). Le chapitre 4 commence par le rappel
d'une vingtaine de secondes sur les νᵢ algébriques demandé par Thomas. Il a été refait le jour même
(voix plus dynamique, exercice résolu de calorimétrie en fin de vidéo) : la 1ʳᵉ version
(`1g0EXKxPFiU`, 7 min 21) reste en non répertorié sur YouTube, retirée du site.

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
