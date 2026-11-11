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

## B. Automatique, par l'API YouTube (à mettre en place une fois, pas encore essayé)

Permet à une session Claude Code d'envoyer elle-même la vidéo, les sous-titres et la description.
À faire par Thomas, de préférence sur un ordinateur :

1. <https://console.cloud.google.com> → créer un projet → « API et services » → activer
   **YouTube Data API v3**.
2. Écran de consentement OAuth : type « Externe » ; ajouter son propre compte comme utilisateur ;
   puis **publier l'application** (« En production »). En mode « Test », l'autorisation expire au
   bout de 7 jours et tout serait à refaire chaque semaine.
3. Identifiants → créer un **ID client OAuth** de type « Application de bureau » : noter
   l'identifiant client et le code secret.
4. Lancer une session Claude Code et lui demander « mets en place l'envoi YouTube » : elle fournit
   une adresse à ouvrir, on accepte (écran « application non validée » → Paramètres avancés →
   Continuer), puis on lui recopie l'adresse de la page d'erreur `localhost` obtenue. Elle en tire
   un **jeton d'actualisation**.
5. Dans l'environnement cloud, ajouter trois variables : `YT_CLIENT_ID`, `YT_CLIENT_SECRET`,
   `YT_REFRESH_TOKEN`. Jamais dans le dépôt.

Repères pour la session qui écrira le script d'envoi (`video/commun/youtube.py`, à créer) :

- `videos.insert` (`part=snippet,status`, envoi « resumable »), `status.privacyStatus = "unlisted"`,
  `status.selfDeclaredMadeForKids = false`, `status.containsSyntheticMedia` selon la règle ci-dessus ;
  portées OAuth `youtube.upload` et `youtube.force-ssl` (sous-titres : `captions.insert`) ;
- la référence officielle de `videos.insert` indiquait le 11/11/2026 que les envois d'un projet non
  validé ne sont **plus** forcés en privé ; plusieurs guides plus anciens disent l'inverse. Vérifier
  sur la première vidéo envoyée que « non répertoriée » est bien respecté ;
- les domaines `*.googleapis.com` font partie de la liste « Trusted » des environnements cloud ;
- la première vidéo envoyée sert de test : la contrôler dans Studio avant d'automatiser la suite.
