#coding=utf-8
from socket import *
from time import sleep

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)

#connNum = int(input("请输入要最大的链接数:"))

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcpSerSocket.listen(10)

while True:

    # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
    newSocket, clientAddr = tcpSerSocket.accept()
    print (clientAddr)
    sleep(1)