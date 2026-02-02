#!/usr/bin/env python3
import os, sys
args = sys.argv[1:]
cmd = args[0]  # = sys.argv[1]= sys.argv[1:][0]

if os.fork() == 0:
    # processus fils, exécute la commande
    try:
        os.execvp(cmd, args)
    except FileNotFoundError:
        print(f"fichier {cmd} introuvable", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"fichier {cmd} non exécutable", file=sys.stderr)
        sys.exit(1)

# processus père, récupère la terminaison et affiche succès ou échec
_pid, status = os.wait()

if os.WIFEXITED(status):
    print("le programme a eu le temps de faire exit")
    if os.WEXITSTATUS(status) == 0:
        print("succès: il a terminé avec un code de sortie = 0")
    else:
        print("échec: il a terminé avec un code de sortie != 0")
else:
    print("le programme a terminé sans avoir fait exit ou n'a pas terminé...")