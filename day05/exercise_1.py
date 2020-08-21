"""
1. 编写一个程序,输入一个接口名称,得到
    该接口运行状况描述中的address 地址
    address is 10f3.114b.978e

    文件特点 : 1. 每段之间有一个空行
              2.每段是一个接口运行状态说明
                其中第一个单词是接口名称

    提示: 根据输入的端口名称确定段落
          在对应段落中进行目标获取
"""
import re

# 生成器,每次提供一个段落
def get_info():
    # 获取段落
    f = open('log.txt') # 读方式

    while True:
        # 每次while循环找到一段
        data = ""
        for line in f:
            if line == '\n':
                # 说明是空行,一段结束
                break
            data += line

        # 如果一段文字都是空则说明没有内容了
        if not data:
            f.close()
            return # 结束生成器

        # data就是一段内容,判断是否为我们要的那一段
        yield data

def get_address():
    # 输入接口名称
    name = input("接口名称:")
    # 调用生成器 每次获取一段内容
    for info in get_info():
        # 提取一段的首单词
        obj = re.match(r"\S+",info)
        # 判断是否是想要的
        if name == obj.group():
            # 开始匹配地址
            pattern = r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            result = re.search(pattern,info)
            if result:
                print(result.group())
            else:
                print("Unknown")
            return
    print("没有该接口!")

get_address()

