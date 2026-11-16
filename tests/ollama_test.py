import ollama
import random
import json

format_reponse = {
    "type": "object", #objet json => dico avec clés + valeurs
    "properties": {
        "reponse": {
            "type": "string", 
            "description": "La réponse à fournir"
        },
        "fonction": {
            "type": "string",
            "description": "Le nom de la fonction à exécuter",
            "enum": ["", "alarms"]
        },
        "action": {
            "type": "string",
            "description": "L'action à effectuer par la fonction",
            "enum": ["", "create"]
        },
        "donnee": {
            "type": "object",
            "description": "Les données nécessaires pour exécuter l'action",
            "properties": {
                "nom": {
                    "type": "string",
                    "description": "Le nom de l'alarme. Si aucun nom n'est fourni, utiliser 'Alarme' par défaut. Si l'utilisateur fournit un contexte dans sa demande, utiliser ce contexte pour générer un nom d'alarme approprié, en français, avec des espaces si nécessaire."
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
                    "type": "integer",
                    "description": "Valeur en secondes."
                },
                "actions": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": ["sonner"],
                    },
                    "uniqueItems": True,
                    "description": "Les actions à effectuer lorsque l'alarme se déclenche"
                },
                "jetable": {
                    "type": "boolean",
                    "description": "Indique si l'alarme est à usage unique ou non. true = à usage unique, false = répétée. Si l'utilisateur ne fournit pas cette information, utiliser true par défaut."
                }
            }
        }
    },
    "required": ["reponse", "fonction", "action", "donnee"]
}

models_messages = {
    1: "Que voulez-vous faire ?",
    2: "Salut",
    3: "Comme ça va ?"
}

choix_message = random.randint(1, 3)

user_input = input(models_messages[choix_message])

reponse = ollama.chat(
    model = "qwen2.5:3b",
    messages = [
        {
            "role": "system",
            "content": "Tu es le module de compréhension d'un assistant domestique. Tu ne contrôles pas directement les appareils. Ton rôle est de convertir les demandes de l'utilisateur en commandes structurées. Si l'utilisateur demande une fonction non disponible ou s'il pose une autre question, laisse les propriétés requises 'fonction, 'action' et 'donnee' vides. La propriété reponse doit contenir la réponse à fournir à l'utilisateur."
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
    format = format_reponse,
)

print(reponse["message"]["content"])