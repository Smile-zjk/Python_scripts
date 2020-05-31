# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:48:09 2020

@author: 24592
"""
import time 

def getPrimesInRange(n):
    primes = [True] * (n+1)
    primes[0] = False
            
    for i in range(2, n+1):
        if primes[i] == True:
            j = 2
            while i * j <= n:
                primes[i*j] = False
                j += 1
                
    return [i for i, v in enumerate(primes) if v]
        

n = 10000

start  = time.time()
primes = getPrimesInRange(n)
print(primes)
end = time.time()
print('time is {}'.format(end - start))
# time is 0.009974956512451172