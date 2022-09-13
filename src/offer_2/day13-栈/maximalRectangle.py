# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-20
    FileName   : maximalRectangle.py
    Author     : Honghe
    Descreption: 剑指 Offer II 040. 矩阵中最大的矩形
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        res = 0
        heights = [0]*col
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='0':
                    heights[j]=0
                elif i>0 and matrix[i-1][j]=='0':
                    heights[j] = 1
                else:
                    heights[j]+=1

            tmp_res = self.find_max_area(heights)
            res = max(res,tmp_res)
        return res

    def find_max_area(self, heights):
        """
        单调栈寻找最大的矩形
        :param heights:
        :return:
        """
        stack = []
        left = [-1]*(len(heights))
        right = [len(heights)]*len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                right[stack[-1]]=i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i]*(right[i]-left[i]-1))
        return ans



if __name__ == '__main__':
    sol = Solution()
    matrix = ["10100","10111","11111","10010"]
    print(sol.maximalRectangle(matrix))




