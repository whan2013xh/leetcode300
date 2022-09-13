# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-29
    FileName   : findWhetherExistsPath-0401.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import defaultdict

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if start<0 or start>n-1 or target<0 or target>n-1:
            return False
        edages = defaultdict(set)
        for i,j in graph:
            # 去掉环
            if start==target and i==j==start:
                return True
            if i!=j:
                edages[i].add(j)
        path = set()
        path.add(start)
        res = self.dfs(target,edages,path,start)
        return res


    def dfs(self,target,edages,path,node):
        for i in edages.get(node,[]):
            if i==target:
                return True
            if i in path or not edages.get(i):
                continue
            path.add(i)
            res = self.dfs(target,edages,path,i)
            if res:
                return True
            path.pop()
        return False



if __name__ == '__main__':
    sol = Solution()
    n = 5
    graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3],
                    [3, 4]]
    start = 0
    target = 4
    print(sol.findWhetherExistsPath(n,graph,start,target))





