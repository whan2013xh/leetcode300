# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-31
    FileName   : lengthOfLongestSubstring.py
    Author     : Honghe
    Descreption: 剑指 Offer 48. 最长不含重复字符的子字符串
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sub_string = set()
        max_len = 1
        start = 0
        for index,i in enumerate(s):
            if i not in sub_string:
                sub_string.add(i)
                max_len = max(max_len,len(sub_string))
            else:
                i_index = start+s[start:index].find(i)
                sub_string = set(s[i_index+1:index+1])
                start = i_index+1
        return max_len

if __name__ == '__main__':
    sol = Solution()
    s = "umvejcuuk"
    print(sol.lengthOfLongestSubstring(s))