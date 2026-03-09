# exercice supplementaire: ecrire un programme `timeout.py cmd delay`
# qui lance la commande dans un fils et tue le fils au bout de delay 
# s'il n'a pas encore terminé

# indices: voir photo
# utiliser signal.alarm pour programmer un minuteur dans le père
# installer un handler dans le père pour réagir à sigalarm
# envoyer sigkill au fils depuis le handler

import os, sys, signal

try:
    cmd = sys.argv[1]
    delay = int(sys.argv[2])
except:
    print("USAGE: timeout.py <cmd> <delay>", file=sys.stderr)
    sys.exit(1)


def handler(signum, frame):
    global pid_fils
    print("timeout: delai atteint")
    os.kill(pid_fils, signal.SIGKILL)

signal.signal(signal.SIGALRM, handler)

pid_fils = os.fork()
if  pid_fils == 0:
    os.execvp(cmd, [cmd])

signal.alarm(delay)
os.wait()