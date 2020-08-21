"""
tcp 客户端循环流程 2
重点代码 !!!
"""
from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)


while True:
    msg = input(">>")
    if not msg:
        break

    # 默认值就是创建tcp套接字
    tcp_socket = socket()
    # 发起链接 对应 accept
    tcp_socket.connect(ADDR)

    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("Server:",data.decode())

    # 关闭
    tcp_socket.close()
