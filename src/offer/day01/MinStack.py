# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-15
    FileName   : MinStack.py
    Author     : Honghe
    Descreption: 剑指 Offer 30. 包含min函数的栈
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_value = []
        self.value = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.value.append(x)
        # 这个要理解，min_value只用保存非升序的元素即可
        if not self.min_value or x<=self.min_value[-1]:
            self.min_value.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.value.pop()==self.min_value[-1]:
            self.min_value.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.value[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.min_value[-1]




