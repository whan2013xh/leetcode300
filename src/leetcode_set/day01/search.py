# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-09
    FileName   : search.py
    Author     : Honghe
    Descreption: 704. 二分查找
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
        res = self.bin_search(nums,target,left,right)
        return res

    def bin_search(self, nums, target, left, right):
        if left>right:
            return -1
        if left==right:
            if nums[left]==target:
                return left
            else:
                return -1
        middle = (right-left)//2+left
        if nums[middle]>target:
            return self.bin_search(nums,target,left, middle)
        elif nums[middle]<target:
            return self.bin_search(nums, target, middle+1, right)
        else:
            return middle

    def bin_search2(self, nums, target):
        """
        非递归法
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums)
        while left<=right:
            middle = (right-left)//2+left
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    sol = Solution()
    res = sol.search(nums,target)
    print(res)