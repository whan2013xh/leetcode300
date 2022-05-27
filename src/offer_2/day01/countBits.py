# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-06
    FileName   : countBits.py
    Author     : Honghe
    Descreption: 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        if n>=0:
            res.append(0)
        if n>=1:
            res.append(1)
        tmp = []
        i = 2
        while i<=n:
            for j in res:
                if i<=n:
                    tmp.append(j+1)
                    i+=1
                else:
                    break
            res+=tmp
            tmp = []
        return res

if __name__ == '__main__':
    sol = Solution()
    n = 5
    print(sol.countBits(n))



