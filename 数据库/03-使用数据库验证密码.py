from MysqlControl import MysqlControl
import hashlib

user = input("输入账户：")
passwd_plain = input("输入密码")
passwd_plain = passwd_plain.encode("utf-8")
passwd_encry = hashlib.sha1(passwd_plain).hexdigest()




#
conn = MysqlControl(host='127.0.0.1', username='test', passwd='Shell523569!', db='test')
conn.conn()
# 查询语句
sql = "SELECT password FROM stu WHERE name=%s"
name = [user]

result = conn.query(sql, name)

if result == ():
    print("查无此人")
elif result[0][0] == passwd_encry:
    print("密码正确")
else:
    print("密码错误")

