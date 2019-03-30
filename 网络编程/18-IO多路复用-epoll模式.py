import socket
import select
import queue

s_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_socket.bind(("", 8889))
s_socket.listen()

# 创建epoll对象，用于监控套接字
e = select.epoll()

# epoll第一个参数是提供需要监控的套接字的FD，第二个参数是指定如何去监控，例如监控模式和对哪些消息进行监控。
# ET模式效率比LT要高
e.register(s_socket.fileno(), select.EPOLLIN|select.EPOLLET)
c_socket = {}
c_socket[s_socket.fileno()] = s_socket
w_list_queue = {}


while True:
    print("等待着新事件的发生")
    # 当有事件发生时，epoll会返回事件列表，包含fd和事件类型
    events = e.poll()
    # if not events:
    #     print("这一秒没有发生任何事件，继续下轮等待")
    #     continue
    # else:
    #     print("有%d个事件发生"%(len(events)))

    # 有事件发生,开始遍历有事件发生的套接字
    for fd, event in events:
        # print(fd)
        # 首先，取出有事件发生的套接字
        n_socket = c_socket[fd]
        print(event)
        # 判断是否新连接
        if n_socket == s_socket:
            new_conn, addr = n_socket.accept()
            # 在epoll注册
            e.register(new_conn.fileno(), select.EPOLLIN|select.EPOLLET)
            # 把客户的套接字引用保存在字典中
            c_socket[new_conn.fileno()] = new_conn
            # 为客户创建一个消息队列
            w_list_queue[new_conn.fileno()] = queue.Queue()
            print("有新连接了，客户信息%s" % (str(addr)))

        # 可读事件
        elif event == select.EPOLLIN:
            # print("我在可读事件中")
            # 取出数据
            data = n_socket.recv(1024)
            # 客户端是否关闭连接？
            if not data:
                e.unregister(fd)
                del c_socket[fd]
                print("客户断开")
            else:
                # 加入到可写事件中。
                w_list_queue[fd].put(data)
                # 把该fd修改成EPOLLOUT，由下面的循环处理，在一定程度上能解耦
                e.modify(fd, select.EPOLLOUT)

        # 可写事件
        elif event == select.EPOLLOUT:
            # print("我在可写事件中")
            #print(w_list_queue)
            try:
                send_data = "copy:".encode("gb2312") + w_list_queue[fd].get_nowait()
                n_socket.send(send_data)
            except :
                print("Queue is empty")
            # 处理完，必须把套接字fd修改回读事件，否则会一直处于写状态
            e.modify(fd, select.EPOLLIN)



e.close()