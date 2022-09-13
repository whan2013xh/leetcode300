# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-06
    FileName   : minWindow.py
    Author     : Honghe
    Descreption: 剑指 Offer II 017. 含有所有字符的最短字符串
"""
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)<len(t):
            return ""
        min_length = len(s)+1
        need = len(t)
        start = 0
        count = Counter(t)
        left = -1
        for index, letter in enumerate(s):
            if letter in count:
                if count.get(letter)>0:
                    need-=1
                count[letter]-=1

            while need==0:
                length = index-start+1
                if length<min_length:
                    left = start
                    min_length = length
                if s[start] in count:
                    if count[s[start]]==0:
                        need+=1
                    count[s[start]]+=1
                start+=1
        return "" if min_length==len(s)+1 else s[left:left+min_length]

if __name__ == '__main__':
    sol = Solution()
    s = "A"
    t = "A"
    print(sol.minWindow(s,t))




