import os

def execute(command : str):
    args = command.split()

    try:
        path = args[1]
    except IndexError:
        print("ArgsError: Des arguments attendus n'ont pas été spécifiés. ErrorCode(2)")
        return

    try:
        os.chdir(path)
        print(f"Votre position a changé : {os.getcwd()}.")
    except FileNotFoundError:
        print(f"PathNotFoundError: Chemin '{path}' introuvable. ErrorCode(7)")
        return