# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:17:41 2020

@author: 24592
"""

S = [10, 4, 8, 7, 9, 6, 2, 5, 3]

maxProfit = 0
buyDay = 0
sellDay = 0

for i in range(len(S) - 1):
    for j in range(i+1, len(S)):
        if S[j] - S[i] > maxProfit:
            maxProfit = S[j] - S[i]
            buyDay = i
            sellDay = j

print("应该在第{0}天买入，第{1}天卖出，最大交易利润为: {2}".format(buyDay+1, sellDay+1, maxProfit))