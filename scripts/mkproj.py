import os

def execute(command : str) -> None:
    args = command.split()

    try:
        project_name = args[1]
    except IndexError:
        print("ArgsError: Des arguments attendus n'ont pas été spécifiés. ErrorCode(2)")
        return

    try:
        os.mkdir(project_name)
    except FileExistsError:
        print(f"FolderExistsError: Le dossier '{project_name}' existe déjà. ErrorCode(3)")
        return

    print(f"Projet '{project_name}' créé.")
    open = input("Voulez-vous vous positionner dedans ? (y, n) > ")

    while True:
        if open == 'y' or 'n':
            if open == 'y':
                os.chdir(project_name)
                print(f"Projet '{project_name}' ouvert.")
            break