"""
数据库数据读取实例
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

# 执行select语句
sql = "select name,age,score from cls;"
cur.execute(sql)

# cur在执行查询之后 可以通过迭代获取结果
for row in cur:
    print(row)

# # 获取一条记录
# one = cur.fetchone()
# print(one)
#
# # 获取多条记录
# many = cur.fetchmany(2)
# print(many)
#
# # 获取所有条记录
# all = cur.fetchall()
# print(all)

# 关闭游标和数据库连接
cur.close()
db.close()