# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-20
    FileName   : sumRegion.py
    Author     : Honghe
    Descreption: 
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.dp = self.init_dp()

    def init_dp(self):
        if not self.matrix:
            return []
        row = len(self.matrix)
        col = len(self.matrix[0])
        dp = [[0]*col for _ in range(row)]
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                tmp_right = 0 if j+1>=col else dp[i][j+1]
                tmp_down = 0 if i+1>=row else dp[i+1][j]
                last_dp = 0 if j+1>=col or i+1>=row else dp[i+1][j+1]
                dp[i][j] = self.matrix[i][j]+tmp_down+tmp_right-last_dp
        return dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row = len(self.matrix)
        col = len(self.matrix[0])
        tmp_down = 0 if row2+1>=row else self.dp[row2+1][col1]
        tmp_right = 0 if col2+1>=col else self.dp[row1][col2+1]
        last_dp = 0 if row2+1>=row or col2+1>=col else self.dp[row2+1][col2+1]
        return self.dp[row1][col1]-tmp_right-tmp_down+last_dp




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    row1=1
    col1=1
    row2=2
    col2 = 2
    print(obj.sumRegion(row1,col1,row2,col2))

