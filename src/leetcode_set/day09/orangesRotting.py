# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-16
    FileName   : orangesRotting.py
    Author     : Honghe
    Descreption: 994. 腐烂的橘子
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        bad_oranges = []
        good_oranges = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    bad_oranges.append((i,j))
                elif grid[i][j] == 1:
                    good_oranges.append((i,j))
        visited = list(bad_oranges)
        times = 0
        level_oranges = []
        while bad_oranges:
            i,j = bad_oranges.pop(0)
            for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if 0<=x<row and 0<=y<col and grid[x][y]==1 and (x,y) not in visited:
                    level_oranges.append((x,y))
                    good_oranges.remove((x,y))
                    grid[x][y] = 2
            if not bad_oranges and level_oranges:
                bad_oranges = level_oranges
                level_oranges = []
                times+=1

        return -1 if good_oranges else times


if __name__ == '__main__':
    sol = Solution()
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(sol.orangesRotting(grid))

