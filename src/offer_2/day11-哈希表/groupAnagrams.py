# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-16
    FileName   : groupAnagrams.py
    Author     : Honghe
    Descreption: 剑指 Offer II 033. 变位词组
"""
from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_count =[]
        visited = {}
        for index,s in enumerate(strs):
            count_s = Counter(s)
            if count_s in str_count:
                i = str_count.index(count_s)
                tmp = visited[i]
                tmp.append(s)
                visited[i] = tmp
            else:
                str_count.append(count_s)
                visited[len(str_count)-1] = [s]
        return list(visited.values())


if __name__ == '__main__':
    strs = ["a"]
    sol = Solution()
    print(sol.groupAnagrams(strs))