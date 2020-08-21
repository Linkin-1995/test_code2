from socket import *
import time

#  服务端地址
ADDR = ("127.0.0.1",8889)

def main(filename):
    # 默认值就是创建tcp套接字
    tcp_socket = socket()

    # 发起链接 对应 accept
    tcp_socket.connect(ADDR)

    file = open(filename,'rb')

    # 边读取边发送
    while True:
        data = file.read(1024)
        # 读到文件结尾为空 发送## 表示发送结束
        if not data:
            time.sleep(0.1) # 防止##粘包
            tcp_socket.send(b'##')
            break
        tcp_socket.send(data)
    file.close()
    # 接收最后的消息
    msg = tcp_socket.recv(1024)
    print(msg.decode())

    # 关闭
    tcp_socket.close()

if __name__ == '__main__':
    main("./timg.jpg")