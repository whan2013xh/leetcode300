# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-02
    FileName   : exist.py
    Author     : Honghe
    Descreption: 剑指 Offer 12. 矩阵中的路径
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
        visited = []
        pos = 0
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[pos]:
                    visited.append((i,j))
                    if len(visited)==len(word):
                        return True
                    pos+=1
                    res = self.find_path(board,word,i,j,visited,pos)
                    if res:
                        return True
                    pos=0
                    visited.remove((i,j))
        return False


    def find_path(self,board,word,pos_x,pos_y,visited,pos):
        row = len(board)
        col = len(board[0])
        for x, y in [[pos_x - 1, pos_y], [pos_x + 1, pos_y], [pos_x, pos_y - 1], [pos_x, pos_y + 1]]:
            if 0<=x<row and 0<=y<col and board[x][y]==word[pos] and (x,y) not in visited:
                visited.append((x,y))
                if len(visited) == len(word):
                    return True
                pos+=1
                res = self.find_path(board,word,x,y,visited,pos)
                if res:
                    return True
                visited.remove((x,y))
                pos-=1
        return False


if __name__ == '__main__':
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(sol.exist(board,word))


