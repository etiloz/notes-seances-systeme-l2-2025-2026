# Écrivez un programme Python qui, par le biais de créations de processus et de 
# recouvrements, exécute la suite de commandes who ; pwd ; ls -l (rappel : le point-virgule
# signifie qu’une commande est exécutée lorsque la commande précédente est terminée).

import os, sys
cmd1 = "who"
args1 = ["who"]
cmd2 = "pwd"
args2 = ["pwd"]
cmd3 = "ls"
args3 = ["ls", "-l"]

if os.fork() == 0:
    # le premier fils exécute la commande who
    os.execvp(cmd1, args1)
os.wait()  # le père attend la fin du premier fils
if os.fork() == 0:
    # le deuxième fils exécute la commande pwd
    os.execvp(cmd2, args2)
os.wait()  # le père attend la fin du deuxième fils
if os.fork() == 0:
    # le troisième fils exécute la commande ls -l
    os.execvp(cmd3, args3)
os.wait()  # le père attend la fin du troisième fils