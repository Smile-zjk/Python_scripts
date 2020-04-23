# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:29:59 2020

@author: 24592
"""
class Node:   
    def __init__(self, val):
        self.val = val
        self.next = None
        
    
class Singlelink:
    def __init__(self, node=None):
        self.__head = node

    def __len__(self):  
        count = 0
        cur = self.__head
        while cur is not None:
            cur = cur.next
            count += 1
        return count   
     
    def get_head(self):
        return self.__head
    
    def head_add(self, val):    # 头插法
        node = Node(val)
        node.next = self.__head
        self.__head = node
        
    def tail_add(self, val=None):   # 尾插法
        if self.__head == None:
            self.head_add(val)
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            node = Node(val)
            cur.next = node
        
    def traverse(self):     # 遍历
        cur = self.__head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next

            
alink = Singlelink()
blink = Singlelink()
a = [1, 3, 5]
b = [1, 2, 6, 8]
for i in a:
    alink.tail_add(i)
for i in b:
    blink.tail_add(i)
alink.traverse()
blink.traverse()

    
        