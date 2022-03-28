# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-28
    FileName   : findNumberIn2DArray.py
    Author     : Honghe
    Descreption: 剑指 Offer 04. 二维数组中的查找
"""

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        col = len(matrix[0])
        row = len(matrix)

        i=0
        j=0
        end = col-1
        visited = [[0]*col for _ in range(row)]
        while 0<=i<row and 0<=j<=end:
            visited[i][j]=1
            while j<=end and matrix[i][j]<=target:
                if matrix[i][j] == target:
                    return True
                j+=1
            i+=1
            end = min(j,end)
            j=0
        return False

    def findNumberIn2DArray2(self, matrix, target):
        """
        从矩阵的右上角开始遍历
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False
        col = len(matrix[0])
        row = len(matrix)
        i = 0
        j = col-1
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
    matrix = [
  [1,1]
]
    target = 0

    print(sol.findNumberIn2DArray(matrix,target))

