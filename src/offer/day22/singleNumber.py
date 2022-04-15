# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-12
    FileName   : singleNumber.py
    Author     : Honghe
    Descreption: 剑指 Offer 56 - II. 数组中数字出现的次数 II
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        统计二进制中1的个数，对3进行求余
        :type nums: List[int]
        :rtype: int
        """
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)



if __name__ == '__main__':
    sol = Solution()
    nums = [3,3,1,3]
    print(6&6)
    print(sol.singleNumber(nums))
