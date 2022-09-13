# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-22
    FileName   : findCircleNum.py
    Author     : Honghe
    Descreption: 547. 省份数量 https://leetcode.cn/problems/number-of-provinces/
"""
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        dfs
        :param isConnected:
        :return:
        """
        res = 0
        row = len(isConnected)
        visited = [False]*row
        for i in range(row):
            if visited[i]:
                continue
            res+=1
            visited[i] = True
            self.dfs(isConnected,visited,i)
        return res

    def dfs(self,isConnected,visited,index):
        col = len(isConnected)
        for i in range(col):
            if i==index or not isConnected[index][i] or visited[i]:
                continue
            visited[i] = True
            self.dfs(isConnected,visited,i)

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        """
        查并集
        :param isConnected:
        :return:
        """
        row = len(isConnected)
        parents = list(range(row))
        for i in range(row-1):
            for j in range(i+1,row):
                if isConnected[i][j]:
                    self.union(i,j,parents)
        return sum(index==value for index,value in enumerate(parents))

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
    isConnected =[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(sol.findCircleNum2(isConnected))
