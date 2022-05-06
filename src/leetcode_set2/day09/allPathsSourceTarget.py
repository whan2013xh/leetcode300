# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-18
    FileName   : allPathsSourceTarget.py
    Author     : Honghe
    Descreption: 797. 所有可能的路径
"""
import copy

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        path = []
        self.dfs(graph,path,[0])
        return path

    def dfs(self,graph,path,res):
        last_node = res[-1]
        if not graph[last_node]:
            return
        for i in graph[last_node]:
            res.append(i)
            if i==len(graph)-1:
                path.append(copy.deepcopy(res))
            else:
                self.dfs(graph,path,res)
            res.remove(i)


if __name__ == '__main__':
    sol = Solution()
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sol.allPathsSourceTarget(graph))
