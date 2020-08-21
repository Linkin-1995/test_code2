"""
tcp 服务端流程基础示例
"""

from socket import *

# 创建tcp套接字 其实使用默认值就是tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听,让tcp套接字可以被链接
tcp_socket.listen(5)

# 处理客户端连接
print("等待客户端连接....")
connfd,addr = tcp_socket.accept()
print("连接:",addr) # 客户端地址

# 先接收后发送
data = connfd.recv(1024)
print("接收到:",data.decode())

connfd.send(b"Thanks")

# 关闭
connfd.close()
tcp_socket.close()




