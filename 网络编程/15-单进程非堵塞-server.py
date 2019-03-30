import socket


l_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
l_socket.bind(("", 8889))

l_socket.listen(1024)
l_socket.setblocking(False)
client_list = []

# 等待客户端连接
while True:
    try:
        new_client, client_addr = l_socket.accept()
        # print(new_client)
    except:
        pass
    else:
        new_client.setblocking(False)
        client_list.append((new_client, client_addr))
        print("一共有%d个客户" % len(client_list))

    for client, addr in client_list:
        try:
            recv = client.recv(1024)
        except:
            pass
        else:
            # 判断是否长度为0，如果是则表示客户端关闭了连接
            if len(recv) <= 0:
                print("%s关闭了连接" % (str(addr)))
                client_list.remove((client, addr))
                client.close()
                print("当前长度%d" % len(client_list))
            else:
                print(recv)

