"""
缓冲区演示
"""

# f = open("test.txt","w+")
# f = open("test.txt","w+",buffering=1) # 行缓冲

# 二进制打开可以指定缓冲区大小
f = open("test.txt","wb+",buffering=10)

while True:
    # 输入什么写入什么
    info = input(">>")
    f.write(info.encode())
    # f.flush() # 刷新缓冲