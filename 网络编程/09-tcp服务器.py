import socket
import multiprocessing
import time


def service(socket, addr):
    while True:
        # print(socket, addr)
        recv_data = socket.recv(1024)
        print(recv_data.decode("gb2312"))
        if len(recv_data) <= 0:
            print("有客户主动断开")
            socket.close()
            return


s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(("", 8889))
s_socket.listen(100)
pool = multiprocessing.Pool(10)


while True:

    recv_socket, recv_addr = s_socket.accept()
    #print("有客户连接")
    pool.apply_async(func=service, args=(recv_socket, recv_addr))
    recv_socket.close()
    time.sleep(10)
    


s_socket.close()
c_socket.close()