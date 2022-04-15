# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-08
    FileName   : sumNums.py
    Author     : Honghe
    Descreption: 剑指 Offer 64. 求1+2+…+n
"""

class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res




if __name__ == '__main__':
    sol = Solution()
    n=10
    print(sol.sumNums(n))