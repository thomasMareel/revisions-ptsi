# Mise en place, à faire une seule fois

Guide que **la session Claude Code suit avec Thomas** pour brancher les deux services dont les
cours vidéo ont besoin :

- **A. la voix** : déposer la clé Mistral dans l'environnement cloud (2 minutes, possible au téléphone) ;
- **B. YouTube** : autoriser l'envoi automatique des vidéos (20 minutes ; faisable au téléphone).

**Où en est-on (2026-11-11)** : partie A **faite** ; partie B faite jusqu'à B7 (projet Google « Cours
video PTSI », application « En production », client « Application de bureau » ; `YT_CLIENT_ID`,
`YT_CLIENT_SECRET` et `YT_REFRESH_TOKEN` enregistrées sur l'environnement « revisions-ptsi » par le
site claude.ai/code : l'application mobile n'offre pas ce réglage ; autorisation donnée sur la chaîne
« La Vengeance en Prépa »). Autorisation durable **vérifiée** dans une nouvelle session le
2026-11-11 (`python3 video/commun/youtube.py test` → « Accès YouTube : OK », « Jeton durable : variable
YT_REFRESH_TOKEN »). B8 **faite** le même jour : chapitres 1 à 3 de thermochimie en ligne, non
répertoriés, sous-titres compris (liens : tableau « Vidéos livrées » de `video/README.md`). **La mise
en place est terminée** ; reste à Thomas un coup d'œil dans YouTube Studio (fin de B8).

**Environnement cloud dédié « revisions-ptsi »** (personnel, créé le 2026-11-11 à la demande de
Thomas) : il porte le secret réseau Mistral et portera les variables YouTube ; « Default » n'en a
aucun. **Toute session vidéo doit tourner sur cet environnement** : le choisir à l'ouverture de la
session (sélecteur d'environnement). Une session ouverte sur « Default » ne voit ni la clé ni les
identifiants (`test_voix.py` : 401 ; `youtube.py` : « YT_CLIENT_ID et YT_CLIENT_SECRET sont absents »).

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

**Fait le 2026-11-11** par la voie la plus simple : la session a ouvert le **formulaire sécurisé de
dépôt d'un secret** de Claude Code (hôte `api.mistral.ai`, type Bearer, nom « Mistral ») et Thomas y a
collé sa clé ; le secret est enregistré sur l'environnement « revisions-ptsi ». Contrôle A2 réussi
(« clé acceptée », « Voix : OK », transcription exacte, clé passée par le secret réseau). Le repli
A3 n'a pas servi. Les étapes ci-dessous restent la voie manuelle, si le secret est à refaire.

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

Essayé et validé le 2026-11-11 : le secret réseau avec ce projet. Les scripts envoient leurs
requêtes sans en-tête `Authorization` quand `MISTRAL_API_KEY` est absente, pour laisser le secret
réseau le poser.

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

Constaté le 2026-11-11 (Google Auth Platform) :

- **pas de logo** : pour une application Externe en production, un logo déclenche la vérification
  de la marque, et il reste masqué tant qu'elle n'est pas faite ;
- **« Publier l'application » reste grisé** (« terminer sa configuration sur la page de branding »)
  tant que la page **Branding** n'a pas ses liens, même pour un usage personnel. Valeurs retenues :
  page d'accueil et règles de confidentialité = `https://thomasmareel.github.io/revisions-ptsi/`,
  conditions d'utilisation vides, domaine autorisé `thomasmareel.github.io`. Publication acceptée
  ensuite, sans demande de vérification.

**B3 — Thomas : identifiants.** « Identifiants » (ou « Clients ») → « Créer des identifiants » →
« ID client OAuth » → type **« Application de bureau »**. Google affiche un **ID client** et un
**code secret** : les garder sous les yeux pour l'étape suivante. Le code secret n'est montré
**qu'une fois** (sinon : en ajouter un nouveau dans la fiche du client). Case « Utiliser ce client
pour un agent basé sur l'IA » : **décochée** (elle ne concerne que les serveurs MCP de Google
Workspace ; `youtube.py` appelle l'API REST de YouTube ; choix figé par Google après le 12/11/2026).

**B4 — Thomas : les ranger dans l'environnement.** Dans les réglages de l'environnement cloud
**« revisions-ptsi »** (pas « Default »), champ « Environment variables », ajouter deux lignes (sans
guillemets ni espaces). Ce réglage n'existe pas dans l'application Claude du téléphone : passer par
**claude.ai/code** dans le navigateur (session ouverte → flèche ⌄ après le titre → « Edit cloud
environment » → « Environment variables » → « Save changes »). Le formulaire sécurisé des secrets
réseau ne convient pas ici : l'ID client doit être lisible par la session (adresse de B5) et le
code secret part dans le corps de la requête, pas dans un en-tête. La session peut vérifier les
**noms** des variables enregistrées (outil d'environnement), jamais leurs valeurs.

```
YT_CLIENT_ID=<ID client>
YT_CLIENT_SECRET=<code secret>
```

Enregistrer, puis **ouvrir une nouvelle session** sur le dépôt, **sur l'environnement
« revisions-ptsi »**, avec le message : « reprends video/MISE-EN-PLACE.md à l'étape B5 ». Une
session déjà ouverte ne voit pas les nouvelles variables. Les étapes B5 à B7 n'ont pas besoin de
`installer.sh` (`youtube.py` n'utilise que la bibliothèque standard) ; les adresses Google
(`oauth2.googleapis.com`, `www.googleapis.com`) sont joignables depuis cet environnement (vérifié
le 2026-11-11).

**B5 — Session, puis Thomas : autoriser.** Contrôler d'abord, **sans afficher les valeurs**, que les
deux variables sont là et bien formées (ID en `….apps.googleusercontent.com`, secret en `GOCSPX-…`,
ni espace ni guillemet), par exemple avec un petit script Python qui n'imprime que des booléens.

```
python3 video/commun/youtube.py lien
```

Donner l'adresse affichée à Thomas. Il l'ouvre, choisit le compte (et la chaîne) des cours, passe
l'écran « Google n'a pas validé cette application » (« Paramètres avancés » → « Accéder à … »),
coche les autorisations et accepte. Le navigateur arrive alors sur une page **qui ne s'affiche pas**
(adresse commençant par `http://localhost:8765/`) : c'est normal. Thomas copie **l'adresse complète**
de cette page et la colle dans la conversation. Elle contient un code à usage unique, valable
quelques minutes et inutilisable sans le code secret. Thomas a demandé qu'on ne lui fasse jamais
coller de clé ni de code secret : lui expliquer avant que cette adresse n'est ni sa clé ni le code
secret du client, et pourquoi elle peut transiter par la conversation.

**B6 — Session : terminer et vérifier.**

```
python3 video/commun/youtube.py jeton "<adresse collée par Thomas>"
python3 video/commun/youtube.py test      # attendu : « Accès YouTube : OK — chaîne « … » »
```

Faire confirmer à Thomas que le nom affiché est bien celui de sa chaîne.

**B5 et B6 faites le 2026-11-11** : variables bien formées, adresse `localhost` collée par Thomas,
échange réussi du premier coup. Chaîne autorisée : « La Vengeance en Prépa ». Thomas l'a renommée
lui-même ce jour-là : **l'API ne peut pas renommer une chaîne** (`channels.update` répond
`channelTitleUpdateForbidden`, quelle que soit l'autorisation). Cela se fait dans l'application YouTube
(photo de profil → la chaîne → crayon → Nom) ou sur studio.youtube.com (Personnalisation → Profil),
**2 fois au plus tous les 14 jours** ; l'autorisation, liée à la chaîne et non à son nom, reste valable.

**B7 — Rendre l'autorisation durable.** L'autorisation n'existe pour l'instant que dans cette
session. Prévenir Thomas, puis :

```
python3 video/commun/youtube.py montrer-jeton
```

Thomas recopie la valeur affichée dans une troisième variable de l'environnement,
`YT_REFRESH_TOKEN=<valeur>`. Lui dire clairement : cette valeur permet de gérer les vidéos de sa
chaîne ; elle ne va nulle part ailleurs, et il peut la révoquer à tout moment sur
<https://myaccount.google.com/permissions>. Les sessions suivantes fonctionneront sans rien refaire.

**Fait le 2026-11-11**, avec un obstacle : en mode **Auto**, le contrôle de sécurité de Claude Code
refuse `montrer-jeton` (affichage d'un identifiant), **même après l'accord de Thomas** dans la
conversation. Solution retenue : Thomas passe le sélecteur de mode (à côté de la zone de saisie) sur
**« Accept edits »**, la session relance la commande, Thomas l'autorise dans la demande qui s'affiche,
puis remet « Auto ». La variable a été enregistrée par claude.ai/code ; son nom est vérifiable par
l'outil d'environnement, sa valeur seulement par `youtube.py test` dans une **nouvelle** session.
**Vérifié le 2026-11-11** dans une nouvelle session sur « revisions-ptsi », sans autorisation locale
(`~/.config/cours-video/youtube.json` absent) : variable présente et bien formée (forme `1//…`, ni
espace ni guillemet), échange accepté par Google, chaîne « La Vengeance en Prépa » lue, « Jeton
durable : variable YT_REFRESH_TOKEN ». Le titre renvoyé par l'API finit par une espace (à retoucher
dans YouTube Studio si ce n'est pas voulu ; sans effet sur l'envoi).
Repli si l'on ne veut pas afficher le jeton : pas de `YT_REFRESH_TOKEN`, et refaire B5-B6 (≈ 1 minute)
dans chaque session qui envoie une vidéo.

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

**Fait le 2026-11-11** avec les chapitres 1 à 3 de thermochimie (voir C) : trois envois réussis du
premier coup, visibilité **non répertoriée respectée** (aucun bridage « private » du projet non
validé), sous-titres acceptés (piste « Français », état `serving`), titre, description, catégorie
Éducation, langue et « pas pour les enfants » relus par l'API. Le geste manuel de repli n'a pas servi.

## C. Une fois tout branché

- Constaté le 2026-11-11 : secret réseau Mistral **oui** (pas de repli) ; visibilité non répertoriée
  **respectée** ; sous-titres envoyés par l'API.
- Chaque envoi écrit `youtube.json` dans le dossier du chapitre : le versionner, reporter le lien
  dans le tableau « Vidéos livrées » de `video/README.md` et ajouter la vidéo à l'onglet « Vidéos »
  du site (table `window.__VIDEOS` et image d'aperçu : `video/README.md`, « Intégration au site »).
- **Chapitres 1 à 3 de thermochimie : en ligne** (2026-11-11). Leurs MP4 avaient été fabriqués avant
  ce dépôt ; Thomas les a joints à la conversation (MP4 + SRT). Avant l'envoi, la session a vérifié
  qu'ils correspondent aux `timeline.json` du dépôt (durée au centième, chapitres intégrés, SRT
  identique octet pour octet à celui que recalcule `assemble.py`), les a placés dans `out/` et a écrit
  `out/youtube.txt` avec le code même d'`assemble.py` (sans relancer le montage). Même démarche pour
  tout MP4 livré hors session. Ne pas les régénérer sans l'accord de Thomas : la voix serait
  différente de celle qu'il a validée.
- Ensuite : chapitre 4 de thermochimie (`video/README.md`).
