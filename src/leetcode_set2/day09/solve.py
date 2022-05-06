# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-18
    FileName   : solve.py
    Author     : Honghe
    Descreption: 130. 被围绕的区域
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])
        if row<=2 or col<=2:
            return
        pos = [[0,i] for i in range(col)]+[[row-1,i] for i in range(col)]+[[i,0] for i in range(1,row-1)]+[[i,col-1] for i in range(1,row-1)]
        visited = []
        for i,j in pos:
            if (i,j) not in visited:
                if board[i][j]=='O':
                    visited.append((i, j))
                    self.dfs(board,i,j,visited)
        for i in range(1,row-1):
            for j in range(1,col-1):
                if board[i][j]=='O' and (i,j) not in visited:
                    board[i][j]='X'
        # board = [['X']*col for _ in range(row)]
        # for i,j in visited:
        #     board[i][j]='O'
        return board

    def dfs(self,board,x,y,visited):
        if board[x][y]=='X':
            return
        row = len(board)
        col = len(board[0])
        for i,j in [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]:
            if 0<=i<row and 0<=j<col and (i,j) not in visited:
                if board[i][j]=='O':
                    visited.append((i, j))
                    self.dfs(board,i,j,visited)


if __name__ == '__main__':
    sol = Solution()
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    print(sol.solve(board))


