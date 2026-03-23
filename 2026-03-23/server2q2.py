import select, socket, sys
HOST = "127.0.0.1" # or 'localhost' or '' - Standard loopback interface address
PORT = 2004 # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()


fd_list = [serversocket, 0]
while len(fd_list) > 0:
    print(f"{fd_list=}")
    (readable, _, _) = select.select(fd_list, [], [])
    for s in readable:
        if s == serversocket: # serversocket receives a connection
            (clientsocket, (addr, port)) = s.accept()
            print("connection from:", addr, port)
            fd_list.append(clientsocket)
        elif s == 0: # stdin receives input
            print("input received from stdin, shutting down server...")
            data = input() # os.read(0, MAXBYTES) --- IGNORE ---
            # on arrête le serveur si l'utilisateur tape quelque chose
            for fd in fd_list: # on ferme tous les clients connectés
                if fd != serversocket and fd != 0:
                    fd.shutdown(socket.SHUT_RDWR)
                    fd.close()
            serversocket.close() # on ferme le serveur
            sys.exit(0) # on arrête le serveur
        else: # data is sent from given client
            data = s.recv(MAXBYTES)
            if len(data) > 0:
                s.sendall(data)
            else: # client has disconnected
                s.close()
                fd_list.remove(s)
serversocket.close()
