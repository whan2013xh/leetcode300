# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-06
    FileName   : findAnagrams.py
    Author     : Honghe
    Descreption: 剑指 Offer II 015. 字符串中的所有变位词
"""
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []

        letter_count = Counter(p)
        tmp_count = letter_count
        res = []
        count = len(p)
        for index, letter in enumerate(s):
            if letter in letter_count:
                if tmp_count.get(letter)>0:
                    count-=1
                tmp_count[letter] = tmp_count.get(letter)-1
            if index<len(p)-1:
                continue
            if count==0:
                res.append(index-len(p)+1)
            if s[index-len(p)+1] in tmp_count:
                if tmp_count[s[index-len(p)+1]]>=0:
                    count+=1
                tmp_count[s[index - len(p)+1]] = tmp_count[s[index - len(p)+1]]+1
        return res

    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        letter_count = Counter(p)
        res = []
        need = len(p)

        for index, letter in enumerate(s):
            # 滑动窗口右窗口滑入元素
            if letter in letter_count:
                if letter_count.get(letter)>0:
                    need-=1
                letter_count[letter]-=1
            # 滑动窗口左窗口滑入元素
            if index-len(p)+1>0:
                pre_letter = s[index-len(p)]
                if pre_letter in letter_count:
                    if letter_count.get(pre_letter) >= 0:
                        need += 1
                    letter_count[pre_letter] += 1
            if need==0:
                res.append(index-len(p)+1)
        return res



if __name__ == '__main__':
    sol = Solution()
    s = "abab"
    p = "ab"
    print(sol.findAnagrams2(s,p))




