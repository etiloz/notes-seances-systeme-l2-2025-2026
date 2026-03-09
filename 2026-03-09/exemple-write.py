# on ouvre un fichier toto.out et on ecrit hello dedans

import os
fd = os.open("toto.out", os.O_WRONLY | os.O_CREAT | os.O_APPEND)
os.write(fd, b'hal')
#nb_octets = os.write(fd, b'lo') # nb_octetst effectivement écrits
os.close(fd)