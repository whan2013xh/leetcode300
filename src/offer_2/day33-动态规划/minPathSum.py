# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-12
    FileName   : minPathSum.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i-1][j])+grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(grid))


