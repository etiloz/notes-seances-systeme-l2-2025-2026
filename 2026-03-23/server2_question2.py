import select, socket, sys
HOST = "127.0.0.1" # or 'localhost' or '' - Standard loopback interface address
PORT = 2004 # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()


fdlist = [serversocket, 0]
while len(fdlist) > 0:
    print(f"{fdlist=}")
    (readable, _, _) = select.select(fdlist, [], [])
    for fd in readable:
        if fd == serversocket: # serversocket receives a connection
            (clientsocket, (addr, port)) = fd.accept()
            print("connection from:", addr, port)
            fdlist.append(clientsocket)
        elif fd == 0: # stdin receives input
            data = input()
            # on arrête le serveur si l'utilisateur tape quelque chose
            for fd in fdlist:
                if fd != serversocket and fd != 0:
                    fd.shutdown(socket.SHUT_RDWR)
                    fd.close()
            serversocket.close()
            sys.exit(0)
        else: # data is sent from given client
            data = fd.recv(MAXBYTES)
            if len(data) > 0:
                fd.sendall(data)
            else: # client has disconnected
                fd.close()
                fdlist.remove(fd)
serversocket.close()
