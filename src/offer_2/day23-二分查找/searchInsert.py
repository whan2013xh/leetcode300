# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-30
    FileName   : searchInsert.py
    Author     : Honghe
    Descreption: 剑指 Offer II 068. 查找插入位置
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (right-left)//2+left
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return left

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 0
    print(sol.searchInsert(nums,target))
