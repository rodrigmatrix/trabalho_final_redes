#import socket module
from socket import *
import sys # para terminar o programa
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepara o socket servidor
serverSocket.bind(('', 8080))
serverSocket.listen(1)
while True:
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.readlines()
        f.close()
        #codigo_inicio
        #codigo_fim
        connectionSocket.send('HTTP/1.0 200 OK\n'.encode())
        connectionSocket.send('Content-type: text/html\n\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.0 404 Not Found\n'.encode())
        connectionSocket.send('Content-type: text/html\n\n'.encode())
        connectionSocket.send(""" 
        <html>
            <body>
                Status 404 - File Not Found
            </body>
        </html>        
        """.encode())
        connectionSocket.close()
serverSocket.close()
sys.exit()
#Termina o programa depois de enviar os dados