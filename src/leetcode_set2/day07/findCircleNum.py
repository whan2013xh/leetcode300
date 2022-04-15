# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-14
    FileName   : findCircleNum.py
    Author     : Honghe
    Descreption: 547. 省份数量
"""
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        num = 0
        row = len(isConnected)
        col = len(isConnected[0])
        for i in range(row):
            tmp = False
            for j in range(col):
                if isConnected[i][j]==1:
                    isConnected[i][j]=0
                    tmp = True
                    if i!=j:
                        self.dfs(isConnected,j,i)
            if tmp:
                num+=1
        return num

    def dfs(self, isConnected, x,y):
        col = len(isConnected[0])
        isConnected[x][y]=0
        isConnected[x][x]=0
        for i in range(col):
            if isConnected[x][i]==1:
                isConnected[x][i] = 0
                self.dfs(isConnected,i,x)
        return

if __name__ == '__main__':
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))