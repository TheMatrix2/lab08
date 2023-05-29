# Сервер

import logging
import socket

HOST = '127.0.0.1'
PORT = 8080

logging.basicConfig(level=logging.INFO)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
logging.info(f'Server started')

while True:
    con, addr = sock.accept()
    output = ''
    data = con.recv(1024).decode()
    output += data
    con.send('Hello! Connect!'.encode())
    if not data:
        break
    print(output)
