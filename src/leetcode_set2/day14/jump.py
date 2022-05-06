# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-21
    FileName   : jump.py
    Author     : Honghe
    Descreption: 45. 跳跃游戏 II
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next_num = 0
        step = 0
        max_path = 0
        for index,num in enumerate(nums):
            max_path = max(max_path,num+index)
            if max_path>=len(nums)-1:
                return step+1
            if index==next_num:
                next_num = max_path
                step+=1


if __name__ == '__main__':
    sol = Solution()
    nums=[2]
    print(sol.jump(nums))