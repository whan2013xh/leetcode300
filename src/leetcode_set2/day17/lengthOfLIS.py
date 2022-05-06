# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-25
    FileName   : lengthOfLIS.py
    Author     : Honghe
    Descreption: 300. 最长递增子序列
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)


        return max(dp)

if __name__ == '__main__':
    sol =Solution()
    nums =[10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))
