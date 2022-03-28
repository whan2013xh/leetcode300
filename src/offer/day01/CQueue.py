# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-15
    FileName   : CQueue.py
    Author     : Honghe
    Descreption: 剑指 Offer 09. 用两个栈实现队列
"""

class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack1.append(value)



    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2.pop()
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        else:
            return -1
        return self.stack2.pop()
