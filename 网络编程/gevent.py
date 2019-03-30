import os
import time
import gevent
from gevent import monkey, socket


# 修改标准库的命令为非堵塞
monkey.patch_all()





def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("recv:", data)
        conn.send(data)


def server(port):
    s = socket.socket()
    s.bind(('', port))
    s.listen()
    while True:
        cli, addr = s.accept()
        print(cli)
        gevent.spawn(handle_request, cli)

if __name__ == "__main__":
    server(8889)