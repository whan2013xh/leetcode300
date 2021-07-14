# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-13
    FileName   : permute.py
    Author     : Honghe
    Descreption: 46、全排列
"""
import copy

class Solution(object):
    def permute(self, nums):
        """
        回溯法
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = {}
        for i in nums:
            visited[i] = False
        result = []
        self.back_trace(nums, result, visited, [])
        return result

    def back_trace(self, nums, result, visited, choose_list):
        if len(choose_list)==len(nums):
            result.append(copy.deepcopy(choose_list))
            return

        for i in nums:
            if not visited.get(i):
                choose_list.append(i)
                visited[i] = True
                self.back_trace(nums, result, visited, choose_list)
                choose_list.remove(i)
                visited[i] = False

        return

if __name__ == '__main__':
    nums = [1,2,3]
    sol = Solution()
    res = sol.permute(nums)
    print(res)
