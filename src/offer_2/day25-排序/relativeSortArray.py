# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-04
    FileName   : relativeSortArray.py
    Author     : Honghe
    Descreption: 剑指 Offer II 075. 数组相对排序
"""
from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_nums = dict(Counter(arr1))
        res = []
        for num in arr2:
            counts = arr1_nums.get(num)
            res+=[num]*counts
            arr1_nums.pop(num)

        arr_nums = sorted(arr1_nums.items(),key=lambda x:x[0])

        for key,item in arr_nums:
            res+=[key]*item
        return res

if __name__ == '__main__':
    sol = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(sol.relativeSortArray(arr1,arr2))



