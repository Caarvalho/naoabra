from lib.menu import desenhar_menu
import os
# client.py
import socket
# create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # get local machine name
# host = '127.0.0.1'
# port = 9999
# # connection to hostname on the port.
# s.connect((host, port))

#draw menu
opcoes = desenhar_menu()
# if opcoes:
#     grandeza = opcoes[0]
#     origem = opcoes[1]
#     destino = opcoes[2]
#     entrada = opcoes[3]
#     data = "{grandeza};{origem};{destino};{entrada}\r\n\r\n"
#     s.send(data.encode('utf-8'))
#     resposta_buffer = s.recv(1024)
#     s.close()
#     if resposta_buffer:
#         resposta = resposta_buffer.decode('utf-8')
#         print("{:^127}".format(f"{resposta}"))

    
    
