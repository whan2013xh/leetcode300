# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-01
    FileName   : mySqrt.py
    Author     : Honghe
    Descreption: 
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0
        while left<=right:
            mid = (right-left)//2+left
            if mid*mid<=x:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res


if __name__ == '__main__':
    sol = Solution()
    x = 10
    print(sol.mySqrt(x))

