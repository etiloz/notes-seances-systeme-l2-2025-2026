import os, sys


def capture_stdout(cmd, args):
    fd_read, fd_write = os.pipe() # création et ouverture du tube anonyme
    fork_result = os.fork()

    if fork_result == 0:
        os.close(fd_read)  
        os.dup2(fd_write, 1) # redirection: la commande alimente le tube 
        os.close(fd_write)
        os.execvp(cmd, args)

    os.close(fd_write)
    acc = b""
    while True:
        msg = os.read(fd_read, 100)
        if len(msg) == 0 : 
            break
        acc += msg
    os.close(fd_read)
    os.wait()
    return acc.decode()

print("test de capture_stdout")
out = capture_stdout("ls", ["ls", "-l"])
print("sortie capturée :", out)