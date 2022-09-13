# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-12
    FileName   : minimumTotal.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        col = len(triangle[-1])
        dp = [[float("inf")]*col for _ in range(row)]

        for i in range(row):
            for j in range(i+1):
                if i==0 and j==0:
                    dp[i][j] = triangle[i][j]
                elif j==0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j==i:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(sol.minimumTotal(triangle))
