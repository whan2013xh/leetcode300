# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-30
    FileName   : twoSum-0530.py
    Author     : Honghe
    Descreption: 1. 两数之和
"""
from dis import dis

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}
        for index,num in enumerate(nums):
            if target-num not in count:
                tmp = count.get(num,[])
                tmp.append(index)
                count[num]=tmp
            else:
                return [count.get(target-num)[0],index]
        return []




if __name__ == '__main__':
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums,target))
