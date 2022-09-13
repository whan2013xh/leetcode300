# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-14
    FileName   : updateMatrix.py
    Author     : Honghe
    Descreption: 542. 01 矩阵 https://leetcode.cn/problems/01-matrix/
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        多源bfs
        :param mat:
        :return:
        """
        row = len(mat)
        col = len(mat[0])
        res = [[0] * col for _ in range(row)]
        zero_pos = []

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    zero_pos.append((i,j))
        visited = set(zero_pos)
        while zero_pos:
            x, y = zero_pos.pop(0)
            for i,j in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
                if 0<=i<row and 0<=j<col and mat[i][j]==1 and (i,j) not in visited:
                    res[i][j] = res[x][y]+1
                    zero_pos.append((i,j))
                    visited.add((i,j))
        return res

    def bfs(self, start, target):
        import collections
        # 核心队列，将初始状态添加进初始队列中
        q = collections.deque(start)
        # 记录已经访问过的路径
        visited = set().add(start)

        # 广度优先搜索
        while q:
            # 记录当前高度的广度是多少
            level_size = len(q)
            for i in range(level_size):
                cur = q.popleft()
                if cur is target:
                    return
                # 遍历邻接节点
                for node in cur.adj():
                    # 如果没有访问过
                    if node not in visited:
                        q.append(node)
                        visited.add(node)






if __name__ == '__main__':
    sol = Solution()
    mat =[[0,0,0],[0,1,0],[1,1,1]]
    print(sol.updateMatrix(mat))