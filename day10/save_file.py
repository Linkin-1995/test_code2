"""
存储文件
1. 将文件已二进制方式读取出来
2. 将该数据存储在 blob 类型字段中
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

# 存储文件
# f = open("timg.jfif",'rb')
# data = f.read() # 二进制字节串
# # 插入数据库
# try:
#     sql = "update cls set image=%s " \
#           "where name=%s;"
#     cur.execute(sql,[data,"Joy"])
#     db.commit()
# except:
#     db.rollback()

# 提取文件
f = open('pyy.jpg','wb')

sql = "select image from cls " \
      "where name='Joy';"
cur.execute(sql)
data = cur.fetchone()
f.write(data[0])

# 关闭游标和数据库连接
f.close()
cur.close()
db.close()