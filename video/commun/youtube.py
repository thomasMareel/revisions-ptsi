#!/usr/bin/env python3
"""Mise en ligne automatique d'un chapitre sur YouTube : vidéo non répertoriée, description, sous-titres.

Mise en place, une seule fois (guide pas à pas : video/MISE-EN-PLACE.md) :
    python3 video/commun/youtube.py lien                  adresse d'autorisation à ouvrir dans un navigateur
    python3 video/commun/youtube.py jeton "<adresse>"     termine l'autorisation (adresse de la page « localhost »)
    python3 video/commun/youtube.py test                  vérifie l'accès à la chaîne, sans rien envoyer
    python3 video/commun/youtube.py montrer-jeton         affiche le jeton à recopier dans l'environnement cloud

Pour chaque chapitre, DEPUIS son dossier, après assemble.py :
    python3 ../../commun/youtube.py envoi [--prive] [--synthetique] [--encore]

Identifiants : variables d'environnement YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN. Jamais dans le dépôt.
Bibliothèque standard seulement (aucune installation)."""
import os, sys, json, time, urllib.request, urllib.parse, urllib.error

AUTH = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN = os.environ.get("YT_TOKEN_URL", "https://oauth2.googleapis.com/token")   # ces deux adresses ne se
API = os.environ.get("YT_API_URL", "https://www.googleapis.com")                # changent que pour les essais
REDIRECT = "http://localhost:8765/"
PORTEES = "https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.force-ssl"
LOCAL = os.path.expanduser("~/.config/cours-video/youtube.json")   # hors du dépôt, propre à la session

AIDE = {
 "invalid_grant": "L'autorisation n'est plus valable : révoquée, ou application Google restée en mode « Test » "
                  "(elle expire alors au bout de 7 jours). Refaire « lien » puis « jeton ».",
 "invalid_client": "YT_CLIENT_ID ou YT_CLIENT_SECRET est incorrect.",
 "redirect_uri_mismatch": "Le client OAuth doit être de type « Application de bureau » (Desktop app).",
 "access_denied": "L'autorisation a été refusée dans le navigateur. En mode « Test », le compte doit figurer "
                  "parmi les utilisateurs de test ; le plus simple est de publier l'application.",
 "youtubeSignupRequired": "Ce compte Google n'a pas encore de chaîne YouTube : en créer une, puis recommencer.",
 "accessNotConfigured": "« YouTube Data API v3 » n'est pas activée dans le projet Google Cloud.",
 "quotaExceeded": "Quota quotidien de l'API atteint : réessayer demain (remise à zéro à minuit, heure du Pacifique).",
 "uploadLimitExceeded": "YouTube limite le nombre d'envois de cette chaîne : réessayer dans 24 h.",
 "insufficientPermissions": "L'autorisation ne couvre pas cette action : refaire « lien » puis « jeton ».",
}

def stop(msg): print("ÉCHEC :", msg); sys.exit(1)

def appel(methode, url, corps=None, entetes=None):
    req = urllib.request.Request(url, data=corps, method=methode, headers=entetes or {})
    try:
        with urllib.request.urlopen(req, timeout=900) as r: return r.status, r.headers, r.read()
    except urllib.error.HTTPError as e: return e.code, e.headers, e.read()
    except urllib.error.URLError as e: stop(f"réseau : {e.reason} ({url.split('?')[0]})")

def explique(code, corps, quoi):
    raison, detail = "", corps[:300].decode("utf-8", "replace")
    try:
        d = json.loads(corps); err = d.get("error")
        if isinstance(err, str): raison, detail = err, d.get("error_description", "")
        elif isinstance(err, dict):
            detail = err.get("message", detail); raison = (err.get("errors") or [{}])[0].get("reason", "") or err.get("status", "")
    except Exception: pass
    stop(f"{quoi} (HTTP {code}, {raison or 'sans motif'}) : {detail}" + (f"\n→ {AIDE[raison]}" if raison in AIDE else ""))

def identifiants():
    cid, sec = os.environ.get("YT_CLIENT_ID"), os.environ.get("YT_CLIENT_SECRET")
    if not cid or not sec:
        stop("YT_CLIENT_ID et YT_CLIENT_SECRET sont absents de l'environnement. Les ajouter aux variables de "
             "l'environnement cloud, puis ouvrir une NOUVELLE session (voir video/MISE-EN-PLACE.md, étape B4).")
    return cid.strip(), sec.strip()

def jeton_durable():
    if os.path.exists(LOCAL): return json.load(open(LOCAL))["refresh_token"]      # le plus récent
    if os.environ.get("YT_REFRESH_TOKEN"): return os.environ["YT_REFRESH_TOKEN"].strip()
    stop("aucune autorisation YouTube : lancer « lien » puis « jeton » (voir video/MISE-EN-PLACE.md, partie B).")

def acces():
    cid, sec = identifiants()
    corps = urllib.parse.urlencode({"client_id": cid, "client_secret": sec, "refresh_token": jeton_durable(), "grant_type": "refresh_token"}).encode()
    code, _, rep = appel("POST", TOKEN, corps, {"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200: explique(code, rep, "autorisation YouTube")
    return {"Authorization": "Bearer " + json.loads(rep)["access_token"]}

def cmd_lien():
    cid, _ = identifiants()
    q = urllib.parse.urlencode({"client_id": cid, "redirect_uri": REDIRECT, "response_type": "code", "scope": PORTEES,
                                "access_type": "offline", "prompt": "consent"})
    print("Adresse à ouvrir dans un navigateur, connecté au compte Google de la chaîne :\n")
    print(f"{AUTH}?{q}\n")
    print("Accepter (écran « application non validée » : Paramètres avancés → Accéder à l'application).\n"
          "La page finale ne s'affiche pas (localhost) : c'est normal. Copier son ADRESSE complète et lancer :\n"
          '    python3 video/commun/youtube.py jeton "<adresse copiée>"')

def cmd_jeton(arg):
    cid, sec = identifiants(); code_auth = arg.strip()
    if "code=" in arg or "error=" in arg:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(arg.strip()).query)
        if "error" in q: stop("Google a répondu « " + q["error"][0] + " ». " + AIDE.get(q["error"][0], ""))
        code_auth = q["code"][0]
    corps = urllib.parse.urlencode({"code": code_auth, "client_id": cid, "client_secret": sec, "redirect_uri": REDIRECT,
                                    "grant_type": "authorization_code"}).encode()
    code, _, rep = appel("POST", TOKEN, corps, {"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200: explique(code, rep, "échange du code (il ne sert qu'une fois et expire en quelques minutes : refaire « lien »)")
    d = json.loads(rep)
    if not d.get("refresh_token"): stop("Google n'a pas fourni de jeton durable : refaire « lien » (l'adresse force l'écran d'accord).")
    os.makedirs(os.path.dirname(LOCAL), exist_ok=True)
    with open(os.open(LOCAL, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600), "w") as f: json.dump({"refresh_token": d["refresh_token"]}, f)
    print("Autorisation enregistrée pour cette session. Vérifier : python3 video/commun/youtube.py test\n"
          "Pour la garder d'une session à l'autre : « montrer-jeton », puis recopier la valeur dans la variable\n"
          "YT_REFRESH_TOKEN de l'environnement cloud.")

def cmd_test():
    code, _, rep = appel("GET", f"{API}/youtube/v3/channels?part=snippet&mine=true", None, acces())
    if code != 200: explique(code, rep, "lecture de la chaîne")
    ch = json.loads(rep).get("items") or []
    if not ch: stop(AIDE["youtubeSignupRequired"])
    print(f"Accès YouTube : OK — chaîne « {ch[0]['snippet']['title']} ».")
    print("Jeton durable :", "session en cours seulement (penser à YT_REFRESH_TOKEN)" if os.path.exists(LOCAL) and not os.environ.get("YT_REFRESH_TOKEN") else "variable YT_REFRESH_TOKEN" if not os.path.exists(LOCAL) else "session en cours + variable")

def cmd_montrer():
    if not os.path.exists(LOCAL): stop("aucun jeton enregistré dans cette session (lancer « lien » puis « jeton »).")
    print("Valeur à recopier dans la variable YT_REFRESH_TOKEN de l'environnement cloud (elle donne accès à la gestion\n"
          "des vidéos de la chaîne : ne la mettre nulle part ailleurs ; révocable sur myaccount.google.com/permissions) :\n")
    print(json.load(open(LOCAL))["refresh_token"])

def cmd_envoi(options):
    if not os.path.exists("chapitre.json"): stop("à lancer depuis le dossier du chapitre (chapitre.json absent).")
    nom = json.load(open("chapitre.json", encoding="utf-8"))["fichier"]
    mp4, srt, fiche = f"out/{nom}.mp4", f"out/{nom}.srt", "out/youtube.txt"
    for f in (mp4, fiche):
        if not os.path.exists(f): stop(f"{f} absent : lancer d'abord assemble.py.")
    if os.path.exists("youtube.json") and "--encore" not in options:
        stop("ce chapitre est déjà en ligne (" + json.load(open("youtube.json"))["url"] + "). Un nouvel envoi crée une "
             "DEUXIÈME vidéo, avec une autre adresse : ajouter --encore pour le faire quand même.")
    lignes = open(fiche, encoding="utf-8").read().split("\n")
    titre, desc = lignes[0].strip()[:100], "\n".join(lignes[1:]).strip()[:4900]
    visibilite = "private" if "--prive" in options else "unlisted"
    meta = {"snippet": {"title": titre, "description": desc, "categoryId": "27", "defaultLanguage": "fr", "defaultAudioLanguage": "fr"},
            "status": {"privacyStatus": visibilite, "selfDeclaredMadeForKids": False, "embeddable": True}}
    if "--synthetique" in options: meta["status"]["containsSyntheticMedia"] = True
    h = acces(); taille = os.path.getsize(mp4)
    print(f"Envoi de {mp4} ({taille/1e6:.1f} Mo) — « {titre} »")
    code, ent, rep = appel("POST", f"{API}/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
                           json.dumps(meta).encode("utf-8"),
                           {**h, "Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(taille)})
    if code != 200 or not ent.get("Location"): explique(code, rep, "ouverture de l'envoi")
    with open(mp4, "rb") as f:
        code, _, rep = appel("PUT", ent["Location"], f, {**h, "Content-Type": "video/mp4", "Content-Length": str(taille)})
    if code not in (200, 201): explique(code, rep, "envoi de la vidéo")
    vid = json.loads(rep)["id"]
    bilan = {"id": vid, "url": f"https://youtu.be/{vid}", "integration": f"https://www.youtube-nocookie.com/embed/{vid}",
             "titre": titre, "visibilite": visibilite, "sous_titres": False, "date": time.strftime("%Y-%m-%d")}
    def note():
        with open("youtube.json", "w", encoding="utf-8") as f: f.write(json.dumps(bilan, ensure_ascii=False, indent=1) + "\n")
    note()                                              # écrit tout de suite : pas de second envoi par erreur
    if os.path.exists(srt):
        b = "limite-cours-video"
        corps = (f"--{b}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"
                 + json.dumps({"snippet": {"videoId": vid, "language": "fr", "name": "Français"}})
                 + f"\r\n--{b}\r\nContent-Type: application/octet-stream\r\n\r\n").encode("utf-8") + open(srt, "rb").read() + f"\r\n--{b}--\r\n".encode()
        code, _, rep = appel("POST", f"{API}/upload/youtube/v3/captions?uploadType=multipart&part=snippet", corps,
                             {**h, "Content-Type": f"multipart/related; boundary={b}"})
        if code in (200, 201): bilan["sous_titres"] = True; note()
        else: print(f"!! sous-titres non envoyés (HTTP {code}) : {rep[:200].decode('utf-8', 'replace')}\n   La vidéo est en ligne ; les ajouter à la main dans YouTube Studio ({srt}).")
    code, _, rep = appel("GET", f"{API}/youtube/v3/videos?part=status&id={vid}", None, h)
    reelle = ((json.loads(rep).get("items") or [{}])[0].get("status") or {}).get("privacyStatus") if code == 200 else None
    if reelle: bilan["visibilite"] = reelle; note()
    print(f"En ligne : {bilan['url']}   (visibilité : {reelle or 'non vérifiée'} ; sous-titres : {'oui' if bilan['sous_titres'] else 'non'})")
    if reelle and reelle != visibilite:
        print(f"!! YouTube a classé la vidéo « {reelle} » au lieu de « {visibilite} » : restriction possible des projets Google non\n"
              "   validés. Changer la visibilité à la main dans YouTube Studio et le signaler à Thomas.")
    print("Reporter le lien dans le tableau de video/README.md ; youtube.json (à versionner) garde l'identifiant.")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help", "aide"): print(__doc__)
    elif a[0] == "lien": cmd_lien()
    elif a[0] == "jeton" and len(a) > 1: cmd_jeton(a[1])
    elif a[0] == "test": cmd_test()
    elif a[0] == "montrer-jeton": cmd_montrer()
    elif a[0] == "envoi": cmd_envoi(a[1:])
    else: stop("commande inconnue ou incomplète.\n" + __doc__)
