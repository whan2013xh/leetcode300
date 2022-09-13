# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-19
    FileName   : allPathsSourceTarget.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]
        self.dfs(graph,0,path,res)
        return res


    def dfs(self,graph, index, path, res):
        n = len(graph)-1
        if index>n:
            return
        for node in graph[index]:
            path.append(node)
            if node==n:
                res.append(path[:])
                path.pop()
                continue
            self.dfs(graph,node,path,res)
            path.pop()

if __name__ == '__main__':
    sol = Solution()
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sol.allPathsSourceTarget(graph))

