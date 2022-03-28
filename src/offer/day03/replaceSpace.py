# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-22
    FileName   : replaceSpace.py
    Author     : Honghe
    Descreption: 剑指 Offer 05. 替换空格
"""

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            if i==" ":
                res.append("%20")
            else:
                res.append(i)
        return res

