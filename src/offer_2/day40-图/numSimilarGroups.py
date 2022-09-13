# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-22
    FileName   : numSimilarGroups.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        length = len(strs)
        parents = list(range(length))
        for i in range(length-1):
            for j in range(i+1,length):
                if parents[i]==parents[j]:
                    continue
                if self.is_same(strs[i],strs[j]):
                    self.union(i,j,parents)

        return sum(index==value for index,value in enumerate(parents))

    def is_same(self,word1,word2):
        if word1==word2:
            return True
        diff = 0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                diff+=1
                if diff>2:
                    return False
        return diff==2

    def find(self,node,parents):
        father = parents[node]
        if node!=father:
            parents[node]=self.find(father,parents)
        return parents[node]

    def union(self,node_a,node_b,parents):
        father_a = self.find(node_a,parents)
        father_b = self.find(node_b,parents)
        if father_a==father_b:
            return
        parents[father_a]=father_b


if __name__ == '__main__':
    sol = Solution()
    strs = ["omv","ovm"]
    print(sol.numSimilarGroups(strs))
