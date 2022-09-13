# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-01
    FileName   : fib-0601.py
    Author     : Honghe
    Descreption: 
"""


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        first_pre = 0
        pre = 1
        res = 1
        for i in range(2,n+1):
            res = first_pre+pre
            first_pre = pre
            pre = res
        return res

if __name__ == '__main__':
    sol = Solution()
    n=5
    print(sol.fib(n))
