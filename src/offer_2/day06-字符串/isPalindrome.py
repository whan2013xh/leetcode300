# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-06
    FileName   : isPalindrome.py
    Author     : Honghe
    Descreption: 剑指 Offer II 018. 有效的回文
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left = 0
        right = len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

if __name__ == '__main__':
    sol = Solution()
    s = ".,"
    print(sol.isPalindrome(s))
