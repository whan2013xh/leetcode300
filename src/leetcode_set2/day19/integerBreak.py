# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-28
    FileName   : integerBreak.py
    Author     : Honghe
    Descreption: 
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(i):
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j])
        return dp[-1]

    def integerBreak2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n-1
        p = n//3
        q = n%3
        if q==0:
            return 3**p
        elif q==1:
            return 3**(p-1)*4
        else:
            return 3 ** p * 2
