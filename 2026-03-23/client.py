import os, socket, sys
MAXBYTES = 4096
if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "hote port")
    sys.exit(1)
HOST = sys.argv[1]
PORT = int(sys.argv[2])
sockaddr = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # déclare la socket



s.connect(sockaddr)  # bloquant, jusqu'à ce que le serveur soit prêt et accepte la connexion. 

print("connected to:", sockaddr)
while True: 
    # Client synchrone !! On alterne écriture vers serveur 
    # et lecture depuis serveur. Le serveur doit donc lui aussi alterner
    line = os.read(0, MAXBYTES)
    if len(line) == 0:
        s.shutdown(socket.SHUT_WR)
        break
    s.send(line)
    data = s.recv(MAXBYTES) # attention, si le serveur n'envoie rien on est bloqué.
    if len(data) == 0:
        break
    os.write(1, data)
s.close()