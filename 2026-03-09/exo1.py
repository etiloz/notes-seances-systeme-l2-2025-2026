# import os, sys
# fd1 = os.open("toto.txt", os.O_RDONLY)
# print(fd1) # 3 (pris avant: 0 pour stdin, 1 pour stdout, 2 pour stderr)
# os.close(fd1) # 3 est libéré
# fd2 = os.open("titi.txt", os.O_RDONLY)
# print(fd2)  # 3
# fd3 = os.open("titi.txt", os.O_RDONLY)
# print(fd3)   # 4
# os.close(fd2)
# os.close(fd3)
# sys.exit(0)

# import os, sys
# fd1 = os.open("toto.txt", os.O_RDONLY)
# bytes_sequence = os.read(fd1, 2) # séquence d'octets
# print(bytes_sequence) # 2 premiers octets du fichier, b'az'
# print(bytes_sequence.decode("utf-8"))  # 'az'
# bytes_sequence = os.read(fd1, 1)   # le 3ème octet du fichier, i.e le premier des deux octets qui code é
# os.close(fd1)
# print(bytes_sequence)   # b'\xc3'
# print(bytes_sequence.decode("utf-8"))
# sys.exit(0)

# import os, sys
# fd1 = os.open("toto.txt", os.O_RDONLY)
# fd2 = os.open("toto.txt", os.O_RDONLY)
# bytes_sequence = os.read(fd1, 2) # séquence d'octets
# bytes_sequence = os.read(fd2, 6)
# os.close(fd1)
# os.close(fd2)
# print(bytes_sequence)   # 6 premiers octets du fichier, b'az\xc3\xa9rt
# print(bytes_sequence.decode("utf-8"))
# print(bytes_sequence.decode("latin-1"))
# sys.exit(0)

# import os, sys
# fd = os.open("toto.txt", os.O_RDONLY)
# pid = os.fork()
# if pid == 0:
#     c = os.read(fd, 1)  # (1)
#     sys.exit(0)
# os.wait()
# c = os.read(fd, 1) # (2) après (1), à cause du wait -> même fichier ouvert, donc curseur avancé par le premier read, on lit le 2ème octet
# print(c)
# sys.exit(0)


import os, sys
fd1 = os.open("titi.txt", os.O_RDONLY)
fd2 = os.open("titi.txt", os.O_RDONLY)
c = os.read(fd2, 1)
os.dup2(fd2, fd1)
c = os.read(fd1, 1)
os.close(fd1)
os.close(fd2)
print(c)  # le deuxième octet, b'a'
sys.exit(0)