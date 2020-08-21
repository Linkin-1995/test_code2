"""
文件写操作示例
"""

# 打开文件
file = open("test.txt",'w')
# file = open("test.txt",'a') # 追加

# 写入内容
# n = file.write("天佑中华,龙魂不死")
# print("写入了%d个字符"%n)

# file.write(b"hello dead ghost\n")
# file.write("哎呀,干啥\n".encode())

# 将列表中的内容逐个写入 需要换行自己添加
l = ["呵呵\n","哈哈\n","嘿嘿\n"]
file.writelines(l)


file.close()