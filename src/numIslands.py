# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021/7/28 21:54
    FileName   : numIslands.py
    Author     : xuhan
    Descreption: 200. 岛屿数量
"""


class Solution(object):
    def numIslands(self, grid):
        """
        dfs:深度优先搜索，递归搜索将为连成岛屿的1全部变成0
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        nums = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    nums += 1
                    self.dfs(grid, i, j, row, col)
        return nums

    def dfs(self, grid, x, y, row, col):
        grid[x][y] = "0"
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if i > row - 1 or j > col - 1 or i < 0 or j < 0:
                continue
            if grid[i][j] == "1":
                self.dfs(grid, i, j, row, col)

    def numIslands2(self, grid):
        """
        bfs:广度优先遍历，需要借助队列来遍历
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        nums = 0
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    nums += 1
                    grid[i][j] = 0
                    queue.append([i, j])
                while len(queue) > 0:
                    x, y = queue.pop(0)
                    for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= cur_x <= row - 1 and 0 <= cur_y <= col - 1 and grid[cur_x][cur_y] == "1":
                            grid[cur_x][cur_y] = 0
                            queue.append([cur_x, cur_y])
        return nums


    def numIslands3(self, grid):
        """
        并查集：
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        union = UnionFind(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    for cur_x, cur_y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= cur_x <= row - 1 and 0 <= cur_y <= col - 1 and grid[cur_x][cur_y] == "1":
                            union.merge(i*col+j, cur_x*col+cur_y)
        return union.get_count()


class UnionFind:
    def __init__(self, grid):
        """
        并查集初始化，并查集的重要思想在于，用集合中的一个元素代表集合，可以参考树结构用根节点表示这个树，同一个集合就是一棵树
        :param grid:
        """
        row = len(grid)
        col = len(grid[0])
        # parent数组保存的是当前索引位置对应的父节点的索引值
        self.parent = [i for i in range(row*col)]
        # 标记对应索引位置所在子树/集合的复杂度，用处在于在合并两个集合/子树时，优先把复杂度低的集合合并到复杂度高的集合中，这样整体复杂度不变
        self.rank = [0] * (row*col)
        self.count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    self.count+=1

    def find(self, x):
        if self.parent[x]==x:
            return x
        else:
            # 递归设置父节点为最终的根节点，能够压缩查询路径
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        # 如果这两个节点对应的祖先节点是同一个的话，代表已经merge过了
        if x_parent==y_parent:
            return

        self.count -= 1
        x_rank = self.rank[x_parent]
        y_rank = self.rank[y_parent]

        # 下面这个逻辑就是把复杂度低的子树合并到复杂度高的子树中去，复杂度相同时，把合并后的子树复杂度加一
        if x_rank<y_rank:
            self.parent[x_parent] = y_parent
        elif x_rank>y_rank:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent]+=1

    def get_count(self):
        return self.count



if __name__ == '__main__':
    grid = [
        ["1"],["1"]
    ]

    sol = Solution()
    res = sol.numIslands3(grid)
    print(res)
