import os, sys

# attention à l'ordre d'ouverture des tubes : même ordre dans les deux programmes
fd_w = os.open("back2front.fifo", os.O_WRONLY)
fd_r = os.open("front2back.fifo", os.O_RDONLY)
print("tubes ouverts")
MAXBYTES = 1024


while True:


    
    byts = os.read(fd_r, MAXBYTES) # réception
    if not byts:
        break
    if os.fork() == 0:
        args = byts[:-1].decode().split(" ")
        cmd = args[0]
        os.execvp(cmd, args)
    os.wait()
    os.write(fd_w, b"ack")  # envoi
