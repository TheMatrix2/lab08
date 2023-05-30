# Сервер

import logging
import socket
import perform

HOST = '127.0.0.1'
PORT = 8080

logging.basicConfig(level=logging.INFO)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
logging.info(f'Server started')

while True:
    con, addr = sock.accept()
    logging.info(f'Connected: {addr}')
    data = [int(x) for x in con.recv(1024).decode().split(',')]
    output = perform.perform(data[0], data[1], data[2], data[3])
    con.send(f"Hello! You're connected\n{output}".encode())
    if not data:
        break
