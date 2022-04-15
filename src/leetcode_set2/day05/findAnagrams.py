# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-13
    FileName   : findAnagrams.py
    Author     : Honghe
    Descreption: 438. 找到字符串中所有字母异位词
"""
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        window_size = len(p)
        res = []
        for i in range(len(s)-window_size+1):
            window = s[i:i+window_size]
            if self.is_same(window,p):
                res.append(i)
        return res

    def is_same(self, p, q):
        return collections.Counter(p)==collections.Counter(q)

    def findAnagrams2(self, s, p):
        if len(s)<len(p):
            return []
        window_size = len(p)
        res = []
        count = [0]*26
        window_count = [0]*26
        for i in range(window_size):
            count[ord(p[i])-ord('a')] += 1
            window_count[ord(s[i])-ord('a')] += 1

        if window_count==count:
            res.append(0)
        left = 0
        for j in range(window_size,len(s)):
            window_count[ord(s[left])-ord('a')]-=1
            window_count[ord(s[j])-ord('a')] +=1
            left+=1
            if window_count==count:
                res.append(left)
        return res





if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams2(s,p))