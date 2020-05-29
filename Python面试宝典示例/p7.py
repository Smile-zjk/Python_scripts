# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:02:29 2020

@author: 24592
"""

#S = [1, 2, 9, 4, 5, 6 , 7, 10]
S = [7, 10, 9, 4, 5, 6 , 1, 2]
minPrice = S[0]
N = 0
profit = 0
selDay = 0
buyDay = 0
day = 0

for N in range(len(S)):
    if (S[N] < minPrice):
        minPrice = S[N]
        day = N
    if (S[N] - minPrice > profit):
        profit = S[N] - minPrice
        buyDay = day
        selDay = N
        
print("应该在第{0}天买入，第{1}天卖出，最大交易利润为: {2}".format(buyDay+1, selDay+1, profit))