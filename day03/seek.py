"""
文件偏移量现象示例
"""

f = open("test.txt",'wb+')

# 文件偏移量已经到了文件结尾
f.write(b"hello world")
f.flush()

print("偏移量:",f.tell())

# 以结尾为基准向前移动3个字节
f.seek(-3,2)
f.write(b"xx")

# 从文件偏移量标记位置开始
data = f.read()
print(data)

f.close()
