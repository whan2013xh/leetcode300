# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-23
    FileName   : search.py
    Author     : Honghe
    Descreption: 剑指 Offer 53 - I. 在排序数组中查找数字 I
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<=right:
            middle = (right-left)//2+left
            if nums[middle]<target:
                left = middle+1
            elif nums[middle]>target:
                right = middle-1
            else:
                left = middle
                right = middle
                while left>=0 and nums[left]==target:
                    left -=1
                while right<len(nums) and nums[right]==target:
                    right +=1
                return right - left - 1
        return 0


if __name__ == '__main__':
    sol = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(sol.search(nums,target))

