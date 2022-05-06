# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-18
    FileName   : subsetsWithDup.py
    Author     : Honghe
    Descreption: 90. 子集 II
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.back_trace(nums,0,res,[])
        return res

    def back_trace(self,nums, begin, res, tmp):
        if len(tmp)<=len(nums):
            res.append(tmp[:])

        for index,num in enumerate(nums[begin:]):
            tmp.append(num)
            if not tmp in res:
                self.back_trace(nums, begin+index+1,res,tmp)
            tmp.pop()

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2]
    print(sol.subsetsWithDup(nums))


