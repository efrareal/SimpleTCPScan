import socket

# AF_INET = IPv4 address | SOCK_STREAM = TCP connection
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Direccion IP a scanear: \n")
port = int(input("[*] Puerto TCP: \n"))

def PortScanner(port):
    if mysocket.connect_ex((host,port)):
        print("Puerto %d esta cerrado" %port)
    else:
        print("Puerto %d esta abierto" %port)

PortScanner(port)
