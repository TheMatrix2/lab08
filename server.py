import logging
import os.path
import socket
import enum
import os.path
import asyncio


class Status(enum.Enum):
    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]

    OK = (200, 'OK')
    NotFound = (404, 'Not Found')


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.in_size = 1024

    def response(self, proto, status, size=0):
        result = [
            f'{proto} {status.code} {status.msg}'
        ]
        if size != 0:
            result.append(f'Content-Length: {size}\r\n')
        result.append('')
        return '\r\n'.join(result).encode()

    async def handle_client(self, con, addr):
        loop = asyncio.get_event_loop()

        logging.info(f'{addr} connected')
        with con:
            while True:
                data = await loop.sock_recv(con, self.in_size)
                if not data:
                    break
                cmd = data.decode().splitlines()[0]
                logging.debug(f'{data}')
                method = cmd.split()[0]
                match method:
                    case 'GET':
                        path = cmd[1]
                        proto = cmd[2]
                        if path == '/':
                            path = '/index.html'
                        path = f'root{path}'
                        if os.path.isfile(path):
                            with open(path, 'rb') as file:
                                data = file.read()
                                response = self.response(proto, Status.OK, len(data))
                                response += data
                        else:
                            response = self.response(proto, Status.NotFound)
                        await loop.sock_sendall(con, response)
                    case _:
                        pass

    async def run(self):
        loop = asyncio.get_event_loop()

        sock = socket.socket()
        sock.bind((self.host, self.port))
        sock.listen()
        logging.info(f'Server started')
        while True:
            con, addr = await loop.sock_accept(sock)
            asyncio.create_task(self.handle_client(con, addr))


async def main():
    server = Server('127.0.0.1', 1234)
    await asyncio.create_task(server.run())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

