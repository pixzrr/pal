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

models_messages = {
    1: "Que voulez-vous faire ?",
    2: "Salut",
    3: "Comme ça va ?"
}

choix_message = random.randint(1, 3)

user_input = input(models_messages[choix_message])

dispatch = {
    "none": 0,
    "alarms": {
        "create": alarms.set_alarm
    }
}

commande = text_to_data.comprendre_commande(user_input)

if commande["fonction"] == "none":
    print("Aucune action n'a été effectuée.")
else:
    fonction = dispatch[commande["fonction"]][commande["action"]]
    fonction(commande["data"])