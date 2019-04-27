import pymysql
import hashlib


class MysqlControl(object):

    def __init__(self, host='127.0.0.1', username='root', passwd='', db=''):
        self.host = host
        self.username = username
        self.passwd = passwd
        self.db = db
        self.connection = ''
        self.cursor = ''

    def conn(self):
        self.connection = pymysql.connect(host=self.host,
                                     user=self.username,
                                     password=self.passwd,
                                     db=self.db,
                                     charset='utf8mb4')
        self.cursor = self.connection.cursor()

    def query(self, sql, parameter=[]):
        result = ""
        try:
            self.cursor.execute(sql, parameter)
            result = self.cursor.fetchall()
        except Exception as e:
            print (e)
        return result

    def commit(self, sql, parameter=[]):

        try:
            with self.connection.cursor() as cursor:
                count = cursor.execute(sql, parameter)
                self.connection.commit()
                return "ok,effect" + str(count)
        except Exception as e:
            print(e)



    def close(self):
        return self.connection.close()



def main():
    test = MysqlControl(host='127.0.0.1', username='test', passwd='Shell523569!', db='test')
    test.conn()
    sql = 'INSERT INTO stu(name,password) VALUES (%s,%s)'
    passwd = hashlib.sha1("1234".encode("utf-8")).hexdigest()
    parameter = ('李钊文', passwd)
    print(test.commit(sql, parameter))



if __name__ == "__main__":
    main()