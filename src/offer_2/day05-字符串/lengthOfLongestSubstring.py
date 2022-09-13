# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-06
    FileName   : lengthOfLongestSubstring.py
    Author     : Honghe
    Descreption: 剑指 Offer II 016. 不含重复字符的最长子字符串
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_length = 1
        start = 0
        end = 0
        length = 0
        count = {}
        for index, letter in enumerate(s):
            if letter not in count:
                count[letter] = 1
                length += 1
                if length>max_length:
                    start = index-length+1
                    max_length = length
            else:
                while start<index:
                    cur = s[start]
                    count[cur]-=1
                    start += 1
                    if cur==letter and count[letter]==0:
                        count[letter]=1
                        length = index-start+1
                        break
                    if count[cur]==0:
                        count.pop(cur)
        return max_length

if __name__ == '__main__':
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))



