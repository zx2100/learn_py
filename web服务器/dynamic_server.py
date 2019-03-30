import socket
import multiprocessing
import re
import sys


class Httpserver(object):

    def __init__(self, app_server):
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_socket.bind(("", 80))
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_socket.listen()
        self.response_headers = ""
        self.send_data = ""
        # 应用服务器
        self.app_server = app_server

    def start(self):
        try:
            while True:
                conn_sock, conn_ip = self.s_socket.accept()
                p = multiprocessing.Process(target=self.handle, args=(conn_sock,))
                p.start()
                conn_sock.close()
        finally:
            self.s_socket.close()

    # 组建HTTP头部
    def start_response(self, stat_us, headers):
        """组建HTTP头部和首行"""
        head_data = "HTTP/1.1 " + stat_us + "\r\n"
        for head in headers:
            head_data += "%s :%s\r\n" %head
        # 空白行
        head_data += "\r\n"
        # 编码成utf-8
        self.response_headers = head_data.encode("utf-8")

    # 处理用户请求
    def handle(self, cli_socket):
        # 返回数据
        recv_data = cli_socket.recv(1024)
        list_recv_data = recv_data.decode("utf-8").split("\r\n")

        # 获取首行数据
        first_line = list_recv_data[0]
        # print(first_line)

        # 设置根目录
        ROOT_DIR = "./html"
        WSGI_DIR = "./wsgi"

        # 添加wsgi目录到搜索路径
        sys.path.insert(1, WSGI_DIR)

        # 获取请求方法 GET / HTTP/1.1
        try:
            request_method = re.search(r"^[A-Z]*", first_line).group()
            request_uri = re.search(r"/\w*\.?\w*", first_line).group()
            print("请求方法%s ,请求uri%s " % (request_method, request_uri))

            # 补全首页文件
            if "/" == request_uri:
                request_uri = "/index.html"

            # 把请求URI传递进去
            env = {
                "PATH_INFO": request_uri,
            }

            # 先对请求进行动态分析，如果是动态内容，则优先输出
            # 获取动态内容的结果
            response_body = self.app_server(env, self.start_response)

            # 获取到动态body信息后，随机组建响应报文
            if response_body:
                # print("动态内容为：%s" % response_body)
                self.send_data = self.response_headers + response_body

            # ----------------以下是静态请求------------------------------------
            else:
                # 打开请求文件
                # 当打开不成功时，异常退出，执行except
                request_file = open(ROOT_DIR+request_uri, "rb")
                request_file_data = request_file.read()
                request_file.close()

                # 组建响应报文
                # 组建起始行
                send_data = "HTTP/1.1 200 ok \r\n"

                # 组建HTTP报文头
                send_data = send_data + "Content-Type: text/html\r\n"
                send_data = send_data + "charset=utf8\r\n"

                # 分割行，必须在HTTP头部尾部
                send_data = send_data + "\r\n"

                # 组建body
                send_data = bytes(send_data.encode("utf-8"))
                send_data = send_data + request_file_data
                self.send_data = send_data

        except Exception:
            # 执行不成功的
            send_data = "HTTP/1.1 404 404 Not Found \r\n"
            # 组建HTTP报文头
            send_data = send_data + "Content-Type: text/html;charset=utf8\r\n"

            # 分割行，必须在HTTP头部尾部
            send_data = send_data + "\r\n"
            send_data = send_data + "找不到指定资源!"
            send_data = send_data.encode("utf-8")
            self.send_data = send_data

        finally:

            # 响应数据
            print("响应报文%s" % self.send_data)
            cli_socket.send(bytes(self.send_data))

            cli_socket.close()



def main():
    http_server = Httpserver()
    http_server.start()


if __name__ == "__main__":
    main()