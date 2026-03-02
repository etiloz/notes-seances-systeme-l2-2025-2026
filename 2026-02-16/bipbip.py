# affiche BIP toutes les secondes
# contrainte: utiliser signal.alarm (pas time.sleep)
import signal, sys

compteur = 0
def react_on_alarm(signum, frame):    
    global compteur
    compteur += 1
    print("BIP")
    if compteur == 5:
        sys.exit(0)
    else:
        signal.alarm(1)  # sorte d'appel récursif avec temporisation d'une seconde


# avec une cloture, sans variable globale (cf programmation fonctionnelle)
# def create_closure():
#     compteur = 0
#     def closure(signum, frame):    
#         nonlocal compteur
#         compteur += 1
#         print("BIP")
#         if compteur == 5:
#             sys.exit(0)
#         else:
#             signal.alarm(1)  # sorte d'appel récursif avec temporisation d'une seconde
#     return closure

# react_on_alarm = create_closure()

signal.signal(signal.SIGALRM, react_on_alarm)
print("BIP")
signal.alarm(1)
while True:  # boucle d'attente active
    pass