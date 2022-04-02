# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : twoSum.py
    Author     : Honghe
    Descreption: 剑指 Offer 57. 和为s的两个数字
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = set(nums)
        for i in nums:
            if i>target:
                return []
            if target-i in count:
                return [i,target-i]
        return []

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                return [nums[left],nums[right]]
        return []