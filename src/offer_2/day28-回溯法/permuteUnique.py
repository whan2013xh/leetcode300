# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-06
    FileName   : permuteUnique.py
    Author     : Honghe
    Descreption: 
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in nums:
            visited = {}
            tmp = []
            for j in res:
                for k in range(len(j) + 1):
                    num = j[:]
                    num.insert(k, i)
                    if tuple(num) not in visited:
                        visited[tuple(num)] = 0
                        tmp.append(num[:])
            res = tmp[:]
        return res

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        :param nums:
        :return:
        """
        res = []
        path = []
        visited = [False] * len(nums)
        nums.sort()
        self.back_track(nums, path, res, visited)
        return res

    def back_track(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i] or (i>0 and nums[i]==nums[i-1] and not visited[i-1]):
                continue
            visited[i] = True
            path.append(nums[i])
            self.back_track(nums, path, res, visited)
            path.pop()
            visited[i] = False


if __name__ == '__main__':
    sol = Solution()
    nums = [2,2,1,1]
    print(sol.permuteUnique2(nums))
