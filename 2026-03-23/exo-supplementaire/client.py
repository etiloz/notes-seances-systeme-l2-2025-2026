import os, socket, sys, select
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
fds = [s, 0] 
while True: 
    # attend des données sur l'entrée standard ou sur la socket
    readable, _, _ = select.select(fds, [], []) 
    for fd in readable:
        if fd == 0: 
            # si les données viennent de l'entrée standard, 
            # on les lit et on les envoie au serveur via la socket
            line = os.read(0, MAXBYTES)
            if len(line) == 0:
                s.shutdown(socket.SHUT_WR)
                s.close()
                sys.exit(0)
            s.send(line)
        elif fd == s:
            # si les données viennent de la socket, on les lit et on 
            # les affiche
            data = s.recv(MAXBYTES) # attention, si le serveur n'envoie rien on est bloqué.
            if len(data) == 0:
                s.close()
                sys.exit(0)
            os.write(1, data)
