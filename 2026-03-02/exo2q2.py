# Modifier le programme pour qu'il reçoive un entier n sur la ligne de commande, et
# modifier le fils et le père pour que l'échange de signaux se passe successivement n
# fois (le fils envoie n signaux)
import os, sys, signal

n = int(sys.argv[1])

def print_and_kill(signum, frame): # handler du père
    global pid_du_fils
    print("signal reçu et renvoyé")
    os.kill(pid_du_fils, signal.SIGUSR1)
signal.signal(signal.SIGUSR1, print_and_kill)

pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    compteur = 0
    def print_and_exit(signum, frame): # handler du fils
        global compteur
        compteur += 1
        print("signal reçu, et ... ")
        if compteur == n:
            print("... bye!")
            sys.exit(0)
        else:
            print("... renvoyé!")
            os.kill(os.getppid(), signal.SIGUSR1) 
    signal.signal(signal.SIGUSR1, print_and_exit)
    os.kill(os.getppid(), signal.SIGUSR1)
    while True: # attente (boucle infinie)
        pass
#père
os.wait()