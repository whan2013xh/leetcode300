# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-21
    FileName   : rob.py
    Author     : Honghe
    Descreption: 213. 打家劫舍 II
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp2=[0]*len(nums)
        pre_flag = False
        cur_flag = False
        for index,num in enumerate(nums):
            if index==0:
                dp[index]=num
                dp2[index]=0
                pre_flag=True
            elif index==1:
                cur_flag = num<dp[index-1]
                dp[index] = max(dp[index-1],num)
                dp2[index]=num
            elif index==len(nums)-1:
                tmp = dp[index-2]+num if not pre_flag else max(dp[index-2]+max(0,num-nums[0]),dp2[index-2]+num)
                dp[index] = max(dp[index - 1], tmp)
            else:
                tmp_flag = cur_flag
                cur_flag = cur_flag if dp[index-1]>=(dp[index-2]+num) else pre_flag
                dp[index] = max(dp[index-1],dp[index-2]+num)
                dp2[index] = max(dp2[index-1],dp2[index-2]+num)
                pre_flag = tmp_flag

        return dp[-1]

    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

if __name__ == '__main__':
    sol = Solution()
    nums = [200,3,140,20,10]
    print(sol.rob(nums))
