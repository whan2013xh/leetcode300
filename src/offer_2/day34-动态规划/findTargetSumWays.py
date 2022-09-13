# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-12
    FileName   : findTargetSumWays.py
    Author     : Honghe
    Descreption: 本题与主站 494 题相同： https://leetcode-cn.com/problems/target-sum/
"""
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        暴力法，会超时
        :param nums:
        :param target:
        :return:
        """
        length = len(nums)
        dp = [0]
        num=0
        for i in range(1,length+1):
            res = []
            for j in dp:
                res.append(j+nums[i-1])
                res.append(j -nums[i - 1])
                if i==length :
                    if j+nums[i-1]==target:
                        num+=1
                    if  j -nums[i - 1]==target:
                        num+=1
            dp=res[:]
        return num

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
        动态规划：nums都是非负数，那么问题可以转换为找到nums中数组和为neg的序列
        :param nums:
        :param target:
        :return:
        """
        num_sum = sum(nums)
        neg = num_sum-target
        if neg%2!=0 or neg<0:
            return 0
        neg = neg//2
        dp = [[0]*(neg+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(neg+1):
                if i==0:
                    if j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=0
                else:
                    if nums[i-1]>j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i-1][j-nums[i-1]]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 0]
    target = 1
    print(sol.findTargetSumWays2(nums,target))



