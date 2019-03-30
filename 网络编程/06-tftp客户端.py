import socket
import struct
# import sys


server_ip = "192.168.30.135"
dest_file = ""
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def get_file_info():
     # if len(sys.argv) < 3:
     #     print("程序需要2个参数，第一个参数是服务器IP，第二个参数是文件名称")
     #     exit()
    global server_ip
    global dest_file
    server_ip = "192.168.30.135"
    dest_file = "wire.rar"


def down_up_str(opt, data):

    str_data = struct.pack("!H"+str(len(data))+"sb5sb", opt, data.encode("utf-8"),
                           0, "octet".encode("utf-8"), 0)
    return str_data


def main():
    get_file_info()

    send_data = down_up_str(1, "wire.rar")

    # # 构建发送报文,字符串要先编码
    # print(send_data)
    udp_socket.sendto(send_data, (server_ip, 69))

    while True:

        ret = udp_socket.recvfrom(1024)
        content, source_ip = ret
        # 收到数据后，需要先解包。获取到前4个字节的重要判断内容
        opt, current_pack = struct.unpack("!HH", content[:4])
        ack = struct.pack("!HH", 4, current_pack)
        print(current_pack)
        if opt == 3:
            # 第一次接受到数据，即代表需要创建新文件
            if current_pack == 1:
                open_file = open(dest_file, "ab")
                # 第一次写入字节
                open_file.write(content[4:])
                # 回复ack
                udp_socket.sendto(ack, source_ip)
            else:
                # 如果不是第一次创建文件，则直接写入即可。
                if len(content[4:]) >= 512:
                    open_file.write(content[4:])
                    # 也需要回复ack
                    udp_socket.sendto(ack, source_ip)
                else:
                    # 如果数据小于512 即数据传输完毕
                    open_file.write(content[4:])
                    udp_socket.sendto(ack, source_ip)
                    open_file.close()
                    print("数据传输完毕")
                    break

    udp_socket.close()


def upload():
    cmd_buf = struct.pack("!H9sb5sb", 2, "mycat.zip".encode("utf-8"), 0,
                          "octet".encode("utf-8"), 0)
    udp_socket.sendto(cmd_buf, (server_ip, 69))
    local_ack = 0
    # 发送上传请求后，服务器会回复ack确认
    while True:
        recv_data, recv_ip = udp_socket.recvfrom(1024)
        recv_cmd, recv_ack = struct.unpack("!HH", recv_data[:4])
        print(recv_cmd, recv_ack)
        # 服务器回复确认,服务器回复ack为0后，即可以发送第一个数据包
        if recv_cmd == 4:
            # 第一个数据包
            if recv_ack == 0:
                try:
                    print("1")
                    open_file = open("mycat.zip", "rb")
                except:
                    print("打开文件错误")
                    break
            if local_ack == recv_ack:
                #print(local_ack, recv_ack)
                send_data = open_file.read(512)
                local_ack += 1
                print(local_ack, recv_ack)
                send_buf = struct.pack("!HH", 3, local_ack)
                send_buf = send_buf + send_data
                print(send_buf)
                udp_socket.sendto(send_buf, recv_ip)
        else:
            break
    udp_socket.close()
    open_file .close()

if __name__ == "__main__":
    #main()
    upload()

