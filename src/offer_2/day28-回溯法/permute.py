# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-06
    FileName   : permute.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        顺序法
        :param nums:
        :return:
        """
        res = [[]]
        for i in nums:
            tmp = []
            for j in res:
                for k in range(len(j)+1):
                    num = j[:]
                    num.insert(k,i)
                    tmp.append(num[:])
            res = tmp[:]
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        :param nums:
        :return:
        """
        res = []
        path = []
        visited = [False]*len(nums)
        self.back_track(nums,path,res,visited)
        return res


    def back_track(self,nums, path,res,visited):
        if len(path)==len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            path.append(nums[i])
            self.back_track(nums,path,res,visited)
            path.pop()
            visited[i] = False

if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,3]
    print(sol.permute2(nums))