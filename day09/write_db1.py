"""
数据库的写操作
注意 : 如果数据表支持事务则使用commit rollback
提交或回滚.
       如果不支持事务择直接生效
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

# 写数据库 insert  update  delete
try:
    # 可以多次执行sql一次commit
    sql = "update cls set score=%s where id=%s;"
    cur.execute(sql,[91,1])
    sql = "delete from cls where score<60;"
    cur.execute(sql)

    # 提交写操作语句结果
    db.commit()
except Exception as e:
    print(e)
    db.rollback() # 回滚 所有操作失效




# 关闭游标和数据库连接
cur.close()
db.close()