# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-06
    FileName   : validPalindrome.py
    Author     : Honghe
    Descreption: 剑指 Offer II 019. 最多删除一个字符得到回文
"""
from collections import Counter

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
                continue
            return self.is_palindrome(s[:left]+s[left+1:])|self.is_palindrome(s[:right]+s[right+1:])
        return True

    def is_palindrome(self, s):
        return s==s[::-1]

if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    print(sol.validPalindrome(s))