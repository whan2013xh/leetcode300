# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-25
    FileName   : findNumberOfLIS.py
    Author     : Honghe
    Descreption: 673. 最长递增子序列的个数

"""
from collections import Counter

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        dp2 = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        dp2[i]=dp2[j]
                    elif dp[i]==dp[j] + 1:
                        dp2[i]+=dp2[j]
        max_path = max(dp)
        res=0
        for i in range(len(nums)):
            if dp[i] ==max_path:
                res+=dp2[i]
        return res




if __name__ == '__main__':
    sol =Solution()
    nums =[1,1,1,1,1,1]
    print(sol.findNumberOfLIS(nums))