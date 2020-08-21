"""
正则表达式 函数示例 1
"""
import re

# 目标字符串
s = """
   Alex:2000 
   Sunny:1999  
   Tom:1998
"""
pattern = r"(\w+):(\d+)" # 正则表达式

# 如果正则表达式有子组
# 则findall只返回子组中所对应的匹配部分
# result = re.findall(pattern,s)
# print(result)

# 使用正则表达式分割目标字符串
# result = re.split(r"\W+",s,3)
# print(result)

# 使用xxxx 替换正则表达式匹配到的内容，返回新字符串
new = re.sub(r"\d+","xxxx",s,2)
print(new)










