"""
进程创建示例 1

【1】 将需要新进程执行的任务封装为函数
【2】 通过模块的Process类创建进程对象，关联函数
【3】 通过进程对象调用start启动进程
【4】 通过进程对象调用join回收进程资源
"""

import multiprocessing
import time

a = 1

# 进程执行函数
def fun():
    print("开始运行一个进程")
    global a
    print("a = ",a)
    a = 10000
    time.sleep(2) # 模拟,假装这个事很大执行2s
    print("这个进程结束了")



# 实例化进程对象
p = multiprocessing.Process(target=fun)

# 启动进程:进程诞生,自动执行fun函数作为进程执行内容
p.start()

# 让它与子进程同时执行
print("我也想做点事")
time.sleep(3)
print("我也做完了哦...")

# 等待进程结束,回收进程
p.join()

print("a:",a) # 1





