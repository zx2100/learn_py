import socket
import multiprocessing
import re

class Httpserver(object):

    def __init__(self):
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_socket.bind(("", 80))
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_socket.listen()

    def start(self):
        while True:
            conn_sock, conn_ip = self.s_socket.accept()
            p = multiprocessing.Process(target=self.handle, args=(conn_sock,))
            p.start()
            conn_sock.close()

    def handle(self, cli_socket):
        # 返回数据
        recv_data = cli_socket.recv(1024)
        list_recv_data = recv_data.decode("utf-8").split("\r\n")

        # 获取首行数据
        first_line = list_recv_data[0]
        # print(first_line)

        # 设置根目录
        ROOT_DIR = "./html"

        # 获取请求方法 GET / HTTP/1.1
        request_method = re.search(r"^[A-Z]*", first_line).group()
        request_uri = re.search(r"/\w*\.?\w*", first_line).group()
        print("请求方法%s ,请求uri%s " % (request_method, request_uri))

        # 补全首页文件
        if "/" == request_uri:
            request_uri = "/index.html"

        # 打开请求文件
        try:
            # 执行成功的
            request_file = open(ROOT_DIR+request_uri, "rb")
            request_file_data = request_file.read()
            request_file.close()

            # 组建响应报文
            # 组建起始行
            send_data = "HTTP/1.0 200 ok \r\n"

            # 组建HTTP报文头
            send_data = send_data + "Content-Type: text/html\r\n"
            send_data = send_data + "charset=utf8\r\n"

            # 分割行，必须在HTTP头部尾部
            send_data = send_data + "\r\n"

            # 组建body
            send_data = bytes(send_data.encode("utf-8"))
            send_data = send_data + request_file_data

        except FileNotFoundError:
            # 执行不成功的
            send_data = "HTTP/1.0 404 404 Not Found \r\n"
            # 组建HTTP报文头
            send_data = send_data + "Content-Type: text/html;charset=utf8\r\n"

            # 分割行，必须在HTTP头部尾部
            send_data = send_data + "\r\n"
            send_data = send_data + "找不到指定资源!"
            send_data = send_data.encode("utf-8")



        # 响应数据
        cli_socket.send(bytes(send_data))
        cli_socket.close()






def main():
    http_server = Httpserver()
    http_server.start()


if __name__ == "__main__":
    main()