# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-06
    FileName   : partition.py
    Author     : Honghe
    Descreption: 剑指 Offer II 086. 分割回文子字符串
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        primes = {}
        for i in range(len(s)):
            tmp = []
            for j in range(i+1,len(s)+1):
                flag = self.is_prime(s[i:j])
                if flag:
                    tmp.append(j)
            primes[i]=tmp

        visited = [False]*len(s)
        res = []
        path = []
        self.back_track(s,primes,path,res,visited,0)
        return res

    def back_track(self, s,primes,path,res,visited,i):
        if i==len(s):
            res.append(path[:])
            return

        if visited[i]:
            return

        for j in primes[i]:
            for k in range(i,j):
                visited[k]=True
            path.append(s[i:j])
            self.back_track(s,primes,path,res,visited,j)
            path.pop()
            for k in range(i,j):
                visited[k]=False

    def is_prime(self,s):
        return s==s[::-1]

    def partition2(self, s: str) -> List[List[str]]:
        """
        动态规划+回溯法
        :param s:
        :return:
        """
        length = len(s)
        dp = [[True]*len(s) for _ in range(len(s))]
        res = []
        path = []
        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
        self.dfs(s,0,res,path,dp)
        return res

    def dfs(self, s,index,res,path,dp):
        if index==len(s):
            res.append(path[:])
            return

        for i in range(index,len(s)):
            if dp[index][i]:
                path.append(s[index:i+1])
                self.dfs(s,i+1,res,path,dp)
                path.pop()





if __name__ == '__main__':
    sol = Solution()
    s = "google"
    print(sol.partition2(s))
