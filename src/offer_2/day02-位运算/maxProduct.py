# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-07
    FileName   : maxProduct.py
    Author     : Honghe
    Descreption: 剑指 Offer II 005. 单词长度的最大乘积
"""
from typing import List

class Solution(object):
    def maxProduct(self, words):
        """
        暴力法
        :type words: List[str]
        :rtype: int
        """
        words_set = [set(word) for word in words]
        max_res = 0
        for index,word in enumerate(words[:-1]):
            for another_index in range(index+1,len(words)):
                if len(words_set[index]-words_set[another_index])==len(words_set[index]):
                    max_res = max(max_res, len(word)*len(words[another_index]))
        return max_res

    def maxProduct2(self, words: List[str]) -> int:
        """
        位运算优化
        :param words:
        :return:
        """
        bitmask_map, ans = {}, 0
        for i in range(len(words)):
            bitmask = 0
            for c in words[i]:
                bitmask |= 1 << (ord(c) - ord('a'))
            if bitmask in bitmask_map:
                bitmask_map[bitmask] = max(bitmask_map[bitmask], len(words[i]))
            else:
                bitmask_map[bitmask] = len(words[i])

        for x in bitmask_map:
            for y in bitmask_map:
                if (x & y) == 0:
                    ans = max(ans, bitmask_map[x] * bitmask_map[y])

        return ans



if __name__ == '__main__':
    sol = Solution()
    words = ["abcw","baz","a","bar","a","abcdef"]
    print(sol.maxProduct(words))
