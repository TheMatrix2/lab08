# Сервер

import logging
import socket

HOST = '127.0.0.1'
PORT = 8080

logging.basicConfig(level=logging.INFO)
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen()
logging.info(f'Server started')
# print(sock.accept())
con, addr = sock.accept()
con.send('Hello! Connect!'.encode())

while True:
    output = ''
    data = con.recv(1024).decode()
    output += data
    if not data:
        break
    print(output)
