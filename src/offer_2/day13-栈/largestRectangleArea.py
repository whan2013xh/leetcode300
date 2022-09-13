# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-20
    FileName   : largestRectangleArea.py
    Author     : Honghe
    Descreption: 剑指 Offer II 039. 直方图最大矩形面积
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        left = [-1]*len(heights)
        for index,i in enumerate(heights):
            while stack and heights[stack[-1]]>=i:
                stack.pop()
            if stack:
                left[index] = stack[-1]
            stack.append(index)

        stack = []
        right = [len(heights)]*len(heights)
        for index,i in enumerate(heights):
            while stack and heights[stack[-1]]>i:
                right[stack[-1]] = index
                stack.pop()
            stack.append(index)

        res = 0
        for index,i in enumerate(heights):
            res = max(res,(right[index]-left[index]-1)*i)
        return res

if __name__ == '__main__':
    sol = Solution()
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))







