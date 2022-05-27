# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-17
    FileName   : pivotIndex.py
    Author     : Honghe
    Descreption: 剑指 Offer II 012. 左右两边子数组的和相等
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        pre_sum = 0
        for i in range(len(nums)):
            if pre_sum * 2 + nums[i] == total:
                return i
            pre_sum += nums[i]
        return -1

if __name__ == '__main__':
    sol = Solution()
    nums = [-1,-1,-1,-1,-1,0]
    print(sol.pivotIndex(nums))


