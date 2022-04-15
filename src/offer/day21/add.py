# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-12
    FileName   : add.py
    Author     : Honghe
    Descreption: 剑指 Offer 65. 不用加减乘除做加法
"""

class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
