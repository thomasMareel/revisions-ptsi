# Mettre en service l'assistant IA (phase 1 : discussion écrite)

Ce guide se suit **une étape à la fois**. Ce qui est déjà prêt dans le dépôt : le panneau de
l'assistant sur le site, le **relais** (`assistant/relais/`, un petit programme Cloudflare Worker
qui garde la clé de l'API Claude et vérifie ton code d'accès) et ses tests. Il reste à créer deux
comptes, à déployer le relais, à y ranger trois secrets, puis à brancher le site dessus.

> **Règle d'or.** Une clé d'API ou ton code d'accès ne se colle **jamais** dans une conversation
> avec Claude, ni dans un fichier du dépôt (il est public). On les tape uniquement dans les consoles
> (Anthropic, Cloudflare) ou dans le terminal quand `wrangler` les demande.

Pourquoi un relais ? Le site est public : une clé écrite dans la page serait lisible par tout le
monde, qui pourrait s'en servir à tes frais. Le relais garde la clé, n'accepte que les appareils
qui connaissent ton code, plafonne la dépense du jour (1,50 $ par défaut) et transmet la réponse de
Claude au fur et à mesure.

## Étape 1 — Compte de l'API Claude (Console Anthropic)

L'API se paie **à part** d'un abonnement Claude (Pro, Max) : c'est un compte distinct, prépayé.

1. Crée un compte sur la Console Claude : <https://platform.claude.com> (avec ton adresse habituelle).
2. Ajoute un moyen de paiement et un petit crédit (10 $ suffisent pour commencer : une
   conversation de dix questions coûte de 0,05 à 0,20 $).
3. Crée un **espace de travail** dédié, par exemple « assistant-revisions », et fixe-lui une
   **limite de dépense mensuelle** (par exemple 10 $) : c'est le filet de sécurité ultime.
4. Dans cet espace, crée une **clé d'API** (nom : « relais-revisions »). La Console ne l'affiche
   qu'une fois : laisse la page ouverte, elle sert à l'étape 4. Ne la copie nulle part ailleurs.

## Étape 2 — Compte Cloudflare (gratuit)

1. Crée un compte sur <https://dash.cloudflare.com/sign-up>.
2. Dans « Workers & Pages », choisis ton sous-domaine `workers.dev` (par exemple
   `thomas-revisions`). L'adresse du relais sera `https://revisions-assistant.<sous-domaine>.workers.dev`.

## Étape 3 — Déployer le relais

**Option A, sur ton PC Windows** (il faut Node.js « LTS » : <https://nodejs.org>) :

1. Ouvre un terminal **dans le dossier** `revisions-ptsi\assistant\relais`.
2. `npm install`
3. `npx wrangler login` (une page Cloudflare s'ouvre : accepte).
4. `npx wrangler kv namespace create COMPTEURS` : recopie l'`id` affiché dans `wrangler.toml`, à
   la place de `A_REMPLACER_PAR_L_ID_DU_NAMESPACE` (un id n'est pas un secret : tu peux me le donner
   et je le recopie).
5. `npx wrangler deploy` : note l'adresse affichée, en `…workers.dev`.

**Option B, depuis une session Claude Code** : dans Cloudflare, « My Profile › API Tokens › Create
Token », modèle **« Edit Cloudflare Workers »**. Puis demande-moi de déployer : j'ouvrirai le
formulaire sécurisé où tu enregistres ce jeton comme secret réseau de l'environnement (je ne vois
jamais sa valeur), et je fais les étapes 3 et 5.

## Étape 4 — Les trois secrets du relais

Dans le tableau de bord Cloudflare : **Workers & Pages › revisions-assistant › Settings ›
Variables and Secrets › Add**, type **Secret** (les intitulés peuvent varier un peu). Ou, dans le
terminal de l'option A, `npx wrangler secret put NOM` puis tape la valeur quand on te la demande.

| Nom | Valeur |
|---|---|
| `ANTHROPIC_API_KEY` | la clé créée à l'étape 1 |
| `ASSISTANT_CODE` | **ton code d'accès** : une phrase de passe longue que tu inventes (au moins 4 ou 5 mots) ; tu la taperas une fois par appareil |
| `JETON_CLE` | une longue chaîne au hasard (40 caractères tapés n'importe comment) : elle signe les jetons des appareils |

Vérification : ouvre `https://revisions-assistant.<sous-domaine>.workers.dev/sante` dans le
navigateur ; la page doit afficher `{"ok":true,…}`.

## Étape 5 — Brancher le site

Donne-moi l'adresse du relais (elle n'est pas secrète) : je l'écris dans `assistant/assistant.js`
(constante `RELAIS`), je lance les tests et je publie.

## Étape 6 — Sur chaque appareil

1. Ouvre une fois `https://thomasmareel.github.io/revisions-ptsi/?assistant=1` : le bouton
   « Assistant » apparaît (en-tête à l'ordinateur, menu ⋯ au téléphone).
2. Ouvre l'assistant, tape ton code d'accès : l'appareil reçoit un jeton valable 30 jours, rangé
   hors de la Sauvegarde (il n'est jamais exporté).

## En cas de problème

- **Appareil perdu, ou jeton à révoquer** : change `JETON_CLE` (étape 4) ; tous les appareils
  devront retaper le code.
- **Code d'accès connu de quelqu'un d'autre** : change `ASSISTANT_CODE`, puis `JETON_CLE`.
- **Clé d'API exposée par erreur** : supprime-la dans la Console Anthropic, crées-en une autre et
  remplace `ANTHROPIC_API_KEY`.
- **« Budget du jour atteint »** : le plafond `BUDGET_JOUR_USD` de `wrangler.toml` (1,50 $) est
  atteint ; il repart chaque jour à minuit UTC (1 h du matin à Paris, 2 h en été). Pour le changer : modifier la valeur
  puis redéployer.
- **Retirer le bouton d'un appareil** : ouvrir l'adresse du site suivie de `?assistant=0`.
