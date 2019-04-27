import pymysql

# 连接数据库
connection = pymysql.connect(host="127.0.0.1",
                             user="root",
                             password="523569",
                             db='test',
                             charset='utf8mb4')

# 获取SQL游标
try:
    with connection.cursor() as cursor:
        # SQL语句,%s是占位符,指定了输入4个字段，所以有4个占位符
        sql = "INSERT INTO students(name,hometown,birthday) VALUES(%s,%s,%s)"
        name = input("请输入名字")
        hometown = input("城市")
        birthday = input("生日")

        value_list = [name, hometown, birthday]
        cursor.execute(sql, value_list)
        connection.commit()

finally:
    connection.close()


