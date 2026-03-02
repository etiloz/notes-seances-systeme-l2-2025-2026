# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils.
#    Le fils envoie le signal SIGUSR1 au père puis se termine.
# 2. Modifier le père pour qu'il affiche un message lorsque le 
#    signal SIGUSR1 est capté.
# 3. Modifier le programme pour qu'il reçoive un entier n sur la ligne 
# de commande, et modifier le fils de telle sorte qu'il envoie à la 
# suite n signaux SIGUSR1 au père avant de se terminer.
# 4. Modier le père pour qu'il compte le nombre de signaux SIGUSR1 reçus ; 
# supprimer tout affichage dans le handler de signal du père, et afficher
#  le nombre final de signaux reçus après la fin du fils.

import os, signal, sys, time
try:
    n = int(sys.argv[1])
except:
    print(f"Usage: {sys.argv[0]} n", file=sys.stderr)
    sys.exit(1)

compteur = 0
def f(signum, frame):
    global compteur
    compteur += 1
#    print("signal SIGUSR1 reçu")


signal.signal(signal.SIGUSR1, f) # on installe f pour réagir à l'arrivée de SIGUSR1

# possible aussi: pid_du_pere = os.getpid()
if os.fork() == 0:
    # fils
    pid_du_pere = os.getppid()
    for _ in range(n):
        os.kill(pid_du_pere, signal.SIGUSR1)
#        time.sleep(0.01)
    sys.exit(0)
# père
os.wait()
print("nombre de signaux reçus", compteur)




