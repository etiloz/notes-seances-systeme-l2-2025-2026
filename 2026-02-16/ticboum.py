# affiche TIC toutes les secondes
# affiche BOUM si on fait Ctrl+C (mais n'interrompt pas le programme)

import signal, sys, os, time
def handler(sig, ignore):
    print("BOUM")

print(f"{os.getpid()=}")
signal.signal(signal.SIGINT, handler) # Met en place le nouveau traitant
# signal.signal(signal.SIGKILL, handler) # <- INTERDIT!

while True:
    print("TIC")
    time.sleep(1)
