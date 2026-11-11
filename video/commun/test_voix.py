"""Essai réel de la voix (une phrase, moins d'un centime) : synthèse puis transcription de contrôle.
À lancer après avoir déposé la clé Mistral :  python3 video/commun/test_voix.py"""
import base64, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mistral_client import client
PHRASE = "Bonjour à tous, ceci est un essai de la voix du cours."
try:
    c = client()
    r = c.audio.speech.complete(model="voxtral-mini-tts-3", input=PHRASE, voice_id="voice_3141", response_format="mp3")
    mp3 = os.path.join(tempfile.gettempdir(), "essai_voix.mp3"); open(mp3, "wb").write(base64.b64decode(r.audio_data))
    tr = c.audio.transcriptions.complete(model="voxtral-mini-latest", file={"content": open(mp3, "rb"), "file_name": "a.mp3"}, language="fr").text
except Exception as e:
    msg = str(e)
    print("ÉCHEC :", msg[:300])
    if "401" in msg:
        print("→ Mistral ne reçoit pas de clé valable. Vérifier le secret réseau (hôte api.mistral.ai, en-tête Authorization,\n"
              "  préfixe Bearer) ; s'il vient d'être ajouté, ouvrir une nouvelle session. Voir video/MISE-EN-PLACE.md, partie A.")
    sys.exit(1)
print(f"Voix : OK ({os.path.getsize(mp3)//1000} ko, {mp3})")
print("Transcription de contrôle :", tr.strip())
print("Clé utilisée :", "variable MISTRAL_API_KEY" if os.environ.get("MISTRAL_API_KEY") else "secret réseau de l'environnement")
