"""
重点代码 !!

练习2:
使用input输入一个文件名字(/home/tarene/xxx),
将该文件复制到当前目录.

要求 : 1. 不确定文件的类型
       2. 不确定文件大小

思路 :  从源文件中读取出内容来,
       将这个内容写入到新的文件里
"""
# filename --> "/home/tarena/timg.jfif"
filename = input("要拷贝的文件:")

fr = open(filename,'rb') # 源文件打开

# 从输入的路径中提取文件名字 timg.jfif
new_file = filename.split('/')[-1]

fw = open(new_file,'wb') # 写打开

# 开始 一边读一边写
while True:
    data = fr.read(1024) # 读取源文件
    if not data:
        break
    fw.write(data) # 写入新文件

fr.close()
fw.close()



