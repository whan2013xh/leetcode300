# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-23
    FileName   : reverseLeftWords.py
    Author     : Honghe
    Descreption: 剑指 Offer 58 - II. 左旋转字符串
"""

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:]+s[:n]

if __name__ == '__main__':
    sol = Solution()
    s = "abcdefg"
    n = 2
    print(sol.reverseLeftWords(s,n))