import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

for i in range(10):
    try:
        message = "Ping " + str(i+1)
        startTime = time.time()
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
        response, adress = sock.recvfrom(1024)
        endTime = time.time()
        elapsedTime = str(endTime - startTime)
        print(response, str(elapsedTime))
    except socket.timeout:
        print("Solicitação expirada ping", str(i+1))

