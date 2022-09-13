# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-07
    FileName   : minCostClimbingStairs.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre_first = cost[0]
        pre_second = cost[1]
        for i in range(2, len(cost)):
            cur = min(pre_second, pre_first)+cost[i]
            pre_first = pre_second
            pre_second = cur
        return min(pre_first,pre_second)


