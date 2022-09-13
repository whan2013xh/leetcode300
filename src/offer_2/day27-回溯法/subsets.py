# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-05
    FileName   : subsets.py
    Author     : Honghe
    Descreption: 剑指 Offer II 079. 所有子集
"""
from typing import List
import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            tmp = copy.deepcopy(res)
            for j in res:
                j.append(i)

            res+=tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))