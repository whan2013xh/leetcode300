# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-26
    FileName   : findRedundantConnection.py
    Author     : Honghe
    Descreption: 684. 冗余连接
"""
from collections import defaultdict,deque
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges)+1))
        for edage in edges:
            x,y =edage
            if self.find(x,parents)== self.find(y,parents):
                return edage
            parents[self.find(x,parents)]=self.find(y,parents)
        return []

    def find(self,node,parents):
        father = parents[node]
        if father!=node:
            parents[node] = self.find(father,parents)
        return parents[node]

if __name__ == '__main__':
    sol = Solution()
    edges = [[16,25],[7,9],[3,24],[10,20],[15,24],[2,8],[19,21],[2,15],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]
    print(sol.findRedundantConnection(edges))
