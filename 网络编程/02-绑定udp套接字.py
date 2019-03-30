import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


address = ("", 8888)

s.bind(address)
ret = s.recvfrom(1024)
# 返回一个元组，有2个元素，第一个元素是内容，第二元素是发送方的信息
content, dest_ip = ret

print(content.decode("gb2312"))

s.close()
