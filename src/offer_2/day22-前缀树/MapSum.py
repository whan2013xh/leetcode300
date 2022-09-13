# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-29
    FileName   : MapSum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 066. 单词之和
"""
class Trie:
    def __init__(self):
        self.childs = [None]*26
        self.val = None

    def insert(self, key,val):
        cur = self
        for i in key:
            index = ord(i)-ord('a')
            if cur.childs[index] is not None:
                cur = cur.childs[index]
            else:
                node = Trie()
                cur.childs[index]=node
                cur = node
            cur.val+=val


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()
        self.map = {}


    def insert(self, key: str, val: int) -> None:
        delta = val if self.map.get(key) is None else val-self.map[key]
        self.map[key]=val
        self.root.insert(key,delta)


    def sum(self, prefix: str) -> int:
        node = self.root
        for i in prefix:
            index = ord(i)-ord('a')
            if node.childs[index] is None:
                return 0
            node = node.childs[index]
        return node.val
