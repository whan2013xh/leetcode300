# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-07
    FileName   : findMin.py
    Author     : Honghe
    Descreption: 153. 寻找旋转排序数组中的最小值
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            middle = (right-left)//2+left
            if nums[right]>=nums[middle]:
                right = middle
            else:
                left = middle+1
        return nums[left]

if __name__ == '__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    print(sol.findMin(nums))