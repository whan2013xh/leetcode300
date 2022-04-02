# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-02
    FileName   : rob.py
    Author     : Honghe
    Descreption: 198. 打家劫舍
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*(len(nums)+1)
        for index,i in enumerate(nums):
            if index<=1:
                dp[index+1]=max(dp[index],i)
            else:
                dp[index+1] = max(dp[index],i+dp[index-1])
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    nums = [2,7,9,3,1]
    print(sol.rob(nums))