# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-04
    FileName   : minEatingSpeed.py
    Author     : Honghe
    Descreption: 875. 爱吃香蕉的珂珂
"""
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = 1
        res = 1
        while min_speed<=max_speed:
            mid = (max_speed+min_speed)>>1
            tmp = self.cost(piles,mid)
            if tmp<=h:
                res = mid
                max_speed = mid-1
            else:
                min_speed = mid+1
        return res

    def cost(self, piles, speed):
        res = 0
        for pile in piles:
            res += math.ceil(pile/speed)
        return res


if __name__ == '__main__':
    sol = Solution()
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(sol.minEatingSpeed(piles,h))