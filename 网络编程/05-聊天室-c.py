import socket
import threading

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", 8889))
source_ip = ("192.168.30.21", 8888)


def main():
    content = "new"
    # print(content)
    udp_socket.sendto(content.encode("utf-8"), source_ip)
    echo = threading.Thread(target=recv_msg)
    echo.start()
    send = threading.Thread(target=send_msg)
    send.start()


def recv_msg():
    # global source_ip
    while True:

        ret = udp_socket.recvfrom(1024)
        content = ret[0]
        content = content.decode("utf-8")
        # print("收到信息:%s" % (content))
        if content[0:3] == "chk":
            udp_socket.sendto("kep".encode("utf-8"), source_ip)
        elif content[0:3] == "msg":
            print("\r<<\n\r%s" % (content[3:]))


def send_msg():
    while True:
        content = input(">>")
        content = "msg"+content
        # print(source_ip)
        udp_socket.sendto(content.encode("utf-8"), source_ip)


if __name__ == "__main__":
    main()