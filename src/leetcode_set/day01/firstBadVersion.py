# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-09
    FileName   : firstBadVersion.py
    Author     : Honghe
    Descreption: 278. 第一个错误的版本
"""

def isBadVersion(version):
    return version==1

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            middle = (right - left) // 2 + left
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

if __name__ == '__main__':
    sol = Solution()
    res = sol.firstBadVersion(3)
    print(res)