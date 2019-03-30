import socket
import threading

udp_socket = None
udp_ip = ""
udp_port = 0


def sent_data():
    while True:
        data = input(">>")
        udp_socket.sendto(data.encode("gb2312"), (udp_ip, udp_port))


def recv_data():
    while True:
        ret = udp_socket.recvfrom(1024)
        content, source_ip = ret
        print("\r<<%s:%s\n\r>>" % (source_ip, content.decode("gb2312")), end="")


def main():
    global udp_socket
    global udp_ip
    global udp_port
    udp_ip = "192.168.2.103"
    udp_port = 8080
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8888))
    send = threading.Thread(target=sent_data)
    recv = threading.Thread(target=recv_data)
    send.start()
    recv.start()


if __name__ == "__main__":
    main()
