"""
扩展: 空洞文件
"""

f = open('test.txt','wb')

f.write(b"begin")
f.seek(10000,2)
f.write(b'end')

f.close()