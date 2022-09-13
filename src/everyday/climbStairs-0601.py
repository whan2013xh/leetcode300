# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-01
    FileName   : climbStairs-0601.py
    Author     : Honghe
    Descreption: 70. 爬楼梯
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        first_pre = 1
        pre = 2
        res =2
        for i in range(3,n+1):
            res = first_pre+pre
            first_pre = pre
            pre = res
        return res