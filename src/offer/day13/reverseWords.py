# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : reverseWords.py
    Author     : Honghe
    Descreption: 剑指 Offer 58 - I. 翻转单词顺序
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        return " ".join(words[::-1])