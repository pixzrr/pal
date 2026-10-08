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

# -------------------------------------------------------------------

texte = input("Que voulez-vous faire ? ")

fonctions = {
    "alarms": {
        "create": alarms.set_alarm
    }
}

commande = text_to_data.comprendre_commande(texte)

fonction = fonctions[commande["domain"]][commande["action"]]
fonction(commande["data"])