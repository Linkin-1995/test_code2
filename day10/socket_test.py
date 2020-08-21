"""
创建套接字示例
"""

import socket

# 创建UDP套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

# 绑定测试地址,用于本地客户端访问测试
# udp_socket.bind(("127.0.0.1",8888))

# 万能地址,本地客户端可以通过127或者网络IP访问
# 其他网络计算机通过ip访问
# udp_socket.bind(("0.0.0.0",8888))

# 自己的网络ip地址,用于其他网络计算机通过ip访问
udp_socket.bind(("172.40.91.202",8888))