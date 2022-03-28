# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-28
    FileName   : hasAlternatingBits-0328.py
    Author     : Honghe
    Descreption: 693. 交替位二进制数
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=1
        pre = n%(2**num)
        while 2**num<=n:
           cur = (n//(2**num))%2
           if not pre ^ cur:
               return False
           pre = cur
           num+=1
        return True

if __name__ == '__main__':
    sol = Solution()
    n=5
    print(sol.hasAlternatingBits(n))

