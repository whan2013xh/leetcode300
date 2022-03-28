# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-14
    FileName   : lengthOfLongestSubstring.py
    Author     : Honghe
    Descreption: 3. 无重复字符的最长子串
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ""
        left = 0
        right = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] not in sub_str:
                right +=1
                max_length = max(max_length,right-left)
            else:
                index = sub_str.find(s[i])
                left += index+1
                right +=1
            sub_str = s[left:right]
        return max_length

if __name__ == '__main__':
    sol = Solution()
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))