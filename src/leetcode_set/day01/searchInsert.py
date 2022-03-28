# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-09
    FileName   : searchInsert.py
    Author     : Honghe
    Descreption: 35. 搜索插入位置
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left<right:
            middle = (right-left)//2+left
            if nums[middle]>target:
                right = middle
            elif nums[middle]<target:
                left = middle+1
            else:
                return middle
        return left

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    sol = Solution()
    res = sol.searchInsert(nums, target)
    print(res)