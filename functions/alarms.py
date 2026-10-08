from datetime import datetime, timedelta
import string
import re

class Alarm:
    def __init__(self, nom, heure, jours, intervalle, actions, jetable):
        self.nom = nom
        self.heure = heure
        self.jours = jours
        self.intervalle = intervalle
        self.actions = actions
        self.jetable = jetable # jetable = 1 => détruit après objectif ; jetable = 0 => répété les jours inscrits

    def __str__(self): #__str__ autre méthode de la classe Alarm : si qq1 veut transformer mon objet en texte, je lui fournis ...
        return f"{self.nom} - {self.heure} - {self.jours} - {self.intervalle} - {self.actions} - {self.jetable}" #f = formatted string => signifie qu'on peut ajouter des variables directement avec {} (comme en c++)

def set_alarm(donnees):
    nom_alarme = donnees["nom"]
    heure_alarme = donnees["heure"]
    jours_alarme = donnees["jours"]
    intervalle_alarme = donnees["intervalle"]
    actions_alarme = donnees["actions"]
    jetable_alarme = donnees["jetable"]

    print("Je crée une alarme avec :", nom_alarme, heure_alarme, jours_alarme, intervalle_alarme, actions_alarme, jetable_alarme)