"""
练习: 从客户端传递一张图片给服务端,在服务端
以当前日期为名字保存起来

    思路:  客户端  将文件内容读取出来发送
           服务端  接收文件内容,写入本地

    要求 : 文件可能很大,不允许一次性读取
           循环读取发送
"""

from socket import *
import time

# 获取图片函数 边接收边写入
def get_image(connfd):
    filename = "%s-%s-%s.jpg"%time.localtime()[:3]
    file = open(filename,'wb')
    # 边接收边写入
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        file.write(data) # 直接写入字节串
    file.close()

def main():
    # 创建tcp套接字 其实使用默认值就是tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定地址
    tcp_socket.bind(("0.0.0.0",8888))
    # 设置监听,让tcp套接字可以被链接
    tcp_socket.listen(5)

    # 处理客户端连接
    while True:
        print("等待客户端连接....")
        connfd,addr = tcp_socket.accept()
        print("连接:",addr) # 客户端地址

        # 接受图片
        get_image(connfd)

        connfd.close() # 客户端退出链接套接字就没用了

    # 关闭
    tcp_socket.close()

if __name__ == '__main__':
    main()


