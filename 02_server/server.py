from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)

while True:
    print('Ready to serve...') 
    connectionSocket, addr = ""
    try:
        message = ""
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = ""
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
    except IOError:
        #Envia uma mensagem de resposta “File not Found”
        #Fecha o socket cliente
    serverSocket.close()
    sys.exit()
