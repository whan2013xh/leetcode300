# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-23
    FileName   : setZeroes-0108.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        row_set = set()
        col_set = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_set.add(i)
                    col_set.add(j)

        for i in row_set:
            for j in range(col):
                matrix[i][j] = 0

        for i in range(row):
            for j in col_set:
                matrix[i][j] = 0

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    print(matrix)
