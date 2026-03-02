import os, sys, signal, time

n = int(sys.argv[1])

def handler_pere(signum, frame):
    global fork_result
    print("signal reçu et renvoyé")
    os.kill(fork_result, signal.SIGUSR1)

def handler_fils(signum, frame):
    print("signal reçu")

signal.signal(signal.SIGUSR1, handler_pere)

fork_result = os.fork()
if fork_result == 0:
    # fils
    signal.signal(signal.SIGUSR1, handler_fils)
    for _ in range(n):
        os.kill(os.getppid(), signal.SIGUSR1)
        signal.pause() # attend l'arrivée du signal du père
    print("bye")
    sys.exit(0)

# père
os.wait()