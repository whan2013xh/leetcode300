# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-16
    FileName   : updateMatrix.py
    Author     : Honghe
    Descreption: 542. 01 矩阵
"""
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        visited = [[-1 for _ in range(col)] for _ in range(row)]
        res = [[-1 for _ in range(col)] for _ in range(row)]
        step = 0
        for i in range(row):
            for j in range(col):
                if visited[i][j] ==-1:
                    res[i][j] = self.dfs(mat,visited,i,j,step)
                else:
                    res[i][j] = visited[i][j]
        return res

    def dfs(self, mat,visited, i, j, step):
        """
        dfs：但是时间超时了,动态规划一种
        :param mat:
        :param visited:
        :param i:
        :param j:
        :param step:
        :return:
        """
        row = len(mat)
        col = len(mat[0])
        if mat[i][j]==0:
            return step

        change_pos = [[-1,0],[1,0],[0,-1],[0,1]]
        steps = []
        vaild = []

        for x,y in change_pos:
            if i+x>=row or i+x<0 or j+y>=col or j+y<0:
                continue
            if mat[i+x][j+y]==0:
                visited[i][j] = 1
                return step+1
            vaild.append([i+x,j+y])
        for tmp_x,tmp_y in vaild:
            if visited[tmp_x][tmp_y]!=-1:
                steps.append(visited[tmp_x][tmp_y]+1)
            else:
                visited[tmp_x][tmp_y]=self.dfs(mat,visited,tmp_x,tmp_y,step)
                steps.append(visited[tmp_x][tmp_y]+1)
        return min(steps)

    def updateMatrix2(self, mat):
        """
        bfs
        :param mat:
        :return:
        """
        row = len(mat)
        col = len(mat[0])

        res = [[0 for _ in range(col)] for _ in range(row)]
        zero_queue = [(i,j) for i in range(row) for j in range(col) if mat[i][j]==0]
        change_pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited =list(zero_queue)
        while zero_queue:
            i, j = zero_queue.pop(0)
            for x, y in change_pos:
                if 0<=i + x < row and 0<=j + y < col and (i+x,j+y) not in visited:
                    # 下面为啥是直接加1就行，因为这是bfs
                    res[i+x][j+y]=res[i][j]+1
                    zero_queue.append((i+x,j+y))
                    visited.append((i+x,j+y))

        return res

    def updateMatrix3(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10 ** 9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


if __name__ == '__main__':
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(sol.updateMatrix2(mat))