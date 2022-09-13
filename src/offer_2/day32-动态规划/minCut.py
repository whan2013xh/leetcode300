# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-11
    FileName   : minCut.py
    Author     : Honghe
    Descreption: 
"""


class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        dp = [[True]*length for _ in range(length)]
        costs = [i for i in range(length)]

        for i in range(1,length):
            for j in range(i-1,-1,-1):
                dp[i][j] = s[i]==s[j] and dp[i-1][j+1]

        for i in range(1,length):
            tmp = []
            for index, val in enumerate(dp[i]):
                if index>i:
                    break
                if val:
                    if index==0:
                        tmp.append(-1)
                    else:
                        tmp.append(costs[index-1])
            costs[i] = min(tmp)+1 if len(tmp)>1 else costs[i-1]+1
        return costs[-1]

    def minCut2(self, s: str) -> int:
        length = len(s)
        dp = [[True]*length for _ in range(length)]

        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                dp[i][j] = s[i]==s[j] and dp[i+1][j-1]

        costs = [max(i-1,0) for i in range(length)]
        for i in range(1,length):
            if dp[0][i]:
                costs[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        costs[i] = min(costs[i],costs[j]+1)
        return costs[-1]



if __name__ == '__main__':
    sol = Solution()
    s = "aa"
    print(sol.minCut(s))