# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-23
    FileName   : moveZeroes.py
    Author     : Honghe
    Descreption: 283. 移动零
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        直接遍历法
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        no_zero = 0
        for index, i in enumerate(nums):
            if i!=0:
                nums[no_zero] = i
                no_zero +=1
        for j in range(no_zero, len(nums)):
            nums[j]=0
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,0,3,12]
    res =sol.moveZeroes(nums)
    print(res)