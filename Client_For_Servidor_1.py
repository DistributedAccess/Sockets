#For the correct function this program must be
#execute on Python3.

#This program pretend communicate with Servidor_1.py

#In this program a Client can connect to a Server
#writting the Host name & Port name :)

#Try to use parts of this program for future programs...

from socket import *
import sys

HOST = 'localhost'
PORT = 1105
BUFSIZ = 512

if __name__ == '__main__':

    try:
        Client_Socket = socket(AF_INET, SOCK_STREAM)
    except socket.error as err:
        print("Failed to create a socket")
        print("Reason: %s" %str(err))
        sys.exit();

    print('The Sockets has Created')

    Target_Host = input("Enter the Target_Host name to connect[%s]: " %HOST) or HOST
    Target_Port = input("Enter the Target_Port [%s]: " %PORT) or PORT

    ADDR = (Target_Host, int(Target_Port))
    Client_Socket.connect(ADDR)

    Playload = 'GET ME THE TIME MFKR!'

    try:
        while True:
            Client_Socket.send(Playload.encode('utf-8'))
            data = Client_Socket.recv(BUFSIZ)
            print(data)
            more =  input("Want to send more data to Server [Y/N]: ")
            if more.lower() == 'y':
                Playload = input("Write here whatever you want! Muahahaha: ")
            else:
                break
    except KeyboardInterrupt:
        print("Exited by user")

    Client_Socket.close()
