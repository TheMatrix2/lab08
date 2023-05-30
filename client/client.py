# Клиент

import socket

HOST = '192.168.77.77'
PORT = 8080
p = [10, 10, 20, 20]

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((HOST, PORT))
con.send(f'{p[0]},{p[1]},{p[2]},{p[3]}'.encode())
rd = con.recv(1024)
print(rd.decode())
con.close()
