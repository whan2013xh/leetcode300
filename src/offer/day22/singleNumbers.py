# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-12
    FileName   : singleNumbers.py
    Author     : Honghe
    Descreption: 
"""
import functools

class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i=0
        res = []
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                res.append(nums[i])
                if len(res)==2:
                    return res
                i+=1
            else:
                i+=2
        res.append(nums[-1])
        return res

    def singleNumbers2(self, nums):
        """
        位运算
        :param nums:
        :return:
        """
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == '__main__':
    sol = Solution()
    nums = [4,1,4,2]
    print(sol.singleNumbers(nums))
