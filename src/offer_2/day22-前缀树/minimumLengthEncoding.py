# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-29
    FileName   : minimumLengthEncoding.py
    Author     : Honghe
    Descreption: 剑指 Offer II 065. 最短的单词编码

"""
from typing import List

class Trie:
    def __init__(self):
        self.childs = [None]*26
        self.is_end = False

    def add(self, word):
        cur = self
        flag = False
        for tmp_index,i in enumerate(word):
            index = ord(i) - ord('a')
            if cur.childs[index] is not None:
                cur = cur.childs[index]
            else:
                node = Trie()
                cur.childs[index] = node
                cur = node
                flag = True

        cur.is_end=True
        return len(word)+1 if flag else 0



class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        res = 0
        words = sorted(words,key=lambda t:len(t),reverse=True)
        for word in words:
            tmp_len = trie.add(word[::-1])
            res+=tmp_len
        return res

if __name__ == '__main__':
    sol = Solution()
    words = ["time","atime","btime"]
    print(sol.minimumLengthEncoding(words))



