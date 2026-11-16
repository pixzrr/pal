import ollama
import json


def comprendre_commande(texte):

    retour = {
        "fonction": "",
        "action": "",
        "data": {}
    }

    # ===================================================================== Etape 1 : Définir fonction ==================================================================

    format_reponse_fonction = {
        "type": "object",
        "properties": {
            "reponse": {
                "type": "string", 
                "description": "La réponse à fournir à l'utilisateur en français, avec espaces et phrase polie"
            },
            "fonction": {
                "type": "string",
                "description": "Le nom de la fonction à exécuter",
                "enum": ["none", "alarms"]
            }
        },
        "required": ["reponse", "fonction"]
    }

    reponse_fonction = ollama.chat(
    model = "ministral-3:8b",
    messages = [
        {
            "role": "system",
            "content": "Tu es un assistant domestique. Tu ne contrôles pas directement les appareils. Ton rôle est de convertir les demandes de l'utilisateur en commandes structurées. Si l'utilisateur demande une fonction non disponible ou s'il pose une autre question, mets fonction = 'none'. C'est toi qui paramètre la fonction, et réponds à l'utilisateur. L'affichage des réglages n'est pas ta tache. Tu envoies les bons réglages et confirmes simplement à l'utilisateur que la commande a été prise en compte. Si l'utilisateur demande une fonction non disponible, réponds simplement que tu ne peux pas faire ça."
        },
        {
            "role": "user",
            "content": texte
        }
    ],
    format = format_reponse_fonction,
    )

    reponse_fonction = json.loads( #on remplace le tableau déjà existant par un dico python pour le traitement plus tard
        reponse_fonction["message"]["content"]
    )

    retour["fonction"] = reponse_fonction["fonction"]
    print(reponse_fonction["reponse"])

    # ===================================================================== Etape 2 : Définir action ==================================================================

    format_reponse_action = {}

    if reponse_fonction["fonction"] == "none":
        retour["action"] = "none"
        return retour

    elif reponse_fonction["fonction"] == "alarms":
        format_reponse_action = {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Le nom de la fonction à exécuter",
                    "enum": ["create"]
                }
            },
            "required": ["action"]
        }

    reponse_action = ollama.chat(
        model = "qwen2.5:3b",
        messages = [
            {
                "role": "system",
                "content": "Tu es un assistant domestique. Tu ne contrôles pas directement les appareils. Ton rôle est de convertir les demandes de l'utilisateur en commandes structurées."
            },
            {
                "role": "user",
                "content": texte
            }
        ],
        format = format_reponse_action,
    )

    reponse_action = json.loads(
        reponse_action["message"]["content"]
    )

    retour["action"] = reponse_action["action"]

    # ===================================================================== Etape 3 : Définir donnees ==================================================================

    format_reponse_donnees = {}

    if reponse_fonction["fonction"] == "alarms":

        if reponse_action["action"] == "create":
            format_reponse_donnees = {
                "type": "object",
                "properties": {
                    "nom": {
                        "type": "string",
                        "description": "Le nom de l'alarme"
                    },
                    "heure": {
                        "type": "string",
                        "pattern": "^([01][0-9]|2[0-3]):[0-5][0-9]$",
                        "description": "L'heure de l'alarme au format HH:MM"
                    },
                    "jours": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                            "enum": [0, 1, 2, 3, 4, 5, 6]
                        },
                        "description": "Les jours de la semaine pour l'alarme (0-6, où 0 = lundi et 6 = dimanche)"
                    },
                    "intervalle": {
                        "type": "string",
                        "description": "Durée de répétition demandée par l'utilisateur. Extraire la durée exprimée, sans la convertir. Exemples : '5min' si l'utilisateur dit '5min', '10 minutes' s'il dit '10 minutes', '1h' s'il dit '1 heure'. Ne jamais renvoyer 'sync'. Si aucune durée n'est précisée, renvoyer une chaîne vide."
                    },
                    "actions": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["sonner"],
                        },
                        "uniqueItems": True,
                        "description": "Les actions à effectuer lorsque l'alarme se déclenche. ['sonner'] doit toujours être activé par défaut."
                    },
                    "jetable": {
                        "type": "boolean",
                        "description": "Indique si l'alarme est à usage unique ou non. true = à usage unique, false = répétée. Si l'utilisateur ne fournit pas cette information, utiliser true par défaut."
                    }
                },
                "required": ["nom", "heure", "jours", "intervalle", "actions", "jetable"]
            }

    # -------------------------------------------

    reponse_donnees = ollama.chat(
            model = "qwen2.5:3b",
            messages = [
                {
                    "role": "system",
                    "content": "Tu es un assistant domestique. Tu ne contrôles pas directement les appareils. Ton rôle est de convertir les demandes de l'utilisateur en commandes structurées."
                },
                {
                    "role": "user",
                    "content": texte
                }
            ],
            format = format_reponse_donnees,
        )

    reponse_donnees = json.loads(
            reponse_donnees["message"]["content"]
        )

    if "intervalle" not in texte and "répétition" not in texte and "rappel" not in texte:
        reponse_donnees["intervalle"] = "10 minutes"

    print("intervalle brute : ", reponse_donnees["intervalle"])

    retour["data"] = reponse_donnees

    return retour