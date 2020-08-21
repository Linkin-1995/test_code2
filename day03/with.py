"""
with 打开文件
"""

with open('test.txt',"r+") as f:
    # f只能在with语句块中使用
    data = f.read()
    print(data)

# with结束后f会自动消息