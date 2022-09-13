# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-07
    FileName   : minCost.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        row = len(costs)
        col = len(costs[0])
        if row==1:
            return min(costs[0])

        dp = [[float("inf")]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i==0:
                    dp[i][j]=costs[i][j]
                else:
                    left = dp[i-1][:j] if col>j>0 else []
                    right = dp[i-1][j+1:] if j<col-1 else []
                    dp[i][j] = min(left+right)+costs[i][j]

        return min(dp[-1][:])


if __name__ == '__main__':
    costs = [[17, 2, 17], [16, 5, 16], [14, 3, 19]]
    sol = Solution()
    print(sol.minCost(costs))