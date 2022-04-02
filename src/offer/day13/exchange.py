# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : exchange.py
    Author     : Honghe
    Descreption: 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
"""

class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left]%2==0:
                nums[right],nums[left]=nums[left],nums[right]
                right-=1
            else:
                left+=1
        return nums


if __name__ == '__main__':
    sol = Solution()
    nums=[1,2,3,4]
    print(sol.exchange(nums))