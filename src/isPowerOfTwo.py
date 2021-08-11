# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-11
    FileName   : isPowerOfTwo.py
    Author     : Honghe
    Descreption: 231. 2 的幂
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        位运算法：如果n是2的幂，则n&(n-1)=0
        因为n相对于n-1来说进了一位
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return n&(n-1)==0

    def isPowerOfTwo1(self, n):
        """
        位运算法：2的幂对应的二进制只有一个1
        因为n相对于n-1来说进了一位
        :type n: int
        :rtype: bool
        """
        return n>0 and bin(n).count('1') == 1


    def isPowerOfTwo2(self, n):
        """
        二分法
        :param n:
        :return:
        """
        if n<=0:
            return False
        start = 0
        end = n

        while start<=end:
            mid = (end - start) // 2 + start
            res = pow(2, mid)
            if res==n:
                return True
            elif res>n:
                end = mid-1
            else:
                start = mid+1
        return False


if __name__ == '__main__':
    n = 3
    sol = Solution()
    res = sol.isPowerOfTwo2(n)
    print(res)