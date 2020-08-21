"""
线程创建示例
1. 线程多任务同执行,互不影响,各自执行
2. 线程属于进程
3. 线程共用进程资源
"""
import threading
from time import sleep
import os

a = 1

# 线程执行函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:黄河大合唱")
    global  a
    print("a = ",a)
    a = 10000

# 生成线程对象
t = threading.Thread(target=music)

# 启动线程 线程才真正存在
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放:葫芦娃")

# 回收线程
t.join()

print("a:",a) # ?


