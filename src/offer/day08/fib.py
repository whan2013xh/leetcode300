# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-30
    FileName   : fib.py
    Author     : Honghe
    Descreption: 
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
           return n
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=1
        mod = 10**9+7
        for i in range(2,n+1):
            dp[i] = (dp[i-1]+dp[i-2])%mod
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    n = 45
    print(sol.fib(n))
