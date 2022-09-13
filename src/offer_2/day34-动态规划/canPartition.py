# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-12
    FileName   : canPartition.py
    Author     : Honghe
    Descreption:  416 https://leetcode-cn.com/problems/partition-equal-subset-sum/
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        total = total//2

        dp = [[False]*(1+total) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0,total+1):
                if nums[i] == j or j == 0:
                    dp[i][j] = True

                if i>0:
                    dp[i][j] = dp[i][j] | dp[i-1][j]
                    if nums[i]<j:
                        dp[i][j] = dp[i][j] |dp[i-1][j-nums[i]]
                if j==total and dp[i][j]:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    nums = [1,5,10,6]
    print(sol.canPartition(nums))

