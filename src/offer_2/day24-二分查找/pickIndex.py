# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-01
    FileName   : pickIndex.py
    Author     : Honghe
    Descreption: 剑指 Offer II 071. 按权重生成随机数
"""
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [sum(w[:i+1]) for i in range(len(w))]
        self.total = sum(w)


    def pickIndex(self) -> int:
        num = random.randint(1,self.total)
        left = 0
        right = len(self.prefix_sum)-1
        while left<right:
            mid = (right-left)//2+left
            if num==self.prefix_sum[mid]:
                return mid
            elif num>self.prefix_sum[mid]:
                left = mid+1
            else:
                right = mid
        return right

if __name__ == '__main__':
    weight = [1,2,3,4]
    sol = Solution(weight)
    print(sol.pickIndex())



