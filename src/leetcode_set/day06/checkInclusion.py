# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-14
    FileName   : checkInclusion.py
    Author     : Honghe
    Descreption: 567. 字符串的排列
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        window_size = len(s1)
        sorted_s1 = sorted(list(s1))
        for i in range(len(s2)-window_size+1):
            if s2[i] not in s1:
                continue
            if sorted_s1==sorted(s2[i:i+window_size]):
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s1 = "adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1,s2))