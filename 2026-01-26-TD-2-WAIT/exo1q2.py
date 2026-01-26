import os, sys
print("Hello")
pid = os.fork()
print("ici : {}".format(pid))
if pid != 0:
    pid_wait, status = os.wait()
    if os.WIFEXITED(status):
        print("là : {}".format(os.WEXITSTATUS(status)))
    print("Bye")
    sys.exit(2)
sys.exit(0)