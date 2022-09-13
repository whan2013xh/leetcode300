# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-11
    FileName   : getMaxMatrix-1724.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        """
        动态规划:最大子序列和的升级版，最大子序列是一维数组，这个是二维的，但是能够将二维数组转换成一维。
        通过前缀和的方式将二维数组压缩成一维数组，具体就是将从第i行到第j行的每一列元素相加，这样形成一个一维数组，不断求这个一维数组的最长子序列
        :param matrix:
        :return:
        """
        row = len(matrix)
        col = len(matrix[0])
        res = [0]*4
        tmp_max = float("-inf")
        for i in range(row):
            prefix_matrix = [0]*col
            for j in range(i,row):
                dp = [0]*col
                start_x = 0
                start_y = 0
                for k in range(col):
                    # 这里是一个技巧，如何不断更新前缀和的数组
                    prefix_matrix[k]+=matrix[j][k]
                    if k==0 or dp[k-1]<0:
                        # 如果子序列开头重新开始，那么更新起始为坐标
                        dp[k] = prefix_matrix[k]
                        start_x = i
                        start_y = k
                    else:
                        dp[k] = dp[k - 1] + prefix_matrix[k]

                    if dp[k]>tmp_max:
                        res = [start_x,start_y,j,k]
                        tmp_max = dp[k]
        return res


if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [-1, 1],
        [0, -1]
    ]
    print(sol.getMaxMatrix(matrix))



