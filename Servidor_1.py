#For the correct function this program must be
#execute on Python3.

#

#Try to use parts of this program for future programs...

from socket import *
from time import *
import sys

#HOST = '10.7.31.237'
HOST = 'localhost'
PORT = 2018
BUFSIZ = 1024           #1kbit
ADDR = (HOST, PORT)

if __name__ == '__main__':

    Server_socket = socket(AF_INET, SOCK_STREAM)
    Server_socket.bind(ADDR)
    Server_socket.listen(5)
    Server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)    #Honestly I don't know what is this. The manual says that it puts the sockets options.

while True:

    print("Waiting for the connection...")
    Client_Socket, Addr = Server_socket.accept()
    print('Client connected from: ', Addr)

    while True:

        data = Client_Socket.recv(BUFSIZ)

        if not data or data.decode('utf-8') == 'END':
            break;

        print("Recived from Client: %s" % data.decode('utf-8'))
        print('Sending the Server time to Client: %s'  %ctime())

        try:
            Client_Socket.send(bytes(ctime(), 'utf-8'))
        except KeyboardInterrupt:
            print("Exited by user")

    Client_Socket.close()
    continue                #This is the line death D: 

    Server_socket.close()
