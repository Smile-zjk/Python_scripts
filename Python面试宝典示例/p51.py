# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:53:19 2020

@author: 24592
"""
import time

prime_array = [2, 3]

def isPrime2(k):
    if k <= 3:
        return True
    for _, v in enumerate(prime_array):
        if k > v and k % v == 0:
            return False
    # 如果k是素数，将k加入素数数组
    prime_array.append(k)
    return True


def getPrimes2(n):
    primes = [i for i in range(1, n+1) if isPrime2(i)]
    return primes

start  = time.time()
primes = getPrimes2(10000)
print(primes)
end = time.time()
print('time is {}'.format(end - start))
# time is 0.09670805931091309