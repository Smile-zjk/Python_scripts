# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:12:28 2020

@author: 24592

把s表示的数字字符串转换成b进制数,这个程序是不完善的，没有检查边界条件以及错误参数。
"""

def strToInt(s: str, b: int):
    val = 0
    base = 1
    i = len(s) - 1
    while i >= 0:
        c = s[i]
        v = 0
        if '0' <= c and c <= '9':
            v = ord(c) - ord('0')
        if 'A' <= c and c <= 'E':
            v = 10 + ord(c) - ord('A')
        if i < len(s) - 1:
            base *= b
        val += v * base
        i -= 1
    return val

print(strToInt('1234', 10))
print(strToInt('1B', 13))

