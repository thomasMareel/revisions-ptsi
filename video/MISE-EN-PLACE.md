# Mise en place, à faire une seule fois

Guide que **la session Claude Code suit avec Thomas** pour brancher les deux services dont les
cours vidéo ont besoin :

- **A. la voix** : déposer la clé Mistral dans l'environnement cloud (2 minutes, possible au téléphone) ;
- **B. YouTube** : autoriser l'envoi automatique des vidéos (20 minutes, ordinateur conseillé).

## Règles pour la session

- **Une étape à la fois.** Donner l'étape, attendre que Thomas dise que c'est fait, vérifier avec la
  commande prévue, puis seulement passer à la suivante. Thomas débute : phrases courtes, où cliquer, quoi coller.
- **Aucun secret dans la conversation ni dans le dépôt.** Ne jamais demander à Thomas de coller sa
  clé Mistral ou son code secret Google dans la discussion : il les saisit lui-même dans les réglages
  de l'environnement. Ne jamais afficher une variable d'environnement. Seule exception, inévitable :
  le jeton YouTube de l'étape B7, affiché une fois pour que Thomas le recopie.
- **Les écrans changent.** Les intitulés ci-dessous datent de novembre 2026. S'ils ne correspondent
  pas à ce que Thomas voit, chercher la documentation actuelle (Claude Code : « cloud environments » ;
  Google : « YouTube Data API, OAuth 2.0 for installed applications ») plutôt que deviner.
- Les réglages de l'environnement se font dans l'interface de Claude Code ; la session ne peut pas
  les modifier elle-même.
- Commencer par `bash video/installer.sh` et lire le contrôle final.

## A. La voix : clé Mistral

Thomas a déjà créé sa clé dans la console Mistral (formule à l'usage, plafond de dépenses réglé).

**A1 — Thomas.** Dans Claude Code, ouvrir les réglages de l'environnement cloud utilisé pour ce
dépôt (sélecteur d'environnement, puis l'icône de réglages de l'environnement). Dans la section
**« Network secrets »**, choisir « Add secret » et remplir :

| Champ | Valeur |
|---|---|
| Name | `Mistral` |
| Secret type | `Bearer` (par défaut) |
| Allowed websites | `api.mistral.ai` |
| Custom headers | nom `Authorization`, préfixe `Bearer`, valeur : la clé Mistral |

Valider avec « Add ». La valeur n'est plus consultable ensuite : c'est voulu. Avec ce réglage, la
clé est ajoutée aux requêtes en dehors de la machine ; la session ne la voit jamais, et
`api.mistral.ai` devient joignable sans autre réglage réseau.

**A2 — Session.** Vérifier :

```
bash video/installer.sh              # attendu : « ok voix Mistral (clé acceptée) »
python3 video/commun/test_voix.py    # attendu : « Voix : OK » et la phrase retranscrite
```

Si la réponse reste 401 une minute après l'ajout, demander à Thomas d'ouvrir une nouvelle session
(« reprends video/MISE-EN-PLACE.md à l'étape A2 »).

**A3 — Repli**, seulement si le secret réseau ne fonctionne pas : dans les mêmes réglages, champ
« Environment variables », ajouter une ligne `MISTRAL_API_KEY=<la clé>` (sans guillemets), puis
ouvrir une nouvelle session. Moins protégé : toute session de l'environnement peut lire la valeur.

Jamais essayé avant cette mise en place : le secret réseau avec ce projet. Les scripts envoient
leurs requêtes sans en-tête `Authorization` quand `MISTRAL_API_KEY` est absente, pour laisser le
secret réseau le poser.

## B. YouTube : envoi automatique

Préalable : le compte Google de Thomas a une **chaîne YouTube** (sinon : youtube.com → « Créer une chaîne »).

**B1 — Thomas : projet Google.** Sur <https://console.cloud.google.com> : créer un projet (nom
libre, par exemple « Cours video »). Puis « API et services » → « Bibliothèque » → chercher
**YouTube Data API v3** → « Activer ».

**B2 — Thomas : écran d'accord.** « API et services » → « Écran de consentement OAuth » (ou
« Google Auth Platform ») : type d'utilisateurs **Externe**, nom de l'application libre, son adresse
e-mail comme contact. Puis, dans « Audience », **« Publier l'application »** (état « En production »).
C'est indispensable : en mode « Test », l'autorisation expire au bout de 7 jours. Aucune validation
par Google n'est à demander pour un usage personnel ; un écran d'avertissement apparaîtra à l'étape B5.

**B3 — Thomas : identifiants.** « Identifiants » (ou « Clients ») → « Créer des identifiants » →
« ID client OAuth » → type **« Application de bureau »**. Google affiche un **ID client** et un
**code secret** : les garder sous les yeux pour l'étape suivante.

**B4 — Thomas : les ranger dans l'environnement.** Dans les réglages de l'environnement cloud,
champ « Environment variables », ajouter deux lignes (sans guillemets ni espaces) :

```
YT_CLIENT_ID=<ID client>
YT_CLIENT_SECRET=<code secret>
```

Enregistrer, puis **ouvrir une nouvelle session** sur le dépôt avec le message :
« reprends video/MISE-EN-PLACE.md à l'étape B5 ». Une session déjà ouverte ne voit pas les
nouvelles variables.

**B5 — Session, puis Thomas : autoriser.**

```
python3 video/commun/youtube.py lien
```

Donner l'adresse affichée à Thomas. Il l'ouvre, choisit le compte (et la chaîne) des cours, passe
l'écran « Google n'a pas validé cette application » (« Paramètres avancés » → « Accéder à … »),
coche les autorisations et accepte. Le navigateur arrive alors sur une page **qui ne s'affiche pas**
(adresse commençant par `http://localhost:8765/`) : c'est normal. Thomas copie **l'adresse complète**
de cette page et la colle dans la conversation. Elle contient un code à usage unique, valable
quelques minutes et inutilisable sans le code secret.

**B6 — Session : terminer et vérifier.**

```
python3 video/commun/youtube.py jeton "<adresse collée par Thomas>"
python3 video/commun/youtube.py test      # attendu : « Accès YouTube : OK — chaîne « … » »
```

Faire confirmer à Thomas que le nom affiché est bien celui de sa chaîne.

**B7 — Rendre l'autorisation durable.** L'autorisation n'existe pour l'instant que dans cette
session. Prévenir Thomas, puis :

```
python3 video/commun/youtube.py montrer-jeton
```

Thomas recopie la valeur affichée dans une troisième variable de l'environnement,
`YT_REFRESH_TOKEN=<valeur>`. Lui dire clairement : cette valeur permet de gérer les vidéos de sa
chaîne ; elle ne va nulle part ailleurs, et il peut la révoquer à tout moment sur
<https://myaccount.google.com/permissions>. Les sessions suivantes fonctionneront sans rien refaire.

**B8 — Premier envoi réel : c'est le test.** Le script n'a été essayé que contre un faux serveur :
le premier envoi valide tout. Depuis le dossier d'un chapitre assemblé :

```
python3 ../../commun/youtube.py envoi
```

Puis demander à Thomas de vérifier dans YouTube Studio : visibilité **Non répertoriée**, description
et chapitres, sous-titres français, lecture correcte. Deux points à surveiller :

- si le script signale une visibilité « private » au lieu de « unlisted », Google bride encore les
  projets non validés : Thomas passe la vidéo en « Non répertoriée » à la main dans Studio, et on
  note ici que ce geste reste nécessaire ;
- si les sous-titres sont refusés, la vidéo reste en ligne : les ajouter à la main (`video/YOUTUBE.md`, partie A).

Options de `envoi` : `--prive` (vidéo privée, pour un essai), `--synthetique` (déclare un contenu
synthétique réaliste ; inutile pour un tableau animé), `--encore` (renvoie un chapitre déjà en
ligne : cela crée une **deuxième** vidéo).

## C. Une fois tout branché

- Noter dans ce fichier la date et ce qui a été constaté (secret réseau : oui ou repli ; visibilité
  respectée : oui ou non), et retirer les mentions « jamais essayé ».
- Chaque envoi écrit `youtube.json` dans le dossier du chapitre : le versionner, et reporter le lien
  dans le tableau « Vidéos livrées » de `video/README.md`.
- **Chapitres 1 à 3 de thermochimie** : leurs MP4 ont été fabriqués avant ce dépôt et ne sont pas
  dans la machine de la session. Thomas les possède (fichiers `Thermochimie_Chapitre1..3.mp4` et
  `.srt`). Soit il les envoie à la main (`video/YOUTUBE.md`, partie A) et donne les liens, soit il les
  met à disposition de la session, qui les place dans `out/` du chapitre et lance `envoi`.
  Ne pas les régénérer sans son accord : la voix serait différente de celle qu'il a validée.
- Ensuite : chapitre 4 de thermochimie (`video/README.md`).
