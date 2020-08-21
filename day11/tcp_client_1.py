"""
tcp 客户端循环流程 1
重点代码 !!!
"""
from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)

# 默认值就是创建tcp套接字
tcp_socket = socket()

# 发起链接 对应 accept
tcp_socket.connect(ADDR)

# 发送接受消息
while True:
    msg = input(">>")
    # 循环退出方案2  不通知服务端
    if not msg:
        break
    tcp_socket.send(msg.encode())
    # 输入quit退出 循环退出方案1
    # if msg == 'quit':
    #     break
    data = tcp_socket.recv(1024)
    print("Server:",data.decode())

# 关闭
tcp_socket.close()
