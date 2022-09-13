# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-05
    FileName   : combinationSum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 081. 允许重复选择元素的组合
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self.trace(candidates,target,res,path)
        return res


    def trace(self, candidates, target,res,path):
        if target==0:
            res.append(path[:])
            return
        if target<0 or not candidates:
            return

        self.trace(candidates[1:],target,res,path)
        path.append(candidates[0])
        self.trace(candidates,target-candidates[0],res,path)
        path.pop()

if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 5, 7]
    target = 8
    print(sol.combinationSum(candidates,target))