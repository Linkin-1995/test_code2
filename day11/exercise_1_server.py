"""
使用udp套接字完成
从客户端输入单词,发送给服务端,从服务端得到
单词的解释 打印出来

要求: 客户端可以循环输入单词,直接回车退出
    服务端利用dict数据库进行单词查询

"""

from socket import *
import pymysql

class Database:
    def __init__(self):
        # 连接数据库 (连接本机可以不写host和port)
        self.db = pymysql.connect(user = "root",
                             password = "123456",
                             database = "dict",
                             charset = "utf8"
        )

        # 创建游标 (执行sql语句获取执行结果的对象)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def find_word(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        result = self.cur.fetchone() # (mean,) None
        # 分情况讨论
        if result:
            return result[0]
        else:
            return "Not Found"


# 启动服务
def main():
    # 创建udp套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    # 绑定地址
    udp_socket.bind(("0.0.0.0",8888))

    db = Database() # 数据库对象
    while True:
        # 接受单词
        word,addr = udp_socket.recvfrom(1024)

        #得到单词的解释
        mean = db.find_word(word)

        # 发送单词解释
        udp_socket.sendto(mean.encode(),addr)

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()