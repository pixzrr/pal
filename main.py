

from functions import alarms
from functions import presence
from functions import reminders
from functions import text_to_data

from devices import camera
from devices import display
from devices import esp32
from devices import microphone
from devices import speaker

from voice import speech_to_text
from voice import text_to_speech

from communication import mqtt

import random

# -------------------------------------------------------------------
# IHM

from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

ihm = FastAPI()

ihm.mount(
    "/pal/fichiers", # sous chemin pour récuperer les fichiers statiques
    StaticFiles(directory="interface"), #staticFiles : classe permettant de servir des fichiers statiques (css, js, images, etc.) depuis un répertoire donné (via le dossier interface ici)
    name="fichiers"
)

@ihm.get("/pal/") #lorsqu'il y a requête sur racine
def accueil():
    return FileResponse("interface/index.html")

@ihm.post("/pal/chat")
def recevoir_commande(message: str = Body(media_type="text/plain")): # Body(...) indique à FastAPI qu'on veut chercher la donnée dans le corps de la requête, et media_type="text/plain" indique que le corps de la requête est du texte brut (plain text)
    resultat = traiter_commande(message)
    return resultat

# -------------------------------------------------------------------

def traiter_commande(user_input):

    dispatch = {
        "none": 0,
        "alarms": {
            "create": alarms.set_alarm
        }
    }

    commande = text_to_data.comprendre_commande(user_input)

    # if commande["fonction"] == "none":
    #     return {
    #         "success": True,
    #         "message": "Aucune action n'a été effectuée."
    #     }

    if commande["fonction"] == "none":
        pass
    else:
        fonction = dispatch[commande["fonction"]][commande["action"]]
        fonction(commande["data"])

    return {
        "success": True,
        "message": commande["reponse"]
    }



# models_messages = {
#     1: "Que voulez-vous faire ?",
#     2: "Salut",
#     3: "Comme ça va ?"
# }

# choix_message = random.randint(1, 3)

# user_input = input(models_messages[choix_message])

# dispatch = {
#     "none": 0,
#     "alarms": {
#         "create": alarms.set_alarm
#     }
# }

# commande = text_to_data.comprendre_commande(user_input)

# if commande["fonction"] == "none":
#     print("Aucune action n'a été effectuée.")
# else:
#     fonction = dispatch[commande["fonction"]][commande["action"]]
#     fonction(commande["data"])