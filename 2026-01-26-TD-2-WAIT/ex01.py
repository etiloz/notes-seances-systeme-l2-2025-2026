import errno, os, sys
nbChildren = 20
pids = [] # list of child PIDs
for i in range(nbChildren):
    fork_result = os.fork()
    if fork_result == 0: # child
        sys.exit(100 + i)
    else: # parent
        pids.append(fork_result)
        print(f"{pids=}")

for pid in pids:
        pid, status = os.waitpid(pid, 0)
        if os.WIFEXITED(status):
            print(f"child {pid} terminated normally with exit status={os.WEXITSTATUS(status)}")
        else:
            print(f"child {pid} terminated abnormally")

sys.exit(0)
