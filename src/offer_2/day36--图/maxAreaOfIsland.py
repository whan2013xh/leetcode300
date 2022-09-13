# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-14
    FileName   : maxAreaOfIsland.py
    Author     : Honghe
    Descreption: 本题与主站 695 题相同： https://leetcode.cn/problems/max-area-of-island/
"""
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if visited[i][j] or grid[i][j]==0:
                    continue
                if grid[i][j]==1:
                    visited[i][j]=True
                    tmp = self.dfs(grid,i,j,visited)
                    res = max(res,tmp)
        return res

    def dfs(self,grid,x,y,visited):
        row = len(grid)
        col = len(grid[0])
        res = 1
        for tmp_x,tmp_y in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
            if 0<=tmp_x<row and 0<=tmp_y<col and grid[tmp_x][tmp_y]==1 and not visited[tmp_x][tmp_y]:
                visited[tmp_x][tmp_y] = True
                res = res+ self.dfs(grid,tmp_x,tmp_y,visited)
        return res

if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(sol.maxAreaOfIsland(grid))