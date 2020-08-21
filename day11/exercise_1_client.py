"""
查单词客户端

"""
from socket import *

# 服务端地址写好
address = ("127.0.0.1",8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送
while True:
    # 输入什么发送什么
    word = input("Word:")
    if not word:
        # msg为空字符串则退出循环
        break
    udp_socket.sendto(word.encode(),address)
    data,addr = udp_socket.recvfrom(1024)
    print(word,":",data.decode())

# 关闭套接字
udp_socket.close()




