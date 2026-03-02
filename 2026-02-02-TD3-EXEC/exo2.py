# Écrire un programme verifier.py dont l’usage sera
# ./verifier.py cmd arg1 .. argn
# et qui lance la commande cmd arg1 .. argn, signale une éventuelle erreur lors du 
# lancement, attend la fin de l’exécution et précise par un message le résultat (succès ou échec).

# sys.argv = ["verifier.py", "cmd", "arg1", ... , "argn"]

import os, sys
cmd = sys.argv[1]  # "cmd"
args = sys.argv[1:] # ["cmd", "arg1", ... , "argn"]

if os.fork() == 0:
    # le fils exécute la commande
    os.execvp(cmd, args)

# le père attend la fin de l’exécution de la commande et vérifie le résultat
pid, status = os.wait()
if not os.WIFEXITED(status):
    print("La commande s'est terminée avant de pouvoir rendre un code de sortie, ou ne s'est pas vraiment terminée")
exit_code = os.WEXITSTATUS(status)
if exit_code == 0:
    print("La commande s'est terminée avec succès")
else:
    print(f"La commande s'est terminée avec un échec (code {exit_code})")