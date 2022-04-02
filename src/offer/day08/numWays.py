# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-30
    FileName   : numWays.py
    Author     : Honghe
    Descreption: 剑指 Offer 10- II. 青蛙跳台阶问题
"""

class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        if n<=2:
            return n
        dp = [0]*(n+1)
        for i in range(1,n+1):
            if i<=2:
                dp[i]=i
            else:
                dp[i] = (dp[i-1]+dp[i-2])%mod
        return dp[n]