"""
进程对象属性演示
"""

from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

# 创建进程
p = Process(target=fun,name="Tarena")

# 子进程随父进程而结束 start前
p.daemon = True

p.start() # 启动进程

print("Name:",p.name)
print("PID:",p.pid)
print("is alive:",p.is_alive())
time.sleep(1)