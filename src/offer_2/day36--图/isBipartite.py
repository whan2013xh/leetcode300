# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-14
    FileName   : isBipartite.py
    Author     : Honghe
    Descreption: 
"""
from typing import List


class DSU_normal:
    def __init__(self, size):
        self.father = list(range(size))

    def find(self, node):
        father = self.father[node]
        if node != father:
            # 保证子树节点数正确
            father = self.find(father)
        return father

    def union(self, node_a, node_b):
        father_a = self.find(node_a)
        father_b = self.find(node_b)
        self.father[father_a] = father_b



class DSU:
    def __init__(self, size):
        self.father = list(range(size))
        # 子树的节点个数作为秩
        self.size = [1 for _ in range(size)]

    def find(self, node):
        """
        查找：路径压缩，用递归方法查找，同时维护子树的秩
        :param node:
        :return:
        """
        father = self.father[node]
        if node != father:
            # 保证子树节点数正确
            if father != self.father[father]:
                self.size[father] -= 1
            father = self.find(father)
        self.father[node] = father
        return father

    def union(self, node_a, node_b):
        """
        合并:注意维持子树的秩
        :param node_a:
        :param node_b:
        :return:
        """
        father_a = self.find(node_a)
        father_b = self.find(node_b)
        if father_a == father_b:
            return
        # 保证小的子树合并到大的子树里面
        if self.size[father_a] > self.size[father_b]:
            father_a, father_b = father_b, father_a
        self.father[father_a] = father_b
        self.size[father_b] = self.size[father_a] + self.size[father_b]


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        广度优先遍历,这里直接用空间换时间了，按照LeetCode上解法，还可以借助染色来解决，大同小异
        :param graph:
        :return:
        """
        if len(graph) == 1:
            return True

        visited = [False] * len(graph)
        stack1 = []
        stack2 = []
        set1 = set()
        set2 = set()
        for index, nodes in enumerate(graph):
            if visited[index]:
                continue
            stack1 = nodes[:]
            set2.add(index)
            visited[index] = True
            while stack1 or stack2:
                while stack1:
                    num = stack1.pop()
                    if num in set2:
                        return False
                    if visited[num]:
                        continue
                    visited[num] = True
                    set1.add(num)
                    stack2 += graph[num]

                while stack2:
                    num = stack2.pop()
                    if num in set1:
                        return False
                    if visited[num]:
                        continue
                    visited[num] = True
                    set2.add(num)
                    stack1 += graph[num]
        return True

    def isBipartite2(self, graph: List[List[int]]) -> bool:
        """
        查并集
        :param graph:
        :return:
        """
        if len(graph) == 1:
            return True
        parents = list(range(len(graph)))

        for node, next_nodes in enumerate(graph):
            for i in next_nodes:
                if self.find(node, parents) == self.find(i, parents):
                    return False
                # 这步就是在合并
                parents[self.find(i, parents)] = self.find(next_nodes[0], parents)
        return True

    def find(self, node, parents):
        """
        查找祖先
        :param node:
        :param parents:
        :return:
        """
        while node != parents[node]:
            node = parents[node]
        return node


if __name__ == '__main__':
    sol = Solution()
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(sol.isBipartite2(graph))
