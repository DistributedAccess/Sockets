#For the correct function this program must be
#execute on Python3.

#In this program a Client can connect to a Server
#writting the Host name & Port name :)

#Try to use parts of this program for future programs...

from socket import *
import sys

if __name__ == '__main__':

    try:
        sock = socket(AF_INET, SOCK_STREAM)
    except socket.error as err:
        print("Failed to create a socket")
        print("Reason: %s" %str(err))
        sys.exit();

    print('The Sockets has Created')

    Target_Host = input("Enter the Target_Host name to connect: ")
    Target_Port = input("Enter the Target_Port: ")

    try:
        sock.connect((Target_Host, int(Target_Port)))
        print("The Socket has connected %s on port: %s" %(Target_Host, Target_Port))
        sock.shutdown(2)
    except socket.error as err:
        print("Failed to connect to %s on port: %s" %(Target_Host, Target_Port))
        print("Reason is: %s" %str(err))
        sys.exit()
