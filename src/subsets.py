# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-21
    FileName   : subsets.py
    Author     : Honghe
    Descreption: 78. 子集
"""
import copy

class Solution(object):
    def subsets(self, nums):
        """
        暴力法：就是按照遍历顺序每次添加一个元素进行扩展。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        for i in nums:
            tmp = copy.deepcopy(res)
            for num in tmp:
                num.append(i)
                res.append(num)
        return res

    def subsets2(self, nums):
        """
        深度优先遍历：
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, begin, res, tmp_list):
        if len(tmp_list)<=len(nums):
            res.append(copy.deepcopy(tmp_list))

        for index in range(begin,len(nums)):
            tmp_list.append(nums[index])
            self.dfs(nums, index+1, res, tmp_list)
            tmp_list.pop()

    def subsets3(self, nums):
        """
        回溯法：
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        for i in range(1, len(nums)+1):
            self.back_trace(nums, res, 0, [], i)
        return res

    def back_trace(self, nums, res, begin, tmp_list, target):
        if len(tmp_list)==target:
            res.append(copy.deepcopy(tmp_list))
            return

        for index in range(begin, len(nums)):
            tmp_list.append(nums[index])
            self.back_trace(nums, res, index+1, tmp_list, target)
            tmp_list.pop()





if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    res = sol.subsets3(nums)
    print(res)
