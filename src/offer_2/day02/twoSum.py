# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-07
    FileName   : twoSum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 006. 排序数组中两个数字之和
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left,right]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return
