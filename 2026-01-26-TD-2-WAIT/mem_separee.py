# pourquoi le fils ne peut pas donner son pid au père?
import os, sys

pids = []  # liste des PIDs des enfants
for i in range(3):
    pid = os.fork()
    if pid == 0:  # code du fils
        pids.append(os.getpid())
        print(f"[fils] {pids}")
        sys.exit(0)

print(pids)