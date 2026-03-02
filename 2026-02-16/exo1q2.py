# Écrire un programme qui ne fait rien (exécute une boucle vide) mais qui reçoit un
# signal signal.SIGALRM toutes les secondes, et aﬃche alors un message «bip». À la
# réception du sixième signal, le programme aﬃche « bye » et se termine.
import signal, time, sys, random
compteur = 0
def alarm_reaction(signum, frame):
    global compteur # le nombre de fois où alarm_reaction a été appelée
    compteur += 1
    if compteur <= 6:
        print("BIP")
        signal.alarm(1)
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, alarm_reaction)

signal.alarm(1) # programme un minuteur, SIGALRM arrivera dans 1 sec
while True:
    n = random.randint(2 ** 48, 2 ** 49)
    m = random.randint(2 ** 48, 2 ** 49)
    p = n * m 
    print(n,m, p)
    time.sleep(0.1)