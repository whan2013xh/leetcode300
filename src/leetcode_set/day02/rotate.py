# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-10
    FileName   : rotate.py
    Author     : Honghe
    Descreption: 189. 轮转数组
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return nums[len(nums)-k:]+nums[:len(nums)-k]

    def rotate2(self, nums, k):
        """
        翻转数组
        :param nums:
        :param k:
        :return:
        """
        k = k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        return nums

    def reverse(self, nums, start, stop):
        while start<stop:
            tmp = nums[start]
            nums[start] = nums[stop]
            nums[stop] = tmp
            start += 1
            stop-=1



if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    res = sol.rotate2(nums,k)
    print(res)