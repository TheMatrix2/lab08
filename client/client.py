# Клиент

import socket

HOST = '127.0.0.2'
PORT = 8080

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect_ex((HOST, PORT))
rd = con.recv(1024)
print(rd.decode())
con.send("Hello!".encode())
con.close()
