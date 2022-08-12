import os

def execute(command : str):
    args = command.split()

    try:
        project_name = args[1]
        print(f"Projet '{project_name}' selectionné.")
        continue_number = 0
    except IndexError:
        continue_number = 1

    if continue_number == 0:
        os.chdir(project_name)
        try:
            html = open('index.html', 'x')
            html.close()

            css = open('styles.css', 'x')
            css.close()

            print("Initialisation terminée.")
        except FileExistsError:
            print("FileExistsError: Les fichier existent déjà dans la destination. ErrorCode(4)")
            return
        
        print(f"/!\\ Vous êtes maintenant positionné(e) dans le dossier '{project_name}'. /!\\")

    elif continue_number == 1:
        try:
            html = open('index.html', 'x')
            html.close()

            css = open('styles.css', 'x')
            css.close()

            print("Initialisation terminée.")
        except FileExistsError:
            print("FileExistsError: Les fichier existent déjà. ErrorCode(4)")
            return