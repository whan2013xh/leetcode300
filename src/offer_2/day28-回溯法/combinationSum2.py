# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-05
    FileName   : combinationSum2.py
    Author     : Honghe
    Descreption: 剑指 Offer II 082. 含有重复元素集合的组合
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        visited = {}
        if sum(candidates)<target:
            return []
        self.trace(candidates,target,res,path,visited)
        return res


    def trace(self,nums, target, res,path,visited):
        if not nums and target!=0:
            return
        if target==0:
            if tuple(path) not in visited:
                visited[tuple(path)] = 0
                res.append(path[:])
            return

        if nums and target<nums[0]:
            return

        self.trace(nums[1:],target,res,path,visited)
        path.append(nums[0])
        self.trace(nums[1:],target-nums[0],res,path,visited)
        path.pop()

if __name__ == '__main__':
    sol = Solution()
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 5
    print(sol.combinationSum2(candidates,target))