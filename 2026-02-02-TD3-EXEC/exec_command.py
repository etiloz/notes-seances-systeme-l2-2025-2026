#!/usr/bin/env python3
# SHEBANG sur la ligne au-dessus (première ligne du script)

# Écrire un programme exec_command.py qui exécute une commande Unix qu’on lui passe en
# paramètre (en ligne de commande, cf sys.argv). Exemple d’exécution :
# ./exec_command.py /bin/ls -Ft /

import os, sys

filename = sys.argv[1]  # "/bin/ls"
args = sys.argv[1:]     # ["/bin/ls", "-Ft", "/"]
os.execvp(filename, args)  # <- sans retour!
print("bye") # ne s'affiche pas