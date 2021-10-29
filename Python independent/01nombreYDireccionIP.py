import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

cadenaDeTexto = (f'El nombre de tu ordenador es: {hostname}.  \n Tu dirección Ip es: {ip}.')
print(cadenaDeTexto)

input()

