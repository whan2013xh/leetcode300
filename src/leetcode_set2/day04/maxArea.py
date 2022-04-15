# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : maxArea.py
    Author     : Honghe
    Descreption: 11. 盛最多水的容器
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height)-1
        while left<right:
            res = max(res, min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right -= 1
        return res

    def maxArea2(self, height):
        res = 0
        right = len(height) - 1
        while right>0:
            for i in range(right):
                res = max(res, min(height[i],height[right])*(right-i))
            right-=1
        return res


