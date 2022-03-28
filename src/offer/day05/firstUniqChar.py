# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-28
    FileName   : firstUniqChar.py
    Author     : Honghe
    Descreption: 剑指 Offer 50. 第一个只出现一次的字符
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        chars = []
        for i in s:
            if count.get(i):
                if i in chars:
                    chars.remove(i)
                count[i] = count.get(i)+1
            else:
                count[i] = 1
                chars.append(i)
        return chars[0] if chars else " "

if __name__ == '__main__':
    sol=Solution()
    s = "leetcode"
    print(sol.firstUniqChar(s))
