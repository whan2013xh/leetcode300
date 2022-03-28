# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-15
    FileName   : maxAreaOfIsland.py
    Author     : Honghe
    Descreption: 695. 岛屿的最大面积
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pos = []
        #pos.append([0, 0])
        row = len(grid)
        col = len(grid[0])
        visited = []
        max_area = 0
        for tmp_row in range(row):
            for tmp_col in range(col):
                if [tmp_row,tmp_col] in visited:
                    continue
                visited.append([tmp_row,tmp_col])
                if grid[tmp_row][tmp_col]==0:
                    continue
                else:
                    tmp_area = 1
                    pos.append([tmp_row,tmp_col])
                    while pos:
                        cur = pos.pop(0)
                        tmp_sr, tmp_sc = cur
                        round_pos = [[tmp_sr - 1, tmp_sc], [tmp_sr + 1, tmp_sc], [tmp_sr, tmp_sc - 1], [tmp_sr, tmp_sc + 1]]
                        for i, j in round_pos:
                            if [i, j] in visited:
                                continue
                            else:
                                visited.append([i, j])
                            if 0 <= i < row and 0 <= j < col and grid[i][j] == 1:
                                tmp_area+=1
                                pos.append([i, j])
                    max_area = max(max_area, tmp_area)
        return max_area

if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    grid = [[0,1],[1,0]]

    print(sol.maxAreaOfIsland(grid))