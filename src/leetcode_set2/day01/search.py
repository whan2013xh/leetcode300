# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-06
    FileName   : search.py
    Author     : Honghe
    Descreption: 33. 搜索旋转排序数组
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
            if nums[middle]==target:
                return middle
            if nums[0]>nums[middle]:
                if nums[middle]<target<nums[0]:
                    left = middle + 1
                else:
                    right = middle-1
            elif nums[0]<=nums[middle]:
                if nums[middle]>target>=nums[0]:
                    right = middle-1
                else:
                    left = middle+1
        return -1

if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    target = 0
    print(sol.search(nums,target))