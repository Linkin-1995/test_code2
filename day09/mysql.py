"""
pymysql 连接数据库
"""

import pymysql

# 连接数据库 (连接本机可以不写host和port)
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "stu",
                     charset = "utf8"
)

# 创建游标 (执行sql语句获取执行结果的对象)
cur = db.cursor()

# 执行各种sql语句,操作数据库
print("假设执行了sql")


# 关闭游标和数据库连接
cur.close()
db.close()









