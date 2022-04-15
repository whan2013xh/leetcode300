# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-15
    FileName   : shortestPathBinaryMatrix.py
    Author     : Honghe
    Descreption: 1091. 二进制矩阵中的最短路径
"""


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[0][0]==1 or grid[-1][-1]==1:
            return -1

        path = [(0,0)]
        self.res= float("inf")
        self.dfs(grid,0,0,path)
        return self.res if self.res!=float("inf") else -1

    def dfs(self,grid,x,y,path):
        row = len(grid)
        col = len(grid[0])
        if not (0<=x<row and 0<=y<col):
            return -1
        if row==1 and col==1:
            self.res = 1
            return

        for i,j in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
            if not (0 <= i < row and 0 <= j < col) or (i,j) in path:
                continue
            if grid[i][j]==0:
                if i==row-1 and j == col-1:
                    self.res = min(self.res,len(path)+1)
                if len(path)<self.res:
                    path.append((i,j))
                    self.dfs(grid,i,j,path)
                    path.remove((i,j))

        return -1

    def bfs(self,grid):
        """
        层次遍历，最短的最快到
        :param grid:
        :return:
        """
        if not grid or grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        row = len(grid)
        col = len(grid[0])
        if row==1 and col:
            return 1

        # visited = [(0,0)]
        queue = [(0,0)]
        grid[0][0]=1

        start = 1
        while queue:
            level = len(queue)
            for _ in range(level):
                x,y = queue.pop(0)
                for i,j in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                    if not (0 <= i < row and 0 <= j < col):
                        continue
                    if grid[i][j] == 0:
                        if i == row - 1 and j == col - 1:
                            return start+1
                        grid[i][j]=1
                        queue.append((i,j))

            start+=1
        return -1

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
    print(sol.bfs(grid))



