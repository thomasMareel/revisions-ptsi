# Mettre une vidéo en ligne sur YouTube

Les vidéos sont publiées en **non répertorié** : visibles par quiconque a le lien, absentes de la
recherche et de la chaîne. Le site pointe vers elles.

Pour chaque chapitre, `assemble.py` prépare dans `out/` :

- `<fichier>.mp4` : la vidéo ;
- `<fichier>.srt` : les sous-titres français ;
- `youtube.txt` : le titre, la description (avec les chapitres et la mention « voix de synthèse »).

## A. À la main (fonctionne aujourd'hui)

1. Récupérer le MP4 et le SRT (la session Claude Code les envoie dans la conversation).
2. YouTube Studio → Créer → Importer une vidéo → choisir le MP4.
3. Titre et description : copier `youtube.txt`. Audience : « Non, pas conçue pour les enfants ».
4. Visibilité : **Non répertoriée**.
5. Sous-titres : Studio, de préférence dans un navigateur → Sous-titres
   → Ajouter une langue : français → Importer un fichier → « Avec minutage » → le SRT.
6. Copier le lien de la vidéo et le donner à la session pour l'ajouter au site et au tableau de
   `video/README.md`.

Contenu modifié ou synthétique : YouTube demande une déclaration pour un contenu **réaliste**
(faire dire à une vraie personne ce qu'elle n'a pas dit, scène réaliste inventée). Un tableau animé
avec une narratrice de synthèse n'entre pas dans ces cas ; répondre « Oui » ne pénalise pas la vidéo.

## B. Automatique, depuis une session Claude Code

Une fois l'autorisation en place (**`MISE-EN-PLACE.md`, partie B**, à faire une seule fois), depuis
le dossier du chapitre, après `assemble.py` :

```
python3 ../../commun/youtube.py envoi
```

Le script envoie le MP4 en **non répertorié** avec le titre et la description de `out/youtube.txt`
(catégorie Éducation, langue française), ajoute les sous-titres du SRT, relit la visibilité réellement
appliquée par YouTube et écrit `youtube.json` (identifiant, lien, adresse d'intégration). Il refuse
de renvoyer un chapitre déjà en ligne, sauf avec `--encore`.

Repères techniques :

- `videos.insert` en envoi « resumable », puis `captions.insert` ; portées OAuth `youtube.upload` et
  `youtube.force-ssl` ; identifiants dans `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN` ;
- la référence officielle de `videos.insert` indiquait le 11/11/2026 que les envois d'un projet non
  validé ne sont **plus** forcés en privé ; des guides plus anciens disent l'inverse. Le script
  signale tout écart entre la visibilité demandée et celle appliquée ;
- quota par défaut : une centaine d'envois par jour, très au-dessus du besoin ;
- les domaines `*.googleapis.com` font partie de la liste « Trusted » des environnements cloud ;
- le script n'a été essayé que contre un faux serveur reproduisant ces échanges : le premier envoi
  réel sert de test (étape B8 de `MISE-EN-PLACE.md`).
