# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-28
    FileName   : MagicDictionary.py
    Author     : Honghe
    Descreption: 剑指 Offer II 064. 神奇的字典
"""
from typing import List

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childs = [None]*26
        self.is_end = False

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self

            for i in word:
                index = ord(i)-ord('a')

                if cur.childs[index] is not None:
                    cur = cur.childs[index]
                else:
                    node = MagicDictionary()
                    cur.childs[index] = node
                    cur = node
            cur.is_end = True

    def search(self, searchWord: str) -> bool:
        return self.search2(searchWord,0)

    def search2(self, searchWord: str,count:int) -> bool:
        cur =self
        for word_index,i in enumerate(searchWord):
            index = ord(i)-ord('a')
            next_node = [j for j in cur.childs if j is not None]

            if not next_node:
                return False

            for node in next_node:
                if node != cur.childs[index]:
                    if count==1:
                        continue
                    count+=1
                tmp = node.search2(searchWord[word_index+1:],count)
                if tmp:
                    return True
                if node != cur.childs[index]:
                    count-=1
            return False

        if cur.is_end:
            return False if count==0 else True
        else:
            return False

if __name__ == '__main__':
    sol = MagicDictionary()
    dictory = ["judge", "judgg"]
    sol.buildDict(dictory)
    print(sol.search("juggg"))
    # print(sol.search("hhllo"))
    # print(sol.search("hell"))
    # print(sol.search("leetcoded"))