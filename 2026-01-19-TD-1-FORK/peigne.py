# fait un peigne de n processus
import os, sys

n = int(sys.argv[1])


print(f"{os.getpid()=}, {os.getppid()=}")

for i in range(n):
    fork_result = os.fork()
    if fork_result == 0:
        print(f"{os.getpid()=}, {os.getppid()=}")
        sys.exit(0)