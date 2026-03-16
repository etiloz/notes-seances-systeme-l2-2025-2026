import os, sys

try:
    file0 = sys.argv[1]
    file1 = sys.argv[2]
    file2 = sys.argv[3]
    cmd = sys.argv[4]
    args = sys.argv[4:]
except:
    print("Usage: exo-redirection.py <file0> <file1> <file2> <cmd> [args...]")
    sys.exit(1)

fd0 = os.open(file0, os.O_RDONLY)
fd1 = os.open(file1, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
fd2 = os.open(file2, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
os.dup2(fd0, 0)
os.dup2(fd1, 1)
os.dup2(fd2, 2)
os.close(fd0)  # <- bonne pratique de fermer les descripteurs de fichiers après les avoir dupliqués
os.close(fd1)
os.close(fd2)
os.execvp(cmd, args)
