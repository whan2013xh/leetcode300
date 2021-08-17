# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-17
    FileName   : missingNumber.py
    Author     : Honghe
    Descreption: 268. 丢失的数字
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        求和法：这个数组里没有重复的元素所以，对0~n求和，再减去这个数组的和就死重复的数
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(range(len(nums)+1)))-sum(nums)

if __name__ == '__main__':
    nums = [3,0,1]
    sol = Solution()
    res =sol.missingNumber(nums)
    print(res)