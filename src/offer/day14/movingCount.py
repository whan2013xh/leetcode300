# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-02
    FileName   : movingCount.py
    Author     : Honghe
    Descreption: 剑指 Offer 13. 机器人的运动范围
"""

class Solution(object):
    def movingCount(self, m, n, k):
        """
        dfs
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        visited = []
        self.dfs(m,n,k,0,0,visited)
        # print(visited)
        # res = [(i,j) for i in range(m) for j in range(n)]
        # print(list(set(res)-set(visited)))
        return len(visited)

    def dfs(self,m,n,k,x,y,visited):
        if not (0<=x<m and 0<=y<n and self.bit_sum(x,y)<=k and (x,y) not in visited):
            return
        visited.append((x,y))
        # self.dfs(m,n,k,x-1,y,visited)
        self.dfs(m, n, k, x+1, y, visited)
        self.dfs(m, n, k, x, y+1, visited)
        # self.dfs(m, n, k, x, y-1, visited)

    def bit_sum(self,x,y):
        bit_x =0
        for i in str(x):
            bit_x+=int(i)
        bit_y = 0
        for i in str(y):
            bit_y+=int(i)
        return bit_y+bit_x


if __name__ == '__main__':
    sol = Solution()
    m=11
    n=8
    k=16
    sol.bit_sum(10,7)
    print(sol.movingCount(m,n,k))