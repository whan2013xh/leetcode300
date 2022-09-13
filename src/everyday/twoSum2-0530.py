# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-30
    FileName   : twoSum2-0530.py
    Author     : Honghe
    Descreption: 167. 两数之和 II - 输入有序数组
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        双指针
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                return [left+1, right+1]

