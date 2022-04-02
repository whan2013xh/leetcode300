# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-31
    FileName   : maxSubArray.py
    Author     : Honghe
    Descreption: 剑指 Offer 42. 连续子数组的最大和
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = float("-inf")
        start = 0
        end = 0
        tmp = 0
        for index, num in enumerate(nums):
            tmp = max(tmp+num,num)
            max_sub = max(max_sub,tmp)
        return max_sub

if __name__ == '__main__':
    sol = Solution()
    nums = [-5,-1,-2,-4,5]
    print(sol.maxSubArray(nums))