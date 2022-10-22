from PySimpleGUI import *

theme("PythonPlus")

commands = [
    "help"
]

layout = [
    [Text("Bienvenue sur Pyternet !", font=("Verdana", 13), justification="center", text_color="yellow")],
    [Text("Pour voir la liste des commandes, tapez 'help'.", font=("Verdana", 13), text_color="yellow")],
    [Text("Commande :", text_color="Green", font=("Verdana", 12)), Input(size=(50, 10), key="-INPUT-COMMAND-", text_color="white")],
    [Text()],
    [Button("Envoyer", key="-BUTTON-SUBMIT-", size=(15, 1), font=("Verdana", 13))],
    [Text(key="OutputMessage", font=("Verdana", 13))]
]

window = Window("Pyternet", layout=layout)

while True:
    event, values = window.read()
    
    if event == WINDOW_CLOSED:
        break
    
    if event == "-BUTTON-SUBMIT-":
        if (values["-INPUT-COMMAND-"]) == "help":
            window["OutputMessage"].update("Commande 'help' exécutée !", text_color="green")
        else:
            window["OutputMessage"].update("La commande saisie n'existe pas / Syntaxe invalide.", text_color="red")
    
window.close()