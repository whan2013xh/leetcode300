# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-06
    FileName   : searchRange.py
    Author     : Honghe
    Descreption: 34. 在排序数组中查找元素的第一个和最后一个位置
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        二分查找找左右边界
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        left = 0
        right = len(nums)-1
        left_pos = -1
        right_pos = -1
        while left<=right:
            middle = (right-left)//2+left
            if nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1
            else:
                tmp = middle
                while middle>=left:
                    if nums[middle]!=target:
                        left_pos = middle+1
                        break
                    middle-=1
                if middle<left:
                    left_pos = left
                middle = tmp
                while middle<=right:
                    if nums[middle]!=target:
                        right_pos = middle-1
                        break
                    middle+=1
                if middle>right:
                    right_pos = right
                break
        return [left_pos, right_pos]


    def searchRange2(self, nums, target):
        """
        二分查找找左右边界
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binary_search(nums, target)
        if left == len(nums) or nums[left]!=target:
            return [-1,-1]
        right = self.binary_search(nums, target+1)
        return [left, right-1]


    def binary_search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            middle = (right - left) // 2 + left
            if nums[middle]>=target:
                right = middle-1
            else:
                left = middle+1
        return left

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 8]
    target = 8
    print(sol.searchRange(nums,target))



