# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-07
    FileName   : singleNumber.py
    Author     : Honghe
    Descreption: 剑指 Offer II 004. 只出现一次的数字
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        位运算
        :type nums: List[int]
        :rtype: int
        """
        # 统计32位中每位1的个数
        count = [0]*32
        for num in nums:
            for j in range(32):
                count[j] += num&1
                num>>=1

        res = 0
        # 统计不能被3整除的位置，求和,考虑负数
        for index,num in enumerate(count):
            if num%3>0:
                res+=2**index
        return res if count[31] % 3 == 0 else ~(res ^ 0xffffffff)

if __name__ == '__main__':
    sol = Solution()
    nums = [-2,-2,1,1,4,1,4,4,-4,-2]
    print(sol.singleNumber(nums))


