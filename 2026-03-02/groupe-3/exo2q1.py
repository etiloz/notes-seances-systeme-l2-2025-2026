# Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. Le fils envoie
# le signal SIGUSR1 au père. À la réception du signal, le père affiche un message puis
# envoie le signal SIGUSR1 au fils. À la réception du signal, le fils affiche un message
# puis se termine. Le père attend la fin du fils, affiche un message puis se termine.

import os, sys, signal, time

def handler_pere(signum, frame):
    global fork_result
    print("signal reçu et renvoyé")
    os.kill(fork_result, signal.SIGUSR1)

def handler_fils(signum, frame):
    global fork_result
    print("signal reçu")


signal.signal(signal.SIGUSR1, handler_pere)

fork_result = os.fork()
if fork_result == 0:
    # fils
    signal.signal(signal.SIGUSR1, handler_fils)
    os.kill(os.getppid(), signal.SIGUSR1)
    time.sleep(2) # attend le signal retour
    print("bye")
    sys.exit(0)

# père
os.wait()