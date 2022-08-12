import os

def execute(command : str) -> None:
    args = command.split()

    try:
        project_name = args[1]
    except IndexError:
        print("ArgsError: Des arguments attendus n'ont pas été spécifiés. ErrorCode(2)")
        return

    try:
        os.chdir(project_name)
        print(f"Projet '{project_name}' ouvert.")
    except FileNotFoundError:
        print(f"FolderNotFoundError: Projet '{project_name}' introuvable. ErrorCode(4)")
        return