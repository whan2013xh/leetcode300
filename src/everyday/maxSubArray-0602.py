# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-02
    FileName   : maxSubArray-0602.py
    Author     : Honghe
    Descreption: 53. 最大子数组和
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划
        :type nums: List[int]
        :rtype: int
        """
        max_res = float("-inf")
        res = float("-inf")
        for i in nums:
            max_res = max(max_res+i,i)
            res = max(res,max_res)
        return res


if __name__ == '__main__':
    sol =Solution()
    nums = [1]
    print(sol.maxSubArray(nums))
