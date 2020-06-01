# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:01:44 2020

@author: 24592
"""
class Rectangele(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
    
    def isInterset(self, r):
        if max(self.x, r.x) <= min(self.x+self.w, r.x+r.w) and max(self.y, r.y) <= min(self.y+self.h, r.x+r.h):
            return True
        return False
    
    def intersetRectangle(self, r):
        if self.isInterset(r):
            return Rectangele(max(self.x, r.x), max(self.y, r.y), min(r.x+r.w, self.x+self.w)-max(r.x, self.x), min(r.y+r.h,self.y+self.h)-max(r.y,self.y))
        return None

import matplotlib.pyplot as plt
import matplotlib.patches as patches

S = Rectangele(0.1, 0.1, 0.5, 0.5)
R = Rectangele(0.2, 0.2, 0.6, 0.5)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
# 用红色绘制S表示的矩形
ax.add_patch(patches.Rectangle((S.x, S.y), S.w, S.h, facecolor='red'))
# 用蓝色绘制R表示的矩形
ax.add_patch(patches.Rectangle((R.x, R.y), R.w, R.h, facecolor='blue'))

if S.isInterset(R):
    interset = S.intersetRectangle(R)
    print("x:{0}, y:{1}, w:{2}, h{3}".format(interset.x, interset.y, interset.w, interset.h))
    ax.add_patch(patches.Rectangle((interset.x, interset.y), interset.w,interset.h, facecolor='green'))
    fig.savefig('rectangle1.png', dpi=90, bbox_inches='tight')
    plt.show('rectangle1.png')


