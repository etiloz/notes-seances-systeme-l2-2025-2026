# on redirige l'entree standard vers a.out
import os
fd = os.open("a.out", os.O_RDONLY)
os.dup2(fd, 0)
os.close(fd)  # <- bonne pratique, fermer un descripteur de fichier inutile

MAXBYTES = 1024
byts = os.read(0, MAXBYTES) # s = input()
os.write(1, byts)           # print(s)