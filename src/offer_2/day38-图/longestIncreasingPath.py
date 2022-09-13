# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-19
    FileName   : longestIncreasingPath.py
    Author     : Honghe
    Descreption:  329 题相同： https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/
"""
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = 1
        dp = [[-1]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                res = max(res,self.dfs(matrix,i,j,dp))
        return res

    def dfs(self, matrix,x,y,dp):
        """
        深度优先遍历
        :param matrix:
        :param x:
        :param y:
        :param dp:
        :return:
        """
        row = len(matrix)
        col = len(matrix[0])
        if dp[x][y]!=-1:
            return dp[x][y]
        res = 1
        for i,j in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
            if 0<=i<row and 0<=j<col and matrix[i][j]>matrix[x][y]:
                res = max(res,self.dfs(matrix,i,j,dp)+1)
        dp[x][y] = res
        return res

if __name__ == '__main__':
    sol = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(sol.longestIncreasingPath(matrix))
