# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-18
    FileName   : subsets.py
    Author     : Honghe
    Descreption: 78. 子集
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.get_sets(nums,0,res,[])
        return res


    def get_sets(self,nums,begin,res,tmp):
        if len(tmp)<=len(nums):
            res.append(tmp[:])

        for index,num in enumerate(nums[begin:]):
            tmp.append(num)
            self.get_sets(nums,begin+index+1,res,tmp)
            tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.subsets(nums))
