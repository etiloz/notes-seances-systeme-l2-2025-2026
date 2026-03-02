# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. Le fils envoie
# le signal SIGUSR1 au père. À la réception du signal, le père affiche un message puis
# envoie le signal SIGUSR1 au fils. À la réception du signal, le fils affiche un message
# puis se termine. Le père attend la fin du fils, affiche un message puis se termine.

import os, sys, signal

def print_and_kill(signum, frame): # handler du père
    global pid_du_fils
    print("signal reçu et renvoyé")
    os.kill(pid_du_fils, signal.SIGUSR1)
signal.signal(signal.SIGUSR1, print_and_kill)

pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    def print_and_exit(signum, frame): # handler du fils
        print("signal reçu, bye.")
        sys.exit(0)
    signal.signal(signal.SIGUSR1, print_and_exit)
    os.kill(os.getppid(), signal.SIGUSR1)
    while True: # attente (boucle infinie)
        signal.pause()  # possible aussi: `pass` (dans ce cas, attente "active")
#père
os.wait()