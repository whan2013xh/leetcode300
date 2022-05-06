# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-21
    FileName   : canJump.py
    Author     : Honghe
    Descreption: 55. 跳跃游戏
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        dp = [0]*len(nums)
        flag=0
        for index,num in enumerate(nums[:-1]):
            if flag<index:
                return False
            dp[index] = index + num
            flag = max(dp[index], flag)
            if dp[index]>=len(nums)-1:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,8,2,0,0,1]
    print(sol.canJump(nums))


