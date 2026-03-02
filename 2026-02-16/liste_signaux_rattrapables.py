# liste les signaux rattrapables
import signal
def foo(signum, frame):
    return None

for signum in range(1,32):
    try:
        signal.signal(signum, foo)
        print(signum)
    except:
        continue