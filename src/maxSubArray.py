# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-14
    FileName   : maxSubArray.py
    Author     : Honghe
    Descreption: 53. 最大子序和
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        暴力法：求出以i开始的序列的最大序列和，再求出最大的那个
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(nums)-1):
            tmp_sum = float('-inf')
            for j in range(i, len(nums)+1):
                tmp_sum = max(tmp_sum, sum(nums[i:j]))
            result.append(tmp_sum)
        return max(result)

    def maxSubArray2(self, nums):
        """
        动态规划：
        dp[i]表示以结尾的序列最大的和
        dp[i] = max(i, dp[i-1]+i)
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)

    def maxSubArray3(self, nums):
        """
        分治法：
        将序列二分，则最大子序列和就是左边序列最大序列和、右边序列最大序列和以及跨域
        最大子序列=max(left_array, right_array, mid_max)
        :type nums: List[int]
        :rtype: int
        """
        return self.get_max_num(nums, 0, len(nums)-1)

    def get_max_num(self, nums, left, right):
        if left==right:
            return nums[left]

        mid = (right-left)//2 + left
        left_max = self.get_max_num(nums, left, mid)
        right_max = self.get_max_num(nums, mid+1, right)
        mid_max = self.get_mid_max(nums, left, right, mid)
        return max(left_max, right_max, mid_max)

    def get_mid_max(self, nums, left, right, mid):
        if left == right:
            return nums[left]
        left_max_list = nums[mid]
        for i in range(mid-left):
            left_max_list = max(left_max_list, sum(nums[mid-i:mid+1]))
        right_max_list = nums[mid+1]
        for i in range(2, right-mid):
            right_max_list=max(right_max_list, sum(nums[mid+1:mid+i]))
        return max(left_max_list, right_max_list, left_max_list+right_max_list)




if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    res = sol.maxSubArray3(nums)
    print(res)