
# client.py
import socket
import pickle
novaConsulta = 'Sim'
while novaConsulta == 'Sim':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9999
    s.connect((host, port))
    data = []
    print("1. Converter COMPRIMENTO;\n")
    print("2. Converter TEMPERATURA;\n")
    opcao1 = int(input("Qual a opção desejada?\n"))
    if opcao1 == 1:
        print("a. Converter de METRO para CENTIMETRO;\n")
        print("b. Converter CENTIMETRO para MILIMETRO;\n")
        opcao2 = str(input("Qual a opção desejada?\n"))
        if opcao2 == 'a':
            medida = int(input("Qual valor converter para CENTIMETRO?\n"))
        if opcao2 == 'b':
            medida = int(input("Qual valor converter para MILIMETRO?\n"))
    if opcao1 == 2:
        print("c. Converter de CELCIUS para FAHRENHEIT;\n")
        print("d. Converter CELCIUS para KELVIN;\n")
        opcao2 = str(input("Qual a opção desejada?\n"))
        if opcao2 == 'c':
            medida = int(input("Qual valor converter para FAHRENHEIT?\n"))
        if opcao2 == 'd':
            medida = int(input("Qual valor converter para KELVIN?\n"))

    data.append(opcao2)
    data.append(medida)
    s.send(pickle.dumps(data))
    nova_medida = s.recv(1024)
    nova_medida = pickle.loads(nova_medida)

    print("\nA medida convertida é: %s\n" % nova_medida)
    novaConsulta = str(input("Fazer uma nova consulta?\n Sim.\n Nao.\n"))
    s.close()

s.close()