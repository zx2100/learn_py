import gevent
from gevent import socket, monkey




monkey.patch_all()

s_socket = socket.socket()
s_socket.bind(("", 8889))
s_socket.listen()
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_list = []

def client_service():
    for socket in client_list:
        print("2")
        data = socket.recv(1024)
        if not data:
            socket.close()
            return
        else:
            send_data = "return : ".encode("gb2312")+ data
            socket.send(send_data)


def listen_server():
    g2 = gevent.spawn(client_service)
    while True:

        new_conn, new_addr = s_socket.accept()

        # 如果有一个新的客户就新建一个协程来服务客户,在协程内并不需要遍历套接字
        # 因为对于服务器，每当有新的客户端来连接，都会新建一个协程来处理


        # 把新客户加入列表
        client_list.append(new_conn)
        # 这是等待g2完成任务，所以g2不能有死循环，否则新客户接受不到，
        # 并且，对于连接多了情况下，新客户的接受会不及时，因为它在等待g2的遍历
        print("列表长度为：%d"%len(client_list))

        # 堵塞至此，等待g2遍历完成
        g2.join()



def main():
    print("123")
    g1 = gevent.spawn(listen_server)
    # 这是等待g1同步，因为g1是死循环，所以程序进去就基本上不会出来了。
    g1.join()
    # 这句永远都不会执行，因为在g1有个死循环
    print("asd")

if __name__ == "__main__":
    main()

