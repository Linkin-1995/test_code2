"""
练习: 模拟一个简单的对话机器人
多个客户端可以同时对话 ,在客户端输入问题发送给
小美(服务端),服务端会根据问题进行回复

 你多大啦  --> 2岁啦
 你是男生女生 --> 我是机器人
 你漂亮么 --> 我天生丽质
 xxxx --> 人家还小,还不懂
"""

from socket import *

# 对话字典
chat = {"几岁":"我两岁啦",
        "男生女生":"我是机器人",
        "叫什么":"我叫小美"
        }

def main():
    # 创建tcp套接字 其实使用默认值就是tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定地址
    tcp_socket.bind(("0.0.0.0",8888))
    # 设置监听,让tcp套接字可以被链接
    tcp_socket.listen(5)

    # 处理客户端连接
    while True:
        connfd,addr = tcp_socket.accept()
        data = connfd.recv(1024).decode()
        # 遍历字典--> 取键
        for key in chat:
            if key in data:
                connfd.send(chat[key].encode())
                break
        else:
            connfd.send("人家还小,听不懂".encode())

        connfd.close()
    # 关闭
    tcp_socket.close()

if __name__ == '__main__':
    main()


