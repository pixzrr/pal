# PAL

------------------------------------------------------------------------

## Présentation

PAL est un projet d'assistant
domestique phyisique dont l'objectif est de proposer une interface unique
pour différentes fonctions.

L'utilisateur formule une demande en langage naturel. PAL l'analyse,
identifie l'action correspondante, extrait les paramètres nécessaires et
l'exécute.

L'objectif n'est pas simplement de créer un chatbot, mais de développer
un système entier capable de faire le lien entre intelligence
artificielle, logiciel et composants physiques

## Aperçu

<img width="660" height="364" alt="image" src="https://github.com/user-attachments/assets/8a8286e3-c71a-4a7f-8f53-bdd9c2f5ecd9" />

*Interface graphique de PAL --- prototype en cours de développement.*

## Technologies

Voici les technologies utilisées (pour l'instant):

  - Python
    
  - FastAPI
    
  - Ollama
    
  - Ministral 3 (8B)
    
  - Qwen 2.5 (3B)
    
  - HTML / CSS
    
  - JavaScript
    
  - MQTT
  -----------------------------------------------------------------------

## Rôle des principaux modules

-   `main.py` : point d'entrée du backend, configuration de FastAPI et
    réception des requêtes.
-   `functions/text_to_data.py` : interprétation des demandes et
    extraction des paramètres grâce aux modèles de langage.
-   `functions/` : regroupe les fonctionnalités proposées par PAL, comme
    les alarmes et les rappels.
-   `devices/` : regroupe les interfaces logicielles associées aux
    équipements physiques.
-   `communication/` : regroupe les modules de communication, notamment
    MQTT.
-   `voice/` : modules dédiés à la reconnaissance et à la synthèse
    vocale.
-   `interface/` : interface utilisateur accessible depuis un
    navigateur.

## Installation

### Prérequis

-   Python 3.10 ou supérieur
-   [Ollama](https://ollama.com/)
-   Git (facultatif, pour cloner le dépôt)

### 1. Récupérer le projet

``` bash
git clone https://github.com/pixzrr/pal/
cd PAL
```

### 2. Installer les dépendances

``` bash
pip install fastapi uvicorn ollama
```

### 4. Télécharger les modèles

Les modèles utilisés actuellement par le projet sont :

``` bash
ollama pull ministral-3:8b
ollama pull qwen2.5:3b
```

Ollama doit être démarré et accessible localement.

### 5. Lancer PAL

Depuis le dossier contenant `main.py` :

``` bash
python<version> -m uvicorn main:ihm --reload
```

L'interface est accessible depuis un navigateur à l'adresse :

<http://127.0.0.1:8000/pal/>

## État du développement

  Fonctionnalité                      État
  ----------------------------------- --------------------------------------------
  Interface web                       Prototype fonctionnel
  Communication HTTP avec FastAPI     Fonctionnelle
  Analyse des demandes avec Ollama    En cours de développement
  Extraction de données structurées   En cours de développement
  Dispatch des commandes              Partiellement implémenté
  Création d'alarmes                  Logique d'extraction et traitement amorcés
  Gestion des rappels                 À développer
  Détection de présence               À développer
  Communication MQTT                  À développer
  Intégration ESP32                   À développer
  Reconnaissance vocale               À développer
  Synthèse vocale                     À développer

## Orientations futures

-   **Gestion du temps** : développer un système complet d'alarmes et de
    rappels.
-   **Communication avec les équipements** : intégrer MQTT et les
    microcontrôleurs ESP32.
-   **Reconnaissance vocale** : permettre à l'utilisateur de communiquer
    avec PAL sans interface clavier.
-   **Synthèse vocale** : rendre les réponses accessibles à l'oral.
-   **Détection de présence** : exploiter des capteurs et des systèmes
    de vision pour adapter le comportement de l'assistant.
-   **Déploiement distant** : permettre un accès sécurisé à l'interface
    depuis différents appareils.

------------------------------------------------------------------------

*PAL*
