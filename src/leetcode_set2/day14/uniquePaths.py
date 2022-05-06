# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-22
    FileName   : uniquePaths.py
    Author     : Honghe
    Descreption: 
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = []
        self.res = 0
        self.dfs(m,n,0,0,visited)
        return self.res


    def dfs(self,m,n,x,y,visited):
        if x==m-1 and y==n-1:
            self.res+=1
            return
        for i,j in [(x+1,y),(x,y+1)]:
            if 0<=i<m and 0<=j<n and (i,j) not in visited:
                visited.append((i,j))
                self.dfs(m,n,i,j,visited)
                visited.pop()

    def uniquePaths2(self, m, n):
        dp = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    m=3
    n = 3
    print(sol.uniquePaths2(m,n))