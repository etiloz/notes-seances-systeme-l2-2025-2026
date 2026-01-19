# fait un escalier de n processus
import os, sys

n = int(sys.argv[1])

for i in range(n):
    print(f"{os.getpid()=}, {os.getppid()=}")
    fork_result = os.fork()
    if fork_result != 0:
        sys.exit(0)