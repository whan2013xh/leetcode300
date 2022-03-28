# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-23
    FileName   : missingNumber.py
    Author     : Honghe
    Descreption: 剑指 Offer 53 - II. 0～n-1中缺失的数字
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        return (n - 1) * n / 2 - sum(nums)