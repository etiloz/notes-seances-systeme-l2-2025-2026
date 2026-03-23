import os, sys

# attention à l'ordre d'ouverture des tubes : même ordre dans les deux programmes
fd_r = os.open("back2front.fifo", os.O_RDONLY)
fd_w = os.open("front2back.fifo", os.O_WRONLY)
print("tubes ouverts")
MAXBYTES = 1024


while True:
    print("> ", end="", flush=True)
    byts = os.read(0, MAXBYTES)
    os.write(fd_w, byts) # envoi
    os.read(fd_r, MAXBYTES)  # réception







    
    
    os.read(fd_r, MAXBYTES)  # réception
