class PassError(BaseException):
    def __init__(self,passlen):
        print("密码长度不够，要求为8，你的密码长度为：%s"%(passlen))

class Dog:
    pass


def inputpass():
    passwd = input("请输入密码")
    if len(passwd)< 8:
        raise PassError(len(passwd))


try:
    inputpass()
except PassError:
    pass


