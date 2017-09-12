#For the correct function this program must be
#execute on Python3.

#In this program a Client connect to a Server.

#Try to use parts of this program for future programs...

from socket import *
import sys

HOST = 'Google.com'             #Or: 'localhost'
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':

    Client_Socket = socket(AF_INET, SOCK_STREAM)
    Client_Socket.connect(ADDR)

    while 1:
        data = 'GET / HTTP/1.0\r\n\r\n'

        if not data:
            break
        Client_Socket.send(data.encode('utf-8'))
        data = Client_Socket.recv(BUFSIZ)

        if not data:
            break
        print(data.decode('utf-8'))

    Client_Socket.close()
