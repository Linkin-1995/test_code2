"""
练习: 写一个函数input 输入一位学生的姓名
返回这个学生的分数.
学生信息存在cls表中
"""

import pymysql

class Database:
    def __init__(self):
        # 连接数据库 (连接本机可以不写host和port)
        self.db = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "123456",
                             database = "stu",
                             charset = "utf8"
        )

        # 创建游标 (执行sql语句获取执行结果的对象)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def get_score(self):
        name = input("Name:")
        sql = "select score from cls where name=%s;"
        # print(sql)
        self.cur.execute(sql,[name])
        # result --> (score,)
        result = self.cur.fetchone()
        return result[0]

if __name__ == '__main__':
    db = Database()
    print(db.get_score())
    db.close()

