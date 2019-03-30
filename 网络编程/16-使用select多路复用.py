import socket
import select
import queue

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(("", 8889))
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)
s_socket.listen(128)
input_list = [s_socket]
output_list = []


def main():
    data_queue = {}
    # 如果监控的fd没有活动，程序会堵塞在这里
    while True:
        readable, writeable, exceptional = select.select(input_list, output_list, input_list)

        # 循环可读列表
        for s in readable:
            # 表示有客户连接
            if s is s_socket:
                conn, client_addr = s.accept()
                print("new connection from", client_addr)
                # 把client套接字加入input_list,下次循环由select监控
                input_list.append(conn)
                # 创建客户端的消息队列缓存，用于保存客户发送过来的数据
                data_queue[conn] = queue.Queue()

            # 如果有消息的套接字不是s_socket,那就是客户有数据发送过来了。
            else:
                data = s.recv(1024)
                if data:
                    # 如果data不为空，那就获取下来打印
                    print("recv %s from%s" % (data, s.getpeername()))
                    # 把消息放入data_queue字典中
                    data_queue[s].put(data)

                    # 把有消息的套接字放入到列表中，在可写循环中处理，不在这里做处理
                    if s not in output_list:
                        output_list.append(s)

                else:
                    # 如果data为空，表示客户主动断开
                    print("disconnet by the %s" % (str(s.getpeername())))
                    s.close()
                    input_list.remove(s)

        # 循环可写列表
        for s in writeable:
            try:
                data = data_queue[s].get_nowait()
            # 如果队列为空，则没必要再检测了
            except queue.Empty:
                print("Empty of queue")
                output_list.remove(s)
            else:
                # 如果有数据则回复
                data = "copy:".encode("gb2312") + data
                s.send(data)


if __name__ == "__main__":
    main()
