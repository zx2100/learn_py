import gevent
from gevent import socket, monkey

monkey.patch_all()

s_socket = socket.socket()
s_socket.bind(("", 8889))
s_socket.listen()
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def client_service(socket):
    while True:
        print("2")
        data = socket.recv(1024)
        if not data:
            socket.close()
            return
        else:
            send_data = "return : ".encode("gb2312")+ data
            socket.send(send_data)


def listen_server():

    while True:

        new_conn, new_addr = s_socket.accept()

        # 如果有一个新的客户就新建一个协程来服务客户,在协程内并不需要遍历套接字
        # 因为对于服务器，每当有新的客户端来连接，都会新建一个协程来处理
        print(new_conn)
        gevent.spawn(client_service, new_conn)


if __name__ == "__main__":
    listen_server()
