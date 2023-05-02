
# server.py
import socket
import pickle
import time
import math

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

serversocket.bind((host, port))

serversocket.listen()
print("Server running...\n")
while True:

    clientsocket, addr = serversocket.accept()
    print("Conectado a %s" % str(addr))
    data = clientsocket.recv(1024)
    data = pickle.loads(data)
    opcao = data[0]
    medida = data[1]
    if opcao == 'a':
        medida = medida * 100

    if opcao == 'b':
        medida = medida * 10

    if opcao == 'c':
        medida = (medida * 9/5) + 32

    if opcao == 'd':
        medida = medida + 273

    medida = pickle.dumps(medida)
    clientsocket.send(medida)
    clientsocket.close()