# le père crée deux fils
# chaque fils envoie un signal au père qui le fait suivre à l'autre fils
# chaque fils affiche "je suis mort quand il reçoit le signal"

# EXERCICE: écrire les handlers!

import os, sys, signal


pid_fils1 = os.fork()
if pid_fils1 != 0:
    pid_fils2 = os.fork()

if pid_fils1 != 0 and pid_fils2 != 0:
    signal.signal(signal.SIGUSR1, handler_du_pere)
    signal.signal(signal.SIGUSR2, handler_du_pere)
    os.wait()
    os.wait()
    print("bye")
else:
    signal.signal(signal.SIGINT, handler_des_fils)
    if pid_fils1 == 0:
        # fils 1
        os.kill(os.getppid(), signal.SIGUSR1)
    else:
        # fils 2
        os.kill(os.getppid(), signal.SIGUSR2)
