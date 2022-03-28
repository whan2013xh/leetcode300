# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-23
    FileName   : findRepeatNumber.py
    Author     : Honghe
    Descreption: 剑指 Offer 03. 数组中重复的数字
"""

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                return i
