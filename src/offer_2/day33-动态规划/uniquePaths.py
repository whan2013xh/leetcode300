# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-12
    FileName   : uniquePaths.py
    Author     : Honghe
    Descreption: 
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    m=3
    n=7
    print(sol.uniquePaths(m,n))
