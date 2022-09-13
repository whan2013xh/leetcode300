# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-28
    FileName   : replaceWords.py
    Author     : Honghe
    Descreption: 剑指 Offer II 063. 替换单词
"""
from typing import List

class Trie:
    def __init__(self):
        self.childs = [None]*26
        self.is_end = False

    def insert(self, word):
        cur = self
        for i in word:
            index = ord(i)-ord('a')
            if cur.childs[index] is not None:
                cur = cur.childs[index]
            else:
                node = Trie()
                cur.childs[index] = node
                cur = node
        cur.is_end = True

    def replace_word(self, word):
        cur = self
        for word_index,char in enumerate(word):
            index = ord(char)-ord('a')
            if cur.childs[index] is not None:
                cur = cur.childs[index]
                if cur.is_end:
                    return word[:word_index+1]
            else:
                return word
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefix_tree = Trie()
        for i in dictionary:
            prefix_tree.insert(i)

        words = sentence.split()
        res = []
        for word in words:
            replace_word = prefix_tree.replace_word(word)
            res.append(replace_word)
        return " ".join(res)

if __name__ == '__main__':
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence ="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    sol = Solution()
    print(sol.replaceWords(dictionary,sentence))




