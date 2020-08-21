"""
re模块功能扩展标志
"""
import re

s = """Hello world
北京 你好
"""
# ^ $ 表示每行的开头结尾位置
result = re.findall(r"\w+$",s,flags=re.M)
print(result)

# 忽略字母大小写
# result = re.findall(r"[a-z]+",s,flags=re.I)
# print(result)

# 让. 匹配换行符
# result = re.findall(r".+",s,flags=re.S)
# print(result)


# 让正则表达式只能匹配英文字符
# result = re.findall(r"\w+",s,flags=re.A)
# print(result)