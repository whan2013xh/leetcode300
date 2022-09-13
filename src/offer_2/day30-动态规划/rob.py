# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-07
    FileName   : rob.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)

        first = nums[0]
        second = nums[1]
        third = nums[0]+nums[2]
        for i in range(3,len(nums)):
            cur = max(first,second)+nums[i]
            first = second
            second = third
            third = cur

        return max(second,third)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.rob(nums))

