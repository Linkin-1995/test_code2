"""
练习1: 使用input输入一个目录位置,删除该
目录下所有大小小于1kb的普通文件
"""

import os

dir = input(">>") # 输入要处理的目录

# 逐个文件获取
for file in os.listdir(dir):
    # 注意拼接路径
    filename = dir+'/'+file
    # 判断大小和类型
    if os.path.getsize(filename) < 1024 and os.path.isfile(filename):
        os.remove(filename)



