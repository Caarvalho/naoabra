import socket
from lib.servidor.conversor import SpeedConversor, VolumeConversor, VolumeUnit, SpeedUnit, AllowedGrandezas

mapa_grandeza = {
    1: AllowedGrandezas.speed,
    2: AllowedGrandezas.volume
}

mapa_unidade_velocidade = {
    3: SpeedUnit.mps,
    4: SpeedUnit.kmph,
    5: SpeedUnit.mph
}

mapa_unidade_volume = {
    6: VolumeUnit.m3,
    7: VolumeUnit.liter,
    8: VolumeUnit.barrel,
}



# server.py
# create a socket object
serversocket = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
# get local machine name
host = '127.0.0.1'
port = 9999
# bind to the port
serversocket.bind((host, port))
# starts listening requests
serversocket.listen()
while True:
    try:
        # establish a connection
        clientsocket, addr = serversocket.accept()
        print("Got a connection from %s" % str(addr))
        tmp = clientsocket.recv(1024)
        
        pedido = tmp.decode('utf-8')
        pedido = pedido.strip()
        pedido = pedido.split(';')
        print(pedido)
        # input('45 CONTINUAR')
        #
        grandeza = mapa_grandeza[int(pedido[0])]
        origem = None
        destino = None
        conversor = None
        if grandeza == AllowedGrandezas.volume:
            origem = mapa_unidade_volume[int(pedido[1])]
            destino = mapa_unidade_volume[int(pedido[2])]
            conversor = VolumeConversor
        elif grandeza == AllowedGrandezas.speed:
            origem = mapa_unidade_velocidade[int(pedido[1])]
            destino = mapa_unidade_velocidade[int(pedido[2])]
            conversor = SpeedConversor
        else:
            raise Exception()
        entrada = float(pedido[3])
        resposta = conversor.convert(entrada, origem, destino)
        clientsocket.send(f"{resposta}".encode('utf-8'))

        #
        conversor = None

        # clientsocket.send(currentTime.encode('utf-8'))
        # input('Terminar sessão?')
        clientsocket.close()
    except Exception as e:
        print(e)
        clientsocket.close()
        # input('')
        break
# print('Servidor Morreu!')
# TESTE
