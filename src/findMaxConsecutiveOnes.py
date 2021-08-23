# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-23
    FileName   : findMaxConsecutiveOnes.py
    Author     : Honghe
    Descreption: 485. 最大连续 1 的个数
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        直接遍历
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for index, i in enumerate(nums):
            if i==0:
                res = max(res, count)
                count=0
            else:
                count+=1
        return max(res,count)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,0,1,1,1]
    res = sol.findMaxConsecutiveOnes(nums)
    print(res)

