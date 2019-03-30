import socket
import multiprocessing
import time
import re

def service_client(c_socket):

    recv_data = c_socket.recv(1024)
    recv_data = recv_data.decode("utf-8")
    # 提取方法
    pa1 = re.compile(r"^\s?[A-Z]*\s")
    #提取请求资源
    pa2 = re.compile(r"^\s?.* ")
    first_line = pa2.search(recv_data)
    method = pa1.search(recv_data)
    if not method:
        c_socket.close()
        return
    # 获取方法文本信息
    method = method.group().rstrip()



    # 请求方法
    if method == "GET":
        # 获取请求资源
        root_path = "."
        requery_path = re.search("/.*\s", first_line.group()).group().rstrip()
        print(requery_path)
        if requery_path == "/":
            requery_path = "/index.html"
        print("requery_file：%s"%(requery_path))
        try:
            file = open(root_path+requery_path, "rb")
            print(file)
            file_data = file.read()
            file.close()
            send_data = b"HTTP/1.1 200 ok\r\nContent-Type: text/html;charset=utf8" \
                        b"\r\nContent-Length: " \
                        b"%d\r\n\r\n" % (len(file_data))
            print(send_data)
            send_data = send_data+file_data

        except:
            send_data = "HTTP/1.1 404 Not Found \r\nContent-Type: text/html;charset=utf8\r\n\r\n 我找不到你要的东西".encode("utf-8")
    else:
        send_data = "HTTP/1.1 400 deny \r\n\r\n DENY!!".encode("utf-8")
        c_socket.send(send_data)
        c_socket.close()
        return

    # 发生响应
    print(send_data)
    print(send_data)
    c_socket.send(send_data)
    c_socket.close()



# 创建套接字
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(("", 80))
s_socket.listen()
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


while True:
    client_socket, client_addr = s_socket.accept()
    #print("new client from %s" % str(client_addr))
    p1 = multiprocessing.Process(target=service_client, args=(client_socket,))
    p1.start()
    client_socket.close()

# 使用多进程等待客户连接
