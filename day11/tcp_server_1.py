"""
tcp 服务端循环流程 1

特点 : 每次只处理一个客户端事务,处理完一个
客户端再处理下一个

重点代码!!!
"""

from socket import *

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

    # 先接收后发送 为客户端服务
    while True:
        data = connfd.recv(5)
        # 退出方案2 如果data是空字节串意味着客户端退出
        if not data:
            break

        # 循环退出方案1  收到quit意味着客户端退出了
        # if data == b"quit":
        #     break
        print("接收到:",data.decode())
        connfd.send(b"Thanks#")

    connfd.close() # 客户端退出链接套接字就没用了

# 关闭
tcp_socket.close()




