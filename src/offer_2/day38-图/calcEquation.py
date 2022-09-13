# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-19
    FileName   : calcEquation.py
    Author     : Honghe
    Descreption: 399. 除法求值 https://leetcode.cn/problems/evaluate-division/
"""
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        dfs,构建出图来就行，注意是有向图。
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        num_values = {}
        graph = defaultdict(list)

        for index,equation in enumerate(equations):
            x,y = equation
            graph[x].append(y)
            graph[y].append(x)
            num_values[(x,y)]=values[index]
            num_values[(y,x)] = round(1/values[index],5)

        res = []
        for query in queries:
            x,y = query
            if x not in graph or y not in graph:
                res.append(-1.0)
                continue
            if x==y:
                res.append(1.0)
                continue
            path = [x]
            visited = set([x])
            tmp = self.dfs(graph,path,y,x,visited)
            if not tmp:
                res.append(-1.0)
            else:
                value = 1.0
                print((x,y))
                for i in range(len(path)-1):
                    value*=num_values.get((path[i],path[i+1]))
                res.append(value)
        return res

    def dfs(self,graph,path,target,node,visited):
        for i in graph.get(node):
            if i in visited:
                continue
            visited.add(i)
            path.append(i)
            if i==target:
                return True
            res = self.dfs(graph,path,target,i,visited)
            if res:
                return True
            path.pop()
        return False

    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        带权查并集，注意合并时的权重更新。
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        node_ids = {}
        count = 0
        parents = list(range(len(equations)*2))
        size_list = [1.0] * len(equations)*2
        for index,equation in enumerate(equations):
            x, y = equation
            if x not in node_ids:
                node_ids[x] = count
                count+=1
            if y not in node_ids:
                node_ids[y] = count
                count += 1
            self.union(node_ids[x],node_ids[y],parents,size_list,values[index])

        res = []
        for query in queries:
            x, y = query
            if x not in node_ids or y not in node_ids:
                res.append(-1.0)
                continue
            if x==y:
                res.append(1.0)
                continue
            father_x = self.find(node_ids[x],parents,size_list)
            father_y = self.find(node_ids[y], parents, size_list)
            if father_x!=father_y:
                res.append(-1.0)
            else:
                res.append(size_list[node_ids[x]]/size_list[node_ids[y]])
        return res

    def find(self, node, parents, size_list):
        father = parents[node]
        if father!=node:
            parents[node] = self.find(father,parents,size_list)
            size_list[node] *= size_list[father]   # 注意权重/距离更新
        return parents[node]

    def union(self,node_a,node_b, parents, size_list,weight):
        father_a = self.find(node_a, parents, size_list)
        father_b = self.find(node_b, parents, size_list)
        if father_a==father_b:
            return
        parents[father_a] = father_b
        size_list[father_a] = size_list[node_b]*weight/size_list[node_a] # 注意权重/距离更新

if __name__ == '__main__':
    equations = [["a", "b"], ["e", "f"], ["b", "e"]]
    values = [3.4, 1.4, 2.3]
    queries = [["a", "f"]]
    sol = Solution()
    print(sol.calcEquation2(equations,values,queries))




