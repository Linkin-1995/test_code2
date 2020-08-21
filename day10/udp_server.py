"""
udp 服务端程序基础示例
重点代码 !!!
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))

print("等到花都谢了...")

while True:
    # 服务端先收  阻塞函数
    data,addr = udp_socket.recvfrom(1024)
    print(addr,"收到消息:",data.decode())

    # 发送消息  发送字节串
    n = udp_socket.sendto(b"Thanks",addr)
    print("发送了%d bytes"%n)

# 关闭套接字
udp_socket.close()









