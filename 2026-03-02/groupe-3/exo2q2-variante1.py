import os, sys, signal, time

n = int(sys.argv[1])

def handler_pere(signum, frame):
    global fork_result
    print("signal reçu et renvoyé")
    os.kill(fork_result, signal.SIGUSR1)

compteur = 0
def handler_fils(signum, frame):
    global compteur
    print("signal reçu")
    compteur += 1
    if compteur < n :
        os.kill(os.getppid(), signal.SIGUSR1)
    else:
        print("bye")
        sys.exit(0)



signal.signal(signal.SIGUSR1, handler_pere)

fork_result = os.fork()
if fork_result == 0:
    # fils
    signal.signal(signal.SIGUSR1, handler_fils)
    os.kill(os.getppid(), signal.SIGUSR1)
#    time.sleep(2) # attend le signal retour
    while True:
        pass

# père
os.wait()