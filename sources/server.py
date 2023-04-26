# Сервер

import socket

HOST = ''  # Символическое имя, означающее все доступные интерфейсы
PORT = 12345  # Арбитражный не зарезервированный порт

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Подключен клиент:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

