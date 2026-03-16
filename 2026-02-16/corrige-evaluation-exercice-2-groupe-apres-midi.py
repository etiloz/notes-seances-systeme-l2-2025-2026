import os, sys

try:
    cmd = sys.argv[1]
    A = int(sys.argv[2])
    B = int(sys.argv[3])
except:
    print("Usage: script.py cmd A B", file=sys.stderr)
    sys.exit(1)

D = {}  # L = []
for i in range(A,B):
    fork_result = os.fork()
    if fork_result == 0:
        try: 
            os.execvp(cmd, [cmd, str(i)])
        except:
            print("erreur commande")
            sys.exit(1)
    D[fork_result] = i   # L.append(fork_result)
for _ in range(A,B):
    pid,status = os.wait()
    if os.WIFEXITED(status) and os.EXITSTATUS(status) == 0 :
        print("i = ", D[pid])     # L.index(pid) + A
        break
else: 
    print("Not found")