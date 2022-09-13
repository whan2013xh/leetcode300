# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-07
    FileName   : rob2.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        return max(self.trace(nums,0,len(nums)-2),self.trace(nums,1,len(nums)-1))


    def trace(self,nums,start,end):
        first = nums[start]
        second = max(nums[start],nums[start+1])
        for i in range(start+2,end+1):
            first,second = second,max(first+nums[i],second)
        return second

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,1,3,100]
    print(sol.rob(nums))
