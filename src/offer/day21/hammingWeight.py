# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-12
    FileName   : hammingWeight.py
    Author     : Honghe
    Descreption: 剑指 Offer 15. 二进制中1的个数
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n//(2**i)>0:
            i+=1
        res = 0
        for j in range(i-1,-1,-1):
            if n>=2**j:
                n = n-2**j
            else:
                continue
            res+=1
            if n==0:
                break

        return res

if __name__ == '__main__':
    sol = Solution()
    n=11
    print(sol.hammingWeight(n))