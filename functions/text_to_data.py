def comprendre_commande(texte):

    commande = {
        "domain": "alarms",
        "action": "create",
        "data": {
            "nom": "Alarme de test",
            "heure": "08:00",
            "jours": ["demain"],
            "intervalle": "15min",
            "actions": ["allumer lampe chambre"],
            "jetable": 1
        }
    }

    return commande