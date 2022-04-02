# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-02
    FileName   : climbStairs.py
    Author     : Honghe
    Descreption: 70. 爬楼梯
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        pre = 1
        cur = 2
        res = 0
        for i in range(2, n):
            res = pre+cur
            pre = cur
            cur = res
        return res

if __name__ == '__main__':
    sol = Solution()
    n =10
    print(sol.climbStairs(n))