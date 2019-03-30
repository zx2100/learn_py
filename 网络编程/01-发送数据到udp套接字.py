import socket


def sendTo(sendData, socket):

    sendAddr = ("192.168.2.103", 8080)

    ret = socket.sendto(sendData.encode("gb2312"), sendAddr)
    print(ret)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for num in range(10):
        sendData1 = " 测试 " + str(num)
        sendTo(sendData1, s)
    s.close()


if __name__ == "__main__":
    main()