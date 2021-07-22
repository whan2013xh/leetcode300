# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021/7/22 21:31
    FileName   : subsetsWithDup.py
    Author     : xuhan
    Descreption: 
"""
import copy

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        暴力法：先对nums进行排序，然后再遍历每个元素，添加进入
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        nums.sort()
        for i in nums:
            res += [j+[i] for j in res if j+[i] not in res]
        return res

    def subsetsWithDup2(self, nums):
        """
        DFS:深度优先
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, res, 0, [])
        return res

    def dfs(self, nums, res, begin, tmp_list):
        if len(tmp_list)<=len(nums) and tmp_list not in res:
            res.append(copy.deepcopy(tmp_list))

        for i in range(begin, len(nums)):
            tmp_list.append(nums[i])
            self.dfs(nums, res, i+1, tmp_list)
            tmp_list.pop()

    def subsetsWithDup3(self, nums):
        """
        BFS:广度优先
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0, len(nums)+1):
            self.bfs(nums, res, 0, i, [])
        return res


    def bfs(self, nums, res, begin, length, tmp_list):
        if len(tmp_list)==length and tmp_list not in res:
            res.append(copy.deepcopy(tmp_list))

        for i in range(begin, len(nums)):
            tmp_list.append(nums[i])
            self.bfs(nums, res, i+1, length, tmp_list)
            tmp_list.pop()

if __name__ == '__main__':
    nums =  [1,2,2]
    sol = Solution()
    res = sol.subsetsWithDup3(nums)
    print(res)
