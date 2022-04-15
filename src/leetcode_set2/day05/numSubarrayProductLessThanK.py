# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-13
    FileName   : numSubarrayProductLessThanK.py
    Author     : Honghe
    Descreption: 713. 乘积小于K的子数组
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=0:
            return 0
        left = 0
        res = 0
        tmp = 1
        for right,num in enumerate(nums):
            tmp*=num
            while tmp>=k and left<=right:
                tmp/=nums[left]
                left+=1
            if tmp<k:
                res += right-left+1
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [10,5,2,6]
    k=100
    print(sol.numSubarrayProductLessThanK(nums,k))







