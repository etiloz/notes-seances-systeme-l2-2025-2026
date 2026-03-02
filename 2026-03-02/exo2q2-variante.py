# Modifier le programme pour qu'il reçoive un entier n sur la ligne de commande, et
# modifier le fils et le père pour que l'échange de signaux se passe successivement n
# fois (le fils envoie n signaux)
# variante: on utilise signal.pause et une boucle for
import os, sys, signal

n = int(sys.argv[1])

def print_and_kill(signum, frame): # handler du père
    global pid_du_fils
    print("signal reçu et va être renvoyé")
    os.kill(pid_du_fils, signal.SIGUSR1)

signal.signal(signal.SIGUSR1, print_and_kill)

pid_du_fils = os.fork()

if pid_du_fils == 0:
    # fils
    def handler(signum, frame):
        print("signal reçu")
    signal.signal(signal.SIGUSR1, handler)
    for i in range(n):
        os.kill(os.getppid(), signal.SIGUSR1)
        print("signal envoyé")
        signal.pause() # attente d'un signal
    sys.exit(0)
#père
os.wait()