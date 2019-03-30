import socket


s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_socket.bind(("", 8889))
s_socket.listen()
s_socket.setblocking(False)
client_list = []


def client():
    # yield使用时注意，最好确保yield能一直循环，因为如果这里循环到底了，
    # 即函数已经执行完了，那么在外层继续调用next会报错的
    while True:
        for s in client_list:
            try:
                data = s.recv(1024)
            except:
                # 没有数据就继续查看下一个客户端是否有数据
                continue
            else:
                if not data:
                    s.close()
                    client_list.remove(s)
                    print("有客户退出了，当前列表长度为%d" % (len(client_list)))
                else:
                    send_data = "i hear you".encode("gb2312") + data
                    s.send(send_data)

        yield


def main(func):
    while True:
        try:
            new_conn, new_addr = s_socket.accept()
        except:
            # 当前如果取不到新的客户端，则进入协程，看看是否有客户端有数据，
            func.__next__()
        else:
            print("有新客户了，客户信息%s" % (str(new_addr)))
            new_conn.setblocking(False)
            client_list.append(new_conn)


if __name__ == "__main__":
    c = client()
    main(c)

