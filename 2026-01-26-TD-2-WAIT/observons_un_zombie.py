# 1. lancer ce programme en tâche de fond : python3 exo1q2.py &
# 2. observer le comportement avec la commande 'ps'

import os, sys, time
if os.fork() == 0:
    print(f"[fils] {os.getpid()=}, going zombie...")
    sys.exit(0)

while True:
    time.sleep(1)