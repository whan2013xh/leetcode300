# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-15
    FileName   : RandomizedSet.py
    Author     : Honghe
    Descreption: 剑指 Offer II 030. 插入、删除和随机访问都是 O(1) 的容器
"""
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.values = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.values:
            return False
        self.values[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.values:
            return False
        index = self.values.get(val)
        self.nums[index] = self.nums[-1]
        self.values[self.nums[index]] = index
        self.nums.pop()
        del self.values[val]
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)
