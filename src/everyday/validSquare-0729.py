# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-29
    FileName   : validSquare-0729.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from math import pow

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dis1 = pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2)
        dis1_1 = pow(p3[0]-p4[0],2)+pow(p3[1]-p4[1],2)
        dis2 = pow(p1[0] - p3[0], 2) + pow(p1[1] - p3[1], 2)
        dis2_1 = pow(p2[0] - p4[0], 2) + pow(p2[1] - p4[1], 2)
        dis3 = pow(p1[0] - p4[0], 2) + pow(p1[1] - p4[1], 2)
        dis3_1 = pow(p2[0] - p3[0], 2) + pow(p2[1] - p3[1], 2)
        if dis1>0 and dis2>0 and dis3>0 and dis1==dis1_1 and dis2==dis2_1 and dis3==dis3_1:
            max_length = max(dis1,dis2,dis3)
            min_length = min(dis1,dis2,dis3)
            return max_length==2*min_length
        return False

if __name__ == '__main__':
    sol =Solution()
    p1 = [0,0]
    p2 = [5,0]
    p3 = [5,4]
    p4 = [0,4]
    print(sol.validSquare(p1,p2,p3,p4))



