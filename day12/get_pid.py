"""
进程相关小函数
"""
from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"---",os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),"---",os.getpid())

def th3():
    sys.exit("不打豆豆")
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"---",os.getpid())

# 循环一次创建一个进程
jobs = []
for th in [th1,th2,th3]:
    p = Process(target=th)
    jobs.append(p) # 存储进程对象
    p.start()

# 统一回收
for i in jobs:
    i.join()