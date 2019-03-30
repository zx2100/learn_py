import socket

a = int(input("数量:"))

for value in range(a):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8889))
    print(value)