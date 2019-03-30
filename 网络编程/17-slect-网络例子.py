# -*- coding: UTF-8 -*-

import select
import socket
import queue
import sys

# Create a TCP/IP socket
server = socket.socket()
# set noblocking
server.setblocking(False)

# Bind the socket to the port
server_address = ('', 9999)
print(sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)

# Listen for incoming connections
server.listen()

# 所有连接进来的对象都放在inputs
inputs = [server, ]  # 自己也要监控，因为server本身也是个对象

# 需要发送数据的对象
outputs = []

# 对外发送数据的队列，记录到字典中
message_queues = {}

while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # 如果没有任何fd就绪,那程序就会一直阻塞在这里

    for s in readable:  # 每一个s就是有个socket

        if s is server:
            # 别忘记,上面我们server自己也当做一个fd放在了inputs列表里,传给了select,如果这个s是server,代表server这个fd就绪了,
            # 就是有活动了, 什么情况下它才有活动? 当然 是有新连接进来的时候
            # 新连接进来了,接受这个连接
            conn, client_addr = s.accept()
            print("new connection from", client_addr)
            conn.setblocking(0)
            inputs.append(conn)
            # 为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接
            # 就会被交给select去监听,如果这个连接的客户端发来了数据 ,那这个连接的fd在server端就会变成就续的,select就会把这个连接返回,
            # 返回到readable 列表里,然后你就可以loop readable列表,取出这个连接,开始接收数据了, 下面就是这么干的

            message_queues[conn] = queue.Queue()
            # 接收到客户端的数据后,不立刻返回 ,暂存在队列里,以后发送

        else:  # s不是server的话,那就只能是一个 与客户端建立的连接的fd了
            # 客户端的数据过来了,在这接收
            data = s.recv(1024)
            if data:
                print('received [%s] from %s' % (data, s.getpeername()[0]))
                message_queues[s].put(data)  # 收到的数据先放到queue里,一会返回给客户端
                if s not in outputs:
                    outputs.append(s)  # 为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端

            else:  # 如果收不到data代表什么呢? 代表客户端断开了
                print("client [%s] closed", s)

                if s in outputs:
                    # 既然客户端都断开了，我就不用再给它返回数据了，
                    # 所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                    outputs.remove(s)

                inputs.remove(s)  # 这个连接必然在inputs中，也删掉
                s.close()

                # 关闭的连接在队列中也删除
                del message_queues[s]

    for s in writable:

        try:
            next_msg = message_queues[s].get_nowait()
            print(next_msg)
        except queue.Empty:
            # 没有数据了，该连接对象队列为空，停止检测
            print('output queue for [%s] is empty' % s.getpeername()[0])
            outputs.remove(s)

        else:
            print('send %s to %s' % (next_msg, s.getpeername()[0]))
            s.send(next_msg)

    for s in exceptional:
        print('handling exceptional condition for', s.getpeername()[0])
        # 从inputs中删除
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # 删除队列
        del message_queues[s]