# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-28
    FileName   : solveNQueens-0812.py
    Author     : Honghe
    Descreption: 08.12. 八皇后 https://leetcode.cn/problems/eight-queens-lcci/
"""
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        回溯法，记录访问坐标，更新
        :param n:
        :return:
        """
        visited = [[False]*n for _ in range(n)]
        path = []
        res = []
        for i in range(n):
            path.append((0,i))
            change_pos = set()
            self.set_flag(0, i, visited, n,change_pos)
            self.dfs(0,i,visited,n,path,res)
            path.pop()
            self.set_flag(0, i, visited, n, change_pos,False)
        res_list = []
        for i in range(len(res)):
            tmp = []
            for x,y in res[i]:
                row = ["."]*n
                row[y]='Q'
                tmp.append("".join(row))
            res_list.append(tmp[:])
        return res_list

    def dfs(self, x, y, visited,n, path, res):
        if x==n-1:
            res.append(path[:])
            return

        for i in range(n):
            if visited[x+1][i]:
                continue
            path.append((x+1, i))
            change_pos = set()
            self.set_flag(x+1, i, visited, n, change_pos)
            self.dfs(x+1,i,visited,n,path, res)
            path.pop()
            self.set_flag(x+1, i, visited, n, change_pos,False)

    def set_flag(self,x,y,visited,n,change_pos=None,flag=True):
        if x==n-1:
            return
        if not change_pos:
            visited[x][y] = flag
            change_pos.add((x,y))
            for i in range(x+1,n):
                for tmp_x,tmp_y in [(i,y-(i-x)),(i,y),(i,y+(i-x))]:
                    if 0<=tmp_y<n and not visited[tmp_x][tmp_y]:
                        visited[tmp_x][tmp_y]=flag
                        change_pos.add((tmp_x, tmp_y))
        else:
            for tmp_x,tmp_y in change_pos:
                visited[tmp_x][tmp_y] = flag

    def solveNQueens2(self, n: int) -> List[List[str]]:
        """
        回溯法，借助坐标系斜率来记录访问位置
        :param n:
        :return:
        """
        path = []
        res = []
        column = set() # 当前列
        left = set()  # 左对角线，记录行坐标-列坐标
        right = set() # 右对角线，记录行坐标+列坐标
        self.dfs2(0,n,path,res,column,left,right)
        res_list = []
        for i in range(len(res)):
            tmp = []
            for y in res[i]:
                row = ["."] * n
                row[y] = 'Q'
                tmp.append("".join(row))
            res_list.append(tmp[:])
        return res_list

    def dfs2(self, index, n, path, res,column,left,right):
        if index==n:
            res.append(path[:])
            return
        for i in range(n):
            if i in column or index-i in left or index+i in right:
                continue
            path.append(i)
            column.add(i)
            left.add(index-i)
            right.add(index+i)
            self.dfs2(index+1,n,path,res,column,left,right)
            path.pop()
            column.remove(i)
            left.remove(index-i)
            right.remove(index+i)


if __name__ == '__main__':
    sol = Solution()
    n=5
    res = sol.solveNQueens2(n)
    print(res)
    print(len(res))


    # [["Q....", "..Q..", "....Q", ".Q...", "...Q."], ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
    #  [".Q...", "...Q.", "Q....", "..Q..", "....Q"], [".Q...", "....Q", "..Q..", "Q....", "...Q."],
    #  ["..Q..", "Q....", "...Q.", ".Q...", "....Q"], ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
    #  ["...Q.", "Q....", "..Q..", "....Q", ".Q..."], ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
    #  ["....Q", ".Q...", "...Q.", "Q....", "..Q.."], ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]]

