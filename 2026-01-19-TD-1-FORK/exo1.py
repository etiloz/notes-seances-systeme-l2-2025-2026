import os, sys
x = 1
fork_result = os.fork()

if fork_result == 0: # child
    x = x + 1
    print("child: x =", x)
    sys.exit(0)

# parent
x = x - 1
print("parent: x =", x)
sys.exit(0)