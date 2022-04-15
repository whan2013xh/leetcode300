# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-14
    FileName   : numIslands.py
    Author     : Honghe
    Descreption: 200. 岛屿数量
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        visited = [[0]*col for _ in range(row)]
        num = 0

        for i in range(row):
            for j in range(col):
                if visited[i][j]!=0:
                    continue
                if grid[i][j]=='0':
                    visited[i][j] = -1
                else:
                    num+=1
                    visited[i][j] = num
                    self.dfs(grid,visited,num,i,j)
        return num



    def dfs(self,grid,visited,num,x,y):
        row = len(grid)
        col = len(grid[0])
        if not (0<=x<row and 0<=y<col):
            return
        for dp_i,dp_j in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
            if 0<=dp_i<row and 0<=dp_j<col:
                if visited[dp_i][dp_j]!=0:
                    continue
                if grid[dp_i][dp_j]=='0':
                    visited[dp_i][dp_j] = -1
                else:
                    visited[dp_i][dp_j] = num
                    self.dfs(grid,visited,num,dp_i,dp_j)
        return

if __name__ == '__main__':
    sol = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]


]
    print(sol.numIslands(grid))

