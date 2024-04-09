# Tracker de Commande pour Confirmed

![Python Version](https://img.shields.io/badge/python-%3E%3D3.6-blue.svg)

Ce projet est un Tracker de Commande pour vos commandes Confirmed. Il vous permet de suivre l'état de votre commande en enregistrant votre adresse e-mail et votre numéro de commande en écrivant une commande à travers le bot discord, tout est expliquer en dessous. (Non maintenu , ne dois surement plus fonctionner)

## Features

- [x] Bot Discord
- [x] Affichage du status
- [x] Lien pour suivre le colis si celui çi est disponible
- [x] Affichage des SKU en fonction des commandes (pour mieux vous y retrouver)
- [x] Récupere les factures (si disponibles)
- [x] Très simple d'utilisation (juste mettre le token du bot !)
- [x] Répond en privé (evite de leak vos infos si le tool est utilisé sur un grand serveur)
- [x] Requetes asynchrones avec aiohttp au lieu de requests (permet a plusieurs utilisateurs de faire la commande en meme temps) 

## Configuration du Bot Discord

Avant de lancer le Tracker de Commande, assurez-vous d'avoir créé votre propre bot Discord sur le [site développeur de Discord](https://discord.com/developers/applications). Une fois que vous avez créé le bot, veuillez récupérer le token d'accès.

Ensuite, notez le token quelque part vous en aurez besoin pour la suite.

## Installation

Veuillez vous assurer d'avoir installé les dépendances requises en exécutant dans le cmd :

```bash
pip install -r requirements.txt
```

Puis effectuez :

```bash
DiscordBot.py
```
![image](https://github.com/julesgtz/confirmed-tracker-discord-bot/assets/113105305/80c3f543-740f-45a2-a45d-3e2830df9d95)

Entrez le token du bot récupéré préalablement.

## Utilisation

Vous pouvez maintenant DM le bot, la commande est de la forme suivante :

![image](https://github.com/julesgtz/confirmed-tracker-discord-bot/assets/113105305/68d68467-82d2-4eb6-9ac9-bd8737193dba)

Dans infos, veuillez mettre votre mail:numérocommande.

Exemple :

![image](https://github.com/julesgtz/confirmed-tracker-discord-bot/assets/113105305/16280051-6add-47a6-9bb2-d9ee8b79d880)

Vous pouvez aussi tracker plusieurs commandes a la fois, Exemple:

![image](https://github.com/julesgtz/confirmed-tracker-discord-bot/assets/113105305/41715302-d6da-4b2e-a488-a2d229c8d3a5)

## Résultats

Voici ce à quoi ressemble le tracker une fois la commande faite:

![image](https://github.com/julesgtz/confirmed-tracker-discord-bot/assets/113105305/e3e9e279-d791-4fd8-b3f2-437b7eb099db)

On peut voir ici tous les cas différents :

1. Si le ``statut est souligné en bleu``, vous pouvez cliquer dessus pour accéder à ``votre lien de suivi``.
2. Si le ``numéro de commande est souligné en bleu``, vous pouvez cliquer dessus pour accéder à la ``facture`` correspondante.
3. Si rien n'est cliquable, c'est que rien n'est disponible !

