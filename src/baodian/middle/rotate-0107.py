# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-23
    FileName   : rotate-0107.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i+1,col):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(row):
            for j in range(col//2):
                matrix[i][j],matrix[i][col-j-1] = matrix[i][col-j-1],matrix[i][j]


if __name__ == '__main__':
    sol = Solution()
    matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    sol.rotate(matrix)
    print(matrix)
