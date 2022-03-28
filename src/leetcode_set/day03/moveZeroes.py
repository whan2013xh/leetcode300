# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-11
    FileName   : moveZeroes.py
    Author     : Honghe
    Descreption: 283. 移动零
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = -1
        for i in range(len(nums)):
            if nums[i]==0 and pos==-1:
                pos = i
            elif nums[i]!=0 and pos>-1:
                nums[pos] = nums[i]
                nums[i] = 0
                pos+=1



if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 0, 4, 5, 6, 7]

    res = sol.moveZeroes(nums)
    print(nums)