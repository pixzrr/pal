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


    # -------------------------------------------
    intervalle_brute = donnees["intervalle"]
    intervalle_alarme = 0
    
    h = 0
    m = 0
    s = 0
    match_h = re.search(r"(\d+)\s*(?:h|heure|heures)\s*(?:avec|et|.)\s*(\d+)", intervalle_brute)
    match_m = re.search(r"(\d+)\s*(?:m|min|minute|minutes)\s*(?:avec|et|.)\s*(\d+)", intervalle_brute)
    #(\d+) → nombre d'heures     \s* → zéro ou plusieurs espaces       h → la lettre h       \s* → zéro ou plusieurs espaces     (\d+) → nombre de minutes    ?: → val. non recuperable
    
    if match_h:
        h = int(match_h.group(1))
        m = int(match_h.group(2))
    elif match_m:
        m = int(match_m.group(1))
        s = int(match_m.group(2))
    elif re.search(r"(s|sec|seconde|secondes)", intervalle_brute):
        s = int(re.search(r"(\d+)", intervalle_brute).group(1))
    elif re.search(r"(m|min|minute|minutes)", intervalle_brute):
        m = int(re.search(r"(\d+)", intervalle_brute).group(1))
    elif re.search(r"(h|heure|heures)", intervalle_brute):
        h = int(re.search(r"(\d+)", intervalle_brute).group(1))
    
    intervalle_alarme = h * 3600 + m * 60 + s
    # -------------------------------------------


    actions_alarme = donnees["actions"]
    jetable_alarme = donnees["jetable"]

    print("Je crée une alarme avec :", nom_alarme, heure_alarme, jours_alarme, intervalle_alarme, actions_alarme, jetable_alarme)