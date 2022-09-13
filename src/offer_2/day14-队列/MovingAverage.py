# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-21
    FileName   : MovingAverage.py
    Author     : Honghe
    Descreption: 剑指 Offer II 041. 滑动窗口的平均值
"""
from queue import Queue

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.windows = Queue(maxsize=size)
        self.total = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.windows.full():
            first_num = self.windows.get()
            self.total+=val-first_num
        else:
            self.total+=val
        self.windows.put(val)
        return self.total/self.windows.qsize()

if __name__ == '__main__':
    sol = MovingAverage(3)
    print(sol.next(1))
    print(sol.next(10))
    print(sol.next(3))
    print(sol.next(5))

