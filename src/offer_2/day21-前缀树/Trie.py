# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-28
    FileName   : Trie.py
    Author     : Honghe
    Descreption: 剑指 Offer II 062. 实现前缀树
"""
class Node:
    def __init__(self,val,is_end=False,childs=None):
        self.val = val
        self.is_end = is_end
        self.childs = [] if childs is None else childs
        self.childs_val = [] if childs is None else [i.val for i in childs]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for i in word:
            if i in cur.childs_val:
                cur = cur.childs[cur.childs_val.index(i)]
                continue
            node = Node(i)
            cur.childs.append(node)
            cur.childs_val.append(i)
            cur = node
        cur.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for i in word:
            if i not in cur.childs_val:
                return False
            cur = cur.childs[cur.childs_val.index(i)]
        return cur.is_end


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for i in prefix:
            if i not in cur.childs_val:
                return False
            cur = cur.childs[cur.childs_val.index(i)]
        return True

if __name__ == '__main__':
    sol = Trie()
    sol.insert("apple")
    print(sol.search("apple"))
    print(sol.search("app"))
    print(sol.startsWith("app"))
    sol.insert("app")
    print(sol.search("app"))