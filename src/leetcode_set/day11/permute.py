# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-21
    FileName   : permute.py
    Author     : Honghe
    Descreption: 46. 全排列
"""
import copy


class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums,res,[])
        return res

    def dfs(self, nums, res, tmp):
        if len(tmp)==len(nums):
            res.append(copy.deepcopy(tmp))

        for i in nums:
            if i in tmp:
                continue
            tmp.append(i)
            self.dfs(nums,res,tmp)
            tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))
