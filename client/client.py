# Клиент

import socket

# HOST = '192.168.77.77'
PORT = 8080

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect(('172.28.0.2', PORT))
con.send("Hello!".encode())
rd = con.recv(1024)
print(rd.decode())
con.close()
