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

    print("Bien sûr.")
    nom_alarme = input("Comment voulez-vous appeler votre alarme ?")


    heures_lettre = {
        "minuit": 0,
        "midi": 12
    }

    heure_brute = input("À quelle heure ?")

    match_alarme = re.search(r"(minuit|midi|\d+)\s*(?:h|:|heure|heures)?\s*((\d+)|\s*)", heure_brute)

    if match_alarme.group(1) in heures_lettre:
        heure = heures_lettre[match_alarme.group(1)]
    else:
        heure = int(match_alarme.group(1))

    if match_alarme.group(2).strip():
        minute = int(match_alarme.group(2)) #group() renvoit un string
    else:
        minute = 0

    heure_alarme = f"{heure:02d}:{minute:02d}"


    jours_semaine = {
        "lundi": 0,
        "mardi": 1,
        "mercredi": 2,
        "jeudi": 3,
        "vendredi": 4,
        "samedi": 5,
        "dimanche": 6
    }

    jours_relatifs = {
        "aujourd'hui": 0,
        "demain": 1,
        "après-demain": 2,
        "après après-demain": 3,
        "dans un jour": 1,
        "dans deux jours": 2,
        "dans trois jours": 3,
        "dans quatre jours": 4,
        "dans cinq jours": 5,
    }

    reponse_brute = input("Quels jours ?").lower()
    jours_alarme = []

    if re.search(r"(semaine|jours|temps|quot)", reponse_brute):
        jours_alarme = [0, 1, 2, 3, 4, 5, 6]
    else:
        for i in jours_semaine:
            if i in reponse_brute and jours_semaine[i] not in jours_alarme:
                jours_alarme.append(jours_semaine[i])

        for i in jours_relatifs:
            if i in reponse_brute and jours_relatifs[i] not in jours_alarme:
                jours_alarme.append(jours_relatifs[i])
        
    if not "tous" in reponse_brute and not "les" in reponse_brute and not "toutes" in reponse_brute:
        jetable_alarme = 1
    else :
        jetable_alarme = 0


    intervalle_brute = input("Quel intervalle entre les répétitions ?") #en sec
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

    actions_alarme = [] #à coder plus tard
    #actions_alarme.append("allumer lampe chambre")


    alarme1 = Alarm(nom_alarme, heure_alarme, jours_alarme, intervalle_alarme, actions_alarme, jetable_alarme)

    print(alarme1)