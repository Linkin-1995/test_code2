from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)

def main(filename):
    # 默认值就是创建tcp套接字
    tcp_socket = socket()

    # 发起链接 对应 accept
    tcp_socket.connect(ADDR)

    file = open(filename,'rb')

    # 边读取边发送
    while True:
        data = file.read(1024)
        # 读到文件结尾为空
        if not data:
            break
        tcp_socket.send(data)
    # 关闭
    file.close()
    tcp_socket.close()

if __name__ == '__main__':
    main("./timg.jfif")