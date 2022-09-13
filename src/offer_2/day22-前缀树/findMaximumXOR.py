# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-30
    FileName   : findMaximumXOR.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Trie:
    def __init__(self):
        self.childs = [None]*2


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        res = float("-inf")
        root =Trie()
        for num in nums:
            self.insert(num,root)

        for num in nums:
            num_xor = self.search_max_xor(num,root)
            res = max(num_xor,res)
        return res


    def insert(self, num, root):
        cur = root
        for i in range(30,-1,-1):
            index = num>>i&1
            if cur.childs[index] is None:
                node = Trie()
                cur.childs[index]=node
                cur = node
            else:
                cur = cur.childs[index]

    def search_max_xor(self, num, root):
        cur = root
        res = 0
        for i in range(30, -1, -1):
            index = num >> i & 1
            other = 0 if index == 1 else 1
            if cur.childs[other] is not None:
                res = res*2+other
                cur = cur.childs[other]
            else:
                res = res*2+index
                cur = cur.childs[index]
        return num^res

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    print(sol.findMaximumXOR(nums))




