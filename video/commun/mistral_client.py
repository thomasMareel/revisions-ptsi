"""Client Mistral du projet. La clé n'est jamais dans le dépôt :
- soit l'environnement cloud porte un « secret réseau » pour api.mistral.ai : la clé est ajoutée à
  chaque requête en dehors de la machine. La requête part alors SANS en-tête Authorization
  (le client en mettrait un faux, qui pourrait gêner) ;
- soit la variable d'environnement MISTRAL_API_KEY est définie, et elle est utilisée telle quelle."""
import os
from mistralai.client import Mistral

def client():
    cle = os.environ.get("MISTRAL_API_KEY")
    if cle: return Mistral(api_key=cle)
    import httpx2
    def sans_cle(requete): requete.headers.pop("authorization", None)
    return Mistral(api_key="secret-reseau",
                   client=httpx2.Client(event_hooks={"request": [sans_cle]}, timeout=180, follow_redirects=True))
