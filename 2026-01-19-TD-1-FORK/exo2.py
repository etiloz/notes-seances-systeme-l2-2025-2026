import os, sys
# 1 seul processus
fork_result = os.fork()
if fork_result == 0:
    os.fork()
# 3 processus
print("hello!")
sys.exit(0)
print("salut")