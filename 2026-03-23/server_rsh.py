import select, socket, os
HOST = "127.0.0.1" # or 'localhost' or '' - Standard loopback interface address
PORT = 2004 # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()

while True:
    (clientsocket, _) = serversocket.accept()
    if os.fork() == 0 :
        serversocket.close() # close the original socket in the child process
        os.dup2(clientsocket.fileno(), 0) # stdin
        os.dup2(clientsocket.fileno(), 1) # stdout
        os.dup2(clientsocket.fileno(), 2) # stderr
        clientsocket.close() # close the original socket in the child process
        os.execvp("bash", ["bash"])
    else:
        clientsocket.close() # close the original socket in the parent process