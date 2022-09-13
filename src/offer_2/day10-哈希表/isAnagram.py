# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-15
    FileName   : isAnagram.py
    Author     : Honghe
    Descreption: 
"""
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s)==Counter(t) and s!=t