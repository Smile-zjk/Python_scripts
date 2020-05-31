# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:36:51 2020

@author: 24592
"""
# 求a除以b后所得余数
def module(a, b):
    T = []
    t = 0
    # 先求T[n-1]
    while (b<<t) <= a:
        t += 1
    t -= 1
    T.append(t)
    # 下面代码求取T[n-2], t[n-3]...T[0]
    a_prime = a - (b << T[len(T)-1])
    while a_prime >= b:
        while (b<<t) > a_prime:
            t -= 1
        T.append(t)
        a_prime = a_prime - (b << T[len(T)-1])
    '''
    k = 2<<T[n-1] + 2<<T[n-2] + ... + 2<<T[0]
    a = k * b + d
    所以 d = a - k * b = a - (b<<T[n-1] + b<<T[n-2] + ... + b<<T[0])
    '''
# 书上写法如下，但觉得没有必要，因为a_prime已经是余数了，没必要在计算一次
#    d = a
#    for i in range(0, len(T)):
#        d -= (b<<T[i])
#    
#    # d 就是两数相除余数
#    return d
    return a_prime

def binaryGcd(a, b):
    # 如果a能整除b，那么b就算两数的最大公约数
    if module(a, b) == 0:
        return b
    d = module(a, b)
    # a, b的最大公约数等于b, d的最大公约数 
    return binaryGcd(b, d)

a = 128
b = 48
print("the greatest common divisor of {0} and {1} is: {2}".format(a, b, binaryGcd(a, b)))
