import os, time, sys
from scripts import cd, help, init, instru, mkproj, open, path

print("Bienvenue sur Pyternet ! \n\nTapez 'help' pour obtenir la liste des commandes.")
time.sleep(1)

while True:
    time.sleep(1)
    cmd = input("[Pyternet] > ")

    # --------------------- Informations Commands ---------------------

    if cmd == "help":
        help.execute()

    elif cmd == "instru":
        instru.execute()

    # --------------------- Project creation Commands ---------------------

    elif cmd.startswith("mkproj"):
        mkproj.execute(cmd)

    elif cmd.startswith("open"):
        open.execute(cmd)

    elif cmd.startswith("init"):
        init.execute(cmd)

    # --------------------- Another Commands ---------------------

    elif cmd.startswith("cd"):
        cd.execute(cmd)

    elif cmd == "path":
        path.execute()

    elif cmd == "quit":
        break

    else: print(f"CommandError: Commande '{cmd}' introuvable. ErrorCode(1)")