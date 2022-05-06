# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-20
    FileName   : exist.py
    Author     : Honghe
    Descreption: 79. 单词搜索
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        if row==1 and col==1:
            return board[0][0]==word
        visited = []
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j]==word[0]:
                    if len(word)==1:
                        return True
                    visited.append((i,j))
                    res = self.dfs(board,word,1,visited,i,j)
                    if res:
                        return True
                    visited = []
        return False


    def dfs(self,board,word,index,visited,x,y):
        row = len(board)
        col = len(board[0])
        res = False
        for i,j in [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]:
            if 0<=i<row and 0<=j<col and (i,j) not in visited and board[i][j]==word[index]:
                if index==len(word)-1:
                    return True
                visited.append((i, j))

                res = self.dfs(board,word,index+1,visited,i,j)
                if res:
                    return res
                visited.pop()
        return res

if __name__ == '__main__':
    sol = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    print(sol.exist(board,word))

