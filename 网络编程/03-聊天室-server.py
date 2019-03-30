import socket
import time
import threading
# from multiprocessing import Pool


udp_socket = None
user_list = []
check_alive_list = set()





def main():
    global udp_socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_addr = ("", 8888)
    udp_socket.bind(udp_addr)
    conn = threading.Thread(target=wait_conn)
    conn.start()
    check = threading.Thread(target=check_alive)
    check.start()


def wait_conn():

    global user_list
    global check_alive_list
    while True:
        ret = udp_socket.recvfrom(1024)
        content, source_info = ret
        # 先解码获取内容
        content = content.decode("utf-8")
        # 新建连接
        # print("收到信息：%s" % (content))

        if content[0:3] == "new":
            # 去重
            if source_info not in user_list:
                user_list.append(source_info)
            print("当前在线用户："+str(user_list))
        elif content[0:3] == "kep":
            if check_alive_list:
                check_alive_list.remove(source_info)
        elif content[0:3] == "msg":
            # 发送数据到所有主机
            for hosts in user_list:
                print("发送数据到%s主机,内容是：%s"%(hosts, content[3:]))
                sent_txt = "msg"+str(source_info)+content[3:]
                udp_socket.sendto(sent_txt.encode("utf8"), hosts)

        else:
            continue


def check_alive():
    global user_list
    global check_alive_list
    while True:
        # print (check_alive_list)
        for host in user_list:
            udp_socket.sendto("chk".encode("utf-8"), host)
            check_alive_list.add(host)
        time.sleep(2)


if __name__ == "__main__":
    main()
