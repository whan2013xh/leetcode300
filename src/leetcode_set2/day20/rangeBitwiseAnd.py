# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-28
    FileName   : rangeBitwiseAnd.py
    Author     : Honghe
    Descreption: 201. 数字范围按位与
"""


class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0
        # 找到公共前缀
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift


if __name__ == '__main__':
    sol = Solution()
    left = 1
    right = 2147483647
    print(sol.rangeBitwiseAnd(left,right))
