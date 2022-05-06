# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-19
    FileName   : permuteUnique.py
    Author     : Honghe
    Descreption: 47. 全排列 II
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # for index,num in enumerate(nums):
        self.back_trace(nums,[],res,[])
        return res


    def back_trace(self, nums, begin,res,tmp):
        if len(tmp)==len(nums) and tmp not in res:
            res.append(tmp[:])
            tmp = []

        for index,num in enumerate(nums):
            if index not in begin:
                tmp.append(num)
                begin.append(index)
                self.back_trace(nums,begin,res,tmp)
                tmp.pop()
                begin.pop()

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,2,3]
    print(sol.permuteUnique(nums))


