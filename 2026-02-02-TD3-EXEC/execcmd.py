#!/usr/bin/env python3
# ligne de dessus = SHEBANG
# Écrire un programme execcmd.py qui exécute une commande Unix qu’on lui passe en
# paramètre. Exemple d’exécution :
# ./execcmd.py /bin/ls -Ft /


import sys, os
try:
    filename = sys.argv[1] # le nom du programme à exécuter se trouve à l'indice 1
    argv = sys.argv[1:] # la liste des arguments à passer au programme commence à l'indice 1
    os.execv(filename, argv)
except IndexError:
    # Pas assez d'arguments, on affiche un message d'erreur et on quitte
    print("Usage: {} <command> [args...]".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)
except FileNotFoundError:
    print("Error: Command '{}' not found.".format(filename), file=sys.stderr)
    sys.exit(1)
except PermissionError:
    print("Error: Permission denied for command '{}'.".format(filename), file=sys.stderr)
    sys.exit(1)
