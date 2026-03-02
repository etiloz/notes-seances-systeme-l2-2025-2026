import signal, sys, os, time
def my_handler(sig, ignore):
    print("Caught SIGINT")
    sys.exit(0)

print(f"{os.getpid()=}")
signal.signal(signal.SIGINT, my_handler) # Met en place le nouveau traitant
# signal.signal(signal.SIGKILL, my_handler) # <- INTERDIT! SIGKILL N'EST PAS UN SIGNAL DONT ON PEUT REDEFINIR LE HANDLER

# à partir d'ici, SIGINT déclence my_handler

signal.pause() # attend la reception d'un signal
print("signal reçu")
sys.exit(0)