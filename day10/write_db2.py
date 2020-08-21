"""
写数据库演示 2
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

# 执行多次sql语句 多用于写语句
try:
    sql = "update cls set score=score+1 " \
          "where id=%s;"
    cur.executemany(sql,[(1,),(2,),(3,)])

    # for i in [(1,),(2,),(3,)]:
    #     cur.execute(sql,i)

    db.commit()
except:
    db.rollback()



# 关闭游标和数据库连接
cur.close()
db.close()









