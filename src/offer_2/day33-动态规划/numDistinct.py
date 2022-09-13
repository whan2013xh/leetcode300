# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-12
    FileName   : numDistinct.py
    Author     : Honghe
    Descreption: 
"""
import math

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        visited = [[-1]*len(t) for _ in range(len(s))]
        res = self.dp(s,0,t,0,visited)
        return res


    def dp(self,s,i,t,j,visited):
        if len(s)-i<len(t)-j:
            return 0
        if j==len(t):
            return 1
        if visited[i][j]!=-1:
            return visited[i][j]

        res = 0
        if s[i]==t[j]:
            res = self.dp(s,i+1,t,j+1,visited) + self.dp(s,i+1,t,j,visited)
        else:
            res = self.dp(s,i+1,t,j,visited)
        visited[i][j] = res
        return res

    def numDistinct2(self, s: str, t: str) -> int:
        """
        正常二维dp
        :param s:
        :param t:
        :return:
        """
        if len(t)>len(s):
            return 0

        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if j>i:
                   break
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

    def numDistinct3(self, s: str, t: str) -> int:
        """
        空间压缩1：用两个一维数组交替
        :param s:
        :param t:
        :return:
        """
        if len(t)>len(s):
            return 0

        cur = [0]*(len(t)+1)
        pre = [0] * (len(t) + 1)
        pre[0] = 1
        cur[0] = 1

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if j>i:
                   break
                if s[i-1]==t[j-1]:
                    cur[j] = pre[j]+pre[j-1]
                else:
                    cur[j] = pre[j]
            pre = cur[:]
        return cur[-1]

    def numDistinct4(self, s: str, t: str) -> int:
        """
        空间压缩2：用一个一维数组
        :param s:
        :param t:
        :return:
        """
        if len(t)>len(s):
            return 0

        cur = [0]*(len(t)+1)
        cur[0] = 1

        for i in range(1,len(s)+1):
            tmp1 = cur[0]
            for j in range(1,len(t)+1):
                if j>i:
                   break
                tmp2 = cur[j]
                if s[i-1]==t[j-1]:
                    cur[j] = tmp1+tmp2
                else:
                    cur[j] = tmp2
                tmp1 = tmp2
        return cur[-1]


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    sol = Solution()
    print(sol.numDistinct4(s,t))





