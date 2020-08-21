"""
os 模块处理文件示例
"""
import os

# 获取文件大小  单位: 字节
print("文件大小:",os.path.getsize("../day03/3.txt"))

# 获取文件夹下所有文件名称
print(os.listdir("../day03"))

# 查看一个文件是否存在  bool
print(os.path.exists("4.txt"))

# 查看一个文件是否为普通文件 -  d
print(os.path.isfile("4.txt"))

# 删除一个文件
# os.remove("../day03/test.txt")

