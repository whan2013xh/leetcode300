# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-06
    FileName   : countBits.py
    Author     : Honghe
    Descreption: 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n>=0:
            res.append(0)
        if n>=1:
            res.append(1)
        tmp = []
        count = 1
        for i in range(2,n):
