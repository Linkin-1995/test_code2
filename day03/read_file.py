"""
文件读取 演示示例
"""

# 打开文件
file = open("test.txt",'r')

# 读取file文件中的内容
# data = file.read()
# print(data)

# 循环读取文件内容
# while True:
#     data = file.read(10) # 一次读取10个字符
#     # 读取到文件结尾后还继续读,就会获取空字符串
#     if not data:
#         break
#     print(data,end="") # 打印完不换行

# readline 读取一行内容
# line = file.readline(3)
# print(line)
# line = file.readline(3)
# print(line)

# 读取文件内容,形成一个列表,列表每个元素是一行
# l = file.readlines(15)
# print(l)

# 迭代每次取一行
for line in file:
    print(line)


file.close()
