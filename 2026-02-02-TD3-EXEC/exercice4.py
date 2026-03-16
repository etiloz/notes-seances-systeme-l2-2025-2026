import os

cmd1 = "who"
args1 = ["who"]
if os.fork() == 0:
    os.execvp(cmd1, args1)
pid, status = os.wait()

if ....:

    cmd2 = "pwd"
    args2 = ["pwd"]
    if os.fork() == 0:
        os.execvp(cmd2, args2)
    os.wait()

else:
    cmd3 = "ls"
    args2 = ["ls", "-l"]
    if os.fork() == 0:
        os.execvp(cmd3, args3)
    os.wait()
