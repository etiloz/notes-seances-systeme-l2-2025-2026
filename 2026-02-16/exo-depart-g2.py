# affiche BIP toutes les secondes
# affiche BOUM si Ctrl+C (mais ne termine pas)
import signal, time

def my_handler():
    print("BOUM")

signal.signal(signal.SIGINT, my_handler)

while True:
    print("BIP")
    time.sleep(1)