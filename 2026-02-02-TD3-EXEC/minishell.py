# on répète les étapes suivantes indéfiniment :
# 1. afficher le prompt "minishell> "
# 2. lire une ligne de commande tapée par l'utilisateur
# 3. créer un processus fils qui exécute la commande tapée
# 4. le processus père attend la fin du fils avant de recommencer au point


import os, sys

while True:
    # 1. afficher le prompt
    print("minishell> ", end="")

    # 2. lire une ligne de commande
    ligne = input()
    ligne = ligne.strip()
    args = ligne.split()
    if len(args) == 0:
        continue  # si l'utilisateur n'a rien tapé, on recommence au point 1
    cmd = args[0]

    # 3. créer un processus fils qui exécute la commande tapée
    fork_result = os.fork()
    if fork_result == 0:
        # processus fils
        try:
            os.execvp(cmd, args)
        except FileNotFoundError:
            print(f"{cmd}: command not found", file=sys.stderr)
            sys.exit(1)  # quitter le fils avec un code d'erreur
        except PermissionError:
            print(f"{cmd}: permission denied", file=sys.stderr)
            sys.exit(1)  # quitter le fils avec un code d'erreur
    else:
        # processus père
        os.wait()  # 4. attendre la fin du fils
