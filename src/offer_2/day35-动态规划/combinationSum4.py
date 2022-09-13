# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-13
    FileName   : combinationSum4.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(1+target)

        dp[0]=1
        for i in range(1,target+1):
            for num in nums:
                if i>=num:
                    dp[i]+=dp[i-num]
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    target = 4
    print(sol.combinationSum4(nums,target))
