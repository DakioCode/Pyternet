def execute() -> None:
    commands_list = """====================
LISTE DES COMMANDES
====================

                    --- Informations ---
 - help : Obtenir la liste des commandes.
 - instru : Obtenir les instructions pour créer un projet.

                    --- Création de projet ---
 - mkproj <project_name> : Créer un projet.
 - open <project_name> : Ouvrir un projet existant.
 - init [project_name] : Initialiser un projet.

                    --- Autres ---
 - user : Entrer dans les paramètres utilisateur.
 - quit : Arrêter la création.
 
                    --- Légende ---
<...> => Arguments obligatoires.
[...] => Arguments facultatifs."""

    print(commands_list)