"""
正则表达式 函数示例 2
"""
import re

# 目标字符串
s = """
    Alex:2000 
   Sunny:1999  
   Tom:1998
"""
pattern = r"(\w+):(?P<age>\d+)"

# 返回值是一个迭代对象
# result = re.finditer(pattern,s)
#
# # 迭代取出每处匹配内容对应的match对象
# for i in result:
#     print(i.group()) # 获取对应的匹配内容

# 只匹配开始位置
# obj = re.match(pattern,s)
# print(obj.group())

# 只匹配一处
obj = re.search(pattern,s)
print(obj.group())
print(obj.group(1)) # 组序号
print(obj.group("age")) # 组名字

#(5, 14) s[5:14] 就是匹配到的内容
print(obj.span())

# {'age': '2000'} 捕获组字典
print(obj.groupdict())




