# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-07
    FileName   : restoreIpAddresses.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4 or len(s)>12:
            return []

        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i,i+3):
                if i==j:
                    dp[i][j] = True
                    continue
                if j>=len(s) or s[i]=='0':
                    break
                dp[i][j] = int(s[i:j+1])<=255
        res = []
        path = []
        self.dfs(s,res,path,dp,0)
        return res

    def dfs(self,s,res,path,dp,index):
        if len(path)>4:
            return
        if index==len(s) and len(path)==4:
            res.append(".".join(path))
            return

        for i in range(index,len(s)):
            if dp[index][i]:
                path.append(s[index:i+1])
                self.dfs(s,res,path,dp,i+1)
                path.pop()
            else:
                break


if __name__ == '__main__':
    sol = Solution()
    s = "010010"
    print(sol.restoreIpAddresses(s))


