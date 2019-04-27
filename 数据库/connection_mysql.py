import pymysql


connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='523569',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)




try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO students(name, hometown, birthday, gender)" \
              "VALUES" \
              "(" \
              "'张三丰','武当派','19110101',1" \
              ");"
        # print(sql)
        cursor.execute(sql)
        #result = cursor.fetchall()
        #print(result)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()

finally:

    connection.close()