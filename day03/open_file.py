"""
文件打开 演示示例
"""

# 打开一个文件
file = open("test.txt",'w') # 写 文件不存在创建
# file = open("test.txt",'r') # 读 默认
# file = open("test.txt",'a') # 追加写

# 对文件操作
print(file) # 打印文件对象

# 关闭文件对象
file.close()


