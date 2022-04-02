# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-31
    FileName   : maxValue.py
    Author     : Honghe
    Descreption: 剑指 Offer 47. 礼物的最大价值
"""

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(row+1):
            for j in range(col+1):
                if i==0 or j==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=grid[i-1][j-1]+max(dp[i-1][j],dp[i][j-1])
        return dp[row][col]

if __name__ == '__main__':
    sol = Solution()
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    print(sol.maxValue(grid))