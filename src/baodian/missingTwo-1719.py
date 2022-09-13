# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-05
    FileName   : missingTwo-1719.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        length = len(nums)
        n = length+2
        two_sum = n*(n+1)//2-sum(nums)
        mid = two_sum//2
        sum_num = 0
        for i in nums:
            if i<=mid:
               sum_num+=i
        left = mid*(mid+1)//2-sum_num
        return [left,two_sum-left]

    def missingTwo2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        n = length+2
        xorsum = 0
        for i in range(1,n+1):
            xorsum^=i
        for i in nums:
            xorsum ^= i
        # 求出不一样的那个最低位的1
        low_bit = xorsum&(-xorsum)
        type1 = 0
        type2 = 0
        for j in nums:
            if j&low_bit:
                type1^=j
            else:
                type2^=j
        for i in range(1,n+1):
            if i&low_bit:
                type1^=i
            else:
                type2^=i
        return [type1,type2]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 4, 5, 6, 7, 8, 10]
    print(sol.missingTwo2(nums))
