"""
vi 编写一个程序   求100000以内的质数之和
"""

# 判断一个数是否为质数
def isPrime(n):
    """
    :param n: 要判断的数
    :return: bool 表达结果
    """
    if n <= 1:
        return False 
    for i in range(2,n):
        if n % i == 0:
            return False 
    return True

def prime_sum():
    prime = []
    # 逐个判断每个数字是不是质数
    for i in range(1,100001):
        if isPrime(i):
            prime.append(i) # 所有质数加入列表
    print(sum(prime))

prime_sum()







