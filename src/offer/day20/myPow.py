# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : myPow.py
    Author     : Honghe
    Descreption: 剑指 Offer 16. 数值的整数次方
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)

        y = self.myPow(n//2)
        return y*y if n%2==0 else y*y*x
        