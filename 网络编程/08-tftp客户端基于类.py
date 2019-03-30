import socket
import struct


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class Service(object):

    def __init__(self, ip, filename, socket_file ):
        self.server_ip = ip
        self.file_name = filename
        self.socket_file = socket_file

    def download(self):
        # 构建TFTP协议报文
        send_buf = struct.pack("!H%dsb5sb" % (len(self.file_name)), 1,
                               self.file_name.encode("utf-8"), 0,
                               "octet".encode("utf-8"), 0)

        # 发送要下载的文件名字
        self.socket_file.sendto(send_buf, (self.server_ip, 69))

        local_ack = 0
        # 服务器会回复数据
        while True:
            recv_data, recv_addr = self.socket_file.recvfrom(2048)
            recv_cmd, recv_ack = struct.unpack("!HH", recv_data[:4])
            # recv_cmd == 3即数据文件
            if recv_cmd == 3:
                # 收到的第一个数据
                print(recv_ack)
                if recv_ack == 1:
                    down_file = open(self.file_name, "ab")
                    local_ack += 1
                # 如果不是第一个数据包，直接写入，回复ack即可
                # 此方法有BUG，当数据ack到达65535后，服务器会把ack重置为0，此判断就出问题
                # if local_ack == recv_ack or recv_ack == 0:
                #     # 先判断是否收到的最后一个包,如果是，把这次数据写入后就退出循环
                #     if len(recv_data[4:]) < 512:
                #         down_file.write(recv_data[4:])
                #         down_file.close()
                #         print("数据下载成功")
                #         break
                #     else:
                #         down_file.write(recv_data[4:])
                #         local_ack += 1
                #         send_buf = struct.pack("!HH", 4, recv_ack)
                #         # print(send_buf)
                #         self.socket_file.sendto(send_buf, recv_addr)
                # 重写此方法，解决BUG
                # 直接判断发送过来的数据大小是否小于512，如果是，就是最后一次传输。
                if len(recv_data[4:]) < 512:
                    down_file.write(recv_data[4:])
                    print("下载成功")
                    # 下载成功后，也需要回复最后一个确认包
                    send_buf = struct.pack("!HH", 4, recv_ack)
                    # print(send_buf)
                    self.socket_file.sendto(send_buf, recv_addr)
                    break
                else:
                    down_file.write(recv_data[4:])
                    local_ack += 1
                    send_buf = struct.pack("!HH", 4, recv_ack)
                    # print(send_buf)
                    self.socket_file.sendto(send_buf, recv_addr)
        # 循环结束，关闭文件
        down_file.close()

    def upload(self):
        # 构建TFTP协议上传报文
        send_buf = struct.pack("!H%dsb5sb" % (len(self.file_name)), 2,
                               self.file_name.encode("utf-8"), 0,
                               "octet".encode("utf-8"), 0)
        # 发送
        self.socket_file.sendto(send_buf, (self.server_ip, 69))

        local_ack = 0

        while True:
            recv_data, recv_addr = udp_socket.recvfrom(1024)
            recv_cmd, recv_ack = struct.unpack("!HH", recv_data[:4])
            # 服务器返回确认包文
            if recv_cmd:
                # 判断是否第一个确认包，如果是，则需要打开文件上传
                if recv_ack == 0:
                    try:
                        upload_file = open(self.file_name, "rb")
                    except:
                        print("文件不能打开，请查找原因")
                        exit()
                # 用于判断ack的返回值，如果ack接受不到，也就没传输的必要了，整个传输就是失败的
                if recv_ack == local_ack:
                    # 开始读入
                    send_data = upload_file.read(512)
                    local_ack += 1

                    # 如果小于512则表示读完了
                    if len(send_data) < 512:
                        send_buf = struct.pack("!HH", 3, local_ack)
                        send_buf = send_buf+send_data
                        self.socket_file.sendto(send_buf, recv_addr)
                        print("上传完成")
                        break
                    else:
                        send_buf = struct.pack("!HH", 3, local_ack)
                        send_buf = send_buf + send_data
                        self.socket_file.sendto(send_buf, recv_addr)
        upload_file.close()


def main():
    f = Service("192.168.30.135", "mycat.zip", udp_socket)
    f.upload()
    udp_socket.close()


if __name__ == "__main__":
    main()