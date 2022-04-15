# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-06
    FileName   : searchMatrix.py
    Author     : Honghe
    Descreption: 74. 搜索二维矩阵
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j= col-1
        while 0<=i<row and 0<=j<col:
            if matrix[i][j]>target:
                j-=1
            elif matrix[i][j]<target:
                i+=1
            else:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,3]]
    target = 3
    print(sol.searchMatrix(matrix, target))